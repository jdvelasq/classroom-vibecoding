"""Records accepted documents as mapped in 02-competencies/mapped.csv.

Usage (from the repository root):

    python3 .agents/skills/mapping-competencies/scripts/record.py E0001 E0003

Run it only after validate.py passes. A document that adds nothing to the
map is recorded too, with an empty competency list, so it is not read again
until the format or the domain changes.
"""

from __future__ import annotations

import argparse

from competency_lib import (
    ROOT,
    Layout,
    accepted,
    cited_ids,
    document_version,
    load_map,
    read_index,
    read_ledger,
    require_supported_format,
    today,
    write_ledger,
)


def record(layout: Layout, ids: list[str]) -> dict[str, dict[str, str]]:
    format_version = require_supported_format(layout)
    domain_version = document_version(layout.domain)
    index = read_index(layout)
    rejected = [i for i in ids if not accepted(index, i)]
    if rejected:
        raise SystemExit(f"Not accepted in index.csv: {', '.join(rejected)}")
    competencies = load_map(layout)
    ledger = read_ledger(layout)
    for evidence_id in ids:
        citing = sorted(c.id for c in competencies if evidence_id in cited_ids(c))
        ledger[evidence_id] = {
            "id": evidence_id,
            "format_version": format_version,
            "domain_version": domain_version,
            "date": today(),
            "competencias": ";".join(citing),
        }
    write_ledger(layout, ledger)
    return {i: ledger[i] for i in ids}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="+")
    args = parser.parse_args()
    for evidence_id, row in record(Layout(ROOT), args.ids).items():
        print(f"{evidence_id}: {row['competencias'] or '(no competency)'}")


if __name__ == "__main__":
    main()
