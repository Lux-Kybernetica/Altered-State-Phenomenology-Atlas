# Phosphenic Pathway report-analysis QA

- Canonical NC IDs available: **92**
- Report JSON files discovered: **1**
- Synthetic fixtures: **1**
- Participant reports (`self_report` / `interview`): **0**
- Literature cases: **0**
- Non-synthetic reports: **0**
- Errors: **0**

## Evidence status

**No non-synthetic pathway evidence exists yet. Participant and literature stage/transition counts are correctly zero.**

The existing synthetic fixture is parsed and reference-checked but excluded before any evidence count.

## Evidence-class guards

The report pipeline now keeps three evidence classes separate:

1. participant reports (`self_report`, `interview`);
2. literature cases;
3. synthetic fixtures.

Literature cases are never silently pooled with direct participant reports. A combined non-synthetic view may exist only as an explicitly exploratory output.

## Semantic-exposure guard

Experience-report schema v0.2 records:

- prior framework exposure;
- terminology exposure before the report;
- elicitation mode;
- whether NC/external labels were shown before raw description;
- whether the raw report was frozen before mapping;
- capture delay.

This allows later convergence analyses to stratify reports by semantic-contamination risk rather than pretending that trained vocabulary and spontaneous description are equally independent.

The current synthetic v0.1 fixture is classified as `not_recorded_v0.1`; it remains excluded regardless.

## Result

**PASS at manual baseline — the current zero-evidence state is preserved while the pipeline now distinguishes synthetic, participant, literature and semantic-exposure strata.**
