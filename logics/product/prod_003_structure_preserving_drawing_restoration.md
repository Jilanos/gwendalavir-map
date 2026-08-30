## prod_003_structure_preserving_drawing_restoration - Structure-Preserving Drawing Restoration
> Date: 2026-08-30
> Status: Settled
> Related request: `req_002_restore_canonical_drawing_detail_without_geometric_invention`
> Related backlog: `item_011_build_layered_restoration_inputs_and_web_verified_label_registry`
> Related task: `task_003_orchestrate_structure_preserving_drawing_restoration`
> Related architecture: (none yet)
> Reminder: Update status, linked refs, scope, decisions, success signals, and open questions when you edit this doc.
> Indicators reviewed: 2026-08-30 15:41:45

# Overview
A local, quantitative restoration pipeline for improving print-scale readability while treating the 12k map as immutable geometry.

```mermaid
flowchart LR
  master[Immutable 12k master] --> layers[Separated ink, text, and parchment layers]
  layers --> metrics[Local blur metrics and heatmap]
  metrics --> restore[Accepted local restoration candidates]
  restore --> qa[QA contact sheets and guardrails]
  qa --> print[Print exports]
```

# Goals
- Recover readability without uniform black-line conversion.
- Protect authoritative labels through web-backed spelling verification.
- Keep restoration reversible, local, and inspectable.

# Non-goals
- Global sharpening or threshold-only line replacement.
- Generated geography or textual content.
- Replacing the current first-draft and refined outputs.

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
- Product back-reference: `item_011_build_layered_restoration_inputs_and_web_verified_label_registry`
- Task back-reference: `task_003_orchestrate_structure_preserving_drawing_restoration`
