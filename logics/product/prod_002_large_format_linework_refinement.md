## prod_002_large_format_linework_refinement - Large-Format Linework Refinement
> Date: 2026-08-30
> Status: Settled
> Related request: `req_001_refine_canonical_linework_for_large_format_print`
> Related backlog: `item_006_diagnose_print_scale_linework_weaknesses`
> Related task: `task_002_orchestrate_large_format_linework_refinement`
> Related architecture: (none yet)
> Reminder: Update status, linked refs, scope, decisions, success signals, and open questions when you edit this doc.
> Indicators reviewed: 2026-08-30 15:18:05

# Overview
A constrained finishing pipeline that improves print-scale line clarity and controlled texture while preserving canonical map geometry.

```mermaid
flowchart LR
  master[Canonical master] --> diagnose[Print-scale diagnostics]
  diagnose --> mask[Protected refinement masks]
  mask --> refine[Deterministic line refinement]
  refine --> review[Overlay and difference review]
  review --> export[Print derivatives]
```

# Goals
- Make soft source marks legible at A2 and larger sizes.
- Preserve the exact master-map geometry and authoritative lettering.
- Keep every enhancement reversible, parameterized, and visually inspectable.
- Produce print-safe derivatives without replacing the existing first-draft outputs.

# Non-goals
- Freehand redrawing or generative replacement of geographical features.
- Generating new place names, symbols, coastlines, rivers, or terrain layout.
- Applying global sharpening, denoising, or texture that damages fine labels or line rhythm.
- Deleting or overwriting the current master maps, masks, reports, or poster drafts.

# Scope and guardrails
- In: scaffolded request, product, backlog, orchestration task, validation, and handoff context.
- Out: unrelated workflow docs and implementation of generated tasks.

# Key product decisions
- Use structured input as the source of truth for generated docs.
- Keep generated write paths local and repo-bounded.

# Success signals
- Generated docs pass lint and audit without broad manual rewrites.
- Context-pack output can be handed to an implementation agent directly.

# References
- Product back-reference: `item_006_diagnose_print_scale_linework_weaknesses`
- Task back-reference: `task_002_orchestrate_large_format_linework_refinement`
