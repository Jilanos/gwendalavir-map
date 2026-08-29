## item_004_define_constrained_artistic_layer_generation - Define constrained artistic layer generation
> From version: 1.0.0
> Schema version: 1.0
> Status: In progress
> Understanding: 90%
> Confidence: 85%
> Progress: 30%
> Complexity: High
> Theme: Controlled stylization
> Reminder: Update status/understanding/confidence/progress and linked request/task references when you edit this doc.
> Indicators reviewed: 2026-08-29 18:16:29

# AI Context
- Summary: (unfilled: replace before this doc is used)
- Keywords: define, constrained, artistic, layer, generation
- Use when: (unfilled: replace before this doc is used)
- Skip when: (unfilled: replace before this doc is used)

# Problem
- The project needs an artistic result without allowing a generator to reinterpret the map.

# Scope
- In:
  - Define a style direction for paper, palette, sea, land, relief, vegetation, aging, decorative elements, and realism level.
  - Create generation templates referencing the approved image, target layer, mask, allowed freedom, and preservation constraints.
  - Define review gates and experiment recording for separate background, land/sea, relief, vegetation, and decoration passes.
- Out:
  - Single-pass full-map generation, text generation, or unconstrained geometry changes.

# Acceptance criteria
- AC4.1: Every generation request identifies an input reference, layer, mask, freedom level, and explicit preservation constraints.
- AC4.2: Artistic outputs are accepted only after overlay review confirms constrained geometry was not displaced.
- AC4.3: Experiments and selected outputs remain traceable to their prompt, mask, and reference.

# AC Traceability
- request-AC4 -> This backlog slice. Proof: AC4.1: Every generation request identifies an input reference, layer, mask, freedom level, and explicit preservation constraints.
- request-AC6 -> This backlog slice. Proof: AC4.2: Artistic outputs are accepted only after overlay review confirms constrained geometry was not displaced.

# Decision framing
- Product framing: Not needed
- Architecture framing: Not needed

# Links
- Product brief(s): `prod_001_faithful_hd_map_poster_pipeline`
- Architecture decision(s): (none yet)
- Request: `req_000_deliver_a_faithful_high_definition_map_production_pipeline`
- Primary task(s): `task_001_orchestrate_faithful_hd_map_poster_pipeline`

# Priority
- Priority: Medium
- Rationale: Set by scaffold input or defaulted for grooming.
