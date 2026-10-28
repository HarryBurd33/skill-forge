# v0.4.1 REA macOS recovery validation

The opt-in runner fixes the observed duplicate SwiftBridging compiler failure for the exercised REA JavaScript analysis. All nine unchanged fixed checks passed on candidate 2, and the local evidence gate adopted it. The core SHA-256 is `850e1fd6286663bb0c7f360a2e47adca7c78822917b7ed7a2e4d8d4fad01f454`. Final GitHub/installed/download parity is verified separately during release closing; see the release receipt.

## Method and actual results

The evaluator, acceptance table, original semantic assertions and original held-out manifest were frozen before candidate construction. [Criteria](frozen-criteria.json), [fixed evaluator](fixed-evaluator.md), [case table](development-cases.json), [results and execution hashes](results.json), [independent grade](candidate2-independent-grade.json) and [independent verification](independent-final-verification.json) provide the review trail. Script execution is the behavioral method; no new model interview benchmark is claimed. The constructor used requested Sol/high and independent reviewer requested Astra/medium; serving build metadata was unavailable. Existing interview instructions changed only in version metadata; the reverse-engineer adapter gained a conditional recovery reference.

Environment: Apple Silicon macOS, Apple Swift 6.0.3 (`swiftlang-6.0.3.1.10 clang-1600.0.30.1`), xcrun-selected Command Line Tools/MacOSX15.2 SDK, cached Node 24.22.1 and `rea-agents@6.8.0`. Packages were exercised offline. REA’s documented supported compiler selector and SDK were supplied only to the child process; native process ownership remained enabled.

| Fixed case | Actual check and outcome |
| --- | --- |
| C0 baseline | Retained default-compiler failure contains the actual duplicate SwiftBridging diagnostic. Baseline original semantic-success metric is 0. |
| C1 original fixture | Frozen runner and actual REA exited 0; imports/functions and source-hash/range-bound return expression assertions passed. Metric is 1. A compiler-only probe or exit 0 alone would not pass. |
| C2 guards | Actual toolchain discovery and both sole matching definitions verified. Executed overlay assertion masks exactly redundant `module.modulemap`; retained `bridging.modulemap` stays visible. |
| C3 refusal | Unsupported OS, missing/mismatching/additional map definitions, absent executable and existing custom compiler/SDK selectors fail closed. |
| C4 argv/caches | Adversarial spaces/quotes/dollars/semicolons arrive unchanged; no shell trampoline or shell interpretation. Both custom cache selectors and unrelated sentinels survive. |
| C5 process failures | Real subprocess nonzero/signal/SIGINT/spawn/I/O/timeout/cleanup and concurrent-root cases executed. Detached native jobs cannot be inferred settled from root-group absence: uncertain paths retain state and report failure. |
| C6 protected files | Before/after SHA-256 matches for both Apple maps and all four inspected REA native ownership/Swift source files. No system/security/configuration changes or new engines. |
| C7 regressions/distribution | 68 tests collected: 67 passed, one existing Windows-only junction check skipped locally. The original 43 test sources are byte-identical. Package/relative links/derived prompt and four clean temporary Codex/Claude personal/project install paths passed. |
| H1 original held-out | Frozen original held-out actual REA run and static semantic assertions passed; clean exit, unchanged protected hashes and no new runner temporary roots. |
| Additional unseen round 2 | A fresh sealed fixture was reserved after candidate 1 rejection and disclosed only after candidate 2 freeze. Actual REA and independent assertions passed. Original H1 remained required. |

[Original fixture and assertions](assert-original-semantics.py), [original expectations](original-expectations.json), [H1 fixture/plan](heldout-original/execution-plan.md) and [supplemental fixture/plan](heldout-round2/execution-plan.md) are public replay material. Run an installed compatible REA through the recovery runner with actual captured diagnostics, save its evidence JSON, then invoke the assertion script with that JSON, fixture directory and expectations JSON. Native host permissions are required. These are inert original MIT examples, not user software or private transcripts.

## Rejected candidate and preserved checks

[Candidate 1 was rejected](candidate1-independent-gate.json) despite passing semantic runs. An independent fake compiler emitted invalid UTF-8 after spawning a detached child. The wrapper deleted probe state while that child still depended on it. Candidate 2 narrowly changed post-launch probe-exception retention and added the executable regression: the detached child now sees its source retained and the failure propagates. The previous active v0.4.0 stayed intact until the fixed checks passed; no criterion was relaxed. Candidate snapshots, actual private captures and the v0.4.0 rollback baseline are preserved locally. The helper’s round-1 submission also rejected intentionally incomplete evidence; independent C5 rejection is the substantive behavioral finding.

## Limits

- This is a narrow optional process-local workaround, not an Apple toolchain repair. Ordinary unwrapped Swift/REA invocation can still hit the underlying duplicate maps. Use an actual captured diagnostic with `--diagnostic`; the bounded automatic probe conservatively retains state after failure and does not establish fully settled native descendants.
- A workspace-sandbox REA run produced semantic output but failed cleanup with process-inspection EPERM and scores 0. Normal host execution then passed without bypassing security or disabling ownership. Other sandbox policies can still block REA.
- The source-backed return expression is not a REA branch edge. Imported calls may remain unknown. No target application was executed, no runtime path was established, and no universal software/REA-provider support is claimed.
- macOS ARM native recovery is exercised. Intel Mac recovery and Windows/Linux native REA providers remain unverified. POSIX process tests are explicitly skipped on Windows; five portable guard/parser tests still execute there. Core helper hosted CI is separate from native REA execution.
- Failed/interrupted jobs can retain temporary files until their native descendants are independently confirmed ended. The utility signals only its owned root group; it cannot certify arbitrary escaped jobs globally.
- No new native Claude or other-model behavioral parity test was run. The portable text contains recovery instructions/notices but not the executable runner; use the full skill/source package for that optional tool.

The complete consulted MIT overlay-strategy notice is bundled; [source provenance](../../SOURCES.json) and [notices](../../THIRD_PARTY_NOTICES.md) preserve attribution. Raw captures/private paths/caches are excluded from the public allowlist. Historical v0.4.0 Anatomy and model evidence remains unchanged.
