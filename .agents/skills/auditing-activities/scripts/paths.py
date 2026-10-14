"""Where every file this skill reads or writes lives, relative to the repository root.

This is the only place that fixes those locations: change a template here and
every script follows. `{course}` is the course folder of 05-implementation/,
`{folder}` the Pxxx_ folder of an activity and `{activity}` its Pxxx id.
"""

IMPLEMENTATION = "05-implementation/{course}"
ACTIVITY = "05-implementation/{course}/{folder}/activity.md"
LOG = "05-implementation/{course}/{folder}/log.md"
TASKS = "05-implementation/{course}/tasks/{activity}_tasks.md"
COURSE_TASKS = "05-implementation/{course}/tasks/course_tasks.md"
AUDIT = "05-implementation/{course}/tasks/course_audit.md"
TRACEABILITY = "05-implementation/{course}/traceability.yaml"

FORMAT = ".agents/skills/auditing-activities/references/format.md"

