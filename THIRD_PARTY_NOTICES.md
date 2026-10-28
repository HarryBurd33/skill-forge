# Third-party research and notices

Skill Forge's original material is licensed under [MIT](LICENSE). The original builder and earlier conceptual foundations were independently implemented. The v0.4.0 additionally bundles the explicitly identified Anatomy renderer/CSS and retains complete MIT notices for its Anatomy and REA integrations, as described below. This research acknowledgment does not relicense any upstream material.

| Reviewed material | Pinned commit | Inspected license | Credit |
| --- | --- | --- | --- |
| Matt Pocock, `grill-me` and `grilling` | `49dd158d1076134a641b33efb035946536778336` | [MIT](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/LICENSE) | Copyright (c) 2026 Matt Pocock |
| Anthropic, `skill-creator` and evaluation helpers | `dbd4588f9e1033efb41dad4bef2f7947c8993d44` | [Apache License 2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/LICENSE.txt) | Copyright 2026 Anthropic, PBC. |
| OpenAI, `skill-creator` | `49f948faa9258a0c61caceaf225e179651397431` | [Apache License 2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/LICENSE.txt) | OpenAI; the inspected license appendix contains the standard copyright placeholder rather than a filled attribution. |

The official Agent Skills specification, Agent Skills evaluation guide, OpenAI documentation, and Claude Code documentation were consulted as documentation, not copied into this distribution. No blanket permission to reuse their prose or assets is asserted.

[SOURCES.json](SOURCES.json) identifies the exact retrieved material and dates; [the comparison](docs/foundations.md) explains the design influence. For current bundled files and any future contribution that copies or substantially adapts third-party expression, record the affected files and modifications, include the applicable license and required notices in both repository and release packages, and verify compatibility before merging. MIT for original work does not erase upstream obligations.

Skill Forge is an independent project and is not affiliated with or endorsed by these authors or product vendors.

Anthropic’s *The Complete Guide to Building Skills for Claude* was reviewed on 2026-10-26 as a conceptual reference for optional metadata checks. The PDF and its prose/templates are not redistributed. No permission or license is inferred from Anthropic’s separately licensed skill repository. See [the review](docs/claude-guide-review.md) and source ledger.

## v0.4.0: bundled material and retained notices

| Source | Pinned revision | Included material and changes | License/credit |
| --- | --- | --- | --- |
| [morluto/rea](https://github.com/morluto/rea/tree/0cd7ef456bf960da265e04b341e82a24b1e377d5) | `0cd7ef456bf960da265e04b341e82a24b1e377d5` | Original scoped workflow adapter informed by routing/evidence practice; no REA server or provider engine bundled. | MIT; Copyright (c) 2026 morluto. Complete notice: [reverse-engineer/LICENSE](skills/skill-forge/subskills/reverse-engineer/LICENSE). |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy/tree/1482e8469b0a9e0d8cc18ea2740a01423d29ae80) | `1482e8469b0a9e0d8cc18ea2740a01423d29ae80` | Actual `kit/iso-kit.mjs` and `kit/iso.css` copied byte-for-byte to the basic resource slice; original Forge adapter/model/build example added. | MIT; Copyright (c) 2026 Ryan. Complete notice: [vendor/LICENSE](skills/skill-forge/resources/anatomy/vendor/LICENSE). |

The [resource provenance](skills/skill-forge/resources/anatomy/PROVENANCE.json) and [source ledger](SOURCES.json) record immutable source paths, vendor hashes and modification scope. Copies attached to generated skills must retain their complete notices and provenance. Built HTML includes the renderer's notice; standalone SVG redistribution should be accompanied by the license/provenance. Original Skill Forge MIT licensing does not erase these obligations or relicense an inspected target.

Only the basic SVG core/CSS is bundled. Advanced upstream modules, browser verification scripts, the example library and publishing workflows are excluded. See [integration scope](docs/integrations.md). Earlier historical acknowledgments describe their own release scopes; the table above records the later code addition.

## macOS compiler overlay strategy

Consulted [tobias-x/screentime-archive](https://github.com/tobias-x/screentime-archive/tree/27fb07e3edb0f715c1e187fc41e6cb0458d63ab1), MIT, copyright (c) 2026 Tobias Franks. Forge’s runner is original; the complete consulted upstream notice is retained in [rea-macos-license.txt](skills/skill-forge/references/rea-macos-license.txt).
