# v0.3.0 evaluation report

Status: candidate 7 was **actually rejected** by the unchanged local update helper on 2026-10-21 at 22:05:51 UTC. It is not adopted, installed or released. Stable v0.2.0 remains active on main and in the personal installation. Candidate 6 was also rejected after complete evaluation.

## Fixed comparison

Candidate 6 used 18 paired builder cases and 72 required conditions per arm, plus six separate description-only activation probes. Candidate 7 preserved these checks and added three independently frozen L cases: 21 pairs / 84 conditions per arm. Its separate activation probe was not executed. Inputs, expected behavior, failure conditions and the evaluator were frozen before execution. All original 48 conditions remain required; independently authored J and K cases add 12 conditions each. K was frozen before candidate 6 and was unseen by its implementation author. All required checks, question budgets and relevant regressions must pass, with no loss on a baseline-passing regression.

Only the original 20 new-feature conditions determine the predefined benefit: at least one additional satisfied condition against stable v0.2.0. J/K additions cannot inflate that metric. A positive result on the comparable canonical-first D01/D02/H03 subset is also required. Formatting and narrated success cannot satisfy behavioral conditions.

All 18 candidate arms, the three K baseline arms and the replacement D05 baseline arm are fresh: 22 fresh records and 14 predetermined baseline caches. Initially all 15 original baseline records were selected prospectively regardless of score; the registered entire-pair D05 interruption retry replaced that one cached counterpart before new output. Cached records retain their actual original dates, loading methods and limitations. Fresh actors receive one source, the current scripted turn and its allowed capabilities; future corrections and grading answers are withheld. The executor and grader work separately. User-visible plan messages are recorded in order, separately from generated files.

## Revision history

| Candidate | Source tree SHA-256 | Actual outcome |
| --- | --- | --- |
| 1 | `3fbcb24e5f81d9c622d41a33c514fa29f9adeb45d6f7e5a03da02c1c8db475cf` | Rejected: visible pre-build plan/check failures in D01/D02 and a missing corrected-output check in D04. |
| 2 | `75df8b714e5804f5f2f1ef2148efa67dea437870e39edcf3ee63d464e288aef7` | Rejected: incomplete implementation sequence in D01 and missing manual-save/resume handoff in D02. |
| 3 | `7c7a0467e500321a4d872e199317a69eec1dba7890c677b6465d03db9e169990` | Rejected: parent constructed the skill while both children only evaluated; D05 construction-role check failed. |
| 4 | `3735ddcdc3aebe6be3a0dca442a0147cdc789860f66d1577a048e94b5b4221a0` | Rejected: D06 reopened delivery discovery and returned no prior/candidate text pair or replacement. 26/28 observed conditions passed across seven cases; incomplete coverage did not authorize adoption. |
| 5 | `18ee2424eaffd4aad52145fe0dc35452b6b03713980a87b20aa2b8d59bf696cb` | Rejected: 58/60 conditions and 14/15 cases passed. J03 omitted material requirements from the visible preview and a settled correction from the resume handoff; J03-R2 was a baseline-passing regression loss. |
| 6 | `b644adc2f9984dd210066a7a0410b120a68d284f7d723c86f0e7a253e436d6ee` | Rejected: 70/72 conditions and 15/18 cases passed. K02 omitted pre-build checks; K03 omitted an independent resource-contract check; D07 exceeded the zero-question budget after its draft. |
| 7 | `8557ea0c92c2d2e1ba1978d31655cfeb5152d190a8420e4579d92ebb786f8f2e` | Rejected after a required K02-N1 failure. Only three pairs were independently graded; this is an incomplete suite, not a 10/84 performance estimate. |

Candidate 5 passed every original condition (48/48 against baseline 36/48) and all original new-feature conditions (20/20 against 10/20). The additional heldouts still prevented adoption: its ten-condition benefit did not excuse a required failure or regression. The helper actually rejected the candidate and preserved the prior active version. This is a narrow fixture comparison, not a statistical or universal-model claim.

## Candidate6 completed evidence

All18 pairs completed:22fresh records/14preselected baseline caches. Candidate6 passed70/72 conditions, all40 regression conditions, and15/18 case gates. Baseline had51passes,17failures and4unavailable conditions; only2case gates were eligible passes, with6other cases inconclusive/unavailable because historical capture was insufficient. Its missing checks were not imputed passes or failures. Original new-feature counts were20passes for candidate versus10observed baseline passes,6failures and4unavailable; the frozen full benefit comparison therefore remained inconclusive. The separate description-only probe matched6/6 activation decisions in each arm.

The unchanged helper actually rejected candidate6 on K02 and preserved stable0.2. K03's clean grade was transparently corrected from pass to fail for both arms after evidence clarification under the same criterion. A prior grader's source-read exposure made its preliminary batch03 findings uncredited; a registered fresh source-blind grader assessed the same ended actors without replay. Exact raw hashes, corrected grades and limitations are in [candidate6 grades](round6-grades.json), [executions](model-executions-round6.json), and [activation execution](activation-execution-round6.json).

Candidate7 preserves all72 prior conditions and adds12 independent L conditions frozen before its patch. All21 candidate cases run fresh; fourteen original baseline captures and all three new L baselines are prospectively fresh. A metadata-only capture audit replaced every cached record lacking an exact ended return before any new baseline dispatch; all results are selected regardless of score. Four complete-capture baseline records remain fixed. The38fresh plus4cached records retain the same inputs and checks. The evaluator, original20-only benefit metric, question budgets and failure conditions are unchanged. The actual stopped outcome follows.

## Candidate 7 stopped result

18 of 42 planned records completed: 14 fresh executions and four preselected complete-capture baseline caches. New dispatch stopped after an independently confirmed required failure; 24 fresh arms and the separate activation probe were not executed. Already running D01-B finished before the checkpoint. Completed responses were not replayed to seek a pass.

A source-blind independent grader audited D07, K02 and K03. Candidate A passed 10 of their 12 conditions and two of their three case gates; baseline B passed eight conditions and none of the three gates. All seven regression conditions in these three cases passed for each arm. The 110 selected artifact hashes/sizes, 40 original reused artifacts and ten frozen source-blind action views were audited with zero errors. These limited results do not establish the full original 20-condition benefit metric.

**Valid behavioral failure, K02-A-N1:** the visible plan before the target file omitted the manifest input columns `Item,Expected`, count-sheet columns `Item,Observed` and exact CSV header `Item,Expected,Observed,Delta`. These details appeared inside the completed skill. Correct finished contents cannot retroactively supply the missing pre-build preview.

**Separate test-design flaw, K02-N2:** the frozen criterion demanded Expected=8, Observed=6, Delta=-2, but the actual user input supplied no numerical example. The fixed score is preserved rather than relaxed after observing output; the omitted undisclosed numbers do not establish failure to preserve a supplied example. Other candidate N2 conjuncts (order, absence and explicit-zero behavior) passed. N1 independently justifies rejection. A future evaluation must prospectively align the input and expected check and rerun the comparable baseline; it must not teach the builder hidden fixture numbers.

Across all 84 conditions per arm, A has 10 pass / 2 fail / 24 executed but independently ungraded / 48 unexecuted; B has 8 pass / 4 fail / 24 independently ungraded / 48 unexecuted. The latter categories are inconclusive/unavailable, never passes. Fresh L cases remain unexecuted. The full benefit comparison is inconclusive. The unchanged helper actually rejected source 7 and preserved stable 0.2.0; its previous version and rejected candidate snapshot remain available locally. No further source candidate was authorized in this bounded run.

See [partial final grades](final-grades.json), [actual selected executions](model-executions-final.json), [activation status](activation-execution-final.json), [independent focus audit](candidate7-focus-audit.json), and [actual rejection](candidate7-rejection.json). Broader claims still require the remaining cases, activation, independent grading and relevant native/host checks. This report does not claim a completed release.

## Protocol and evidence

[Administrative and protocol amendments](evaluation-amendments.json) record owner-authorized effort extensions, actual quota interruptions, baseline reuse and prospectively selected retries. They do not relax original acceptance checks or change the evaluator. Candidate 4's first D05 pair was diagnostic because a child read an extra guide. Candidate 5's first pair lacked full plaintext child task/return capture. Their entire replacement pairs were registered before output and retained regardless of outcome. No ordinary behavior failure was retried to seek a passing answer.

Candidate 6's first D05 attempt stopped at a real usage limit before a response or child return; its fixed five-minute window expired during the wait. Original tasks and partial workspace were retained. One entire fresh pair was registered before any new output, with the same source, input, capabilities, checks and five-minute/two-child bounds. Completed J03 evidence was retained without replay. Quota waits use the owner's existing authorization and are excluded from active effort; new control timestamps are actual, never backdated.

These are actual isolated model responses/actions for intentionally public fictional inputs. Execution exports include exact inputs, visible response order, tasks/returns and selected artifacts with distinct raw and path-aliased publication hashes. Private user sessions, credentials and native diagnostic streams are excluded. Independent raw-artifact auditing and release privacy review are separate from behavioral grading. Earlier evidence remains available beside this report.

The inherited Codex model is retained without override; its exact serving identifier/build is not exposed. Coded arms are imperfectly blind because content and source metadata can reveal identity. Cached baselines introduce timing and, for some older arms, full-export versus conditional-resource loading differences; these limits are disclosed. No-tools cases exercise builder behavior but cannot execute the generated skill's domain workflow. D05 separately requires actual construction and fixture checks. Description-only activation is distinct from native skill discovery.

## Helpers and host limits

[Local helper and package evidence](helper-checks.json) includes 28 helper tests (27 passed and one Windows-only skip locally), portable generation/drift checks, packaged relative links and four temporary personal/project Codex/Claude installation paths. Candidate 6's prepared archives were extracted and compared with the frozen canonical source. Its helper code is byte-identical to the code actually tested on Python 3.15.0 / macOS 14.6 ARM. These are script/filesystem results, not native model execution.

[Hosted platform checks](final-source-platform-checks.json) currently identify source 5: six successful jobs cover Windows and Ubuntu with Python 3.9/3.13, Intel macOS with 3.9, and ARM macOS with 3.13. Actual expanded job logs supplied runtime profiles. Final-source publication-head CI and public-download first use remain pending.

The historical [native Codex smoke](native-codex-smoke.json), using CLI 0.163.0-alpha.10.2 on macOS ARM with exact candidate-4 source, verified project discovery, a visible plan, a draft and metadata. Its reviewer claim lacks a captured launch/return and receives **no independent-review credit**. Exact final-source native Codex execution, native Claude execution, native Windows/Linux model runs and equivalent performance across other LLMs remain unverified.

Before release, final model grades must satisfy every gate; automatic adoption, managed personal-copy equality, exact public file selection, final-head CI, release asset hashes and clean public-download first use must be verified. Missing or inconclusive evidence keeps the prior version active. This rejected-candidate report is not a passing release report.
