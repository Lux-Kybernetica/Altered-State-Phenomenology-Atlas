# Current status

## Source layer

- Nova Conscientia nomenclature v1.0 captured.
- 92 terms extracted.
- 6 top-level families extracted.
- Original resonance mechanism reproduced separately.

## Lux semantic layer

### Pilot v0.2
- 10 concepts manually enriched.
- Multiple types allowed.
- Explicit modality arrays.
- Phase model.
- Embodiment/selfhood axis.
- Assertion-level epistemic status.

### Full pre-annotation v0.3
- 92 concepts heuristically pre-annotated.
- Used as a review aid only, not as authoritative classification.

### Manual review v0.4 — COMPLETE

- **92 / 92 terms manually reviewed.**
- **États & lucidité: 11 / 11.**
- **Transitions: 15 / 15.**
- **Phénomènes perceptifs: 25 / 25.**
- **Navigation / actions: 19 / 19.**
- **Obstacles: 13 / 13.**
- **Sécurité: 9 / 9.**

## Model changes discovered during review

- `awakening` phase added for hypnopompic material;
- `situation` and `condition` logical types added;
- motor state separated from perceptual modality;
- `selfhood_dimensions[]` retained for self-location, body ownership, perspective, agency and body boundaries;
- `cognitive_dimensions[]` added for meta-awareness, reasoning clarity, memory continuity, goal maintenance, executive control, attention stability, temporal continuity and reality monitoring;
- `action_functions[]` added to distinguish stabilization, regulation, separation, navigation, interaction, epistemic monitoring, return, memory consolidation and integration;
- source category mismatches are preserved rather than silently corrected;
- absence of perceptual content can still be a state of a modality (`Écran noir`);
- source recommendations and causal claims remain separate from observations, especially in the safety layer.

## Current model axes

- `types[]`
- `modalities[]`
- `phases[]`
- `selfhood_dimensions[]`
- `cognitive_dimensions[]`
- `action_functions[]`
- `motor_states[]`
- `assertions[]` with assertion-level epistemic status

## Next phase — v0.5

1. Consolidate the 92 reviewed annotations into one normalized dataset.
2. Validate all records against the current schema / controlled vocabularies.
3. Systematically review typed relation candidates.
4. Separate explicit-source relations from inferred/proposed relations.
5. Generate the first knowledge-graph export only after relation review.
6. Build the first explicit pathway model separately from the ontology.

## Not done yet

- consolidated v0.5 dataset;
- systematic relation review;
- knowledge-graph export;
- pathway model;
- scientific source layer;
- Monroe/Vieira crosswalks;
- public application.
