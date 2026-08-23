#!/usr/bin/env python3
"""Aggregate structured reports against the Phosphenic Pathway.

Synthetic fixtures are validated but ALWAYS excluded from empirical counts.
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
    synthetic_count = 0
    empirical = []

    for path in report_paths:
        payload = load(path)
        reports.append(payload)
        if payload.get("source_type") == "synthetic_test":
            synthetic_count += 1
        else:
            empirical.append(payload)

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

    stage_occurrence = Counter()
    ordered_transition_counts = Counter()
    report_stage_sequences = []

    # Empirical statistics intentionally exclude synthetic_test reports.
    for report in empirical:
        event_stage_sets = []
        seen_stages = set()
        for event in sorted(report.get("events", []), key=lambda e: e["sequence"]):
            stages = set()
            for ref in event.get("term_refs", []):
                stages.update(term_to_stages.get(ref, set()))
            event_stage_sets.append((event["sequence"], stages))
            seen_stages.update(stages)

        for stage_id in seen_stages:
            stage_occurrence[stage_id] += 1

        # Count order between stages occurring in different event blocks.
        first_seen = {}
        for sequence, stages in event_stage_sets:
            for stage_id in stages:
                first_seen.setdefault(stage_id, sequence)
        ordered = sorted(first_seen.items(), key=lambda kv: kv[1])
        ordered_stage_ids = [stage_id for stage_id, _ in ordered]
        report_stage_sequences.append({"report_id": report["id"], "stage_sequence": ordered_stage_ids})
        for i, source_stage in enumerate(ordered_stage_ids):
            for target_stage in ordered_stage_ids[i + 1:]:
                ordered_transition_counts[(source_stage, target_stage)] += 1

    summary = {
        "metadata": {
            "pathway_id": pathway["id"],
            "pathway_version": pathway["version"],
            "report_files_total": len(reports),
            "synthetic_reports_excluded": synthetic_count,
            "empirical_reports": len(empirical),
            "warning": "Synthetic fixtures are validation-only and never contribute to empirical counts."
        },
        "stage_occurrence": [
            {
                "stage_id": stage_id,
                "stage_label": stage_by_id[stage_id]["label"],
                "report_count": stage_occurrence.get(stage_id, 0)
            }
            for stage_id in stage_by_id
        ],
        "ordered_stage_pairs": [
            {"from": a, "to": b, "report_count": count}
            for (a, b), count in sorted(ordered_transition_counts.items())
        ],
        "report_stage_sequences": report_stage_sequences,
    }

    dump(ANALYSIS_DIR / "phosphenic-pathway-report-summary.json", summary)

    report = [
        "# Phosphenic Pathway report-analysis QA", "",
        f"- Canonical NC IDs available: **{len(canonical_ids)}**",
        f"- Report JSON files discovered: **{len(reports)}**",
        f"- Synthetic fixtures: **{synthetic_count}**",
        f"- Empirical reports included in statistics: **{len(empirical)}**",
        f"- Errors: **{len(errors)}**", "",
        "## Empirical status", "",
    ]
    if not empirical:
        report.append("**No empirical pathway statistics exist yet. All stage and transition counts are correctly zero.**")
    else:
        report.append("Empirical reports are present; see `analysis/phosphenic-pathway-report-summary.json` for counts.")
    report += [
        "", "## Synthetic-data guard", "",
        "Reports with `source_type: synthetic_test` are parsed and reference-checked but excluded before stage occurrence or temporal-order counts are calculated.",
    ]
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — report pipeline preserves the synthetic/empirical boundary.**"]
    AUDIT_DIR.mkdir(exist_ok=True)
    (AUDIT_DIR / "pathway-report-analysis-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps({
        "reports": len(reports),
        "synthetic": synthetic_count,
        "empirical": len(empirical),
        "errors": len(errors)
    }, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
