# Two improvement loops

## Scope and state

Target updates serve the user's workflow. Builder updates serve a reusable decision or process. First decide which loop an observation belongs to. Keep private preference values and raw transcripts outside source, release files and shared defaults. Use synthetic/minimized public cases only after checking for identifying information. Credentials never belong in a session export.

Store session and run records in a user-controlled private directory outside any skill or repository, for example `~/.local/state/skill-forge/`. The helper enforces permissions for state it creates; do not claim that makes arbitrary storage encrypted. In a restricted environment choose an allowed private location and explain persistence limits. Without files, return the handoff template for the user to retain.

## Candidate procedure

1. Record observation, reproducible input, affected outcome and hypothesis. Set effort limit (default 30 active minutes) and max candidates (default 3). Snapshot baseline including notices and customizations.
2. Before patching, freeze acceptance criteria and evaluator in the private run directory. Identify regression and held-out cases, evidence kind and the minimum observable benefit. Criteria cannot be weakened by a candidate. Each attempt counts toward the limit, including rejected or inconclusive attempts.
3. Patch an isolated copy. Run baseline and candidate under comparable conditions. Capture actual output artifacts and hashes; use independent grading where available. A self-reported pass without artifacts is insufficient.
4. If all required checks pass and benefit is demonstrated, automatically replace the active writable target, record the change and keep the prior version. Otherwise leave the active version unchanged and retain candidate/evidence for later. Read-only installations receive a candidate package and installation handoff, never a false adoption claim.
5. Verify installed version, preserve rollback, and synchronize authorized managed copies. Refuse overwrite of a changed destination; compare its customization with the candidate and merge only the relevant requested change, then reevaluate. Never force-reset a custom copy.

The helper's `prepare`, `submit`, and `rollback` commands implement an auditable local gate; see helpers.md. It checks hashes and declared evidence, not a malicious evaluator's honesty. The acting agent remains responsible for genuine execution, fixed criteria, public/private separation and authorization. Protect run records from candidates; use an external trusted evaluator when stronger isolation is needed.

## Library evolution

For a proposed question, search existing records by decision and synonyms. Prefer revising a question's ask/skip conditions over creating a duplicate. State why the answer changes the result and when to skip it. A new accepted question needs a motivating case and a regression case; broader claims need held-out checks. Retire questions that no longer help. Accepted → revised preserves stable ID and records rationale; retired records stay searchable for history but are not asked.

Personal examples may motivate a general rule, but values must not become defaults. “Ask about protected commitments when planning capacity” can generalize; “everyone sleeps 23:00–07:00” cannot.

## Stop and report

Stop on criteria met, no demonstrated marginal benefit, or limits reached. Save unresolved observations, next action, evidence status and candidate path. Include what changed, why, actual results, limitations and rollback command/path. Local successful adoption does not itself authorize publishing, upstream writes, paid calls or background jobs. Persistence means revised files plus records; it is not retraining or guaranteed cross-chat memory.
