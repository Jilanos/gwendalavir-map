## item_005_recompose_authoritative_poster_and_prepare_print_exports - Recompose authoritative poster and prepare print exports
> From version: 1.0.0
> Schema version: 1.0
> Status: Done
> Understanding: 90%
> Confidence: 85%
> Progress: 100%
> Complexity: High
> Theme: Final composition
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.
> Indicators reviewed: 2026-08-29 20:20:44

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: recompose, authoritative, poster, prepare, print, exports
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Problem
- Layered outputs must become a coherent poster while retaining exact contours and authoritative typography.

# Scope
- In:
  - Create deterministic composition order for background, land/sea, relief, vegetation, structural contours, decorations, and labels.
  - Reinject canonical contours and vector labels after stylization.
  - Produce high-resolution raster, print, and vector deliverables with controlled texture/grain and print specifications.
- Out:
  - Rewriting geographic data, embedding unverified generated text, or applying geometry-changing final enhancements.

# Acceptance criteria
- AC5.1: The composition script can reproduce a review poster from declared inputs and ordering.
- AC5.2: Final raster output meets an agreed 8,000–12,000 pixel width or print-size target while preserving the approved ratio.
- AC5.3: Print exports include the documented color, DPI, bleed, format, and validation checks appropriate to the selected printer.
- AC5.4: A final visual comparison proves authoritative contours and labels are retained.

# AC Traceability
- request-AC5 -> This backlog slice. Proof: AC5.1: The composition script can reproduce a review poster from declared inputs and ordering.
- request-AC6 -> This backlog slice. Proof: AC5.2: Final raster output meets an agreed 8,000–12,000 pixel width or print-size target while preserving the approved ratio.

# Decision framing
- Product framing: Not needed
- Architecture framing: Not needed

# Links
- Product brief(s): `prod_001_faithful_hd_map_poster_pipeline`
- Architecture decision(s): (none yet)
- Request: `req_000_deliver_a_faithful_high_definition_map_production_pipeline`
- Primary task(s): `task_001_orchestrate_faithful_hd_map_poster_pipeline`

# Priority
- Priority: High
- Rationale: Set by scaffold input or defaulted for grooming.

# Tasks
- `task_001_orchestrate_faithful_hd_map_poster_pipeline`

# Notes
- Task `task_001_orchestrate_faithful_hd_map_poster_pipeline` was finished via `logics-manager flow finish task` on 2026-08-29.
