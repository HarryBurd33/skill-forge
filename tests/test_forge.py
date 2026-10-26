"""Executed helper checks; these do not claim to evaluate an LLM interview."""
import copy
import os
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from types import SimpleNamespace
import zipfile


SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "skill-forge" / "scripts" / "forge.py"
SPEC = importlib.util.spec_from_file_location("forge", SCRIPT)
forge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(forge)


def write_fixture(path, text):
    Path(path).write_bytes(text.encode("utf-8"))


def question(identifier, text):
    return {"id": identifier, "status": "accepted", "question": text,
            "purpose": text, "ask_when": "When missing.", "skip_when": "When settled.",
            "dependencies": [], "affects": ["output"], "evidence": "Test fixture."}


class ForgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="forge-test-")
        self.root = Path(self.temp.name)
        self.repo = self.root / "repository"
        self.skill = self.repo / "skills" / "skill-forge"
        self.skill.mkdir(parents=True)
        write_fixture(self.repo / "LICENSE", "MIT License\nCopyright example\n")
        write_fixture(self.repo / "NOTICE", "Original test fixture.\n")
        write_fixture(self.repo / "README.md", "Example\n")
        write_fixture(self.skill / "SKILL.md", "---\nname: skill-forge\ndescription: Build useful skills.\n---\n# Builder\n\n[Reference](references/test.md)\n")
        (self.skill / "references").mkdir()
        write_fixture(self.skill / "references" / "test.md", "Preserve constraints.\n")
        (self.skill / "questions").mkdir()
        forge.write_json(self.skill / "questions" / "questions.json", [question("q-constraints", "What constraints apply?")])
        self.criteria = {"schema_version": 1, "scope": "builder", "change_kind": "behavior",
                         "evaluation_kind": "script_execution",
                         "checks": [
                             {"id": "destination", "kind": "acceptance", "input": "spreadsheet", "expected": "Retrieve destination question", "failure": "No destination match"},
                             {"id": "constraints", "kind": "regression", "input": "constraints", "expected": "Preserve constraints question", "failure": "Missing constraints"},
                             {"id": "csv", "kind": "held_out", "input": "csv", "expected": "Retrieve destination question", "failure": "No destination match"}],
                         "benefit": {"metric": "destination_hits", "direction": "higher", "min_delta": 1}}
        self.criteria_path = self.root / "criteria.json"
        forge.write_json(self.criteria_path, self.criteria)
        self.evaluator = self.root / "evaluate.py"
        write_fixture(self.evaluator, """import importlib.util, json, pathlib, sys
s = importlib.util.spec_from_file_location('forge', sys.argv[1])
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
skill = pathlib.Path(sys.argv[2])
print(json.dumps({q: [x['id'] for x in m.search_questions(skill, q)] for q in ['spreadsheet', 'constraints', 'csv']}))
""")
        self.state = self.root / "private-state"

    def tearDown(self):
        self.temp.cleanup()

    def test_optional_compatibility_contract(self):
        original = (self.skill / "SKILL.md").read_text(encoding="utf-8")
        for scalar in ('"P"', '"' + 'x' * 500 + '"', "'Python 3.9 or newer'", '>\n  Python 3.9\n  with file access', '|\n  Python 3.9\n  with file access', '"null"'):
            write_fixture(self.skill / "SKILL.md", original.replace('description: Build useful skills.\n', 'description: Build useful skills.\ncompatibility: ' + scalar + '\n'))
            self.assertEqual(forge.validate(self.skill)["status"], "pass")
        for scalar in ('', '""', "''", 'null', '~', 'x' * 501):
            write_fixture(self.skill / "SKILL.md", original.replace('description: Build useful skills.\n', 'description: Build useful skills.\ncompatibility: ' + scalar + '\n'))
            with self.assertRaisesRegex(forge.ForgeError, 'compatibility'):
                forge.validate(self.skill)
        write_fixture(self.skill / "SKILL.md", original)
        self.assertEqual(forge.validate(self.skill)["status"], "pass")

    def test_claude_profile_is_explicit_and_metadata_only(self):
        root = self.root / 'claude-helper'
        root.mkdir()
        write_fixture(root / 'SKILL.md', '---\nname: claude-helper\ndescription: Build useful skills.\n---\n# Helper\n')
        self.assertEqual(forge.validate(root)["profile"], "generic")
        with self.assertRaisesRegex(forge.ForgeError, 'reserved'):
            forge.validate(root, 'claude')
        original = (self.skill / 'SKILL.md').read_text(encoding='utf-8')
        write_fixture(self.skill / 'SKILL.md', original.replace('description: Build useful skills.', 'description: Use <task> input.'))
        self.assertEqual(forge.validate(self.skill)["status"], "pass")
        with self.assertRaisesRegex(forge.ForgeError, 'description'):
            forge.validate(self.skill, 'claude')
        write_fixture(self.skill / 'SKILL.md', original.replace('description: Build useful skills.', 'description: >\n  Build useful skills.') + '\n<example>Allowed body markup</example>\n')
        self.assertEqual(forge.validate(self.skill, 'claude')["profile"], 'claude')

    def test_validate_profile_cli(self):
        process = subprocess.run([sys.executable, str(SCRIPT), 'validate', str(self.skill), '--profile', 'claude'], capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr + process.stdout)
        self.assertEqual(json.loads(process.stdout)["profile"], 'claude')
        process = subprocess.run([sys.executable, str(SCRIPT), 'validate', str(self.skill), '--profile', 'unknown'], capture_output=True, text=True)
        self.assertNotEqual(process.returncode, 0)
        self.assertIn('invalid choice', process.stderr)

    def prepare_candidate(self):
        manifest = forge.prepare(self.skill, self.state, self.criteria_path, self.evaluator, 30)
        run = Path(manifest["run"])
        candidate = self.root / "candidate" / "skill-forge"
        forge.copy_tree(self.skill, candidate)
        questions = forge.read_json(candidate / "questions" / "questions.json")
        questions.append(question("q-destination", "Should the output be a spreadsheet, CSV, document or repository?"))
        forge.write_json(candidate / "questions" / "questions.json", questions)
        return manifest, run, candidate

    def evidence(self, manifest, candidate):
        results = {}
        for label, path in (("baseline", self.skill), ("candidate", candidate)):
            process = subprocess.run([sys.executable, str(self.evaluator), str(SCRIPT), str(path)], text=True, capture_output=True, check=True)
            results[label] = json.loads(process.stdout)
        artifact = self.root / "execution.json"
        forge.write_json(artifact, {"command": [sys.executable, str(self.evaluator)], "actual_results": results})
        evidence = {"schema_version": 1,
                    **{k: manifest[k] for k in ("baseline_hash", "criteria_hash", "evaluator_hash")},
                    "candidate_hash": forge.tree_hash(candidate),
                    "execution": {"kind": "script_execution", "coverage": "behavior", "model": "not-applicable", "host": "Python " + sys.version.split()[0], "conditions": "Same script, queries, and machine; two subprocess executions."},
                    "results": [], "benefit": {"metric": "destination_hits", "baseline": len(results["baseline"]["spreadsheet"]), "candidate": len(results["candidate"]["spreadsheet"])}}
        for case, query in (("destination", "spreadsheet"), ("constraints", "constraints"), ("csv", "csv")):
            evidence["results"].append({"id": case, "baseline": "pass" if results["baseline"][query] else "fail", "candidate": "pass" if results["candidate"][query] else "fail", "artifact": artifact.name})
        path = self.root / "evidence.json"
        forge.write_json(path, evidence)
        return path, evidence

    def test_validation_and_query(self):
        self.assertEqual(forge.validate(self.skill)["status"], "pass")
        self.assertEqual(forge.search_questions(self.skill, "constraints")[0]["id"], "q-constraints")
        self.assertEqual(forge.search_questions(self.skill, "spreadsheet"), [])

    def test_broken_and_escaping_link(self):
        for link in ("missing.md", "../../../LICENSE"):
            write_fixture(self.skill / "references" / "test.md", "[Bad]({})".format(link))
            with self.assertRaises(forge.ForgeError):
                forge.validate(self.skill)

    def test_question_schema_and_duplicate_id(self):
        q = question("same", "What?")
        forge.write_json(self.skill / "questions" / "questions.json", [q, q])
        with self.assertRaisesRegex(forge.ForgeError, "Duplicate"):
            forge.validate(self.skill)

    def test_bundle_contains_resources_and_detects_drift(self):
        output = self.repo / "portable" / "skill-forge-prompt.md"
        self.assertEqual(forge.main(["bundle", "--skill", str(self.skill), "--output", str(output)]), 0)
        text = output.read_text(encoding="utf-8")
        self.assertIn("Preserve constraints", text)
        self.assertIn("q-constraints", text)
        self.assertEqual(forge.main(["bundle", "--skill", str(self.skill), "--output", str(output), "--check"]), 0)
        write_fixture(output, text + "drift")
        self.assertEqual(forge.main(["bundle", "--skill", str(self.skill), "--output", str(output), "--check"]), 1)

    def test_real_executed_candidate_adopts_and_rolls_back(self):
        manifest, run, candidate = self.prepare_candidate()
        path, _ = self.evidence(manifest, candidate)
        result = forge.submit(run, candidate, path)
        self.assertEqual(result["status"], "adopted")
        self.assertEqual(forge.tree_hash(self.skill), forge.tree_hash(candidate))
        self.assertEqual(forge.rollback(run)["restored_hash"], manifest["baseline_hash"])
        self.assertTrue(Path(result["candidate_preserved"]).exists())

    def test_nested_finder_survives_portable_export_and_install(self):
        finder = self.skill / "subskills" / "skill-finder"
        finder.mkdir(parents=True)
        write_fixture(finder / "SKILL.md", "---\nname: skill-finder\ndescription: Inspect candidate foundations.\n---\nCheck the actual license before reuse.\n")
        write_fixture(finder / "LICENSE", "MIT License\nNested resource notice\n")
        with (self.skill / "SKILL.md").open("a", encoding="utf-8", newline="\n") as stream:
            stream.write("\n[Finder](subskills/skill-finder/SKILL.md)\n")
        text = forge.portable_text(self.skill)
        self.assertIn("Check the actual license before reuse.", text)
        self.assertIn("Nested resource notice", text)
        self.assertIn("#resource-subskills-skill-finder-skill-md", text)
        destination = self.root / "personal" / "skill-forge"
        forge.install(self.skill, destination)
        self.assertEqual((destination / "subskills/skill-finder/SKILL.md").read_bytes(), (finder / "SKILL.md").read_bytes())
        self.assertEqual(forge.validate(destination)["status"], "pass")

    def test_session_keeps_distribution_separate_from_domain_output(self):
        path = Path(forge.session_init(self.state, "Delivery choices")["session"])
        record = forge.read_json(path)
        self.assertIn("skill_delivery", record)
        self.assertIn("skill_finder", record)
        record["skill_delivery"].update({"format": "skill-folder", "destination": "local", "publication_authorized": False})
        record["skill_finder"].update({"status": "complete", "brief_fingerprint": "fixture-brief", "report": "finder-report.json"})
        record["domain_output_contract"] = {"format": "spreadsheet"}
        forge.write_json(path, record)
        resumed = forge.read_json(path)
        self.assertFalse(resumed["skill_delivery"]["publication_authorized"])
        self.assertEqual(resumed["domain_output_contract"]["format"], "spreadsheet")
        self.assertEqual(resumed["skill_finder"]["brief_fingerprint"], "fixture-brief")

    def test_failed_candidate_is_preserved_and_baseline_stays_active(self):
        manifest, run, candidate = self.prepare_candidate()
        path, evidence = self.evidence(manifest, candidate)
        evidence["results"][0]["candidate"] = "fail"
        forge.write_json(path, evidence)
        result = forge.submit(run, candidate, path)
        self.assertEqual(result["status"], "rejected")
        self.assertEqual(forge.tree_hash(self.skill), manifest["baseline_hash"])
        self.assertTrue(Path(result["candidate_preserved"]).exists())

    def test_simulation_and_format_only_behavior_evidence_rejected(self):
        manifest, run, candidate = self.prepare_candidate()
        path, evidence = self.evidence(manifest, candidate)
        evidence["execution"]["kind"] = "simulated"
        forge.write_json(path, evidence)
        self.assertEqual(forge.submit(run, candidate, path)["status"], "rejected")
        evidence["execution"].update(kind="script_execution", coverage="formatting")
        forge.write_json(path, evidence)
        self.assertEqual(forge.submit(run, candidate, path)["status"], "rejected")

    def test_no_benefit_and_hash_mismatch_rejected(self):
        manifest, run, candidate = self.prepare_candidate()
        path, evidence = self.evidence(manifest, candidate)
        evidence["benefit"]["candidate"] = 0
        forge.write_json(path, evidence)
        self.assertEqual(forge.submit(run, candidate, path)["status"], "rejected")
        evidence["candidate_hash"] = "incorrect"
        forge.write_json(path, evidence)
        self.assertEqual(forge.submit(run, candidate, path)["status"], "rejected")

    def test_frozen_criteria_cannot_be_weakened(self):
        manifest, run, candidate = self.prepare_candidate()
        path, _ = self.evidence(manifest, candidate)
        altered = copy.deepcopy(self.criteria)
        altered["benefit"]["min_delta"] = 0
        forge.write_json(run / "criteria.json", altered)
        with self.assertRaisesRegex(forge.ForgeError, "Frozen criteria"):
            forge.submit(run, candidate, path)
        self.assertEqual(forge.tree_hash(self.skill), manifest["baseline_hash"])

    def test_round_limit_and_time_limit(self):
        manifest, run, candidate = self.prepare_candidate()
        path, evidence = self.evidence(manifest, candidate)
        evidence["results"][0]["candidate"] = "inconclusive"
        forge.write_json(path, evidence)
        for _ in range(3):
            self.assertEqual(forge.submit(run, candidate, path)["status"], "rejected")
        with self.assertRaisesRegex(forge.ForgeError, "round limit"):
            forge.submit(run, candidate, path)
        data = forge.read_json(run / "run.json")
        data.update(rounds=0, created="2000-01-01T00:00:00+00:00")
        forge.write_json(run / "run.json", data)
        with self.assertRaisesRegex(forge.ForgeError, "time limit"):
            forge.submit(run, candidate, path)

    def test_rollback_preserves_later_customization(self):
        manifest, run, candidate = self.prepare_candidate()
        path, _ = self.evidence(manifest, candidate)
        self.assertEqual(forge.submit(run, candidate, path)["status"], "adopted")
        write_fixture(self.skill / "personal.md", "Local change")
        with self.assertRaisesRegex(forge.ForgeError, "diverged"):
            forge.rollback(run)
        self.assertTrue((self.skill / "personal.md").exists())

    def test_adoption_preserves_concurrent_target_change(self):
        manifest, run, candidate = self.prepare_candidate()
        path, _ = self.evidence(manifest, candidate)
        write_fixture(self.skill / "local.md", "Personalization")
        with self.assertRaisesRegex(forge.ForgeError, "Active target changed"):
            forge.submit(run, candidate, path)
        self.assertTrue((self.skill / "local.md").exists())

    def test_managed_install_update_and_customization_refusal(self):
        dest = self.root / "installed" / "skill-forge"
        forge.install(self.skill, dest)
        write_fixture(self.skill / "references" / "test.md", "New upstream guidance\n")
        forge.install(self.skill, dest, update=True)
        self.assertEqual(forge.tree_hash(dest), forge.tree_hash(self.skill))
        write_fixture(dest / "local.md", "My preference")
        with self.assertRaisesRegex(forge.ForgeError, "customizations"):
            forge.install(self.skill, dest, update=True)
        self.assertEqual((dest / "local.md").read_text(encoding="utf-8"), "My preference")

    def test_private_session_outside_repo_and_snapshot(self):
        result = forge.session_init(self.state, "My planning")
        session = Path(result["session"])
        data = forge.read_json(session)
        data["private_personalization"] = {"wake": "07:15"}
        forge.write_json(session, data)
        with self.assertRaisesRegex(forge.ForgeError, "outside"):
            forge.session_init(self.repo / "private", "bad")
        with self.assertRaises(forge.ForgeError):
            forge.prepare(self.skill, self.skill / "private", self.criteria_path, self.evaluator, 30)
        self.assertNotIn("07:15", forge.portable_text(self.skill))

    def test_package_notices_links_and_private_exclusion(self):
        forge.session_init(self.state, "Private test")
        output = self.root / "skill.zip"
        result = forge.package(self.repo, output)
        self.assertEqual(result["status"], "pass")
        with zipfile.ZipFile(output) as archive:
            names = archive.namelist()
            self.assertIn("skill-forge/LICENSE", names)
            self.assertIn("skill-forge/NOTICE", names)
            self.assertFalse(any("session" in n for n in names))
        (self.skill / "private").mkdir()
        write_fixture(self.skill / "private" / "answers.json", '{"wake":"07:15"}')
        with self.assertRaisesRegex(forge.ForgeError, "Private"):
            forge.package(self.repo, self.root / "bad.zip")

    def test_source_manifest_allowlist_and_portable_bundle(self):
        portable = self.repo / "portable" / "skill-forge-prompt.md"
        portable.parent.mkdir()
        write_fixture(portable, forge.portable_text(self.skill))
        selected = [p.relative_to(self.repo).as_posix() for p in forge.files(self.repo)]
        forge.write_json(self.repo / "release-manifest.json", {"files": selected})
        forge.package(self.repo, self.root / "source.zip", "source")
        forge.package(self.repo, self.root / "portable.zip", "portable")
        selected.append("../criteria.json")
        forge.write_json(self.repo / "release-manifest.json", {"files": selected})
        with self.assertRaisesRegex(forge.ForgeError, "Invalid publication path"):
            forge.package(self.repo, self.root / "escape.zip", "source")

    def test_symlink_is_not_followed(self):
        try:
            (self.skill / "linked").symlink_to(self.root / "criteria.json")
        except OSError as exc:
            if os.name == "nt" and getattr(exc, "winerror", None) == 1314:
                self.skipTest("Windows symlink privilege is unavailable: {}".format(exc))
            raise
        with self.assertRaisesRegex(forge.ForgeError, "Symlink"):
            forge.validate(self.skill)

    def test_utf8_lf_and_unicode_paths_survive_delivery(self):
        folder = self.root / "Café 项目"
        folder.mkdir()
        text = "Résumé — naïve\n第二行\n"
        json_path = folder / "réponse.json"
        forge.write_json(json_path, {"answer": text})
        self.assertEqual(forge.read_json(json_path), {"answer": text})
        self.assertIn("Résumé".encode("utf-8"), json_path.read_bytes())
        self.assertNotIn(b"\r\n", json_path.read_bytes())
        write_fixture(self.skill / "references/test.md", text)
        output = folder / "prompt.md"
        self.assertEqual(forge.main(["bundle", "--skill", str(self.skill), "--output", str(output)]), 0)
        self.assertEqual(output.read_bytes(), forge.portable_text(self.skill).encode("utf-8"))
        self.assertNotIn(b"\r\n", output.read_bytes())
        destination = folder / "installed skills" / "skill-forge"
        forge.install(self.skill, destination)
        self.assertEqual(forge.tree_hash(destination), forge.tree_hash(self.skill))
        archive_path = folder / "skill.zip"
        forge.package(self.repo, archive_path)
        with zipfile.ZipFile(archive_path) as archive:
            self.assertEqual(archive.read("skill-forge/references/test.md"), text.encode("utf-8"))
            self.assertTrue(all(info.create_system == 3 for info in archive.infolist()))

    def test_generated_text_normalizes_crlf_without_locale_defaults(self):
        output = self.root / "lines.txt"
        forge.write_text(output, "Café\r\n第二行\r\n")
        self.assertEqual(output.read_bytes(), "Café\n第二行\n".encode("utf-8"))

    def test_private_directory_permissions_are_platform_accurate(self):
        with mock.patch.object(forge.os, "chmod", wraps=forge.os.chmod) as chmod:
            root = forge.private_root(self.state)
        if os.name == "posix":
            chmod.assert_called_once_with(str(root), 0o700)
            self.assertEqual(root.stat().st_mode & 0o777, 0o700)
        else:
            chmod.assert_not_called()

    def test_reparse_point_detection_and_traversal_refusal(self):
        attributes = SimpleNamespace(st_mode=forge.stat.S_IFDIR, st_file_attributes=0x400)
        with mock.patch.object(forge.Path, "lstat", return_value=attributes):
            self.assertTrue(forge.is_link(self.skill))
            with self.assertRaisesRegex(forge.ForgeError, "reparse"):
                forge.validate(self.skill)
        junction = self.skill / "junction"
        junction.mkdir()
        original = forge.is_link
        with mock.patch.object(forge, "is_link", side_effect=lambda path: Path(path) == junction or original(path)):
            with self.assertRaisesRegex(forge.ForgeError, "reparse"):
                forge.files(self.skill)

    @unittest.skipUnless(os.name == "nt", "Native junction creation requires Windows")
    def test_native_windows_junction_is_not_followed(self):
        outside = self.root / "outside"
        outside.mkdir()
        write_fixture(outside / "sensitive.txt", "Must not enter the skill")
        junction = self.skill / "junction"
        result = subprocess.run(["cmd", "/c", "mklink", "/J", str(junction), str(outside)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Could not create Windows junction: " + result.stderr)
        with self.assertRaisesRegex(forge.ForgeError, "reparse"):
            forge.validate(self.skill)
        self.assertEqual((outside / "sensitive.txt").read_text(encoding="utf-8"), "Must not enter the skill")

    def replacement_candidate(self):
        candidate = self.root / "replacement" / "skill-forge"
        forge.copy_tree(self.skill, candidate)
        write_fixture(candidate / "references/test.md", "Changed behavior\n")
        return candidate

    def test_failed_replacement_restores_previous_tree(self):
        candidate = self.replacement_candidate()
        previous_hash = forge.tree_hash(self.skill)
        replace = forge.os.replace
        calls = []
        def fail_stage(source, target):
            calls.append((source, target))
            if len(calls) == 2:
                raise PermissionError("Simulated file lock")
            return replace(source, target)
        with mock.patch.object(forge.os, "replace", side_effect=fail_stage):
            with self.assertRaisesRegex(PermissionError, "file lock"):
                forge.replace_tree(self.skill, candidate)
        self.assertEqual(forge.tree_hash(self.skill), previous_hash)
        self.assertEqual(list(self.skill.parent.glob(".forge-stage-*")), [])

    def test_failed_restore_keeps_recoverable_previous_tree(self):
        candidate = self.replacement_candidate()
        previous_hash = forge.tree_hash(self.skill)
        replace = forge.os.replace
        calls = []
        def fail_stage_and_restore(source, target):
            calls.append((source, target))
            if len(calls) >= 2:
                raise PermissionError("Simulated file lock")
            return replace(source, target)
        with mock.patch.object(forge.os, "replace", side_effect=fail_stage_and_restore):
            with self.assertRaisesRegex(forge.ForgeError, "prior version is preserved") as error:
                forge.replace_tree(self.skill, candidate)
        backups = list(self.skill.parent.glob(".forge-stage-*/previous"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(forge.tree_hash(backups[0]), previous_hash)
        self.assertIn(str(backups[0]), str(error.exception))
        self.assertFalse(self.skill.exists())
        self.assertEqual(forge.tree_hash(backups[0].parent / self.skill.name), forge.tree_hash(candidate))

    def test_first_replacement_move_failure_keeps_target(self):
        candidate = self.replacement_candidate()
        previous_hash = forge.tree_hash(self.skill)
        with mock.patch.object(forge.os, "replace", side_effect=PermissionError("Simulated locked target")):
            with self.assertRaisesRegex(PermissionError, "locked target"):
                forge.replace_tree(self.skill, candidate)
        self.assertEqual(forge.tree_hash(self.skill), previous_hash)
        self.assertEqual(list(self.skill.parent.glob(".forge-stage-*")), [])

    def test_cli_help_and_version(self):
        help_result = subprocess.run([sys.executable, str(SCRIPT), "--help"], text=True, capture_output=True, check=True)
        self.assertIn("prepare", help_result.stdout)
        version_result = subprocess.run([sys.executable, str(SCRIPT), "--version"], text=True, capture_output=True, check=True)
        self.assertEqual(version_result.stdout.strip(), (SCRIPT.parents[3] / "VERSION").read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
