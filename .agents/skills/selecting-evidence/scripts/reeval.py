"""Finds decisions made under an earlier domain.md and returns them to the inbox.

Usage (from the repository root):

    python3 .agents/skills/selecting-evidence/scripts/reeval.py
    python3 .agents/skills/selecting-evidence/scripts/reeval.py --restore E0002 [E0007 ...]

Without arguments, prints a JSON list of the decisions whose domain_version
differs from the current domain.md, split into documents rejected for
pertinence and accepted documents. Whether the domain widened or narrowed
is a judgment, so this script does not choose which ones to restore.

With --restore, moves each document back to the inbox (its PDF and .md),
removes it from index.csv and moves its decision file to
decisions/superseded/. The next selection run judges it again and links the
new decision through `reevaluates`.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

from evidence_lib import (
    AGENT_INBOX,
    ROOT,
    Layout,
    domain_version,
    read_decision,
    read_index,
    write_index,
)


def outdated(layout: Layout) -> dict[str, object]:
    current = domain_version(layout)
    rejected, accepted = [], []
    for path in sorted(layout.decisions.glob("E*.yaml")):
        record = read_decision(path)
        # Normative documents were excluded by david's decision, not by the domain.
        if record.get("domain_version") == current or record.get("excluded_as"):
            continue
        pertinencia = re.search(r"^  pertinencia: (\S+)$", path.read_text(encoding="utf-8"), re.M)
        entry = {
            "id": record["id"],
            "title": record["title"],
            "decision": record["decision"],
            "domain_version": record.get("domain_version"),
            "file": record["file"],
            "file_present": (layout.root / str(record["file"])).exists(),
        }
        if record["decision"] == "accept":
            accepted.append(entry)
        elif record["decision"] == "reject" and pertinencia and pertinencia.group(1) == "0":
            rejected.append(entry)
    return {
        "domain_version": current,
        "rejected_for_pertinence": rejected,
        "accepted": accepted,
    }


def restore(layout: Layout, doc_id: str) -> Path:
    decision_file = layout.decisions / f"{doc_id}.yaml"
    if not decision_file.exists():
        raise SystemExit(f"No decision {doc_id}")
    record = read_decision(decision_file)
    pdf = layout.root / str(record["file"])
    if not pdf.exists():
        raise SystemExit(f"{doc_id}: {record['file']} not found")
    inbox = layout.ingest / AGENT_INBOX if record["source"] == "agent" else layout.ingest
    inbox.mkdir(parents=True, exist_ok=True)
    target_pdf = inbox / pdf.name
    if record.get("md"):
        md = layout.root / str(record["md"])
        if md.exists():
            text = re.sub(
                r'^source: ".*"$',
                f'source: "{layout.shown(target_pdf)}"',
                md.read_text(encoding="utf-8"),
                count=1,
                flags=re.M,
            )
            (inbox / md.name).write_text(text, encoding="utf-8")
            md.unlink()
    shutil.move(str(pdf), str(target_pdf))

    write_index(layout, [r for r in read_index(layout) if r["id"] != doc_id])
    superseded = layout.decisions / "superseded"
    superseded.mkdir(parents=True, exist_ok=True)
    shutil.move(str(decision_file), str(superseded / decision_file.name))
    return target_pdf


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--restore", nargs="+", metavar="ID", default=[])
    ap.add_argument("--root", type=Path, default=ROOT, help="repository root")
    args = ap.parse_args()
    layout = Layout(args.root.resolve())
    if args.restore:
        for doc_id in args.restore:
            print(f"{doc_id} -> {layout.shown(restore(layout, doc_id))}")
        return 0
    json.dump(outdated(layout), sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
