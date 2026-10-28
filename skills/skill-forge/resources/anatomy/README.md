# Anatomy SVG resource slice

This folder is self-contained. Copy the whole folder, including [vendor/LICENSE](vendor/LICENSE), with a generated skill. The renderer and CSS are actual unchanged files from the pinned Anatomy revision recorded in [PROVENANCE.json](PROVENANCE.json). The pressure rig is an original example rather than a copied upstream example.

Render from any working directory with Node.js 20.10 or later:

```sh
node /path/to/your-skill/assets/anatomy/build.mjs 250 200
node /path/to/your-skill/assets/anatomy/build.mjs 400 200 --light
```

No npm installation is needed. The build writes `figure.svg` and `figure.html` beside [build.mjs](build.mjs), so use a writable copy. These are generated outputs and a subsequent build replaces them. Open the HTML in Chrome or another modern browser. It embeds the complete renderer, model and CSS, works without a server or external dependencies, and can be copied independently. The SVG is a standalone static snapshot with embedded CSS.

[model.mjs](model.mjs) validates finite nonnegative numeric pressure_kpa and piston_area_mm2. Zero is valid. Force in newtons is pressure_kpa × piston_area_mm2 / 1000. A spring stiffness of 10 N/mm converts this force to illustrative piston travel; the drawing has a 16 mm mechanical stop. Force remains unbounded by that illustrated stop. The same pure model drives the force readout, gauge needle and piston shoe position. This explanatory model omits losses and is not a calibrated instrument.

The original drawing has 59 named purposeful solids: the base and four feet, mounting screws, twin paired guide columns with collars/washers/nuts, crosshead, specimen fixture, spring seats, piston rod and shoe, actuator barrel and cap fasteners, hydraulic manifold and valve, gauge and scale. Pressure is a native keyboard-accessible range control; area is a labeled number input. There is no autonomous animation. A reduced-motion rule disables animations and transitions, including those in vendor CSS. The theme button switches light/dark appearance.

For a generated skill, add a relative reference to this README in its workflow and specify its inputs, build location and visual verification requirements. The attachment helper never rewrites target SKILL.md. No Skill Forge installation or runtime is required after copying this folder.

Before claiming completion, actually run the build; parse/check the SVG; inspect desktop and 390px mobile output in both themes; use the slider's arrow/Home keys and area control; verify 0 × area = 0 N and 250 × 200 / 1000 = 50 N; reject negative/nonfinite input; compare piston positions for two valid inputs; test reduced motion. Record checks not run as unexecuted. The bundle itself does not supply browser captures or proof that these visual checks passed.

Keep the complete [MIT notice](vendor/LICENSE) and [provenance](PROVENANCE.json) with redistributed resources and built HTML. When redistributing a standalone SVG, accompany it with that notice and provenance too.
