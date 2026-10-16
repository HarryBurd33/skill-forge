# Predefined evaluation protocol

This protocol and [cases.json](cases.json) define expected behavior **before** candidate execution. Authored demonstrations in examples are fixtures, not results. Keep raw outputs and a result manifest for actual runs. Freeze the case-file SHA-256 in that manifest; a candidate cannot edit its own acceptance criteria or evaluator to qualify for adoption.

## Comparable conditions

For a new-builder comparison, give the baseline this instruction:

> Help the user create or improve a reusable agent skill from their request. Ask for missing information when needed, then provide practical skill instructions, examples, and validation guidance. Preserve explicit user constraints and be honest about unavailable tools.

Give the Skill Forge condition the canonical skill and the relevant supporting resources. Both conditions receive the same user input, factual context, capabilities, output allowance, and interaction budget. For generated-skill domain cases, compare the generated SKILL.md against the same task without that skill; report this separately from the builder comparison. For existing-skill updates, use the actual previous skill as baseline. Do not substitute a deliberately broken invented baseline.

Use separate execution contexts where available. An executor sees the user input and necessary source artifacts, **not** expected outcomes, failure conditions, the proposed fix, or earlier grades. A grader sees the outputs and frozen criteria; randomize version labels when practical. Record whether execution was one batch context or isolated per case. A single batch is useful smoke coverage but permits cross-case influence and is weaker than isolated runs.

Identify the observed host and model version when exposed by the environment. If the exact model build is unavailable, say so instead of inferring it from a role or product name. Record tool availability, prompt/source hashes, case IDs, interaction count, and any truncation or run error. Comparable first-turn tests establish first-turn behavior only; they do not establish a complete multi-turn interview or successful file mutation.

## Evidence levels

| Level | What counts | What it does not prove |
| --- | --- | --- |
| Static check | A validator ran on files, relative links, schemas, or packaging | Useful interviewing or output quality |
| Authored illustration | A human/agent writes an expected example without executing the skill | A behavioral pass |
| Model execution | A separate model context actually receives the task and returns a preserved output | Repeated reliability or a real human study |
| Tool/integration execution | A helper actually updates, rejects, rolls back, or exports files and observable state is checked | Model judgment quality beyond those checks |
| Unavailable | A required action cannot run with current tools or permissions | Success; keep the candidate unadopted if this evidence is required |

Report unavailable checks, failures, and inconclusive comparisons explicitly. Never upgrade “the model said it would do this” into proof that a file was saved, a test ran, or an update was adopted.

## Rubric

Score each applicable dimension from 0 to 2. Use `N/A` when a dimension does not apply, and quote or point to the output evidence for every failure and improvement claim.

| Dimension | 0: fails | 1: partial | 2: meets |
| --- | --- | --- | --- |
| Requirement fidelity | Violates a material constraint or invents a settled answer | Preserves core intent but misses a relevant requirement | Preserves confirmed requirements, boundaries, and changed decisions |
| Decision quality | Asks irrelevant questions or hides a consequential uncertainty | Finds some important choices but misses a dependency | Resolves/targets the choice with greatest material effect and distinguishes discoverable facts |
| User effort | Repeats settled questions or blocks a draft with a fixed questionnaire | A useful but avoidable question or unnecessary repetition | Meets the case's question budget and produces useful progress |
| Artifact usefulness | Unusable output or incorrect contract | Useful draft with a material omission | Independently usable requested artifact, example, and clear assumptions |
| Evidence honesty | Fabricated source, tool result, experiment, test pass, or memory | Limits are present but ambiguous | Clearly distinguishes supplied evidence, assumptions, illustrations, executed checks, and gaps |
| Improvement discipline | Adopts on imagined evidence, weakens checks, leaks private material, or loses rollback | Proposal is reasonable but evidence/recovery is incomplete | Connects observation, hypothesis, patch, fixed checks, comparison, and rollback; adopts only when prerequisites actually pass |

An individual behavioral case passes only if **all its expected behaviors are observable**, no listed failure condition occurs, and applicable dimensions score 2. A partial score is useful diagnostic evidence, not a pass. A first-turn artifact may explicitly defer a tool action; that is honest but is not proof of action completion. Mark action-dependent criteria untested rather than granting them from a promise.

Activation is a separate binary routing check against `expected_activate`. Do not use good output quality to excuse misrouting, or use routing success as evidence that the skill works. `routing-review` means a selection judgment under supplied metadata; actual host discovery remains unverified unless tested in that host.

## Improvement and adoption

Before a candidate run, name the intended benefit and relevant cases. Compare both conditions using the fixed rubric and original acceptance criteria. A demonstrated benefit is a concrete corrected failure or fewer unnecessary user decisions with no lost required behavior, supported by actual outputs. A higher self-reported confidence or more elaborate text is not a benefit.

A general builder update requires the motivating development case, applicable regression cases, and at least one relevant held-out case. Keep development examples separate from the regression and held-out splits. If held-out cases were inspected while designing a candidate, disclose that contamination and introduce a new withheld scenario before making a broader improvement claim. A one-run result is smoke evidence, not a statistically reliable advantage across users or models.

The passing condition must be decided before evaluation. Do not lower a threshold, remove a failed case, or change the evaluator to accept the current candidate. If a criterion is genuinely invalid, document and version its revision separately, then rerun both baseline and candidate under the new criteria.

Use at most three candidate rounds by default and state an effort limit at the start. Stop when acceptance criteria and the demonstrated benefit are met, no further benefit appears, or the limit is reached. Preserve failed or inconclusive candidates and missing evidence for later work. Successful authorized local updates should be automatic; the evidence and change record are reviewable outputs, not an extra approval gate.

The update integration cases require actual temporary files. Verify candidate adoption by content/hash, verify failed-candidate rejection by an unchanged active hash, and verify rollback by equality to the recorded prior snapshot. Include a customized managed copy to ensure it is preserved or explicitly reported as conflicted. Keep these tests separate from model behavior grades.

## Suggested first-release workload

1. Run static format, links, packaging, and script tests.
2. Run the 17 behavioral cases as bounded decisions or artifacts, with a representative sample producing full SKILL.md contents. Report any first-turn-only limit.
3. Compare at least simple creation, ambiguous complexity, detailed complexity, resume, and one domain failure against the direct baseline under comparable conditions.
4. Run the six activation cases independently of artifact grading, and the three update integration cases with real files.
5. Independently grade preserved outputs, record disagreements, and summarize limitations. Do not turn authored demonstration text into an execution log.

The workload is deliberately a small release smoke suite. Broader claims require more independent cases, repeated runs, and evaluation by actual users.
