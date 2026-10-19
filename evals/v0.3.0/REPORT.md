# v0.3.0 evaluation report

Status: v0.3.0 is **not adopted or released**. Four candidates were rejected under fixed checks. A fifth source is frozen for a separately authorized focused repair run; its behavioral evaluation is pending. Stable v0.2.0 remains active on main and in the personal installation.

## Recorded comparisons

The fixed design contains 15 paired builder cases / 60 required conditions per arm, plus six separate activation probes. Inputs, expected behavior, failure conditions and the evaluator were defined before execution. The original 48 conditions remain intact; 12 independently authored J conditions add held-out coverage. The implementation author has not read those prompts. The original 20 new-feature conditions alone determine the benefit metric; additional held-out checks cannot inflate it.

| Candidate | Source tree SHA-256 | Outcome |
| --- | --- | --- |
| 1 | `3fbcb24e5f81d9c622d41a33c514fa29f9adeb45d6f7e5a03da02c1c8db475cf` | Rejected: visible pre-build plan/check failures in D01/D02 and missing explicit corrected-output check in D04. |
| 2 | `75df8b714e5804f5f2f1ef2148efa67dea437870e39edcf3ee63d464e288aef7` | Rejected: incomplete implementation sequence in D01 and missing manual-save/resume handoff in D02. |
| 3 | `7c7a0467e500321a4d872e199317a69eec1dba7890c677b6465d03db9e169990` | Rejected: parent constructed the skill while both children only evaluated responses; D05 construction-role check failed. |
| 4 | `3735ddcdc3aebe6be3a0dca442a0147cdc789860f66d1577a048e94b5b4221a0` | Rejected: D06 reopened delivery discovery and returned no prior/candidate text pair or replacement. |
| 5 | `18ee2424eaffd4aad52145fe0dc35452b6b03713980a87b20aa2b8d59bf696cb` | Frozen; fresh behavioral evaluation pending after a quota interruption before the first response. |

Candidate 4 passed 26 of 28 conditions across seven graded paired cases, and six of those seven cases passed completely. The baseline passed 18 of 28 conditions. The observed new-feature subset improved by seven conditions, with no observed baseline-passing regression loss. These partial counts **do not establish adoption eligibility**: D06 failed two required checks, eight candidate cases and all activation probes remain unexecuted, and no held-out J actor was dispatched. See [the independent candidate-4 grades](round4-grades.json).

Its first D05 run met the four behavior conditions but was protocol-inconclusive because a constructor read an extra installed guide outside frozen resources. The entire pair was retained as diagnostic evidence. One preregistered paired retry applied the existing source boundary explicitly to all descendants. That eligible candidate run passed construction, separate evaluation, actual fixture checks and package requirements. No ordinary behavior failure was retried to seek a pass. [Administrative amendments](evaluation-amendments.json) distinguish owner-authorized effort/candidate extensions from unchanged behavioral acceptance criteria.

## Evidence and limits

These are actual isolated builder model executions, not imagined runs. All user-visible response messages, inputs, action records and selected artifacts were saved and hashed. [Candidate-4 execution records](model-executions-round4.json) contain intentionally public fictional fixtures with machine-specific paths aliased; raw and published text hashes are distinct. Previous rounds and source freezes remain alongside them. Raw private user answers, native diagnostic streams and authentication metadata are excluded.

The evaluator runs separately from the author and neutral execution coordinator. Coded arms are imperfectly blinded because source/version names and loader metadata can reveal identity. The current inherited Codex model was retained; its exact serving identifier/revision is not exposed. Predetermined baseline reuse saves work but introduces timing and, for some older cached arms, full-export versus conditional-resource loading differences. A positive result on the comparable D01/D02/H03 subset remains additionally required; H03 is still unexecuted. No statistical or universal-model claim is made.

No-tools cases execute the builder's response but cannot execute the generated skill's domain workflow. Their sample checks are planned/static unless actual action records establish otherwise. D05 supplies actual construction and downstream fixture execution. Activation is evaluated separately from output quality and remains pending.

[Six hosted helper jobs](final-source-platform-checks.json) passed for candidate 4 on Windows/Ubuntu with Python 3.9 and 3.13, Intel macOS with 3.9, and ARM macOS with 3.13. [Local helper/package evidence](helper-checks.json) includes 28 unit tests (27 passed and one Windows-only skip locally), packaged links and four temporary installation paths. These are filesystem/helper results, not native Claude or every-platform model tests. The fifth source needs its own final-source and publication-head checks.

An [exact-source native Codex CLI smoke](native-codex-smoke.json) on 0.163.0-alpha.10.2 / macOS ARM verified candidate-4 project discovery, a visible pre-build plan, a draft and its metadata. Its claimed independent static review has no captured launch/return evidence and receives **no independent-review credit**. Generated-skill behavior was not benchmarked by this smoke. Native Claude, native Codex model execution on Windows/Linux, and parity across other LLMs remain unverified.

Before adoption or release, every required condition, relevant regression, held-out case and activation probe must pass; the fixed benefit threshold must be demonstrated; selected public files, final-head CI, managed-copy equality and clean public-download first use must be verified. Failed or missing evidence keeps v0.2.0 active. The current report is an interim record, not a passing release report.
