# Build a useful skill

Use the Agent Skills folder format: lowercase hyphenated folder/name, a `SKILL.md` with YAML `name` and `description`, then instructions. Name: 1–64 characters; description: 1–1024 characters. Make discovery specific enough to avoid activating for incidental mentions. Keep the main instructions short; link conditional detail from the point of use. Avoid mandatory boilerplate resources.

Define the workflow's actual decisions, output and completion criteria. Do not repeat general model capabilities or import host-only tool names into shared instructions. Prefer deterministic utilities for fragile repeated transformations; include dependencies, usage and failure behavior. Document whether integrations are optional and what happens if unavailable. Keep templates independent of Skill Forge and use relative paths within each delivered folder.

MIT is a proposed default for original material, not a license to relicense somebody else's work. Inspect repository and file-level licenses before reuse, pin a commit and retrieval date, retain required notices, and identify modifications. When reuse rights are absent or unclear, produce an original implementation of the ideas or ask for the missing permission; do not copy protected expression. Preserve upstream behavior and attribution during improvements.

For an existing skill: snapshot source and hash, list its intended behavior and the demonstrated gap, make a minimal relevant candidate, compare it with the snapshot, and explain changes and limitations. Never silently change neighboring skills or global settings.

Return installation/export steps and at least one natural-language invocation. Include activation and non-activation examples, validation results with evidence type, any tool dependencies and unfinished checks. A skill can be delivered provisionally when testing is unavailable, but the existing active version must remain until its required improvement checks pass.
