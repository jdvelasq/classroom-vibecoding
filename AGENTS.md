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

## Course-identity audit questions

Use this ordered sequence when auditing the design or implementation of every
course. The audit evaluates the **terminal analytical product**, not the names
of its techniques, models, or source disciplines.

1. What analytical question does the terminal product answer, and for which
   decision, user, or stakeholder context?
2. What durable product does a successful student create: an explanation of
   what occurred, a prediction with uncertainty, a repeatable decision policy,
   a product capability, or another explicitly justified analytical artifact?
3. Does that product answer the question appropriate to the course's line?
   - Descriptive: what is occurring, for whom, where, when, and with what
     evidence?
   - Predictive: what future or unobserved result is estimated, over what
     horizon, and with what uncertainty?
   - Prescriptive: what recurrent action should be taken under which
     objectives, constraints, safeguards, exceptions, and review mechanism?
   - Data products: how is an analytical capability made usable, reliable,
     maintainable, and observable for its users?
4. Are Statistics, ML, OR/Optimization, Data Engineering, Databases, BI, AI,
   or another discipline visibly serving that analytical product, rather than
   supplying the course's organizing logic?
5. Could the course still reasonably be described as an abbreviated,
   introductory, or relabelled course in one contributing discipline? If so,
   identify the missing analytical product, decision connection, or boundary
   and treat the audit as unresolved.

For Prescriptive Analytics, a model, Pareto frontier, simulation result, or
decision tree alone is not a sufficient terminal product. It may support the
design of a policy, but the audit must establish the connection from observable
context to feasible action, including applicable constraints, guardrails,
human authority, and outcome monitoring. Automation is a possible execution
mode; require a stated decision cadence and response need, not an assumption
that every valid policy is instantaneous or fully automated.

## Python environment

The root-level `requirements.txt` is the single canonical definition of the
Python environment for this repository. Course folders and task folders must
not introduce an independent dependency manifest or environment definition.

An activity may retain a local `requirements.txt` only when its execution
contract requires that file at the activity root, for example a Docker build,
a Nox session, or a self-contained repository template used in class. Such a
file is an execution artifact, not a second source of truth: it must declare
only the smallest compatible subset of packages already defined at the root.
Before changing one, verify that every package and version constraint remains
compatible with the root manifest.

Before adding a dependency, verify that it is compatible with the repository's
supported Python version. Reproduce the environment from the root
`requirements.txt`.

## Code clarity

Code in this repository must be clear, pedagogical, and self-explanatory
through its structure and names. Do not add comments or docstrings that merely
describe what the code does. Comments and docstrings are reserved for a
decision, constraint, rationale, or non-obvious limitation that cannot be made
clear in the code itself.

In notebooks, a code cell may begin with a comment when it materially improves
the pedagogical sequence by explaining the reason for that step. Such a comment
must be the first line of the cell and must be followed by a blank line. It is
not required in every cell and must not restate what the code makes clear.
When an activity addresses a genuine analytical question, the first notebook
cell should begin by stating that question explicitly when it gives the student
a useful analytical frame. Do not force this pattern onto purely technical
activities that do not have a meaningful analytical question.
Blank lines within a notebook cell may separate conceptually distinct elements
or key stages of a process when that improves readability; they must not be
added mechanically to otherwise cohesive code.

Notebook cells and Python files may include concise text diagrams when they
materially clarify a relationship, structure, or process for the reader. Use
them selectively as explanatory comments, not as decoration or a substitute
for clear code.

Every instructor notebook must include visual evidence cells whenever a visual
inspection materially helps students understand or verify a transformation,
assumption, input condition, intermediate result, model behavior, or final
output. Examples include a focused table, a sorted sample, a matrix view, a
plot, or another rendered artifact. These cells are part of the pedagogical
sequence: they make the evidence visible before the next analytical decision.
Choose the smallest useful visual and do not add decorative displays.

## Case and dataset provenance

Prefer an existing, traceable dataset available in `datalabs/`, documented in
`catalog/`, or provided through DataCamp when designing or revising a workshop.
`datalabs/` is a primary course source under the instructor's control. Reuse a
suitable case across a pedagogical sequence when it strengthens continuity. Do
not introduce fictitious or newly generated source data merely for convenience
when a suitable existing case is available.

Derived teaching artifacts, such as a deliberately scoped extract or a
normalized representation of a source, are permitted when their origin,
transformation, and limitations are documented. Preserve known provenance,
access, redistribution, and classroom-use restrictions with the activity.
Synthetic data is an exception: use it only when the learning objective
requires a controlled simulation that a real source cannot support, and state
that limitation explicitly.

## Presential workshops (`Pxxx_`)

This convention applies to **every course**. Within each course
implementation folder, `Pxxx_` directories represent enumerated presential
workshops led by the instructor. They are guided learning experiences: the
instructor presents and discusses the problem, develops the solution
progressively in code, and explains the analytical decisions, alternatives,
and practices to avoid.

Activity identifiers are scoped to their parent implementation folder: the
same `Pxxx` may exist in different folders when it identifies distinct
activities. References to an activity outside its own course folder must use
a path-qualified identifier such as `common/P100` to remain unambiguous.
`P001` is the universal common activity. Within course folders, `P100`–`P199`
are reserved for activities specific to Descriptive Analytics and `P500`–
`P599` for Fundamentos de data para analítica. `Pxxx_` directories do not
contain a `README.md`. This convention will be refined as the implementation
materials are organized and audited.

All assessment of a `Pxxx_` workshop uses `pytest`. Students must be able to
run its tests through VS Code's Testing view.

`tests/test_activity.py` evaluates participation in the guided activity, not
software correctness. Its checks should be proportionate to that purpose,
normally verifying the expected persistent artifacts in `submission/` rather
than reimplementing or exhaustively testing the student's solution.

When a course is distributed, its `Pxxx_` directories are copied into a new
repository under `distribution/`; their depth relative to that repository's
root can change. Test discovery and execution must therefore be independent
of the workshop's relative depth. `pytest` must never fail during test
discovery because of the distribution layout.

`Pxxx_` assessment is verified through GitHub Actions in the distributed
course repository.

Whenever a particular `Pxxx_` activity is inspected, designed, modified, or
approved, review its course-level `traceability.yaml` entry as part of that
activity's audit. Confirm that the mapped capabilities reflect the evidence in
the activity; do not defer this review to a later course-level audit.
