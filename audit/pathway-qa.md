# Pathway QA

- Canonical reviewed NC term IDs: **92**
- Pathway files: **1**
- Errors: **0**

## Pathways

- `lux.phosphenic_pathway.v0_1` — 8 stages, 9 transitions, status `experimental_proposal`, errors 0

## Checks performed

- all stage IDs are unique;
- all 15 NC term references used by the pathway resolve to reviewed canonical `nova.*` IDs;
- all transition endpoints resolve to declared pathway stages;
- all transition kinds and evidence statuses belong to the controlled pathway vocabulary;
- no pathway stage is injected into the Nova source layer.

## Result

**PASS — all pathway references and transition endpoints are internally valid.**
