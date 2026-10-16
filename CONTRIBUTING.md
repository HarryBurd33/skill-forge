# Contribute a demonstrated improvement

Start with an issue or a small pull request. You do not need to write code to report a useful failure.

Include a sanitized or fictional input, what you expected, what actually happened, and why it matters. State the host/model if known and which tools were available. Mark an authored example as illustrative; do not call it an executed failure. Do not upload private transcripts, personal schedules, tokens or credentials.

For a question proposal, search `skills/skill-forge/questions/questions.json` by purpose and synonyms. Include question text, purpose, ask/skip conditions, dependencies, affected decisions, motivating evidence, tags, and candidate status. Prefer revising an overlapping question over adding a duplicate. See the [question proposal form](.github/ISSUE_TEMPLATE/question.yml).

A maintainer follows this path:

1. Reproduce the observation and distinguish personal preferences from general decisions.
2. Freeze inputs, expected results, failure conditions and evaluator before changing the skill. Keep development, regression and held-out cases distinct.
3. Patch the canonical skill or library. Record baseline and candidate artifacts under comparable conditions. Run relevant helper checks and real behavioral checks for behavioral changes.
4. Accept only demonstrated benefit with no required regressions. A useful accepted question receives a stable ID, version/history, and a regression case. Retire redundant questions with rationale instead of silently deleting history.
5. Regenerate the portable prompt, update CHANGELOG and the public evidence record, and rebuild allowlisted packages. Local successful adoption needs no extra approval ritual; repository writes still require the contributor's access and destination authorization.

Run the three development commands in README. New utility changes need tests of meaningful invariants. Read `evals/rubric.md` before making behavioral claims. Freeze the evaluator outside candidates and never lower acceptance checks simply to admit a patch. Limit an improvement run to three candidates and a stated effort budget unless explicitly changed.

Keep third-party reuse documented with exact source URLs, commit, retrieval date, license and required notices. MIT is the default only for original compatible material. Examples should be self-contained and preserve source attribution.
