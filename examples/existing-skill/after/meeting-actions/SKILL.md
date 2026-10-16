---
name: meeting-actions
description: Extract action items from supplied meeting notes into an ordered Markdown table.
license: MIT
---

# Meeting actions

Read the supplied meeting notes. Extract explicit action items into a Markdown table with columns Action, Owner, and Due date. Keep the order in which actions appear. Use an owner or due date only when the notes explicitly associate it with that action; otherwise write `Unassigned` or `Not stated`, respectively. A nearby speaker's name does not assign them an action. Do not turn an unresolved discussion into a commitment. If there are no actions, say so.
