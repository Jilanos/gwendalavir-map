## req_002_restore_canonical_drawing_detail_without_geometric_invention - Restore canonical drawing detail without geometric invention
> From version: 1.0.0
> Schema version: 1.0
> Status: Draft
> Understanding: 90%
> Confidence: 85%
> Complexity: High
> Theme: Structure-preserving drawing restoration
> Reminder: Update status/understanding/confidence and linked backlog/task references when you edit this doc.

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: restore, canonical, drawing, detail, geometric, invention
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Needs
- Restore soft pencil-like drawing marks locally for large-format print without thickening noise or inventing missing geography.
- Separate parchment, continuous grayscale ink, protected text, and structural illustration before enhancement.
- Verify every written name against web research and authoritative published references before final rendering.

# Context
- The 12k master is geometrically authoritative and must not be resized during restoration.
- The current alpha-only refinement can strengthen weak marks but cannot reconstruct missing source information safely.
- Web verification must record exact spelling, source URL, source type, and verification status for every final label; reference sources include the Gwendalavir places index and published/book-derived references.

# Acceptance criteria
- AC1: The pipeline creates separate parchment, continuous grayscale ink, text-protection, and structural-detail layers from the 12k master without altering its coordinate system.
- AC2: Per-block sharpness heatmaps quantify Laplacian variance, contour width, local contrast, and ink density for 256–512 px regions.
- AC3: Only regions flagged as soft receive local candidate restoration; each candidate is rejected when it exceeds 20% stroke-width growth, loses fine components, adds halos, alters contours, or changes letters.
- AC4: Text areas receive only conservative deconvolution, contrast, and halo cleanup; no skeletonization, vectorization, generative pixels, or guessed spelling is allowed.
- AC5: Existing mountains, trees, cliffs, waves, coasts, rivers, and symbols are structure-preserved; optional detail is permitted only in the parchment background as near-invisible print-scale grain.
- AC6: A QA contact sheet covers 15–30 representative regions with original, current 12k, restored, and amplified difference views, alongside provenance and web-label verification evidence.

# Definition of Ready (DoR)
- [x] Problem statement is explicit and user impact is clear.
- [x] Scope boundaries (in/out) are explicit.
- [x] Acceptance criteria are testable.
- [x] Dependencies and known risks are listed.

# Companion docs
- Product brief(s): `prod_003_structure_preserving_drawing_restoration`
- Architecture decision(s): (none yet)

# References
- docs/reports/refined-print-review.html
- scripts/diagnose_linework.py
- scripts/refine_linework.py
- scripts/compose_poster.py
- data/labels.json
- data/landmarks.json

# Backlog
- `item_011_build_layered_restoration_inputs_and_web_verified_label_registry`
- `item_012_implement_local_blur_diagnostics_and_restoration_candidate_selection`
- `item_013_preserve_illustrated_structures_and_add_print_scale_paper_grain`
- `item_014_generate_qa_sheet_and_print_safe_restoration_exports`
