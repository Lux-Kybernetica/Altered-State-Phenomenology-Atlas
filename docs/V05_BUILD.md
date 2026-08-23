# v0.5 build pipeline

The v0.5 layer is **generated**, not hand-maintained.

## Inputs

- `data/source/terms-*.json` — Nova Conscientia v1 source layer.
- `data/reviewed/v0.4/*.json` — 92 manually reviewed Lux semantic records.
- `data/reviewed/v0.4/vocabularies.json` — controlled values.

## Builder

`scripts/build_v05.py`

The builder performs six jobs:

1. verifies that Nova source contains exactly 92 unique terms and IDs `t0..t91`;
2. verifies that exactly one reviewed Lux annotation exists for every source term;
3. validates controlled values used by the semantic axes and relation assertions;
4. creates a normalized 92-node v0.5 dataset;
5. preserves Nova's original lexical resonance network as a separate undirected edge layer;
6. extracts already-reviewed typed relation assertions as a seed and creates a queue for systematic relation review.

## Generated outputs

`data/v0.5/nova-v0.5.json`
: complete normalized model, source + semantic layers.

`data/v0.5/nodes.json`
: graph-ready node records.

`data/v0.5/manifest.json`
: source ID ↔ canonical ID ↔ review-file traceability.

`data/v0.5/resonance-edges-original.json`
: Nova v1 lexical resonance pairs. These are preserved as source behavior, **not treated as semantic truth**.

`data/v0.5/typed-edges-seed.json`
: typed relations already present in reviewed Lux assertions.

`data/v0.5/relation-review-queue.json`
: original resonance pairs with typed-seed coverage, ready for relation-by-relation review.

`audit/v0.5-qa-report.md`
: structural QA, counts and failures.

## Automation

`.github/workflows/build-v05.yml` runs the builder when source, reviewed annotations, schemas, or the builder itself change. If generated artifacts differ, GitHub Actions commits them back to `main`.

This makes v0.5 reproducible. The generated dataset is never an opaque manual export.

## Epistemic boundary

The build does **not** automatically turn a Nova resonance into a semantic edge. That would merely put a nicer suit on the same lexical relation mechanism. Typed relations remain a separate review task.
