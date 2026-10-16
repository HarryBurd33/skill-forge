# Use Skill Forge in Codex

Skill Forge works as an ordinary local skill. You need Codex and the downloaded repository (or the skill archive). Python is optional for the interview and required only for the bundled helpers. See [the README](../README.md) for downloads and [compatibility](compatibility.md) for what has actually been tested.

## Install

Choose **personal** for all your projects, or **project** for one repository. From the downloaded Skill Forge repository directory, run one command:

Personal:

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.agents/skills/skill-forge"
```

Project: replace `/absolute/path/to/your-project` with the project folder you use in Codex.

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge /absolute/path/to/your-project/.agents/skills/skill-forge
```

The helper refuses to overwrite an existing destination. You can also copy the entire `skills/skill-forge` folder manually into the chosen `skills` directory. For the standalone archive, its `skill-forge` directory is the folder to copy; do not copy only `SKILL.md`.

Current official documentation places personal skills under `~/.agents/skills`; project skills use `.agents/skills`. Codex searches project ancestors up to the repository root and supports symlinked skill directories. Changes are detected automatically; restart if a skill is missing. Multiple same-name skills can appear, so choose one installation scope. [Official setup reference](https://learn.chatgpt.com/docs/build-skills).

## First use

In Codex CLI or the IDE extension, select the skill with `/skills` or type `$skill-forge`. In the desktop app, use its skill selector; interfaces can differ. Try:

```text
$skill-forge Create a skill that turns my rough meeting notes into an action list.
Keep unknown owners and dates explicit. Draft now; use your judgment.
```

Expect a compact brief, a usable skill draft, sample invocations, and a report distinguishing checks actually run from checks still needed. Ask for “quick,” “thorough,” or “expert challenge” to change the interview pace. To continue later, supply the saved session record and say “resume.”

## Update and remove

Keep the downloaded repository as your canonical working copy. After retrieving a newer release and reviewing its changes, run the install command with `--update`:

```sh
python3 skills/skill-forge/scripts/forge.py install skills/skill-forge "$HOME/.agents/skills/skill-forge" --update
```

For project scope, use the project destination instead. This updates a helper-managed copy only when it still matches its recorded installation; locally modified copies require reconciliation. Preserve your customizations in the canonical copy and rerun the relevant checks before syncing. Do not replace private session state with release contents.

An alternative on macOS/Linux is a symbolic link to one canonical skill folder. Create the parent directory, then link an **absolute** source path into the same personal/project destination. An existing destination must first be backed up and reconciled. This avoids copied versions drifting, but deleting or moving the source breaks the link.

To remove Skill Forge, move its installed folder or link outside the discovered `skills` directory, or delete that one installation after saving wanted changes. Restart Codex if its selector is stale. Keep your session records separately if you want to resume later. No changes to global settings are needed.

## Tools and permissions

The common instructions do not require Codex-specific calls. File access, browsing, scripts, separate evaluator contexts, and GitHub writes depend on the current environment. The builder can draft without them, but must report unavailable checks and cannot claim a saved update or publication without doing it. Native discovery and UI invocation are documentation-supported; consult [the release evidence](../evals/REPORT.md) for executed tests.
