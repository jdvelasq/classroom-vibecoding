# Shared protocol — periodic publisher case collection

This protocol is used by the publisher-specific `s0?-collect-*-cases.md`
tasks. Read the named task first, then apply this protocol.

## Purpose

Periodically extend a publisher's portion of the case catalog. Existing records
under `catalog/<publisher>/` are the local record of books, editions, and cases
already considered; they are a baseline, not a complete representation of the
publisher's current or historical catalog.

The publisher directory and prior records are optional. If
`catalog/<publisher>/` does not yet exist or contains no case records, treat the
run as the first collection. Do not create placeholder **case** files or infer
prior coverage from an absent directory.

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
4. Create or update `<book-slug>/book.yaml` for every identified book or edition
   considered in the run, including its publisher identity, official page,
   documented companion sources, review date, and collection status.
5. Identify candidate cases and apply the source-specific task's verification
   gate.
6. Add only qualifying, nonduplicate case records.

If a later book, edition, dataset revision, or better-documented case might
supersede an existing case, add it separately and report the relationship.
Never delete, overwrite, or silently replace an existing case; course design
will later decide which case to select.

If a reviewed book has no qualifying case, retain its `book.yaml` with a status
such as `no_qualifying_cases_found` or `candidates_pending_case_audit`, plus a
concise reason. This records collection coverage without representing the book
as a case.

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

Every considered book additionally has
`catalog/<publisher>/<book-slug>/book.yaml`. This is a source-discovery record,
not a case record. It must state the edition, official and companion sources,
review date, collection status, and whether individual case data remain pending
audit.

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

## Final response

Report books and editions inspected; new or revised publications found;
companion-package decisions; records created; legacy entries removed; duplicates
not created; excluded leads and failed gates; and benchmark connections.
