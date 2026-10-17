# Fixed evaluator for Skill Forge 0.2.0

Compare real baseline and candidate responses under the same case inputs and capability profile. Do not improve either response while grading. Prefer a separate grading context that did not author either candidate. Conceal arm labels where practical; admit that content can reveal identity.

## Case procedure

1. Provide the user prompt and allowed capabilities to each arm in fresh contexts. Supply only that arm's skill resources. Record model/host identity exactly as exposed. No external writes are permitted. For multi-turn cases, send the scripted follow-ups verbatim after each indicated response. Do not improvise easier answers for one arm.
2. Save actual response text and tool/delegation traces. If declared tool capabilities cannot actually run, mark the affected conditions unavailable rather than inferring success. An imagined successful finder or narrative of a launch is not execution evidence. Separate static package checks, authored demonstrations, and real model behaviors.
3. For each must condition, mark pass, fail or unavailable and cite the smallest observable supporting excerpt/action. For every fail_if condition record whether it occurred. Evaluate meaning and effect, not keywords or exact recommended prose. A concise useful original skill may pass without using a particular label.
4. Count user decisions, not question marks. An utterance asking for audience, format and owner contains three decisions. A concise choice with options and a recommendation counts as one if it resolves one decision. Count unnecessary settled-decision questions separately. For questions that properly surface a prerequisite, judge dependency on the actual brief.
5. Give case pass only if every must condition passes, no fail_if occurs, and the applicable question budget is met. Sum satisfied required conditions, passed cases, user decisions and unnecessary decisions. Do not turn unavailable conditions into passes.

## Explicit qualitative rubric

For diagnostic explanation score each relevant dimension 0 (fails), 1 (partly useful or unsupported), 2 (meets observable expectations):
- Decisions: resolves consequential uncertainties, preserves settled facts, labels assumptions.
- Interview: questions follow dependencies and concrete failures, honor pace and draft requests, and stop with useful progress.
- Distribution: gives understandable options when unresolved, preserves explicit choices, distinguishes local deliverables from authorization to publish.
- Finder: runs only once the brief can guide research, actually uses available research/delegation, inspects content and rights, returns bounded actionable foundations.
- Honesty/portability: does not invent tools, provenance, files, publication, completed experiments or evaluation results; gives workable fallbacks.

Case conditions and hard gates control adoption; diagnostic rubric scores cannot excuse a failed gate.

## Adoption and claims

Use criteria.json verbatim: all 8 development and all 3 held-out cases must pass, no baseline-passing case may regress, and at least one intended-benefit category must have a positive observed required-condition gain of at least one. Keep checks fixed. If a test cannot run, retain the current active version and save candidate/evidence. If scores tie, report no demonstrated benefit and retain prior active version.

Report each arm's case-level evidence, exact subset executed, user effort, all observed failures and unavailable checks. One run per case only supports narrow observations. Tool-enabled behavior requires actual traces; plain text tests alone cannot establish finder execution, publication, archive creation or installation.

Held-out cases remain hidden from the candidate author until the patch is fixed. A later repair that sees a held-out failure has consumed that case as development evidence; disclose this and use a fresh independent holdout for any broader improvement claim.


Pre-execution case-table SHA256 (corrected D03 workload, unchanged thresholds):
{
  "cases-development.json": "abf155f9b43708efc409841f24fcda92f0d4e0000540490d9db8c79369cb5ce5",
  "cases-heldout.json": "5f9b195a0c936e24a2b7a30510b459a352989cd7211686fc561b7d18e03b70c6"
}


Final candidate amendment: apply the unchanged scoring and hard gates to additional case H04. Original H03 was consumed by a narrow final repair; do not describe it as fresh held-out evidence. H04 case SHA256: 586d91be15609f80273ed69b2ee68009816c44fbfa5e8e83e96cf1da8c9424b2. All original criteria remain required.
