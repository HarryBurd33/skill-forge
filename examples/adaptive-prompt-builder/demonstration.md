# Illustrative revision

**This is an authored example, not a model evaluation or an exported spreadsheet.**

Settled context: operations-team audience; meeting notes as input; handoff actions as the repeated task; do not invent owners or dates.

New feedback: “Actually, this needs to go into a spreadsheet, with one row per action. The tracker accepts Action, Owner, Due date, and Status.”

Expected prompt revision:

> Extract explicit action items from the supplied meeting notes for the operations team. Return CSV with columns Action, Owner, Due date, Status, in that order, one action per row. Preserve the order in which actions appear. Leave Owner and Due date empty unless explicitly stated. Use Status `Open` unless the notes explicitly state another status. Quote CSV fields containing commas, quotation marks, or newlines. Do not add inferred commitments. If no actions appear, return only the header. Return copyable CSV; do not claim to have created or imported a file unless tools actually do so.

The change replaces the document contract; it need not ask again who the audience is. If the destination rejects a date format, the next revision should address that demonstrated issue and add a check using the destination's documented format.

Sample invocation: “Use the prompt above on: Priya will send the draft by 2026-10-19. A data-owner decision remains open.” Expected content: one action assigned to Priya and no invented action or owner for the unresolved discussion.

Limitations: CSV is suitable for simple tabular interchange, not formulas, charts, or multi-sheet workbook behavior. A richer requested workbook requires compatible tools or a clear handoff.
