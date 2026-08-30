## item_008_separate_protected_labels_from_refinable_linework - Separate protected labels from refinable linework
> From version: 1.0.0
> Schema version: 1.0
> Status: In progress
> Understanding: 90%
> Confidence: 85%
> Progress: 100%
> Complexity: Medium
> Theme: Typography protection
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.
> Indicators reviewed: 2026-08-30 14:11:05

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: separate, protected, labels, refinable, linework
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Problem
- Small names are sensitive to sharpening and must be protected or reconstructed from authoritative data before print.

# Scope
- In:
  - Build reviewable label-protection masks and extend the normalized label inventory.
  - Create a deterministic final-label review/rendering path.
  - Define name-by-name proof requirements before final approval.
- Out:
  - Accepting generated text or guessing unreadable names.

# Acceptance criteria
- AC3.1: Refinement masks exclude protected text unless a separately approved label-rendering pass is used.
- AC5.1: Final typography has a documented verification workflow and legibility checks at print scale.

# AC Traceability
- request-AC3 -> This backlog slice. Proof: AC3.1: Refinement masks exclude protected text unless a separately approved label-rendering pass is used.
- request-AC5 -> This backlog slice. Proof: AC5.1: Final typography has a documented verification workflow and legibility checks at print scale.

# Decision framing
- Product framing: Not needed
- Architecture framing: Not needed

# Links
- Product brief(s): `prod_002_large_format_linework_refinement`
- Architecture decision(s): (none yet)
- Request: `req_001_refine_canonical_linework_for_large_format_print`
- Primary task(s): `task_002_orchestrate_large_format_linework_refinement`

# Priority
- Priority: High
- Rationale: Set by scaffold input or defaulted for grooming.
