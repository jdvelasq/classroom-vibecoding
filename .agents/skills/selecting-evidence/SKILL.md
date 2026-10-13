---
name: selecting-evidence
description: Selects the documents waiting in evidence/ingest/ as evidence for the Analytics curriculum, applying evidence/criteria.md against evidence/domain.md, then files, indexes and reports each one. Use when david adds PDFs to evidence/ingest/, asks to process, select, classify or triage evidence documents, or when the agent has placed documents it found in evidence/ingest/agent/.
---

# Selecting evidence

Deterministic Python scripts do everything mechanical: conversion, hashing,
duplicate detection, the decision rule, identifiers, file moves and the
index. You contribute only judgment: reading each document and scoring it.

Sources of truth, read them before judging; never restate them here:

- `evidence/criteria.md`: criteria, scales, decision rule, calibration set.
- `evidence/domain.md`: field, subfields, precursors and neighbours.

Documents in `evidence/ingest/agent/` were found by the agent; every other
document in `evidence/ingest/` was contributed by david. The scripts derive
the source from that location.

Run every command from the repository root.

## 1. Convert

```bash
uv run design/tasks/s01-convert-benchmarks.py
```

If `uv` is not on the PATH, try `~/Library/Python/3.9/bin/uv`. The converter
skips files that are already up to date.

## 2. Intake

```bash
python3 .agents/skills/selecting-evidence/scripts/intake.py
```

It creates `evidence/index.csv` if missing, moves exact duplicates (same
SHA-256 as an indexed document) to `evidence/rejected/duplicates/`, and
prints a JSON manifest of pending documents with their source and conversion
warnings. Report the duplicates; do not judge them.

## 3. Judge (your part)

For each pending document, read only the start of its `.md` (header and the
first pages: title, issuer, date, table of contents, purpose). Read further
only when that is not enough to score it. If there is no `.md` or no usable
text, judge pertinencia from the title, file name and metadata, as
criteria.md allows.

Score the five criteria of criteria.md (0, 1, 2). For a document whose
pertinencia is 0, the other scores may be `null`. Also decide:

- `material_warnings`: `true` only when the conversion warnings prevent you
  from judging or later citing the content (for example, most pages without
  text). A cover page with little text is not material.
- `category`: the authority category of criteria.md, written as the folder
  name: `authoritative`, `governmental`, `institutional`,
  `literature-derived` or `professional-learning`.
- `role`: `actual` or `precursor`, as criteria.md defines them.
- `title`, `issuer`, `year`, and a one- or two-sentence `rationale` that
  names the subfield, precursor or neighbour of domain.md it relates to.

Write the judgments as a JSON list to `evidence/ingest/.judgments.json`
(the inbox is gitignored); the expected shape is in the docstring of
`scripts/apply.py`.

## 4. Apply

```bash
python3 .agents/skills/selecting-evidence/scripts/apply.py evidence/ingest/.judgments.json --dry-run
python3 .agents/skills/selecting-evidence/scripts/apply.py evidence/ingest/.judgments.json
```

The script refuses to run if criteria.md is not the version its rule
implements; in that case update `decide` in `scripts/evidence_lib.py` to the
new rule and its tests first. It then:

- moves accepted documents to `evidence/pdf/<category>/` and
  `evidence/md/<category>/`;
- moves rejected documents (PDF and `.md`) to `evidence/rejected/`, which is
  gitignored;
- leaves documents to review in `evidence/ingest/` for david;
- flags a title and issuer that are already indexed: the same year is held
  for review as a possible duplicate; a different year is processed as a new
  edition and linked through `previous_edition`;
- writes `evidence/decisions/<id>.yaml` and appends to `evidence/index.csv`.

Delete `evidence/ingest/.judgments.json` after a successful run.

## 5. Report

Give david a short report: accepted (category and role), rejected, left in
`ingest/` with the reason, duplicates and new editions. Do not repeat the
scores; they are in `evidence/decisions/`.

TODO: once a competency map exists, also report what each accepted document
adds to it.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/selecting-evidence/scripts/
```
