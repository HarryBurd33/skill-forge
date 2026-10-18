# Skill Finder

Skill Finder is the bundled research sub-skill at `skills/skill-forge/subskills/skill-finder/SKILL.md`. Skill Forge loads it after the idea has a usable brief and before implementing the skill. Nested folders alone do not guarantee native discovery by every host.

With subagents available, Skill Forge sends one researcher a sanitized brief: purpose, activation, inputs and outputs, material constraints, acceptance checks, delivery choice and search limits. The parent can prepare tests while research runs, then uses the findings to choose a foundation. Private examples and credentials do not belong in public search queries.

The default search takes about five minutes, shortlists at most five candidates and inspects the strongest three. It searches GitHub and uses Hugging Face, primary documentation or papers when they fit the problem. Actual instructions or implementation, dependencies and relevant licenses/notices matter more than stars or a repository description. Each recommended foundation records source URL, retrieval date, commit/revision when available, inspected files, reuse rights, fit, gaps and an adopt/adapt/reference/reject recommendation.

A verified resource may become the foundation for the generated skill, with its required attribution. Sometimes an existing skill is already sufficient. An unsuitable or unlicensed candidate instead leads to another source or an original implementation; finding a public file does not grant copying rights. Finder does not install or execute fetched code, publish files or change configuration.

## Use

Ask Skill Forge to refine an idea normally. Once it is ready, the research stage runs before implementation. You can also say:

> Use Skill Finder on this refined brief. Search no more than three promising resources and explain which foundation would help before building.

Say “skip finder” to decline research, or resume with a still-current saved report. A changed requirement can require refreshing the affected findings. A research result that exposes a design gap returns that decision to the interview.

When subagent launch is unavailable, the main model says so explicitly, performs the bounded search directly, and reports actual queries, inspected results and any verification gaps. Without browsing, it can inspect supplied references, return a pending research task and draft original provisional files. It must not invent repository findings or successful tool actions. The portable prompt includes the complete Finder instructions and report template.

To use Finder independently, copy its entire `skill-finder` directory into a host's skill directory using that host's setup instructions. Its workflow has no dependency on Skill Forge; normal tool and permission limits still apply. The Skill Forge installer includes Finder as a nested component and does not create a second personal installation automatically.

## Test evidence

The versioned evaluation report records whether delegated research and direct-search fallback actually ran. File validation alone does not establish good source selection or licensing judgment.
