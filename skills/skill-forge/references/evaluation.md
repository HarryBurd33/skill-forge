# Evidence proportional to the change

Before building, put concrete checks, expected outcomes, failure conditions, baseline and unavailable checks into the user-visible implementation spec. Preserve any review-first request. Before running candidates, freeze a small case table: id, input, expected observable outcome, failure conditions, required tools, maximum unnecessary questions, split, and evaluator. Separate development cases from regression cases; use held-out inputs not used to craft general changes. Reusing a known test is regression evidence, not held-out evidence.

Trace material requirements and supplied acceptance examples to checks before construction. Preserve the exact supplied inputs and expected results; a convenient substitute cannot establish that an agreed case was covered. Add discriminating cases where order or missing-versus-valid values affect behavior. Check each behavior-bearing supporting resource independently against the final contract, including stale instructions; final artifact correctness does not supply a missing pre-build verification plan. Count user decisions across the whole response, including questions appended after a draft.

Evaluate activation independently: should a request select this skill at all? Then evaluate task quality: requirements preserved, usable artifact, uncertainty handled honestly, effort requested, and completion. Choose a few observable binary checks and a qualitative 0–2 rubric (0 fails, 1 partial, 2 meets criteria). Define critical failures that cannot be averaged away, such as invented citations or violated fixed constraints.

For new skills compare with a simple direct prompt or an appropriate existing creator. For updates compare baseline and candidate on identical inputs, tools, model/version, effort settings and evaluator where possible. Record mismatches and avoid causal claims they cannot support. A separate executor receives the request and relevant files but not expected answers or proposed fix. A separate grader uses frozen criteria and actual artifacts. Use blind labels where feasible; disclose small samples, shared contexts or non-blind reviews.

Evidence types:
- Static: format, links, metadata, schemas. Proves structure only.
- Executed deterministic: actual utility invocation, invariant or scheduling calculation with captured results.
- Real model execution: actual input/output in a new model context; simulated users remain simulated users.
- Illustration: authored transcript or demonstration; useful documentation, no behavioral pass.
- Unavailable: state the exact missing capability. Do not substitute confidence.

Behavior-changing updates require observed behavioral benefit and relevant regressions. For a search/index change, actual retrieval correctness/effort checks can establish that narrow benefit; they do not establish improved downstream model outcomes. Keep the evaluator and criteria fixed for the comparison. Failed or inconclusive required checks prevent adoption. If criteria genuinely need changing, record a separate evaluation-design change and rerun the prior version under the new criteria before assessing a candidate.

A concise report includes case IDs, baseline/candidate hashes, model/host and known versions, date, actual output paths, evaluator/rubric hash, pass/fail/inconclusive per case, effort (questions and elapsed time where measured), and limits. No numeric aggregate should hide a critical failure.
