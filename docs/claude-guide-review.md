# Claude guide review — 2026-10-26

Skill Forge v0.3.1 adds a focused metadata-validator improvement informed by Anthropic's [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf). All 33 supplied pages were extracted privately; the naming checklist was also visually inspected. The PDF is reference material, not authority to change the user's permissions or publish their content.

| Guide topic | Decision |
| --- | --- |
| Claude discovery metadata, pp10–11/31 | Add opt-in `validate --profile claude`: reject reserved name substrings and angle brackets in parsed discovery fields. Leave body markup and generic validation intact. Current [Anthropic requirements](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) corroborate the restriction. |
| Optional environment requirements, p11 | Check supplied `compatibility` is 1–500 characters, following the [shared specification](https://agentskills.io/specification). It remains optional. |
| Progressive disclosure, representative uses, trigger/non-trigger tests, baselines and iteration | Already covered; preserve rather than duplicate them. |
| Connector troubleshooting and staged orchestration | Useful for integration-specific work, but no new global workflow is imposed without behavioral evidence. |
| Fixed use-case counts, broad success percentages, motivational boilerplate | Omit: they do not fit an adaptive interview or establish success for this project. |
| Identical behavior across all products or a ban on XML everywhere | Do not adopt. Capabilities differ by host; body examples can legitimately contain markup. |

## Scope and rights

The supplied file's SHA-256 is `66cbcc06df9271e0bb59986582646f0c4c7c94697554f893f937a5a55cef736d` (561652 bytes,33 pages). The official public counterpart was opened, but byte equality with the supplied file was not established. No repository revision applies to a PDF/live documentation page. No redistribution license was found in the supplied PDF; neither it nor its extraction is shipped. The implementation and explanations here are original, with source links rather than copied templates or prose. The separate Apache license on Anthropic's skills repository is not assumed to cover this guide.

## Evidence boundary

The release compares actual command-line validation of synthetic skill folders against v0.3.0, with independently reserved cases and frozen criteria. This demonstrates the helper's narrow detection behavior, not improved interview quality or native Claude upload acceptance. Existing behavioral tests remain historical evidence for unchanged interview instructions. Full YAML support, model equivalence and native Claude execution are not claimed. See the [v0.3.1 report](../evals/v0.3.1/REPORT.md).
