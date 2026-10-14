"""Prints, as JSON, the state of every course without auditing any of them.

Usage (from the repository root):

    python3 .agents/skills/auditing-activities/scripts/courses_status.py

For each course of 04-curriculum/courses.md it reports whether its
implementation folder exists, how many activities it has, which still lack a
description, whether what it must cover can already be read from the
curriculum, how many traceability entries are audited or legacy, how many
proposals are open, and the date of its last audit. It reads only.
"""

from __future__ import annotations

import json
import re

from activity_lib import ROOT, Layout, parse_traceability, require_supported_format
from audit_lib import (
    activity_tasks,
    course_activities,
    course_tasks,
    curriculum,
    curriculum_layout,
    open_tasks,
    requirements,
)


def course_state(layout: Layout, course: curriculum.Course) -> dict[str, object]:
    state: dict[str, object] = {"course": course.folder, "level": course.level, "status": course.status}
    if not layout.implementation(course.folder).is_dir():
        return {**state, "implementation": False}
    activities = course_activities(layout, course.folder)
    try:
        reqs = requirements(layout, course.folder)
        coverage: object = {"targets": len(reqs.targets), "items": len(reqs.items)}
    except SystemExit as reason:
        coverage = str(reason)
    trace = parse_traceability(layout.traceability(course.folder)).entries
    audit = layout.audit(course.folder)
    last = re.search(r"\*\*Fecha / executor:\*\* (\S+)", audit.read_text(encoding="utf-8")) if audit.exists() else None
    return {
        **state,
        "implementation": True,
        "activities": len(activities),
        "to_describe": [a.ref for a in activities
                        if not layout.activity(a.owner, a.folder.name).exists()],
        "must_cover": coverage,
        "traceability_audited": sum(isinstance(v, dict) for v in trace.values()),
        "traceability_legacy": sum(not isinstance(v, dict) for v in trace.values()),
        "open_activity_proposals": sum(len(open_tasks(activity_tasks(layout, a))) for a in activities
                                       if a.owner == course.folder),
        "open_course_proposals": len(open_tasks(course_tasks(layout, course.folder))),
        "last_audit": last.group(1) if last else None,
    }


def status(layout: Layout) -> dict[str, object]:
    format_version = require_supported_format(layout)
    _, courses = curriculum.load_courses(curriculum_layout(layout))
    return {"format_version": format_version, "courses": [course_state(layout, c) for c in courses]}


if __name__ == "__main__":
    print(json.dumps(status(Layout(ROOT)), ensure_ascii=False, indent=2))
