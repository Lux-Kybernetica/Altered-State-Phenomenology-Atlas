#!/usr/bin/env python3
"""Build the NC × Lux v0.5 normalized dataset and relation-review artifacts.

No external dependencies. The script treats Nova source, Lux annotation, and
relation proposals as separate layers and fails loudly on structural drift.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "source"
REVIEWED_DIR = ROOT / "data" / "reviewed" / "v0.4"
OUT_DIR = ROOT / "data" / "v0.5"
AUDIT_DIR = ROOT / "audit"

SOURCE_FILES = [
    "terms-etats.json", "terms-transitions.json", "terms-phenomenes.json",
    "terms-actions.json", "terms-obstacles.json", "terms-securite.json",
]
AXES = [
    "types", "modalities", "phases", "selfhood_dimensions",
    "cognitive_dimensions", "action_functions", "motor_states",
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ordered_pair(a: str, b: str) -> tuple[str, str]:
    return (a, b) if a < b else (b, a)


def main() -> int:
    errors, warnings = [], []
    vocab = load_json(REVIEWED_DIR / "vocabularies.json")

    source_terms = []
    for filename in SOURCE_FILES:
        source_terms.extend(load_json(SOURCE_DIR / filename)["terms"])
    source_by_name = {t["terme"]: t for t in source_terms}
    source_by_id = {t["id"]: t for t in source_terms}

    if len(source_terms) != 92:
        errors.append(f"Expected 92 source terms, found {len(source_terms)}")
    if len(source_by_name) != len(source_terms):
        errors.append("Duplicate Nova source term names detected")
    if len(source_by_id) != len(source_terms):
        errors.append("Duplicate Nova source IDs detected")
    expected_source_ids = {f"t{i}" for i in range(92)}
    if set(source_by_id) != expected_source_ids:
        errors.append(
            f"Source ID set differs from t0..t91; missing={sorted(expected_source_ids-set(source_by_id))}, "
            f"extra={sorted(set(source_by_id)-expected_source_ids)}"
        )

    annotation_records = []
    annotation_paths = {}
    for path in sorted(REVIEWED_DIR.glob("*.json")):
        if path.name == "vocabularies.json":
            continue
        payload = load_json(path)
        if "annotation_lux_v0_4" not in payload:
            warnings.append(f"Skipped non-annotation JSON: {path.relative_to(ROOT)}")
            continue
        annotation_records.append(payload)
        annotation_paths[payload["term"]] = str(path.relative_to(ROOT)).replace("\\", "/")

    ann_by_name = {a["term"]: a for a in annotation_records}
    ann_by_id = {a["id"]: a for a in annotation_records}
    if len(annotation_records) != 92:
        errors.append(f"Expected 92 reviewed annotations, found {len(annotation_records)}")
    if len(ann_by_name) != len(annotation_records):
        errors.append("Duplicate reviewed annotation term names detected")
    if len(ann_by_id) != len(annotation_records):
        errors.append("Duplicate reviewed canonical IDs detected")

    source_names, annotation_names = set(source_by_name), set(ann_by_name)
    if source_names - annotation_names:
        errors.append(f"Source terms without reviewed annotation: {sorted(source_names-annotation_names)}")
    if annotation_names - source_names:
        errors.append(f"Reviewed annotations without source term: {sorted(annotation_names-source_names)}")

    normalized_annotations = {}
    for name, record in ann_by_name.items():
        ann = dict(record["annotation_lux_v0_4"])
        for axis in AXES:
            ann.setdefault(axis, [])
        ann.setdefault("assertions", [])
        ann.setdefault("notes", [])
        for axis in AXES:
            allowed = set(vocab.get(axis, []))
            for value in ann[axis]:
                if value not in allowed:
                    errors.append(f"{name}: invalid {axis} value {value!r}")
            if len(ann[axis]) != len(set(ann[axis])):
                errors.append(f"{name}: duplicate values in {axis}")
        for i, assertion in enumerate(ann["assertions"]):
            status = assertion.get("epistemic_status")
            if status not in set(vocab["epistemic_status"]):
                errors.append(f"{name}: assertion {i} invalid epistemic status {status!r}")
            if assertion.get("kind") == "relation":
                pred = assertion.get("predicate")
                if pred not in set(vocab["relation_types"]):
                    errors.append(f"{name}: relation assertion {i} invalid predicate {pred!r}")
                target = assertion.get("target_id")
                if target and target not in ann_by_id:
                    errors.append(f"{name}: relation assertion {i} target_id not found: {target}")
        normalized_annotations[name] = ann

    nodes, manifest = [], []
    for source in sorted(source_terms, key=lambda t: int(t["id"][1:])):
        name = source["terme"]
        reviewed = ann_by_name.get(name)
        if not reviewed:
            continue
        ann = normalized_annotations[name]
        nodes.append({
            "source_id": source["id"], "id": reviewed["id"], "term": name,
            "source_family": source["famille"],
            "source_family_label": source.get("famille_label"),
            "source_category": source.get("categorie"),
            "source": {
                "definition": source.get("definition", ""),
                "signs": source.get("signes", ""),
                "confusions": source.get("confusions", ""),
                "equivalents": source.get("equivalents", ""),
                "resonances_original": source.get("relations", []),
            },
            "semantic": ann,
        })
        manifest.append({
            "source_id": source["id"], "id": reviewed["id"], "term": name,
            "family": source["famille"], "review_file": annotation_paths.get(name),
            "review_status": ann.get("review_status"),
            "annotation_method": ann.get("annotation_method"),
        })

    canonical_by_term = {n["term"]: n["id"] for n in nodes}
    resonance_pairs, unresolved = {}, []
    for source in source_terms:
        for target_name in source.get("relations", []):
            if target_name not in canonical_by_term:
                unresolved.append((source["terme"], target_name))
                continue
            a, b = canonical_by_term[source["terme"]], canonical_by_term[target_name]
            if a == b:
                continue
            pair = ordered_pair(a, b)
            resonance_pairs[pair] = {
                "source": pair[0], "target": pair[1],
                "relation_type": "resonance_original", "direction": "undirected",
                "provenance": "nova_v1_lexical_resonance",
                "epistemic_status": "source_derived", "review_required": True,
            }
    if unresolved:
        errors.append(f"Unresolved source resonance targets: {unresolved}")
    source_resonance_edges = sorted(resonance_pairs.values(), key=lambda e: (e["source"], e["target"]))

    typed_seed, seen_typed = [], set()
    for node in nodes:
        for assertion in node["semantic"].get("assertions", []):
            if assertion.get("kind") != "relation":
                continue
            target_id = assertion.get("target_id")
            if not target_id:
                warnings.append(f"{node['term']}: relation assertion without target_id")
                continue
            key = (node["id"], target_id, assertion.get("predicate"), assertion.get("epistemic_status"), assertion.get("basis", ""))
            if key in seen_typed:
                continue
            seen_typed.add(key)
            typed_seed.append({
                "source": node["id"], "target": target_id,
                "relation_type": assertion.get("predicate"),
                "epistemic_status": assertion.get("epistemic_status"),
                "basis": assertion.get("basis", ""),
                "provenance": "lux_reviewed_assertion_v0.4",
                "review_required": assertion.get("epistemic_status") == "proposed",
            })
    typed_seed.sort(key=lambda e: (e["source"], e["target"], e["relation_type"]))

    seed_by_pair = defaultdict(list)
    for edge in typed_seed:
        seed_by_pair[ordered_pair(edge["source"], edge["target"])].append(edge)
    relation_review_queue = []
    for edge in source_resonance_edges:
        pair = ordered_pair(edge["source"], edge["target"])
        relation_review_queue.append({
            "source": edge["source"], "target": edge["target"],
            "original_relation": "resonance_original",
            "typed_seed_coverage": seed_by_pair.get(pair, []),
            "review_status": "seeded" if pair in seed_by_pair else "unreviewed",
        })

    family_counts = Counter(n["source_family"] for n in nodes)
    type_counts = Counter(v for n in nodes for v in n["semantic"]["types"])
    modality_counts = Counter(v for n in nodes for v in n["semantic"]["modalities"])
    phase_counts = Counter(v for n in nodes for v in n["semantic"]["phases"])
    epistemic_counts = Counter(a.get("epistemic_status") for n in nodes for a in n["semantic"].get("assertions", []))

    consolidated = {
        "metadata": {
            "title": "Nova Conscientia v1 × Lux semantic model", "version": "0.5",
            "status": "normalized_from_manual_review_v0.4",
            "source_term_count": len(source_terms), "reviewed_term_count": len(annotation_records),
            "principle": "SOURCE, ANALYSIS and PROPOSAL remain distinct",
        },
        "vocabularies": vocab, "nodes": nodes,
    }

    dump_json(OUT_DIR / "nova-v0.5.json", consolidated)
    dump_json(OUT_DIR / "nodes.json", nodes)
    dump_json(OUT_DIR / "manifest.json", manifest)
    dump_json(OUT_DIR / "resonance-edges-original.json", source_resonance_edges)
    dump_json(OUT_DIR / "typed-edges-seed.json", typed_seed)
    dump_json(OUT_DIR / "relation-review-queue.json", relation_review_queue)

    report = [
        "# NC × Lux v0.5 — QA report", "",
        f"- Source terms: **{len(source_terms)}**",
        f"- Reviewed annotations: **{len(annotation_records)}**",
        f"- Consolidated nodes: **{len(nodes)}**",
        f"- Original Nova resonance pairs: **{len(source_resonance_edges)}**",
        f"- Typed relation seed edges: **{len(typed_seed)}**",
        f"- Relation queue items already seeded: **{sum(q['review_status']=='seeded' for q in relation_review_queue)}**",
        f"- Relation queue items unreviewed: **{sum(q['review_status']=='unreviewed' for q in relation_review_queue)}**",
        f"- Errors: **{len(errors)}**", f"- Warnings: **{len(warnings)}**", "", "## Family counts", "",
    ]
    report += [f"- `{k}`: {v}" for k, v in sorted(family_counts.items())]
    report += ["", "## Type counts", ""] + [f"- `{k}`: {v}" for k, v in sorted(type_counts.items())]
    report += ["", "## Modality counts", ""] + [f"- `{k}`: {v}" for k, v in sorted(modality_counts.items())]
    report += ["", "## Phase counts", ""] + [f"- `{k}`: {v}" for k, v in sorted(phase_counts.items())]
    report += ["", "## Assertion epistemic-status counts", ""] + [f"- `{k}`: {v}" for k, v in sorted(epistemic_counts.items(), key=lambda kv: str(kv[0]))]
    if warnings:
        report += ["", "## Warnings", ""] + [f"- {w}" for w in warnings]
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — v0.5 structural consolidation is internally consistent.**"]
    (AUDIT_DIR / "v0.5-qa-report.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps({
        "nodes": len(nodes), "source_resonance_pairs": len(source_resonance_edges),
        "typed_seed_edges": len(typed_seed),
        "relation_queue_seeded": sum(q["review_status"] == "seeded" for q in relation_review_queue),
        "relation_queue_unreviewed": sum(q["review_status"] == "unreviewed" for q in relation_review_queue),
        "errors": len(errors), "warnings": len(warnings),
    }, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
