# S02 — Collect Historical Cases from HistData

Read and comply with the repository-level `AGENTS.md` and `catalog/README.md` before execution.

## Objective

Use the **HistData** project as a defined discovery source to identify and
verify additional historical cases for `catalog/s02-histdata/`.

HistData is an external source, not the catalog's output. The output of this
task is one updated or new case record per qualifying case; it is never a
parallel inventory of HistData datasets, package files, or book chapters.

This task is catalog construction. It is not curriculum design, activity
construction, assessment design, or audit.

---

## Governing instructions

Read and comply with the repository-level `AGENTS.md` before performing this
task.

Analytics is the curricular identity of the project. Statistical, visual,
computational, spatial, or other methods revealed by HistData are contributing
capabilities in service of Analytics; do not turn the catalog into a syllabus
for any one discipline.

---

## Source boundary

Inspect the current HistData package and its accompanying documentation:

- package landing page: `https://CRAN.R-project.org/package=HistData`;
- project site: `https://friendly.github.io/HistData/`;
- current reference manual and dataset documentation linked from those sources.

HistData describes itself as a collection of datasets from the history of
statistics and data visualization, intended for instructional use and
historical research. Treat each included dataset as a **lead**, not as an
automatic catalog entry.

Do not download, copy, redistribute, or store HistData datasets in this
repository. Record access and terms only.

---

## Candidate selection

Review the HistData dataset index and identify candidates that represent a
named, historically identifiable event, decision, person, organization, public
problem, or analytical episode. Prioritize cases where data, evidence,
interpretation, and action or consequence are materially connected.

Do not create case records for:

- unnamed measurements or generic historical series without a bounded case;
- datasets whose relation to a named case cannot be established;
- duplicate representations of a case already recorded under another name;
- cases without sufficiently documented provenance, access, and terms.

Examples of already cataloged cases that may appear in HistData include Florence
Nightingale's Crimean War mortality analysis, Minard's representation of
Napoleon's Russian campaign, and John Snow's Broad Street cholera
investigation. Locate their existing YAML records first; update them only when
HistData adds material provenance, access, contents, or limitation information.

---

## Verification gate

For every candidate, verify all of the following before creating or updating a
record:

- a specific named historical case exists;
- the HistData dataset is materially related to that case;
- the current package documentation identifies dataset contents and provenance;
- public access is concrete through CRAN or the documented project route;
- HistData's GPL-2 | GPL-3 package terms are recorded precisely enough for a
  later educational-use decision;
- the data's reconstruction, aggregation, omission, and interpretation limits
  can be described.

Reject candidates that fail any condition. A historically interesting dataset
is not enough when it lacks a bounded case or clear provenance.

---

## Required output

For each qualifying case, create or update exactly one file:

`catalog/s02-histdata/<case-slug>.yaml`

Use the case-record structure defined by
`catalog/tasks/s01-collect-historical-cases.md`. In addition:

- preserve the existing canonical name and `id` when updating a record;
- add HistData as a dataset or provenance source when it materially improves
  the record;
- record the version or access date used when the documentation exposes it;
- do not overwrite a stronger primary or institutional source with HistData;
- search `design/benchmarks/` for the canonical name and meaningful aliases;
  record substantive connections or explicitly preserve `not_found`.

Do not create a file for the HistData package itself, its companion book, or
the Milestones Project. They are discovery sources, not cases.

---

## Execution method

1. Read the current HistData dataset index and package terms.
2. Compare its named cases with `catalog/s02-histdata/` to identify additions,
   updates, aliases, and possible duplicates.
3. For each candidate, verify historical context, dataset provenance, access,
   terms, contents, and limitations from HistData documentation and stronger
   sources where needed.
4. Apply the verification gate; create or update only qualifying case YAMLs.
5. Search local benchmarks by canonical name and aliases without editing them.
6. Validate every changed YAML file.

---

## Completion condition

The task is complete when every changed case record remains a named historical
case with verifiable data and terms, avoids duplicates, identifies HistData's
role accurately, preserves limitations, and documents the local benchmark
lookup.

## Final response

Report:

- cases created and cases updated;
- HistData datasets used and the version/access date consulted;
- duplicates intentionally avoided;
- local benchmark connections found or not found;
- excluded leads and the exact gate they failed.
