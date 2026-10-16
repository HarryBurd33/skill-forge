---
name: adaptive-prompt-builder
description: Turn an emerging workflow idea into a reusable, executable prompt through targeted questions, drafts, and feedback. Use when designing or improving a prompt; do not interview for a fully specified one-off task.
license: MIT
---

# Adaptive prompt builder

Build a prompt another capable model can execute without this conversation. Read the user's context before asking questions and retain settled decisions.

Track a short brief: intended outcome, audience, inputs, output format and destination, constraints, available tools, examples, success criteria, and unresolved choices. Separate confirmed answers from proposed defaults. Research discoverable facts when tools permit. Do not imply browsing, file access, code execution, or publication capabilities the receiving host lacks.

Choose the next question by how much its answer changes the prompt. Resolve prerequisites first: the output's destination may determine its format and fields. Ask one focused question when choices depend on each other; group a few independent questions when that saves effort. Offer options and a recommendation when helpful, with room for a free-form answer. Probe vague requests with a concrete example. A well-specified request may need no questions.

Accept “use your judgment,” “skip,” and “draft now.” Produce a useful provisional prompt with labeled assumptions instead of requiring a questionnaire. “Go deeper” adds exploration of material tradeoffs and failure cases; “resume” loads the available brief or handoff and asks only about unresolved or changed decisions.

Draft the prompt around its outcome and acceptance criteria. Include the needed role or context, input contract, essential constraints, output artifact, destination-specific fields, treatment of missing facts, and a representative example when it clarifies execution. Avoid decorative roles, duplicated rules, or instructions unrelated to the workflow.

When feedback changes the deliverable, update the output contract and dependent examples while preserving unaffected decisions. A switch from document to spreadsheet may require columns, data types, one-row semantics, formulas, or import rules. Ask only for consequential missing details; a draft schema can be labeled as a proposal.

If execution tools are available, test the prompt on representative inputs and report actual results. Otherwise provide an explicit expected outcome and a test the user can run; do not call an imagined example a successful test. Deliver the copyable prompt, a sample invocation, remaining assumptions, and a compact resume handoff. Create files only when tools permit and the request authorizes them.
