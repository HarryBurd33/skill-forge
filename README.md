# Skill Forge

> **Development branch: v0.3.0 is not released.** Candidate 8 was rejected automatically after a required verification-planning failure; candidate 7 also failed. Use [stable v0.2.0](https://github.com/HarryBurd33/skill-forge/tree/main) for installation. The instructions below describe the proposed behavior; see the [evaluation report](evals/v0.3.0/REPORT.md) for actual results and limits.

**Turn a useful idea into a reusable AI skill—and improve it with evidence.**

Describe a workflow in ordinary language, or say **“Based on this conversation, build me a skill.”** Skill Forge extracts what is settled, asks and challenges what matters, shows an implementation spec and verification plan, then builds and checks an installable skill. It also improves existing skills and evaluates improvements to its own interview and tools.

- Simple, clear ideas can go straight to a draft. Complex uncertainty gets deeper questions.
- Refine through focused questions, examples and constructive challenge until material gaps close. Say **quick**, **thorough**, **expert challenge**, **draft now**, **skip**, or **resume** to control the pace.
- Choose how to receive the skill itself: local Markdown, an installable folder/ZIP, a GitHub repository, or another destination. Settled choices are remembered.
- Before implementation, [Skill Finder](docs/skill-finder.md) delegates a bounded search for useful foundations, inspecting actual source, licenses and fit. It has honest fallbacks when browsing or subagents are unavailable.
- See what will be built and how it will be checked before implementation. Say **review first** to pause for edits; the pause is optional, so **draft now** and already-authorized work can continue after the plan.
- Available useful subagents automatically help construct resources, review the result or run independent checks. Small tasks can stay in one context; unavailable tools are disclosed.
- Successful updates are applied automatically after predefined checks, with history and rollback. Failed or untested candidates stay separate.
- Private preferences and conversations stay outside published source by default.

## Start here

Choose one route. No paid API or custom service is required for the core conversation.

| Where you work | Start |
| --- | --- |
| Codex | [Install for yourself or a project](docs/codex.md) |
| Claude Code | [Install for yourself or a project](docs/claude-code.md) |
| Another capable chat model | Paste or upload [the self-contained prompt](portable/skill-forge-prompt.md), then describe your idea |

The instructions work as text across operating systems. Installation guides include **Windows PowerShell** and **macOS/Linux** commands plus manual whole-folder copying without Python. Intel/x64 and ARM are processor architectures; choose a host/Python version available for your machine. See [compatibility](docs/compatibility.md) for actual tested OS/CPU combinations and the difference between helper tests and native model execution. Local installation does not install the skill on every device or cloud chat account.

Download the [latest release](https://github.com/HarryBurd33/skill-forge/releases/latest): the **skill ZIP** contains an installable `skill-forge/` folder; the **portable ZIP** contains the standalone prompt and license; the **source ZIP** contains examples, tests and documentation. See [compatibility](docs/compatibility.md) for what was actually tested.

After installation, try:

> Use Skill Forge to build a skill that turns my meeting notes into action items. Keep unknown owners and dates explicit. Return a Markdown table. Draft now.

Codex users can explicitly start with `$skill-forge`; Claude Code users with `/skill-forge`. Plain-chat users first supply the portable prompt. Your generated skill will include its own `SKILL.md`, any needed supporting files, sample requests, installation steps and a short validation report. It does **not** need Skill Forge to run.

For a plan you want to edit first:

> Based on this conversation, build me a reusable skill. Preserve my final corrections and use synthetic examples. Show the implementation spec and how you will verify it. Review first; wait before building.

For a project, supply the relevant files or accessible authorized project context. Skill Forge states what it actually read; it cannot see hidden chats or an entire project merely because you name one. See [conversation/project intake](skills/skill-forge/references/context-intake.md) and [other LLMs](docs/other-llms.md).

For the first result, check one realistic input and a failure case. Tell the builder what was wrong or changed:

> Improve this skill: it assigns a speaker as the owner even when nobody accepted the task. Keep its table format and meeting order.

Or improve the builder:

> Evaluate a Skill Forge improvement: users who ask for a spreadsheet are not finding the output-destination question. Compare retrieval before and after, preserve the prior version, and adopt only if checks pass.

## What happens during a session

The builder maintains a compact brief of confirmed needs, proposed defaults, assumptions, examples, acceptance checks, open questions, skill delivery, source coverage and research status. It inspects available facts before asking you. Each answer or example can reveal the next dependent question. A coverage pass checks consequential gaps and weak assumptions without a fixed questionnaire. The skill’s own delivery choice is separate from the document, spreadsheet or other output it will later produce. Repairs preserve an existing skill’s delivery context unless you ask to change it. Without file access, the builder returns complete prior and replacement contents for you to save; unavailable execution prevents adoption, not drafting the repair.

Once the brief is ready, Skill Finder sends a researcher a sanitized task. It searches GitHub, Hugging Face when relevant, and other primary resources; checks actual files, revision and reuse rights; and recommends a foundation or original implementation. Findings can reopen a specific design decision. Research is bounded, can be declined, and does not authorize installing fetched code or publishing your materials.

Before building, it presents an [implementation spec](skills/skill-forge/templates/implementation-spec.md): intended behavior, files/dependencies, assumptions, work and delegated roles, delivery/privacy, concrete acceptance inputs, expected outcomes, failure conditions and unavailable checks. Review pauses are optional: **review first** or **spec only** waits for you; otherwise authorized work proceeds. **Draft now** shows a compact plan and draft in the same response. If delivery is undecided, it returns provisional saveable text and leaves that choice for finalization without appending another required question. User edits update the spec and affected checks before building. Supplied acceptance examples keep their exact inputs and expected results; supporting resources receive their own checks against the final behavior.

For useful separable work it automatically launches available constructors, resource authors, reviewers or evaluators with bounded tasks and clear file ownership. It waits for results and integrates them; a promise that a subagent or test ran is not evidence. Tools, permissions and model capability still determine what can actually execute.

When a session pauses, save its private record or copy its handoff into the next chat. Improvement means revised files and recorded evidence; it does not retrain a model or promise memory across unrelated conversations.

[Worked examples](examples/README.md) cover research and writing, an adaptive prompt builder, a planner handling an exam, and a correction to an existing skill. The public inputs are fictional. Authored demonstrations are labeled separately from executed evaluation results: [v0.1.0](evals/REPORT.md), [v0.2.0](evals/v0.2.0/REPORT.md), and [v0.3.0](evals/v0.3.0/REPORT.md).

## Evidence and automatic updates

A candidate connects an observation to a hypothesis, patch and checks declared before testing. It must preserve existing acceptance criteria, pass relevant regressions and demonstrate its intended benefit against the prior version. Broader builder changes need held-out scenarios. Formatting alone cannot establish behavioral improvement.

The optional Python helper snapshots files, freezes the evaluator and criteria, checks hash-bound evidence, adopts passing candidates, and rolls back safely. It does not generate or authenticate model results. Use genuine execution artifacts and a trusted evaluator. Default improvement runs allow three candidates and a 30-minute wall-clock limit; failures or missing evidence preserve the active version. [Helper commands and evidence format](skills/skill-forge/references/helpers.md).

For local development with Python 3.9 or newer:

```sh
python3 skills/skill-forge/scripts/forge.py validate skills/skill-forge
python3 -m unittest discover -s tests -v
python3 skills/skill-forge/scripts/forge.py bundle --skill skills/skill-forge --output portable/skill-forge-prompt.md --check
```

On Windows, use `py` or `python` in place of `python3`; the installation guides include complete PowerShell examples. Before installing a generated skill, verify that its innermost folder matches the `name` in its metadata. Preserve versions under separate parents (`baseline/skill-name`, `candidate/skill-name`). See [the release report](evals/v0.3.0/REPORT.md) for exact results, earlier failure rechecks and remaining limits.

The canonical builder lives in `skills/skill-forge/`. The portable prompt is generated from it, so edits cannot quietly drift. Managed installations refuse to overwrite customized copies; keep personal settings outside the shared skill.

## Contribute an improvement

[Report a failure or propose a question](CONTRIBUTING.md). A helpful contribution includes a realistic input, expected behavior, actual failure, and why the proposed change helps. Search the question library first: fewer useful questions beat more repetitive questions. Accepted changes gain a regression case and a versioned change record. Do not submit private transcripts or credentials.

See [foundations and comparison](docs/foundations.md), [source ledger](SOURCES.json), [notices](THIRD_PARTY_NOTICES.md), and [changelog](CHANGELOG.md). Original project material is [MIT licensed](LICENSE). Installation, tool access and results vary by host; external publication always requires authorization for that destination.
