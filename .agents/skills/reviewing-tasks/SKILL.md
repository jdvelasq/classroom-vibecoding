---
name: reviewing-tasks
description: Reviews with david, one at a time, the pending improvement proposals of a course - the point changes in each 05-implementation/<curso>/Pxxx_<nombre>/tasks.md and the new activities in the course tasks.md - that auditing-activities wrote. For each one it presents the proposal, discusses it, and records david's decision (approved or rejected) by removing it from tasks.md and adding a DEC note to the log, so later audits never propose it again. Use when david runs /reviewing-tasks <curso>/<Pxxx> (one activity) or /reviewing-tasks <curso> (the course proposals), asks to review, discuss, approve or reject proposals, tasks or improvements of a course or an activity.
---

# Reviewing tasks

David's procedure: for each activity with pending improvements in its
`tasks.md`, one improvement at a time is analyzed and discussed with david.
Once discussed, approved or rejected, it leaves `tasks.md` and a note goes
to the log, so it is not proposed again in later iterations.

Deterministic Python scripts do the mechanical part: listing the proposals
in order, removing a decided one from its `tasks.md` and writing its note
to the log. You contribute the discussion: presenting one proposal
clearly, giving your reading of it, answering david, and recording exactly
what david decided and why.

The files and their locations belong to `auditing-activities`
(`.agents/skills/auditing-activities/scripts/paths.py` and
`references/format.md`). Read `AGENTS.md` at the repository root and the
course file in `04-curriculum/` before discussing: a proposal is judged by
the identity and the course outcomes they define.

It runs on one activity at a time, `/reviewing-tasks <curso>/<Pxxx>`, or
on the course proposals, `/reviewing-tasks <curso>`. Run every command
from the repository root.

## 1. Next proposal

```bash
python3 .agents/skills/reviewing-tasks/scripts/pending.py <curso>/<Pxxx>
python3 .agents/skills/reviewing-tasks/scripts/pending.py <curso>
```

It prints how many proposals are open, the full text of the next one and
the queue by id and title: those of the activity's `tasks.md`, or those of
the course `tasks.md`. If nothing is open, say so and stop.

## 2. Discuss it (your part)

Present only that proposal, in a few lines david can answer:

- what changes in the activity, or what new activity is proposed;
- what the student gains, and the methodological, technical and
  pedagogical reasons the proposal gives;
- what it costs: the length of the activity, what it displaces, and its
  interactions with the other proposals of the same activity;
- your recommendation, approve or reject, with its reason. Check it
  against the rules of `auditing-activities`: no markdown cells in
  notebooks, tests that only check the artifacts of `submission/`, and an
  activity that stays a short, well-defined problem.

Read the activity's `activity.md`, and its implementation only when the
discussion needs it. Answer david's questions. Do not decide for david:
wait for an explicit «aprobada» or «rechazada» and its reason. If david
changes the proposal, record the approved version in the reason.

## 3. Record the decision

```bash
python3 .agents/skills/reviewing-tasks/scripts/decide.py <curso>/<Pxxx> <Tnn> \
    --decision aprobada|rechazada --reason "…" --write
python3 .agents/skills/reviewing-tasks/scripts/decide.py <curso> <Nnn> \
    --decision aprobada|rechazada --reason "…" --write
```

The proposal leaves `tasks.md` (the file is removed when it is empty), and
a `DEC` entry with the date, the decision, the reason and the full text of
the proposal is appended to the activity's `log.md`, or to the course
`log.md` for a course proposal. Either log is created if it does not
exist. An approved proposal is recorded with its implementation pending.

Then go back to step 1 for the next proposal, unless david stops.

## 4. Report

When the review ends, give david a short summary: the proposals approved,
those rejected, and those still open.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/reviewing-tasks/scripts/
```
