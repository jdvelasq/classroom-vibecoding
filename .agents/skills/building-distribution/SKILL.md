---
name: building-distribution
description: Regenerates 06-distribution/, the student-facing copy of each course, from the activities in 05-implementation/. Fully deterministic, no judgment involved. Use when david asks to build, rebuild or refresh the distribution, or after activities in 05-implementation/ were added, renamed or changed.
---

# Building the distribution

This skill has no judgment point: one deterministic script does all the
work. Do not edit `06-distribution/` by hand; it is rebuilt from scratch on
every run.

Run every command from the repository root.

## 1. Build

```bash
python3 .agents/skills/building-distribution/scripts/build_distribution.py
```

For each course in `COURSE_ACTIVITIES` (inside the script) it:

1. checks that every listed activity exists in `05-implementation/` and
   stops, listing the missing ones, before touching anything;
2. deletes `06-distribution/<course>/` and recreates it with a copy of the
   root `conftest.py`;
3. copies each listed activity `05-implementation/<path>` into
   `06-distribution/<course>/<activity>/`;
4. empties `professor/`, `submission/` and `temp/` in each copy, leaving a
   `.gitkeep`, and removes local artifacts (`__pycache__`,
   `.pytest_cache`, `.ipynb_checkpoints`, `.DS_Store`).

Which activities go into each course, and in which order, is set by
`COURSE_ACTIVITIES`. When an activity is added, renamed or retired in
`05-implementation/`, update that list first. If the script stops on
missing activities, report them to david; do not guess replacements.

## 2. Check

```bash
git status --short 06-distribution | head
```

Report to david which courses changed. If nothing changed, say so.

## 3. Commit

Commit what the run produced on `main` (no push):

```bash
git add -A 06-distribution
git commit -m "Rebuild 06-distribution from 05-implementation"
```
