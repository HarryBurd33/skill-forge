# Skill Forge v0.3.1 validation — 2026-10-26

A narrow metadata-helper upgrade, not a new interview benchmark. The prior v0.3.0 behavioral evidence remains [historical](../v0.3.0/REPORT.md); it was not rerun or relabeled as a v0.3.1 model test.

## Predefined comparison

Independent review froze [criteria](criteria.json), [22 development cases](development-cases.json), [four reserved cases](heldout-cases.json), and a [real-subprocess evaluator](evaluator.py) before implementation. The implementer did not read the reserved cases before freezing. All26 candidate cases were required; the minimum predefined benefit was three additional correctly rejected invalid inputs. Evaluation uses actual CLI return codes and diagnostics, not imagined model runs.

| Check | v0.3.0 baseline | v0.3.1 candidate |
| --- | --- | --- |
| Full fixed case outcomes including diagnostics | 16/26 | 26/26 |
| Invalid metadata cases correctly rejected | 3 | 12 |
| Independent reserved cases | See per-case artifact | 4/4 |
| Local helper unit suite after integration | Historical suite retained | 31 run:30 passed,1Windows-only skip |

The baseline lacks the new profile flag; for known Claude cases the evaluator runs its existing generic validator and explicitly records that fallback. An unknown-profile diagnostic also differs in the old argparse output; it does not count toward the benefit metric. This is a versioned capability comparison, not an identical-flag baseline or causal model-quality experiment.

[Actual results](execution.json), [fixed-control hashes](freeze.json), [independent final review](final-independent-review.md) and [gate evidence](gate-evidence.json) are included. Public execution case-path labels and artifact references are remapped to colocated files; the private original remains retained. No criteria or scores were changed.

## Adoption and preserved history

The first authored candidate passed CLI tests but independent review found a closing-fence formatting defect in the new helper documentation. It was not adopted; [the finding](candidate1-review-rejection.json) is retained. A newline-only documentation repair produced the final source, reran the same26cases and passed review. There were two authored candidates and one successful formal gate submission within the bounded run.

Final core SHA256: `5b25ded0676dc20f8331442bfe62a4d3e17df05a9f71603cd745224c7b5a27c7`.
Baseline core SHA256: `86daffd3c4e7cdeed994717466b0ba9a8e3c6c16bd596acbef3ed01114963608`.
The fixed gate automatically adopted this source; the managed laptop installation was updated with its customization guard and verified to the same hash. The local run retains baseline, candidate, evidence and rollback. Its private absolute paths are not published.

## Scope and limits

- Original code, no new dependencies; Python3.9+ remains the target. Generic validation is the default; Claude-only restrictions are opt-in. Body markup is preserved.
- Supports a small scalar subset, not arbitrary YAML structures, typing, escaping or comment semantics. It is lint, not a security audit or a full YAML parser. A passing profile does not prove native Claude upload/discovery or model quality.
- Local execution used Python3.15 on macOS ARM. Subprocess evaluator reports its observed runtime. Existing unit tests were retained; three new test methods cover metadata, profile isolation and CLI flags. A first unit-test command used the workspace parent instead of repository and failed discovery; the corrected repository invocation passed, without test changes.
- Independent design/evaluation/review used separate agent contexts; exact serving model build and task cost are unavailable. No new LLM-generated-skill benchmark was run.
- Public source/package checks, hosted cross-platform CI and release-download receipts are reported separately when observed. Native Claude and other model-family limitations remain unchanged.
- The guide's provenance, already-covered topics and deliberately omitted advice are in [the source review](../../docs/claude-guide-review.md). Its PDF and extracted text remain outside the public manifest.
