# Compatibility and evidence boundaries

Portability means shared instructions and file format, not identical behavior or tool access. This release uses one canonical directory, `skills/skill-forge`, with no mandatory host-specific execution syntax. The prompt export is derived from that source. Installation guides were checked against official documentation on **2026-10-15**, with the Codex personal path reconfirmed on **2026-10-17**.

| Surface | Status | What the status means |
| --- | --- | --- |
| Agent Skills folder and common metadata | Supported by [the specification](https://agentskills.io/specification); structural checks recorded in [the report](../evals/v0.2.0/REPORT.md) | A valid bundle is usable by compatible hosts; validation cannot guarantee a model's behavior. |
| Codex local installation/discovery | Supported by [official documentation](https://learn.chatgpt.com/docs/build-skills) | The v0.1.0 personal installation appeared in the next-turn Codex skill catalog on 2026-10-17. Updated-file validation is a filesystem check; selector UI and native project discovery were not exercised end to end. |
| Codex model context | Real execution evidence only as enumerated in [the report](../evals/v0.2.0/REPORT.md) | Development host: Codex desktop, GPT-6-based agent context. The exact model identifier and host build were not exposed; the user's requested role is not runtime-version evidence. |
| Claude Code local installation/invocation | Supported by [official documentation](https://code.claude.com/docs/en/skills); native runtime unverified | The same skill folder is documented to load. No Claude model or native CLI run was performed here. |
| Self-contained prompt bundle | Generated from canonical source; checks in [the report](../evals/v0.2.0/REPORT.md) | Paste/upload it to a capable model. Tool-free reasoning examples do not establish universal support across chat products. |
| Other models and operating systems | Unverified except where explicitly recorded | Follow the common format and test a representative task before depending on it. Shell examples in the setup guides use macOS/Linux syntax. |
| Python helpers | Python 3.9.6 observed in the development environment | Standard-library implementation; exact executed checks and limitations belong in the release report. No Python is needed for the core conversation. |

## Capabilities are separate from installation

| Capability | If available | If unavailable |
| --- | --- | --- |
| Read local files | Inspect the actual skill, examples, and license. | Ask for file contents with filenames; treat an inaccessible link as unverified. |
| Browse | Verify current sources and provenance. | Use supplied excerpts and identify missing verification. Never invent citations. |
| Execute scripts | Run validators, examples, and relevant deterministic tests. | Return runnable instructions and label checks unexecuted. |
| Subagents | Delegate Skill Finder from a sanitized refined brief; wait for its report before integration. | Perform bounded direct research when browsing exists, or return a pending research task. |
| Independent model evaluation | Compare frozen cases in separate contexts with the same tools/model/settings. | Label same-context review as a simulation or limited self-review; do not claim an independent benchmark. |
| Save files | Persist brief, candidate, evidence, snapshot, and accepted change. | Return exact file contents and a compact handoff for the user to save. |
| Publish to GitHub | Inspect the selected public material, then use an authorized destination and authenticated access. | Deliver local artifacts plus the smallest remaining publication step. |

A model with no tools can still conduct the interview and produce usable file contents. It cannot actually install files, inspect remote licenses, execute tests, persist changes, or publish a release. Required tests that cannot run keep a behavioral update as a candidate; narration is not an adoption pass.

Improvement persists through revised files and explicit session records. It is not model retraining, a guarantee of memory in another chat, or a background process. Private preferences and raw evidence belong outside publishable source. See [the core portability reference](../skills/skill-forge/references/portability.md) for the tool-free handoff.
