# Use Skill Forge in Codex

You need Codex and the downloaded [repository or skill ZIP](../README.md). The same Skill Forge folder works on macOS, Windows and Linux. Intel/x64 and ARM64 describe processors, separate from operating systems. Choose a compatible Codex host from its [CLI setup](https://learn.chatgpt.com/docs/codex/cli) or [Windows guide](https://learn.chatgpt.com/docs/windows/windows-sandbox). Native Windows PowerShell is supported; WSL is an alternative, not a Skill Forge requirement.

Python is optional for the interview, implementation spec and skill-file output. Only the optional helpers need Python 3.9 or later. See [compatibility](compatibility.md) for documented support versus executed tests.

## Install without commands

1. Extract the download. Find the complete `skills/skill-forge` folder in the repository, or `skill-forge` in the skill ZIP.
2. Choose **personal** for local projects or **project** for one working repository. Create missing parent folders.
3. Copy the entire folder to one destination below. Keep its references, templates, scripts, license and nested Skill Finder; copying only `SKILL.md` is incomplete.
4. Open Codex and select Skill Forge. Changes are normally detected automatically; restart if it is missing.

| Scope | macOS/Linux | Windows |
| --- | --- | --- |
| Personal | `~/.agents/skills/skill-forge` | `%USERPROFILE%/.agents/skills/skill-forge` |
| Project | `<project>/.agents/skills/skill-forge` | `<project>/.agents/skills/skill-forge` |

Here `~` or `%USERPROFILE%` means your home folder; replace `<project>` with your repository path. Windows tools also accept native backslash paths. Choose one scope to avoid duplicate same-name entries. This installs on that machine, not across your account, other devices or every cloud environment. [Official discovery reference](https://learn.chatgpt.com/docs/build-skills).

## Optional managed installation

From the **downloaded repository directory**, choose your shell and one scope. Replace sample project paths.

macOS/Linux:

```sh
# Personal
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.agents/skills/skill-forge"
# Or project
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "/path/to/project/.agents/skills/skill-forge"
```

Windows PowerShell:

```powershell
# Personal
py -3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.agents/skills/skill-forge"
# Or project
py -3 skills/skill-forge/scripts/forge.py install skills/skill-forge "C:/path/to/project/.agents/skills/skill-forge"
```

Use `python` instead of `py -3` if that is your working Python command. Keep paths with spaces quoted. For the standalone skill ZIP, run from its extracted parent and substitute `skill-forge/scripts/forge.py` for the script and `skill-forge` for the source. The helper refuses an existing destination.

## First use

In Codex CLI or the IDE extension type `$skill-forge` or select it with `/skills`. In the desktop app use its skill selector; presentation may differ.

```text
$skill-forge Create a skill that turns rough meeting notes into an action list.
Keep unknown owners and dates explicit. Use your judgment.
```

Expect focused questions where needed, a compact brief, bounded foundation research, and an implementation spec with planned checks **before** target implementation. The spec is shown for correction; say “review first” to pause there, otherwise already-authorized building continues. Useful available subagents can build independent components, review or run checks. Delivery includes skill files, sample invocations and an honest validation report.

Use “quick,” “thorough,” “expert challenge,” “draft now,” “skip” or “resume” to steer the interview. You can also ask:

```text
$skill-forge Based on this conversation, build me a reusable skill.
Use the final corrections and show any assumptions.
```

Only visible context and supplied or authorized retrieved project material can be used. Supply missing context; Skill Forge cannot see unrelated chats automatically. To resume later provide the saved session or handoff.

## Update and remove

Keep one canonical working source. From a newer downloaded repository, update a helper-managed personal copy:

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.agents/skills/skill-forge" --update
```

Windows PowerShell:

```powershell
py -3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.agents/skills/skill-forge" --update
```

For project scope substitute the project destination used to install. The helper refuses customized installed copies: reconcile wanted changes into the canonical source, run relevant checks, then synchronize. For a manual installation, back up the old folder outside the discovered `skills` directory before comparing customizations and copying the complete replacement. Keep private sessions separately. Symlinks are optional, not a Windows prerequisite.

Remove by moving only the installation outside the discovered `skills` directory. Choose an unused backup destination, or move it in your file manager. Personal examples:

```sh
mv "$HOME/.agents/skills/skill-forge" "$HOME/skill-forge-backup"
```

```powershell
Move-Item -LiteralPath "$HOME/.agents/skills/skill-forge" -Destination "$HOME/skill-forge-backup"
```

For project scope move that project's installation instead. Start a new Codex chat if already-loaded instructions remain. No global settings change is needed.

## Tools and permissions

Installation does not grant file, network, execution, subagent or publication access. The nested [Skill Finder](skill-finder.md) needs no second installation; independent discovery of its nested directory is not assumed. Without a launch tool the parent works directly and says so; without browsing it uses supplied material and marks external research unavailable.

Host setup and paths were checked against official documentation on **2026-10-21**. Executed behavior and helper evidence are recorded separately in [compatibility](compatibility.md).
