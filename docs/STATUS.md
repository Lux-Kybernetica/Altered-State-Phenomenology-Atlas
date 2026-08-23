# Current status

## Source layer — COMPLETE

- Nova Conscientia nomenclature v1.0 captured.
- **92 terms** extracted across **6 source families**.
- Original lexical-resonance mechanism preserved separately.

## Lux semantic layer v0.4 — COMPLETE

- **92 / 92 terms manually reviewed.**
- États & lucidité: 11 / 11.
- Transitions: 15 / 15.
- Phénomènes perceptifs: 25 / 25.
- Navigation / actions: 19 / 19.
- Obstacles: 13 / 13.
- Sécurité: 9 / 9.

Current semantic axes:

- `types[]`
- `modalities[]`
- `phases[]`
- `selfhood_dimensions[]`
- `cognitive_dimensions[]`
- `action_functions[]`
- `motor_states[]`
- `assertions[]` with assertion-level epistemic status

## Relation layer v0.5 — REVIEW COMPLETE

Nova v1 produced **97 unique lexical resonance pairs**.

Semantic-review outcome:

- **92 pairs** produce at least one accepted typed semantic edge;
- **5 pairs** are explicitly rejected as lexical/context artifacts;
- **96 typed edges** are accepted in total because some pairs legitimately encode more than one relation.

Accepted-edge provenance:

- `source_explicit`: **56**
- `source_supported`: **40**
- accepted `proposed` Nova edges: **0**

Lux pathway hypotheses remain separate from the Nova semantic graph.

## Reviewed graph topology

- Nodes: **92**
- Typed edges: **96**
- Connected components in undirected projection: **29**
- Largest component: **64 nodes**
- Isolated concepts: **28**
- Main hubs: `Lucidité` (17), `Zone de bascule` (16), `Endormissement` (9), `Décrochage` (8)

Isolation is not automatically repaired. A concept stays isolated until a justified relation source exists.

## Phosphenic Pathway v0.1 — MODELLED AND VALIDATED

- Status: `experimental_proposal`
- **8 stages**
- **9 pathway transitions**
- **15 canonical NC term references**
- Pathway QA errors: **0**

The pathway is explicitly separate from the NC ontology. It supports optional branches and optional marker sets and does not claim a universal sequence.

## Structured-report layer — BOOTSTRAPPED

Created:

- `schemas/experience-report-v0.1.schema.json`
- `docs/REPORTING_PROTOCOL.md`
- synthetic end-to-end test fixture
- canonical pathway validator
- pathway-report aggregator

Current report status:

- report files: **1 synthetic fixture**
- empirical reports: **0**
- synthetic reports included in empirical statistics: **0**
- pathway/report QA errors: **0**

The empirical baseline is therefore correctly **zero**.

## Build automation

The repository contains reproducible builders for:

- normalized v0.5 consolidation (`scripts/build_v05.py`);
- conservative lexical-resonance candidate generation (`scripts/suggest_relations.py`);
- graph export + QA (`scripts/build_graph_v05.py`);
- pathway validation (`scripts/validate_pathways.py`);
- structured-report aggregation (`scripts/analyze_pathway_reports.py`).

A GitHub Actions workflow is configured to regenerate derived `data/v0.5`, `graph/v0.5`, `analysis`, and QA artifacts. The connected GitHub interface has not yet exposed a successful bot-generated artifact commit, so generated-export execution remains to be verified. Reviewed semantic/relationship data is already committed and does not depend on that unresolved CI visibility.

## Open work

### Issue #2 — v0.5 generated exports

- verify generated consolidated 92-node export;
- verify GraphML/JSON export from the reviewed 96-edge relation layer;
- close when CI/generated artifacts are confirmed.

### Issue #3 — empiricalize Phosphenic Pathway

- encode genuine/anonymized reports;
- calculate actual stage/transition frequencies;
- allow evidence to confirm, weaken, branch, or falsify v0.1.

## Later layers

- scientific-source mapping;
- Monroe / Gateway crosswalk;
- Vieira / Conscientiology crosswalk;
- public/interactive application only after provenance and reuse boundaries are settled.
