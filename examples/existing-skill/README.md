# Improve an existing skill

This original MIT-licensed fixture models a narrow correction to an existing skill. It is intentionally small and contains fictional notes. No third-party skill text was copied.

- [Starting snapshot](before/meeting-actions/SKILL.md): extract actions as a Markdown table, preserving meeting order.
- [Candidate revision](after/meeting-actions/SKILL.md): preserve the same task and format, while explicitly retaining missing owners and dates as unknown.
- [Predefined fixture](fixture.json): input, expected behavior, and failure conditions to use before adoption.

Observation motivating the candidate: an extractor may assign the nearest named speaker to an action whose owner was never agreed. The candidate hypothesis is that preserving explicit unknowns prevents that fabrication without losing real actions. The revision also treats an open discussion as a discussion, not a new commitment.

The before/after files began as a worked proposal. A subsequent exact-fixture model execution and the predefined explicit-owner comparison supplied passing candidate evidence. The helper then automatically updated the [active example](active/meeting-actions/SKILL.md). See the [actual transaction](../../evals/results/target-adoption.json) and [release report](../../evals/REPORT.md) for observed outcomes and limits. The original snapshot remains available for rollback.

Attribution: created for Skill Forge as original project material, 2026-10-15. The starting snapshot is immutable reference material for this demonstration; its SHA-256 is recorded in [fixture.json](fixture.json). The candidate does not modify other installed skills or configuration.
