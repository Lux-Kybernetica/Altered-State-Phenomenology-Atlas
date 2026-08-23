# External source-claim layer — manual audit v0.1

## Files reviewed

1. `sources/monroe-gateway-focus-claims-v0.1.json`
2. `sources/vieira-projectiology-claims-v0.1.json`

## Current volume

- Monroe/Gateway claims: **10**
- Vieira/Projectiology claims: **13**
- Total typed external claims: **23**

## Monroe claim distribution

- `program_definition`: 6
- `interpretive_claim`: 1
- `metaphysical_claim`: 3

Import policy:

- `crosswalk_eligible`: 4
- `context_only`: 2
- `do_not_import_as_fact`: 4

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
- Every current claim has an explicit `source_basis`.
- Claim subjects resolve to concepts declared in the external crosswalk layer.

## Important architecture change

The source-claim vocabulary was generalized beyond Monroe by adding `framework_definition`.

`program_definition` remains appropriate for Gateway Focus states because they are training-program units. `framework_definition` is used for Projectiology concepts such as Estado vibracional, Psicossoma and Catalepsia projetiva.

## Result

**PASS at manual review — 23 external claims are typed with explicit import boundaries, preventing program/framework definitions from silently promoting interpretive or metaphysical assertions into Nova.**

Automated validation remains implemented in `scripts/validate_external_claims.py`; GitHub Actions execution is still unresolved.
