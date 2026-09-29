# S14 — Collect datasets from Hortonworks HDP assets

Read and comply with the repository-level `AGENTS.md` before execution.

## Purpose

Periodically inspect `https://github.com/jdvelasq/hortonworks-hdp` for datasets
and bounded analytical cases used by Hortonworks HDP materials. The repository
is discovery provenance, not proof that every included asset is reusable.
Analytics remains the curricular identity; Hadoop-platform implementation is a
contributing context only.

## Source and review unit

- Inspect the repository tree, README files, tutorial documentation,
  file-level notices, generators, and first-party asset sources.
- Treat each top-level tutorial, workshop, or otherwise documented asset group
  as one review unit. Identify the original data provider independently of the
  repository or fork owner.
- Do not copy, download into this repository, or redistribute external data.
  Git LFS pointers and unavailable binaries do not verify data contents.

## Recurring execution

1. Inspect `catalog/s14-hortonworks-hdp/` to find reviewed units.
2. Enumerate source units and inspect every unreviewed unit; re-evaluate one
   only when its source revision, assets, or terms materially change.
3. For each candidate, verify a bounded Analytics case, concrete contents and
   access route, original provider, reproducible tutorial relation, and terms
   sufficient for a later educational-use decision.
4. Search all `catalog/` for duplicates by canonical dataset, provider,
   aliases, and source identifiers.
5. Create one passing record per dataset at
   `catalog/s14-hortonworks-hdp/<unit-slug>/<dataset-slug>.yaml`, using
   `type: tutorial_dataset`. Each record must include `book_source` (as
   source organization, tutorial identity, official URL, and repository path),
   `dataset`, `associated_cases`, `sources`, `possible_analytical_questions`,
   `limitations`, `curricular_signal`, `benchmark_connections`, and
   `verification`.
6. Where a reviewed unit has no passing dataset, create only
   `catalog/s14-hortonworks-hdp/<unit-slug>/.gitkeep`.

## Verification rules

- A repository or code license does not by itself establish rights for data.
- Synthetic data is eligible only when the generator and its terms clearly
  permit educational use; identify it as synthetic.
- For external data, document its original provider and terms, not merely the
  repository license.
- If notices require a separate agreement, conflict, or do not clearly cover
  data, the terms gate fails. Do not create a YAML record.
- Exclude generic platform demonstrations, code-only examples, toy data, and
  unverified claims.

## Report

Report revision and access date, units inspected, records or markers created,
duplicates avoided, excluded candidates and their failed gates, and source
changes requiring reinspection.
