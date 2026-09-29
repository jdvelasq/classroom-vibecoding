# S03 — Collect Cases from Manning

## Objective

Inspect Manning books and their documented companion repositories to identify,
verify, and record cases that may later be selected from the catalog for
Analytics-course design.

This task is catalog construction. It is not curriculum design, activity
construction, assessment design, or audit.

The catalog unit is a case. A newly found Manning book is not itself an output:
continue into its documented companion material until a named project with
concrete data either passes the verification gate and yields a case YAML, or is
reported as excluded with the unmet condition.

---

## Governing instructions

Read and comply with the repository-level `AGENTS.md` before performing this
task.

Analytics is the curriculum's organizing identity. Methods, tools, and
technologies found in a Manning book may be recorded only for their bounded
contribution to an Analytics case; do not use a book's chapter sequence or
disciplinary framing to redefine the curriculum.

---

## Source boundary

Treat **Manning** as the publisher source and each identifiable book as a
distinct subsource. A book may have its own Manning page, author site,
repository, organization, or companion materials; do not assume that one URL
or one repository represents all Manning books.

Use first-party Manning pages and documented book-specific sources to establish
book identity. Prefer an official companion repository, author-maintained
repository explicitly linked to the book, or documented downloadable materials
to verify a candidate case and its data.

Do not download, copy, redistribute, or store datasets, code, or book content
in this repository. Record provenance, access, and terms only.

---

## Periodic collection behavior

This task is intended to be run repeatedly. The existing contents of
`catalog/manning/` are the local record of what has already been considered;
they are a baseline for comparison, not evidence that the Manning catalog is
complete or current.

The directory and prior records are optional. If `catalog/manning/` does not
exist or contains no case records, this is the first collection: establish the
baseline from current Manning sources and create the directory only when a case
passes the verification gate.

At the start of every execution:

1. Inspect the existing Manning book directories and records, including their
   editions and access dates.
2. Search current first-party Manning listings and documented book pages for
   books or new editions published since the newest relevant materials already
   represented locally, as well as older eligible books that are absent from
   the local catalog.
3. For each newly found or revised book, locate its specific companion sources
   and apply this task's verification gate to its cases.

A newer book, edition, dataset revision, or better-documented case may be a
potential successor to an existing case, but it must be added as a separate
record. Never delete, overwrite, or silently replace the earlier record. Make
the possible relationship visible in the new record and final report so that a
later course-design decision can choose between them.

If no qualifying material is found during a run, leave the existing catalog
unchanged and report the sources searched and the date of the review.

---

## Exhaustive-completion rule

Do not stop after finding the first qualifying case. A run may report the
Manning review as **complete** only after it has exhausted the documented search
scope available on the access date:

1. Enumerate the relevant books and editions in Manning's current first-party
   catalog, including pagination or category listings where used.
2. Compare that set with the book paths already represented under
   `catalog/manning/` and identify absent books and newer editions.
3. For every relevant absent or revised book, inspect the documented companion
   material far enough to enumerate its named projects or cases with concrete
   data.
4. Classify every candidate as a created case record, an existing cross-source
   duplicate, or an excluded lead with the exact unmet verification condition.

Completion is a bounded claim about Manning's documented catalog at the review
date; it is not a claim that every Manning book ever published has been found.
If a catalog page, companion source, or candidate cannot be inspected, report
the run as **partial**, name the unreviewed scope, and do not say Manning has
been exhausted.

The final response must list reviewed books and editions, all created case
files, duplicates, exclusions, and any unreviewed or inaccessible material. No
book-level YAML, publisher inventory, or placeholder file may be created to
record that coverage.

---

## Output structure

For a verified new case discovered through a Manning book, create one YAML
record under:

`catalog/manning/<book-slug>/<case-slug>.yaml`

The publisher and book path records **where the case was discovered**. It does
not imply that Manning owns the case, dataset, or historical event.

Each record must identify:

- the Manning book, edition when available, official page, and access date;
- every book-specific repository or companion source used;
- the named case, data source, access route, and license or terms;
- the relationship between the data and the case;
- a concise analytical problem, limitations, and possible analytical questions;
- any substantive connection to `design/benchmarks/`.

Use one YAML per case, never separate `datasets/` and `problems/` records.

---

## Duplicate rule

Before creating a case, search all of `catalog/` by canonical name, aliases,
dataset name, and meaningful source identifiers.

- If no equivalent case exists, create the Manning-path YAML record.
- If the same case already exists, do not create a duplicate merely because it
  appears in a Manning book. Report the possible cross-source link, including
  the existing path and Manning-book evidence, for a later canonical-linking
  decision.
- Do not move, rename, or overwrite existing case records during this task.

This rule preserves the case as the catalog unit while the source path records
the discovery route.

---

## Verification gate

Create a record only when all of the following are verified:

- a named, bounded case or real-world analytical episode is identifiable;
- a concrete dataset or documented reconstruction is materially related to it;
- dataset provider, access route, and contents are concrete;
- data terms are explicit enough for a later educational-use decision;
- the book or documented companion source establishes the Manning connection;
- provenance, reproducibility, and material limitations can be described.

Exclude generic code examples, toy datasets, anonymous exercises, marketing
anecdotes, and cases whose dataset, terms, or book connection cannot be
verified.

---

## Required record contents

Use the case-record structure defined in
`catalog/tasks/s01-collect-historical-cases.md`, adapted to include a source
entry that records the Manning book and any documented companion repository.

Include a `book_source` block:

```yaml
book_source:
  publisher: Manning
  title: <book title>
  edition: <edition or null>
  official_url: <Manning book URL>
  companion_sources:
    - title: <repository or companion-material title>
      url: <URL>
      relationship: <how it is documented as belonging to the book>
  access_date: YYYY-MM-DD
```

Record original dataset provenance separately in `datasets` and `sources`.
An author repository is not sufficient evidence of data provenance unless it
identifies and supports that provenance.

---

## Execution method

1. Identify a current Manning book and its official page.
2. Compare it with the books and editions already represented in
   `catalog/manning/`, and determine whether it is newly discovered, a new
   edition, or an update to a previously considered source.
3. Locate documented book-specific companion materials and repositories.
4. Inspect those materials to identify a named project, its analytical problem,
   and its concrete associated data; do not stop at the book or repository
   landing page.
5. Identify named candidate cases, then apply the duplicate search.
6. Verify case identity, dataset provenance, access, terms, contents, and
   limitations from the strongest available sources.
7. Create only qualifying YAML records in the book-specific Manning path.
8. Search `design/benchmarks/` for substantive case connections without
   editing benchmark files.
9. Validate all YAML files created or updated.

---

## Completion condition

The task is complete when each newly created record is a verified, nonduplicate
case associated with a specific Manning book and documented companion source;
its data and terms are traceable; its limitations are visible; and its local
benchmark lookup is recorded.

## Final response

Report:

- Manning books and companion sources inspected;
- new or revised books and editions found since the prior local collection;
- YAML records created or updated;
- duplicates intentionally not created, with their existing catalog paths;
- excluded leads and the verification condition each failed;
- local benchmark connections found or not found.
