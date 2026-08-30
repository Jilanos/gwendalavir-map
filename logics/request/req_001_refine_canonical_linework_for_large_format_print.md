## req_001_refine_canonical_linework_for_large_format_print - Refine canonical linework for large-format print
> From version: 1.0.0
> Schema version: 1.0
> Status: Done
> Understanding: 90%
> Confidence: 85%
> Complexity: High
> Theme: Large-format linework refinement
> Reminder: Update status/understanding/confidence and linked backlog/task references when you edit this doc.

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: refine, canonical, linework, large, format, print
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Needs
- Improve the readability of soft or pencil-like strokes at A2 and larger print sizes without changing canonical geography.
- Apply local, mask-constrained contrast and line refinement so dense regions, mountains, and small labels remain legible from one to two metres.
- Add only controlled decorative texture or detail where it reinforces the existing map, never where it would invent or relocate geographic information.

# Context
- The current refined print candidate is 12,000 × 9,180 px at 300 dpi and remains a first draft to preserve.
- A canonical ink mask is derived directly from the master map and must remain the geometric authority for all refinements.
- Current visual concern: soft source strokes and pencil-like marks can become visibly blurry at poster scale, especially in dense regions.
- Existing reports, metadata, comparison scripts, and no-source-write safeguards must be reused rather than replaced.

# Acceptance criteria
- AC1: The pipeline identifies soft, low-contrast, and high-density regions with reproducible diagnostic outputs at target print resolution.
- AC2: Linework contrast and sharpness can be refined through deterministic, mask-constrained operations with before/after overlays and difference checks.
- AC3: Refinement never moves, removes, redraws, or invents constrained coastlines, rivers, relief placement, settlements, symbols, or canonical labels.
- AC4: Optional textures and micro-details are layer-local, documented, reviewable, and prohibited from introducing map structure or text.
- AC5: The refined poster retains readable authoritative typography and exports print-ready PNG, TIFF, JPEG, and HEIC derivatives with provenance.
- AC6: A review report exposes every refinement pass, mask, parameter set, and visual comparison needed for approval before print.

# Definition of Ready (DoR)
- [x] Problem statement is explicit and user impact is clear.
- [x] Scope boundaries (in/out) are explicit.
- [x] Acceptance criteria are testable.
- [x] Dependencies and known risks are listed.

# Companion docs
- Product brief(s): `prod_002_large_format_linework_refinement`
- Architecture decision(s): (none yet)

# References
- docs/reports/refined-print-review.html
- docs/map-spec.md
- docs/workflow.md
- scripts/prepare_source.py
- scripts/extract_ink_mask.py
- scripts/compose_poster.py
- scripts/compare_images.py
- layers/masks/

# Backlog
- `item_006_diagnose_print_scale_linework_weaknesses`
- `item_007_implement_mask_constrained_linework_refinement`
- `item_008_separate_protected_labels_from_refinable_linework`
- `item_009_add_constrained_local_texture_and_micro_detail`
- `item_010_validate_large_format_exports_and_finishing_report`
