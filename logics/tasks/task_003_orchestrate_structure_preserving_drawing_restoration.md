## task_003_orchestrate_structure_preserving_drawing_restoration - Orchestrate structure-preserving drawing restoration
> From version: 1.0.0
> Schema version: 1.0
> Status: Ready
> Understanding: 90%
> Confidence: 85%
> Progress: 0%
> Complexity: Medium
> Theme: Implementation delivery
> Reminder: Update status/understanding/confidence/progress and linked request/backlog references when you edit this doc.

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: orchestrate, structure, preserving, drawing, restoration
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Context
- Orchestrate the scaffolded request chain and keep sibling implementation slices linked.

# Plan
- [ ] 1. Separate protected layers and verify labels from web and published references.
- [ ] 2. Measure local blur and generate heatmaps.
- [ ] 3. Restore only accepted weak regions with conservative candidates and guardrails.
- [ ] 4. Apply optional background-only grain and recompose.
- [ ] 5. Produce QA evidence and print exports.
- [ ] ADR 009 checkpoint: update affected Logics docs during each meaningful wave and leave the repo commit-ready.
- [ ] Keep commit creation under operator control; do not force one commit per micro-step.
- [ ] GATE: do not close until lint, audit, and scaffold validation pass.

# Backlog
- `item_011_build_layered_restoration_inputs_and_web_verified_label_registry`
- `item_012_implement_local_blur_diagnostics_and_restoration_candidate_selection`
- `item_013_preserve_illustrated_structures_and_add_print_scale_paper_grain`
- `item_014_generate_qa_sheet_and_print_safe_restoration_exports`

# Definition of Done (DoD)
- [ ] Generated request, product, backlog, and task docs are present.
- [ ] Context-pack handoff is available when requested.
- [ ] Validation passes.
- [ ] Meaningful waves followed ADR 009: affected docs updated and the repo left commit-ready without automatic commits.

# AC Traceability
- request-AC1 -> `item_011_build_layered_restoration_inputs_and_web_verified_label_registry`. Proof deferred to slice closeout.
- request-AC4 -> `item_011_build_layered_restoration_inputs_and_web_verified_label_registry`. Proof deferred to slice closeout.
- request-AC2 -> `item_012_implement_local_blur_diagnostics_and_restoration_candidate_selection`. Proof deferred to slice closeout.
- request-AC3 -> `item_012_implement_local_blur_diagnostics_and_restoration_candidate_selection`. Proof deferred to slice closeout.
- request-AC5 -> `item_013_preserve_illustrated_structures_and_add_print_scale_paper_grain`. Proof deferred to slice closeout.
- request-AC6 -> `item_014_generate_qa_sheet_and_print_safe_restoration_exports`. Proof deferred to slice closeout.

# Validation
- (no validation recorded yet)

# Report
- Not started.

# Links
- Request: `req_002_restore_canonical_drawing_detail_without_geometric_invention`
- Product brief(s): `prod_003_structure_preserving_drawing_restoration`
- Architecture decision(s): (none yet)
