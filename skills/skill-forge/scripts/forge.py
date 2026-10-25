#!/usr/bin/env python3
"""Small, dependency-free Skill Forge file, session, and release helpers.

Evidence is supplied by an evaluator. This tool checks bindings and adoption
rules; it cannot authenticate that a reported model execution really occurred.
"""

import argparse
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
import uuid
import zipfile

VERSION = "0.3.0"
SCHEMA = 1
MARKER = ".skill-forge-managed.json"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}
PRIVATE_PARTS = {".env", ".state", ".private", "private", "sessions", "transcripts", "credentials", "node_modules", ".venv"}
SECRET_RE = re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{24,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)")


class ForgeError(Exception):
    pass


def require(condition, message):
    if not condition:
        raise ForgeError(message)


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        raise ForgeError("Cannot read JSON {}: {}".format(path, exc)) from exc


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    write_text(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def write_text(path, text):
    """Use UTF-8 and literal LF bytes on every OS, including Python 3.9."""
    Path(path).write_bytes(text.replace("\r\n", "\n").encode("utf-8"))


def is_link(path):
    """Reject symlinks and Windows reparse points (including junctions)."""
    try:
        info = Path(path).lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    )


def digest(data):
    return hashlib.sha256(data).hexdigest()


def file_hash(path):
    return digest(Path(path).read_bytes())


def within(path, parent):
    try:
        Path(path).resolve().relative_to(Path(parent).resolve())
        return True
    except ValueError:
        return False


def files(root):
    """Reject symlinks/reparse points before reading an inspected tree."""
    root = Path(root)
    require(root.is_dir() and not is_link(root), "Expected a real directory, not a symlink/reparse point: {}".format(root))
    result = []
    for directory, dirs, names in os.walk(str(root), followlinks=False):
        base = Path(directory)
        for name in list(dirs):
            require(not is_link(base / name), "Symlink/reparse point is not supported: {}".format(base / name))
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(names):
            path = base / name
            require(not is_link(path), "Symlink/reparse point is not supported: {}".format(path))
            require(path.is_file(), "Not a regular file: {}".format(path))
            if name != MARKER and not name.endswith((".pyc", ".pyo")):
                result.append(path)
    return sorted(result, key=lambda p: p.relative_to(root).as_posix())


def tree_hash(root):
    root = Path(root)
    inventory = [[p.relative_to(root).as_posix(), file_hash(p)] for p in files(root)]
    return digest(json.dumps(inventory, separators=(",", ":")).encode())


def copy_tree(source, dest):
    source, dest = Path(source), Path(dest)
    require(not dest.exists(), "Destination already exists: {}".format(dest))
    inventory = files(source)
    dest.mkdir(parents=True)
    for path in inventory:
        target = dest / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(path), str(target))


def private_root(path, target=None):
    path = Path(path).expanduser()
    require(not is_link(path), "Private state root cannot be a symlink/reparse point")
    path = path.resolve()
    for ancestor in [path] + list(path.parents):
        if (ancestor / ".git").exists() or ((ancestor / "skills").is_dir() and (ancestor / "LICENSE").exists()):
            raise ForgeError("Private state must be outside the publishable repository")
    if target is not None:
        target = Path(target).resolve()
        require(not within(path, target) and not within(target, path), "Private state and target must be separate directory trees")
        for ancestor in [target] + list(target.parents):
            if (ancestor / ".git").exists() or ((ancestor / "skills").is_dir() and (ancestor / "LICENSE").exists()):
                require(not within(path, ancestor), "Private state must be outside the publishable repository")
                break
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    # Windows mode bits do not set ACLs. The directory inherits its parent's
    # permissions; keep it under the user's profile and inspect sensitive data ACLs.
    if os.name == "posix":
        os.chmod(str(path), 0o700)
    ignore = path / ".gitignore"
    if not ignore.exists():
        write_text(ignore, "*\n!.gitignore\n")
    return path


def metadata(text):
    require(text.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    parts = text.split("\n---", 1)
    require(len(parts) == 2, "SKILL.md frontmatter needs a closing ---")
    head = parts[0][4:]
    values = {}
    for key in ("name", "description"):
        match = re.search(r"^" + key + r":\s*(.+)$", head, re.M)
        require(match is not None, "Frontmatter requires {}".format(key))
        value = match.group(1).strip()
        if value in ("|", ">", "|-", ">-"):
            tail = head[match.end():]
            lines = []
            for line in tail.splitlines():
                if line and not line[0].isspace():
                    break
                if line.strip():
                    lines.append(line.strip())
            value = " ".join(lines)
        else:
            value = value.strip("\"'")
        require(bool(value), "Empty frontmatter {}".format(key))
        values[key] = value
    name = values["name"]
    require(len(name) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name), "name must be <=64 lowercase letters, numbers, and single hyphens")
    require(len(values["description"]) <= 1024, "description must be <=1024 characters")
    return values


def validate(skill):
    require(not is_link(skill), "Skill root cannot be a symlink/reparse point")
    skill = Path(skill).resolve()
    inventory = files(skill)
    require((skill / "SKILL.md").is_file(), "Missing SKILL.md")
    meta = metadata((skill / "SKILL.md").read_text(encoding="utf-8"))
    require(meta["name"] == skill.name, "Frontmatter name must match skill directory name")
    checked = 0
    for path in inventory:
        if path.suffix != ".md":
            continue
        content = path.read_text(encoding="utf-8")
        # Ignore fenced examples, then inspect Markdown links and literal resource paths.
        content = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", content, flags=re.M | re.S)
        links = [(raw, path.parent) for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content)]
        links += [(raw, skill) for raw in re.findall(r"`((?:references|templates|questions|scripts|assets)/[^`\s]+)`", content)]
        for raw, origin in links:
            link = raw.strip().split(' "', 1)[0].strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", link) or link.startswith("#"):
                continue
            link = link.split("#", 1)[0].split("?", 1)[0]
            if not link or any(token in link for token in ("*", "{", "}")):
                continue
            require(not link.startswith("/"), "Absolute local link in {}: {}".format(path.name, link))
            target = origin / link
            require(within(target, skill), "Relative link escapes skill package: {}".format(link))
            require(target.exists(), "Missing relative link in {}: {}".format(path.relative_to(skill), link))
            checked += 1
    question_file = skill / "questions" / "questions.json"
    question_count = 0
    if question_file.exists():
        questions = question_entries(read_json(question_file))
        seen = set()
        for q in questions:
            require(isinstance(q, dict) and q.get("id") and q.get("question"), "Every question needs id and question")
            require(q["id"] not in seen, "Duplicate question id: {}".format(q["id"]))
            seen.add(q["id"])
            require(q.get("status") in ("candidate", "accepted", "revised", "retired"), "Unknown question status")
            for field in ("purpose", "ask_when", "dependencies", "affects", "evidence", "skip_when"):
                require(field in q, "Question {} lacks {}".format(q["id"], field))
        question_count = len(questions)
    return {"status": "pass", "name": meta["name"], "files": len(inventory), "relative_links": checked, "questions": question_count, "limitations": "Checks supported frontmatter fields and file links, not full YAML or semantic quality."}


def question_entries(data):
    entries = data.get("questions") if isinstance(data, dict) else data
    require(isinstance(entries, list), "questions.json must be an array or an object containing questions")
    return entries


def search_questions(skill, query, status=None):
    entries = question_entries(read_json(Path(skill) / "questions" / "questions.json"))
    words = query.casefold().split()
    matches = []
    for item in entries:
        if status and item.get("status") != status:
            continue
        haystack = json.dumps(item, ensure_ascii=False).casefold()
        score = sum(haystack.count(word) for word in words)
        if not words or all(word in haystack for word in words):
            matches.append((score, item))
    return [item for _, item in sorted(matches, key=lambda pair: (-pair[0], pair[1]["id"]))]


def portable_text(skill):
    skill = Path(skill).resolve()
    validate(skill)
    sections = []
    sources = [skill / "SKILL.md"]
    for folder in ("references", "templates", "questions", "subskills"):
        if (skill / folder).exists():
            sources.extend(p for p in files(skill / folder) if p.suffix in (".md", ".json", ".txt") or p.name in ("LICENSE", "NOTICE"))
    sources.extend(skill / name for name in ("LICENSE", "THIRD_PARTY_NOTICES.md") if (skill / name).is_file())
    source_names = {p.resolve(): p.relative_to(skill).as_posix() for p in sources}
    def anchor(name):
        return "resource-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    for path in sources:
        rel = path.relative_to(skill).as_posix()
        body = path.read_text(encoding="utf-8").rstrip()
        def inline_link(match):
            label, link = match.group(1), match.group(2)
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", link) or link.startswith("#"):
                return match.group(0)
            linked = (path.parent / link.split("#", 1)[0]).resolve()
            if linked in source_names:
                return "[{}](#{})".format(label, anchor(source_names[linked]))
            return "{} (full skill package: `{}`)".format(label, link)
        body = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", inline_link, body)
        sections.append('<a id="{}"></a>\n\n## Included resource: {}\n\n{}'.format(anchor(rel), rel, body))
    source_digest = digest("\n\n".join(sections).encode())
    header = """# Skill Forge — portable prompt bundle

Use the instructions and included resources below as a reusable skill-building
workflow. Resource paths refer to sections in this document. Tools are optional:
when unavailable, ask the user to supply relevant source text, provide complete
file contents they can save, and return a compact resume record. Never claim to
have browsed, executed tests, saved files, installed, or published without doing so.
Without executable checks, retain behavior changes as unverified candidates.
Executable helpers are optional and are distributed with the full skill package;
their references below describe capabilities, not tools available in plain chat.

Generated from canonical instructions and all reference, template, question,
and bundled sub-skill resources. Edit those sources and regenerate this file; do not edit this bundle.

Source SHA-256: `{}`

""".format(source_digest)
    return header + "\n\n".join(sections) + "\n"


def session_init(state, name):
    root = private_root(state)
    safe = re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-") or "session"
    folder = root / (safe + "-" + uuid.uuid4().hex[:8])
    folder.mkdir(mode=0o700)
    record = {"schema_version": SCHEMA, "id": folder.name, "created": now(), "workflow": None, "confirmed": [], "defaults": [], "assumptions": [], "examples": [], "acceptance": [], "unresolved": [], "next_step": "Read supplied context and resolve the most consequential uncertainty.", "private_personalization": {}, "round_limit": 3}
    record.update({
        "skill_delivery": {"format": None, "destination": None, "publication_authorized": False,
                           "owner": None, "repository": None, "visibility": None},
        "domain_output_contract": {},
        "refinement_status": {"open_material_decisions": [], "next_question": None, "ready_to_build": False},
        "skill_finder": {"status": "not-started", "brief_fingerprint": None, "report": None, "skip_reason": None},
        "source_context": {"kind": "idea", "scope": None, "accessible_sources": [],
                           "coverage_limits": [], "superseded_decisions": []},
        "implementation_spec": {"status": "not-started", "path": None, "revision": None,
                                "review_pause_requested": False, "review_state": "not-requested",
                                "user_corrections": []},
        "delegation": {"available": None, "effort_limit": None, "tasks": [], "skip_reason": None},
        "verification_plan": {"cases": [], "baseline": None, "evaluator": None, "unavailable_checks": []},
        "effort_limit": {"wall_clock_minutes": 30, "max_candidates": 3}
    })
    write_json(folder / "session.json", record)
    return {"session": str(folder / "session.json"), "privacy": "State is outside publishable source; do not add it to releases. POSIX directories use owner-only modes; Windows inherits parent ACLs, so use a user-owned location and inspect permissions for sensitive data."}


def check_criteria(criteria):
    require(isinstance(criteria, dict), "Criteria must be an object")
    require(criteria.get("schema_version") == SCHEMA, "Unsupported criteria schema")
    require(criteria.get("scope") in ("target", "builder"), "criteria.scope must be target or builder")
    require(criteria.get("change_kind") in ("behavior", "structural"), "Unknown change_kind")
    require(criteria.get("evaluation_kind") in ("model_execution", "script_execution"), "A real model_execution or script_execution is required")
    checks = criteria.get("checks", [])
    require(isinstance(checks, list) and checks, "Define checks before preparing a candidate")
    ids, kinds = set(), set()
    for case in checks:
        require(isinstance(case, dict), "Each check must be an object")
        require(isinstance(case.get("id"), str) and case["id"] not in ids, "Checks need unique string ids")
        ids.add(case["id"])
        kinds.add(case.get("kind"))
        for field in ("input", "expected", "failure"):
            require(isinstance(case.get(field), str) and case[field].strip(), "Each check needs concrete {}".format(field))
    require(kinds <= {"acceptance", "regression", "held_out"}, "Unknown check kind")
    require({"acceptance", "regression"} <= kinds, "Acceptance and regression cases are required")
    if criteria["scope"] == "builder" and criteria["change_kind"] == "behavior":
        require("held_out" in kinds, "Builder behavior updates require a held-out case")
    benefit = criteria.get("benefit", {})
    require(isinstance(benefit, dict), "Criteria benefit must be an object")
    require(isinstance(benefit.get("metric"), str) and benefit["metric"], "Define a benefit metric")
    require(benefit.get("direction") in ("higher", "lower"), "Benefit direction must be higher or lower")
    require(type(benefit.get("min_delta")) in (float, int) and math.isfinite(benefit["min_delta"]) and benefit["min_delta"] > 0, "Benefit min_delta must be finite and positive")


def prepare(target, state, criteria_path, evaluator_path, effort_minutes, max_rounds=3):
    target = Path(target).resolve()
    require(target.is_dir(), "Target directory does not exist")
    require(1 <= max_rounds <= 3, "Use between one and three candidate rounds")
    require(0 < effort_minutes <= 1440, "State a positive effort limit of at most 1440 minutes")
    criteria = read_json(criteria_path)
    check_criteria(criteria)
    evaluator = Path(evaluator_path).resolve()
    require(evaluator.is_file() and not is_link(evaluator) and evaluator.stat().st_size > 0, "Supply a nonempty fixed evaluator file")
    require(not within(evaluator, target), "Evaluator must be outside the candidate-controlled target")
    require(not within(Path(criteria_path), target), "Criteria must be outside the candidate-controlled target")
    state = private_root(state, target)
    run = state / ("run-" + uuid.uuid4().hex[:12])
    run.mkdir(mode=0o700)
    copy_tree(target, run / "baseline")
    shutil.copy2(str(criteria_path), str(run / "criteria.json"))
    shutil.copy2(str(evaluator), str(run / "evaluator"))
    manifest = {"schema_version": SCHEMA, "target": str(target), "created": now(), "effort_minutes": effort_minutes, "max_rounds": max_rounds, "rounds": 0, "status": "prepared", "baseline_hash": tree_hash(target), "criteria_hash": file_hash(run / "criteria.json"), "evaluator_hash": file_hash(run / "evaluator"), "adopted_hash": None}
    write_json(run / "run.json", manifest)
    return dict(manifest, run=str(run), next_step="Build candidate separately; run the fixed evaluator against baseline and candidate; submit hash-bound evidence.")


def verify_frozen(run, manifest):
    require(file_hash(run / "criteria.json") == manifest["criteria_hash"], "Frozen criteria changed")
    require(file_hash(run / "evaluator") == manifest["evaluator_hash"], "Frozen evaluator changed")
    require(tree_hash(run / "baseline") == manifest["baseline_hash"], "Baseline snapshot changed")


def evidence_check(evidence, criteria, manifest, candidate_hash, evidence_dir, artifacts):
    require(isinstance(evidence, dict), "Evidence must be an object")
    require(evidence.get("schema_version") == SCHEMA, "Unsupported evidence schema")
    for key, expected in (("baseline_hash", manifest["baseline_hash"]), ("candidate_hash", candidate_hash), ("criteria_hash", manifest["criteria_hash"]), ("evaluator_hash", manifest["evaluator_hash"])):
        require(evidence.get(key) == expected, "Evidence {} does not match evaluated files".format(key))
    execution = evidence.get("execution", {})
    require(isinstance(execution, dict), "Execution must be an object")
    require(execution.get("kind") == criteria["evaluation_kind"], "Evidence must use the predefined real execution kind")
    for field in ("model", "host", "conditions"):
        require(isinstance(execution.get(field), str) and execution[field].strip(), "Execution must record {} (use not-applicable for scripts)".format(field))
    if criteria["change_kind"] == "behavior":
        require(execution.get("coverage") == "behavior", "Formatting-only checks cannot authorize behavior changes")
    results = evidence.get("results", [])
    require(isinstance(results, list), "Evidence results must be an array")
    require(all(isinstance(result, dict) for result in results), "Every result must be an object")
    expected_ids = {case["id"] for case in criteria["checks"]}
    require(len(results) == len(expected_ids) and {r.get("id") for r in results} == expected_ids, "Evidence must cover every frozen check exactly once")
    for result in results:
        require(result.get("candidate") == "pass", "Candidate failed or was inconclusive: {}".format(result.get("id")))
        require(result.get("baseline") in ("pass", "fail"), "Baseline outcome must be observed, not unknown")
        require(isinstance(result.get("artifact"), str), "Each result needs a reviewable execution artifact")
        artifact = evidence_dir / result["artifact"]
        require(not Path(result["artifact"]).is_absolute() and within(artifact, evidence_dir), "Evidence artifact must be relative and inside the evidence directory")
        require(artifact.is_file() and not is_link(artifact) and artifact.stat().st_size > 0, "Missing nonempty execution artifact")
        dest = artifacts / (digest(result["artifact"].encode())[:12] + "-" + artifact.name)
        shutil.copy2(str(artifact), str(dest))
    benefit, expected = evidence.get("benefit", {}), criteria["benefit"]
    require(isinstance(benefit, dict), "Evidence benefit must be an object")
    require(benefit.get("metric") == expected["metric"], "Benefit metric differs from frozen criteria")
    for key in ("baseline", "candidate"):
        value = benefit.get(key)
        require(type(value) in (int, float) and math.isfinite(value), "Benefit values must be finite observed numbers")
    delta = benefit["candidate"] - benefit["baseline"]
    if expected["direction"] == "lower":
        delta = -delta
    require(delta >= expected["min_delta"], "Candidate did not demonstrate the predefined benefit")
    return delta


def replace_tree(target, source):
    """Stage on the target filesystem and restore old contents on move failure."""
    target, source = Path(target), Path(source)
    temporary = Path(tempfile.mkdtemp(prefix=".forge-stage-", dir=str(target.parent)))
    stage, old = temporary / target.name, temporary / "previous"
    preserve_recovery = False
    try:
        copy_tree(source, stage)
        # A managed copy remains managed; changing its content deliberately means
        # a later upstream update must detect the customization.
        if (target / MARKER).exists():
            shutil.copy2(str(target / MARKER), str(stage / MARKER))
        os.replace(str(target), str(old))
        try:
            os.replace(str(stage), str(target))
        except BaseException as move_error:
            try:
                os.replace(str(old), str(target))
            except BaseException as restore_error:
                preserve_recovery = True
                raise ForgeError(
                    "Replacement and restoration failed; prior version is preserved at {}. "
                    "Restore it before continuing. Move error: {}; restore error: {}".format(
                        old, move_error, restore_error
                    )
                ) from restore_error
            raise
    finally:
        if not preserve_recovery:
            shutil.rmtree(str(temporary), ignore_errors=True)


def submit(run, candidate, evidence_path):
    run, candidate = Path(run).resolve(), Path(candidate).resolve()
    manifest = read_json(run / "run.json")
    require(manifest["status"] not in ("adopted", "rolled_back"), "Prepare a new run after adoption or rollback")
    target = Path(manifest["target"])
    require(candidate != target and not within(candidate, target) and not within(target, candidate), "Build the candidate separately from the active target")
    require(not within(run, candidate), "Candidate cannot contain its own private run")
    require(manifest["rounds"] < manifest["max_rounds"], "Candidate round limit reached; unresolved work remains saved")
    elapsed = (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(manifest["created"])).total_seconds() / 60
    require(elapsed <= manifest["effort_minutes"], "Effort/time limit reached; prepare a new authorized run")
    verify_frozen(run, manifest)
    require(tree_hash(target) == manifest["baseline_hash"], "Active target changed since snapshot; preserve customization and prepare again")
    round_id = manifest["rounds"] + 1
    attempt = run / "candidates" / ("{:02d}".format(round_id))
    copy_tree(candidate, attempt / "skill")
    candidate_hash = tree_hash(attempt / "skill")
    manifest["rounds"] = round_id
    write_json(run / "run.json", manifest)
    evidence_path = Path(evidence_path).resolve()
    record = {"round": round_id, "time": now(), "candidate_hash": candidate_hash, "status": "rejected", "reason": None}
    try:
        evidence = read_json(evidence_path)
        write_json(attempt / "evidence.json", evidence)
        artifacts = attempt / "artifacts"
        artifacts.mkdir()
        criteria = read_json(run / "criteria.json")
        check_criteria(criteria)
        delta = evidence_check(evidence, criteria, manifest, candidate_hash, evidence_path.parent, artifacts)
        # A snapshot folder has a different name; validate a temporary sibling
        # carrying the canonical directory name before adoption.
        with tempfile.TemporaryDirectory(prefix="forge-validate-") as temp:
            validation_copy = Path(temp) / target.name
            copy_tree(attempt / "skill", validation_copy)
            validation = validate(validation_copy)
        require(candidate_hash != manifest["baseline_hash"], "Candidate is unchanged")
        require(tree_hash(target) == manifest["baseline_hash"], "Active target changed during evaluation")
        verify_frozen(run, manifest)
        replace_tree(target, attempt / "skill")
        record.update(status="adopted", reason="All frozen checks passed and predefined benefit was demonstrated", benefit_delta=delta, validation=validation)
        manifest.update(status="adopted", adopted_hash=candidate_hash, adopted_at=now())
    except (ForgeError, OSError, ValueError, TypeError, KeyError) as exc:
        record["reason"] = str(exc)
        manifest["status"] = "candidate_rejected"
    write_json(attempt / "result.json", record)
    write_json(run / "run.json", manifest)
    record["run"] = str(run)
    record["candidate_preserved"] = str(attempt / "skill")
    record["evidence_limit"] = "Supplied execution records were checked; authenticity and evaluator quality require independent review."
    return record


def rollback(run):
    run = Path(run).resolve()
    manifest = read_json(run / "run.json")
    require(manifest["status"] == "adopted", "Run has no active adopted update to roll back")
    verify_frozen(run, manifest)
    target = Path(manifest["target"])
    require(tree_hash(target) == manifest["adopted_hash"], "Active files diverged after adoption; refusing to overwrite later changes")
    replace_tree(target, run / "baseline")
    manifest.update(status="rolled_back", rolled_back_at=now())
    write_json(run / "run.json", manifest)
    return {"status": "rolled_back", "target": str(target), "restored_hash": tree_hash(target)}


def install(source, dest, update=False):
    require(not is_link(source) and not is_link(Path(dest).expanduser()), "Install source/destination cannot be a symlink/reparse point")
    source, dest = Path(source).resolve(), Path(dest).expanduser().resolve()
    validate(source)
    require(dest.name == source.name, "Install destination must end with the skill name")
    require(not within(dest, source) and not within(source, dest), "Source and install destination must be separate trees")
    source_hash = tree_hash(source)
    if dest.exists():
        require(update, "Destination exists; use --update only for a managed copy")
        marker = read_json(dest / MARKER)
        require(tree_hash(dest) == marker.get("installed_hash"), "Managed copy has local customizations; refusing to overwrite. Merge in a separate candidate first.")
        replace_tree(dest, source)
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        copy_tree(source, dest)
    write_json(dest / MARKER, {"schema_version": SCHEMA, "source": str(source), "installed_hash": source_hash, "updated": now()})
    return {"status": "updated" if update else "installed", "destination": str(dest), "installed_hash": source_hash}


def check_public_file(path, rel):
    require(not (set(rel.parts) & (PRIVATE_PARTS | SKIP_DIRS)), "Private or generated directory cannot be packaged: {}".format(rel))
    require(not any(part.startswith(".env") or part.startswith("run-") or part.startswith("session-") for part in rel.parts), "Private state cannot be packaged: {}".format(rel))
    require(path.suffix.lower() not in (".pem", ".key", ".p12", ".pyc", ".pyo"), "Private/generated file cannot be packaged: {}".format(rel))
    require(not is_link(path) and path.is_file(), "Package entries must be regular files, not symlinks/reparse points")
    data = path.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = ""
    require(not SECRET_RE.search(text), "Possible credential in publication file: {}".format(rel))


def package(repo, output, kind="skill", manifest_path=None):
    repo, output = Path(repo).resolve(), Path(output).resolve()
    skill = repo / "skills" / "skill-forge"
    validate(skill)
    require((repo / "LICENSE").is_file(), "Release requires LICENSE")
    require(any((repo / name).is_file() for name in ("NOTICE", "THIRD_PARTY_NOTICES.md")), "Release requires an attribution/notice record")
    notices = [repo / name for name in ("LICENSE", "NOTICE", "THIRD_PARTY_NOTICES.md") if (repo / name).is_file()]
    entries = []
    if kind == "skill":
        entries = [(p, Path("skill-forge") / p.relative_to(skill)) for p in files(skill)]
        entries += [(p, Path("skill-forge") / p.name) for p in notices if not (skill / p.name).exists()]
    elif kind == "portable":
        prompt = repo / "portable" / "skill-forge-prompt.md"
        require(prompt.is_file() and prompt.read_text(encoding="utf-8") == portable_text(skill), "Portable bundle missing or drifted; regenerate before packaging")
        portable_notices = [skill / p.name if (skill / p.name).exists() else p for p in notices]
        entries = [(prompt, Path(prompt.name))] + [(p, Path(p.name)) for p in portable_notices]
    elif kind == "source":
        manifest_path = Path(manifest_path) if manifest_path else repo / "release-manifest.json"
        manifest = read_json(manifest_path)
        paths = manifest.get("files") if isinstance(manifest, dict) else manifest
        require(isinstance(paths, list) and all(isinstance(p, str) for p in paths), "Source package requires an explicit release-manifest.json files list")
        require(len(paths) == len(set(paths)), "Duplicate release manifest entry")
        for raw in paths:
            rel = Path(raw)
            require(not rel.is_absolute() and ".." not in rel.parts and within(repo / rel, repo), "Invalid publication path")
            entries.append((repo / rel, Path("skill-forge") / rel))
        for notice in notices:
            require(notice.name in paths, "Source manifest omits required notice: {}".format(notice.name))
        required = {"README.md", "skills/skill-forge/SKILL.md", "portable/skill-forge-prompt.md"}
        require(required <= set(paths), "Source manifest omits essential deliverables")
    else:
        raise ForgeError("Unknown package kind")
    names = set()
    unique_entries = []
    for path, rel in entries:
        check_public_file(path, rel)
        if rel.as_posix() in names:
            # Root notices are authoritative when duplicated inside a skill.
            existing = next(p for p, r in unique_entries if r == rel)
            require(file_hash(existing) == file_hash(path), "Conflicting duplicate package path: {}".format(rel))
            continue
        names.add(rel.as_posix())
        unique_entries.append((path, rel))
    output.parent.mkdir(parents=True, exist_ok=True)
    require(not output.exists(), "Package output already exists; choose a new path or remove the reviewed old artifact")
    with zipfile.ZipFile(str(output), "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, rel in sorted(unique_entries, key=lambda pair: pair[1].as_posix()):
            info = zipfile.ZipInfo(rel.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3  # Stable archive metadata on Windows and POSIX.
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    # Verify the actual extracted package, including relative links.
    with tempfile.TemporaryDirectory(prefix="forge-package-check-") as temp:
        with zipfile.ZipFile(str(output)) as archive:
            archive.extractall(temp)
        if kind == "skill":
            validate(Path(temp) / "skill-forge")
        elif kind == "source":
            validate(Path(temp) / "skill-forge" / "skills" / "skill-forge")
    return {"status": "pass", "kind": kind, "output": str(output), "files": len(unique_entries), "sha256": file_hash(output), "publication_review": "Inspect manifest and examples before publishing; secret-pattern checks cannot prove absence of private information."}


def parser():
    default_skill = Path(__file__).resolve().parent.parent
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--version", action="version", version=VERSION)
    sub = p.add_subparsers(dest="command", required=True)
    q = sub.add_parser("validate", help="Check skill metadata and packaged references")
    q.add_argument("path", type=Path)
    q = sub.add_parser("questions", help="Search question metadata")
    q.add_argument("query", nargs="?", default="")
    q.add_argument("--skill", type=Path, default=default_skill)
    q.add_argument("--status", choices=("candidate", "accepted", "revised", "retired"))
    q = sub.add_parser("bundle", help="Generate or check self-contained portable prompt")
    q.add_argument("--skill", type=Path, default=default_skill)
    q.add_argument("--output", type=Path, required=True)
    q.add_argument("--check", action="store_true")
    q = sub.add_parser("session-init", help="Create private portable session JSON")
    q.add_argument("--state-dir", type=Path, required=True)
    q.add_argument("--name", default="session")
    q = sub.add_parser("hash", help="Compute a candidate directory binding")
    q.add_argument("path", type=Path)
    q = sub.add_parser("prepare", help="Freeze criteria, evaluator, and baseline before editing")
    q.add_argument("target", type=Path)
    q.add_argument("--state-dir", type=Path, required=True)
    q.add_argument("--criteria", type=Path, required=True)
    q.add_argument("--evaluator", type=Path, required=True)
    q.add_argument("--effort-minutes", type=float, required=True)
    q.add_argument("--max-rounds", type=int, default=3)
    q = sub.add_parser("submit", help="Check evidence and automatically adopt or retain candidate")
    q.add_argument("run", type=Path)
    q.add_argument("--candidate", type=Path, required=True)
    q.add_argument("--evidence", type=Path, required=True)
    q = sub.add_parser("rollback", help="Restore baseline without overwriting later changes")
    q.add_argument("run", type=Path)
    q = sub.add_parser("install", help="Install or safely update a managed copy")
    q.add_argument("source", type=Path)
    q.add_argument("destination", type=Path)
    q.add_argument("--update", action="store_true")
    q = sub.add_parser("package", help="Create an inspected release ZIP")
    q.add_argument("--repo", type=Path, required=True)
    q.add_argument("--output", type=Path, required=True)
    q.add_argument("--kind", choices=("skill", "portable", "source"), default="skill")
    q.add_argument("--manifest", type=Path)
    return p


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        if args.command == "validate":
            result = validate(args.path)
        elif args.command == "questions":
            result = search_questions(args.skill, args.query, args.status)
        elif args.command == "bundle":
            content = portable_text(args.skill)
            if args.check:
                require(args.output.is_file() and args.output.read_text(encoding="utf-8") == content, "Portable prompt has drifted or is missing")
            else:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                write_text(args.output, content)
            result = {"status": "pass", "output": str(args.output), "checked": args.check}
        elif args.command == "session-init":
            result = session_init(args.state_dir, args.name)
        elif args.command == "hash":
            result = {"sha256": tree_hash(args.path)}
        elif args.command == "prepare":
            result = prepare(args.target, args.state_dir, args.criteria, args.evaluator, args.effort_minutes, args.max_rounds)
        elif args.command == "submit":
            result = submit(args.run, args.candidate, args.evidence)
        elif args.command == "rollback":
            result = rollback(args.run)
        elif args.command == "install":
            result = install(args.source, args.destination, args.update)
        else:
            result = package(args.repo, args.output, args.kind, args.manifest)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 2 if isinstance(result, dict) and result.get("status") == "rejected" else 0
    except (ForgeError, OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
