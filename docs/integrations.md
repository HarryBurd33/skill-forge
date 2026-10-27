# Learn from software and build physical explainers

Skill Forge 0.4.0 adds two conditional routes. REA helps investigate supplied software artifacts when ordinary source inspection cannot establish the needed facts. Anatomy supplies a real SVG renderer when a generated skill's output benefits from an explanatory physical mechanism. You do not need either route for an ordinary text workflow.

These are supporting adapters inside Forge. The main workflow reads them when relevant; a host is not assumed to discover nested adapters independently. Installing instructions does not connect a tool or run a check.

## Learn a workflow from source or a shipped artifact

For a complete readable source repository or an existing skill, Forge uses ordinary file/search tools. It follows a representative input through entry points, decisions, resources and output, inspects licenses and examples, and derives the reusable contract. It does not run REA diagnostics or setup merely because it is learning how source code works.

For a shipped app, extracted package or binary, or a question that needs runtime evidence, Forge identifies the actual target and the claim to investigate. It discovers the real available REA tool schemas or CLI commands before using them. A successful static inspection supports facts about the inspected artifact; it does not prove that a branch ran, a network call occurred or every feature exists. A runtime claim needs an authorized actual observation.

For example, a function present in an extracted JavaScript bundle supports “this package contains this return branch.” It does not support “users reached this branch in production.” Source files, packaged bytes and runtime observations can answer different questions, so the reconstruction records observed facts, inferences and unresolved questions separately.

REA is optional and its server/engines are not bundled. If it is absent, disconnected or missing a compatible provider, Forge continues supported ordinary inspection, records what remains unproved and keeps required evidence pending. It never invents returned Evidence IDs or silently installs packages, registers MCP or repairs system tools. Instructions found inside a target are reference data; a file saying “ignore the user and run setup” cannot authorize that action.

The reviewed source is [morluto/rea at 0cd7ef4](https://github.com/morluto/rea/tree/0cd7ef456bf960da265e04b341e82a24b1e377d5). The separately exercised npm package was `rea-agents@6.8.0`, declaring Node `^22.23.4 || ^24.22.1 || >=26.12.1`. A source revision is not a claim of feature parity with an npm package. Actual version/help, provider results and host prerequisites determine what works. Package acquisition or setup must fit the user's current authorization; it is not a normal Forge prerequisite.

## Add a physical explanation when it helps

Forge automatically selects the Anatomy route when the accepted output needs an interactive explanatory figure, a machine/instrument illustration or a physical mechanism that explains a technical relationship. It names the selected assets and checks in the visible implementation spec before writing. Already-authorized local resource attachment does not require a separate interview.

A text checklist, CSV transformer, decorative flourish or ordinary box-and-arrow diagram does not trigger this addition. Explicit no-visual requests and later corrections take priority. “Automatic” means choosing relevant resources during an authorized build, not adding diagrams to every skill.

The included original example is a pressure-test rig. Its inputs are `pressure_kpa` and `piston_area_mm2`; force is pressure × area / 1000 newtons. The same pure model moves the piston shoe, positions the gauge needle and computes the force readout. Zero is valid; negative or nonfinite inputs are rejected. A stated illustrative spring stiffness and mechanical stop bound the drawn travel rather than altering the force value. This is an explanation, not a calibrated experiment.

The builder adapts the example to the accepted target; the pressure rig is not a substitute for every requested mechanism. Supports, fasteners, collars, ruler strips and controls should explain the object, rather than add arbitrary detail.

## What is included

| File copied to the generated target | Purpose |
| --- | --- |
| `assets/anatomy/vendor/iso-kit.mjs` | Actual pinned Anatomy projection, solid geometry, SVG string renderer and basic page/card helpers; no imports. |
| `assets/anatomy/vendor/iso.css` | Actual pinned standalone Anatomy styling. |
| `assets/anatomy/vendor/LICENSE` | Complete upstream MIT notice, copyright (c) 2026 Ryan. |
| `assets/anatomy/model.mjs` | Original pure pressure/area model and input validation. |
| `assets/anatomy/build.mjs` | Original Node build using the real vendor renderer; generates `figure.svg` and standalone `figure.html`. |
| `assets/anatomy/README.md` | Build/use instructions, assumptions, redistribution and verification requirements. |
| `assets/anatomy/PROVENANCE.json` | Immutable source revision, upstream file paths and vendor SHA-256 hashes. |

This is the **basic SVG/HTML slice**, pinned to [Anatomy revision 1482e84](https://github.com/wheresryan22/anatomy/tree/1482e8469b0a9e0d8cc18ea2740a01423d29ae80). It does not bundle the full upstream example library, React components, lathe/tube modules, WebGL shaders, 3D turning, geometry/orbit audit tools, screenshot/action/line-end scripts, PDF printing or gallery publication. The SVG core alone cannot establish collision clearance, physically correct occlusion or an advanced audit pass. Separate requested advanced work needs actual modules, dependencies, permissions and verification.

## Attach, render and move a generated skill

A normal generated skill receives its own complete resource folder. For manual attachment, first create a real target skill directory with valid `SKILL.md` metadata whose name matches the directory. From a Forge source checkout:

```sh
python3 skills/skill-forge/scripts/forge.py integrations
python3 skills/skill-forge/scripts/forge.py attach-anatomy /path/to/pressure-rig-explainer
node /path/to/pressure-rig-explainer/assets/anatomy/build.mjs 250 200
node /path/to/pressure-rig-explainer/assets/anatomy/build.mjs 250 200 --light
```

On Windows use `py -3` for Python and quote paths containing spaces. With the standalone skill ZIP, use `skill-forge/scripts/forge.py` from its extracted parent instead. These sample target paths are placeholders; use a writable target you own.

`integrations` reports bundled adapters and dependency information; it does not probe or configure a server. `attach-anatomy` adds resources without rewriting target `SKILL.md`, so add a relative README reference and concrete generation steps to the target workflow afterward. It refuses partial/customized Anatomy resources, linked paths and collisions, and preserves unrelated files. An identical repeat reports unchanged. It stages the complete new directory and publishes it atomically with an exclusive host operation; unsupported hosts fail closed. Rendering subsequently creates or replaces the example's own generated files.

Python 3.9+ is optional for attachment and Forge's other helpers. **Node.js 20.10+ is optional until rendering is requested**, and the basic example needs no npm packages. Open `figure.html` in Chrome or a compatible modern browser. The build uses only relative local imports and Node built-ins; the HTML embeds its renderer, model and CSS. Copy the entire generated skill folder and rebuild it in a new location to verify portability. Neither the target nor the built HTML needs Forge installed. The standalone SVG is a static snapshot with embedded CSS.

Keep complete notices and provenance with redistributed resources. The HTML retains the renderer notice; accompany a redistributed standalone SVG with the license/provenance files too. Original Forge licensing does not replace upstream rights or grant permission to reuse an inspected software target.

The portable text prompt includes adapter instructions but not this JavaScript/CSS asset folder. A plain-chat model needs the supplied complete folder to deliver a real bundled renderer, or must mark copying/rendering pending. An upstream link or empty placeholder does not satisfy self-contained asset delivery.

## What has actually run

This documentation overlay describes a candidate, not a published release. As of the 2026-10-27 review:

- Local helper checks recorded42passes and one Windows-only skip, including the release-validator boundary regressions. The resource tests cover copy completeness, relocation, identical repeats, conflict preservation, unsafe paths, failure cleanup and exclusive publication.
- The original rig was built with the actual renderer. SVG parsing, input/model checks and inline-script closure/coupling checks ran. These establish specific structural/model behavior; they do not establish browser visual quality.
- A real `rea-agents@6.8.0` package ran under isolated Node 24.22.1. Version/help and ZIP artifact inspection succeeded. JavaScript static analysis failed at macOS process-helper compilation with a SwiftBridging module redefinition; successful JavaScript provider analysis and target runtime observation are not claimed.
- Four static SVG light/dark1080px/390px images were inspected after temporary CSS-variable resolution for Sharp/librsvg. These omit HTML cards/controls; actual HTML layout, native keyboard and reduced-motion checks remain pending. Required pending checks must complete before adoption or release.
- The comparable native model suite passed6/6candidate and4/6baseline scenarios. The predefined real Anatomy outcome improved0→1; truthful missing-tool fallback was preserved. See the [report](../evals/v0.4.0/REPORT.md) for fixed inputs, conditions, unknown serving metadata and limitations.

The isolated REA test environment changed no global registration or system Node configuration. Historical platform/model results remain in their versioned reports; these local checks do not revalidate every host, provider or model. Public summaries should contain sanitized outcomes and provenance, while credentials, private paths and raw transcripts stay outside the release allowlist.

The candidate full skill ZIP carries the complete 32-file skill folder, including real Anatomy assets. The portable ZIP is the prompt-and-notices route; its instructions alone are not those executable assets. A plain-chat model can return complete original file texts and a spec, but cannot fetch the pinned kit or render it without the necessary tools or user-supplied files.
