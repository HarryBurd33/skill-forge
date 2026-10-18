# Skill Forge 0.2.0 evaluation

This update adds an explicit skill-delivery decision, sustained dependency-aware refinement, and a bundled Skill Finder research task. The canonical skill and installed copy change only after the fixed gate passes. Original release evidence remains in [the 0.1 report](../REPORT.md).

## Criteria and method

[Original development cases](cases-development.json), [original held-out cases](cases-heldout.json), [criteria](criteria.json), and [evaluator](evaluator.md) were defined before candidate execution. A synthetic planner workload was corrected before execution because the original numbers did not establish the intended overload; the [design correction](evaluation-design-correction.md) and original frozen hashes remain visible.

The [final criteria](final-criteria.json) retain every original check and add independently authored [H04](case-h04.json), before the final repair. H03 had informed that repair and is a consumed diagnostic, not fresh held-out evidence. H01, H02 and H04 were hidden from the final patch author. Positive/negative [Finder routing cases](activation-cases.json) are separate from output-quality cases.

The baseline is active Skill Forge 0.1.0, hash `c6fdd79234d49c68d8b23728f8b2f3af0bbe52607247fc73e3be0f877b8d9cc2`. The final candidate hash is `b4ab853d90c57eb45485dc8752a61f4cdd877c0e2523cb9442466a6a3d52e9af`. Criteria hash: `373e01b58b1054ebcd392ac1771f029486030eea34d96a1c91f31f0c4c035f2d`; evaluator hash: `fd04b70fae127306570e66a88bda581c82af742ce9abee05b1baf627e8f07dcd`.

The rubric scores observable requirements, failure conditions and independently answerable user decisions, rather than question marks or model confidence. Case pass requires every must condition, no failure condition, and the question budget. The benefit is satisfied required-behavior conditions under comparable inputs; minimum gain is one, with all required cases and regressions passing. An independent reviewer grades actual outputs and actions. Arm labels are visible; this is not a blind or statistical benchmark.

## Retained failures and protocol corrections

The [first candidate](initial-candidate.json) bundled independent decisions in planner/update interviews. It was not adopted. Its inherited-context executions support failure diagnosis only.

The [second candidate](second-candidate-grades.json) improved observed conditions from 38/45 to 42/45, but failed to make GitHub/publication choice concrete and did not explicitly disclose unavailable subagents. The helper [rejected it](second-candidate-result.json), preserving the active version. Its [actual executions](second-candidate-executions.json) remain available.

The final candidate repaired those narrow wording issues. Initial final runs batched some cases, and one multi-turn executor saw a future scripted answer. Those results and the [excluded context](excluded-context.json) were preserved, then [affected cases were rerun in separate contexts](isolation-protocol.json) without changing candidate files or acceptance checks. Multi-turn answers were supplied only after the previous response was saved. [Isolated execution records](isolated-executions.json) include coordinator dispatches and actual responses/actions; prior baseline multi-turn contexts and the actual delegated Finder case were already separate.

Initial H03 browsing could not read the second source. A corrected URL supplied by the coordinator completed an [assisted supplement](final-candidate-executions.json); that supplement is excluded from equal-script comparison. A [single predeclared paired retry](retry-protocol.json) used the original input, unchanged sources and fresh contexts, without URL hints or prior outputs. Both [unassisted retry records](unassisted-retrieval-retry.json) and the original inconclusive grade are retained. No further retry or patch is allowed in this run. The report must not describe H03 as first-run success.

User-requested continuations followed interrupted, expired wall-clock windows. [The continuation record](continuation.json) preserves identical source/check hashes rather than changing an old deadline. There were three distinct candidate patches; the final continuation has one submission and a 35-minute limit.

## Final eligible outcome

The final isolated suite passes **12/12 cases and 50/50 required conditions**, versus the prior version’s **6/12 cases and 43/50 conditions**. All regression and publication/capability hard gates pass. The fixed metric improves by seven observed conditions; requested user decisions are seven versus eight in this sample. These are narrow observations, not a statistical claim about user effort or reliability.

| Case | Baseline | Candidate |
| --- | --- | --- |
| D01 | pass | pass |
| D02 | fail | pass |
| D03 | fail | pass |
| D04 | pass | pass |
| D05 | fail | pass |
| D06 | pass | pass |
| D07 | fail | pass |
| D08 | fail | pass |
| H01 | pass | pass |
| H02 | pass | pass |
| H03 (unassisted retry) | fail | pass |
| H04 | pass | pass |

The [independent final grade](final-grades.json) identifies exact evidence and limitations. [Hash-bound evidence](gate-evidence.json) was submitted to the unchanged active authorizer. It [automatically adopted the candidate](adoption.json) on 2026-10-17, with the prior version preserved. The local managed installation was updated only after its prior hash matched, and now matches the canonical candidate hash. Helper rollback tests restore prior hashes and refuse to overwrite later customization; the prior Git tag/release remains a public rollback source.

## Executed tools and limits

D07 actually delegated one bounded researcher before implementation, inspected three repositories, assessed Hugging Face relevance, and produced an original issue-planning skill informed by the findings. Source and license/revision gaps were disclosed; fetched code was not executed. D04 produced real local files and small synthetic PDF/CSV checks. Those deterministic fixture checks are not independent proof of the generated skill's general model performance. Tool-free cases used imposed capability limits inside otherwise tool-capable contexts; no external publication ran in test scenarios.

[Six description-only routing judgments](activation-check.json) matched their positive/negative labels. These do not test native discovery or domain output quality. [Twenty helper tests](unit-tests.txt) cover evidence rejection/adoption, rollback, customization protection, question retrieval, bundle consistency, session contracts and packaging. [Clean first-use checks](first-use-check.json) extracted the skill package, installed/validated four personal/project directory shapes, rebuilt the portable prompt byte-for-byte, included Finder and excluded a private sentinel. They test filesystem behavior, not native Claude Code execution.

Development used Codex desktop, Python 3.9.6 and an inherited model whose exact identifier/build/settings were not exposed. No paid API is mandatory. This is a small, selected case sample; no human-user study, repeated-sample reliability claim, universal model compatibility or performance superiority is established. Prior batched/follow-up-exposed results and assisted source recovery are disclosed rather than silently counted as independent successes. Raw third-party page dumps are omitted from public archives; source URLs, actual inspection actions, original-byte hashes and verification gaps remain, with local machine paths redacted.

Native Claude Code execution, native project discovery and other model families remain unverified. The prior Codex personal installation appeared in a later skill catalog; updating its files and checking hashes does not prove every native UI flow. See [compatibility](../../docs/compatibility.md).
