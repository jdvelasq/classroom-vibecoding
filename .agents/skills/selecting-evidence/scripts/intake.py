"""Lists the documents in 01-evidence/ingest/ that still need a selection decision.

Usage (from the repository root):

    python3 .agents/skills/selecting-evidence/scripts/intake.py

Prints a JSON manifest. Exact copies (same SHA-256) of a document in
00-regulations/ or of an indexed document leave the inbox for
01-evidence/rejected/duplicates/ and are reported under "regulations" or
"duplicates"; they are not judged or indexed again.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from evidence_lib import ROOT, Layout, md_header, read_index, sha256, source_of


def move_duplicate(layout: Layout, pdf: Path) -> Path:
    target_dir = layout.rejected / "duplicates"
    target_dir.mkdir(parents=True, exist_ok=True)
    md = pdf.with_suffix(".md")
    if md.exists():
        shutil.move(str(md), str(target_dir / md.name))
    target = target_dir / pdf.name
    shutil.move(str(pdf), str(target))
    return target


def intake(layout: Layout) -> dict[str, list[dict]]:
    by_sha = {row["sha256"]: row for row in read_index(layout)}
    # Regulations frame the design process itself; they are never evidence.
    regulations = {sha256(p): p for p in layout.regulations.rglob("*.pdf")} if layout.regulations.exists() else {}
    pending, duplicates, regulatory = [], [], []
    seen_in_batch: dict[str, str] = {}
    for pdf in sorted(layout.ingest.rglob("*.pdf")):
        if any(part.startswith(".") for part in pdf.relative_to(layout.ingest).parts):
            continue
        digest = sha256(pdf)
        if digest in regulations:
            moved = move_duplicate(layout, pdf)
            regulatory.append({"file": layout.shown(moved), "regulation": layout.shown(regulations[digest])})
            continue
        if digest in by_sha:
            original = by_sha[digest]
            moved = move_duplicate(layout, pdf)
            duplicates.append(
                {
                    "file": layout.shown(moved),
                    "duplicate_of": original["id"],
                    "indexed_file": original["file"],
                    "decision": original["decision"],
                }
            )
            continue
        if digest in seen_in_batch:
            moved = move_duplicate(layout, pdf)
            duplicates.append({"file": layout.shown(moved), "duplicate_of_pending": seen_in_batch[digest]})
            continue
        seen_in_batch[digest] = layout.shown(pdf)
        md = pdf.with_suffix(".md")
        header = md_header(md) if md.exists() else {}
        pending.append(
            {
                "pdf": layout.shown(pdf),
                "md": layout.shown(md) if md.exists() else None,
                "sha256": digest,
                "source": source_of(layout, pdf),
                "pages": header.get("pages"),
                "min_text_coverage": header.get("min_text_coverage"),
                "conversion_warnings": header.get("warnings", []),
            }
        )
    return {"pending": pending, "duplicates": duplicates, "regulations": regulatory}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=ROOT, help="repository root")
    args = ap.parse_args()
    layout = Layout(args.root.resolve())
    json.dump(intake(layout), sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
