"""Validates the profile and the learning outcomes against format.md.

Usage (from the repository root):

    python3 .agents/skills/writing-learning-outcomes/scripts/check_outcomes.py [RA01 ...]

With no ids it checks every outcome, then the whole set: the number of
outcomes, the coverage of every included competency and the profile. With
ids it checks only those files, which is useful while drafting. It never
rewrites a file.
"""

from __future__ import annotations

import argparse
import sys

from outcomes_lib import (
    ROOT,
    Layout,
    coverage,
    load_competencies,
    load_outcomes,
    read_index,
    require_supported_format,
    validate_outcome,
    validate_set,
)


def run(layout: Layout, ids: list[str]) -> int:
    format_version = require_supported_format(layout)
    competencies = load_competencies(layout)
    index = read_index(layout)
    outcomes = load_outcomes(layout)
    checked = [o for o in outcomes if not ids or o.path.stem in ids]
    errors: list[str] = []
    warnings: list[str] = []
    for outcome in checked:
        found, warned = validate_outcome(outcome, competencies, index, format_version)
        errors += found
        warnings += warned
    if not ids:
        errors += validate_set(layout, outcomes, competencies, format_version)
        for cid, outcome_ids in coverage(outcomes, competencies).items():
            print(f"coverage: {cid} <- {', '.join(outcome_ids) or 'none'}")
    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"error: {line}")
    print(f"{len(checked)} outcomes checked; {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*")
    args = parser.parse_args()
    sys.exit(run(Layout(ROOT), args.ids))


if __name__ == "__main__":
    main()
