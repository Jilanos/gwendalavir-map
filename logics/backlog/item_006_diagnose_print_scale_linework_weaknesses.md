## item_006_diagnose_print_scale_linework_weaknesses - Diagnose print-scale linework weaknesses
> From version: 1.0.0
> Schema version: 1.0
> Status: In progress
> Understanding: 90%
> Confidence: 85%
> Progress: 100%
> Complexity: Medium
> Theme: Visual diagnostics
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.
> Indicators reviewed: 2026-08-30 14:11:05

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: diagnose, print, scale, linework, weaknesses
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Problem
- Soft strokes must be located and measured before any refinement can be safely targeted.

# Scope
- In:
  - Create reproducible local-contrast, edge-density, and print-scale preview diagnostics.
  - Add annotated review crops for sparse, dense, and label-heavy regions.
- Out:
  - Changing raster content or applying corrective filters.

# Acceptance criteria
- AC1.1: Diagnostics identify candidate regions and preserve a link to the exact master-map coordinates.
- AC1.2: The review report includes target-size crops and reproducible generation parameters.

# AC Traceability
- request-AC1 -> This backlog slice. Proof: AC1.1: Diagnostics identify candidate regions and preserve a link to the exact master-map coordinates.
- request-AC6 -> This backlog slice. Proof: AC1.2: The review report includes target-size crops and reproducible generation parameters.

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
