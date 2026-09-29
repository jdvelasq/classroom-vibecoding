# S04 — Collect Cases from Wiley

## Objective

Inspect Wiley books and their documented book-specific companion materials to
identify, verify, and record cases that may later be selected from the catalog
for Analytics-course design.

This task is catalog construction. It is not curriculum design, activity
construction, assessment design, or audit.

The catalog unit is a case. A newly found Wiley book is not itself an output:
continue into its documented companion material until a named project with
concrete data either passes the verification gate and yields a case YAML, or is
reported as excluded with the unmet condition. Do not create book-level
inventory YAML files.

---

## Governing instructions

Read and comply with the repository-level `AGENTS.md` before performing this
task.

Analytics is the curriculum's organizing identity. Methods, tools, and
technologies found in a Wiley book may be recorded only for their bounded
contribution to an Analytics case; do not use a book's chapter sequence or
disciplinary framing to redefine the curriculum.

---

## Source boundary

Treat **Wiley** as the publisher source and each identifiable book as a
distinct subsource. A book may have its own Wiley page, author site,
repository, organization, package, or companion materials; do not assume that
one URL or one repository represents all Wiley books.

Use first-party Wiley pages and documented book-specific sources to establish
book identity. Prefer an official companion repository, an author-maintained
repository explicitly linked to the book, or documented downloadable materials
to verify a candidate case and its data.

Do not download, copy, redistribute, or store datasets, code, or book content
in this repository. Record provenance, access, and terms only.

### Companion-package rule

A general-purpose tool or library (for example pandas, scikit-learn, Keras,
or tidymodels) is a distinct catalog source. A case using data supplied only by
such a tool must not be recorded under Wiley merely because the book uses it.

A package may count as a **book-specific companion distribution** only when
reliable documentation explicitly links it to the identified Wiley book and
states that it contains that book's data or examples. Record the package as a
companion source, then trace the original dataset provenance separately. Do
not treat the package itself as proof that third-party data may be reused.

---

## Periodic collection behavior

This task is intended to be run repeatedly. The existing contents of
`catalog/wiley/` are the local record of what has already been considered;
they are a baseline for comparison, not evidence that the Wiley catalog is
complete or current.

The directory and prior records are optional. If `catalog/wiley/` does not
exist or contains no case records, this is the first collection: establish the
baseline from current Wiley sources and create the directory only when a case
passes the verification gate.

At the start of every execution:

1. Inspect the existing Wiley book directories and records, including their
   editions and access dates.
2. Search current first-party Wiley listings and documented book pages for
   books or new editions published since the newest relevant materials already
   represented locally, as well as older eligible books that are absent from
   the local catalog.
3. For each newly found or revised book, locate its specific companion sources
   and apply this task's companion-package rule and verification gate to its
   cases.

A newer book, edition, dataset revision, or better-documented case may be a
potential successor to an existing case, but it must be added as a separate
record. Never delete, overwrite, or silently replace the earlier record. Make
the possible relationship visible in the new record and final report so that a
later course-design decision can choose between them.

If no qualifying material is found during a run, leave the existing catalog
unchanged and report the sources searched and the date of the review.

---

## Output structure

For a verified new case discovered through a Wiley book, create one YAML
record under:

`catalog/wiley/<book-slug>/<case-slug>.yaml`

The publisher and book path records **where the case was discovered**. It does
not imply that Wiley owns the case, dataset, or historical event.

Each record must identify:

- the Wiley book, edition when available, official page, and access date;
- every book-specific repository or companion source used;
- the named case, original data source, access route, and license or terms;
- the relationship between the data and the case;
- a concise analytical problem, limitations, and possible analytical questions;
- any substantive connection to `design/benchmarks/`.

Use one YAML per case, never separate `datasets/` and `problems/` records.

---

## Duplicate rule

Before creating a case, search all of `catalog/` by canonical name, aliases,
dataset name, and meaningful source identifiers.

- If no equivalent case exists, create the Wiley-path YAML record.
- If the same case already exists, do not create a duplicate merely because it
  appears in a Wiley book. Report the possible cross-source link, including
  the existing path and Wiley-book evidence, for a later canonical-linking
  decision.
- Do not move, rename, or overwrite existing case records during this task.

---

## Verification gate

Create a record only when all of the following are verified:

- a named, bounded case or real-world analytical episode is identifiable;
- a concrete dataset or documented reconstruction is materially related to it;
- the original dataset provider, access route, and contents are concrete;
- data terms are explicit enough for a later educational-use decision;
- the Wiley book or documented book-specific companion establishes the book
  connection;
- provenance, reproducibility, and material limitations can be described.

Exclude generic code examples, toy datasets, anonymous exercises, marketing
anecdotes, and cases whose dataset, terms, or book connection cannot be
verified.

---

## Required record contents

Use the case-record structure defined in
`catalog/tasks/s01-collect-historical-cases.md`, adapted to include a source
entry that records the Wiley book and any documented companion repository.

Include a `book_source` block:

```yaml
book_source:
  publisher: Wiley
  title: <book title>
  edition: <edition or null>
  official_url: <Wiley book URL>
  companion_sources:
    - title: <repository or companion-material title>
      url: <URL>
      relationship: <how it is documented as belonging to the book>
  access_date: YYYY-MM-DD
```

Record original dataset provenance separately in `datasets` and `sources`.

---

## Execution method

1. Identify a current Wiley book and its official page.
2. Compare it with the books and editions already represented in
   `catalog/wiley/`, and determine whether it is newly discovered, a new
   edition, or an update to a previously considered source.
3. Locate documented book-specific companion materials and repositories.
4. Determine whether each dataset comes from the book-specific companion or
   merely from a general library or tool.
5. Inspect the companion materials to identify a named project, its analytical
   problem, and its concrete associated data; do not stop at the book or
   repository landing page.
6. Identify named candidate cases, then apply the duplicate search.
7. Verify case identity, original dataset provenance, access, terms, contents,
   and limitations from the strongest available sources.
8. Create only qualifying YAML records in the book-specific Wiley path.
9. Remove each migrated legacy entry from `catalog/case-inventory.yaml`; if one
   canonical record consolidates multiple legacy entries, remove every covered
   entry and retain their names as aliases.
10. Search `design/benchmarks/` for substantive case connections without
   editing benchmark files.
11. Validate all YAML files created or updated.

---

## Completion condition

The task is complete when each newly created record is a verified, nonduplicate
case associated with a specific Wiley book and documented companion source; its
original data provenance and terms are traceable; its limitations are visible;
and its local benchmark lookup is recorded.

## Final response

Report:

- Wiley books and companion sources inspected;
- new or revised books and editions found since the prior local collection;
- the companion-package decision for each source;
- YAML records created or updated;
- legacy inventory records removed;
- duplicates intentionally not created, with their existing catalog paths;
- excluded leads and the verification condition each failed;
- local benchmark connections found or not found.
