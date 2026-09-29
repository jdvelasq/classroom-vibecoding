# S12 — Collect Cases from Memorial University of Newfoundland

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

This is an **institutional source**, not a commercial publisher. Treat Memorial
University of Newfoundland and each identifiable course or book as distinct
subsources. Inspect `catalog/memorial-university-newfoundland/` first, then use
official institutional pages and documented course repositories to find absent
or revised materials.

## Exhaustive-completion rule

Do not stop after finding the first qualifying case. A run may report this
publisher review as **complete** only after it has exhausted the documented
search scope available on the access date:

1. Enumerate the relevant books and editions in the publisher's current
   first-party catalog, including pagination or category listings where used.
2. Compare that set with the book paths already represented under the
   publisher's `catalog/` directory and identify absent books and newer
   editions.
3. For every relevant absent or revised book, inspect the documented companion
   material far enough to enumerate its named projects or cases with concrete
   data.
4. Classify every candidate as a created case record, an existing cross-source
   duplicate, or an excluded lead with the exact unmet verification condition.

Completion is a bounded claim about that documented publisher catalog at the
review date; it is not a claim that every book ever published by the source has
been found. If a catalog page, companion source, or candidate cannot be
inspected, report the run as **partial**, name the unreviewed scope, and do not
say the publisher has been exhausted.

The final response must list the reviewed books and editions, all created case
files, duplicates, exclusions, and any unreviewed or inaccessible material. No
book-level YAML, publisher inventory, or placeholder file may be created to
record that coverage.

---

## Output

Create only verified, nonduplicate records at:

`catalog/memorial-university-newfoundland/<source-slug>/<case-slug>.yaml`

Use an `institutional_source` block rather than asserting a publisher. Verify
the institutional relationship, original data provenance, access, and terms
independently.

---

## Final response

Report books and editions inspected; new or revised publications found;
companion-package decisions; records created; legacy entries removed; duplicates
not created; excluded leads and failed gates; and benchmark connections.
