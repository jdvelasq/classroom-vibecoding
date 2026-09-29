# S03 — Collect Cases from Manning

## Objective

Inspect Manning books and their documented companion repositories to identify,
verify, and record cases that may later be selected from the catalog for
Analytics-course design.

This task is catalog construction. It is not curriculum design, activity
construction, assessment design, or audit.

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
2. Locate documented book-specific companion materials and repositories.
3. Identify named candidate cases, then apply the duplicate search.
4. Verify case identity, dataset provenance, access, terms, contents, and
   limitations from the strongest available sources.
5. Create only qualifying YAML records in the book-specific Manning path.
6. Search `design/benchmarks/` for substantive case connections without
   editing benchmark files.
7. Validate all YAML files created or updated.

---

## Completion condition

The task is complete when each newly created record is a verified, nonduplicate
case associated with a specific Manning book and documented companion source;
its data and terms are traceable; its limitations are visible; and its local
benchmark lookup is recorded.

## Final response

Report:

- Manning books and companion sources inspected;
- YAML records created or updated;
- duplicates intentionally not created, with their existing catalog paths;
- excluded leads and the verification condition each failed;
- local benchmark connections found or not found.
