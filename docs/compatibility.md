# Compatibility and evidence boundaries

Skill Forge keeps one canonical folder, `skills/skill-forge`, and derives its self-contained prompt from it. Portability means shared instructions and file format; it does not guarantee identical tool access, behavior or quality across models.

## Operating systems and processors

The core is Markdown/JSON text with no OS-specific executable. Optional Python helpers use the standard library and require Python 3.9 or later. Use `python3` on typical macOS/Linux setups or `py -3`/`python` on Windows. Manual folder installation and prompt use require no Python. The setup guides include POSIX and PowerShell examples.

**Intel/x64 and ARM64 describe processors; macOS, Windows and Linux describe operating systems.** Install a host and Python compatible with your machine. Codex's [current source README](https://github.com/openai/codex/blob/8c076942cb70fba8e5c4732c23f1faabc4aed484/README.md) lists Intel Mac/Apple Silicon, x86_64/ARM64 Linux and a Windows installer. [Claude setup](https://code.claude.com/docs/en/setup) documents x64/ARM64 on supported OS versions. These are host support facts, not Skill Forge execution results on every combination.

| Surface | Evidence status | Boundary |
| --- | --- | --- |
| Agent Skills format | Supported by [the specification](https://agentskills.io/specification); repository validators check structure | Valid format does not prove behavior. |
| Codex installation/discovery | Supported by [official docs](https://learn.chatgpt.com/docs/build-skills); personal Skill Forge and nested Finder appeared in this development host's skill catalog | Native selector UI, project discovery and each OS combination require their own checks. Installation is local, not account-wide. |
| Codex model behavior | Real evidence is release-specific; [v0.2.0 report](../evals/v0.2.0/REPORT.md) retains earlier results | A requested model role does not establish the executing model/build. Use recorded environment details. |
| Claude Code | Local paths/invocation supported by [official docs](https://code.claude.com/docs/en/skills); native execution unverified here | Helper success does not establish a Claude model run; personal local installation does not automatically reach cloud/Cowork. |
| Portable prompt | Generated from canonical files; resource completeness/drift checks are available | Use a capable model; no universal performance promise. See [other LLMs](other-llms.md). |
| Python helpers across OSes | Prior evidence records macOS development execution; Windows/Linux/macOS CI is configured for Python 3.9 and 3.13 | Configuration is not a passed check. Release evidence must identify actual completed jobs, OS/CPU and runtime. Native LLM execution is separate. |
| Other OS, CPU or models | Unverified unless release evidence explicitly records them | Test a representative workflow before relying on a combination. |

Host documentation was rechecked on **2026-10-18**. [Codex](codex.md) and [Claude Code](claude-code.md) guides cover personal/project install, invocation, updates and removal. One local copy does not install on every device or grant another account access.

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
