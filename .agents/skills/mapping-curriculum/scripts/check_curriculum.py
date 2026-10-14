"""Validates courses.md, matrix.csv and the undergraduate courses against format.md.

Usage (from the repository root):

    python3 .agents/skills/mapping-curriculum/scripts/check_curriculum.py [--matrix | --undergraduate]

With no option it checks everything and prints the matrix as a table of
learning outcomes × postgraduate courses. `--matrix` checks only the
courses and the matrix; `--undergraduate` checks only the courses and the
undergraduate files, which is useful while drafting one part. It never
rewrites a file.
"""

from __future__ import annotations

import argparse
import sys

from curriculum_lib import (
    ROOT,
    Layout,
    course_subfields,
    load_competencies,
    load_courses,
    load_outcomes,
    load_undergraduate,
    matrix_view,
    read_matrix,
    require_supported_format,
    undergraduate,
    validate_courses,
    validate_matrix,
    validate_undergraduate,
)


def run(layout: Layout, matrix: bool = True, undergrad: bool = True) -> int:
    format_version = require_supported_format(layout)
    document, courses = load_courses(layout)
    competencies = load_competencies(layout)
    errors = validate_courses(document, courses, course_subfields(layout), format_version)
    warnings: list[str] = []

    if matrix:
        outcomes = load_outcomes(layout)
        if not outcomes:
            errors.append("03-learning-outcomes has no learning outcomes yet; write them before the matrix")
        rows, found = read_matrix(layout)
        errors += found
        if not layout.matrix.exists():
            errors.append("matrix.csv is missing")
        elif not found:
            found, warned = validate_matrix(rows, courses, outcomes, competencies)
            errors += found
            warnings += warned
            for line in matrix_view(rows, courses, outcomes):
                print(line)

    if undergrad:
        written = load_undergraduate(layout)
        for course in undergraduate(courses):
            if course.folder not in written:
                errors.append(f"undergraduate/{course.folder}.md is missing")
        for document in written.values():
            found, warned = validate_undergraduate(document, courses, competencies, format_version)
            errors += found
            warnings += warned

    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"error: {line}")
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    part = parser.add_mutually_exclusive_group()
    part.add_argument("--matrix", action="store_true")
    part.add_argument("--undergraduate", action="store_true")
    args = parser.parse_args()
    both = not (args.matrix or args.undergraduate)
    sys.exit(run(Layout(ROOT), matrix=both or args.matrix, undergrad=both or args.undergraduate))


if __name__ == "__main__":
    main()
