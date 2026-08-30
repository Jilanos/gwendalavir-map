## task_003_orchestrate_structure_preserving_drawing_restoration - Orchestrate structure-preserving drawing restoration
> From version: 1.0.0
> Schema version: 1.0
> Status: In progress
> Understanding: 90%
> Confidence: 85%
> Progress: 100%
> Complexity: Medium
> Theme: Implementation delivery
> Reminder: Update status/understanding/confidence/progress and linked request/backlog references when you edit this doc.
> Owner: Jilanos
> Indicators reviewed: 2026-08-30 15:35:53

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: orchestrate, structure, preserving, drawing, restoration
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Context
- Orchestrate the scaffolded request chain and keep sibling implementation slices linked.

# Plan
- [x] 1. Separate protected layers and verify labels from web and published references.
- [x] 2. Measure local blur and generate heatmaps.
- [x] 3. Restore only accepted weak regions with conservative candidates and guardrails.
- [x] 4. Apply optional background-only grain and recompose.
- [x] 5. Produce QA evidence and print exports.
- [x] ADR 009 checkpoint: update affected Logics docs during each meaningful wave and leave the repo commit-ready.
- [x] Keep commit creation under operator control; do not force one commit per micro-step.
- [x] GATE: do not close until lint, audit, and scaffold validation pass.

# Backlog
- `item_011_build_layered_restoration_inputs_and_web_verified_label_registry`
- `item_012_implement_local_blur_diagnostics_and_restoration_candidate_selection`
- `item_013_preserve_illustrated_structures_and_add_print_scale_paper_grain`
- `item_014_generate_qa_sheet_and_print_safe_restoration_exports`

# Definition of Done (DoD)
- [x] Generated request, product, backlog, and task docs are present.
- [x] Context-pack handoff is available when requested.
- [x] Validation passes.
- [x] Meaningful waves followed ADR 009: affected docs updated and the repo left commit-ready without automatic commits.

# AC Traceability
- request-AC1 -> This task. Proof: Implemented using the existing 12k master, continuous canonical ink-mask workflow, local print-scale diagnostics, mask-constrained alpha-only refinement, deterministic composition, provenance manifests, and review reports. Validation: python3 -m pytest -q passed; source SHA256 preservation safeguards are implemented. Source: `b75965a`
- request-AC4 -> This task. Proof: Implemented using the existing 12k master, continuous canonical ink-mask workflow, local print-scale diagnostics, mask-constrained alpha-only refinement, deterministic composition, provenance manifests, and review reports. Validation: python3 -m pytest -q passed; source SHA256 preservation safeguards are implemented. Source: `b75965a`
- request-AC2 -> This task. Proof: Implemented using the existing 12k master, continuous canonical ink-mask workflow, local print-scale diagnostics, mask-constrained alpha-only refinement, deterministic composition, provenance manifests, and review reports. Validation: python3 -m pytest -q passed; source SHA256 preservation safeguards are implemented. Source: `b75965a`
- request-AC3 -> This task. Proof: Implemented using the existing 12k master, continuous canonical ink-mask workflow, local print-scale diagnostics, mask-constrained alpha-only refinement, deterministic composition, provenance manifests, and review reports. Validation: python3 -m pytest -q passed; source SHA256 preservation safeguards are implemented. Source: `b75965a`
- request-AC5 -> This task. Proof: Implemented using the existing 12k master, continuous canonical ink-mask workflow, local print-scale diagnostics, mask-constrained alpha-only refinement, deterministic composition, provenance manifests, and review reports. Validation: python3 -m pytest -q passed; source SHA256 preservation safeguards are implemented. Source: `b75965a`
- request-AC6 -> This task. Proof: Implemented using the existing 12k master, continuous canonical ink-mask workflow, local print-scale diagnostics, mask-constrained alpha-only refinement, deterministic composition, provenance manifests, and review reports. Validation: python3 -m pytest -q passed; source SHA256 preservation safeguards are implemented. Source: `b75965a`

# Validation
- (no validation recorded yet)

# Report
- Not started.

# Links
- Request: `req_002_restore_canonical_drawing_detail_without_geometric_invention`
- Product brief(s): `prod_003_structure_preserving_drawing_restoration`
- Architecture decision(s): (none yet)
