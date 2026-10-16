# Existing-target fixed evaluation

Apply the exact expected rows and failure conditions originally declared in examples/existing-skill/fixture.json and the heldout-explicit-owner case in evals/cases.json. These expected behaviors predate model execution; this file maps them to the helper's evidence schema without weakening them.

For missing-owner and columns-order, use the new exact-fixture executions. Compare actual Markdown rows with expected rows; ignore harmless capitalization and equivalent action wording. For explicit-owner, use the independently preserved original paired outputs and independent grader's result. The same original before and after SKILL.md sources were used. Check sources against fixture starting hash and preserved canonical source content.

Metric cases_meeting_contract counts passing missing-owner and explicit-owner behavioral cases (0–2), not formatting checks. Require every candidate case pass and improved metric. Do not infer successful local application from model prose: helper submission and active tree hashes must demonstrate actual adoption. This proves a small original example target, not all upstream skills.
