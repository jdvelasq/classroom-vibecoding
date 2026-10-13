"""Prints, as JSON, what the model needs before mapping competencies.

Usage (from the repository root):

    python3 .agents/skills/mapping-competencies/scripts/status.py

It reports the format and domain versions, the accepted documents not yet
mapped (or mapped under an older format or domain), the next free
competency id, and a one-line summary of every competency so new evidence
can be matched against the existing map.
"""

from __future__ import annotations

import json

from competency_lib import (
    ROOT,
    Layout,
    document_version,
    load_map,
    next_id,
    read_index,
    read_ledger,
    require_supported_format,
)


def status(layout: Layout) -> dict[str, object]:
    format_version = require_supported_format(layout)
    domain_version = document_version(layout.domain)
    index = read_index(layout)
    ledger = read_ledger(layout)
    pending, outdated = [], []
    for evidence_id, row in index.items():
        if row["decision"] != "accept":
            continue
        entry = {
            "id": evidence_id,
            "title": row["title"],
            "issuer": row["issuer"],
            "category": row["category"],
            "role": row["role"],
            "text": layout.evidence_text(row),
            "pdf": row["file"],
        }
        if not (layout.root / entry["text"]).exists():
            # Some accepted documents have no usable conversion; the model
            # then reads the PDF or reports that it could not.
            entry["text"] = None
        mapped = ledger.get(evidence_id)
        if mapped is None:
            pending.append(entry)
        elif (mapped["format_version"], mapped["domain_version"]) != (format_version, domain_version):
            outdated.append(dict(entry, mapped_under=f"format {mapped['format_version']}, domain {mapped['domain_version']}"))
    competencies = [
        {
            "id": c.id,
            "estado": c.header.get("estado"),
            "subcampos": c.header.get("subcampos"),
            "enunciado": c.header.get("enunciado"),
        }
        for c in load_map(layout)
    ]
    return {
        "format_version": format_version,
        "domain_version": domain_version,
        "next_id": next_id(layout),
        "pending": pending,
        "outdated": outdated,
        "map": competencies,
    }


if __name__ == "__main__":
    print(json.dumps(status(Layout(ROOT)), ensure_ascii=False, indent=2))
