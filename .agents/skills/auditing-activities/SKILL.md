---
name: auditing-activities
description: Maps in detail what the student must learn in one course - the course outcomes of its file in 04-curriculum/ and the knowledge and skills of their competencies - against what each presential workshop (Pxxx_) of 05-implementation/<curso>/ achieves, as the highlights of its activity.md describe it, with levels. It describes activities that lack activity.md, finds what is missing and what is left over, protects the course's identity in Analytics, and writes exact point changes in each Pxxx_/tasks.md and new activities in the course tasks.md, plus the coverage and traceability.yaml, without touching the implementation. Use when david runs /auditing-activities <curso>, asks to describe, audit, map or review the activities or workshops of a course, asks which activities cover an outcome, or asks for the state of the courses.
---

# Auditing activities

Deterministic Python scripts do everything mechanical: listing the
activities, checking descriptions and the paths their highlights cite,
reading what the course must cover, checking the audit, numbering
proposals, and writing the proposals, the logs, the coverage and
`traceability.yaml`. You contribute only judgment: describing what each
activity contributes, mapping what the student must learn against those
highlights, and proposing the changes, each justified on methodological,
technical and pedagogical principles and on the identity of the course.

It runs on one course at a time: `/auditing-activities <curso>`, where
`<curso>` is a folder of `05-implementation/` and of
`04-curriculum/courses.md`, with its course file in
`04-curriculum/postgraduate/` or `04-curriculum/undergraduate/`.

Read before working; never restate them here:

- `references/format.md`: every file this skill writes, its rules, the
  categories, the decisions and the pedagogical limit of an activity.
- `references/describing.md`: the method to describe an activity.
- `references/auditing.md`: the method to audit a course and the audit
  file.
- `AGENTS.md` at the repository root and the **Identidad** of the course
  file: the identity the audit protects. Apply them; do not invent new
  identity criteria.

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

It prints the course outcomes with the level the course owes each, the
items with their ids, the identity, required knowledge and scope of the
course file, the activities with their highlights, surfaces, proposals and
decisions, and the open course proposals. If it stops because the course
file or its outcomes are missing, tell david to run `mapping-curriculum`
first. If it lists blocked
activities, go back to step 1.

Follow `references/auditing.md`: anchor every signal to highlights with
their level, account for every highlight, decide every activity, justify
every proposal and write the audit JSON in the scratchpad.

## 3. Check and apply

```bash
python3 .agents/skills/auditing-activities/scripts/check_audit.py <audit.json>
python3 .agents/skills/auditing-activities/scripts/apply_audit.py <audit.json>
python3 .agents/skills/auditing-activities/scripts/apply_audit.py <audit.json> --write
```

Correct every error of the check and repeat. Without `--write`, the apply
script prints what it would change; with it, it writes the new point
changes in each `Pxxx_<nombre>/tasks.md` and the new course changes in the
course `tasks.md`, adds the audit as a source of the proposals it
reinforces, appends an `AUD` entry to each activity's `log.md` (creating
it if needed), rewrites the audited entries of `traceability.yaml` and
rewrites the course `audit.md`. It refuses an audit with errors or
one already applied.

## 4. Report

Give david a short report:

- the decision of each activity: unchanged, point change or course
  decision, with the reason in a line;
- the course outcomes not reached at the level the course owes them, the
  items left uncovered, and the course changes they produced;
- the highlights outside what the course must teach, kept or trimmed;
- the proposals created or reinforced, with their ids;
- warnings left (legacy traceability entries, activities with many open
  proposals); and
- an identity check against the course file: whether the course still
  ends in its terminal product, and whether any activity reads as the
  abbreviated course its file names as the risk.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/auditing-activities/scripts/
```
