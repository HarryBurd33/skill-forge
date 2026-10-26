# Final independent metadata-helper review

2026-10-26. Candidate2 full-core SHA256 `5b25ded0676dc20f8331442bfe62a4d3e17df05a9f71603cd745224c7b5a27c7` verified with the actual tree-hash helper. Script remains SHA256 `3532563429bc16da27ddcadc9cea9f9f56a9be3499b389ebc691557d3e5a1bcb`.

The fixed26case evaluator was rerun in real subprocesses. All26candidate cases pass, including the four originally reserved cases; baseline16/26. Invalid metadata correctly rejected rises3→12 (+9), exceeding predefined+3. Original evaluator, criteria and both case files still match freeze.json. The original candidate1 execution and review remain unchanged.

The helper Markdown example now closes with a standalone fence and starts its following prose in a new paragraph. The documentation defect in candidate1 is resolved. No remaining acceptance-blocking issue was found in this focused review.

Evidence limits remain unchanged: script behavior only; unsupported YAML syntax/native-host acceptance/downstream model quality are not established. The historical baseline lacked a Claude profile and was evaluated using its generic behavior for those cases; this explicit capability comparison does not imply a hidden baseline profile. Unknown-profile baseline rejection differed only in diagnostics and is excluded from the benefit metric. Rerunning formerly held-out cases after the documentation-only repair is regression confirmation; those inputs are no longer newly unseen.
