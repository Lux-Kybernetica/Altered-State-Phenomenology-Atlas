# External source-claim layer — manual audit v0.1

## Files reviewed

1. `sources/monroe-gateway-focus-claims-v0.1.json`
2. `sources/monroe-gateway-freedom-claims-v0.1.json`
3. `sources/vieira-projectiology-claims-v0.1.json`

## Current volume

- Monroe/Gateway claims: **25**
- Vieira/Projectiology claims: **13**
- Total typed external claims: **38**

## Monroe claim distribution

- `program_definition`: 6
- `procedural_instruction`: 9
- `interpretive_claim`: 5
- `metaphysical_claim`: 5

Import policy:

- `crosswalk_eligible`: 13
- `context_only`: 2
- `do_not_import_as_fact`: 10

### Focus tranche

Focus 3/10/12/15/21/27 contribute 10 claims. Program definitions are separated from interpretive/metaphysical additions such as nonphysical-system access or afterlife-reception framing.

### Freedom tranche

Liftoff, Vectors and First-Stage Separation contribute 15 claims:

- 9 procedural instructions eligible for phenomenological/operational comparison;
- 4 interpretive mechanism claims;
- 2 metaphysical claims involving nonphysical energy / second-body framing.

The procedural content can therefore support mappings such as Log-rolling ↔ Rotation volontaire without treating the Gateway explanation of a separable second body as established fact.

## Vieira claim distribution

- `framework_definition`: 7
- `interpretive_claim`: 3
- `metaphysical_claim`: 3

Import policy:

- `crosswalk_eligible`: 6
- `context_only`: 1
- `do_not_import_as_fact`: 6

## Boundary checks

- No metaphysical claim is marked `crosswalk_eligible`.
- No interpretive mechanism claim is marked `crosswalk_eligible`.
- Phenomenological/framework definitions may be crosswalk-eligible without importing their source ontology.
- Procedural instructions may support technique mappings without proving the framework's proposed mechanism.
- Every current claim has an explicit `source_basis`.
- Claim subjects resolve to concepts declared in the external crosswalk layer.

## Important architecture change

The source-claim vocabulary was generalized beyond Monroe by adding `framework_definition`.

`program_definition` remains appropriate for Gateway Focus states because they are training-program units. `framework_definition` is used for Projectiology concepts such as Estado vibracional, Psicossoma and Catalepsia projetiva.

## Result

**PASS at manual review — 38 external claims are typed with explicit import boundaries, preventing program/framework/procedural definitions from silently promoting interpretive or metaphysical assertions into Nova.**

Automated validation remains implemented in `scripts/validate_external_claims.py`; GitHub Actions execution is still unresolved.
