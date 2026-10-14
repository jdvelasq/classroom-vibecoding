---
name: auditing-activities
description: Describes and audits the presential workshops (Pxxx_) of one course in 05-implementation/<curso>/ against what the course must cover in the design chain - its learning outcomes in 04-curriculum/matrix.csv (or its course outcomes for data and fundamentos) and the knowledge and skills of their competencies in 02-competencies/map/. It describes activities that lack activity.md, classifies every activity as unchanged, point change or course decision, and writes the proposals, the logs, the coverage and traceability.yaml without touching the implementation. Use when david runs /auditing-activities <curso>, asks to describe, audit, map or review the activities or workshops of a course, asks which activities cover an outcome, or asks for the state of the courses.
---

# Auditing activities

Deterministic Python scripts do everything mechanical: listing the
activities, checking descriptions and the paths their highlights cite,
reading what the course must cover, checking the audit, numbering
proposals, and writing the proposals, the logs, the coverage and
`traceability.yaml`. You contribute only judgment: describing what each
activity contributes, and deciding what the course outcomes ask of it.

It runs on one course at a time: `/auditing-activities <curso>`, where
`<curso>` is a folder of `05-implementation/` and of
`04-curriculum/courses.md`.

Read before working; never restate them here:

- `references/format.md`: every file this skill writes, its rules, the
  categories, the decisions and the pedagogical limit of an activity.
- `references/describing.md`: the method to describe an activity.
- `references/auditing.md`: the method to audit a course and the audit
  file.
- `AGENTS.md` at the repository root: the curriculum identity and the
  course-identity audit questions.

Every location is fixed in `scripts/paths.py`. Run every command from the
repository root. Never modify an activity's implementation, its
`activity.md` outside the description phase, `02-competencies/`,
`03-learning-outcomes/` or `04-curriculum/`.

## 0. State of all courses (optional)

```bash
python3 .agents/skills/auditing-activities/scripts/courses_status.py
```

It prints, without auditing, each course's activities, those still to
describe, whether its outcomes can be read, its audited and legacy
traceability entries, its open proposals and its last audit. Use it when
david asks how the courses stand, and to choose the next course.

## 1. Describe what lacks a description

```bash
python3 .agents/skills/auditing-activities/scripts/inventory.py <curso>
```

It lists the activities in order with their files, and `to_describe`: the
activities without `activity.md`. Describe only those, following
`references/describing.md`; an existing description is not regenerated
unless david asks. Then:

```bash
python3 .agents/skills/auditing-activities/scripts/check_activities.py <curso> [Pxxx ...]
```

Correct every error and repeat until there are none. An error in a
description you did not write is reported to david, not rewritten.

## 2. Audit (your part)

```bash
python3 .agents/skills/auditing-activities/scripts/audit_status.py <curso>
```

It prints the targets, the items with their ids, the activities with
their highlights, surfaces, proposals and decisions, and the open course
proposals. If it stops because the matrix gives the course no outcome,
tell david to run `mapping-curriculum` first. If it lists blocked
activities, go back to step 1.

Follow `references/auditing.md`: classify every signal, decide every
activity and write the audit JSON in the scratchpad.

## 3. Check and apply

```bash
python3 .agents/skills/auditing-activities/scripts/check_audit.py <audit.json>
python3 .agents/skills/auditing-activities/scripts/apply_audit.py <audit.json>
python3 .agents/skills/auditing-activities/scripts/apply_audit.py <audit.json> --write
```

Correct every error of the check and repeat. Without `--write`, the apply
script prints what it would change; with it, it writes the new proposals
in `tasks/Pxxx_tasks.md` and `tasks/course_tasks.md`, adds the audit as a
source of the proposals it reinforces, appends an `AUD` entry to each
activity's `log.md`, rewrites the audited entries of `traceability.yaml`
and rewrites `tasks/course_audit.md`. It refuses an audit with errors or
one already applied.

## 4. Report

Give david a short report:

- the decision of each activity: unchanged, point change or course
  decision, with the reason in a line;
- the targets and items left uncovered, and the course decisions they
  produced;
- the proposals created or reinforced, with their ids;
- warnings left (legacy traceability entries, activities with many open
  proposals); and
- an identity check: whether any activity, or the course as a whole,
  reads like an abbreviated course in one contributing discipline.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/auditing-activities/scripts/
```
