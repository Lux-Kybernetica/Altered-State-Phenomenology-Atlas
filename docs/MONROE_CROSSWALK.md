# Monroe / Gateway crosswalk

The Monroe / Gateway layer is an **external vocabulary alignment**, not a merger of ontologies.

## Why this exists

Nova Conscientia and Gateway describe partially overlapping phenomenology using different conceptual systems. A useful research model must be able to ask:

- does a Gateway cue resemble an NC phenomenon?
- does a Gateway technique target an NC transition?
- does a Focus-state description overlap an NC state or process?
- where do the systems explicitly diverge?

These questions do not require asserting that their terms mean the same thing.

## Allowed mapping language

The v0.1 crosswalk uses deliberately asymmetric/weak relations:

- `operationally_similar_to`
- `partial_overlap`
- `may_manifest_as`
- `technique_targets`
- `distinguish_from`
- `no_direct_equivalent`

There is intentionally no `same_as` relation.

## Important examples

### Focus 10

Gateway defines Focus 10 operationally as a state where the mind remains awake/alert while the body sleeps or is profoundly relaxed.

This overlaps strongly with NC `Endormissement conscient`, but the concepts are not identical:

- Focus 10 is a program-defined target state;
- Endormissement conscient is an NC transition/process concept;
- the external terminology and theoretical framework remain distinct.

### Vibrations

Gateway manuals describe possible subjective vibration, tingling, shaking and electric-like sensations. These can be compared phenomenologically with NC `État vibratoire`.

This mapping is **restricted to perceived sensations**. Gateway's broader language about vibrational or nonphysical energy is not converted into the NC phenomenon.

### Rotation

Odyssey's Point of Departure deliberately instructs a 180° rotation. This is a very strong procedural analogue for NC `Rotation volontaire`.

The technique can also be modeled as targeting an NC-like `Décrochage` transition without importing Monroe's energy-body explanation.

### Non-forcing

Gateway repeatedly warns that expectations, checking whether separation is occurring, and trying too hard can interfere with the exercise. This is operationally close to NC `Lâcher-prise` and contrasts with NC `Hypercontrôle`.

### Click-out

Gateway explicitly distinguishes click-out from ordinary sleep and describes absent immediate recall / no perceived elapsed time. NC `Amnésie de retour` shares a memory dimension, but the temporal contexts differ. The mapping therefore remains weak (`partial_overlap`).

## Architecture

```text
NOVA CANONICAL CONCEPTS
        ↑
        │ explicit crosswalk records
        │
MONROE / GATEWAY CONCEPTS
        │
        └── source-specific theory remains here
```

External concepts never become Nova graph nodes merely because a crosswalk exists.

## Current v0.1

- 12 Monroe/Gateway external concepts
- 14 mappings
- 0 identity/equivalence mappings
- 0 unresolved canonical NC references after manual audit

See:

- `crosswalks/monroe-gateway-v0.1.json`
- `schemas/external-crosswalk-v0.1.schema.json`
- `scripts/validate_crosswalks.py`
- `audit/monroe-crosswalk-v0.1.md`

## Next expansion

The next Monroe pass should model the Focus ladder and exercise techniques more completely, while distinguishing four kinds of source material:

1. program definitions;
2. procedural instructions;
3. generalized participant reports;
4. Monroe/Institute interpretive or metaphysical claims.

Only the first three can normally support phenomenological or operational crosswalks. Interpretive claims remain attributable source content until independently supported elsewhere.
