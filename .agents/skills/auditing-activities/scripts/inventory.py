"""Prints, as JSON, the activities of a course that the model must describe.

Usage (from the repository root):

    python3 .agents/skills/auditing-activities/scripts/inventory.py <curso> [Pxxx ...]

For every Pxxx_ folder of the course, in numeric order, it reports the files
of each subfolder, the traceability entry, whether the description and the
log exist, the highlights and surfaces already described, the latest S02 log
entry and the id the next one must take. The locations come from paths.py.
`to_describe` lists the activities that still lack a description: only those
are described. It reads only; it never writes a file.
"""

from __future__ import annotations

import argparse
import json

from activity_lib import (
    DESCRIPTION_LOG,
    ROOT,
    Layout,
    activity_dirs,
    activity_files,
    latest_entry,
    next_entry,
    parse_activity,
    parse_log,
    parse_traceability,
    require_course,
    require_supported_format,
)


def inventory(layout: Layout, course: str, only: list[str] | None = None) -> dict[str, object]:
    format_version = require_supported_format(layout)
    require_course(layout, course)
    trace = parse_traceability(layout.traceability(course))
    dirs = activity_dirs(layout, course)
    unknown = sorted(set(only or []) - set(dirs))
    if unknown:
        raise SystemExit(f"{', '.join(unknown)} is not an activity folder of 05-implementation/{course}/")
    activities = []
    for aid, directory in dirs.items():
        if only and aid not in only:
            continue
        activity_path = layout.activity(course, directory.name)
        entries = parse_log(layout.log(course, directory.name))
        activity = parse_activity(activity_path) if activity_path.exists() else None
        activities.append({
            "id": aid,
            "folder": layout.shown(directory),
            "files": activity_files(layout, course, directory),
            "traceability": trace.entries.get(aid),
            "description": layout.shown(activity_path),
            "description_exists": activity_path.exists(),
            "log": layout.shown(layout.log(course, directory.name)),
            "highlights": [f"{h} — {t}" for h, t in activity.highlights()] if activity else [],
            "surfaces": activity.surface_ids() if activity else [],
            "latest_description": latest_entry(entries, DESCRIPTION_LOG),
            "next_description": next_entry(entries, DESCRIPTION_LOG, aid),
        })
    return {
        "format_version": format_version,
        "course": course,
        "implementation": layout.shown(layout.implementation(course)),
        "traceability": layout.shown(layout.traceability(course)),
        "to_describe": [a["id"] for a in activities if not a["description_exists"]],
        "activities": activities,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("course")
    parser.add_argument("activities", nargs="*")
    args = parser.parse_args()
    print(json.dumps(inventory(Layout(ROOT), args.course, args.activities), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
