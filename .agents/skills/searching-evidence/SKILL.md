---
name: searching-evidence
description: Searches the public web for new evidence documents for the Analytics curriculum, following 01-evidence/sources.md (international university curricula and syllabi), prints or downloads each chosen page to PDF with its URL, date and query, and leaves it in 01-evidence/ingest/agent/ for the selecting-evidence skill. Use when david asks to search, look for, find or gather new evidence, syllabi or curricula. Learning platforms are not searched: they are covered by the syntheses in 01-evidence/syntheses/.
---

# Searching evidence

Deterministic Python scripts do everything mechanical: reading the sources
and the search log, limits, downloading or printing to PDF, hashing,
duplicate detection and logging. You contribute only judgment: searching and
choosing which pages to fetch.

Sources of truth, read them before searching; never restate them here:

- `01-evidence/sources.md`: sources, what to look for, search terms, limits
  and destination category.
- `01-evidence/domain.md`: the field, to judge whether a page is worth
  fetching.

Run every command from the repository root.

## 1. Plan

```bash
python3 .agents/skills/searching-evidence/scripts/plan.py
```

It refuses to run if sources.md is not the version the scripts implement;
in that case review `scripts/search_lib.py` and `scripts/fetch.py` against
the new version and update `SUPPORTED_SOURCES_VERSION` and the tests first.
It prints the parsed sources, the per-run limits, the URLs already fetched,
the queries already run and the titles already indexed.

## 2. Search and choose (your part)

Use WebSearch and WebFetch. For each university in the plan, combine the search terms of sources.md with that source's document
type. Skip queries already run and URLs already fetched; prefer targets with
fewer fetched documents.

Choose a page only when it is public, matches what sources.md asks for (a
programme curriculum or a core course syllabus), and is plausibly pertinent
to domain.md. Never sign in or pay. Learning platforms are not searched:
`01-evidence/syntheses/` covers them.

Write the chosen pages, best first, as a JSON list to
`01-evidence/ingest/agent/.candidates.json`; the expected shape is in the
docstring of `scripts/fetch.py`. List a few more than the limits allow: the
script stops each target at its limit and logs the rest as `over-limit`.

## 3. Fetch

```bash
python3 .agents/skills/searching-evidence/scripts/fetch.py 01-evidence/ingest/agent/.candidates.json
```

It downloads PDFs directly and prints HTML pages to PDF with headless Chrome
(set `CHROME_BIN` if Chrome is not in the usual place), keeping Chrome's
header and footer so each page shows its URL and access date. It skips URLs
already fetched and files whose SHA-256 matches an indexed, logged or inbox
document, applies the per-run limits, writes each new PDF to
`01-evidence/ingest/agent/`, and appends every candidate to
`01-evidence/searches.csv` with its status. A failed page is logged and does
not stop the run.

Open a couple of the new PDFs to check that the printed page carries the
content (not a cookie wall or an empty shell). Delete a PDF that does not,
and change its row's status in `searches.csv` to `failed: empty`.

Delete `01-evidence/ingest/agent/.candidates.json` after the run.

## 4. Report and hand over

Give david a short report: documents fetched per university, and
duplicates, limits or failures worth knowing. Then offer to run the
selecting-evidence skill on them; do not judge them here.

## Testing the scripts

```bash
.venv/bin/python -m pytest -q .agents/skills/searching-evidence/scripts/
```
