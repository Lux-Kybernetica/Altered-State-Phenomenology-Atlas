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

## Monroe / Gateway crosswalk v0.1 — BOOTSTRAPPED

External terminology is now modeled without importing Monroe's ontology into Nova.

Current crosswalk:

- external Monroe/Gateway concepts: **12**
- crosswalk mappings: **14**
- identity/equivalence mappings: **0**
- unresolved canonical NC references after manual audit: **0**

Strong operational comparisons currently include perceived vibrations, buzzing, hypnagogic imagery, non-forcing/lâcher-prise, deliberate rotation, intentional return, grounding and journaling.

Important weak/partial mappings remain explicitly weak:

- Focus 10 ↔ Endormissement conscient: operational similarity, not identity;
- Click-out ↔ Amnésie de retour: partial mnemonic overlap only;
- Monroe separation/projection spans several NC transition/outcome concepts.

Files:

- `schemas/external-crosswalk-v0.1.schema.json`
- `crosswalks/monroe-gateway-v0.1.json`
- `scripts/validate_crosswalks.py`
- `docs/MONROE_CROSSWALK.md`
- `audit/monroe-crosswalk-v0.1.md`

## Build automation

The repository contains reproducible builders/validators for:

- normalized v0.5 consolidation (`scripts/build_v05.py`);
- conservative lexical-resonance candidate generation (`scripts/suggest_relations.py`);
- graph export + QA (`scripts/build_graph_v05.py`);
- pathway validation (`scripts/validate_pathways.py`);
- structured-report aggregation (`scripts/analyze_pathway_reports.py`);
- external crosswalk validation (`scripts/validate_crosswalks.py`).

GitHub Actions is configured for push, pull request, and manual dispatch, but no workflow run is currently exposed even after an explicit diagnostic PR. This points to the Actions execution layer not starting rather than a known script failure. Reviewed semantic, relationship, pathway and crosswalk data remain committed independently of CI.

## Open work

### Issue #2 — v0.5 generated exports

- verify generated consolidated 92-node export;
- verify GraphML/JSON export from the reviewed 96-edge relation layer;
- resolve why GitHub Actions produces no visible run;
- close when generated artifacts are confirmed.

### Issue #3 — empiricalize Phosphenic Pathway

- encode genuine/anonymized reports;
- calculate actual stage/transition frequencies;
- allow evidence to confirm, weaken, branch, or falsify v0.1.

### Monroe expansion

- model Focus 3 / 10 / 12 / 15 / 21 / 27 as external program concepts;
- classify source statements as program definition, procedural instruction, participant-report generalization, or interpretive/metaphysical claim;
- expand exercise-technique mappings without introducing identity edges.

## Later layers

- scientific-source mapping;
- Vieira / Projectiology / Conscientiology crosswalk, only from actual source material;
- public/interactive application only after provenance and reuse boundaries are settled.
