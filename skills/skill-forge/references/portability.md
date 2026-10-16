# Working across hosts and in plain chat

The canonical instructions use the shared Agent Skills format. Host discovery paths and invocation syntax belong in the repository's host guides, not in generated common instructions. Tools, model quality and permissions vary; a documented integration is not a runtime test.

If there are no file tools, ask the user to paste relevant files with filenames or upload their contents. If browsing is unavailable, request source excerpts with provenance or mark verification unavailable. Never claim to inspect a link you cannot access. If a licensed source is unavailable, draft original material from the brief and identify the missing comparison.

Return each generated file in a separate fenced block headed with its relative path. Include all needed supporting content. The user saves them under one folder named for the skill. For a single-file skill, that is `skill-name/SKILL.md`. Give a small manual test the user can perform, but mark it unexecuted until results arrive. Do not claim automatic adoption when the host cannot save files or run the required checks.

At pause/resume return a compact handoff: purpose and mode; confirmed decisions; assumptions/defaults; current version/files; examples and acceptance checks; unresolved questions; tests actually performed; private preferences kept separately; next action. A later chat needs this record or access to saved files. Do not include credentials. The user decides what sensitive material to carry forward.

The self-contained portable prompt is generated from the canonical skill, references, questions and templates. Its embedded sections are the resources referred to by the core. Script commands are optional instructions for a tool-enabled environment; a plain-chat model works from the embedded workflow. Outputting file contents is useful delivery, but is not installation, execution or publication.
