# Evaluation resource checks

Evaluated 2026-11-08. Baseline source: fb341a035fc1cbc50eb5d6c4e794e320cf4f1800 (v0.4.1). One isolated candidate added an optional resource helper and guidance; the core interview instructions are unchanged apart from the version.

## Observed gap and repair

Four paired Prompt Forge evaluations previously read companion contracts outside their declared fixture. A correction attempting private companion export was rejected, then pinned public fixtures resolved the comparison. Existing guidance froze tools but did not explicitly pin companion resource scope, byte identity or sharing constraints. See the [recorded motivating case](https://github.com/HarryBurd33/prompt-forge/blob/ed5f890708a06fb717d75e16ab916d005b7e90ba/docs/VALIDATION-v0.3.0.md).

The optional helper now freezes exact files under permitted roots, provenance and sharing constraints; checks hashes before execution; and audits a separately supplied access record. It emits metadata rather than fixture contents. Existing criteria, evaluator and adoption rules remain intact.

## Executed evidence

Eight new tests exercised valid public/synthetic inputs; changed/missing resources; undeclared inside/outside reads; partial-capture failure precedence; missing/malformed/unbound capture; sharing/provenance; prefix-sibling and symlink boundaries; captured hash mismatch; and real CLI exit codes. The pre-existing version has no corresponding resource checker, so these are newly executed deterministic checks, not a measured model-output improvement.

The constructor and independent Astra/Extra High reviewer each ran the complete suite: **76 tests ran, 75 passed and one Windows-native test skipped**. Skill metadata/link validation passed. An independently reserved input was withheld until the candidate froze: identical bytes and basename in a sibling directory failed, the declared file passed, incomplete capture stayed inconclusive, and an observed outside read failed even with incomplete capture. Four expected classifications passed. This independently checks a boundary also covered by development tests; it is not a new statistical generalization claim.

The helper and tests were authored by Sol/Medium. The frozen helper SHA-256 is cffc0cc67e0b018ab82d4b078809d02f8fe2a4ee751fc3430d05e0e849f80cab; guidance dcb93668ddc23ce3ad4bb134d85508c316ecda15c604f39e9bcf87a623fd9c9e; tests 4e3020c61d2ac4ff9c8cf8404d903f705b5312d238b33be45efa52f06c12ccdc. Parent integration adds version and release documentation only. The integrated suite again ran 76 tests with 75 passes and one platform skip. Release selection/link/portable checks and four disposable clean installs passed. The existing managed personal installation was updated in place, preserving a private prior snapshot; source and installed tree hashes match f4cf8b9b2598b20e46ccda8a99441704172860546115c7cc0d29722a93018a3e.

## Limits and rollback

Local checks used Python 3.15/macOS. Subsequent hosted validation passed all six Windows/Linux/macOS and Python 3.9/3.13 jobs on reviewed head 67da05c20375fb671d29d82aa7d7b81088793d17: [PR run](https://github.com/HarryBurd33/skill-forge/actions/runs/42516359124) and [push run](https://github.com/HarryBurd33/skill-forge/actions/runs/42516354801). This verifies helper/package portability; it does not establish native host/model or Office behavior. Complete production executor capture was not demonstrated. The helper trusts supplied capture/provenance/authorization records, detects only represented violations and is not a sandbox, collector or permission service. Its successful tests establish narrow utility behavior, not guaranteed future model compliance. Missing production capture must not be marked passed.

Private audit state, original conversations, personal paths, raw model runs and installed snapshots are excluded. The source follows [PR #6](https://github.com/HarryBurd33/skill-forge/pull/6); the [v0.4.2 release](https://github.com/HarryBurd33/skill-forge/releases/tag/v0.4.2) records final publication and download verification. See the [future-session plan](../../docs/FUTURE-VALIDATION-PLAN.md) for remaining capability checks. Before installation preserve the previous managed copy; use the existing managed installer update guard for restoration, and reverse only this source commit while preserving later work.
