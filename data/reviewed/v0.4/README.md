# Reviewed annotations — v0.4

This directory contains the manually reviewed Lux annotations currently considered the semantic reference layer.

## Coverage

**92 / 92 Nova v1 terms have now received manual semantic review.**

Completed source families:

- **États & lucidité: 11 / 11**
- **Transitions: 15 / 15**
- **Phénomènes perceptifs: 25 / 25**
- **Navigation / actions: 19 / 19**
- **Obstacles: 13 / 13**
- **Sécurité: 9 / 9**

## Review batches

- Pilot: 10 terms
- Batch 1: 8 additional cross-family terms
- Batch 2: remaining Transitions
- Batch 3: remaining États & lucidité
- Batch 4: remaining Phénomènes perceptifs
- Batch 5: remaining Navigation / actions + Lâcher-prise alignment
- Batch 6: Obstacles
- Batch 7: Sécurité

## Semantic axes currently used

- `types[]`
- `modalities[]`
- `phases[]`
- `selfhood_dimensions[]`
- `cognitive_dimensions[]`
- `action_functions[]`
- `motor_states[]`
- `assertions[]` with assertion-level epistemic status

## Important

The source definitions are not duplicated or rewritten here. They live under `data/source/terms-*.json`, while this directory stores the Lux semantic layer. This separation is deliberate: **source, analysis and proposal must remain distinguishable**.

The next phase is consolidation into a v0.5 dataset and a separate systematic pass over typed relations. Manual classification being complete does **not** mean every causal or sequential relation is validated.
