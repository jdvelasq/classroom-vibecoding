# S15 — Collect datasets from datalabs

Read and comply with the repository-level `AGENTS.md` and `catalog/README.md`
before execution.

## Purpose

Periodically inspect `https://github.com/jdvelasq/datalabs` for datasets that
can support bounded Analytics activities in the course owner's private
classroom. The repository is a collection and discovery source: its ownership
does not, by itself, establish the original dataset's provenance, license, or
redistribution rights. Analytics remains the curricular identity; methods and
tools from contributing disciplines serve the analytical question.

## Source and review unit

- Inspect the repository tree, file names, accompanying documentation, commit
  history when useful, embedded metadata, and identifiable first-party sources.
- Treat each top-level thematic directory as a review unit (for example,
  `commerce/`, `energy/`, `health/`, or `transport/`). Review individual files
  within the unit as separate dataset candidates.
- A source folder is a provenance lead, not a reason to assume that all of its
  files share a provider, license, intended use, or real-world status.
- Do not copy, transform, package, or redistribute source data in this
  repository. The catalog stores selection metadata only.

## Recurring execution

1. Inspect `catalog/s15-datalabs/` to identify thematic units and dataset
   files already reviewed.
2. Enumerate the current top-level thematic directories in the source
   repository. Review one or more unreviewed units per run, prioritizing
   datasets with an identifiable provider, practical decision context, and
   documentation. Continue later runs until the source is covered.
3. For each file candidate, establish its concrete contents and grain, access
   route, original provider, terms, real-world or synthetic status, and a
   bounded Analytics case or decision it can support.
4. Search all `catalog/` for duplicates by canonical dataset identity,
   provider, aliases, file identity, and source URL. Do not create a second
   record merely because the same data appears under a new folder or format.
5. Create one passing dataset record at
   `catalog/s15-datalabs/<thematic-unit>/<dataset-slug>.yaml`, using
   `type: repository_dataset`. Each record must include `book_source` (used
   here for repository identity and path), `dataset`, `associated_cases`,
   `sources`, `possible_analytical_questions`, `limitations`,
   `curricular_signal`, `benchmark_connections`, and `verification`.
6. If a reviewed thematic unit has no eligible dataset, create only
   `catalog/s15-datalabs/<thematic-unit>/.gitkeep`. This is a review marker,
   not a dataset record.
7. When a useful, bounded candidate has conditional or incomplete terms but
   its contents, access route, and case are documented, it may be retained for
   the course owner's **private classroom use** with
   `dataset.status: private_class_candidate`. State the condition and the
   non-redistribution limit explicitly. Do not label it `selection_ready` or
   imply permission beyond that intended private use.

## Verification rules

- The repository owner or a commit author is not automatically the original
  data provider. Identify the provider and terms independently whenever
  possible.
- Preserve file-specific terms; do not infer them from another file in the
  same thematic folder.
- If a dataset is generated, identify the generator, its inputs, and whether
  it is synthetic or derived from an external source.
- Exclude code-only artifacts, generic demonstration files, files with no
  inspectable contents, and datasets without a defensible analytical case.
- If original provenance cannot be established, the normal terms gate fails.
  Retain a record only through the private-class exception above; otherwise
  use a `.gitkeep` review marker.

## Report

Report source revision and access date, units and files inspected, records or
markers created, duplicates avoided, excluded candidates and failed gates,
and source changes that require reinspection.
