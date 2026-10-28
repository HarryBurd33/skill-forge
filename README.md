# Skill Forge

**Version 0.4.1.** Adds an opt-in recovery runner for the verified macOS SwiftBridging compiler conflict that blocked REA JavaScript analysis. The core skill-building workflows and bundled Anatomy renderer remain available. See [the recovery guide](skills/skill-forge/references/rea-macos.md), [validation report](evals/v0.4.1/REPORT.md) and [integration scope](docs/integrations.md).


**Turn a useful idea into a reusable AI skill—and improve it with evidence.**

Describe a workflow in ordinary language, or say **“Based on this conversation, build me a skill.”** Skill Forge extracts what is settled, asks and challenges what matters, shows an implementation spec and verification plan, then builds and checks an installable skill. It also improves existing skills and evaluates improvements to its own interview and tools.

- Simple, clear ideas can go straight to a draft. Complex uncertainty gets deeper questions.
- Refine through focused questions, examples and constructive challenge until material gaps close. Say **quick**, **thorough**, **expert challenge**, **draft now**, **skip**, or **resume** to control the pace.
- Choose how to receive the skill itself: local Markdown, an installable folder/ZIP, a GitHub repository, or another destination. Settled choices are remembered.
- Before implementation, [Skill Finder](docs/skill-finder.md) delegates a bounded search for useful foundations, inspecting actual source, licenses and fit. It has honest fallbacks when browsing or subagents are unavailable.
- Learn from complete source files using ordinary file tools; use the optional [REA adapter](docs/integrations.md#learn-a-workflow-from-source-or-a-shipped-artifact) for shipped-artifact or runtime-dependent questions. Missing providers leave explicit evidence gaps.
- Automatically include the real [Anatomy renderer and notices](docs/integrations.md#add-a-physical-explanation-when-it-helps) when the generated skill needs an explanatory physical mechanism. Text/CSV-only work, ordinary flowcharts and explicit opt-outs skip it.
- See what will be built and how it will be checked before implementation. Say **review first** to pause for edits; the pause is optional, so **draft now** and already-authorized work can continue after the plan.
- Available useful subagents automatically help construct resources, review the result or run independent checks. Small tasks can stay in one context; unavailable tools are disclosed.
- Successful updates are applied automatically after predefined checks, with history and rollback. Failed or untested candidates stay separate.
- Private preferences and conversations stay outside published source by default.

## Install and start using Skill Forge

You need access to Codex, Claude Code, or another capable chat model. Skill Forge itself needs no paid API or custom service. Python is **optional**: only the validation, resource-attachment, packaging and managed-update helpers require Python 3.9 or newer. Node.js 20.10+ is optional and used only when building the bundled Anatomy example; a modern browser is needed to view and verify the interactive output. REA is a separate optional tool with its own runtime/provider requirements. Installing Forge does not install Node, REA or a browser.

| Where you work | Start |
| --- | --- |
| Codex | [Install for yourself or a project](docs/codex.md) |
| Claude Code | [Install for yourself or a project](docs/claude-code.md) |
| Another capable chat model | Paste or upload [the self-contained prompt](portable/skill-forge-prompt.md), then describe your idea |

Choose the skill ZIP for Codex/Claude Code, or the portable ZIP for another capable chat model. Keep the full skill folder when executable resources are needed.

### Codex or Claude Code: install without commands

1. Download [skill-forge-v0.4.1.zip](https://github.com/HarryBurd33/skill-forge/releases/download/v0.4.1/skill-forge-v0.4.1.zip) and extract it.
2. Copy the **complete `skill-forge` folder**, including its references, scripts, templates, resources and nested adapters, to **one** destination below. Create missing parent folders. Copying only `SKILL.md` is incomplete.
3. Open a new session in your host and invoke Skill Forge as shown below. If it does not appear, restart the host.

| Host and scope | macOS / Linux destination | Windows destination |
| --- | --- | --- |
| Codex, personal | `~/.agents/skills/skill-forge` | `%USERPROFILE%/.agents/skills/skill-forge` |
| Codex, one project | `<project>/.agents/skills/skill-forge` | `<project>/.agents/skills/skill-forge` |
| Claude Code, personal | `~/.claude/skills/skill-forge` | `%USERPROFILE%/.claude/skills/skill-forge` |
| Claude Code, one project | `<project>/.claude/skills/skill-forge` | `<project>/.claude/skills/skill-forge` |

`~` and `%USERPROFILE%` mean your home folder; replace `<project>` with your project's folder. On Windows you can paste `%USERPROFILE%` into File Explorer's address bar; native backslashes also work. Personal means your local user installation; project means only the selected repository. Avoid installing the same named skill at multiple scopes.

In **Codex**, select Skill Forge or type:

```text
$skill-forge Create a skill that turns rough meeting notes into action items.
Keep unknown owners and dates explicit. Use your judgment. Draft now.
```

In **Claude Code**, type the same request starting with `/skill-forge` instead of `$skill-forge`.

The [Codex guide](docs/codex.md) and [Claude Code guide](docs/claude-code.md) also include optional managed installation commands for macOS/Linux and Windows PowerShell, updating, removal and troubleshooting. For a manual update, back up and compare your existing folder before replacing it. Managed updates refuse customized copies rather than overwrite them.

### Other capable LLMs: use the portable prompt

1. Download [skill-forge-portable-v0.4.1.zip](https://github.com/HarryBurd33/skill-forge/releases/download/v0.4.1/skill-forge-portable-v0.4.1.zip) and extract it.
2. Upload **`skill-forge-prompt.md`**, or paste its complete contents into a new conversation. Use the full bundle, not just the short installed `SKILL.md`. Choose a model with enough context for the entire file.
3. Say: **“Use Skill Forge to build a skill for [my repeated workflow].”** Supply relevant context and references. With no file tools, it returns complete file contents for you to save.

No installation, Python or operating-system-specific command is needed for this route. Without browsing, subagents or execution, those parts remain unavailable and must be reported honestly. See [the plain-chat guide](docs/other-llms.md).

The instructions work as text across operating systems. Installation guides include **Windows PowerShell** and **macOS/Linux** commands plus manual whole-folder copying without Python. Intel/x64 and ARM are processor architectures; choose a host/Python version available for your machine. See [compatibility](docs/compatibility.md) for actual tested OS/CPU combinations and the difference between helper tests and native model execution. Local installation does not install the skill on every device or cloud chat account.

Download the [latest release](https://github.com/HarryBurd33/skill-forge/releases/latest): the **skill ZIP** contains an installable `skill-forge/` folder; the **portable ZIP** contains the standalone prompt and license; the **source ZIP** contains examples, tests and documentation. See [compatibility](docs/compatibility.md) for what was actually tested.

### What you receive on first use

After installation, try:

> Use Skill Forge to build a skill that turns my meeting notes into action items. Keep unknown owners and dates explicit. Return a Markdown table. Draft now.

Codex users can explicitly start with `$skill-forge`; Claude Code users with `/skill-forge`. Plain-chat users first supply the portable prompt. Your generated skill will include its own `SKILL.md`, any needed supporting files, sample requests, installation steps and a short validation report. It does **not** need Skill Forge to run.

For a plan you want to edit first:

> Based on this conversation, build me a reusable skill. Preserve my final corrections and use synthetic examples. Show the implementation spec and how you will verify it. Review first; wait before building.

For a project, supply the relevant files or accessible authorized project context. Skill Forge states what it actually read; it cannot see hidden chats or an entire project merely because you name one. See [conversation/project intake](skills/skill-forge/references/context-intake.md) and [other LLMs](docs/other-llms.md).

**Review behavior:** the plan and concrete checks appear before the artifact. They can be followed by implementation in the same response. Say **“review first; wait before building”** if you want a separate turn to edit the plan.

For the first result, check one realistic input and a failure case. Tell the builder what was wrong or changed:

> Improve this skill: it assigns a speaker as the owner even when nobody accepted the task. Keep its table format and meeting order.

Or improve the builder:

> Evaluate a Skill Forge improvement: users who ask for a spreadsheet are not finding the output-destination question. Compare retrieval before and after, preserve the prior version, and adopt only if checks pass.

## Remaining limitations and what was actually tested

The v0.4.0 [model comparison](evals/v0.4.0/REPORT.md) passed all six candidate scenarios, including two held-out cases. Local helper checks recorded42 passes and1 Windows-only skip. The maintainer reported the required HTML layout, native keyboard and reduced-motion checks working; independent review accepted that manual evidence. Browser/version remains unknown and automated browser coverage is not claimed. Historical model/host results below apply to their named earlier versions; they are not a pass for the new behavior cases.

Skill Forge implements the requested workflow; it does not guarantee perfect skills or identical behavior on every model. Read these boundaries before relying on it:

| Area | Current capability and limit |
| --- | --- |
| Host and operating-system coverage | Native Codex CLI 0.164.0 was tested on macOS ARM. Six hosted Python/helper and packaging jobs passed across Windows, Linux, Intel macOS and ARM macOS. Native Claude Code, native Codex model runs on Windows/Linux, and other model families remain unverified. Documented installation support is distinct from executed model testing. |
| Tools and permissions | Installation grants no file, browsing, execution, subagent or GitHub access. Useful available subagents are launched; when unavailable, the parent works directly and discloses that limitation. Without execution, planned tests remain unexecuted. |
| REA and Anatomy | Readable source uses normal inspection; shipped artifacts use compatible optional REA tools. ZIP inspection was exercised; v0.4.1 adds guarded recovery for the observed macOS compiler conflict, with actual static semantic checks documented in its report. Runtime behavior remains unproved. Anatomy includes the basic SVG/HTML slice, not the full upstream advanced toolkit. Plain-chat text does not contain its executable assets. See [integration limits](docs/integrations.md). |
| Research and reuse | Skill Finder performs a bounded, relevant search, not an exhaustive search of every service. Hugging Face is searched when useful. No suitable or properly licensed foundation means original work or a documented gap, not forced copying. |
| Interview depth | Questioning continues while material uncertainty remains, within your pace and effort limits. It stops for useful closure or your draft/stop instruction; “maximum possible refinement” is not a measurable guarantee. |
| Automatic updates | Adoption needs predefined checks, relevant regressions, demonstrated benefit and a writable target. Failed, inconclusive or unavailable required checks preserve the prior version. The helper validates hashes and supplied evidence records; it does not independently run a model evaluator or certify its judgment. |
| Memory and installation scope | Continuity comes from saved files or a handoff, not retraining or guaranteed memory between chats. Save the private handoff and supply it when resuming. Local installation does not synchronize other devices, accounts or cloud environments. |
| Privacy and publication | Keep credentials, raw transcripts and personal preferences outside public source. Publishing a generated skill requires authorization and working access to that destination; improving locally does not grant upstream write permission. Private storage is not automatically encrypted; Windows privacy depends on the parent folder's access controls. |
| Evaluation strength | The v0.3.0 evaluation passed all 21 original scenarios / 84 required conditions and 15 supplemental items. Eight historical baseline pairs used different recorded model settings; the full comparison is descriptive, not a perfectly controlled causal benchmark or proof of universal reliability. |

The earlier v0.3.0 release also passed actual rollback/customization checks and clean first-use checks from downloaded public packages. See [the validation report](evals/v0.3.0/REPORT.md), [compatibility record](docs/compatibility.md), [requirements map](REQUIREMENTS.md) and [release verification receipt](https://github.com/HarryBurd33/skill-forge/releases/tag/v0.3.0) for evidence and qualifications.

You can combine Skill Forge with Codex's built-in skill creator for authoring or review. Forge does not silently modify the vendor-managed creator; see [how they work together](docs/foundations.md#combining-skill-forge-with-codexs-skill-creator).

## What happens during a session

The builder maintains a compact brief of confirmed needs, proposed defaults, assumptions, examples, acceptance checks, open questions, skill delivery, source coverage and research status. It inspects available facts before asking you. Each answer or example can reveal the next dependent question. A coverage pass checks consequential gaps and weak assumptions without a fixed questionnaire. The skill’s own delivery choice is separate from the document, spreadsheet or other output it will later produce. Repairs preserve an existing skill’s delivery context unless you ask to change it. Without file access, the builder returns complete prior and replacement contents for you to save; unavailable execution prevents adoption, not drafting the repair.

Once the brief is ready, Skill Finder sends a researcher a sanitized task. It searches GitHub, Hugging Face when relevant, and other primary resources; checks actual files, revision and reuse rights; and recommends a foundation or original implementation. Findings can reopen a specific design decision. Research is bounded, can be declined, and does not authorize installing fetched code or publishing your materials.

Before building, it presents an [implementation spec](skills/skill-forge/templates/implementation-spec.md): intended behavior, files/dependencies, assumptions, work and delegated roles, delivery/privacy, concrete acceptance inputs, expected outcomes, failure conditions and unavailable checks. Review pauses are optional: **review first** or **spec only** waits for you; otherwise authorized work proceeds. **Draft now** shows a compact plan and draft in the same response. If delivery is undecided, it returns provisional saveable text and leaves that choice for finalization without appending another required question. User edits update the spec and affected checks before building. Supplied acceptance examples keep their exact inputs and expected results; supporting resources receive their own checks against the final behavior.

For useful separable work it automatically launches available constructors, resource authors, reviewers or evaluators with bounded tasks and clear file ownership. It waits for results and integrates them; a promise that a subagent or test ran is not evidence. Tools, permissions and model capability still determine what can actually execute.

When a session pauses, save its private record or copy its handoff into the next chat. Improvement means revised files and recorded evidence; it does not retrain a model or promise memory across unrelated conversations.

[Worked examples](examples/README.md) cover research and writing, an adaptive prompt builder, a planner handling an exam, and a correction to an existing skill. The public inputs are fictional. Authored demonstrations are labeled separately from executed evaluation results: [v0.1.0](evals/REPORT.md), [v0.2.0](evals/v0.2.0/REPORT.md), and [v0.3.0](evals/v0.3.0/REPORT.md).

## Optional REA and Anatomy resources

The [integration guide](docs/integrations.md) explains source versus shipped-artifact evidence, automatic selection for physical explainers, the exact bundled file slice, optional dependencies and helper commands. Generated skills receive their own resources and work without Forge. An adapter is workflow guidance; it is not proof that a tool is connected or that an analysis, render or browser check ran.

## Claude metadata checks in v0.3.1

The [Claude guide review](docs/claude-guide-review.md) identified a narrow helper gap. Optional `compatibility` values are now checked for 1–500 characters; omit the field when no environment requirements apply. For Claude-targeted skills, use the opt-in profile from a source checkout:

```sh
python3 skills/skill-forge/scripts/forge.py validate /path/to/my-skill --profile claude
```

On Windows use `py -3` instead of `python3`. The profile checks reserved names and discovery-description angle brackets; body XML/HTML is allowed. Generic validation remains the default. This checks a supported metadata subset, not full YAML validity, native Claude upload success or model quality.

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

The canonical builder lives in `skills/skill-forge/`. The portable prompt is generated from it, so edits cannot quietly drift. Its text-only form does not embed the Anatomy renderer files; an explanatory visual target needs the complete folder assets or an honest pending asset-copy step. See [plain-chat limits](docs/other-llms.md#optional-rea-and-anatomy-resources). Managed installations refuse to overwrite customized copies; keep personal settings outside the shared skill.

## Contribute an improvement

[Report a failure or propose a question](CONTRIBUTING.md). A helpful contribution includes a realistic input, expected behavior, actual failure, and why the proposed change helps. Search the question library first: fewer useful questions beat more repetitive questions. Accepted changes gain a regression case and a versioned change record. Do not submit private transcripts or credentials.

See [foundations and comparison](docs/foundations.md), [source ledger](SOURCES.json), [notices](THIRD_PARTY_NOTICES.md), and [changelog](CHANGELOG.md). Original project material is [MIT licensed](LICENSE). Installation, tool access and results vary by host; external publication always requires authorization for that destination.

The v0.3.0 checks passed all 21 original scenarios (84 required conditions), all 15 supplemental interview items, and the navigation/package checks. A fresh Codex CLI 0.164.0 invocation discovered the installed skill and returned a standalone draft. Historical baseline/model limits and untested native hosts are documented in the validation report.

Track requested capabilities in [REQUIREMENTS.md](REQUIREMENTS.md), current work in [HANDOFF.md](HANDOFF.md), and the project usage policy in [MAINTENANCE.md](MAINTENANCE.md).

### REA JavaScript compiler recovery on macOS

If REA reports `redefinition of module 'SwiftBridging'`, use the [guarded macOS recovery guide](skills/skill-forge/references/rea-macos.md). The opt-in Python runner checks the actual diagnostic and matching module definitions, then supplies a temporary compiler overlay only to the requested command. It does not edit Apple files, disable REA ownership checks, install REA or repair every Swift failure. Existing custom compiler/SDK selections are refused. Normal host process inspection is still required; a sandbox may deny it. Failed or interrupted runs retain temporary state when native descendant cleanup is uncertain.

The executable runner is included in the full skill/source ZIP, not the portable text bundle. Other operating systems keep their ordinary REA setup; this specific workaround refuses non-macOS systems. See [v0.4.1 evidence and limits](evals/v0.4.1/REPORT.md).
