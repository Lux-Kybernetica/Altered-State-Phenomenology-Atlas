#!/usr/bin/env python3
"""Validate the NC × Lux scientific-evidence layer.

The validator is intentionally epistemic as well as structural:
- every NC reference must resolve to a reviewed canonical concept;
- every study must state limitations and what it does *not* establish;
- study IDs must be unique;
- scientific links may contextualize Nova concepts but never silently become
  identity/equivalence assertions.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWED = ROOT / "data" / "reviewed" / "v0.4"
EVIDENCE_DIR = ROOT / "evidence"
AUDIT = ROOT / "audit"

VALID_CLASSES = {
    "primary_experimental", "primary_observational", "case_report",
    "systematic_review", "narrative_review", "methodological_study",
}
VALID_RELATIONS = {
    "experimental_analogue", "mechanistic_context", "clinical_context",
    "phenomenology_context", "measurement_precedent",
    "operationalization_support", "alternative_explanation",
}


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
    files = []
    global_study_ids = set()
    relation_counts = Counter()
    class_counts = Counter()
    linked_nc = Counter()

    for path in sorted(EVIDENCE_DIR.glob("*.json")):
        payload = load(path)
        studies = payload.get("studies", [])
        local_ids = set()
        for index, study in enumerate(studies):
            sid = study.get("id")
            if not sid:
                errors.append(f"{path.name}: study {index} missing id")
                continue
            if sid in local_ids:
                errors.append(f"{path.name}: duplicate local study id {sid}")
            if sid in global_study_ids:
                errors.append(f"{path.name}: duplicate global study id {sid}")
            local_ids.add(sid)
            global_study_ids.add(sid)

            eclass = study.get("evidence_class")
            class_counts[eclass] += 1
            if eclass not in VALID_CLASSES:
                errors.append(f"{path.name}: {sid} invalid evidence_class {eclass}")

            locator = study.get("source_locator", {})
            if not locator.get("doi") and not locator.get("pmid") and not locator.get("pmcid"):
                errors.append(f"{path.name}: {sid} has no stable source locator")

            if not study.get("findings"):
                errors.append(f"{path.name}: {sid} has no findings")
            if not study.get("limitations"):
                errors.append(f"{path.name}: {sid} has no limitations")
            if not study.get("does_not_establish"):
                errors.append(f"{path.name}: {sid} has no does_not_establish boundary")

            for link_index, link in enumerate(study.get("nc_links", [])):
                ref = link.get("nc_ref")
                relation = link.get("relation")
                if ref not in canonical_ids:
                    errors.append(f"{path.name}: {sid} link {link_index} unknown NC ref {ref}")
                if relation not in VALID_RELATIONS:
                    errors.append(f"{path.name}: {sid} link {link_index} invalid relation {relation}")
                if not link.get("basis"):
                    errors.append(f"{path.name}: {sid} link {link_index} missing basis")
                relation_counts[relation] += 1
                linked_nc[ref] += 1

        files.append({"file": path.name, "studies": len(studies)})

    report = [
        "# Scientific evidence QA", "",
        f"- Canonical reviewed NC concepts: **{len(canonical_ids)}**",
        f"- Evidence files: **{len(files)}**",
        f"- Studies: **{len(global_study_ids)}**",
        f"- Distinct NC concepts linked: **{len(linked_nc)}**",
        f"- Errors: **{len(errors)}**", "",
        "## Evidence-class distribution", "",
    ]
    for key, value in sorted(class_counts.items()):
        report.append(f"- `{key}`: **{value}**")
    report += ["", "## Scientific-link roles", ""]
    for key, value in sorted(relation_counts.items()):
        report.append(f"- `{key}`: **{value}**")
    report += ["", "## Most-linked NC concepts", ""]
    for ref, count in linked_nc.most_common(15):
        report.append(f"- `{ref}`: {count}")
    report += [
        "", "## Epistemic boundary", "",
        "A scientific study can be an experimental analogue, mechanism/context, clinical context, measurement precedent or alternative explanation. None of these relations mean `same_as`, and the scientific layer never adjudicates metaphysical interpretations by database convention.",
    ]
    if errors:
        report += ["", "## Errors", ""] + [f"- {error}" for error in errors]
    else:
        report += ["", "## Result", "", "**PASS — scientific records have valid NC targets and explicit inferential boundaries.**"]

    AUDIT.mkdir(exist_ok=True)
    (AUDIT / "scientific-evidence-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({
        "evidence_files": len(files),
        "studies": len(global_study_ids),
        "linked_nc_concepts": len(linked_nc),
        "errors": len(errors),
    }, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
