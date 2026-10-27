# File helpers

The complete [helper reference](../skills/skill-forge/references/helpers.md) ships
inside the installable skill and the portable prompt. It documents validation,
question search, private sessions, frozen evaluation evidence, automatic adoption,
rollback, managed installs, and allowlisted release packaging.

From a source checkout, run:

```sh
python3 skills/skill-forge/scripts/forge.py --help
python3 -m unittest discover -s tests -v
```

The helpers use Python 3.9+ and its standard library. They check evidence supplied
by an evaluator; they do not independently authenticate model executions or replace
the evaluation rubric. See the reference for schemas and limitations.


## Delivery and Finder state in 0.2.0

New session records include separate `skill_delivery` and `domain_output_contract` fields. Skill delivery records local file/folder/package or GitHub destination, owner/repository, visibility and publication authorization; the domain contract records what the generated skill produces. Existing schema-1 records remain usable: add missing optional fields when resuming rather than resetting confirmed answers.

`refinement_status` keeps the next material decision and readiness state. `skill_finder` keeps research status, a brief fingerprint, report location and a skip reason where applicable. Store those records and raw research context privately. A still-current report can be reused; changed requirements can invalidate its fit. Session fields record decisions and evidence, not new external permissions.

The portable bundle now embeds bundled sub-skill resources, including Skill Finder's complete instructions and license. The regular skill ZIP and managed installation include the same nested files. Nested packaging does not itself promise native independent discovery.

## Optional integrations in 0.4.0

From a source checkout:

```sh
python3 skills/skill-forge/scripts/forge.py integrations
python3 skills/skill-forge/scripts/forge.py attach-anatomy /path/to/pressure-rig-explainer
node /path/to/pressure-rig-explainer/assets/anatomy/build.mjs 250 200
```

On Windows use `py -3` for Python and quote paths with spaces. In a standalone skill ZIP, substitute `skill-forge/scripts/forge.py` for the script path. The target must already be a real skill directory with valid metadata and a matching folder name. Attachment adds the complete `assets/anatomy` slice but does not rewrite `SKILL.md`; integrate its relative README reference and generation steps into that target.

`integrations` reports bundled adapters and dependencies without probing, registering or setting up tools. It does not report a connected REA server. `attach-anatomy` preflights conflicts and uses staged, exclusive atomic directory publication. An identical repeat is unchanged; partial/customized resources, unsafe linked paths and destination collisions are refused. Existing unrelated user files are preserved. Unsupported exclusive-publication platforms fail closed. Rendering later creates/replaces the demo's own `figure.html` and `figure.svg`; copy a writable target and preserve wanted generated outputs first.

The original example uses the pinned real Anatomy renderer and standalone CSS with a shared pure pressure/area model. It requires optional Node.js 20.10+ and no npm installation. Attachment itself needs only Python. Chrome or a compatible browser is needed to verify appearance and interactions. See [integration scope and evidence](integrations.md); syntax checks and file copies do not prove visual quality.
