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

## Presential workshops (`PRE_*`)

Within each course implementation folder, `PRE_*` directories represent
enumerated presential workshops led by the instructor. They are guided
learning experiences: the instructor presents and discusses the problem,
develops the solution progressively in code, and explains the analytical
decisions, alternatives, and practices to avoid.

`PRE_*` directories do not contain a `README.md`. This convention will be
refined as the implementation materials are organized and audited.
