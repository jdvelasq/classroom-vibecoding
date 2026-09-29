# S03 — Collect Selectable Datasets from Manning

## Objective

Inspect Manning books and their documented companion repositories to identify,
verify, and record datasets together with their associated analytical cases,
so a later course designer can select a suitable dataset-case combination.

This task is catalog construction. It is not curriculum design, activity
construction, assessment design, or audit.

The catalog unit for this publisher is a dataset. A newly found Manning book
is not itself a dataset output: continue into its documented companion material
until every accessible dataset either passes the verification gate and yields
one dataset YAML, or is reported as excluded with the unmet condition.

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

## Automatic review scope

Establish the review scope yourself on every run; do not ask the user to supply
a category, URL, or cutoff date. The stable publisher boundary for this task is
the current first-party **Data Analysis** subject subtree, beginning at
`https://www.manning.com/catalog/data-science/data-analysis/data-analysis`.
Enumerate every page of that listing and every child category it links as a
Data Analysis category (for example, Data Analytics, Data Analysis and
Business Intelligence, Data Manipulation and Analysis, Data Presentations and
Visualizations, Feature Engineering, Optimization and Experimentation, or
Time Series Analysis when present). Follow cross-listings only once per
book/edition.

Do **not** expand the scope to the parent Data Science catalog, to AI, ML,
Databases, or Statistics catalogs merely because they overlap with Analytics.
Those catalogs are too broad to be an exhaustible publisher-collection run.
Their material can enter the catalog only through its own future source task or
when a qualifying Data Analysis book explicitly links it as companion data.

For each enumerated book page, apply this two-stage filter automatically:

1. Treat it as an *eligible lead* only when the official description identifies
   a named analytical problem, case study, project, or book-specific companion
   data that could meet this task's verification gate.
2. Exclude at discovery stage a title whose official description supports only
   generic API, language, framework, library, or technique instruction and no
   bounded analytical case. Record its title and that exact exclusion reason in
   the final response; do not create a YAML merely to log it.

Do not reject an eligible lead merely because it also uses AI, ML, programming,
or another contributing discipline; those labels do not redefine the
curriculum.

Record in the final response the root and child catalog URLs, pagination
status, discovered categories, filtering rationale, and access date. That
automatically established Data Analysis subtree is the review scope for the
run. If a listing or its pagination cannot be enumerated, the run is
**partial** and must name that unresolved listing. It must not ask the user to
choose a scope as a substitute for this work.

---

## Autonomous execution loop

Execute the full collection loop in one run. Do not ask the user to choose a
book, approve a candidate, provide the next URL, or tell you to continue.

For every newly discovered book, in the same execution:

1. inspect the official book page and every documented companion source;
2. enumerate its accessible datasets and associated analytical cases;
3. create one dataset YAML for each dataset that passes the verification gate;
4. create `.gitkeep` when no dataset passes; and
5. audit the new files before moving to the next book.

Continue until every book newly discovered in the automatic publisher search is
represented by either at least one dataset YAML or `.gitkeep`. Only then return
the final report. A source that cannot be reached is an explicit partial result,
not a reason to delegate the next step to the user.

---

## Periodic collection behavior

This task is intended to be run repeatedly. The existing book directories in
`catalog/manning/` are the persistent local record of reviewed Manning books.

- A reviewed book with one or more usable datasets contains one YAML per
  dataset.
- A reviewed book with no usable dataset contains only `.gitkeep`.
- Do not add `book.yaml`, a publisher inventory, a review ledger, a case-only
  YAML, or any other placeholder.

The absence of a book directory means the book has not yet been reviewed and
must be reviewed when it is discovered in the automatic publisher search.

At the start of a run, audit existing YAMLs. A record counts toward this
contract only when `type: book_dataset` and the required `dataset` and
`associated_cases` fields are present. Treat older case-oriented YAMLs as
legacy inputs: migrate them only when their recorded evidence supports the
dataset contract; otherwise re-review the book. Do not let a legacy YAML cause
a book to be skipped as already reviewed.

The directory and prior records are optional. If `catalog/manning/` does not
exist or contains no dataset records, this is the first collection: establish
the baseline from current Manning sources and create a book directory after its
review, using `.gitkeep` when no dataset passes the verification gate.

At the start of every execution:

1. Inspect the existing Manning book directories and dataset records, including
   their editions and access dates.
2. Build the automatic review scope from the first-party Data Analysis subtree
   and all of its applicable pages, as specified above.
3. Compare every eligible lead in that scope with local book directories,
   identifying books not yet reviewed, new editions, and materially revised
   companions.
4. For every new or revised book, locate its companion sources and enumerate
   every distinct accessible dataset. Record each passing dataset; create
   `.gitkeep` when no dataset passes.

A newer book, edition, dataset revision, or better-documented case may be a
potential successor to an existing case, but it must be added as a separate
record. Never delete, overwrite, or silently replace the earlier record. Make
the possible relationship visible in the new record and final report so that a
later course-design decision can choose between them.

If no qualifying material is found during a run, leave the existing catalog
unchanged and report the sources searched and the date of the review.

---

## Exhaustive-completion rule

Do not stop after finding the first qualifying dataset. A run may report the
Manning review as **complete** only after it has exhausted the documented search
scope available on the access date:

1. Enumerate the books and editions in the automatically established
   first-party review scope, including every applicable category and pagination
   page.
2. Compare that set with the book directories already represented under
   `catalog/manning/` and identify books not yet represented, newer editions,
   and revised companions.
3. For every eligible book, including one already represented by a directory,
   inspect the documented companion material far enough to enumerate its named
   projects or cases with concrete data.
4. Classify every candidate as a created dataset record, an existing
   cross-source dataset, or an excluded lead with the exact unmet verification
   condition.

Completion is a bounded claim about the automatically established Manning
listing(s) at the review date; it is not a claim that every Manning book ever
published has been found.
If a catalog page, companion source, or candidate cannot be inspected, report
the run as **partial**, name the unreviewed scope, and do not say Manning has
been exhausted.

The final response must list reviewed books and editions, all created dataset
files and `.gitkeep` directories, duplicates, exclusions, and any unreviewed
or inaccessible material. No
book-level YAML, publisher inventory, or placeholder file may be created to
record that coverage.

---

## Output structure

For a verified dataset discovered through a Manning book, create one YAML
record under:

`catalog/manning/<book-slug>/<dataset-slug>.yaml`

The publisher and book path record **where the dataset was discovered**. It
does not imply that Manning owns the dataset or its associated real-world case.

Each record must identify:

- the Manning book, edition when available, official page, and access date;
- every book-specific repository or companion source used;
- the dataset name, data source, access route, contents, and license or terms;
- every named case or analytical setting associated with that dataset;
- concise analytical problems, limitations, and possible analytical questions;
- any substantive connection to `design/benchmarks/`.

Use one YAML per dataset, never separate dataset and problem records.

---

## Duplicate rule

Before creating a dataset record, search all of `catalog/` by dataset name,
aliases, and meaningful source identifiers.

- If no equivalent dataset exists, create the Manning-path YAML record.
- If the same underlying dataset already exists, create a Manning-path record
  only when the book-specific association adds selection-relevant information;
  cross-link the existing record in `sources`.
- Do not move, rename, or overwrite existing dataset records during this task.

This rule preserves the dataset as the catalog unit while retaining its
book-specific discovery route and associated cases.

---

## Verification gate

Create a record only when all of the following are verified:

- a concrete web-accessible dataset or documented reconstruction is identifiable;
- one or more associated cases, decisions, or analytical questions are materially
  related to it;
- dataset provider, access route, and contents are concrete;
- data terms are explicit enough for a later educational-use decision;
- the book or documented companion source establishes the Manning connection;
- provenance, reproducibility, and material limitations can be described.

Exclude generic code examples, tool-library samples, anonymous exercises,
marketing anecdotes, and datasets whose access, terms, or book connection
cannot be verified.

---

## Required record contents

Use a dataset-record structure with `book_source`, one `dataset` block, and an
`associated_cases` list. The record must include the following fields:

```yaml
id: manning/<book-slug>/<dataset-slug>
name: <dataset name>
aliases: []
type: book_dataset
book_source: {}
dataset:
  source_url: <direct data, API, archive, or companion-data URL>
  provider: <provider or steward>
  access_method: <how to obtain it>
  availability: <public, registration required, etc.>
  license_or_terms: <identified terms>
  contents: <variables, period, and grain>
  status: real_world | book_curated | simulated | documented_reconstruction
associated_cases: []
possible_analytical_questions: []
limitations: []
curricular_signal: {}
benchmark_connections: []
benchmark_connection_notes: <result of local lookup>
sources: []
verification: {}
```

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

Record original dataset provenance in `dataset` and `sources`.
An author repository is not sufficient evidence of data provenance unless it
identifies and supports that provenance.

---

## Execution method

1. Identify a current Manning book and its official page.
2. Compare it with the books and editions already represented in
   `catalog/manning/`, and determine whether it is newly discovered, a new
   edition, or an update to a previously considered source.
3. Locate documented book-specific companion materials and repositories.
4. Inspect those materials to identify every distinct concrete dataset and its
   associated analytical case or setting; do not stop at the repository landing
   page.
5. Apply the duplicate search to each candidate dataset.
6. Verify dataset provenance, access, terms, contents, associated cases, and
   limitations from the strongest available sources.
7. Create one YAML for every qualifying dataset, or `.gitkeep` if none qualify.
8. Search `design/benchmarks/` for substantive dataset-case connections without
   editing benchmark files.
9. Validate all YAML files created or updated.

---

## Completion condition

The task is complete when every newly discovered book has a directory, every
usable dataset has its own verified YAML, every non-usable reviewed book has
only `.gitkeep`, and each dataset record has a traceable associated case,
access route, terms, limitations, and local benchmark lookup.

## Final response

Report:

- Manning books and companion sources inspected;
- new or revised books and editions found since the prior local collection;
- dataset YAML records and `.gitkeep` directories created or updated;
- duplicates intentionally not created, with their existing catalog paths;
- excluded books or datasets and the verification condition each failed;
- local benchmark connections found or not found.
