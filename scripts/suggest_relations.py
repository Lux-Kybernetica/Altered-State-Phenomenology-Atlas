#!/usr/bin/env python3
"""Generate conservative semantic candidates from Nova v1 lexical resonances.

Important: output is a REVIEW QUEUE, not accepted graph edges.
The script intentionally prefers 'undetermined' over false precision.
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "source"
OUT_DIR = ROOT / "data" / "v0.5"
AUDIT_DIR = ROOT / "audit"
SOURCE_FILES = [
    "terms-etats.json", "terms-transitions.json", "terms-phenomenes.json",
    "terms-actions.json", "terms-obstacles.json", "terms-securite.json",
]
FIELDS = ["definition", "signes", "confusions", "equivalents"]


def norm(text: str) -> str:
    text = (text or "").lower()
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", norm(text)).strip("_")


def strip_parenthetical(text: str) -> str:
    previous = None
    while previous != text:
        previous = text
        text = re.sub(r"\([^()]*\)", "", text)
    return text


def mentions(source: dict, target_name: str) -> list[dict]:
    target = norm(target_name)
    found = []
    for field in FIELDS:
        text = source.get(field, "") or ""
        if target in norm(text):
            found.append({"field": field, "text": text})
    return found


def direct_confusion(source: dict, target_name: str) -> bool:
    # Parenthetical explanations can mention many unrelated terms. Only the
    # outer confusion labels are treated as direct distinction evidence.
    return norm(target_name) in norm(strip_parenthetical(source.get("confusions", "") or ""))


def main() -> int:
    terms = []
    for filename in SOURCE_FILES:
        terms.extend(json.loads((SOURCE_DIR / filename).read_text(encoding="utf-8"))["terms"])
    by_name = {t["terme"]: t for t in terms}

    pairs = set()
    unresolved = []
    for term in terms:
        for target in term.get("relations", []):
            if target not in by_name:
                unresolved.append((term["terme"], target))
                continue
            if target != term["terme"]:
                pairs.add(tuple(sorted((term["terme"], target))))

    candidates = []
    for left_name, right_name in sorted(pairs):
        left, right = by_name[left_name], by_name[right_name]
        left_to_right = mentions(left, right_name)
        right_to_left = mentions(right, left_name)

        left_id = f"nova.{slug(left_name)}"
        right_id = f"nova.{slug(right_name)}"
        source_id, target_id = left_id, right_id
        source_term, target_term = left_name, right_name
        relation = "associated_with"
        direction = "undirected"
        epistemic = "undetermined"
        confidence = 0.30
        rationale = "Lexical resonance only; semantic relation requires human review."

        if direct_confusion(left, right_name) or direct_confusion(right, left_name):
            relation = "distinguish_from"
            epistemic = "source_explicit"
            confidence = 0.95
            rationale = "One term is directly named as a confusion/distinction target in Nova source wording."
        else:
            found = False
            for source, target, evidence, sid, tid, sterm, tterm in [
                (left, right, left_to_right, left_id, right_id, left_name, right_name),
                (right, left, right_to_left, right_id, left_id, right_name, left_name),
            ]:
                target_norm = norm(target["terme"])
                for item in evidence:
                    if item["field"] not in {"definition", "signes"}:
                        continue
                    text = norm(item["text"])
                    target_pos = text.find(target_norm)
                    if target_pos < 0:
                        continue
                    before = text[:target_pos][-100:]
                    if re.search(r"preced\w*\s+(?:souvent\s+)?(?:le|la|l['’]|les)?\s*$", before):
                        relation, direction, epistemic, confidence = "precedes", "directed", "source_supported", 0.90
                        source_id, target_id, source_term, target_term = sid, tid, sterm, tterm
                        rationale = "Nova wording directly places the current term before the target."
                        found = True
                        break
                    if re.search(r"(facilit\w*|aide\w*)\s+(?:le|la|l['’]|les)?\s*$", before):
                        relation, direction, epistemic, confidence = "facilitates", "directed", "source_supported", 0.85
                        source_id, target_id, source_term, target_term = sid, tid, sterm, tterm
                        rationale = "Nova wording explicitly describes a facilitating effect toward the target."
                        found = True
                        break
                    if re.search(r"(provoqu\w*|declench\w*)\s+(?:un|une|le|la|l['’]|les)?\s*$", before):
                        relation, direction, epistemic, confidence = "may_trigger", "directed", "source_supported", 0.80
                        source_id, target_id, source_term, target_term = sid, tid, sterm, tterm
                        rationale = "Nova wording explicitly describes a possible triggering relation toward the target."
                        found = True
                        break
                if found:
                    break

            if not found:
                combined = " ".join(item["text"] for item in left_to_right + right_to_left)
                if re.search(r"\bassocie\w*\b|\baccompagn\w*\b", norm(combined)):
                    epistemic = "source_supported"
                    confidence = 0.65
                    rationale = "Nova uses association/co-occurrence wording, but directionality is not safely inferable."

        candidates.append({
            "source": source_id,
            "target": target_id,
            "source_term": source_term,
            "target_term": target_term,
            "original_pair": [left_id, right_id],
            "suggested_relation": relation,
            "suggested_direction": direction,
            "candidate_epistemic_status": epistemic,
            "machine_confidence": confidence,
            "review_status": "machine_suggested",
            "rationale": rationale,
            "evidence": {left_name: left_to_right, right_name: right_to_left},
        })

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "metadata": {
            "title": "NC v1 lexical resonance → machine semantic candidates",
            "version": "0.5-candidate-pass-1",
            "source_pair_count": len(candidates),
            "status": "machine_suggested_not_accepted",
            "warning": "Review candidates are not graph edges. Lexical co-mention remains semantically undetermined until reviewed.",
        },
        "candidates": candidates,
    }
    (OUT_DIR / "relation-candidates-machine.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    relation_counts = Counter(c["suggested_relation"] for c in candidates)
    epistemic_counts = Counter(c["candidate_epistemic_status"] for c in candidates)
    report = [
        "# NC × Lux v0.5 — Machine relation candidate pass 1", "",
        "This pass operates only on Nova v1 source wording and unique lexical resonance pairs.",
        "It does **not** accept edges into the semantic graph.", "",
        f"- Original unique lexical resonance pairs: **{len(candidates)}**",
    ]
    for relation, count in sorted(relation_counts.items()):
        report.append(f"- `{relation}` candidates: **{count}**")
    report += ["", "## Candidate epistemic status", ""]
    for status, count in sorted(epistemic_counts.items()):
        report.append(f"- `{status}`: **{count}**")
    report += [
        "", "## Conservative rule", "",
        "Direct confusion targets are high-confidence distinction candidates.",
        "Generic lexical co-mention is deliberately left unresolved instead of receiving false semantic precision.",
    ]
    if unresolved:
        report += ["", "## Unresolved source targets", ""] + [f"- {a} → {b}" for a, b in unresolved]
    (AUDIT_DIR / "v0.5-relation-candidate-pass1.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    print(json.dumps({
        "pairs": len(candidates),
        "relations": dict(relation_counts),
        "epistemic": dict(epistemic_counts),
        "unresolved": len(unresolved),
    }, ensure_ascii=False, indent=2))
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
