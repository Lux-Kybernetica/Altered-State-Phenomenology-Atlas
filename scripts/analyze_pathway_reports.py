#!/usr/bin/env python3
"""Aggregate structured reports against the Phosphenic Pathway.

Evidence classes are kept separate:
- synthetic fixtures are validation-only;
- participant reports are self_report/interview;
- literature cases are analyzed separately;
- v0.2 reports are stratified by semantic/framework exposure.

No external dependencies.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWED = ROOT / "data" / "reviewed" / "v0.4"
PATHWAY_FILE = ROOT / "pathways" / "phosphenic-pathway-v0.1.json"
REPORT_ROOT = ROOT / "reports"
ANALYSIS_DIR = ROOT / "analysis"
AUDIT_DIR = ROOT / "audit"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def semantic_exposure_stratum(report: dict) -> str:
    """Classify vocabulary/framework exposure without treating it as report validity."""
    if report.get("schema_version") != "0.2":
        return "not_recorded_v0.1"

    exposure = report.get("exposure", {})
    elicitation = report.get("elicitation", {})
    coding = report.get("coding", {})

    if (
        elicitation.get("mode") == "term_prompted"
        or elicitation.get("nc_terms_shown_before_raw_report")
        or elicitation.get("external_terms_shown_before_raw_report")
    ):
        return "high_semantic_prompting"

    if exposure.get("terminology_exposure_before_report"):
        return "terminology_exposed"

    levels = []
    for item in exposure.get("framework_exposure", []):
        if item.get("before_experience"):
            levels.append(item.get("level"))
    if any(level in {"trained", "practitioner"} for level in levels):
        return "trained_framework_exposure"
    if any(level in {"familiar"} for level in levels):
        return "moderate_framework_exposure"

    if (
        elicitation.get("mode") in {"spontaneous_free_report", "open_interview", "structured_neutral_prompts"}
        and not elicitation.get("nc_terms_shown_before_raw_report")
        and not elicitation.get("external_terms_shown_before_raw_report")
        and coding.get("raw_report_frozen_before_mapping") is True
    ):
        return "lower_semantic_contamination"

    return "uncertain_exposure"


def map_report_to_pathway(report: dict, term_to_stages: dict[str, set[str]]) -> tuple[set[str], list[str]]:
    event_stage_sets = []
    seen_stages = set()
    for event in sorted(report.get("events", []), key=lambda e: e["sequence"]):
        stages = set()
        for ref in event.get("term_refs", []):
            stages.update(term_to_stages.get(ref, set()))
        event_stage_sets.append((event["sequence"], stages))
        seen_stages.update(stages)

    first_seen = {}
    for sequence, stages in event_stage_sets:
        for stage_id in stages:
            first_seen.setdefault(stage_id, sequence)
    ordered = sorted(first_seen.items(), key=lambda kv: kv[1])
    return seen_stages, [stage_id for stage_id, _ in ordered]


def aggregate(report_group: list[dict], term_to_stages: dict[str, set[str]]) -> tuple[Counter, Counter, list[dict]]:
    stage_occurrence = Counter()
    ordered_transition_counts = Counter()
    sequences = []

    for report in report_group:
        seen_stages, ordered_stage_ids = map_report_to_pathway(report, term_to_stages)
        for stage_id in seen_stages:
            stage_occurrence[stage_id] += 1
        for i, source_stage in enumerate(ordered_stage_ids):
            for target_stage in ordered_stage_ids[i + 1:]:
                ordered_transition_counts[(source_stage, target_stage)] += 1
        sequences.append({
            "report_id": report["id"],
            "source_type": report.get("source_type"),
            "semantic_exposure_stratum": semantic_exposure_stratum(report),
            "stage_sequence": ordered_stage_ids,
        })
    return stage_occurrence, ordered_transition_counts, sequences


def stage_rows(stage_by_id: dict, counts: Counter) -> list[dict]:
    return [
        {
            "stage_id": stage_id,
            "stage_label": stage_by_id[stage_id]["label"],
            "report_count": counts.get(stage_id, 0),
        }
        for stage_id in stage_by_id
    ]


def pair_rows(counts: Counter) -> list[dict]:
    return [
        {"from": a, "to": b, "report_count": count}
        for (a, b), count in sorted(counts.items())
    ]


def main() -> int:
    errors = []

    canonical_ids = set()
    for path in REVIEWED.glob("*.json"):
        if path.name == "vocabularies.json":
            continue
        payload = load(path)
        if "annotation_lux_v0_4" in payload:
            canonical_ids.add(payload["id"])

    pathway = load(PATHWAY_FILE)
    stage_by_id = {stage["id"]: stage for stage in pathway["stages"]}
    term_to_stages = defaultdict(set)
    for stage in pathway["stages"]:
        for term_ref in stage["term_refs"]:
            term_to_stages[term_ref].add(stage["id"])

    report_paths = sorted(REPORT_ROOT.rglob("*.json"))
    reports = []
    source_type_counts = Counter()
    exposure_counts = Counter()

    for path in report_paths:
        payload = load(path)
        reports.append(payload)
        source_type = payload.get("source_type")
        source_type_counts[source_type] += 1
        exposure_counts[semantic_exposure_stratum(payload)] += 1

        sequences = [e.get("sequence") for e in payload.get("events", [])]
        if len(sequences) != len(set(sequences)):
            errors.append(f"{path}: duplicate event sequence values")
        if sequences != sorted(sequences):
            errors.append(f"{path}: events are not sorted by sequence")
        for event in payload.get("events", []):
            for ref in event.get("term_refs", []):
                if ref not in canonical_ids:
                    errors.append(f"{path}: unknown NC term ref {ref}")
        for ref in payload.get("outcome_term_refs", []):
            if ref not in canonical_ids:
                errors.append(f"{path}: unknown outcome term ref {ref}")

    synthetic = [r for r in reports if r.get("source_type") == "synthetic_test"]
    participant_reports = [r for r in reports if r.get("source_type") in {"self_report", "interview"}]
    literature_cases = [r for r in reports if r.get("source_type") == "literature_case"]
    non_synthetic = participant_reports + literature_cases

    participant_stage, participant_pairs, participant_sequences = aggregate(participant_reports, term_to_stages)
    literature_stage, literature_pairs, literature_sequences = aggregate(literature_cases, term_to_stages)
    combined_stage, combined_pairs, combined_sequences = aggregate(non_synthetic, term_to_stages)

    summary = {
        "metadata": {
            "pathway_id": pathway["id"],
            "pathway_version": pathway["version"],
            "report_files_total": len(reports),
            "source_type_counts": dict(source_type_counts),
            "synthetic_reports_excluded": len(synthetic),
            "participant_reports": len(participant_reports),
            "literature_cases": len(literature_cases),
            "non_synthetic_reports": len(non_synthetic),
            "semantic_exposure_strata": dict(exposure_counts),
            "warning": "Synthetic fixtures never contribute to evidence counts. Participant reports and literature cases are also reported separately rather than being silently pooled."
        },
        "participant_reports": {
            "stage_occurrence": stage_rows(stage_by_id, participant_stage),
            "ordered_stage_pairs": pair_rows(participant_pairs),
            "report_stage_sequences": participant_sequences,
        },
        "literature_cases": {
            "stage_occurrence": stage_rows(stage_by_id, literature_stage),
            "ordered_stage_pairs": pair_rows(literature_pairs),
            "report_stage_sequences": literature_sequences,
        },
        "combined_non_synthetic_exploratory": {
            "stage_occurrence": stage_rows(stage_by_id, combined_stage),
            "ordered_stage_pairs": pair_rows(combined_pairs),
            "report_stage_sequences": combined_sequences,
            "warning": "Combined counts are exploratory only; source-type strata remain authoritative for interpretation."
        },
    }

    dump(ANALYSIS_DIR / "phosphenic-pathway-report-summary.json", summary)

    report = [
        "# Phosphenic Pathway report-analysis QA", "",
        f"- Canonical NC IDs available: **{len(canonical_ids)}**",
        f"- Report JSON files discovered: **{len(reports)}**",
        f"- Synthetic fixtures: **{len(synthetic)}**",
        f"- Participant reports (self/interview): **{len(participant_reports)}**",
        f"- Literature cases: **{len(literature_cases)}**",
        f"- Errors: **{len(errors)}**", "",
        "## Evidence status", "",
    ]
    if not non_synthetic:
        report.append("**No non-synthetic pathway evidence exists yet. Participant and literature stage/transition counts are correctly zero.**")
    else:
        report.append("Non-synthetic reports exist; participant reports and literature cases are aggregated in separate strata before any exploratory combined view.")

    report += [
        "", "## Semantic-exposure strata", "",
    ]
    for key, value in sorted(exposure_counts.items()):
        report.append(f"- `{key}`: {value}")

    report += [
        "", "## Guards", "",
        "- `synthetic_test` reports are always excluded from evidence counts.",
        "- `literature_case` is never silently pooled with first-person/interview participant reports.",
        "- v0.2 reports record prompting and prior-framework exposure so vocabulary convergence can be stratified by semantic-contamination risk.",
        "- Exposure strata are methodological descriptors, not validity verdicts on an experience.",
    ]
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — report pipeline preserves synthetic, participant, literature and semantic-exposure boundaries.**"]

    AUDIT_DIR.mkdir(exist_ok=True)
    (AUDIT_DIR / "pathway-report-analysis-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps({
        "reports": len(reports),
        "synthetic": len(synthetic),
        "participant_reports": len(participant_reports),
        "literature_cases": len(literature_cases),
        "errors": len(errors),
    }, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
