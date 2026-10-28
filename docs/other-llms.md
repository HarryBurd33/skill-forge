# Use Skill Forge with another capable LLM

The portable prompt contains the core workflow and supporting resources in one text file. It is intended for capable instruction-following models that can handle its length. It needs no Codex, Claude Code, Python, paid API or custom service. A prompt cannot grant missing tools or guarantee equal quality across products.

## Start in a chat

1. Extract the **portable prompt ZIP** from [the release downloads](../README.md). Use `skill-forge-prompt.md`, not only the installed skill's short `SKILL.md`.
2. Upload that file if your host accepts Markdown/text attachments, or paste its complete contents into a new conversation. If it cannot fit, choose a larger-context capable model; silently omitting resources changes the workflow.
3. Give your idea, or supply conversation/project material to turn into a reusable skill. State the intended host and available tools if known.
4. Ask for complete skill-file contents, a folder/package when tools permit, or an explicitly authorized repository. The skill's delivery destination is separate from what its eventual output will be.

Example:

```text
Use the attached Skill Forge prompt. Based on the conversation excerpts below,
build a skill for the repeated workflow we agreed on. Preserve my final corrections.
Show a spec and how it will be checked before building; pause for my review.
[Paste relevant conversation excerpts with private details removed.]
```

Without a review-first request, Skill Forge shows the spec and continues authorized implementation. Use “quick,” “thorough,” “expert challenge,” “draft now,” “skip,” “use your judgment” or “resume” to control the process. A detailed conversation can settle most questions; a complex vague idea can need several focused rounds.

## Supply references and receive files

Give each source a title, URL or filename and its actual content when the model cannot open it. Include relevant user decisions, corrections, examples and failures. For a project supply an overview plus relevant files or permitted access. Do not assume another chat, project history or linked file is visible.

The model can return a file map and a complete code block for each file, such as `meeting-actions/SKILL.md`. Save exact contents with the shown names and relative folders, including referenced resources. Install using the target host's documented paths; the generated skill does not need Skill Forge installed. A simple reusable prompt may need one Markdown file; supporting resources require a directory.

## What changes without tools

- **No files:** supply relevant contents; actual file inspection remains unverified.
- **No browsing:** external Finder research and license verification cannot run. Original provisional files can use supplied material with missing checks recorded.
- **No subagent tool:** the parent works directly and says it cannot launch a subagent. Planned roles are not launched workers.
- **No execution/independent evaluator:** receive predefined cases and candid limited review. Narrated success is not a test; required behavioral adoption checks remain pending.
- **No persistence:** save the brief, spec, decisions, review state, check status and next action as a private handoff. Paste/upload it next time and say “resume.”
- **No GitHub writes:** receive local contents and publication steps. Choosing GitHub does not itself publish anything.

Keep credentials, raw transcripts, sensitive examples and private preferences out of shared files. Use placeholders and local configuration. Revised files and session records provide continuity; they do not retrain the model or create memory across unrelated conversations.

Test a representative request before relying on a new host/model. The [compatibility record](compatibility.md) distinguishes actual checks, documented support and unverified combinations.

## Optional REA and Anatomy resources

The portable prompt contains workflow instructions, including the nested adapters. It does not embed the Anatomy renderer's JavaScript and CSS, and it cannot grant filesystem, execution or REA access. For a visual target, also supply the complete `resources/anatomy` folder from the skill/source ZIP, including vendor files, license and provenance. With file tools, copy that complete slice into the generated target's `assets/anatomy` folder. With text-only access, receive an exact pinned file map and original provisional instructions; actual asset attachment, rendering and required visual checks remain pending. A link to upstream source alone is not a completed self-contained renderer.

[REA](integrations.md#learn-a-workflow-from-source-or-a-shipped-artifact) is optional. Readable complete source still uses normal file tools. Without REA or a compatible provider, record shipped-artifact/runtime questions as unresolved and continue the inspection that the available files support. Never claim an Evidence ID or execution that did not occur. Installing or registering a tool needs the user's current authorization.

When real assets are available, the bundled SVG/HTML example needs Node.js 20.10+ and a browser for visual checks, with no npm dependencies. The built HTML embeds its renderer, model and CSS. Keep notices/provenance when sharing; the generated target and built HTML do not depend on Forge. See [the exact scope](integrations.md#what-is-included).

The candidate full skill ZIP carries the complete skill folder, including real Anatomy assets. The portable ZIP is the prompt-and-notices route; its instructions alone are not those executable assets. A plain-chat model can return complete original file texts and a spec, but cannot fetch the pinned kit or render it without the necessary tools or user-supplied files.

The v0.4.1 portable prompt includes the macOS recovery instructions and notices, but not the executable Python runner. Use the full skill/source package when that optional helper is required.
