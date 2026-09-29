# S13 — Collect datasets from Cloudera tutorial assets

Read and comply with the repository-level `AGENTS.md` before execution.

## Purpose

Periodically inspect the repository
`https://github.com/jdvelasq/cloudera-tutorial-assets` for datasets attached to
Cloudera tutorials. The repository is a source of discovery, not a guarantee
that every file is reusable. The curriculum identity remains Analytics; platform
technology is only a contributing implementation context.

## Source boundary

- Treat the supplied repository as a fork or access route and identify the
  original provider of every asset independently. Do not infer ownership from
  the fork name.
- The repository is organized by tutorial. A tutorial directory is the review
  unit and its name is the stable subsource identifier.
- Inspect the Git tree, README, data-generation code, license files, and
  first-party tutorial pages. Git LFS pointers or unavailable binaries are not
  evidence of dataset contents.
- Do not copy, download into this repository, or redistribute source data.

## Recurring execution

1. Inspect `catalog/s13-cloudera-tutorial-assets/` to identify tutorial
   directories already reviewed.
2. Enumerate current top-level tutorial directories in the source repository.
3. For every unreviewed tutorial, inspect its documentation and all assets far
   enough to determine dataset contents, analytical case, origin, access, and
   terms. Reinspect a reviewed tutorial only if its source revision or terms
   materially changed.
4. Search all `catalog/` for duplicate datasets by provider, canonical name,
   file identity, and meaningful aliases.
5. Create one YAML per passing dataset at
   `catalog/s13-cloudera-tutorial-assets/<tutorial-slug>/<dataset-slug>.yaml`.
   A passing record must satisfy every condition below:
   - bounded analytical case or decision;
   - concrete data contents and access route;
   - identified original provider;
   - terms sufficient for a later educational-use decision;
   - reproducible relation to the tutorial; and
   - no duplicate canonical record elsewhere in the catalog.
6. If no asset in a reviewed tutorial passes, create only
   `catalog/s13-cloudera-tutorial-assets/<tutorial-slug>/.gitkeep`. A review
   marker is not a dataset record and must never be described as one.

## Special verification rules

- A repository-wide code license does not automatically establish rights for
  embedded datasets. Inspect file-level notices and generator headers.
- Synthetic data may be cataloged only when the generator and its terms permit
  the intended downstream educational use; call it synthetic, not real-world.
- For assets derived from an external provider, record that provider and its
  terms rather than the repository license.
- When a notice requires a separate agreement, is contradictory, or does not
  clearly cover the data, the terms gate fails. Leave only `.gitkeep` and state
  the limitation in the execution report.
- Do not catalog generic platform demonstrations, code-only examples, or data
  that is merely created during execution without an inspectable source.

## Record schema

Each passing YAML uses `type: tutorial_dataset` and includes `book_source`
(renamed only in meaning: source organization, tutorial title, official URL,
and repository path), `dataset`, `associated_cases`, `sources`,
`possible_analytical_questions`, `limitations`, `curricular_signal`,
`benchmark_connections`, and `verification`. Explicitly state synthetic or
real-world status, access route, data terms, and any platform prerequisites.

## Output and report

Write only under `catalog/s13-cloudera-tutorial-assets/`. Report the source
revision and access date, tutorials inspected, files or markers created,
duplicates avoided, datasets excluded at the terms/provenance gate, and any
changes that would warrant a future reinspection.
