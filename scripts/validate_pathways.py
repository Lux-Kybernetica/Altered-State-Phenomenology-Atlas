#!/usr/bin/env python3
"""Validate experiential pathway files against canonical reviewed NC term IDs."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWED = ROOT / "data" / "reviewed" / "v0.4"
PATHWAYS = ROOT / "pathways"
AUDIT = ROOT / "audit"

VALID_STATUS = {"experimental_proposal", "observational_model", "validated_internal", "deprecated"}
VALID_ROLES = {"entry", "development", "threshold", "marker_set", "regulation", "transition", "outcome", "integration"}
VALID_KINDS = {"proposed_precedes", "observed_precedes", "optional_branch", "may_facilitate", "may_cooccur"}
VALID_EVIDENCE = {"nova_source_explicit", "nova_source_supported", "lux_working_observation", "lux_hypothesis", "external_evidence_pending"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    canonical_ids = set()
    for path in REVIEWED.glob("*.json"):
        if path.name == "vocabularies.json":
            continue
        payload = load(path)
        if "annotation_lux_v0_4" in payload:
            canonical_ids.add(payload["id"])

    errors = []
    stats = []
    for path in sorted(PATHWAYS.glob("*.json")):
        payload = load(path)
        local_errors = []
        if payload.get("status") not in VALID_STATUS:
            local_errors.append(f"invalid status {payload.get('status')!r}")

        stages = payload.get("stages", [])
        stage_ids = [s.get("id") for s in stages]
        if len(stage_ids) != len(set(stage_ids)):
            local_errors.append("duplicate stage IDs")
        known_stages = set(stage_ids)
        for stage in stages:
            if stage.get("role") not in VALID_ROLES:
                local_errors.append(f"stage {stage.get('id')}: invalid role {stage.get('role')!r}")
            for ref in stage.get("term_refs", []):
                if ref not in canonical_ids:
                    local_errors.append(f"stage {stage.get('id')}: unknown NC term ref {ref}")

        transitions = payload.get("transitions", [])
        for i, transition in enumerate(transitions):
            if transition.get("from") not in known_stages:
                local_errors.append(f"transition {i}: unknown from-stage {transition.get('from')}")
            if transition.get("to") not in known_stages:
                local_errors.append(f"transition {i}: unknown to-stage {transition.get('to')}")
            if transition.get("kind") not in VALID_KINDS:
                local_errors.append(f"transition {i}: invalid kind {transition.get('kind')!r}")
            if transition.get("evidence_status") not in VALID_EVIDENCE:
                local_errors.append(f"transition {i}: invalid evidence status {transition.get('evidence_status')!r}")

        errors.extend([f"{path.name}: {e}" for e in local_errors])
        stats.append({
            "file": path.name,
            "id": payload.get("id"),
            "status": payload.get("status"),
            "stages": len(stages),
            "transitions": len(transitions),
            "errors": len(local_errors),
        })

    report = [
        "# Pathway QA", "",
        f"- Canonical reviewed NC term IDs: **{len(canonical_ids)}**",
        f"- Pathway files: **{len(stats)}**",
        f"- Errors: **{len(errors)}**", "",
        "## Pathways", "",
    ]
    for item in stats:
        report.append(f"- `{item['id']}` — {item['stages']} stages, {item['transitions']} transitions, status `{item['status']}`, errors {item['errors']}")
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — all pathway references and transition endpoints are internally valid.**"]
    AUDIT.mkdir(exist_ok=True)
    (AUDIT / "pathway-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"pathways": len(stats), "canonical_ids": len(canonical_ids), "errors": len(errors)}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
