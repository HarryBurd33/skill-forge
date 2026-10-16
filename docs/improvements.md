# Two recorded builder candidates

The first release includes an actual automatic update to the canonical builder, not only a narrated example.

The initial library contained purpose, quality, output content/audience, evidence, constraints, tools, contradiction and preservation questions. A search for `spreadsheet` returned no question that settled the destination contract. Before changing it, we froze [six checks](../evals/retrieval-criteria.json) and [the evaluator](../evals/retrieval_evaluator.py). A separate author saw the reported spreadsheet gap and library, but not the evaluator or extra query probes.

The candidate adds `q-destination`: where the result will be used and which format/fields that destination needs. It is skipped when the answer is already supplied, discoverable, or irrelevant. It distinguishes delivery constraints from content/audience and available tools. Its public history is in the question record.

Actual executions with the same fixed helper found relevant destination questions for zero of three probes before the patch and all three afterward (`spreadsheet`, withheld `CSV`, withheld `repository`). Existing constraint and research-evidence retrieval still passed, and no duplicated purpose appeared. The helper adopted the candidate into the active canonical skill automatically. [Execution](../evals/results/retrieval-execution.json), [hash-bound evidence](../evals/results/retrieval-evidence.json), [change record](../evals/results/builder-change.json).

This establishes a narrow retrieval improvement. It does not establish better interviews, statistical reliability, or superior downstream skills. The author was not shown the two reserved queries, but the project brief already discussed these artifact types, so the holdout is modest.

A second candidate added “Who is this for?” with the existing audience question's purpose. The frozen evaluator observed a duplicated purpose and no retrieval benefit. Submission retained the previous active hash and preserved the candidate. [Rejected candidate](../evals/results/rejected-question.json), [execution](../evals/results/duplicate-execution.json), [rejection record](../evals/results/rejected-change.json).

The trusted private run directories retain full prior snapshots, candidate files, frozen criteria, evaluator, evidence and rollback pointers outside the publishable repository. Their machine-specific paths are not published. For the public record, [questions-before.json](../evals/results/questions-before.json) preserves the changed file's previous content. `forge.py rollback RUN_DIRECTORY` restores a local run's full snapshot and refuses to overwrite later edits. The automated tests execute adoption and rollback in temporary directories and compare restored hashes; they also verify refusal after customization.

For your own run, follow [the helper guide](../skills/skill-forge/references/helpers.md). Synchronize each known managed installation after successful adoption with `install SOURCE DEST --update`; a changed destination is left intact for reconciliation. No background job, model retraining or permission to publish private session material is implied.

A later resume-wording candidate passed its four behavioral checks, but the previous version also passed. Its fixed benefit metric was 5 → 5, so the helper [rejected it for no demonstrated benefit](../evals/results/resume-rejection.json). The original failed resume sample remains in the report; the candidate did not get to relax its own gate.
