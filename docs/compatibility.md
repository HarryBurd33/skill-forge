# Compatibility and evidence boundaries

Skill Forge keeps one canonical folder, `skills/skill-forge`, and derives its self-contained prompt from it. Portability means shared instructions and file format; it does not guarantee identical tool access, behavior or quality across models.

## Operating systems and processors

The core is Markdown/JSON text with no OS-specific executable. Optional Python helpers use the standard library and require Python 3.9 or later. Use `python3` on typical macOS/Linux setups or `py -3`/`python` on Windows. Manual folder installation and prompt use require no Python. The setup guides include POSIX and PowerShell examples.

**Intel/x64 and ARM64 describe processors; macOS, Windows and Linux describe operating systems.** Install a host and Python compatible with your machine. Codex's [current source README](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/README.md) lists Intel Mac/Apple Silicon, x86_64/ARM64 Linux and a Windows installer. [Claude setup](https://code.claude.com/docs/en/setup) documents x64/ARM64 on supported OS versions. These are host support facts, not Skill Forge execution results on every combination.

| Surface | Evidence status | Boundary |
| --- | --- | --- |
| Agent Skills format | Supported by [the specification](https://agentskills.io/specification); repository validators check structure | Valid format does not prove behavior. |
| Codex installation/discovery | Supported by [official docs](https://learn.chatgpt.com/docs/build-skills); personal installation appears in the desktop catalog; native Codex CLI 0.163.0-alpha.10.2 discovered a v0.3.0 development project copy and produced a visible plan/draft | Selector UI and native Codex execution on Windows/Linux remain separate, unverified integrations. Installation is local, not account-wide. |
| Codex model behavior | Real evidence is release-specific; [v0.3.0 report](../evals/v0.3.0/REPORT.md) records the current comparison and native smoke check, and earlier reports retain previous results | A requested model role does not establish the executing model/build. Use recorded environment details. |
| Claude Code | Local paths/invocation supported by [official docs](https://code.claude.com/docs/en/skills); native execution unverified here | Helper success does not establish a Claude model run; personal local installation does not automatically reach cloud/Cowork. |
| Portable prompt | Generated from canonical files; resource completeness/drift checks are available | Use a capable model; no universal performance promise. See [other LLMs](other-llms.md). |
| Python helpers across OSes | [Six hosted jobs passed](https://github.com/HarryBurd33/skill-forge/actions/runs/39344381465) for Windows and Ubuntu on Python 3.9/3.13, Intel macOS on 3.9 and ARM macOS on 3.13 | These are actual helper, packaging and temporary-install checks. Native LLM execution is separate; other OS/CPU/Python combinations need their own evidence. |
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

Visible job logs record Windows build 10.0.26100 on AMD64/Python 3.9.13; Linux 6.17 x86_64/Python 3.13.16; macOS 15.7.9 x86_64/Python 3.9.25; and macOS 26.6.2 arm64/Python 3.13.16. The six-cell job results include the second Windows/Linux Python versions. These observations establish those helper executions, not every operating-system version or native Claude/model combination.

On POSIX, the helper requests owner-only state-directory mode. On Windows, directory access inherits Windows ACLs; `chmod(0700)` is not an ACL privacy guarantee. Keep private state under your user profile outside repositories and use an appropriately private parent directory.
