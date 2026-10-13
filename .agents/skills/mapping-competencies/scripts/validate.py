"""Validates every competency in 02-competencies/map/ against format.md.

Usage (from the repository root):

    python3 .agents/skills/mapping-competencies/scripts/validate.py [C001 ...] [--fix]

--fix rewrites only the fields the scripts own: the `consenso` block and
`estado`, computed from each sources table with the consensus rule. Every
other problem must be corrected in the file itself.
"""

from __future__ import annotations

import argparse
import sys

from competency_lib import (
    ROOT,
    Layout,
    domain_subfields,
    fix_consensus,
    load_map,
    read_index,
    require_supported_format,
    validate,
)


def run(layout: Layout, ids: list[str], fix: bool) -> int:
    format_version = require_supported_format(layout)
    index = read_index(layout)
    subfields = domain_subfields(layout)
    competencies = [c for c in load_map(layout) if not ids or c.path.stem in ids]
    if fix:
        for competency in competencies:
            if fix_consensus(competency, index):
                print(f"fixed consensus: {competency.path.name}")
        competencies = [c for c in load_map(layout) if not ids or c.path.stem in ids]
    errors: list[str] = []
    warnings: list[str] = []
    for competency in competencies:
        found, warned = validate(competency, layout, index, subfields, format_version)
        errors += found
        warnings += warned
    for line in warnings:
        print(f"warning: {line}")
    for line in errors:
        print(f"error: {line}")
    states: dict[str, int] = {}
    for competency in competencies:
        state = str(competency.header.get("estado"))
        states[state] = states.get(state, 0) + 1
    summary = ", ".join(f"{n} {s}" for s, n in sorted(states.items()))
    print(f"{len(competencies)} competencies ({summary}); {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--fix", action="store_true")
    args = parser.parse_args()
    sys.exit(run(Layout(ROOT), args.ids, args.fix))


if __name__ == "__main__":
    main()
