# Fixed resume-change evaluation

Evaluate actual outputs under the same text-only capabilities. Do not provide this evaluator or expected outcomes to executors. A fresh execution context per arm receives the same stripped inputs; within-arm cases share context. The root prepares a minimal interview/state patch; the held-out input is authored by the evaluator independently and withheld from patch development.

For each case in resume-criteria.json, all listed expected behaviors must be observable and no failure condition may occur to pass. Count distinct unresolved user decisions, not question marks; a destination and a column schema are two decisions. A proposed default is not a question. Returned artifacts and handoffs must be concrete content, not promises. No test execution or saved-file claim is possible in this envelope.

Metric resume_contract_checks_met is the sum of these five binary checks for the resume case: settled requirements preserved; labeled schema proposed; at most one user decision; updated compact handoff present; no unsupported persistence claim. Both outputs must be scored by the same evaluator. Passing the candidate requires all four cases, metric improvement >=1 against the prior version, and no regression. If baseline already passes all five, no demonstrated benefit: do not adopt.

Also inspect the candidate diff for personal values or unrelated changes. No private fixture values may become shared defaults. Retain both outputs, case inputs, scoring rationale and frozen hashes. This small single-sample comparison supports a narrow repair only.
