"""Applies the selection rule to the model's judgments and files each document.

Usage (from the repository root):

    python3 .agents/skills/selecting-evidence/scripts/apply.py JUDGMENTS.json [--dry-run]

JUDGMENTS.json is a list with one object per document in 01-evidence/ingest/:

    {"pdf": "01-evidence/ingest/x.pdf", "title": "...", "issuer": "...",
     "year": 2024, "scores": {"pertinencia": 2, "autoridad": 2,
     "especificidad": 2, "vigencia": 2, "acceso": 2},
     "material_warnings": false, "category": "authoritative",
     "role": "actual", "rationale": "...", "doubts": null}

The model supplies only judgments. Source, hash, decision, identifiers and
file moves are computed here, so the same judgments always produce the same
result.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

from evidence_lib import (
    CATEGORIES,
    CRITERIA,
    ROLES,
    ROOT,
    SUPPORTED_CRITERIA_VERSION,
    Layout,
    append_index,
    criteria_version,
    decide,
    domain_version,
    next_id,
    normalize,
    read_decision,
    read_index,
    sha256,
    source_of,
    today,
)


def validate(judgment: dict, layout: Layout) -> list[str]:
    errors = []
    pdf = layout.root / judgment.get("pdf", "")
    if not pdf.is_file() or layout.ingest not in pdf.parents:
        errors.append(f"pdf not found in the inbox: {judgment.get('pdf')}")
    for key in ("title", "issuer", "rationale"):
        if not str(judgment.get(key) or "").strip():
            errors.append(f"missing {key}")
    scores = judgment.get("scores", {})
    for name in CRITERIA:
        value = scores.get(name)
        if value not in (0, 1, 2, None):
            errors.append(f"score {name} must be 0, 1, 2 or null")
    for name in ("pertinencia", "acceso"):
        if scores.get(name) is None:
            errors.append(f"score {name} is required")
    if not isinstance(judgment.get("material_warnings"), bool):
        errors.append("material_warnings must be true or false")
    if scores.get("pertinencia"):
        if judgment.get("category") not in CATEGORIES:
            errors.append(f"category must be one of {sorted(CATEGORIES)}")
        if judgment.get("role") not in ROLES:
            errors.append(f"role must be one of {sorted(ROLES)}")
    return errors


def edition_match(judgment: dict, known: list[dict[str, str]]) -> tuple[str, dict] | None:
    """Same title and issuer as an indexed document: same year or new edition."""
    key = (normalize(judgment["title"]), normalize(judgment["issuer"]))
    for row in known:
        if (normalize(row["title"]), normalize(row["issuer"])) != key:
            continue
        same_year = str(row["year"]) == str(judgment.get("year") or "")
        return ("same_edition" if same_year else "new_edition", row)
    return None


def yaml_value(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def write_decision(path: Path, record: dict) -> None:
    lines = []
    for key, value in record.items():
        if isinstance(value, dict):
            lines.append(f"{key}:")
            lines += [f"  {k}: {yaml_value(v)}" for k, v in value.items()]
        elif isinstance(value, list):
            lines.append(f"{key}:" + ("" if value else " []"))
            lines += [f"  - {yaml_value(v)}" for v in value]
        else:
            lines.append(f"{key}: {yaml_value(value)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def move_pair(layout: Layout, pdf: Path, pdf_dir: Path, md_dir: Path) -> tuple[Path, Path | None]:
    pdf_dir.mkdir(parents=True, exist_ok=True)
    target_pdf = pdf_dir / pdf.name
    if target_pdf.exists():
        raise SystemExit(f"Refusing to overwrite {layout.shown(target_pdf)}")
    md = pdf.with_suffix(".md")
    target_md = None
    if md.exists():
        md_dir.mkdir(parents=True, exist_ok=True)
        target_md = md_dir / md.name
        # The converter header must keep pointing at the PDF it was made from.
        text = re.sub(
            r'^source: ".*"$',
            f'source: "{layout.shown(target_pdf)}"',
            md.read_text(encoding="utf-8"),
            count=1,
            flags=re.M,
        )
        target_md.write_text(text, encoding="utf-8")
        md.unlink()
    shutil.move(str(pdf), str(target_pdf))
    return target_pdf, target_md


def apply(layout: Layout, judgments: list[dict], dry_run: bool = False) -> list[dict]:
    version = criteria_version(layout)
    if version != SUPPORTED_CRITERIA_VERSION:
        raise SystemExit(
            f"criteria.md is version {version}; the rule in evidence_lib.decide "
            f"implements {SUPPORTED_CRITERIA_VERSION}. Review it before applying."
        )
    problems = {j.get("pdf"): validate(j, layout) for j in judgments}
    problems = {k: v for k, v in problems.items() if v}
    if problems:
        raise SystemExit("Invalid judgments:\n" + json.dumps(problems, indent=2, ensure_ascii=False))

    domain = domain_version(layout)
    rows = read_index(layout)
    superseded = {
        str(read_decision(p)["sha256"]): p.stem
        for p in sorted((layout.decisions / "superseded").glob("E*.yaml"))
    }
    outcomes = []
    for judgment in judgments:
        pdf = layout.root / judgment["pdf"]
        source = source_of(layout, pdf)
        scores = {c: judgment["scores"].get(c) for c in CRITERIA}
        decision = decide(source, scores)
        notes = []
        if judgment["material_warnings"]:
            notes.append("conversion warnings limit the reading")
        if judgment.get("doubts"):
            notes.append(f"doubts: {judgment['doubts']}")
        previous_edition = duplicate_of = None
        match = edition_match(judgment, rows)
        if match and match[0] == "same_edition":
            decision = "reject"
            duplicate_of = match[1]["id"]
            notes.append(f"same title, issuer and year as {duplicate_of}; rejected as duplicate")
        elif match:
            previous_edition = match[1]["id"]
            notes.append(f"new edition of {previous_edition} ({match[1]['year']})")

        outcome = {
            "pdf": judgment["pdf"],
            "title": judgment["title"],
            "source": source,
            "decision": decision,
            "category": judgment.get("category") if decision == "accept" else None,
            "role": judgment.get("role") if decision == "accept" else None,
            "notes": notes,
        }
        outcomes.append(outcome)
        if dry_run:
            continue

        doc_id = next_id(layout, rows)
        digest = sha256(pdf)
        if decision == "accept":
            category = judgment["category"]
            new_pdf, new_md = move_pair(
                layout, pdf, layout.accepted_pdf_dir(category), layout.accepted_md_dir(category)
            )
        else:
            new_pdf, new_md = move_pair(layout, pdf, layout.rejected, layout.rejected)
        record = {
            "id": doc_id,
            "sha256": digest,
            "file": layout.shown(new_pdf),
            "md": layout.shown(new_md) if new_md else None,
            "title": judgment["title"],
            "issuer": judgment["issuer"],
            "year": judgment.get("year"),
            "source": source,
            "decision": decision,
            "category": outcome["category"],
            "role": outcome["role"],
            "scores": scores,
            "material_warnings": judgment["material_warnings"],
            "doubts": judgment.get("doubts"),
            "previous_edition": previous_edition,
            "duplicate_of": duplicate_of,
            "reevaluates": superseded.get(digest),
            "rationale": judgment["rationale"],
            "criteria_version": version,
            "domain_version": domain,
            "date": today(),
        }
        write_decision(layout.decisions / f"{doc_id}.yaml", record)
        row = {k: "" if record[k] is None else str(record[k]) for k in
               ("id", "sha256", "file", "title", "issuer", "year", "source",
                "decision", "category", "role", "criteria_version", "date")}
        append_index(layout, row)
        rows.append(row)
        outcome["id"] = doc_id
        outcome["file"] = record["file"]
    return outcomes


def report(outcomes: list[dict], dry_run: bool) -> str:
    labels = {"accept": "Accepted", "reject": "Rejected"}
    lines = ["Dry run: nothing was moved." if dry_run else "Selection applied."]
    for decision in ("accept", "reject"):
        group = [o for o in outcomes if o["decision"] == decision]
        if not group:
            continue
        lines.append(f"\n{labels[decision]} ({len(group)}):")
        for o in group:
            detail = f" [{o['category']}, {o['role']}]" if decision == "accept" else ""
            ident = f"{o['id']} " if "id" in o else ""
            lines.append(f"  - {ident}{o['title']}{detail}")
            lines += [f"      {n}" for n in o["notes"]]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("judgments", type=Path)
    ap.add_argument("--dry-run", action="store_true", help="decide without moving files")
    ap.add_argument("--root", type=Path, default=ROOT, help="repository root")
    args = ap.parse_args()
    layout = Layout(args.root.resolve())
    judgments = json.loads(args.judgments.read_text(encoding="utf-8"))
    print(report(apply(layout, judgments, args.dry_run), args.dry_run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
