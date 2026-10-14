---
name: writing-learning-outcomes
description: Writes and maintains the graduate profile and the program learning outcomes of the Analytics postgraduate program in 03-learning-outcomes/, from the included competencies of 02-competencies/map/, following 03-learning-outcomes/format.md. Use when david asks to write, draft, update or review the profile, the learning outcomes (resultados de aprendizaje, RA), their coverage of the competency map, or after the map has changed.
---

# Writing learning outcomes

Deterministic Python scripts do everything mechanical: reading the
competency map, listing what must be covered, checking the format of each
outcome, its traceability to evidence, the coverage of the map and the
profile. You contribute only judgment: writing the graduate profile and
each learning outcome.

Sources of truth, read them before writing; never restate them here:

- `03-learning-outcomes/format.md`: file format, verb rules, coverage
  rules and a worked example.
- `02-competencies/map/`: the competencies, their performance evidence and
  their `Pendientes`.
- `AGENTS.md` at the repository root: the curriculum identity and, for
  prescriptive analytics, what counts as a terminal product.
- `00-regulations/md/cesu-acuerdo-02-2020.md`, numeral 2.2 a and b and
  characteristics 18, 24 and 25.

There is one program, at specialization level. Master's and doctoral
research components are out of scope; do not write outcomes for them.

Run every command from the repository root.

## 1. Status

```bash
python3 .agents/skills/writing-learning-outcomes/scripts/outcomes_status.py
```

It prints JSON with the format version and limits, the next free outcome
id, every included competency with its performance evidence, open
`Pendientes` and the outcomes that cover it, the excluded competencies
(candidates and retired), the existing outcomes and the `uncovered` list.
The scripts refuse to run if `format.md` is not the version they implement;
in that case update `scripts/outcomes_lib.py` and its tests first.

If the map itself may be stale, run the `mapping-competencies` validation
first and report its errors to david instead of working around them.

## 2. Draft (your part)

1. Group the included competencies into outcomes. An outcome integrates
   the competencies whose performance evidence can be assessed with one
   product; keep the count and the size within the limits of `format.md`.
2. For each outcome, write `03-learning-outcomes/outcomes/<id>.md` with the
   format of `format.md`: one evaluable sentence (observable verb, object,
   condition, postgraduate level), the competencies it takes, a suggested
   assessment built from their performance evidence, and the traceability
   table citing locations that appear in each competency's `Evidencia de
   desempeño`.
3. Do not name tools in the statement. Do not invent evidence: when a
   competency has none, write `Ninguna fuente` and propose the product.
4. Write or update `03-learning-outcomes/profile.md`, mentioning every
   outcome in `Desempeños`.

Do not edit `01-evidence/` or `02-competencies/`.

## 3. Validate

```bash
python3 .agents/skills/writing-learning-outcomes/scripts/check_outcomes.py
```

It prints the coverage of each included competency, then warnings and
errors. Pass outcome ids (`RA01 RA02`) to check only those files while
drafting; without ids it also checks the count, the coverage and the
profile. Correct every error in the files and repeat until there are none.
Warnings name competencies changed after an outcome was written and
outcomes traced to `Ninguna fuente`.

## 4. Report

Give david a short report:

- outcomes written or changed, and the competencies each one covers;
- warnings left and `Pendientes` opened;
- an identity check: whether the profile or any group of outcomes reads
  like a program in a single contributing discipline (statistics, machine
  learning, optimization, databases, BI), and whether every prescriptive
  outcome ends in a decision policy rather than a model.

Do not repeat the outcomes' content; it is in `03-learning-outcomes/`.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/writing-learning-outcomes/scripts/
```
