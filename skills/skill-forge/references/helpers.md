# Optional file helpers

<!-- skill-forge-contents:start -->
**Contents**

- [Private sessions](#private-sessions)
- [Freeze an improvement before evaluating it](#freeze-an-improvement-before-evaluating-it)
- [Supply actual evidence and adopt automatically](#supply-actual-evidence-and-adopt-automatically)
- [Managed copies](#managed-copies)
- [Release packages](#release-packages)
<!-- skill-forge-contents:end -->

Python 3.9 or later is sufficient; there are no third-party dependencies or paid
API requirements. Run these commands from the installed `skill-forge` directory.
The core conversation also works without Python. All helpers print JSON; success
returns exit code 0, invalid input returns 1, and a retained rejected candidate
returns 2.

```sh
python3 scripts/forge.py --help
python3 scripts/forge.py validate .
python3 scripts/forge.py questions "evidence" --status accepted
python3 scripts/forge.py bundle --skill . --output /tmp/skill-forge-prompt.md
python3 scripts/forge.py bundle --skill . --output /tmp/skill-forge-prompt.md --check
```

`validate` checks required discovery fields, the skill name and directory match,
question record completeness, duplicate question identifiers, and local Markdown
file links. It rejects links outside the package and symlinks. If supplied, the optional
`compatibility` field must contain 1–500 characters. The supported scalar subset
is plain/quoted text and literal/folded block text; this is not a full YAML parser.
It does not establish semantic quality, anchor existence or native-host acceptance.

For a skill intended for Claude, add `--profile claude` to `validate`. This opt-in
profile rejects names containing `claude` or `anthropic` and angle brackets in
the parsed name/description. It deliberately leaves body markup and YAML block
indicators alone. Default `--profile generic` keeps vendor-neutral naming and
description rules. These are discovery-field lint checks, not a security audit.

```sh
python3 scripts/forge.py validate /path/to/my-skill --profile claude
```

Literal paths under `references`, `templates`, `questions`, `scripts`,
and `assets` are checked when written in inline code. Examples inside fenced code
blocks are not interpreted as live links.

`questions` searches all record fields for every query word, ranks by occurrence,
and optionally filters candidate, accepted, revised, or retired records. This is
literal discovery support; the agent must decide whether a question is useful,
already answered, redundant, or dependent on another decision. Search coverage
alone does not prove a better interview.

`bundle` combines the canonical skill and every reference, template, and question
resource. It also includes skill-local license and attribution files when present.
Relative resource links become anchors to included sections; optional executable
files remain references to the full package. A content digest and `--check` detect
drift. The script itself is not required to use the portable instructions.

## Private sessions

Choose a state directory outside the skill and repository. Do not put private
answers in examples, shared question records, commits, or release manifests.

```sh
python3 scripts/forge.py session-init \
  --state-dir "$HOME/.local/share/skill-forge" --name research-project
```

The returned `session.json` separates confirmed requirements, defaults,
assumptions, examples, acceptance criteria, open questions, next action, and private
personalization. Update this record as work proceeds. Resume by reading it before
asking questions. State directories have owner-only permissions and an ignore file;
the helper refuses a state location inside a detected Git or Skill Forge repository.
It cannot identify every arbitrary publishable folder, encrypt data, or stop an
explicitly supplied file from containing private information. Apply normal access
controls and inspect files before sharing. Without files, return the same compact
JSON as a user-saved handoff. No background memory or model training is implied.

## Freeze an improvement before evaluating it

Prepare a small case table and a fixed evaluator outside the target. An evaluator
can be a deterministic script for an actual executable behavior or a rubric/prompt
for a real model run. An editorial improvement to an interview needs observed model
behavior; format checks and imagined transcripts are insufficient.

Criteria JSON uses this schema. Each check needs an input, expected behavior, and
failure condition. Acceptance and regression cases are mandatory. Builder behavior
changes also require a held-out case that was not used to develop the patch.

```json
{
  "schema_version": 1,
  "scope": "builder",
  "change_kind": "behavior",
  "evaluation_kind": "script_execution",
  "checks": [
    {
      "id": "destination",
      "kind": "acceptance",
      "input": "Search questions for spreadsheet",
      "expected": "Retrieve a useful destination question",
      "failure": "No relevant question is returned"
    },
    {
      "id": "existing",
      "kind": "regression",
      "input": "Search questions for constraints",
      "expected": "Preserve the existing constraints question",
      "failure": "The existing question disappears"
    },
    {
      "id": "heldout",
      "kind": "held_out",
      "input": "An independently reserved destination query",
      "expected": "Retrieve a relevant destination question",
      "failure": "No relevant question is returned"
    }
  ],
  "benefit": {
    "metric": "relevant_destination_hits",
    "direction": "higher",
    "min_delta": 1
  }
}
```

`scope` is `target` or `builder`; `change_kind` is `behavior` or `structural`;
`evaluation_kind` is `script_execution` or `model_execution`. Benefit direction
can be `higher` or `lower`; a positive `min_delta` defines the improvement before
testing. Use an explicit qualitative rubric with a consistent scoring scale when
evaluating model outputs, and retain the outputs and scoring justification.

```sh
python3 scripts/forge.py prepare /path/to/active/skill-forge \
  --state-dir "$HOME/.local/share/skill-forge" \
  --criteria /private-work/criteria.json --evaluator /private-work/evaluator.py \
  --effort-minutes 30 --max-rounds 3
```

Replace illustrative absolute paths with actual locations. Preparation snapshots
the active target, criteria, and evaluator, then returns the run directory and
their SHA-256 hashes. Candidates must be separate directory trees. The helper
enforces a wall-clock time limit from preparation and at most three submissions;
it does not measure token use or active typing time. A rejected submission consumes
a round. A later authorized run can resume saved unresolved work with a new limit.
Do not create repeated runs to evade an agreed session budget.

The run directory is trusted local control state. Keep it outside candidate control.
Hash binding detects accidental or candidate-file changes; it is not a security
boundary against a process authorized to rewrite both manifests and evidence.

## Supply actual evidence and adopt automatically

Run the frozen evaluator under comparable conditions against the baseline and
candidate. Record host/runtime and model versions, inputs, outputs, rubric scores,
and relevant limitations. The helper does not run an LLM or invent an evaluator.
Get the candidate binding with:

```sh
python3 scripts/forge.py hash /private-work/candidate/skill-forge
```

Evidence JSON has this shape. The placeholder hashes must be replaced with the
actual returned values. Each frozen check must appear exactly once. Result
artifacts must be nonempty files relative to the evidence file's directory.

```json
{
  "schema_version": 1,
  "baseline_hash": "SHA256_FROM_PREPARE",
  "candidate_hash": "SHA256_FROM_HASH",
  "criteria_hash": "SHA256_FROM_PREPARE",
  "evaluator_hash": "SHA256_FROM_PREPARE",
  "execution": {
    "kind": "script_execution",
    "coverage": "behavior",
    "model": "not-applicable",
    "host": "Python VERSION on HOST",
    "conditions": "Same fixed script and queries run against both versions."
  },
  "results": [
    {"id": "destination", "baseline": "fail", "candidate": "pass", "artifact": "execution.json"},
    {"id": "existing", "baseline": "pass", "candidate": "pass", "artifact": "execution.json"},
    {"id": "heldout", "baseline": "fail", "candidate": "pass", "artifact": "execution.json"}
  ],
  "benefit": {"metric": "relevant_destination_hits", "baseline": 0, "candidate": 1}
}
```

These are **schema examples, not successful execution evidence**. For model runs,
use `model_execution`, the actual model/host identifiers available, a fixed rubric,
and actual baseline/candidate transcripts. If exact versions are unavailable, state
that limitation. Do not label an illustrative simulation as an execution.

```sh
python3 scripts/forge.py submit /private-state/run-ID \
  --candidate /private-work/candidate/skill-forge --evidence /private-work/evidence.json
python3 scripts/forge.py rollback /private-state/run-ID
```

Submission adopts automatically only when the active target still matches its
snapshot, the frozen criteria/evaluator and evidence bindings match, all predefined
checks pass, the stated benefit is achieved, and candidate file validation passes.
Behavior updates need `coverage: behavior`. Simulated, formatting-only, missing,
failed, or inconclusive evidence leaves the active version intact. The candidate,
evidence, copied artifacts, and concise result are retained under the run. Failed
preflight checks such as an expired budget do not copy a new candidate; the supplied
candidate remains untouched at its original path.

The helper validates **caller-supplied evidence records**, not the truth of every
claim inside them. A hash proves which files a record names; it does not prove a
model was called or that the rubric is sound. Review actual artifacts and use an
independent evaluation context when available. Candidates cannot authorize
themselves by weakening their checks. Preserve the old active version when honest
behavioral checks cannot run.

Rollback restores the baseline while retaining the candidate history. It refuses
to overwrite changes made after adoption. After adoption or rollback, prepare a
new run to make another change. The helper replaces a whole skill directory and
stages it on the same filesystem; it is intended for a single writer. Coordinate
parallel writers rather than treating hashes as a file lock.

## Managed copies

```sh
python3 scripts/forge.py install /source/skill-forge /host/skills/skill-forge
python3 scripts/forge.py install /source/skill-forge /host/skills/skill-forge --update
```

Installation creates a small management marker. Updates verify that the installed
copy still matches its last installed hash. If a user customized it, the helper
refuses to overwrite it; merge the customization in a separate candidate and test
it first. Apply the command to each known managed destination and report conflicts.
There is no global registry, configuration editing, automatic discovery of every
host, or upstream publication. A locally improved managed copy intentionally
counts as customized until its merge is resolved. For removal, remove only the
selected installed `skill-forge` directory or link, using the host guide.

## Release packages

Run packaging from a repository checkout using its canonical helper:

```sh
python3 skills/skill-forge/scripts/forge.py package --repo . \
  --kind skill --output /tmp/skill-forge-skill.zip
python3 skills/skill-forge/scripts/forge.py package --repo . \
  --kind portable --output /tmp/skill-forge-portable.zip
python3 skills/skill-forge/scripts/forge.py package --repo . \
  --kind source --output /tmp/skill-forge-source.zip
```

Skill packages contain only the canonical skill tree and license/notice records.
Portable packages contain the checked prompt bundle and license/notice records.
Source packages require an explicit `release-manifest.json` containing a `files`
array of reviewed repository-relative file paths. Required source entries include
README, canonical SKILL.md, portable prompt, and notices. Wildcards and parent
traversal are not accepted. The helper rejects known private-state directories,
symlinks, common credential patterns, and private-key files. It extracts packages
to a clean temporary location and checks the skill's file links before returning a
checksum. Existing archive outputs are not overwritten.

Package checks are safeguards, not proof that arbitrary prose contains no private
details. Inspect every selected file and intentionally public example before GitHub
publication. Keep a source manifest under review; adding a question does not grant
permission to publish its motivating private transcript.
