"""Prints, as JSON, what the model needs before proposing the curriculum.

Usage (from the repository root):

    python3 .agents/skills/mapping-curriculum/scripts/curriculum_status.py

It reports the format version and limits, the courses of courses.md, every
learning outcome with the subfields of its competencies and the cells it
already has in the matrix, the outcomes that never reach mastery, the
postgraduate courses without outcomes, the included competencies available
to the undergraduate courses, and the undergraduate outcomes already
written.
"""

from __future__ import annotations

import json

from curriculum_lib import (
    INCLUDED,
    LEVELS,
    MASTER,
    MAX_COMPETENCIES_PER_COURSE_OUTCOME,
    MAX_COURSE_OUTCOMES,
    MIN_COURSE_OUTCOMES,
    ROOT,
    Layout,
    load_competencies,
    load_courses,
    load_outcomes,
    load_undergraduate,
    parse_course_outcomes,
    postgraduate,
    read_matrix,
    require_supported_format,
    subfields_of,
    undergraduate,
)


def status(layout: Layout) -> dict[str, object]:
    format_version = require_supported_format(layout)
    _, courses = load_courses(layout)
    competencies = load_competencies(layout)
    outcomes = load_outcomes(layout)
    rows, matrix_errors = read_matrix(layout)
    written = load_undergraduate(layout)
    graduate = [c.folder for c in postgraduate(courses)]
    return {
        "format_version": format_version,
        "levels": list(LEVELS),
        "undergraduate_outcomes_allowed": [MIN_COURSE_OUTCOMES, MAX_COURSE_OUTCOMES],
        "max_competencies_per_course_outcome": MAX_COMPETENCIES_PER_COURSE_OUTCOME,
        "courses": [
            {"folder": c.folder, "name": c.name, "level": c.level, "status": c.status, "subfields": list(c.subfields)}
            for c in courses
        ],
        "postgraduate_order": graduate,
        "matrix_exists": layout.matrix.exists(),
        "matrix_errors": matrix_errors,
        "outcomes": [
            {
                "id": rid,
                "enunciado": outcome.header.get("enunciado"),
                "competencias": outcome.header.get("competencias"),
                "subfields": sorted(subfields_of(outcome, competencies)),
                "cells": {r.curso: r.nivel for r in rows if r.ra == rid},
            }
            for rid, outcome in outcomes.items()
        ],
        "not_mastered": [rid for rid in outcomes if not any(r.ra == rid and r.nivel == MASTER for r in rows)],
        "courses_without_outcomes": [f for f in graduate if not any(r.curso == f for r in rows)],
        "included_competencies": [
            {"id": cid, "enunciado": c.header.get("enunciado"), "subcampos": c.header.get("subcampos")}
            for cid, c in competencies.items()
            if c.header.get("estado") == INCLUDED
        ],
        "undergraduate": [
            {
                "folder": c.folder,
                "file_exists": c.folder in written,
                "outcomes": [
                    {"id": o.id, "enunciado": o.statement, "competencias": list(o.competencies)}
                    for o in (parse_course_outcomes(written[c.folder]) if c.folder in written else [])
                ],
            }
            for c in undergraduate(courses)
        ],
    }


if __name__ == "__main__":
    print(json.dumps(status(Layout(ROOT)), ensure_ascii=False, indent=2))
