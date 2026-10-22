# Candidate 8: planning coverage diagnosis

Status: design diagnosis only. Candidate 8's independent verdict establishes required K02-A-N2 failure; the independent judge completed its audit. This document does not rescore that verdict, accept a lesson, propose an authorized ninth candidate, or change source/tests. Stable 0.2 remains active. No L fixture or other case contents were opened.

## What the observed response establishes

The frozen builder already instructs a coverage map from material requirements to observable checks (`SKILL.md`, lines 54–56; `references/specification.md`, lines 13–15). It explicitly calls for separate activation/non-activation checks and discriminating order inputs. Candidate 8 added exact contract detail at the visible build boundary. Its K02 response now supplies both input schemas and the exact CSV header before the artifact (actual return, line 1), and preserves the newly supplied 8/6/−2 acceptance example as a planned check (line 5).

Its check list nevertheless leaves two distinctions uncovered. It states that prices are excluded (line 1) but gives no price request with an expected non-activation decision. “Manifest order B,A with an extra count-sheet item C → rows B,A only” (line 8) tests manifest membership/order as a general assertion, but never specifies a contrasting count-sheet order. A test following the second list's order could not be distinguished from the desired behavior from those inputs alone. The final skill states the right ordering and exclusion rules; that does not complete the missing pre-build verification plan.

This one execution does not show that coverage maps never work, that more prose always fails, or that a particular replacement will succeed. It shows that instructions requesting a map produced an untraced list whose coverage gaps were not caught before the artifact. Candidate 8's narrower exact-contract correction does not establish completion of the distinct verification-coverage requirement.

## Are these checks supported by the request?

Yes. The actual corrected K02 input explicitly restricts output to manifest items **in manifest order**, and explicitly excludes **prices, replacement purchases and authenticity judgments**. An order contrast and a concrete excluded request test those settled rules; they do not introduce a new domain requirement. The fixed N2 criterion specifically requires differing manifest/count-sheet orders and a price non-activation check. The prospective numeric append now supplies the previously undisclosed example. Historical scores remain unchanged. The exact negative or ordering example can be synthetic and need not be hardcoded into shared builder defaults.

## Structural alternative to consider in a future authorized run

Replace overlapping reminders with one small, visible **contract-to-check ledger at the build boundary**, rather than append another general instruction to “cover everything.” Each material claim or related group would have: **settled rule → discriminating input → expected result / failure → method and status**. The assistant would populate this ledger from the brief before emitting target contents, then compare the brief's material claims with the rows. An unpaired boundary or an input that cannot distinguish the forbidden behavior is a coverage gap to fill from settled context.

The distinction is an inspectable output structure and a coverage operation, not a claim that a new heading guarantees compliance. A few numbered lines can serve as the ledger; no mandatory JSON, script, long table or empty section is needed. One fixture can cover several rules if their contrasts and expected results are explicit. Only relevant dimensions enter it: for example, order gets contrasting sequences when order matters; an exclusion gets a concrete request and expected routing decision when activation boundaries matter. The shared instructions would contain no domain names, fixed field names or fixture numbers.

This is an assistant authoring step, not a fixed interview or another approval. It should add no questions for settled requests, preserve optional review and same-turn draft, and work in plain chat. With no execution tools, methods/status remain “planned manual/model check; unexecuted”; the ledger does not turn a paper plan into a behavioral pass or authorize adoption. The source change, if later authorized, should consolidate the existing map requirements rather than grow a second competing questionnaire.

## What would establish improvement

Register that structural hypothesis prospectively; retain the current failed outputs and fixed checks. Independently assess whether the visible rows actually trace material requirements and discriminate prohibited behavior, rather than merely having the right headings. Compare under matching inputs/capabilities/model, retain all required regressions and question budgets, and require the broader frozen suite and independent held-out evidence before a general improvement claim. A new structure could increase verbosity or cause another omission; measure usefulness and effort as well as coverage. No lesson is accepted and no source update is warranted solely by this diagnosis.

Evidence identities: frozen candidate 8 core `36706d8fddada6c9f3b2675b0add9b6038d6592eca516a7e1f493f191bec198d`; corrected K fixture SHA-256 `9de8dd75475d05e18b9d0bb2ac597387c0e6a05b6dc9d55d5636216c0040d210`. The exact ended return and its hash are retained in the execution index; this diagnosis used only K02's supplied input and ended candidate response plus the frozen builder source.
