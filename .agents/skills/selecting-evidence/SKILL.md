---
name: selecting-evidence
description: Selects the documents waiting in 01-evidence/ingest/ as evidence for the Analytics curriculum, applying 01-evidence/criteria.md against 01-evidence/domain.md, then files, indexes and reports each one. Use when david adds PDFs to 01-evidence/ingest/, asks to process, select, classify or triage evidence documents, or when the agent has placed documents it found in 01-evidence/ingest/agent/.
---

# Selecting evidence

Deterministic Python scripts do everything mechanical: conversion, hashing,
duplicate detection, the decision rule, identifiers, file moves and the
index. You contribute only judgment: reading each document and scoring it.

Sources of truth, read them before judging; never restate them here:

- `01-evidence/criteria.md`: criteria, scales, decision rule, calibration set.
- `01-evidence/domain.md`: field, subfields, precursors and neighbours.

Documents in `01-evidence/ingest/agent/` were found by the agent; every other
document in `01-evidence/ingest/` was contributed by david. The scripts derive
the source from that location.

Run every command from the repository root.

## 0. Re-evaluate after a domain change

```bash
python3 .agents/skills/selecting-evidence/scripts/reeval.py
```

It lists decisions made under an earlier `domain.md` version. If the list is
empty, go on. Otherwise read the change log of `domain.md` since those
versions and apply the re-evaluation rule of criteria.md: decide whether the
domain widened, narrowed or both, and restore only the group that rule
names:

```bash
python3 .agents/skills/selecting-evidence/scripts/reeval.py --restore E0002 E0007
```

Restored documents return to the inbox and go through the steps below like
any other document. Report any document whose file is missing.

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

It creates `01-evidence/index.csv` if missing, moves exact duplicates (same
SHA-256 as an indexed document) to `01-evidence/rejected/duplicates/`, and
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

- `material_warnings`: `true` when the conversion warnings limit what you
  could read or later cite (for example, most pages without text). A cover
  page with little text is not material. It never blocks the decision; it
  is recorded and reported.
- `doubts`: optional, one sentence on anything uncertain in your judgment.
  Recorded and reported, never a reason to leave a document pending.
- `category`: the authority category of criteria.md, written as the folder
  name: `authoritative`, `governmental`, `institutional`,
  `literature-derived` or `professional-learning`.
- `role`: `actual` or `precursor`, as criteria.md defines them.
- `title`, `issuer`, `year`, and a one- or two-sentence `rationale` that
  names the subfield, precursor or neighbour of domain.md it relates to.

Write the judgments as a JSON list to `01-evidence/ingest/.judgments.json`
(the inbox is gitignored); the expected shape is in the docstring of
`scripts/apply.py`.

## 4. Apply

```bash
python3 .agents/skills/selecting-evidence/scripts/apply.py 01-evidence/ingest/.judgments.json --dry-run
python3 .agents/skills/selecting-evidence/scripts/apply.py 01-evidence/ingest/.judgments.json
```

The script refuses to run if criteria.md is not the version its rule
implements; in that case update `decide` in `scripts/evidence_lib.py` to the
new rule and its tests first. It then:

- moves accepted documents to `01-evidence/pdf/<category>/` and
  `01-evidence/md/<category>/`;
- moves rejected documents (PDF and `.md`) to `01-evidence/rejected/`, which
  is versioned for audit;
- always decides: nothing is left pending in `01-evidence/ingest/`;
- checks titles and issuers already indexed: the same year is rejected as a
  duplicate (`duplicate_of`); a different year is decided as a new edition
  and linked through `previous_edition`;
- writes `01-evidence/decisions/<id>.yaml` and appends to `01-evidence/index.csv`.

Delete `01-evidence/ingest/.judgments.json` after a successful run.

## 5. Report

Give david a short report: accepted (category and role), rejected,
duplicates, new editions, re-evaluated documents, and any conversion
warnings or doubts. Do not repeat the
scores; they are in `01-evidence/decisions/`.

TODO: once a competency map exists, also report what each accepted document
adds to it.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/selecting-evidence/scripts/
```
