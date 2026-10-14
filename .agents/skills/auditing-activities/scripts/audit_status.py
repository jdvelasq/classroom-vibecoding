"""Prints, as JSON, what the model needs before auditing the activities of a course.

Usage (from the repository root):

    python3 .agents/skills/auditing-activities/scripts/audit_status.py <curso>

It reports what the course must cover (its learning outcomes from the matrix,
or its course outcomes if it is an undergraduate course, and the knowledge
and skill items of their competencies, each with a stable id), the activities
of the course with their highlights, surfaces, current traceability entry,
open proposals and previous decisions, the course proposals, and the
activities whose description must be fixed before auditing. It reads only.
"""

from __future__ import annotations

import argparse
import json

from activity_lib import ROOT, Layout, parse_log, parse_traceability, require_course, require_supported_format
from audit_lib import (
    CATEGORIES,
    COURSE_TASK_TYPES,
    DECISIONS,
    MAX_NEW_TASKS_PER_ACTIVITY,
    MAX_OPEN_TASKS_PER_ACTIVITY,
    TASK_TYPES,
    activity_tasks,
    course_activities,
    course_tasks,
    describe_problems,
    load_description,
    requirements,
)


def status(layout: Layout, course: str) -> dict[str, object]:
    format_version = require_supported_format(layout)
    require_course(layout, course)
    reqs = requirements(layout, course)
    trace = parse_traceability(layout.traceability(course))
    activities = []
    blocked = []
    for activity in course_activities(layout, course):
        problems = describe_problems(layout, activity)
        if problems:
            blocked.append({"actividad": activity.ref, "problems": problems})
            activities.append({"actividad": activity.ref, "described": False})
            continue
        description = load_description(layout, activity)
        log = parse_log(layout.log(activity.owner, activity.folder.name))
        activities.append({
            "actividad": activity.ref,
            "described": True,
            "description": layout.shown(layout.activity(activity.owner, activity.folder.name)),
            "title": description.title,
            "highlights": [f"{h} — {t}" for h, t in description.highlights()],
            "surfaces": description.surface_ids(),
            "traceability": trace.entries.get(activity.ref),
            "proposals": [
                {"id": e.id, "title": e.title, "estado": e.state}
                for e in activity_tasks(layout, activity)
            ],
            "decisions": [e.id for e in log if e.prefix == "DEC"],
            "audits": [e.id for e in log if e.prefix == "AUD"],
        })
    return {
        "format_version": format_version,
        "course": course,
        "level": reqs.level,
        "source": reqs.source,
        "competency_dates": reqs.competency_dates,
        "targets": [
            {"id": t.id, "enunciado": t.statement, "nivel": t.level, "aporte": t.contribution,
             "competencias": list(t.competencies)}
            for t in reqs.targets
        ],
        "items": [{"id": i.id, "texto": i.text} for i in reqs.items],
        "activities": activities,
        "course_proposals": [
            {"id": e.id, "title": e.title, "estado": e.state}
            for e in course_tasks(layout, course)
        ],
        "blocked": blocked,
        "categories": list(CATEGORIES),
        "decisions": list(DECISIONS),
        "task_types": list(TASK_TYPES),
        "course_task_types": list(COURSE_TASK_TYPES),
        "max_new_proposals_per_activity": MAX_NEW_TASKS_PER_ACTIVITY,
        "max_open_proposals_per_activity": MAX_OPEN_TASKS_PER_ACTIVITY,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("course")
    args = parser.parse_args()
    print(json.dumps(status(Layout(ROOT), args.course), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
