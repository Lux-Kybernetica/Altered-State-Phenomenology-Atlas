# Current status

## Source layer

- Nova Conscientia nomenclature v1.0 captured.
- 92 terms extracted.
- 6 top-level families extracted.
- Original resonance mechanism reproduced separately.

## Lux semantic layer

### Manual review v0.4 — COMPLETE

- **92 / 92 terms manually reviewed.**
- **États & lucidité: 11 / 11.**
- **Transitions: 15 / 15.**
- **Phénomènes perceptifs: 25 / 25.**
- **Navigation / actions: 19 / 19.**
- **Obstacles: 13 / 13.**
- **Sécurité: 9 / 9.**

## Relation layer v0.5 — REVIEW COMPLETE

Nova v1 produced **97 unique lexical resonance pairs**.

Semantic review outcome:

- **92 pairs** produce at least one accepted typed semantic edge;
- **5 pairs** are explicitly rejected as lexical/context artifacts;
- **96 typed edges** are accepted in total because some pairs legitimately encode more than one relation.

Accepted edge provenance:

- `source_explicit`: 56
- `source_supported`: 40

No accepted v0.5 edge is currently `proposed`; Lux pathway hypotheses remain separated from the Nova semantic graph.

## Current model axes

- `types[]`
- `modalities[]`
- `phases[]`
- `selfhood_dimensions[]`
- `cognitive_dimensions[]`
- `action_functions[]`
- `motor_states[]`
- `assertions[]` with assertion-level epistemic status

## Graph topology before generated export

- Nodes: 92
- Typed edges: 96
- Connected components in undirected projection: 29
- Largest component: 64 nodes
- Isolated concepts: 28
- Main hubs: `Lucidité` (17), `Zone de bascule` (16), `Endormissement` (9), `Décrochage` (8)

Isolation is not automatically repaired. A concept stays isolated until a justified relation source exists.

## Build automation

The repository now contains reproducible builders for:

- normalized v0.5 consolidation (`scripts/build_v05.py`);
- conservative lexical-resonance candidate generation (`scripts/suggest_relations.py`);
- graph export + QA (`scripts/build_graph_v05.py`).

A GitHub Actions workflow is configured to regenerate `data/v0.5`, `graph/v0.5`, and QA artifacts. At the time of this status update, the connector has not exposed a successful generated-artifact commit, so reviewed data files remain the authoritative relation layer while CI execution is investigated.

## Next phase

1. Get/verify the generated v0.5 consolidated node export.
2. Validate GraphML/JSON graph artifacts against the reviewed 96-edge layer.
3. Introduce the **Phosphenic Pathway** as a separate experimental sequence model.
4. Add scientific-source and Monroe/Vieira mapping layers only after pathway provenance is explicit.

## Not done yet

- verified generated consolidated v0.5 artifact;
- verified generated GraphML export;
- Phosphenic Pathway data model;
- scientific source layer;
- Monroe/Vieira crosswalks;
- public application.
