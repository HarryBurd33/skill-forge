# Use Skill Forge in Claude Code

Use the same canonical Skill Forge folder as Codex. No Claude-only fork, marketplace listing or paid API service is required by Skill Forge; you still need Claude Code access. Its [setup guide](https://code.claude.com/docs/en/setup) documents macOS, Windows and Linux on x64 or ARM64. Intel/x64 describes processors, not an operating system. Native Windows can use PowerShell; Git for Windows is optional for Bash tools, and WSL is an alternative.

Python is optional for interviewing, the spec and file output. Only optional helpers require Python 3.9 or later. **Native Claude Code execution remains unverified here**; documentation-supported installation and helper checks are distinct.

## Install without commands

1. Download and extract the [repository or skill ZIP](../README.md).
2. Find the entire `skills/skill-forge` folder in the repository, or `skill-forge` in the skill ZIP.
3. Choose a destination below, create missing parents, and copy the complete folder. Keep all supporting files, bundled resources and nested adapters.
4. Start Claude Code in your project and enter `/skill-forge`.

| Scope | macOS/Linux | Windows |
| --- | --- | --- |
| Personal local projects | `~/.claude/skills/skill-forge` | `%USERPROFILE%/.claude/skills/skill-forge` |
| Project repository | `<project>/.claude/skills/skill-forge` | `<project>/.claude/skills/skill-forge` |

Replace `<project>` with your repository path; `~` or `%USERPROFILE%` means your home folder. Windows also accepts native backslash paths. Personal skills take precedence over same-name project skills, so normally choose one scope. This local installation does not upload to your Claude account, install on other devices or automatically reach Cowork/cloud sessions. [Official skills reference](https://code.claude.com/docs/en/skills).

## Optional managed installation

Run from the **downloaded repository directory**; replace the project path when choosing that scope.

macOS/Linux:

```sh
# Personal
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.claude/skills/skill-forge"
# Or project
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "/path/to/project/.claude/skills/skill-forge"
```

Windows PowerShell:

```powershell
# Personal
py -3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.claude/skills/skill-forge"
# Or project
py -3 skills/skill-forge/scripts/forge.py install skills/skill-forge "C:/path/to/project/.claude/skills/skill-forge"
```

Use `python` instead of `py -3` if that is your working Python command. Keep paths with spaces quoted. For the standalone skill ZIP use `skill-forge/scripts/forge.py` and source `skill-forge` from the extracted parent. The helper refuses an existing destination.

## First use

```text
/skill-forge Create a skill that turns rough meeting notes into an action list.
Keep unknown owners and dates explicit. Use your judgment.
```

Skill Forge reads context, asks needed questions and challenges material weaknesses. It shows an implementation spec and verification plan before building. Say “review first” to pause for edits; otherwise authorized work continues. Useful available subagents can research, build independent components, review or execute checks. Delivery includes skill files, examples and a report identifying what really ran.

You can instead say `/skill-forge Based on this conversation, build me a skill`, or supply a project workflow. Only visible or supplied/authorized retrieved material is available. Final user corrections govern; private details belong in local configuration, not public instructions. “Quick,” “thorough,” “expert challenge,” “draft now,” “skip” and “resume” remain available. Supply the saved session/handoff to resume later.

## Update and remove

From a newer downloaded repository, update a helper-managed personal copy:

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.claude/skills/skill-forge" --update
```

Windows PowerShell:

```powershell
py -3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.claude/skills/skill-forge" --update
```

For project scope use its installation destination. Customized copies are refused; reconcile wanted changes into the canonical source, verify, then synchronize. For a manual installation back up the old folder outside the scanned skills directory before comparing and replacing it. Keep private sessions separate. Symlinks are optional, not a Windows prerequisite.

To remove, move that installation outside the scanned skills directory. Use an unused backup path or your file manager. Personal examples:

```sh
mv "$HOME/.claude/skills/skill-forge" "$HOME/skill-forge-backup"
```

```powershell
Move-Item -LiteralPath "$HOME/.claude/skills/skill-forge" -Destination "$HOME/skill-forge-backup"
```

Use your project path for project scope. Claude watches established skill directories; use `/reload-skills` if the top-level directory was created after the session started. Start a fresh session to verify removal because already-loaded content can remain. [Update/removal reference](https://code.claude.com/docs/en/skills#edit-a-skill-during-a-session).

## Tools and portability

The common skill requires no Claude-specific substitutions, shell injection, hooks or permission declarations. Installation grants no browsing, file, execution, subagent or GitHub access. The nested [Skill Finder](skill-finder.md) is included with direct-work/no-tools fallbacks. Useful build/review delegation also depends on an available launch tool.

Improve a writable local source rather than vendor-managed or account-synced caches. See [compatibility](compatibility.md) and [other capable LLMs](other-llms.md). Setup references were checked on **2026-10-21**.

## Optional metadata lint

Before installing a generated Claude-targeted skill, the v0.3.1 helper supports `validate /path/to/my-skill --profile claude` (use the script path shown above). It checks reserved name substrings and angle brackets in discovery metadata while allowing markup in the body. A supplied `compatibility` field must contain 1–500 characters. This is supported-subset lint, not a complete YAML parser or a native Claude execution test. See the [guide review](claude-guide-review.md).

## Optional reconstruction and explanatory visuals

No second skill installation is needed for Forge's REA and Anatomy routing instructions. [The integration guide](integrations.md) explains when each applies. Normal complete-source work uses ordinary read tools; shipped-artifact and runtime questions may need a connected compatible REA tool. Installing Forge does not connect REA or install its engines.

For a generated physical explainer, Forge selects Anatomy when it helps the agreed output and includes the actual renderer/CSS and notices in that target. Node.js 20.10+ is optional until rendering; no npm packages are needed for this basic SVG example. A browser is needed for visual/interaction checks. Keep the complete target folder when moving or sharing it; the generated target needs no Forge runtime. Plain text, CSV, ordinary flowcharts and explicit no-visual requests do not receive automatic Anatomy assets.
