# Worked brief: adaptive planner

**Status:** illustrative public example; all people, routines, and commitments are fictional. Original material under MIT.

**Confirmed requirements:** Plan daily, weekly, and monthly work from deadlines, priorities, estimated durations, recurring activities, fixed commitments, and realistic available capacity. Separate firm constraints from preferences. Support a model week plus dated exceptions. Revise affected flexible tasks after disruption and explain tradeoffs.

**Proposed defaults:** Include transitions and slack where the user has not supplied them. Ask about a missing estimate only when it changes feasibility. Keep uncertain estimates labeled and revise them from actual feedback.

**Assumptions:** Calendar and spreadsheet integrations are optional; a copyable schedule is always possible. The user's chosen sleep window is a firm constraint unless they explicitly change it.

**Representative request:** “An exam was added Wednesday 09:00–11:00. I sleep 23:00–07:00, have class 13:00–15:00, and need 30 minutes to travel before class. Move my flexible study and laundry without changing these commitments.”

**Acceptance criteria:** No overlap with the exam, class, required travel, or sleep. Preserve task durations, show where displaced work goes, and report work that cannot fit before its deadline. Feedback about a single bad day does not become a permanent default.

**Unresolved questions:** How much work must occur before the exam, when displaced tasks are due, and free capacity elsewhere matter if not already supplied. Ask about these when needed; do not silently shorten work.

**Artifact:** [SKILL.md](SKILL.md). [Illustrative schedule and limitations](demonstration.md).
