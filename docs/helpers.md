# File helpers

The complete [helper reference](../skills/skill-forge/references/helpers.md) ships
inside the installable skill and the portable prompt. It documents validation,
question search, private sessions, frozen evaluation evidence, automatic adoption,
rollback, managed installs, and allowlisted release packaging.

From a source checkout, run:

```sh
python3 skills/skill-forge/scripts/forge.py --help
python3 -m unittest discover -s tests -v
```

The helpers use Python 3.9+ and its standard library. They check evidence supplied
by an evaluator; they do not independently authenticate model executions or replace
the evaluation rubric. See the reference for schemas and limitations.
