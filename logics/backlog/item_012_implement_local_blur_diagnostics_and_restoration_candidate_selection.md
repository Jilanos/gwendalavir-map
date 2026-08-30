## item_012_implement_local_blur_diagnostics_and_restoration_candidate_selection - Implement local blur diagnostics and restoration candidate selection
> From version: 1.0.0
> Schema version: 1.0
> Status: In progress
> Understanding: 90%
> Confidence: 85%
> Progress: 10%
> Complexity: High
> Theme: Quantitative restoration
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.
> Indicators reviewed: 2026-08-30 15:23:48

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: implement, local, blur, diagnostics, restoration, candidate, selection
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Problem
- Only genuinely soft blocks should be changed.

# Scope
- In:
  - Block metrics, heatmaps, weak-PSF Richardson-Lucy candidates, and automatic quality rejection.
- Out:
  - Unbounded global deconvolution or sharpening.

# Acceptance criteria
- AC2.1: Heatmaps record all four specified metrics.
- AC3.1: Candidate acceptance enforces all quantitative guardrails.

# AC Traceability
- request-AC2 -> This backlog slice. Proof: AC2.1: Heatmaps record all four specified metrics.
- request-AC3 -> This backlog slice. Proof: AC3.1: Candidate acceptance enforces all quantitative guardrails.

# Decision framing
- Product framing: Not needed
- Architecture framing: Not needed

# Links
- Product brief(s): `prod_003_structure_preserving_drawing_restoration`
- Architecture decision(s): (none yet)
- Request: `req_002_restore_canonical_drawing_detail_without_geometric_invention`
- Primary task(s): `task_003_orchestrate_structure_preserving_drawing_restoration`

# Priority
- Priority: High
- Rationale: Set by scaffold input or defaulted for grooming.
