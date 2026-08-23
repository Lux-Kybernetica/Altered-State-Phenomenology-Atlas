# NC × Lux — Nova Conscientia Knowledge Model

> **Status:** private research workspace / working draft.

This repository is a structured research workspace around the **Nova Conscientia SHC nomenclature v1.0**.

The goal is **not** to replace or silently rewrite Nova Conscientia's nomenclature. The goal is to preserve the original material, analyze its structure, enrich it with explicit metadata and typed relations, and progressively build a knowledge model that remains traceable back to the source.

## Core rule

Three layers must never be confused:

1. **SOURCE** — what Nova Conscientia actually wrote.
2. **ANALYSIS** — how Lux classifies or interprets that material.
3. **PROPOSAL** — hypotheses, relations or structural changes that may later be suggested.

The original source material is preserved separately from Lux annotations.

## Current state

- Nova source extracted: **92 terms / 6 families**.
- Full heuristic pre-annotation: **92 terms**.
- Manual review: **52 terms reviewed**, **40 remaining**.
- **Transitions complete: 15 / 15.**
- **États & lucidité complete: 11 / 11.**
- **Phénomènes perceptifs complete: 25 / 25.**
- Knowledge graph generation is intentionally postponed until the semantic model is stable enough.

## Current model

Each concept can be represented through several independent axes:

- `types[]`
- `modalities[]`
- `phases[]`
- `selfhood_dimensions[]`
- `cognitive_dimensions[]`
- `motor_states[]`
- `assertions[]`

Assertions can carry their own epistemic status so that a phenomenological observation is not accidentally treated as an interpretation or causal claim.

## Repository map

```text
.
├── data/          # extracted and enriched structured datasets
├── schemas/       # JSON schemas and controlled vocabularies
├── docs/          # method, decisions, roadmap, status
├── audit/         # human review reports and queues
├── third_party/   # provenance / third-party notes
└── archive/       # superseded working artifacts when needed
```

## Immediate next step

Continue the manual semantic review by conceptual group:

1. ~~Transitions~~ ✅
2. ~~States & lucidity~~ ✅
3. ~~Perceptual phenomena~~ ✅
4. **Actions / navigation** ← next
5. Obstacles
6. Safety

Only then should we generate the first consolidated typed relation graph.

## Attribution / third-party material

Nova Conscientia's original nomenclature and website content remain third-party material. This repository is intended to stay **private** while the collaboration status and reuse permissions are unresolved.

Source page: https://novaconscientia.com/nc-skill-tree.html
