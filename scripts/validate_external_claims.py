#!/usr/bin/env python3
"""Validate external-source claim records and their import boundaries."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
CROSSWALKS = ROOT / "crosswalks"
AUDIT = ROOT / "audit"

VALID_TYPES = {
    "program_definition", "procedural_instruction", "participant_report_generalization",
    "interpretive_claim", "metaphysical_claim",
}
VALID_IMPORT = {"crosswalk_eligible", "context_only", "do_not_import_as_fact"}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors = []
    stats = []

    external_ids = set()
    for path in CROSSWALKS.glob("*.json"):
        payload = load(path)
        external_ids.update(c.get("id") for c in payload.get("concepts", []))

    for path in sorted(SOURCES.glob("*.json")):
        payload = load(path)
        claims = payload.get("claims", [])
        seen = set()
        types = Counter()
        policies = Counter()
        for i, claim in enumerate(claims):
            cid = claim.get("id")
            if cid in seen:
                errors.append(f"{path.name}: duplicate claim id {cid}")
            seen.add(cid)
            ctype = claim.get("claim_type")
            policy = claim.get("import_policy")
            subject = claim.get("subject_id")
            types[ctype] += 1
            policies[policy] += 1
            if ctype not in VALID_TYPES:
                errors.append(f"{path.name}: claim {i} invalid type {ctype}")
            if policy not in VALID_IMPORT:
                errors.append(f"{path.name}: claim {i} invalid import policy {policy}")
            if subject not in external_ids:
                errors.append(f"{path.name}: claim {i} unknown external subject {subject}")
            if ctype == "metaphysical_claim" and policy == "crosswalk_eligible":
                errors.append(f"{path.name}: metaphysical claim {cid} cannot be crosswalk_eligible")
            if ctype == "interpretive_claim" and policy == "crosswalk_eligible":
                errors.append(f"{path.name}: interpretive claim {cid} requires context_only/do_not_import_as_fact")
            if not claim.get("source_basis"):
                errors.append(f"{path.name}: claim {cid} has no source basis")

        stats.append({
            "file": path.name,
            "source_tradition": payload.get("source_tradition"),
            "claims": len(claims),
            "types": dict(types),
            "import_policies": dict(policies),
        })

    report = [
        "# External source-claim QA", "",
        f"- External concept IDs available from crosswalks: **{len(external_ids)}**",
        f"- Source-claim files: **{len(stats)}**",
        f"- Errors: **{len(errors)}**", "",
    ]
    for item in stats:
        report += [
            f"## {item['source_tradition']}", "",
            f"- Claims: **{item['claims']}**",
            f"- Claim types: `{item['types']}`",
            f"- Import policies: `{item['import_policies']}`", "",
        ]
    report += [
        "## Boundary rule", "",
        "`metaphysical_claim` and `interpretive_claim` records cannot be used as direct crosswalk evidence by this validator. They remain source-context records unless a separate evidence layer supports them independently.",
    ]
    if errors:
        report += ["", "## Errors", ""] + [f"- {e}" for e in errors]
    else:
        report += ["", "## Result", "", "**PASS — external claim types and import boundaries are internally coherent.**"]

    AUDIT.mkdir(exist_ok=True)
    (AUDIT / "external-source-claims-qa.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps({"files": len(stats), "external_ids": len(external_ids), "errors": len(errors)}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
