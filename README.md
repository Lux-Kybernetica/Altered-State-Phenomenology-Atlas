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
- Manual semantic review: **92 / 92 complete**. ✅
- **États & lucidité: 11 / 11.**
- **Transitions: 15 / 15.**
- **Phénomènes perceptifs: 25 / 25.**
- **Navigation / actions: 19 / 19.**
- **Obstacles: 13 / 13.**
- **Sécurité: 9 / 9.**

Knowledge-graph generation remains intentionally postponed until relation review is complete.

## Current model

Each concept can be represented through several independent axes:

- `types[]`
- `modalities[]`
- `phases[]`
- `selfhood_dimensions[]`
- `cognitive_dimensions[]`
- `action_functions[]`
- `motor_states[]`
- `assertions[]`

Assertions carry epistemic status so that phenomenological observation, operational definition, interpretation and proposal are not silently conflated.

## Repository map

```text
.
├── data/          # extracted and enriched structured datasets
├── schemas/       # JSON schemas and controlled vocabularies
├── docs/          # method, decisions, roadmap, status
├── audit/         # human review reports
├── third_party/   # provenance / third-party notes
└── archive/       # superseded working artifacts when needed
```

## Next phase — v0.5

The semantic classification pass is finished. Next:

1. consolidate the 92 reviewed records;
2. validate the normalized dataset;
3. review typed relations systematically;
4. distinguish source-explicit, source-supported and proposed links;
5. export the first knowledge graph;
6. model pathways separately, beginning with the Phosphenic Pathway.

## Attribution / third-party material

Nova Conscientia's original nomenclature and website content remain third-party material. This repository is intended to stay **private** while the collaboration status and reuse permissions are unresolved.

Source page: https://novaconscientia.com/nc-skill-tree.html
