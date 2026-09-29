# S01 — Discover and Verify Historical Analytics Cases

## Objective

Build `catalog/historical/` by discovering historically established cases from
Internet sources and documenting only those for which a concrete, usable
dataset can be verified.

The catalog's unit is a **case**: a named historical event, decision, person,
organization, public problem, or analytical episode connected to one or more
datasets and an identifiable analytical question.

This task is catalog construction. It is not curriculum design, activity
construction, assessment design, or audit.

---

## Governing instructions

Read and comply with the repository-level `AGENTS.md` before performing this
task.

Analytics is the curricular identity of the project. Machine Learning,
Statistics, Operations Research and Optimization, Data Science, Data
Engineering, Databases, Business Intelligence, Artificial Intelligence, and
related fields may contribute methods or tools, but must not redefine the
educational identity of the project.

---

## Discovery scope

Search the Internet for historically established cases that can support
Analytics learning and have data suitable for lawful, reproducible classroom
use.

Use named cases as the discovery anchor. Initial examples include:

- the Challenger disaster;
- Florence Nightingale's Crimean War mortality analysis;
- Napoleon's 1812 Russian campaign as represented in historical-data work;
- other named cases discovered through authoritative historical, scientific,
  governmental, archival, university, or research sources.

The examples are seeds, not a closed list and not an instruction to include a
case without qualifying data.

Prioritize cases that make a consequential connection among data, evidence,
uncertainty, interpretation, decision, action, or outcome visible.

---

## Internet research policy

Use the Internet to identify and verify each case and its dataset.

Prefer sources in this order when available:

1. original archives, governments, public institutions, museums, libraries,
   or official statistical agencies;
2. primary research publications and their institutional data repositories;
3. universities, scholarly projects, or recognized open-data repositories;
4. documented package datasets or reproducible research repositories;
5. reputable secondary sources only when they clearly identify and link to the
   underlying data.

Do not treat an unverified tutorial, blog, Kaggle mirror, scraped copy, or
generic GitHub repository as sufficient evidence of data provenance or
permitted use when a stronger source is available.

Record the access date for every Internet source used.

Do not download, copy, redistribute, or store datasets in this repository
during this task. The catalog records availability and terms; it is not a data
warehouse.

---

## Data eligibility gate

Create a case record only when all of the following can be verified:

- the case is historically identifiable and analytically meaningful;
- a specific dataset or documented reconstruction exists;
- the data source and access route are concrete;
- the data can be used for the intended non-commercial educational context, or
  its terms are explicit enough for a later use decision;
- the dataset is materially related to the named case, not merely to the same
  topic, organization, or era;
- the data is sufficiently described to assess reproducibility and limitations.

Do not include a case merely because it is famous, frequently taught, or has a
loosely related public dataset.

If data availability, provenance, license, or relation to the case cannot be
verified, do not create a YAML record. Report the case as an excluded lead in
the final response.

---

## Relationship to local benchmarks

After identifying a case from Internet research, search
`design/benchmarks/` for its canonical name and meaningful aliases.

This lookup documents the relationship between the historical case and the
project's existing benchmark corpus. It does not determine eligibility.

- When the case appears substantively, record each relevant local source and
  locator under `benchmark_connections`.
- When it does not appear, record an empty list and state that no local
  benchmark connection was found during this execution.
- Do not alter benchmark files.

---

## Output location

Create or update one YAML file per verified case:

`catalog/historical/<case-slug>.yaml`

Examples:

- `catalog/historical/challenger-disaster.yaml`
- `catalog/historical/florence-nightingale-crimean-war.yaml`
- `catalog/historical/napoleon-russian-campaign.yaml`

Use lowercase kebab-case slugs. Do not create a consolidated inventory file.

---

## Required case-record structure

Use this structure. Do not omit provenance, data-access, or terms fields.

```yaml
id: historical/<case-slug>
name: <canonical case name>
aliases: []
type: historical_case

historical_context: >
  <concise, sourced description of the event, setting, or episode>

case:
  decision_or_problem: >
    <consequential question, decision, or analytical problem>
  analytical_relevance: >
    <how the case connects data, evidence, interpretation, and action>

datasets:
  - name: <dataset or reconstruction name>
    relationship_to_case: >
      <why this dataset represents the named case>
    source_url: <direct authoritative data or repository URL>
    provider: <provider or steward>
    access_method: <download, API, package dataset, archive, etc.>
    availability: <public, registration required, etc.>
    license_or_terms: <quoted or precisely identified terms>
    access_date: YYYY-MM-DD
    contents: >
      <records, variables, period, and meaningful limitations>

sources:
  - role: historical_context | dataset_provenance | data_terms
    title: <source title>
    url: <source URL>
    access_date: YYYY-MM-DD
    notes: >
      <what this source verifies>

benchmark_connections: []

possible_analytical_questions:
  - <question supported by the verified case and dataset>

curricular_signal:
  analytics_capabilities:
    - <capability evidenced by the case>
  contributing_disciplines:
    - <discipline and its bounded function within Analytics>
  cautions:
    - <historical, ethical, representational, data-quality, or reproducibility limitation>

verification:
  historical_context: verified
  dataset_provenance: verified
  data_access: verified
  data_terms: verified
  benchmark_connection: verified | not_found
```

---

## Execution method

For each candidate:

1. Establish its canonical name, aliases, and historical context from reliable
   sources.
2. Locate a dataset or documented reconstruction that is materially related to
   that case.
3. Verify the dataset's provider, access route, contents, and terms.
4. Reject the candidate if any part of the data eligibility gate fails.
5. Search local benchmarks for the case name and aliases; document substantive
   connections without treating absence as rejection.
6. Describe the analytical problem and questions without inventing facts or
   turning the record into a lesson plan.
7. State limitations plainly, including historical incompleteness,
   reconstruction, aggregation, missing data, or ethical issues.

Avoid duplicate records. If multiple legitimate datasets support the same case,
record them together in the one case YAML and explain their different roles.

---

## Exclusions

Do not include:

- fictional examples;
- generic hypothetical exercises;
- cases without a verifiable dataset or documented reconstruction;
- datasets merely related to an organization or topic but not to the case;
- data with unknown or incompatible terms of use;
- provider marketing anecdotes without independent historical and data support;
- a final course activity, lesson plan, assessment, or syllabus.

---

## Completion condition

The task is complete when every created YAML record:

- represents a named historical case;
- has one or more verified, usable datasets;
- documents data provenance, access, and terms;
- records local benchmark connections when found;
- preserves material limitations;
- leaves benchmark sources unchanged;
- does not select the case for a particular course or module.

## Final response

Report:

- YAML files created or updated;
- verified datasets and their providers;
- local benchmark connections found or not found;
- excluded leads and the exact eligibility condition they failed.
