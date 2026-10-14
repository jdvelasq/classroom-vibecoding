---
name: mapping-curriculum
description: Proposes and maintains the curriculum map of the Analytics programs in 04-curriculum/, following 04-curriculum/format.md - the matrix of postgraduate learning outcomes × courses (introduce, develop, master), one file per postgraduate course, and the course outcomes of the two undergraduate courses, drawn from the competency map. Use when david asks to map the learning outcomes to courses, build or review the RA × courses matrix, write the undergraduate course outcomes, check the curriculum coverage, or after the learning outcomes or the course list have changed.
---

# Mapping the curriculum

Deterministic Python scripts do everything mechanical: reading the course
list, the learning outcomes and the competency map, and checking the
matrix, the coverage and the course files. You contribute only judgment:
proposing in which course each learning outcome is introduced, developed
and mastered, writing the file of each postgraduate course, and writing
the undergraduate course outcomes.

Sources of truth, read them before proposing; never restate them here:

- `04-curriculum/format.md`: file formats, levels, rules and a worked
  example.
- `04-curriculum/courses.md`: the courses, their level, status, subfields
  and purpose. It is david's decision: read it, never edit it.
- `03-learning-outcomes/outcomes/` and `profile.md`: the program's
  learning outcomes.
- `02-competencies/map/`: the competencies the undergraduate outcomes come
  from.
- `01-evidence/domain.md`: the subfields and the emerging trend.
- `AGENTS.md` at the repository root: the curriculum identity.

Run every command from the repository root.

## 1. Status

```bash
python3 .agents/skills/mapping-curriculum/scripts/curriculum_status.py
```

It prints JSON starting with `pending`: every file still to write. A run
is not finished while `pending` lists anything you can write. Then come
the format version, the courses in order, every
learning outcome with the subfields of its competencies and its current
cells, the outcomes not yet mastered, the postgraduate courses without
outcomes, the included competencies and the undergraduate outcomes already
written. The scripts refuse to run if `format.md` is not the version they
implement; in that case update `scripts/curriculum_lib.py` and its tests
first.

If there are no learning outcomes yet, the matrix and the postgraduate
files cannot be written: do the undergraduate part, then tell david
plainly that the postgraduate courses are still missing and that he must
run `writing-learning-outcomes` first.

## 2. Propose (your part)

1. **Matrix.** Write `04-curriculum/matrix.csv`. For each learning
   outcome, choose the postgraduate courses that work on it and the level
   in each, following the course order of `courses.md`. Start from the
   subfields of its competencies; a course outside them needs a reason in
   `aporte`. Every postgraduate course is self-contained: its students
   have not taken the undergraduate courses.
2. **Postgraduate courses.** For each postgraduate course, write
   `04-curriculum/postgraduate/<folder>.md`: its purpose, its entry
   condition (never an undergraduate course), its learning outcomes
   copied from its rows of the matrix with the same level and `aporte`,
   and its boundaries with the other courses.
3. **Undergraduate courses.** For each undergraduate course, write
   `04-curriculum/undergraduate/<folder>.md`. Draw its course outcomes
   directly from the included competencies whose subfields the course
   covers, at an introductory level, as `courses.md` describes the
   course. Never derive them from the program's learning outcomes, and
   never cite them.

Do not edit `courses.md`, `01-evidence/`, `02-competencies/` or
`03-learning-outcomes/`. If an outcome fits no course, or a course has no
outcome that belongs to it, report it to david.

## 3. Validate

```bash
python3 .agents/skills/mapping-curriculum/scripts/check_curriculum.py
```

It prints the matrix as a table, then warnings and errors. A missing
postgraduate file is an error. Use `--matrix`
or `--undergraduate` to check one part while drafting. Correct every error
and repeat until there are none. Warnings name learning outcomes changed
after a row was set, rows whose course shares no subfield with the
outcome, and outcomes introduced again after being mastered.

## 4. Report

Give david a short report:

- the matrix table printed by the check, and which course masters each
  outcome;
- the postgraduate course files written or changed;
- the undergraduate course outcomes written or changed, with their
  competencies;
- warnings left and anything that fits no course;
- an identity check: whether any course reads like an abbreviated course
  in a single contributing discipline, and whether the course that
  masters the prescriptive outcomes ends in a decision policy rather than
  a model.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/mapping-curriculum/scripts/
```
