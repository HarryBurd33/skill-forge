# Worked brief: adaptive prompt builder

**Status:** illustrative public example; original material under the repository's MIT license.

**Confirmed requirements:** Turn an emerging idea into an executable prompt. Establish the intended outcome, audience, available inputs, constraints, capabilities, and observable success criteria. Identify both the output's format and where it will be used. Preserve settled decisions, support draft-now and resume, and revise after feedback.

**Proposed defaults:** Ask one dependent question at a time, batch only independent questions, and use a concrete draft early. Return a copyable prompt plus an example input and a checkable expected outcome.

**Assumptions:** The receiving model can read a prompt and supplied text. Browsing, files, spreadsheets, code execution, and repository writes depend on the actual host.

**Representative request:** “Build a reusable prompt to turn meeting notes into a handoff for our operations team. Initially I want a document, but it may need to become a spreadsheet our tracker can import.”

**Acceptance criteria:** The prompt states the task, inputs, required fields, constraints, output format and destination, treatment of missing facts, and success checks. A document-to-spreadsheet change updates the artifact contract and examples without restarting settled audience or purpose questions. The prompt does not claim to create a file if only text output is available.

**Unresolved questions:** If spreadsheet import is chosen, the destination's required columns or a sample header materially affects the output. The model should request that information or propose a clearly labeled draft schema.

**Artifact:** [SKILL.md](SKILL.md). [Illustrative outcome and limitations](demonstration.md).
