# S11 — Collect Cases from OTexts

Read and comply with the repository-level `AGENTS.md` before execution.

The catalog unit is the **case**. Do not create book-level inventory YAML files,
publisher inventories, or placeholder records in `catalog/`; a book discovered
during a run is evidence to investigate, not a catalog record.

## Purpose

Periodically extend a publisher's portion of the case catalog. Existing records
under `catalog/<publisher>/` are the local record of books, editions, and cases
already considered; they are a baseline, not a complete representation of the
publisher's current or historical catalog.

The publisher directory and prior records are optional. If
`catalog/<publisher>/` does not yet exist or contains no case records, treat the
run as the first collection: create the directory only when at least one case
passes verification. Do not create placeholder case files or infer prior
coverage from an absent directory.

This is catalog construction, not curriculum design, activity construction,
assessment design, or audit. Analytics remains the curriculum's organizing
identity; methods and tools have only bounded contributions to an Analytics
case.

## Recurring execution

1. Inspect the existing publisher directory, if any, plus represented book
   editions and access dates. If it is absent, establish the baseline from the
   current first-party catalog instead.
2. Search first-party publisher listings and documented book pages for books or
   editions that are newer than the represented material, and for eligible older
   books not yet represented.
3. Locate each book's documented companion materials.
4. Inspect the companion materials far enough to identify a named project,
   analytical problem, and concrete associated data; book marketing copy alone
   is not a candidate case.
5. Apply the source-specific verification gate to each such candidate.
6. Add only qualifying, nonduplicate case records.

If a later book, edition, dataset revision, or better-documented case might
supersede an existing case, add it separately and report the relationship.
Never delete, overwrite, or silently replace an existing case; course design
will later decide which case to select.

If a run finds no qualifying material, leave the catalog unchanged and report
the sources searched and review date.

Do not report a discovered book as a catalog addition. A successful collection
adds one or more case YAML records; a run that produces none must plainly report
that no verified case was found and why each leading candidate failed.

## Source and data boundary

Record the publisher/book path as discovery provenance only. It does not mean
the publisher owns the event or data.

General-purpose libraries and tools are separate catalog source categories. A
case using data supplied only by pandas, scikit-learn, Keras, tidymodels, or a
similar tool must not be cataloged under a publisher merely because a book uses
it. A package counts as a book companion only if reliable documentation
explicitly ties it to that book and states it provides that book's data or
examples. In every case, trace original data provenance and terms separately.

Do not download, copy, redistribute, or store datasets, code, or book content
in this repository. Record provenance, access, terms, contents, and material
limitations only.

## Case and duplicate rules

Create one YAML file per verified case at
`catalog/<publisher>/<book-slug>/<case-slug>.yaml`.

There is no `book.yaml`: the book path is only a provenance container for its
case files.

Before creating it, search all of `catalog/` by canonical name, aliases,
dataset name, and meaningful source identifiers. Do not duplicate a case merely
because it occurs in another book; report the cross-source link instead.

Create a record only if a named bounded case, concrete associated dataset or
documented reconstruction, original provider, access route, terms sufficient
for a later educational-use decision, book connection, reproducibility, and
limitations can all be verified. Exclude generic code examples, toy datasets,
anonymous exercises, and unverifiable source or data claims.

Each record must contain the book identity and edition, official page,
book-specific companion sources, case identity, original data provenance,
access, terms, limitations, possible Analytics questions, and benchmark lookup.

When a record is migrated from `catalog/case-inventory.yaml`, remove every
legacy entry it covers only after validating the new YAML. Keep covered legacy
names as aliases when a record consolidates them.


## Source scope

Treat **OTexts** as the publisher source and each identifiable OTexts book as a
distinct subsource. Inspect `catalog/s11-otexts/` first, then use first-party book
pages and documented book-specific repositories or packages to find absent
books and recent editions.

## Output

Create only verified, nonduplicate records at:

`catalog/s11-otexts/<book-slug>/<case-slug>.yaml`

Use `book_source.publisher: OTexts`. Open publication does not by itself
establish the terms or original provenance of an included dataset; document both
separately.

---

## Final response

Report books and editions inspected; new or revised publications found;
companion-package decisions; records created; legacy entries removed; duplicates
not created; excluded leads and failed gates; and benchmark connections.

---

## Authoritative dataset-collection contract

This section supersedes every earlier case-oriented, multi-book, inventory, or
legacy-migration instruction. The catalog unit is a **dataset**, not a case.
Automatically enumerate current first-party OTexts listings and documented book
pages; retain published Analytics-relevant books with a bounded analytical case
or book-specific data lead, excluding prepublication and generic tool-only
titles. Do not ask the user to choose scope, URL, or book.

Sort eligible books without `catalog/s11-otexts/<book-slug>/` by official
publication date descending, then title, and process **exactly one**. Its
directory marks that book reviewed, including when legacy YAMLs are present.
Inspect all documented companion material. Create one `type: book_dataset` YAML
per passing dataset at `catalog/s11-otexts/<book-slug>/<dataset-slug>.yaml`, or
create only `.gitkeep` in that directory when none passes. Never create
`book.yaml`, a review ledger, publisher inventory, case-only YAML, or placeholder.

Each record requires `book_source`, `dataset`, `associated_cases`, `sources`,
`possible_analytical_questions`, `limitations`, `curricular_signal`,
`benchmark_connections`, and `verification`; data provider, access route,
contents, and terms must be concrete. A code license is not evidence of
third-party data rights. Search all `catalog/` for duplicates; cross-link only
when the OTexts association adds selection value. Do not modify legacy records.

Complete only after auditing created YAMLs and exhausting the selected book's
documented companions. Report its files or `.gitkeep`, exclusions, duplicates,
inaccessible sources, scope URLs, and access date.
