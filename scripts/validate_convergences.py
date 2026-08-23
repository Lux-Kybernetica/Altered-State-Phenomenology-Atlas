#!/usr/bin/env python3
"""Validate cross-tradition convergence analysis against canonical NC and crosswalk mappings."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWED = ROOT / "data" / "reviewed" / "v0.4"
CROSSWALKS = ROOT / "crosswalks"
ANALYSIS = ROOT / "analysis" / "cross-tradition-convergences-v0.1.json"
AUDIT = ROOT / "audit"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors = []

    canonical_ids = set()
    for path in REVIEWED.glob("*.json"):
        if path.name == "vocabularies.json":
            continue
        payload = load(path)
        if "annotation_lux_v0_4" in payload:
            canonical_ids.add(payload["id"])

    external_ids = set()
    mapping_index = defaultdict(list)
    crosswalk_files = set()
    for path in CROSSWALKS.glob("*.json"):
        crosswalk_files.add(f"crosswalks/{path.name}")
        payload = load(path)
        for concept in payload.get("concepts", []):
            external_ids.add(concept["id"])
        for mapping in payload.get("mappings", []):
            for nc_ref in mapping.get("nc_refs", []):
                mapping_index[(mapping["external_id"], nc_ref)].append({
                    "relation": mapping["relation"],
                    "confidence": mapping.get("confidence"),
                    "file": f"crosswalks/{path.name}",
                })

    matrix = load(ANALYSIS)
    if matrix.get("metadata", {}).get("not_truth_vote") is not True:
        errors.append("metadata.not_truth_vote must be true")

    included = set(matrix.get("metadata", {}).get("included_crosswalks", []))
    missing_files = included - crosswalk_files
    if missing_files:
        errors.append(f"matrix lists missing crosswalk files: {sorted(missing_files)}")

    seen_nc = set()
    status_counts = Counter()
    kind_counts = Counter()
    tradition_sets = {}
    for i, cluster in enumerate(matrix.get("clusters", [])):
        nc_ref = cluster.get("nc_ref")
        if nc_ref in seen_nc:
            errors.append(f"duplicate cluster for {nc_ref}")
        seen_nc.add(nc_ref)
        if nc_ref not in canonical_ids:
            errors.append(f"cluster {i}: unknown NC ref {nc_ref}")
        if not cluster.get("shared_minimum_description"):
            errors.append(f"cluster {i}: missing shared_minimum_description")
        if not cluster.get("theoretical_divergence"):
            errors.append(f"cluster {i}: missing theoretical_divergence")
        status_counts[cluster.get("coverage_status")] += 1
        kind_counts[cluster.get("convergence_kind")] += 1
        traditions = set()
        for j, alignment in enumerate(cluster.get("external_alignments", [])):
            ext = alignment.get("external_id")
            traditions.add(alignment.get("tradition"))
            if ext not in external_ids:
                errors.append(f"cluster {i} alignment {j}: unknown external id {ext}")
            key = (ext, nc_ref)
            candidates = mapping_index.get(key, [])
            if not candidates:
                errors.append(f"cluster {i} alignment {j}: no crosswalk mapping {ext} -> {nc_ref}")
                continue
            relation = alignment.get("relation")
            source_file = alignment.get("source_file")
            exact = [c for c in candidates if c["relation"] == relation and c["file"] == source_file]
            if not exact:
                errors.append(f"cluster {i} alignment {j}: relation/source mismatch for {ext} -> {nc_ref}")
            confidence = alignment.get("confidence")
            if confidence is not None and not 0 <= confidence <= 1:
                errors.append(f"cluster {i} alignment {j}: confidence out of range")
        tradition_sets[nc_ref] = traditions
        if cluster.get("coverage_status") == "multi_tradition" and len(traditions) < 2:
            errors.append(f"cluster {i}: multi_tradition but only {len(traditions)} tradition(s)")

    multi = [ref for ref, ts in tradition_sets.items() if len(ts) >= 2]
    report = [
        "# Cross-tradition convergence QA", "",
        f"- Canonical NC IDs: **{len(canonical_ids)}**",
        f"- External concepts available: **{len(external_ids)}**",
        f"- Convergence clusters: **{len(matrix.get('clusters', []))}**",
        f"- Clusters with 2+ external traditions: **{len(multi)}**",
        f"- Errors: **{len(errors)}**", "",
        "## Multi-tradition clusters", "",
    ]
    for ref in multi:
        report.append(f"- `{ref}` — {', '.join(sorted(tradition_sets[ref]))}")
    report += ["", "## Coverage statuses", ""]
    for key, value in sorted(status_counts.items()):
        report.append(f"- `{key}`: {value}")
    report += ["", "## Epistemic guard", "",
               "A convergence cluster is a comparison/research target. It does not become evidence for the external frameworks' shared or competing ontological explanations merely because multiple vocabularies align with the same NC node."]
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — every convergence alignment resolves to an explicit committed crosswalk mapping, and multi-tradition labels are structurally justified.**"]

    AUDIT.mkdir(exist_ok=True)
    (AUDIT / "cross-tradition-convergence-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({
        "clusters": len(matrix.get("clusters", [])),
        "multi_tradition": len(multi),
        "external_ids": len(external_ids),
        "errors": len(errors),
    }, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
