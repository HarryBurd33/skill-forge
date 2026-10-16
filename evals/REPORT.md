# v0.1.0 validation report

Release prepared 2026-10-16. Research retrieved 2026-10-15; executions span October 15–16 in America/Denver (machine logs use UTC). This is a usable first release with recorded limitations, not an all-pass reliability claim.

## What actually ran

| Check | Actual result | Evidence |
|---|---|---|
| Python helper suite | 18/18 pass | [Test inventory and clean first-use record](results/first-use.json), [test source](../tests/test_forge.py) |
| Original builder cases | 9/12 strict passes vs direct baseline 8/12 | [Independent grades](results/grades.json) |
| Generated-skill domain cases | 5/5 vs baseline 4/5 | Same grades; separate from builder claims |
| Combined predefined behavioral cases | 14/17 vs 12/17 | [Grader summary](results/grade-summary.md) |
| Activation/non-activation routing review | 6/6 for each arm | Same grades; metadata selection, not native discovery |
| Scripted three-turn research interview | Both conditions meet the three predefined criteria | [Case](multiturn-case.json), [baseline](results/multiturn-baseline.json), [portable condition](results/multiturn-candidate.json) |
| Actual builder question update | Automatically adopted; destination-query coverage 0/3 → 3/3 | [Executed retrieval](results/retrieval-execution.json), [change](results/builder-change.json) |
| Redundant question candidate | Rejected; active hash unchanged | [Rejection](results/rejected-change.json) |
| Proposed resume wording patch | Both arms pass 4/4; benefit metric 5 → 5; automatically rejected | [Grades](results/resume-grades.json), [transaction](results/resume-rejection.json) |
| Existing target example | Automatically adopted after exact-fixture and prior held-out checks | [Actual outputs/review](results/target-execution.json), [adoption](results/target-adoption.json) |
| Rollback/customization/privacy | Real temporary-file tests passed | Helper suite and [first-use record](results/first-use.json) |
| Generated file format | Four initial standalone drafts pass; two existing-skill snapshot labels fail folder/name matching | [Actual validator results](results/generated-format-checks.json) |

The original 26-case table and rubric were defined before execution. [Execution manifest](execution-manifest.json) records their hashes and prompt/capability conditions. The two arms each produced 24 saved outputs: 17 behavioral, six routing, and one exploratory missing-owner case. Exploratory results are excluded from the predefined totals. [Baseline outputs](results/model-baseline.json) and [Skill Forge outputs](results/model-candidate.json) are intentionally public synthetic fixtures, not private user transcripts.

The grader saw anonymized A/B labels, with A=Skill Forge and B=baseline disclosed here afterward. Content could reveal identity; an initial filename inventory exposed original labels but not mapping or contents. Grading was independent of execution, not perfectly blinded. Later repair grading used visible before/after labels.

## Observed strengths and failures

The original runs exercised simple and detailed complex requests without extra clarification, ambiguous research, contradictions, draft-now, resume, question proposals, no tools, evidence-limited research, a document-to-CSV change, an exam reschedule and infeasible capacity. The planner preserved sleep, travel and classes; the research example did not invent quantitative results. Skill Forge supplied a more complete question record and a no-tools handoff than the direct baseline in this sample. The prior meeting-actions skill added an unagreed glossary-discussion action in a held-out case; the revised example retained only the explicit commitment.

Three original Skill Forge cases did not strictly pass:

- **Resume:** requested both receiving destination and required columns, exceeding the one-decision budget, and did not provide the required updated compact handoff. Both arms failed this first sample. A fresh four-case comparison passed for both old and proposed wording, so the predeclared benefit threshold was not met. The patch remains unadopted; no failed original result was overwritten or averaged away.
- **Existing-skill text-only improvement:** no real file snapshot/adoption could occur in that capability envelope. Its proposed `meeting-actions-candidate` and `meeting-actions-baseline` folder labels also disagreed with the `meeting-actions` metadata. These raw outputs remain visible. To save such versions, use separate parents—`candidate/meeting-actions/SKILL.md` and `baseline/meeting-actions/SKILL.md`—and run the validator before installation. The delivered example folders use matching names. A separate tool-enabled target demonstration subsequently executed the adoption; it does not retroactively turn the original text-only case into a pass.
- **Held-out repository deliverable:** selected Python without explicitly labeling that unprovided implementation choice as an assumption. Treat unspecified implementation choices as proposed defaults when reviewing a draft.

Counts of user decisions are judged from the actual output, not self-reported question marks. Across the 17 cases both arms requested five decisions by the grader's definition. This sample does not demonstrate less total user effort, statistical superiority or consistent behavior across models.

## Automatic-update evidence

[The builder-change walkthrough](../docs/improvements.md) connects observation, hypothesis, frozen checks, actual executions, automatic adoption and rejected candidates. The question author did not see the evaluator's CSV/repository probes; the overall brief already named those artifact types, so this was a modest holdout. Retrieval improvement does not establish improved downstream writing or interviews.

The proposed resume change added explicit handoff and decision-counting guidance. A separate author supplied a held-out NDJSON scenario without showing it to the patch author. The fixed metric was five observable resume-contract checks. Both baseline and candidate scored five, so the helper retained the prior version despite all candidate cases passing. [Candidate diff](results/resume-reviewed.diff) is preserved for future investigation; criteria were not weakened.

The existing-target demonstration uses the original MIT fixture. Its exact missing-owner test was executed in two fresh contexts; the prior held-out explicit-owner comparison and independent grade supply the substantive no-extra-commitment benefit. The baseline's `Not agreed` label also fails the predefined exact `Unassigned` convention, although both convey an unknown owner. The orchestrator reviewed the exact-fixture rows; the earlier held-out result was independently graded. [Frozen gate](target-criteria.json), [evaluator](target-evaluator.md), [evidence](results/target-evidence.json), [active example](../examples/existing-skill/active/meeting-actions/SKILL.md). No unrelated skill or user setting was changed.

All successful and rejected transactions have private full snapshots and rollback history outside the publishable repository. Public change records omit local machine paths. Helper tests actually restore prior hashes and refuse rollback after later customization. Evidence records are caller-supplied attestations with file bindings, not cryptographic proof that a model was invoked or an adversarial sandbox.

## First-use and packaging checks

From clean temporary locations, the skill archive was extracted and installed using the documented personal/project directory shapes for both hosts. Installed validation and question search passed. Rebuilding the portable prompt from the extracted installation produced byte-identical content. A private sentinel saved outside source did not appear in either skill or portable package. This tests the filesystem/helper path, not actual host UI discovery.

The release checker validates every reviewed publication path, local Markdown file links, JSON, Python syntax, standalone example metadata and portable-source consistency. Packaging extracts and validates the actual skill contents and includes MIT and attribution notices. The source archive uses an explicit allowlist. Every selected file was reviewed as project material or intentionally public synthetic evidence; no synced project `sources/` files or private session/control-state files are published.

## Limits and next useful work

Development ran in Codex desktop with a GPT-6-based agent context and Python 3.9.6 on macOS. The exact model identifier, reasoning setting and desktop build were not exposed; the requested Astra role is not runtime-version evidence. One fresh context was used per original arm, with cases batched within that context. The four direct domain baselines were regenerated in a fresh child without skill sources after a protocol correction. The baseline instruction's exact wording is preserved in the manifest; it differs slightly from the rubric's prose exemplar while retaining the intended task. There were no repeated samples, human participants or significance estimates.

Claude Code native runtime and both hosts' native discovery were not exercised; installation guidance is supported by current official documentation. Plain-chat tests simulated absent capabilities inside tool-capable execution contexts. The portable prompt was loaded for the scripted follow-up, but other model families and chat products remain unverified. Authored worked examples are illustrations, not execution evidence.

Prioritize repeated resume/destination trials, independent validation of generated file naming, and real first-use trials in both native hosts. Keep the current failed cases as regressions. A larger question library or more detailed output alone is not evidence of improvement.
