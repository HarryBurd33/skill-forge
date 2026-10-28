---
name: anatomy
description: Add an Anatomy-based isometric mechanism or interactive technical explainer to a generated skill when its output benefits from a physical explanation. Skip ordinary text/CSV skills, decorative-only additions, generic box-and-arrow diagrams and explicit opt-outs.
license: MIT
metadata:
  version: "0.4.0"
---

# Conditional Anatomy adapter

This adapter uses the real basic renderer from [Anatomy](https://github.com/wheresryan22/anatomy/tree/1482e8469b0a9e0d8cc18ea2740a01423d29ae80) with original scoped guidance. It is a supported basic SVG/HTML slice, not the full upstream WebGL, React, 3D, printing or gallery workflow.

## Decide relevance without another interview ritual

Automatically select this path when the agreed generated skill needs an interactive explanatory figure, a real mechanism/machine illustration, or a physical model that helps explain a technical concept. Make the selection and exact artifacts visible in the pre-build spec; do not ask another approval for already-authorized local resources. A plain action list, CSV transformer, text-only result, ordinary flowchart or explicit no-visual instruction does not qualify. A purely decorative flourish is not enough. Respect final user corrections and effort/cost limits.

If a full upstream Anatomy skill is already available and its scope fits, inspect its actual version/resources before using it. Otherwise use the bundled basic renderer. Never claim advanced modules or audits are included when they are not.

## Include the implementation in the target

With file tools, run `python3 scripts/forge.py attach-anatomy /path/to/target-skill` from the Forge folder, or copy the complete bundled resource slice under the target's assets/anatomy/ while preserving its license/provenance. The helper must refuse conflicting custom files; it does not rewrite the target SKILL.md. Add a relative resource link and concrete generation/use steps to the generated skill. Inspect actual returned paths rather than assume attachment succeeded.

The kit, CSS, complete MIT notice and original demonstration/model/build resources belong in the generated target; a floating upstream link or a stub that requires Forge is insufficient. Run its build using Node and relocate the entire target to check imports and references. The target then works without Forge installed. Do not attach these resources to unrelated targets or alter user-wide configuration.

## Model first, then mechanism

Define the quantity/relationship, units, assumptions, valid zero and invalid inputs before geometry. Choose a recognizable machine or instrument whose moving part explains that relationship. Drive motion, readout and caption from the same pure model. Distinguish measured physical behavior from an explanatory analogy; a diagram is not an experiment.

Use the actual renderer APIs for projection, solids, four-tone shading and depth order. Give detail a mechanical purpose: supports, fasteners, rulers, bushings and controls rather than arbitrary dense decoration. Read the [bundled resource README](../../resources/anatomy/README.md) and original demo for the supported API/build path; the demo is a starting example, not every requested output. Adapt it to the user's accepted mechanism and inputs.

Verify the generated SVG is well formed, paths finite, output facts/model values correct, controls keyboard usable, small layout legible, reduced-motion behavior appropriate, and light/dark themes inspectable. Use actual browser rendering when available. Static checks cannot prove visual quality or geometry clearance; missing browser or Node remains a named pending check. Claim no WebGL/3D/collision/print audit without its actual modules and executed evidence.

Without filesystem/execution access, return saveable original instructions and an exact pinned dependency/file map with missing implementation/verification explicit. Do not claim real assets were copied or a figure rendered. Keep the target provisional when required evidence is unavailable. External gallery/publication remains a separate authorized action.
