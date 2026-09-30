# Project Instructions

## Curriculum identity

This project designs curricula in **Analytics**.

Analytics is the organizing perspective of all curriculum design decisions.

Machine Learning, Statistics, Operations Research and Optimization, Data
Science, Data Engineering, Databases, Business Intelligence, Artificial
Intelligence, and related fields are **contributing disciplines**, not the
curricular identity.

Concepts, methods, techniques, and tools from contributing disciplines must
be selected, scoped, sequenced, and integrated according to their role in
Analytics. Their inclusion must not be driven by the internal curricular
logic or conventional syllabus of the contributing discipline.

The resulting curriculum must not be reasonably characterizable as an
introductory, abbreviated, or repackaged course in Machine Learning,
Statistics, Operations Research, Data Science, Data Engineering, Databases,
Business Intelligence, Artificial Intelligence, or any other contributing
field.

A specialist in any contributing discipline should recognize relevant
elements from that field while also recognizing that those elements serve
a broader Analytics curriculum.

When making major curriculum design decisions, explicitly verify that this
identity has been preserved.

## Python environment

The root-level `requirements.txt` is the single canonical definition of the
Python environment for this repository. Course folders and task folders must
not introduce independent dependency manifests or environment definitions.

Before adding a dependency, verify that it is compatible with the repository's
supported Python version. Reproduce the environment from the root
`requirements.txt`.

## Presential workshops (`Pxxx_`)

This convention applies to **every course**. Within each course
implementation folder, `Pxxx_` directories represent enumerated presential
workshops led by the instructor. They are guided learning experiences: the
instructor presents and discusses the problem, develops the solution
progressively in code, and explains the analytical decisions, alternatives,
and practices to avoid.

`P001`–`P099` are common foundational activities. `P100`–`P199` are reserved
for activities specific to the Descriptive Analytics course. `P500`–`P599`
are reserved for activities specific to the Fundamentos de data para
analítica course. `Pxxx_` directories do not contain a `README.md`. This
convention will be refined as the implementation materials are organized and
audited.

All assessment of a `Pxxx_` workshop uses `pytest`. Students must be able to
run its tests through VS Code's Testing view.

When a course is distributed, its `Pxxx_` directories are copied into a new
repository under `distribution/`; their depth relative to that repository's
root can change. Test discovery and execution must therefore be independent
of the workshop's relative depth. `pytest` must never fail during test
discovery because of the distribution layout.

`Pxxx_` assessment is verified through GitHub Actions in the distributed
course repository.
