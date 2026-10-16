# Use Skill Forge in Claude Code

Use the same canonical skill folder as Codex. No Claude-only fork, marketplace account, or API service is required by Skill Forge. You still need access to Claude Code itself. Python is optional for interviewing and required for bundled helpers.

## Install

Download the repository from [the README](../README.md). From its directory, choose one scope:

Personal, available across local projects:

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.claude/skills/skill-forge"
```

Project, shared with a particular repository:

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge /absolute/path/to/your-project/.claude/skills/skill-forge
```

Replace the project path. The helper refuses to overwrite an existing installation. Without Python, copy the complete `skills/skill-forge` folder into the chosen `skills` directory. If using the standalone skill archive, copy its `skill-forge` directory. Keep all supporting files.

Claude Code documents personal skills at `~/.claude/skills` and project skills at `.claude/skills`, including symlinked skill directories. Invoke with `/skill-forge`; matching requests can also activate it automatically. Personal skills take precedence over same-name project skills. [Official reference](https://code.claude.com/docs/en/skills).

## First use

Start Claude Code in your working project and enter:

```text
/skill-forge Create a skill that turns my rough meeting notes into an action list.
Keep unknown owners and dates explicit. Draft now; use your judgment.
```

The builder should provide a compact brief, a skill draft, examples, and an honest validation report. It can also improve an existing skill when you supply its source and describe the failure. To propose a shared improvement, describe the repeated failure and an expected outcome, rather than supplying only a new instruction.

## Update and remove

For a helper-managed personal copy, run this from the newer downloaded repository:

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.claude/skills/skill-forge" --update
```

Substitute the project destination when appropriate. Modified installed copies are refused so customizations are not silently lost. Reconcile changes into your canonical working copy, verify them, and then synchronize. A manual copy has no managed update history; snapshot it before replacing or merging files.

A symbolic link from the personal/project skill location to the absolute canonical source path is an alternative on macOS/Linux. Use a single maintained source and keep private state elsewhere. Do not link over an existing folder. If both hosts point to that source, an accepted local source update is shared automatically.

Claude Code watches `SKILL.md` changes in established skills directories. Use `/reload-skills` if the top-level directory was created after the session started; restarting is a fallback. Remove a local skill by moving its directory/link outside the scanned location or deleting that installation. Already-loaded instructions may remain in the current conversation, so start a new session when verifying removal. [Update/removal details](https://code.claude.com/docs/en/skills#edit-a-skill-during-a-session).

## Portability limits

The common skill intentionally omits Claude-specific substitutions, shell injection, hooks, and tool permission declarations. The installation itself does not grant file, network, or publication access. Do not edit cloud-synced or vendor-managed skill caches as though they were your canonical source. Use a writable local copy for candidate work.

Claude Code installation and invocation are **supported by documentation, not runtime-tested in this release environment**. The host-independent helpers and model behavior checks are reported separately in [the release evidence](../evals/REPORT.md).
