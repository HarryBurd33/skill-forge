---
name: adaptive-planner
description: Build and revise feasible daily, weekly, or monthly plans from deadlines, recurring routines, capacity, and fixed commitments. Use for scheduling and replanning; a simple reminder alone does not need this workflow.
license: MIT
---

# Adaptive planner

Create a plan the user can realistically follow. Preserve firm constraints and expose overload instead of hiding it.

Read supplied commitments and preferences first. Record each task's duration or range, deadline, priority, dependencies, and flexibility. Separate fixed events, travel and transition time, sleep, and other firm constraints from preferred timing. Resolve contradictions that would change the plan. Do not invent free time or treat every unscheduled hour as usable capacity.

For a recurring plan, maintain a model week and dated exceptions. Establish the planning dates and time zone when calendar dates or exports depend on them. Use a short clarification only for information that materially changes feasibility. If the user asks for a draft, mark uncertain estimates and provide a provisional plan.

Schedule fixed commitments first. Fit flexible tasks into the remaining usable capacity, honoring deadlines and dependencies, with realistic transitions and slack. If all work cannot fit, state the capacity shortfall and the affected tasks. Offer concrete tradeoffs such as reducing scope, extending a deadline, or changing a preference; do not silently omit tasks, truncate durations, or borrow protected sleep.

When a new exam, meeting, missed task, or energy change arrives, identify the affected interval and move flexible tasks to feasible openings. Preserve unaffected commitments and explain what moved, what was deferred, and any new conflict. An explicit user change can revise a firm constraint; a new task by itself cannot.

After daily or weekly feedback, compare estimates with observed durations and ask whether a change is one-time or recurring when ambiguous. Keep personal sleep times, energy patterns, and preferences in that user's session or local configuration. Do not convert them into defaults for others.

Return a readable schedule plus unscheduled work and assumptions. Produce calendar or spreadsheet output when requested and suitable tools are available; otherwise return copyable fields or content and explain the remaining import step. Do not claim events were saved or synchronized without a tool result confirming it. Save the model week and exceptions when persistence is available and authorized, or supply a compact handoff for resuming.
