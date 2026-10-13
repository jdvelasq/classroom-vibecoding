---
name: mapping-competencies
description: Builds and maintains the competency map of the Analytics curriculum in 02-competencies/map/ from the accepted evidence in 01-evidence/index.csv, following 02-competencies/format.md. Use when david asks to map, extract, update or review competencies, to process accepted evidence into the map, or after new evidence has been selected.
---

# Mapping competencies

Deterministic Python scripts do everything mechanical: reading the index,
finding pending documents, assigning identifiers, checking the format,
computing the consensus and the state, and recording which documents were
mapped. You contribute only judgment: reading each document, extracting the
performances it describes and abstracting them into competencies.

Sources of truth, read them before mapping; never restate them here:

- `02-competencies/format.md`: file format, support types, consensus rule,
  granularity and a worked example.
- `01-evidence/domain.md`: subfields, precursors and neighbours.
- `AGENTS.md` at the repository root: the curriculum identity. The map is an
  Analytics map; contributing disciplines enter as knowledge in service of
  an analytical performance.
- `02-competencies/map/`: the existing competencies, especially the
  calibrated `C001` to `C009`.

The map has no levels. Never write or imply undergraduate, specialization
or master's level; that decision comes later, with the learning outcomes.

Run every command from the repository root.

## 1. Status

```bash
python3 .agents/skills/mapping-competencies/scripts/status.py
```

It prints JSON with the format and domain versions, the next free
competency id, a one-line summary of every competency, and two lists of
accepted documents: `pending` (never mapped) and `outdated` (mapped under an
older format or domain). The scripts refuse to run if `format.md` is not the
version they implement; in that case update `scripts/competency_lib.py` and
its tests first.

Work on the documents david names. If he names none, take the `pending`
documents in small batches (about five), and tell him how many remain.

## 2. Extract and abstract (your part)

For each document, read its `text` (the converted `.md`); if `text` is
`null`, read the PDF if you can, otherwise report it and record nothing.
Locate pages with the `<!-- fin de página N -->` markers: cite the PDF page,
not the printed number. For a synthesis, cite its section.

For each analytical performance the document describes:

1. Compare it with the `map` summary. If an existing competency would have
   the same performance evidence, add to it: a row in its sources table
   and, where the document adds something, knowledge, skill or evidence
   bullets with their citations.
2. Otherwise create `02-competencies/map/<next_id>.md` with the format of
   `format.md`, and take the following id for the next one.
3. Apply the granularity rules of `format.md`: techniques, algorithms and
   tools are knowledge or examples, never competencies.
4. Mark support honestly: `explícito`, `inferido (In)` with its chain of one
   or two steps, or `solo conocimientos` when the document backs knowledge
   but not the performance (typical of course announcements and course
   lists). An `[I]` claim in a synthesis is `inferido`.
5. Justify each subfield as `explícita [Exxxx ...]` or `por domain.md`.

Do not compute `consenso` or `estado`; write any placeholder values and let
the next step set them. Do not edit `01-evidence/`.

## 3. Validate

```bash
python3 .agents/skills/mapping-competencies/scripts/validate.py --fix
```

`--fix` sets `consenso` and `estado` from each sources table; every other
error must be corrected in the file. Repeat until it reports no errors.
Warnings name competencies written under an older `domain.md`: review their
subfields and update `domain_version` when they still hold.

## 4. Record

```bash
python3 .agents/skills/mapping-competencies/scripts/record.py E0001 E0003
```

Record every document you finished, including those that added nothing.
It writes `02-competencies/mapped.csv` with the competencies that cite each
document.

## 5. Report

Give david a short report:

- new competencies, and candidates promoted to `incluida` or retired;
- documents that added nothing, or could not be read;
- `Pendientes` that the batch opened or closed;
- an identity check: whether any group of competencies now reads like a
  syllabus of a single contributing discipline (statistics, machine
  learning, optimization, databases, BI). If so, name it.

Do not repeat the competencies' content; it is in `02-competencies/map/`.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/mapping-competencies/scripts/
```
