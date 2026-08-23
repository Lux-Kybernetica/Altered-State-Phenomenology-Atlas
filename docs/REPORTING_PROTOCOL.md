# Structured experience-report protocol v0.2

The purpose of the report layer is to make experiential sequences **comparable without flattening testimony into interpretation or learned vocabulary**.

The canonical machine-readable format for new reports is now `schemas/experience-report-v0.2.schema.json`. The v0.1 schema remains supported for legacy/synthetic fixtures.

## Three distinct layers inside a report

### 1. Raw description

What the participant says happened, as close as practical to their own wording.

Example:

> "I felt as if I were rotating while my physical body seemed still."

The raw report should be frozen before Nova labels are assigned.

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

## Semantic-contamination variables — new in v0.2

A vocabulary convergence is less independent if the participant already knows the terms being tested. New reports therefore record:

- prior framework exposure and level;
- whether that exposure occurred before the experience;
- whether terminology was supplied before the report;
- elicitation mode;
- whether Nova terms were shown before raw description;
- whether Monroe/Vieira/other external terms were shown before raw description;
- whether raw text was frozen before coding.

Exposure does not invalidate a report. It changes the kind of inference we can make from vocabulary/phenomenology convergence.

See `docs/BLIND_REPORTING_PROTOCOL.md`.

## Elicitation classes

v0.2 distinguishes:

- `spontaneous_free_report`
- `open_interview`
- `structured_neutral_prompts`
- `term_prompted`

Term-prompted reports remain useful for trained-practice research but should not be treated as independent lexical convergence.

## Provenance and memory delay

New reports record:

- delay between experience and capture when known;
- original language;
- literature/source reference when applicable;
- whether the report was transcribed from audio.

A fresh report and a reconstruction years later may both be informative, but they should never silently carry identical memory assumptions.

## Coding method

v0.2 records whether mapping was:

- single analyst;
- independent double coding;
- consensus/adjudication;
- participant self-coding.

For high-value convergence cases, independent double coding is preferred. Disagreement is preserved before consensus.

## Evidence classes

The analysis pipeline now separates:

1. direct participant reports (`self_report`, `interview`);
2. `literature_case` records;
3. `synthetic_test` fixtures.

Synthetic fixtures never enter evidence counts. Literature cases are not silently pooled with direct participant reports. A combined view is explicitly exploratory only.

## Report quality

Three minimum fields remain tracked:

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

## Aggregation goals

Once genuine reports exist, the analysis layer should calculate at minimum:

- frequency of each mapped NC term;
- frequency of pathway-stage occurrence;
- A-before-B counts;
- A-without-B / B-without-A counts;
- branch frequencies;
- transition frequency by induction context;
- source-type-stratified counts;
- semantic-exposure-stratified counts;
- weighted sensitivity analyses using mapping and temporal-order confidence.

No threshold for "proof" is defined at this stage.

## Core rule

**Raw phenomenology first. Vocabulary second. Theory last.**
