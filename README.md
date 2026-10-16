# Skill Forge

**Turn a useful idea into a reusable AI skill—and improve it with evidence.**

Describe a workflow in ordinary language. Skill Forge asks only questions that matter, drafts a skill, tries examples, and leaves you an installable folder. It also improves existing skills and evaluates improvements to its own interview and tools.

- Simple, clear ideas can go straight to a draft. Complex uncertainty gets deeper questions.
- Say **quick**, **thorough**, **expert challenge**, **draft now**, **skip**, or **resume** to control the pace.
- Successful updates are applied automatically after predefined checks, with history and rollback. Failed or untested candidates stay separate.
- Private preferences and conversations stay outside published source by default.

## Start here

Choose one route. No paid API or custom service is required for the core conversation.

| Where you work | Start |
| --- | --- |
| Codex | [Install for yourself or a project](docs/codex.md) |
| Claude Code | [Install for yourself or a project](docs/claude-code.md) |
| Another capable chat model | Paste or upload [the self-contained prompt](portable/skill-forge-prompt.md), then describe your idea |

Download the [v0.1.0 release](https://github.com/HarryBurd33/skill-forge/releases/tag/v0.1.0): the **skill ZIP** contains an installable `skill-forge/` folder; the **portable ZIP** contains the standalone prompt and license; the **source ZIP** contains examples, tests and documentation. See [compatibility](docs/compatibility.md) for what was actually tested.

After installation, try:

> Use Skill Forge to build a skill that turns my meeting notes into action items. Keep unknown owners and dates explicit. Return a Markdown table. Draft now.

Codex users can explicitly start with `$skill-forge`; Claude Code users with `/skill-forge`. Plain-chat users first supply the portable prompt. Your generated skill will include its own `SKILL.md`, any needed supporting files, sample requests, installation steps and a short validation report. It does **not** need Skill Forge to run.

For the first result, check one realistic input and a failure case. Tell the builder what was wrong or changed:

> Improve this skill: it assigns a speaker as the owner even when nobody accepted the task. Keep its table format and meeting order.

Or improve the builder:

> Evaluate a Skill Forge improvement: users who ask for a spreadsheet are not finding the output-destination question. Compare retrieval before and after, preserve the prior version, and adopt only if checks pass.

## What happens during a session

The builder maintains a compact brief of confirmed needs, proposed defaults, assumptions, examples, acceptance checks and open questions. It inspects available facts before asking you. It shows the brief for correction without making you approve every routine step. An early example reveals gaps more efficiently than a long fixed questionnaire.

When a session pauses, save its private record or copy its handoff into the next chat. Improvement means revised files and recorded evidence; it does not retrain a model or promise memory across unrelated conversations.

[Worked examples](examples/README.md) cover research and writing, an adaptive prompt builder, a planner handling an exam, and a correction to an existing skill. The public inputs are fictional. Authored demonstrations are labeled separately from [executed evaluation results](evals/REPORT.md).

## Evidence and automatic updates

A candidate connects an observation to a hypothesis, patch and checks declared before testing. It must preserve existing acceptance criteria, pass relevant regressions and demonstrate its intended benefit against the prior version. Broader builder changes need held-out scenarios. Formatting alone cannot establish behavioral improvement.

The optional Python helper snapshots files, freezes the evaluator and criteria, checks hash-bound evidence, adopts passing candidates, and rolls back safely. It does not generate or authenticate model results. Use genuine execution artifacts and a trusted evaluator. Default improvement runs allow three candidates and a 30-minute wall-clock limit; failures or missing evidence preserve the active version. [Helper commands and evidence format](skills/skill-forge/references/helpers.md).

For local development with Python 3.9 or newer:

```sh
python3 skills/skill-forge/scripts/forge.py validate skills/skill-forge
python3 -m unittest discover -s tests -v
python3 skills/skill-forge/scripts/forge.py bundle --skill skills/skill-forge --output portable/skill-forge-prompt.md --check
```

Before installing a generated skill, verify that its innermost folder matches the `name` in its metadata. See [the release report](evals/REPORT.md) for observed text-only limitations and exact test results.

The canonical builder lives in `skills/skill-forge/`. The portable prompt is generated from it, so edits cannot quietly drift. Managed installations refuse to overwrite customized copies; keep personal settings outside the shared skill.

## Contribute an improvement

[Report a failure or propose a question](CONTRIBUTING.md). A helpful contribution includes a realistic input, expected behavior, actual failure, and why the proposed change helps. Search the question library first: fewer useful questions beat more repetitive questions. Accepted changes gain a regression case and a versioned change record. Do not submit private transcripts or credentials.

See [foundations and comparison](docs/foundations.md), [source ledger](SOURCES.json), [notices](THIRD_PARTY_NOTICES.md), and [changelog](CHANGELOG.md). Original project material is [MIT licensed](LICENSE). Installation, tool access and results vary by host; external publication always requires authorization for that destination.
