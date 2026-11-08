# Evidence proportional to the change

Before building, put concrete checks, expected outcomes, failure conditions, baseline and unavailable checks into the user-visible implementation spec. Preserve any review-first request. Before running candidates, freeze a small case table: id, input, expected observable outcome, failure conditions, required tools, maximum unnecessary questions, split, and evaluator. Separate development cases from regression cases; use held-out inputs not used to craft general changes. Reusing a known test is regression evidence, not held-out evidence.

Assess the visible pre-build ledger in [specification guidance](specification.md): settled material rule/group → discriminating input → expected/forbidden result → method/status. Verify actual coverage against the brief, not merely the presence of headings. A requirement assertion is not a concrete test; inputs that cannot distinguish a relevant wrong result leave a gap. Supplied acceptance inputs/results must be preserved, and applicable order contrasts, concrete non-activation requests, missing-value distinctions, material corrections and independent resource checks must be observable. Correct final artifacts cannot supply missing pre-build coverage. Count user decisions across the whole response, including questions appended after a draft.

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

## Optional resource preflight and captured-access audit

When evaluation depends on local companions or fixtures, declare its resource boundary before execution. Pin **every permitted input file**, including companion instructions, under explicit allowed roots; a root alone does not permit all its files. Record each file's provenance/source revision, classification and sharing constraint. Never copy a private fixture to an external executor without actual authorization. Prefer public revision-pinned or synthetic fixtures when sharing is unresolved.

The optional stdlib helper [evaluation_resources.py](../scripts/evaluation_resources.py) validates supplied metadata and evidence. It does not collect traces, contain an executor, authenticate capture completeness, grant sharing permission or evaluate model quality. Shell-log regex scans are not containment or proof of complete access capture. A successful utility run establishes only its narrow resource checks; existing behavioral, regression, held-out and adoption gates still apply.

With Python 3.9+, create a private JSON declaration outside the candidate-controlled files:

```json
{
  "schema_version": 1,
  "evaluation_id": "comparison-001",
  "execution": "external",
  "allowed_roots": ["/absolute/public-fixtures"],
  "files": [{
    "path": "/absolute/public-fixtures/companion.md",
    "provenance": {"source": "public repository URL or synthetic origin", "revision": "exact commit or fixture revision"},
    "classification": "public",
    "sharing": "external-approved"
  }]
}
```

`execution` is `local` or `external`; classification is `public`, `synthetic` or `private`; sharing is `local-only` or `external-approved`. External execution rejects every `local-only` entry. Private external entries additionally require an `approval_reference` pointing to existing authorization; a string is a record, not proof of permission. The helper never exports resource contents. Paths and provenance can themselves be private metadata: keep declarations and captures in private run records, sanitize before sharing, and do not put secrets in these fields.

```sh
python3 scripts/evaluation_resources.py freeze declaration.json > manifest.json
python3 scripts/evaluation_resources.py check manifest.json
# Run the evaluation only after successful preflight, using an appropriate capture facility.
python3 scripts/evaluation_resources.py audit manifest.json captured-access.json
```

Freeze adds exact SHA-256 hashes. Preserve the frozen manifest outside candidate control, hash its exact bytes and bind the capture to that hash and evaluation ID. Do not redirect freeze output over its input. Missing files, hash drift, symlinks anywhere in an input path, prefix-sibling escapes, undeclared resources and invalid sharing declarations fail preflight. This is a point-in-time check; it cannot prevent changes or reads between checks. Recheck immediately before execution and audit afterward. If a path includes a platform alias such as a symlinked temporary directory, use its actual directory path when declaring it.

The collector's supplied JSON evidence has this shape (replace both hashes):

```json
{
  "schema_version": 1,
  "evaluation_id": "comparison-001",
  "manifest_sha256": "64 lowercase hex digits: SHA-256 of exact manifest bytes",
  "capture": {
    "complete": true,
    "scope": "all-file-reads",
    "method": "named collector, host/version and coverage limitations",
    "reads": [{"path": "/absolute/public-fixtures/companion.md", "sha256": "64 lowercase hex digits: actual bytes read"}]
  }
}
```

`complete: true` asserts complete coverage of the executor's file-resource reads, including implicit companion loads; it must come from the actual collector, never be inferred from absent log matches. Every read needs its absolute path and the hash of the bytes actually read, rather than a later file hash. If the host cannot capture that coverage, mark capture incomplete and report the limitation. A file declared but unused is permitted; the audit does not prove that an evaluator used the inputs correctly.

The audit returns `FAIL` for an observed undeclared read or hash mismatch, even with partial capture; otherwise missing, malformed, partial or incorrectly bound capture is `INCONCLUSIVE`. Only complete, bound supplied evidence without observed violations returns `PASS`. Exit codes are 0 for successful freeze or pass, 1 for fail, and 2 for inconclusive. A missing capture argument or unreadable/malformed capture file is inconclusive. Failed or inconclusive resource checks prevent a scoring-ready/adoption claim; retain the previous active version. Do not relabel an unavailable capture as passed, or treat even a resource pass as the separate model-quality/adoption gate.
