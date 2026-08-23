#!/usr/bin/env python3
"""Validate external crosswalks without importing their ontology into Nova."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWED = ROOT / "data" / "reviewed" / "v0.4"
CROSSWALKS = ROOT / "crosswalks"
AUDIT = ROOT / "audit"

VALID_RELATIONS = {
    "operationally_similar_to", "partial_overlap", "may_manifest_as",
    "technique_targets", "distinguish_from", "no_direct_equivalent",
}
VALID_STATUS = {"source_explicit", "source_supported", "crosswalk_inference", "rejected_identity"}


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
    for path in sorted(CROSSWALKS.glob("*.json")):
        payload = load(path)
        concept_ids = [c["id"] for c in payload.get("concepts", [])]
        if len(concept_ids) != len(set(concept_ids)):
            errors.append(f"{path.name}: duplicate external concept IDs")
        known_external = set(concept_ids)
        relation_counts = Counter()
        status_counts = Counter()
        for i, mapping in enumerate(payload.get("mappings", [])):
            ext = mapping.get("external_id")
            if ext not in known_external:
                errors.append(f"{path.name}: mapping {i} unknown external concept {ext}")
            relation = mapping.get("relation")
            status = mapping.get("status")
            relation_counts[relation] += 1
            status_counts[status] += 1
            if relation not in VALID_RELATIONS:
                errors.append(f"{path.name}: mapping {i} invalid relation {relation}")
            if status not in VALID_STATUS:
                errors.append(f"{path.name}: mapping {i} invalid status {status}")
            refs = mapping.get("nc_refs", [])
            if relation == "no_direct_equivalent" and refs:
                errors.append(f"{path.name}: no_direct_equivalent mapping {i} must have no NC refs")
            for ref in refs:
                if ref not in canonical_ids:
                    errors.append(f"{path.name}: mapping {i} unknown NC ref {ref}")
            if mapping.get("confidence") is not None and not 0 <= mapping["confidence"] <= 1:
                errors.append(f"{path.name}: mapping {i} confidence out of range")

        stats.append({
            "file": path.name,
            "source_tradition": payload.get("source_tradition"),
            "concepts": len(payload.get("concepts", [])),
            "mappings": len(payload.get("mappings", [])),
            "relations": dict(relation_counts),
            "statuses": dict(status_counts),
        })

    report = [
        "# External crosswalk QA", "",
        f"- Canonical reviewed NC IDs: **{len(canonical_ids)}**",
        f"- Crosswalk files: **{len(stats)}**",
        f"- Errors: **{len(errors)}**", "",
    ]
    for item in stats:
        report += [
            f"## {item['source_tradition']}", "",
            f"- External concepts: **{item['concepts']}**",
            f"- Mappings: **{item['mappings']}**",
            f"- Relations: `{item['relations']}`",
            f"- Statuses: `{item['statuses']}`", "",
        ]
    report += [
        "## Boundary rule", "",
        "Crosswalk mappings never become Nova ontology edges automatically. They remain translation/alignment records between vocabularies.",
    ]
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — external concepts resolve only through explicit crosswalk mappings to canonical NC IDs.**"]
    AUDIT.mkdir(exist_ok=True)
    (AUDIT / "crosswalk-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps({"crosswalks": len(stats), "canonical_ids": len(canonical_ids), "errors": len(errors)}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
