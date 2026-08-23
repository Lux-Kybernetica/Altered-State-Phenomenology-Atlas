#!/usr/bin/env python3
"""Build and QA the first reviewed NC × Lux semantic graph.

Inputs are the preserved Nova source layer, reviewed v0.4 annotations, and the
manually accepted v0.5 typed-edge passes. Pathways are intentionally excluded.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict, deque
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "source"
REVIEWED_DIR = ROOT / "data" / "reviewed" / "v0.4"
V05_DIR = ROOT / "data" / "v0.5"
GRAPH_DIR = ROOT / "graph" / "v0.5"
AUDIT_DIR = ROOT / "audit"

SOURCE_FILES = [
    "terms-etats.json", "terms-transitions.json", "terms-phenomenes.json",
    "terms-actions.json", "terms-obstacles.json", "terms-securite.json",
]
EDGE_FILES = [
    "typed-edges-reviewed-pass1.json",
    "typed-edges-reviewed-pass2.json",
]
SYMMETRIC = {"associated_with", "co_occurs_with", "distinguish_from"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def components(node_ids: set[str], edges: list[dict]) -> list[set[str]]:
    adjacency = defaultdict(set)
    for edge in edges:
        a, b = edge["source"], edge["target"]
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = set()
    result = []
    for start in sorted(node_ids):
        if start in seen:
            continue
        comp = set([start])
        queue = deque([start])
        seen.add(start)
        while queue:
            cur = queue.popleft()
            for nxt in adjacency[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    comp.add(nxt)
                    queue.append(nxt)
        result.append(comp)
    return sorted(result, key=lambda c: (-len(c), sorted(c)))


def main() -> int:
    errors = []

    source_terms = []
    for filename in SOURCE_FILES:
        source_terms.extend(load(SOURCE_DIR / filename)["terms"])
    source_by_name = {t["terme"]: t for t in source_terms}

    annotations = {}
    for path in REVIEWED_DIR.glob("*.json"):
        if path.name == "vocabularies.json":
            continue
        payload = load(path)
        if "annotation_lux_v0_4" in payload:
            annotations[payload["term"]] = payload

    if len(source_terms) != 92:
        errors.append(f"Expected 92 source terms, got {len(source_terms)}")
    if len(annotations) != 92:
        errors.append(f"Expected 92 reviewed annotations, got {len(annotations)}")

    nodes = []
    for source in sorted(source_terms, key=lambda t: int(t["id"][1:])):
        term = source["terme"]
        ann_record = annotations.get(term)
        if not ann_record:
            errors.append(f"Missing reviewed annotation for {term}")
            continue
        semantic = dict(ann_record["annotation_lux_v0_4"])
        for optional in ["cognitive_dimensions", "action_functions", "motor_states"]:
            semantic.setdefault(optional, [])
        nodes.append({
            "id": ann_record["id"],
            "source_id": source["id"],
            "term": term,
            "family": source["famille"],
            "family_label": source.get("famille_label"),
            "source_category": source.get("categorie"),
            "types": semantic.get("types", []),
            "modalities": semantic.get("modalities", []),
            "phases": semantic.get("phases", []),
            "selfhood_dimensions": semantic.get("selfhood_dimensions", []),
            "cognitive_dimensions": semantic.get("cognitive_dimensions", []),
            "action_functions": semantic.get("action_functions", []),
            "motor_states": semantic.get("motor_states", []),
        })

    node_ids = {n["id"] for n in nodes}
    node_by_id = {n["id"]: n for n in nodes}

    edges = []
    for filename in EDGE_FILES:
        payload = load(V05_DIR / filename)
        edges.extend(payload["edges"])

    vocab = load(REVIEWED_DIR / "vocabularies.json")
    allowed_relations = set(vocab["relation_types"])
    allowed_status = {"source_explicit", "source_supported", "proposed"}

    triples = set()
    pair_set = set()
    for i, edge in enumerate(edges):
        source, target = edge["source"], edge["target"]
        rel = edge["relation_type"]
        status = edge["epistemic_status"]
        if source not in node_ids:
            errors.append(f"Edge {i}: missing source node {source}")
        if target not in node_ids:
            errors.append(f"Edge {i}: missing target node {target}")
        if source == target:
            errors.append(f"Edge {i}: self loop {source}")
        if rel not in allowed_relations:
            errors.append(f"Edge {i}: invalid relation {rel}")
        if status not in allowed_status:
            errors.append(f"Edge {i}: invalid epistemic status {status}")
        key = (source, target, rel)
        if key in triples:
            errors.append(f"Duplicate edge triple: {key}")
        triples.add(key)
        pair_set.add(tuple(sorted((source, target))))
        if rel in SYMMETRIC and target < source:
            errors.append(f"Symmetric edge not canonicalized: {source} {rel} {target}")

    no_edge = load(V05_DIR / "resonance-no-semantic-edge.json")["decisions"]
    rejected_pairs = {tuple(sorted(d["pair"])) for d in no_edge}
    if len(pair_set) != 92:
        errors.append(f"Expected 92 accepted semantic pairs, got {len(pair_set)}")
    if len(rejected_pairs) != 5:
        errors.append(f"Expected 5 rejected lexical pairs, got {len(rejected_pairs)}")
    if pair_set & rejected_pairs:
        errors.append("A pair is both accepted and explicitly rejected")
    if len(pair_set | rejected_pairs) != 97:
        errors.append(f"Accepted + rejected pair coverage should equal 97; got {len(pair_set | rejected_pairs)}")

    comps = components(node_ids, edges)
    degrees = Counter()
    for edge in edges:
        degrees[edge["source"]] += 1
        degrees[edge["target"]] += 1
    isolates = [node_by_id[next(iter(c))]["term"] for c in comps if len(c) == 1]
    hubs = sorted(degrees.items(), key=lambda kv: (-kv[1], node_by_id[kv[0]]["term"]))[:15]

    GRAPH_DIR.mkdir(parents=True, exist_ok=True)
    dump(GRAPH_DIR / "nodes.json", nodes)
    dump(GRAPH_DIR / "edges.json", edges)

    # GraphML without external dependencies.
    graphml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">',
        '  <key id="label" for="node" attr.name="label" attr.type="string"/>',
        '  <key id="family" for="node" attr.name="family" attr.type="string"/>',
        '  <key id="relation" for="edge" attr.name="relation" attr.type="string"/>',
        '  <key id="epistemic" for="edge" attr.name="epistemic_status" attr.type="string"/>',
        '  <graph id="NC-Lux-v0.5" edgedefault="directed">',
    ]
    for node in nodes:
        graphml += [
            f'    <node id="{escape(node["id"])}">',
            f'      <data key="label">{escape(node["term"])}</data>',
            f'      <data key="family">{escape(node["family"])}</data>',
            '    </node>',
        ]
    for i, edge in enumerate(edges):
        graphml += [
            f'    <edge id="e{i}" source="{escape(edge["source"])}" target="{escape(edge["target"])}">',
            f'      <data key="relation">{escape(edge["relation_type"])}</data>',
            f'      <data key="epistemic">{escape(edge["epistemic_status"])}</data>',
            '    </edge>',
        ]
    graphml += ['  </graph>', '</graphml>']
    (GRAPH_DIR / "graph.graphml").write_text("\n".join(graphml) + "\n", encoding="utf-8")

    relation_counts = Counter(e["relation_type"] for e in edges)
    epistemic_counts = Counter(e["epistemic_status"] for e in edges)
    report = [
        "# NC × Lux v0.5 — Graph QA", "",
        f"- Nodes: **{len(nodes)}**",
        f"- Typed edges: **{len(edges)}**",
        f"- Accepted semantic pairs: **{len(pair_set)}**",
        f"- Explicit no-edge lexical pairs: **{len(rejected_pairs)}**",
        f"- Original resonance-pair coverage: **{len(pair_set | rejected_pairs)} / 97**",
        f"- Connected components (undirected projection): **{len(comps)}**",
        f"- Largest component: **{len(comps[0]) if comps else 0} nodes**",
        f"- Isolated nodes: **{len(isolates)}**",
        f"- Errors: **{len(errors)}**", "",
        "## Relation distribution", "",
    ]
    report += [f"- `{k}`: {v}" for k, v in sorted(relation_counts.items())]
    report += ["", "## Epistemic distribution", ""]
    report += [f"- `{k}`: {v}" for k, v in sorted(epistemic_counts.items())]
    report += ["", "## Highest-degree concepts", ""]
    for node_id, degree in hubs:
        report.append(f"- **{node_by_id[node_id]['term']}**: {degree}")
    report += ["", "## Isolated concepts", ""]
    report += [f"- {name}" for name in sorted(isolates)]
    report += [
        "", "## Interpretation", "",
        "Isolation is not automatically an ontology defect. At this stage, edges are derived only from reviewed Nova v1 lexical-resonance pairs. A concept with no original accepted relation remains isolated rather than receiving an invented connector.",
        "", "## Pathway boundary", "",
        "No Phosphenic Pathway edge is included in this graph. Pathway sequence data remains a separate layer.",
    ]
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — graph structure and resonance-decision coverage are internally consistent.**"]
    (AUDIT_DIR / "v0.5-graph-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps({
        "nodes": len(nodes), "edges": len(edges), "accepted_pairs": len(pair_set),
        "rejected_pairs": len(rejected_pairs), "components": len(comps),
        "largest_component": len(comps[0]) if comps else 0,
        "isolates": len(isolates), "errors": len(errors),
    }, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
