## item_001_harden_source_selection_and_master_map_validation - Harden source selection and master-map validation
> From version: 1.0.0
> Schema version: 1.0
> Status: In progress
> Understanding: 90%
> Confidence: 85%
> Progress: 100%
> Complexity: Medium
> Theme: Reference geometry
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.
> Indicators reviewed: 2026-08-29 18:16:29

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: harden, source, selection, master, map, validation
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Problem
- The ingestion baseline exists, but source selection, alignment review, and master-map approval need a documented operational workflow.

# Scope
- In:
  - Review and validate source inventory, deterministic preparation, alignment, comparison, metadata, and master-map outputs.
  - Define source-selection and visual-approval criteria, including scan quality, crop, orientation, ratio, and coordinate reference declaration.
  - Add regression fixtures and tests for no-source-write guarantees and ratio preservation.
- Out:
  - Generative super-resolution, artistic colorization, layer extraction, and poster composition.

# Acceptance criteria
- AC1.1: A documented command sequence selects and produces an approved master map from one or more scans.
- AC1.2: The approved master map has a recorded source hash, dimensions, ratio, transformation metadata, and visual comparison evidence.
- AC1.3: Automated tests prevent any pipeline output from overwriting source/.

# AC Traceability
- request-AC1 -> This backlog slice. Proof: AC1.1: A documented command sequence selects and produces an approved master map from one or more scans.
- request-AC6 -> This backlog slice. Proof: AC1.2: The approved master map has a recorded source hash, dimensions, ratio, transformation metadata, and visual comparison evidence.

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
