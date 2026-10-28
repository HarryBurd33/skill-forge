# Research acknowledgment

Skill Forge's original instructions and helpers are MIT-licensed. This v0.4.0 bundle additionally includes the identified Anatomy renderer and CSS under their upstream MIT license, with complete notices and provenance retained. The design draws on Matt Pocock's MIT-licensed grill-me/grilling (commit 49dd158d1076134a641b33efb035946536778336), Anthropic's Apache-2.0 skill-creator (dbd4588f9e1033efb41dad4bef2f7947c8993d44), OpenAI's Apache-2.0 skill-creator (49f948faa9258a0c61caceaf225e179651397431), and official Agent Skills and host documentation. Research retrieved 2026-10-15.

See the [source ledger](https://github.com/HarryBurd33/skill-forge/blob/main/SOURCES.json) and [research/attribution record](https://github.com/HarryBurd33/skill-forge/blob/main/THIRD_PARTY_NOTICES.md) for exact paths, licenses and design influence. Upstream licenses remain applicable to upstream material; this MIT license does not relicense it. Skill Forge is independent of those authors and vendors.

## v0.4.0 integrations

Anatomy basic renderer/CSS: Copyright (c) 2026 Ryan, MIT. See the complete bundled license/provenance under resources/anatomy. REA workflow integration: Copyright (c) 2026 morluto, MIT; full notice is retained in subskills/reverse-engineer/LICENSE. Original adapter text narrows the upstream workflows and documents optional tool requirements. No rights to inspected third-party targets are implied.

## v0.4.1 macOS workaround

The optional original Python runner uses a process-local VFS overlay strategy informed by Tobias Franks's MIT-licensed screentime-archive build workaround (2026), pinned at [27fb07e3edb0f715c1e187fc41e6cb0458d63ab1](https://github.com/tobias-x/screentime-archive/blob/27fb07e3edb0f715c1e187fc41e6cb0458d63ab1/build.sh). No upstream implementation is bundled; the complete MIT notice is conservatively retained in [references/rea-macos-license.txt](references/rea-macos-license.txt).
