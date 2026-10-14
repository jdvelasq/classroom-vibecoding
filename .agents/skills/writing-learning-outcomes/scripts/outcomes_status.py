"""Prints, as JSON, what the model needs before writing learning outcomes.

Usage (from the repository root):

    python3 .agents/skills/writing-learning-outcomes/scripts/outcomes_status.py

It reports the format version and limits, every included competency with
its performance evidence and open `Pendientes`, the competencies that do
not enter (candidates and retired), the existing outcomes, which included
competencies no outcome covers yet, and the next free outcome id.
"""

from __future__ import annotations

import json

from outcomes_lib import (
    LEVEL,
    MAX_COMPETENCIES_PER_OUTCOME,
    MAX_OUTCOMES,
    MIN_OUTCOMES,
    ROOT,
    Layout,
    collapse,
    coverage,
    load_competencies,
    load_outcomes,
    next_id,
    require_supported_format,
)


def status(layout: Layout) -> dict[str, object]:
    format_version = require_supported_format(layout)
    competencies = load_competencies(layout)
    outcomes = load_outcomes(layout)
    covered = coverage(outcomes, competencies)
    return {
        "format_version": format_version,
        "level": LEVEL,
        "outcomes_allowed": [MIN_OUTCOMES, MAX_OUTCOMES],
        "max_competencies_per_outcome": MAX_COMPETENCIES_PER_OUTCOME,
        "next_id": next_id(layout),
        "profile_exists": layout.profile.exists(),
        "included": [
            {
                "id": cid,
                "enunciado": competencies[cid].header.get("enunciado"),
                "subcampos": competencies[cid].header.get("subcampos"),
                "evidencia_de_desempeno": competencies[cid].bullets("Evidencia de desempeño"),
                "pendientes": collapse(competencies[cid].sections.get("Pendientes", "")) or None,
                "covered_by": outcome_ids,
            }
            for cid, outcome_ids in covered.items()
        ],
        "excluded": [
            {"id": cid, "estado": c.header.get("estado"), "enunciado": c.header.get("enunciado")}
            for cid, c in competencies.items()
            if cid not in covered
        ],
        "outcomes": [
            {"id": o.id, "enunciado": o.header.get("enunciado"), "competencias": o.header.get("competencias")}
            for o in outcomes
        ],
        "uncovered": [cid for cid, outcome_ids in covered.items() if not outcome_ids],
    }


if __name__ == "__main__":
    print(json.dumps(status(Layout(ROOT)), ensure_ascii=False, indent=2))
