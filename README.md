# Altered-State Phenomenology Atlas

> **Open research atlas for describing, comparing and studying altered-state phenomenology across experiential taxonomies, practice traditions and scientific literature.**

The **Altered-State Phenomenology Atlas** is an independent research project developed by **Lux Kybernetica**.

It began as a structural analysis of the public **Nova Conscientia French SHC nomenclature v1.0** and progressively expanded into a broader framework for representing altered-state experiences without forcing phenomenology, interpretation, tradition and scientific evidence into the same conceptual layer.

The project is not an official Nova Conscientia publication and does not replace their Skill Tree. Nova's original nomenclature remains attributed to Nova Conscientia and is used here as the first structured source corpus.

Original Nova Conscientia nomenclature:
https://novaconscientia.com/nc-skill-tree.html

---

## Why this exists

A pedagogical tree is excellent for exploration, but research questions require a different structure.

A single reported event may simultaneously involve:

- a **state of consciousness**;
- a **temporal phase**;
- a perceptual **modality**;
- a change in **self-location / embodiment**;
- a cognitive or motor dimension;
- a relation to another phenomenon;
- an interpretation proposed by a particular tradition.

The atlas therefore keeps the public-facing taxonomy conceptually simple while allowing a richer model underneath.

The core epistemic rule is:

```text
SOURCE
  what a corpus actually says

OBSERVATION / DESCRIPTION
  what is reported or measured

ANALYSIS
  how the material is classified

INTERPRETATION
  what a framework says it means

HYPOTHESIS / PROPOSAL
  what remains to be tested
```

These layers are deliberately kept separate.

---

# Current state

## Nova Conscientia semantic layer

- **92 / 92 terms manually reviewed**
- **6 source families preserved**
- **97 / 97 original lexical resonance pairs semantically reviewed**
- **96 typed semantic relations accepted**
- **5 lexical links explicitly rejected as semantic edges**

The model currently supports independent axes for:

```text
types[]
modalities[]
phases[]
selfhood_dimensions[]
cognitive_dimensions[]
action_functions[]
motor_states[]
assertions[]
```

Assertions carry epistemic status and provenance.

## Reviewed semantic graph

Current reviewed topology:

- **92 nodes**
- **96 typed edges**
- **29 connected components** in the undirected projection
- **64 nodes** in the largest component
- **28 currently isolated concepts**

Major hubs emerging from the reviewed source structure include:

- **Lucidité**
- **Zone de bascule**
- **Endormissement**
- **Décrochage**

Isolated concepts are not automatically connected merely to make the graph look complete.

---

# External frameworks

The atlas does not treat traditions as interchangeable dictionaries.

A correspondence means phenomenological or operational overlap, **not identity**.

## Monroe / Gateway Experience

The repository contains a source-aware Gateway crosswalk covering:

- Focus-state terminology;
- perceived vibrations and buzzing;
- hypnagogic imagery;
- separation techniques;
- Liftoff, Vectors and First-Stage Separation material;
- deliberate rotation / log-rolling;
- return, grounding and journaling practices.

Program definitions, procedural instructions, interpretations and metaphysical claims are stored separately.

## Vieira / Projeciologia

A first primary-source-oriented Projectiology crosswalk currently includes concepts such as:

- `estado vibracional`;
- `decolagem do psicossoma`;
- `semiprojeção`;
- `projeção semiconsciente`;
- `catalepsia projetiva`;
- `psicossoma`;
- `ballonnement`.

Framework ontology remains external to the Nova semantic layer.

For example, **Psicossoma is not encoded as identical to Nova's Corps de sortie**: one is a framework-defined vehicle, while the Nova concept can remain a description of perceived embodiment.

---

# Cross-tradition convergence

The atlas currently tracks convergence as a **research target**, not a vote on metaphysical truth.

Three especially interesting multi-tradition clusters have already emerged:

```text
État vibratoire
Décrochage
Sortie partielle
```

These clusters are represented through a comparative matrix linking Nova, Monroe and Vieira while preserving theoretical disagreement.

A shared description across traditions may indicate:

- a recurrent phenomenological structure;
- a learned vocabulary;
- a shared technique;
- cultural contamination;
- or some combination of these.

The project is designed to distinguish those possibilities rather than assume one.

---

# Scientific evidence layer

The repository includes a first scientific evidence catalogue connecting peer-reviewed research to Nova concepts through explicit roles such as:

```text
experimental_analogue
mechanistic_context
clinical_context
phenomenology_context
measurement_precedent
operationalization_support
alternative_explanation
```

The initial catalogue contains **11 studies** and **29 concept links**.

Topics currently covered include:

- experimentally manipulated self-location and body ownership;
- temporo-parietal / multisensory context for OBE-like phenomena;
- sleep paralysis and vestibulo-motor experiences;
- hypnagogic imagery and sleep-onset EEG;
- lucid dreaming and REM verification;
- real-time communication during lucid dreams.

Every study record also contains:

- methodological limitations;
- what the result supports;
- and explicitly **what it does not establish**.

Scientific studies are not used as automatic validation or refutation of traditional interpretations.

---

# Phosphenic Pathway

The repository also contains an experimental **Phosphenic Pathway v0.1**.

It is deliberately modeled separately from the ontology.

Current working architecture:

```text
Phosphènes
    ↓
Hypnagogie / images
    ↓
Zone de bascule
    ↓
optional transition markers
    ↓
Décrochage
    ↓
possible partial / complete exit-like outcome
```

Possible marker phenomena include vibrations, buzzing, floating, rotation, traction and stasis.

None is encoded as a universal prerequisite.

The pathway is a falsifiable working model, not a canonical sequence.

---

# Structured experience reports

A major goal of the atlas is to transform taxonomies into tools for empirical comparison.

The reporting protocol therefore separates:

1. **free narrative**;
2. temporal reconstruction;
3. open clarification;
4. narrative lock;
5. analyst mapping to canonical terms;
6. interpretation only afterward.

The report model records potential sources of semantic contamination, including prior exposure to Monroe, Vieira or related traditions and whether terminology was shown before the narrative was recorded.

The aim is to distinguish genuine phenomenological convergence from learned vocabulary.

Synthetic test fixtures are explicitly excluded from empirical statistics.

---

# Repository structure

```text
.
├── data/                 # Nova source, reviewed annotations and semantic relations
├── graph/                # graph exports / graph tooling
├── schemas/              # machine-readable data contracts
├── crosswalks/           # Monroe, Vieira and external-framework mappings
├── sources/              # typed source assertions
├── evidence/             # scientific evidence catalogue
├── pathways/             # experimental temporal models
├── reports/              # structured experience-report layer
├── analysis/             # convergence and pathway analyses
├── audit/                # human and automated QA reports
├── docs/                 # method, policy, decisions and status
└── deliverables/
    └── nova-conscientia/ # contribution package prepared for Nova Conscientia
```

---

# If you are from Nova Conscientia

The most useful starting point is:

### 1. One-page overview

`deliverables/nova-conscientia/ONE_PAGE_SUMMARY.md`

### 2. Contribution brief

`deliverables/nova-conscientia/CONTRIBUTION_BRIEF.md`

### 3. What can be adopted independently

`deliverables/nova-conscientia/IMPLEMENTATION_PLAN.md`

### 4. Reporting / research protocol

`deliverables/nova-conscientia/REPORT_FORM_SPEC.md`

The contribution is modular.

Nova can adopt only the pieces that are useful, for example:

- typed relations;
- embodiment/cognition/motor axes;
- provenance;
- scientific references;
- reporting protocol;
- external crosswalks;
- or the broader knowledge model.

**No complete redesign of the current Skill Tree is required.**

---

# Methodological principles

1. **Preserve sources before interpreting them.**
2. **Do not confuse phenomenology with ontology.**
3. **Do not turn temporal order into causality.**
4. **Do not turn cross-tradition similarity into equivalence.**
5. **Keep hypotheses falsifiable.**
6. **Record uncertainty and provenance.**
7. **Allow concepts to remain isolated when evidence does not justify a link.**
8. **Treat disagreement as data rather than something to erase.**

---

# Attribution and status

The **Nova Conscientia SHC nomenclature** and original Nova website material are third-party work and remain attributed to Nova Conscientia.

This repository contains independent Lux Kybernetica analysis, schemas, annotations, crosswalks, research tooling and experimental models built around publicly available source material and cited external literature.

The project is currently a **working research atlas**, not a validated clinical taxonomy and not an adjudication of metaphysical claims regarding altered states or out-of-body experience.

---

## Short version

> **Pedagogical taxonomy at the surface. Traceable knowledge model, comparative framework and research instrument underneath.**
