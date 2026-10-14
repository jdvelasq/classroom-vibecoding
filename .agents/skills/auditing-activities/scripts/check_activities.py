"""Validates the descriptions and logs of a course against references/format.md.

Usage (from the repository root):

    python3 .agents/skills/auditing-activities/scripts/check_activities.py <curso> [Pxxx ...]

It checks that every Pxxx_ folder has its description, that each
description follows the format, that every highlight is backed by paths that
exist and linked to an existing surface, and that the entries of a log, when
there is one, are numbered in order. It prints warnings and errors and
exits with status 1 when there is an error. It never rewrites a file.
"""

from __future__ import annotations

import argparse
import sys

from activity_lib import (
    ROOT,
    Layout,
    activity_dirs,
    parse_activity,
    require_course,
    require_supported_format,
    validate_activity,
    validate_log,
)


def check(layout: Layout, course: str, only: list[str] | None = None) -> tuple[list[str], list[str]]:
    require_supported_format(layout)
    require_course(layout, course)
    dirs = activity_dirs(layout, course)
    errors: list[str] = []
    warnings: list[str] = []
    selected = only or list(dirs)
    for aid in selected:
        if aid not in dirs:
            errors.append(f"{aid} is not an activity folder of 05-implementation/{course}/")
            continue
        folder = dirs[aid].name
        path = layout.activity(course, folder)
        if not path.exists():
            errors.append(f"{layout.shown(path)}: the description does not exist")
        else:
            e, w = validate_activity(parse_activity(path), layout, course)
            errors += e
            warnings += w
        e, w = validate_log(layout.log(course, folder), layout, aid)
        errors += e
        warnings += w
    return errors, warnings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("course")
    parser.add_argument("activities", nargs="*")
    args = parser.parse_args()
    errors, warnings = check(Layout(ROOT), args.course, args.activities)
    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
