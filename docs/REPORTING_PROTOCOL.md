# Structured experience-report protocol v0.1

The purpose of the report layer is to make experiential sequences **comparable without flattening testimony into interpretation**.

## Three distinct layers inside a report

### 1. Raw description

What the participant says happened, as close as practical to their own wording.

Example:

> "I felt as if I were rotating while my physical body seemed still."

### 2. NC mapping

An analyst may map the description to one or more canonical Nova terms, for example:

- `nova.rotation`
- `nova.stase`

The mapping is metadata. It does not rewrite the testimony.

### 3. Interpretation

Any explanatory or ontological conclusion remains separate:

- dream interpretation;
- neurological hypothesis;
- energetic-body interpretation;
- spiritual interpretation;
- uncertainty.

Interpretation is never required for a useful phenomenological report.

## Temporal structure

Events receive an integer `sequence`. Exact timestamps are optional.

This allows us to distinguish:

- A was reported before B;
- A and B were reported in the same event block;
- order is uncertain;
- a stage was not reported.

Absence of a reported stage does **not** automatically mean the phenomenon did not occur; report completeness and recall confidence remain relevant.

## Mapping confidence

Every event mapping carries:

- `reported_explicitly`
- `analyst_mapped`
- `uncertain`

plus a numeric confidence from 0 to 1.

This prevents later statistics from treating an analyst's weak inference as if the participant had named the phenomenon directly.

## Report quality

Three minimum fields are tracked:

- recall confidence;
- temporal-order confidence;
- completeness.

These are report-quality variables, not judgments about whether the experience was "real".

## Privacy / consent scope

Reports carry an explicit scope:

- `private_research`
- `anonymized_analysis`
- `publication_allowed`
- `synthetic_only`

Personally identifying details should not be required for pathway analysis.

## Synthetic fixtures

Files with `source_type: synthetic_test` exist only to test schemas and analysis code.

They **must be excluded** from empirical counts. A synthetic report becoming a supporting data point because somebody forgot a filter would be an almost perfect parody of bad consciousness research, so the software will guard against it explicitly.

## Future aggregation

Once genuine reports exist, the analysis layer should calculate at minimum:

- frequency of each mapped NC term;
- frequency of pathway-stage occurrence;
- A-before-B counts;
- A-without-B / B-without-A counts;
- branch frequencies;
- transition frequency by induction context;
- weighted counts using mapping and temporal-order confidence.

No threshold for "proof" is defined at this stage.
