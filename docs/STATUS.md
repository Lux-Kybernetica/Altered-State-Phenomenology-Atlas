# Current status

## 1. Nova source layer — COMPLETE

- Nova Conscientia nomenclature v1.0 captured.
- **92 terms** extracted across **6 source families**.
- Original lexical-resonance mechanism preserved separately.
- Original Nova wording remains separate from Lux annotations.

## 2. Lux semantic layer v0.4 — COMPLETE

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

## 3. Relation layer v0.5 — REVIEW COMPLETE

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

## 4. Reviewed graph topology

- Nodes: **92**
- Typed edges: **96**
- Connected components in undirected projection: **29**
- Largest component: **64 nodes**
- Isolated concepts: **28**
- Main hubs: `Lucidité` (17), `Zone de bascule` (16), `Endormissement` (9), `Décrochage` (8)

Isolation is not automatically repaired. A concept stays isolated until a justified relation source exists.

## 5. Phosphenic Pathway v0.1 — MODELLED AND VALIDATED

- Status: `experimental_proposal`
- **8 stages**
- **9 pathway transitions**
- **15 canonical NC term references**
- Pathway QA errors: **0**

The pathway is explicitly separate from the NC ontology. It supports optional branches/marker sets and does not claim a universal sequence.

## 6. Structured-report layer — BOOTSTRAPPED AND HARDENED

Created:

- structured experience-report schema;
- v0.2 anti-contamination variables;
- non-leading reporting protocol;
- participant-facing form specification;
- synthetic end-to-end test fixture;
- pathway-report aggregator.

Current empirical status:

- synthetic fixtures: **1**
- empirical reports: **0**
- synthetic reports included in empirical statistics: **0**

The empirical baseline therefore remains correctly **zero**.

The reporting layer now tracks prior familiarity with Nova / Gateway / Projectiology, pre-report vocabulary exposure, interview style, recall delay and raw-report locking so cross-tradition convergence is not confused with shared learned language.

## 7. Monroe / Gateway layer — ACTIVE

Implemented:

- baseline Gateway crosswalk;
- Focus-level modeling work;
- Freedom technique analysis;
- source-claim typing separating program definition / procedure / interpretation / metaphysical claim;
- conservative crosswalk policy forbidding automatic identity mappings.

Strong operational comparisons include:

- perceived vibrations ↔ `nova.etat_vibratoire`;
- log-rolling / rotation technique ↔ `nova.rotation_volontaire`;
- non-forcing / release of expectations ↔ `nova.lacher_prise`;
- return / grounding / journaling ↔ relevant Nova navigation/post-experience concepts.

Focus states remain program-specific and are not treated as universal consciousness levels.

## 8. Vieira / Projectiology layer v0.1 — BOOTSTRAPPED

Current first pass:

- external concepts: **7**
- mappings: **7**
- typed source claims: **13**

Important mappings:

- `estado vibracional` ↔ `nova.etat_vibratoire` — strong phenomenological similarity;
- `semiprojeção` ↔ `nova.sortie_partielle` — structural overlap;
- `decolagem do psicossoma` ↔ `nova.decrochage` — transition overlap with explicit ontological asymmetry;
- `psicossoma` ↔ `nova.corps_de_sortie` — partial overlap only, never identity.

Projectiology framework ontology remains external to Nova.

## 9. External source-claim layer — ACTIVE

Current manually typed external claims across Monroe / Freedom / Projectiology: **38**.

The schema distinguishes:

- `program_definition`
- `framework_definition`
- `procedural_instruction`
- `participant_report_generalization`
- `interpretive_claim`
- `metaphysical_claim`

Interpretive/metaphysical claims cannot be silently used as direct Nova crosswalk evidence.

## 10. Cross-tradition convergence layer — BOOTSTRAPPED

A first Nova × Monroe × Vieira matrix is available.

High-priority cross-tradition clusters currently include:

1. **État vibratoire**
2. **Décrochage / altered self-location transition**
3. **Sortie partielle**

These are treated as **research targets**, not consensus-based validation.

## 11. Scientific evidence layer v0.1 — BOOTSTRAPPED

Core catalogue:

- peer-reviewed studies: **11**
- scientific-to-Nova links: **29**
- distinct Nova concepts linked: **10**

Domains currently covered:

- bodily self-consciousness / self-location;
- hypnagogia and sleep onset;
- sleep paralysis / vestibular-motor hallucinations;
- lucid REM dreaming and real-time measurement.

Scientific link roles include:

- experimental analogue;
- mechanistic context;
- clinical context;
- phenomenology context;
- measurement precedent;
- operationalization support;
- alternative explanation.

Every study includes limitations and a `does_not_establish[]` boundary.

Scientific disagreement is preserved explicitly; e.g. Voss et al. 2009 is retained alongside Baird, Tononi & LaBerge 2022, which weakens the earlier frontolateral 40-Hz / hybrid-state interpretation.

## 12. Nova Conscientia handoff package — READY v0.1

Human-facing contribution material now exists under:

`deliverables/nova-conscientia/`

Including:

- `README.md`
- `CONTRIBUTION_BRIEF.md`
- `IMPLEMENTATION_PLAN.md`
- `DATA_DICTIONARY.md`
- `GAPS_AND_PRIORITIES.md`
- `REPORT_FORM_SPEC.md`
- `OUTREACH_DRAFT.md`
- `WHAT_TO_SHOW_FIRST.md`

The handoff is deliberately incremental: Nova can adopt relations, provenance, report forms, scientific links or multi-axial metadata independently without replacing its current Skill Tree.

## 13. Build automation

The repository contains reproducible builders/validators for:

- normalized v0.5 consolidation (`scripts/build_v05.py`);
- lexical-resonance candidate generation (`scripts/suggest_relations.py`);
- graph export + QA (`scripts/build_graph_v05.py`);
- pathway validation (`scripts/validate_pathways.py`);
- structured-report aggregation (`scripts/analyze_pathway_reports.py`);
- external crosswalk validation (`scripts/validate_crosswalks.py`);
- external source-claim validation (`scripts/validate_external_claims.py`);
- convergence validation (`scripts/validate_convergences.py`);
- scientific evidence validation (`scripts/validate_scientific_evidence.py`).

GitHub Actions is configured, but no workflow run is currently exposed even after a diagnostic PR. This remains a tooling/Actions execution issue rather than a known semantic-model failure. Reviewed data and handoff artifacts are committed independently of CI.

## Open work

### Issue #2 — generated v0.5 exports / CI

- verify consolidated 92-node export;
- verify generated GraphML/JSON export;
- resolve why GitHub Actions produces no visible run.

### Issue #3 — empiricalize Phosphenic Pathway

- encode genuine/anonymized reports;
- calculate stage/transition frequencies;
- allow evidence to confirm, weaken, branch or falsify v0.1.

### Issue #5 — Monroe expansion

- continue direct-source Focus/technique coverage;
- strengthen source-location metadata;
- preserve no-equivalent decisions.

### Issue #6 — Vieira expansion

- recover additional terms from direct Projectiology source material;
- verify inherited Nova `(Vieira)` labels individually;
- maintain framework/metaphysics boundary.

## Next strategic milestone

The project no longer needs more taxonomy before producing value.

The next high-value steps are:

1. collect high-quality blind/low-suggestion reports;
2. test the three major convergence clusters;
3. expand the scientific layer only where it answers a defined question;
4. produce a lightweight interactive explorer once the data-export/CI path is stable;
5. approach Nova with the human-facing contribution brief rather than the entire repository at once.
