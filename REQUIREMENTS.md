# Skill Forge requirements-to-evidence checklist

Audit date: 2026-10-25. This checklist inventories implementation and existing evidence; it does not grant candidate 9 adoption. No frozen case definitions, actor responses, blind grades or held-out fixtures were read for this audit. No product files or historical scores were changed.

At this checkpoint, stable **v0.2.0** is canonical and personally installed. Both actual folder hashes were rechecked as `b4ab853d90c57eb45485dc8752a61f4cdd877c0e2523cb9442466a6a3d52e9af`. Frozen candidate 9 rechecks as `323f3aff35e785a8c53b7db06bbf40ad5d028e1a2f59c952f318637862f28dab`. Candidate 9 remains under the separate frozen evaluation process. Earlier passing checks are evidence for their recorded version, not an automatic pass for candidate 9.

Paths in the table are repository-relative to `skill-forge-v030-candidate9`, unless marked stable or external. **Implemented** means inspected instruction/code; **executed previously** means a version-specific public report records actual execution; **pending** means this audit cannot establish the requested result. A report is traceable evidence, not a new independent regrade.

## Capability checklist

| Requirement | Implementation inspected | Evidence and current limit |
| --- | --- | --- |
| Create a new independently usable skill | `skills/skill-forge/SKILL.md`; `references/authoring.md` under the core folder | Implemented; v0.1 and v0.2 reports record actual creation. Exact candidate 9 full behavioral suite pending. |
| Improve an existing local/public skill | Core routing, `references/improvement.md`, authoring; existing-skill before/after/active example | Actual original target adoption in `evals/results/target-adoption.json`, described in `evals/REPORT.md`. Current candidate repair behavior still requires its fixed cases. |
| Improve Skill Forge itself | Separate builder loop; question lifecycle; frozen helper gate | Actual retrieval improvement adopted and redundant/no-benefit candidates rejected in `evals/REPORT.md`; v0.2 adoption recorded in `evals/v0.2.0/REPORT.md`. Candidate 9 not adopted. |
| Route naturally rather than require a menu | Core `Start from the request` | Implemented. Separate prior routing checks exist; candidate 9 activation pending. |
| Approachability and technical-depth adaptation | Core plain-language requirement; audience/technical comfort interview fields | Implemented; no human-user usability study or dedicated technical-comfort comparison established. |
| Read context before asking; research discoverable facts | Core; `references/interview.md`; `references/context-intake.md` | Implemented. Earlier simple/detailed-complex/ambiguous examples actually exercised per v0.1 report. Exact candidate 9 pending. |
| Adaptive depth from unresolved decisions and consequences | Interview dependency frontier and coverage pass | Implemented. Long request is not equated with many questions. No fixed questionnaire. Prior selected cases do not establish universal optimal depth. |
| One consequential decision at a time | Core counts independent decisions, not punctuation; interview reference | Implemented. Historical bundled-question failures remain disclosed. v0.2 final 12-case sample passed its fixed budgets; candidate 9 budgets pending. |
| Quick mode | Core pace rules; interview reference | Implemented. Exact named-mode behavior is not separately established by this audit. |
| Thorough mode | Material-branch exploration, examples and failure cases | Implemented; earlier deeper interviews reported. Exact named-mode current behavior pending. |
| Expert-challenge mode | Assumption/alternative/counterexample stress | Implemented; dedicated named-mode execution not established here. |
| Constructive disagreement without forcing agreement | Explain tradeoffs, weak assumptions and alternatives; recommendation optional | Implemented. No claim of perfect disagreement quality from wording alone. |
| Concrete examples and counterexamples | Core; interview; visible verification ledger | Implemented; prior domain examples and failures recorded. Current ledger behavior under evaluation. |
| Preserve confirmed, proposed, assumed and unresolved facts | `templates/session.json`; interview/reference rules | Implemented. v0.1 report records contradictions and resume, including retained failures. |
| Propagate final corrections through brief, spec, checks and handoff | Context intake, core build boundary, specification reference | Implemented; exact candidate 9 behavioral verification pending. |
| `draft now` | Provisional saveable text; stop questions; no appended delivery question | Implemented; previous versions had failures, repaired instructions now frozen for evaluation. |
| `skip` | Record uncertainty/assumption without invented answer | Implemented; dedicated exact-current execution not established by this audit. |
| `use your judgment` | Delegates routine choices, preserves factual/authorization boundaries | Implemented; dedicated exact-current execution not established here. |
| `go deeper` | Explore a concrete remaining uncertainty | Implemented; dedicated exact-current execution not established here. |
| `resume` | Saved brief/spec/review preference/next step; no repeat settled decisions | Implemented; earlier resume failure and no-benefit rejection disclosed in v0.1 report. Current strict check remains pending. |
| Stop interviewing at material closure | Core and interview stopping rule | Implemented; rejects endless abstract perfection. Earlier simple/detailed-complex cases reported. |
| Suggest simpler prompt/adoptable skill when sufficient | Core/interview and Finder adoption decision | Implemented. Not a mandate to create a package for one-off prompt requests. |
| Skill delivery vs produced artifacts | Core explicitly separates Markdown/folder/ZIP/GitHub choice from document/spreadsheet output | Implemented; helper session-contract test exists. Actual v0.2 delivery-choice evidence is in its report. |
| Explicit GitHub or local delivery choice and publication boundary | Core new-skill choice; preserve repair destination; resolve owner/visibility when needed | Implemented; user-specific current destination already authorized. Local delivery does not authorize publication. |
| Nested Skill Finder | `subskills/skill-finder/SKILL.md`, directly linked from core; finder template | Implemented. v0.2 report records real delegated research before implementation. |
| Bounded sanitized research | Finder brief minimization, scope/budget, actual search/query/capability reporting | Implemented. No claim every latest requested source is currently accessible. |
| Inspect actual sources at recorded revisions | Finder shortlist requirements; `SOURCES.json` | Implemented; pinned foundation files/licenses and dates recorded. URLs or stars alone are not fit evidence. |
| GitHub/Hugging Face/other helpful resources | Finder searches by relevance and records actual scope/skips | Implemented; v0.2 actual researcher inspected repositories and assessed Hugging Face relevance. It need not search every service indiscriminately. |
| License-aware reuse and attribution | Finder adopt/adapt/reference/reject; authoring; `LICENSE`, `THIRD_PARTY_NOTICES.md`, `SOURCES.json` | Original project MIT; consulted Apache/MIT sources remain individually recorded. Public visibility never substitutes for reuse rights. |
| Useful construction/review subagents | Core and `references/delegation.md` bound workers/scopes, wait/integrate, reserve capacity | Implemented. Research-only work cannot count as construction. Exact candidate 9 actual-launch conditions remain pending. |
| Honest unavailable-tools/delegation fallback | Finder, portability and core capability checks | Implemented; v0.2 includes imposed no-tools contexts. Native tool availability remains host-dependent. |
| Visible implementation spec before building | Core boundary, specification reference, template | Implemented. Optional pause respected; plans must precede contents/writes. Current source not yet shown to pass all fixed cases. |
| Optional review pause | `review first` waits; otherwise authorized work continues | Implemented; no renewed approval ritual for settled authorized work. Current behavioral tests pending. |
| Verification planned before building | Visible rule → concrete input → expected/forbidden result → method/status ledger | Candidate 9 implementation inspected. The fresh scoped K02 review passed4/4conditions on2026-10-25; the remaining unchanged suite is pending. This documentation audit itself awards no pass. |
| Build from conversation/project | Context-intake reference; final corrections; source-coverage limits; reusable extraction | Implemented. No claim to hidden chats or whole projects. Current evaluation pending. |
| Independent target skills and only useful supporting files | Authoring rules; standalone example folders | Earlier generated-format/domain tests recorded. No mandatory dependency on Skill Forge/Finder. |
| Progressive disclosure and concise main | Main has **85 lines**; all **9 references directly linked** | Actual static inspection passes requested <500/direct-reference properties. See contents gap below. |
| Contents section for every reference over100lines | `references/helpers.md` has **243 lines** | **Gap:** no contents section. Other8reference files are11–31lines. Frozen source was not edited. |
| Specificity matched to fragility | Authoring prefers deterministic helpers for fragile transformations; interview permits judgment; helper gates fixed | Substantially implemented. Anthropic guidance reviewed below. A future authoring revision can state the general freedom principle explicitly without overprescribing simple tasks. |
| Self-contained fresh-chat prompt and no drift | `portable/skill-forge-prompt.md`; helper bundle/hash checks | Prior exact rebuilds pass; candidate 9 static result recorded separately by parent. Universal other-model performance unverified. |
| Private portable resumable state | Session template; improvement/portability references; private-state helper | Earlier private-sentinel and directory tests passed. Plain-chat handoff requires user save; no automatic memory/retraining claim. |
| Private preferences do not become shared defaults | Separate personalization and generalization, sanitized examples, package allowlist | Implemented; helper privacy tests and prior public-selection reviews exist. Exact new publication selection still needs review. |
| Extensible searchable question library |11question records, purpose/ask/skip/dependencies/affects/evidence/history fields | Helper query/schema tests and actual accepted/redundant-question demonstration reported. More questions are not presumed better. |
| Traceable automatic adoption after benefit/regression checks | Frozen criteria/evaluator outside candidate; snapshots, hashes, records | Actual successful target/builder transactions and rejection demonstrations exist. Helper authenticates file bindings, not evaluator truthfulness. |
| Failed/inconclusive/unavailable checks keep prior active | Improvement rules and helper rejection paths | Stable/personal hashes rechecked unchanged; rejected source history remains. Candidate 9 cannot self-authorize. |
| Rollback and managed-copy customization protection | Helper rollback/install checks; `tests/test_forge.py` | Actual prior tests restore hashes and refuse overwriting later customization. Exact final release installation still pending. |
| Bounded rounds/effort; no background work | Default3candidates/30wallminutes; owner can set bound | Current authorized repair controls govern separately. No new automation created. |
| Research-writer worked brief/artifact | `examples/research-writer/`; example guide | Illustrative generated artifacts; original domain suite exercised insufficient evidence without invented statistics. Not a production research application. |
| Prompt-builder worked brief/artifact | `examples/adaptive-prompt-builder/` | Original executed document→CSV change reported. File destination vs skill delivery remains separate. |
| Planner worked brief/artifact | `examples/adaptive-planner/` | Original executed exam adjustment preserved sleep/fixed activities and surfaced infeasibility. Not native calendar integration. |
| Activation separate from quality | Prior description-only positive/negative routing evidence | v0.2 six routing judgments passed; native discovery and candidate 9 activation are separate pending checks. |
| Baseline, fixed rubric, independent context, held-outs | Public reports and external private control process | Previous failures preserved; this audit did not read frozen/held-out inputs and cannot substitute for grader. |
| Beginner README/setup/contribution path | `README.md`, host guides, other-LLMs guide, `CONTRIBUTING.md`, issue templates | Inspected. README labels development unreleased and points to stable. Contribution path ties question/failure to frozen cases and versioned improvement. |
| Codex skill-creator comparison/cooperation | `docs/foundations.md` | Forge adds interview/spec/state/gates; creator can author/review. No upstream/vendor-cache changes implied; each loop separately evaluated. |
| New usage-saving policy | Current task policy; existing bounded delegation/effort guidance | The user’s new execution policy governs this project’s work; see MAINTENANCE.md. Frozen evaluation settings remain unchanged. No mandatory model-routing product feature or paid service is inferred. Per-task tokens and exact serving-model ID are unavailable. |
| Same public and personal intended capabilities | Stable canonical/personal hashes equal | v0.2 equality established locally; candidate9 remains local and uninstalled. Updating public draft is not adoption or release. |
| Exact current release/download/clean first-use | Existing `evals/v0.2.0/first-use-check.json`; current helper evidence | Stable4directory shapes/portable/private exclusion previously passed. Latest final approved candidate public download, upgrade, install and rollback verification remain release work. |
| Keep existing repo/history/visibility/PR workflow | Existing public `HarryBurd33/skill-forge`, draftPR2 | Authenticated owner HarryBurd33 and existing public repository verified2026-10-25; drafthead4aed687d0ad0c1558fd9ef3f2066d64a32ffa1b6 and mainc5c28fc138484d57f703478abe99f0d99455efba confirmed before this checkpoint update. No newrepo/force-push/deletion authorized by this audit. |
| Current source/templates/tests/README/sanitized handoff | Repository material and this checklist | New checklist is local. Must be sanitized/reviewed and synchronized before claiming publication. Live private controls/rawtranscripts excluded. |

## Host and operating-system evidence

| Target | Actual evidence inspected | Remaining limit |
| --- | --- | --- |
| macOS ARM | Prior local helper suite27pass/1Windows-onlyskip, Python3.15.0/macOS14.6ARM; hosted ARMmacOS3.13 job; earlier CodexCLI smoke on candidate4 | Not exact candidate9 native execution. |
| macOS Intel | Hosted macOS3.9 helper/package/temp-install job passed; recorded runtime macOS15.7.9x86_64 | Native Codex/Claude model behavior unverified. |
| Windows | Hosted Python3.9/3.13 helper/package/temp-install jobs passed, including native junction case; one actual runtime Windows10.0.26100AMD64/Python3.9.13 | No native Codex/Claude model execution claimed. WindowsACL privacy differs from POSIXchmod. |
| Linux | Hosted Ubuntu3.9/3.13 helper/package/temp-install jobs passed; recorded Linux6.17x86_64/Python3.13.16 | No native model-host execution claimed; ARM combinations not established here. |
| Codex | Personal installed catalog evidence; earlier CLI0.163.0-alpha.10.2 discovered a candidate4 project skill and drafted | Latest candidate native discovery/output not verified; local install is not account-wide deployment. |
| Claude Code | Official paths/invocation documentation and temporary directory installation tests | Native Claude execution unverified; no claude executable found on this host2026-10-25. No parity claim. |
| Other capable LLMs | Self-contained prompt and imposed tool-free model contexts | External model families/products unverified. Local/free model availability/quality not measured in this audit. |

Platform evidence paths: `docs/compatibility.md`, `evals/v0.3.0/helper-checks.json`, `evals/v0.3.0/final-source-platform-checks.json`, `evals/v0.3.0/native-codex-smoke.json`. Hosted run [39344381465](https://github.com/HarryBurd33/skill-forge/actions/runs/39344381465) binds source5, not9. Helper bytes are unchanged at `861bd90ef4259cd1aa57095a9734fc8c2c7fdb0fa60b134cbbaea1c3693c9115`.

## Foundation and desktop-source review

On2026-10-25 the audit opened [Anthropic authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) and the project's [pinned Anthropic skill-creator](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md). The guidance supports concise instructions, freedom matched to fragility, a main file below500lines, directly reachable references, and contents for references longer than100lines. Skill-creator already supports creation, comparison with prior/no-skill baselines, iteration and conversation intake; those are foundations, not claimed Forge inventions. Its default evaluation workflow differs from this project's deliberately frozen checks; no imported instruction changes the existing evaluator.

The6-page Desktop file `astra-skill-builder-prompt-v1.pdf` was accessible and text-extracted with the bundled PDF library. It is an earlier Skill Forge project brief, substantially overlapping the conversation's original request. Its working defaults are superseded by later confirmed user choices, especially automatic evidence-gated adoption and optional spec-review pause. It adds no authority to relax frozen evaluation or publish rawprivate records. No unrelated Desktop PDF contents were read. The extracted rawtext is a **private local audit aid**, not a public deliverable.

Existing `SOURCES.json` records inspected source files, immutable revisions, dates, licenses and notices; `docs/foundations.md` compares reuse/adapt/omit choices. This audit did not re-fetch every old source or claim a new license review of every upstream repository. No inaccessible-source claim is needed for the two requested guidance sources actually read here.

## Concrete gaps and follow-through

1. The qualified scoped K02 review is complete (A4/4,B2/4); finish the remaining unchanged candidate9 suite before adoption/install/release or all-capabilities-pass claims.
2. Add a contents section to the243-line helper reference through an explicitly recorded source change after the frozen9 decision, keeping its evidence distinct.
3. Address the new usage policy in future source/task records without changing frozen actor/evaluator settings. Record exact model/settings when exposed, otherwise unknown; do not claim local/free model qualification without actual checks.
4. Dedicated current-version evidence for named pace modes and `skip`, `use your judgment`, `go deeper` is not established by this audit. Any supplemental cases must be prospective and additive, never replace frozen checks or expose held-outs to source authors.
5. After an actually passing source, synchronize canonical/personal/public bytes, execute clean upgrade/rollback/first-use and release-download checks, inspect finalCI and update public reports. Native Claude/other-model execution remains explicitly unverified unless actually run.

Audit measurements: one scoped documentation/requirements audit; no actor replay or candidate edit; no paid service; inherited model/settings unchanged and exact runtime model identifier unavailable. Per-task token usage is unknown. Elapsed time is recorded by the parent task; these measurements do not imply a comparative efficiency result.

## Current local verification addendum

On2026-10-25, frozen candidate9 passed the actual release validator:178selectedfiles,163relative links, and4clean temporary personal/project Codex/Claude path installations with matching hashes. Python3.15.0 on macOSARM ran28helper tests:27passed and1native-Windows junction test skipped. Upgrade/customization refusal, evidence-gated adoption/rejection, rollback, privacy exclusions and portable drift were exercised. These are filesystem/helper tests, not native Claude or universal model execution.

The fresh scoped K02 reviewer audited23raw artifacts against both frozen indices, graded candidate4/4 and baseline2/4, and verified0designquestions/0approvalturns. No actor was replayed. The previous scope-invalid review remains preserved and receives no adoption credit. The overall21case gate remains incomplete. Three additive control scenarios were defined prospectively; they are unexecuted at this checkpoint.
