# Compatibility and evidence boundaries

Skill Forge keeps one canonical folder, `skills/skill-forge`, and derives its self-contained prompt from it. Portability means shared instructions and file format; it does not guarantee identical tool access, behavior or quality across models.

## Operating systems and processors

The core is Markdown/JSON text with no OS-specific executable. Optional Python helpers use the standard library and require Python 3.9 or later. Use `python3` on typical macOS/Linux setups or `py -3`/`python` on Windows. Manual folder installation and prompt use require no Python. The setup guides include POSIX and PowerShell examples.

**Intel/x64 and ARM64 describe processors; macOS, Windows and Linux describe operating systems.** Install a host and Python compatible with your machine. Codex's [current source README](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/README.md) lists Intel Mac/Apple Silicon, x86_64/ARM64 Linux and a Windows installer. [Claude setup](https://code.claude.com/docs/en/setup) documents x64/ARM64 on supported OS versions. These are host support facts, not Skill Forge execution results on every combination.

| Surface | Evidence status | Boundary |
| --- | --- | --- |
| Agent Skills format | Supported by [the specification](https://agentskills.io/specification); repository validators check structure | Valid format does not prove behavior. |
| Codex installation/discovery | Supported by [official docs](https://learn.chatgpt.com/docs/build-skills); personal installation appears in the desktop catalog; native CodexCLI0.164.0 discovered the final v0.3.0 personal copy through actual host injection and produced a visible plan/draft with Sol/Medium | Selector UI and native Codex execution on Windows/Linux remain separate, unverified integrations. Installation is local, not account-wide. |
| Codex model behavior | Real evidence is release-specific; [v0.3.0 report](../evals/v0.3.0/REPORT.md) records the completed comparison, final-source native smoke and separate supplemental checks, and earlier reports retain previous results | A requested model role does not establish the executing model/build. Use recorded environment details. |
| Claude Code | Local paths/invocation supported by [official docs](https://code.claude.com/docs/en/skills); native execution unverified here | Helper success does not establish a Claude model run; personal local installation does not automatically reach cloud/Cowork. |
| Portable prompt | Generated from canonical files; resource completeness/drift checks are available | Use a capable model; no universal performance promise. See [other LLMs](other-llms.md). |
| Python helpers across OSes | [Six candidate 9 hosted jobs passed](https://github.com/HarryBurd33/skill-forge/actions/runs/40211274980) for Windows and Ubuntu on Python 3.9/3.13, Intel macOS on 3.9 and ARM macOS on 3.13 | These are actual helper, packaging and temporary-install checks at commit `08fde55`. Native LLM execution is separate; other OS/CPU/Python combinations need their own evidence. |
| Other OS, CPU or models | Unverified unless release evidence explicitly records them | Test a representative workflow before relying on a combination. |

Core installation/discovery documentation was rechecked on **2026-10-21**. [Codex](codex.md) and [Claude Code](claude-code.md) guides cover personal/project install, invocation, updates and removal. One local copy does not install on every device or grant another account access.

## Capabilities are separate from installation

| Capability | If available | If unavailable |
| --- | --- | --- |
| Conversation/project context | Read supplied/authorized material and extract settled workflow and corrections. | Request missing consequential context or a handoff; never claim unseen chat or whole-project access. |
| Read files | Inspect actual skills, examples, paths and licenses. | Ask for contents with filenames; inaccessible links remain unverified. |
| Browse | Verify current primary resources and provenance. | Use supplied material; identify unverified sources/licenses. |
| Subagents | Automatically delegate useful bounded research, independent build work, review or evaluation; parent integrates. | Say no launch tool is available and work directly. Never invent workers or label self-review independent. |
| Execute checks | Run predefined validators, examples and relevant tests. | Supply runnable checks and label them unexecuted; preserve candidates lacking required adoption evidence. |
| Independent evaluation | Compare frozen cases with a baseline in separate contexts. | Disclose limited self-review or simulation, not an independent benchmark. |
| Save files | Persist brief, spec, review choice, candidate, evidence, snapshot and accepted version. | Return complete file contents plus a compact handoff. |
| Publish | Inspect public selection and use actual authenticated access to an authorized destination. | Deliver artifacts plus the remaining publication step; never invent a release. |

Before building, Skill Forge shows its implementation spec and plans checks. Users can request a review pause; otherwise authorized work continues. Workers cannot bypass that boundary or expand publication permission. Tool, account and platform restrictions still apply.

Improvement persists through revised files and explicit evidence/session records, not model retraining or guaranteed memory across chats. A helper verifies hashes, snapshots and evidence structure; it cannot prove an evaluator truthful or infer quality from formatting alone. Failed, inconclusive or unavailable required checks leave the prior version active. Keep private preferences and raw transcripts outside public source. Installation creates no background automation.

## Actual hosted runtime samples — 2026-10-18

On 2026-10-25, [candidate 9 platform checks](../evals/v0.3.0/round9-platform-checks.json) independently confirmed successful unit tests, format validation, portable drift checks and package/temporary-install validation in all six jobs at `08fde55b9293d0fab95e3ad7b329fd502f8be937`. The older runtime samples below remain historical; exact current OS build and patch-level Python versions were not re-read from job logs.

Visible job logs record Windows build 10.0.26100 on AMD64/Python 3.9.13; Linux 6.17 x86_64/Python 3.13.16; macOS 15.7.9 x86_64/Python 3.9.25; and macOS 26.6.2 arm64/Python 3.13.16. The six-cell job results include the second Windows/Linux Python versions. These observations establish those helper executions, not every operating-system version or native Claude/model combination.

On POSIX, the helper requests owner-only state-directory mode. On Windows, directory access inherits Windows ACLs; `chmod(0700)` is not an ACL privacy guarantee. Keep private state under your user profile outside repositories and use an appropriately private parent directory.

Final source86daffd3… adds only reference navigation to the behavior-tested source. The [final native receipt](../evals/v0.3.0/native-final-smoke.json) records a read-only CLI invocation using default per-invocation configuration, with normal authentication and rules. It does not establish behavior under every user configuration.

## v0.3.1 metadata-helper scope

The opt-in Claude profile checks discovery metadata against documented restrictions; it does not establish native Claude upload acceptance. The current comparison ran26actual CLI cases, with30local unit passes and1Windows-only skip. [The v0.3.1 report](../evals/v0.3.1/REPORT.md) records frozen inputs and limits; earlier model/host evidence remains historical.

## v0.4.0 candidate integrations — 2026-10-27

The candidate helper run recorded **38 passes and one Windows-only skip** on the local macOS host. This is local helper evidence; it is not a new six-platform CI run or a native Claude/other-model result. New checks cover complete resource copying, relocation, unchanged repeats, customized/partial conflicts, symlink/path refusal, injected copy/publication failures and exclusive publication. The original mechanism builds with the actual renderer; SVG parsing and model/inline-script checks ran. Browser appearance, keyboard and reduced-motion checks are still pending in this documentation snapshot.

The basic Anatomy slice uses optional Node.js **20.10+** and Node built-in ESM modules, with no npm dependencies. Attachment uses Python only. Generated HTML embeds the renderer, CSS and model, so viewing it needs a modern browser and no Forge installation or server. Advanced upstream rendering modules and verification scripts are not included. See [the file/scope map](integrations.md#what-is-included).

REA is not bundled as an executable service. A real `rea-agents` **6.8.0** package was exercised with an isolated Node **24.22.1** runtime: version/help and ZIP artifact inspection succeeded. A JavaScript static-analysis attempt failed during macOS process-helper compilation because of a **SwiftBridging module redefinition**. That failure does not establish working JavaScript analysis, successful provider setup or runtime observation of the target. Its unresolved analysis requirements remain explicit. The isolated package environment changed no system Node or global registration.

The reviewed REA package declares Node `^22.23.4 || ^24.22.1 || >=26.12.1`; this differs from the basic Anatomy example's minimum. Individual REA providers and operating systems have separate prerequisites. A source revision, CLI version or successful ZIP inspection does not prove all providers work. No new installation, native-host or release claim follows from these candidate checks.
