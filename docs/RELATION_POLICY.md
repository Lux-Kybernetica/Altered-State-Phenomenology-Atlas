# Typed relation policy — v0.5

Nova v1 `relations` are preserved as **lexical resonance links**. They are useful for navigation but do not by themselves specify semantic meaning, direction, causality, or temporal order.

The v0.5 graph therefore uses a separate typed-edge layer.

## Allowed semantic relations

| Relation | Direction | Meaning |
|---|---|---|
| `is_a` | A → B | A is a subtype / specific form of B |
| `part_of` | A → B | A is a constituent/aspect of B |
| `precedes` | A → B | A may occur temporally before B in the described context |
| `follows` | A → B | inverse temporal wording; normalize to `precedes` when possible |
| `co_occurs_with` | symmetric | A and B may occur together |
| `facilitates` | A → B | A is described as making B easier/more likely; **not equivalent to causes** |
| `inhibits` | A → B | A is described as interfering with B; **not equivalent to prevents** |
| `distinguish_from` | symmetric | the source/model explicitly says not to conflate A with B |
| `may_trigger` | A → B | A is reported/described as potentially initiating B; causal confidence remains limited |
| `may_contain` | A → B | B can occur as content/component within A |
| `associated_with` | symmetric | weak semantic relation when stronger wording is not justified |

## Epistemic provenance

Every typed edge must retain one of these statuses:

- `source_explicit` — Nova directly states the relation;
- `source_supported` — Nova wording supports it, but the edge is a formalization;
- `proposed` — Lux hypothesis / structural proposal requiring further evidence.

External evidence will later use separate provenance metadata rather than being silently merged into Nova support.

## Direction rules

### Symmetric by definition

- `co_occurs_with`
- `distinguish_from`
- `associated_with`

Only one canonical edge should be stored for these.

### Directional

- `is_a`
- `part_of`
- `precedes`
- `follows`
- `facilitates`
- `inhibits`
- `may_trigger`
- `may_contain`

Direction must be justified by source wording or explicit proposal.

## Causality rule

Temporal sequence is **not causality**.

`A precedes B` does not imply:

- `A causes B`;
- `A is necessary for B`;
- `A is sufficient for B`.

Likewise, `facilitates` deliberately encodes weaker wording than causation.

## Pathway separation

Repeated or proposed experiential sequences belong to a **Pathway model**, not directly to ontology edges.

For example:

`Phosphènes → Images hypnagogiques → Zone de bascule → Décrochage`

may later exist as a pathway hypothesis even when individual `precedes` edges remain only proposed. This prevents a recurrent narrative sequence from being mistaken for a universal taxonomic law.

## Review order for each Nova resonance pair

1. Is the relation only lexical? If yes, keep no semantic edge.
2. Does Nova explicitly distinguish the two terms? → `distinguish_from`.
3. Is one contained in / part of the other? → `may_contain` or `part_of`.
4. Is temporal order explicitly described? → `precedes`.
5. Are they described as occurring together? → `co_occurs_with`.
6. Is a functional effect described without strong causality? → `facilitates` / `inhibits`.
7. If meaningful but underspecified → `associated_with`.
8. If the relationship is only our model hypothesis → mark `proposed`.

## Non-goal

The graph is not intended to adjudicate whether a SHC interpretation is metaphysically true. It models terminology, phenomenology, operational concepts, reported relations, and provenance.
