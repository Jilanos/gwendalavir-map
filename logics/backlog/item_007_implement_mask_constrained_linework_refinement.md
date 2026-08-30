## item_007_implement_mask_constrained_linework_refinement - Implement mask-constrained linework refinement
> From version: 1.0.0
> Schema version: 1.0
> Status: Done
> Understanding: 90%
> Confidence: 85%
> Progress: 100%
> Complexity: High
> Theme: Deterministic line recovery
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.
> Indicators reviewed: 2026-08-30 15:18:05

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: implement, mask, constrained, linework, refinement
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Problem
- A global contrast or sharpening pass would damage delicate text and create harsh artifacts in already clean regions.

# Scope
- In:
  - Implement conservative local contrast, threshold, unsharp-mask, and morphology options behind explicit masks.
  - Generate before/after, overlay, and difference evidence for every refinement pass.
  - Retain the canonical ink mask as the geometry lock.
- Out:
  - Unmasked global enhancement, manual tracing without evidence, and generative line redraws.

# Acceptance criteria
- AC2.1: Each pass takes an explicit input, mask, and parameter set and writes metadata.
- AC2.2: Overlay/difference checks confirm no displacement of constrained geometry.
- AC2.3: The output improves readability in approved regions without degrading unaffected labels or linework.

# AC Traceability
- request-AC2 -> This backlog slice. Proof: AC2.1: Each pass takes an explicit input, mask, and parameter set and writes metadata.
- request-AC3 -> This backlog slice. Proof: AC2.2: Overlay/difference checks confirm no displacement of constrained geometry.
- request-AC6 -> This backlog slice. Proof: AC2.3: The output improves readability in approved regions without degrading unaffected labels or linework.

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

# Tasks
- `task_002_orchestrate_large_format_linework_refinement`

# Notes
- Task `task_002_orchestrate_large_format_linework_refinement` was finished via `logics-manager flow finish task` on 2026-08-30.
