# S05 — Design the content of the Analytics courses

Read and comply with the repository-level `AGENTS.md` before execution.

## Objective

Generate auditable course-content design documents by translating the
evidence-backed capabilities and boundaries in
`design/synthesis/s04-synthesis.md` into a visible allocation across these six
courses:

- Pregrado: Fundamentos de analítica; Fundamentos de data para analítica.
- Posgrado: Analítica descriptiva y visualización de datos; Analítica
  predictiva; Analítica prescriptiva; Productos de datos.

This is a course-content design task. It determines each course's principal and
recurring responsibility for Analytics capabilities **and translates that
responsibility into a macro-level course promise** stated as “Al finalizar el
curso, el estudiante es capaz de…”. These statements identify integrated
capabilities and their broad content objects, not a detailed inventory of
techniques, algorithms, tools, units, or weeks. It is not a weekly plan, theory
redesign, workshop design, lab design, assessment design, or final
international audit. Its construction must itself be auditable and reproducible
from the declared local inputs.

## Governing constraints

- Analytics is the curricular identity. Statistics, Machine Learning,
  Operations Research/Optimization, Data Science, Data Engineering,
  Databases, Business Intelligence, AI, and related fields contribute only
  when they serve an Analytics capability.
- The two undergraduate courses are optional. They must not be implicit
  prerequisites for any other course.
- Postgraduate courses have no formal prerequisites. They are autonomous in
  purpose and assessment, while students remain responsible for any
  recommended preparation they lack.
- Do not cause autonomy to become wholesale repetition. A capability may recur
  across courses at different depth or function, but only one course should
  normally own its principal development.
- Big Data Analytics is an external course outside this design authority. It
  may be named only as an interface or scale boundary, never designed as a
  hidden component of these six courses.
- Do not infer pedagogical format, contact hours, sequencing, activities,
  assessments, portfolios, tools, or delivery modality from a content
  allocation. Those are separate design stages.

## Source policy

Use these local inputs only:

- `design/synthesis/s04-synthesis.md`, the evidence-backed Analytics
  synthesis; and
- `design/program-context/maestria-en-analitica.pdf`, the current
  institutional programme document.

For the four postgraduate courses, treat the programme document as the primary
internal reference for programme purpose, graduate profile, depth,
research/deepening modalities, and RAP/RAA alignment. Treat S04 as the
disciplinary boundary and cross-course evidence base. For the two optional
undergraduate courses, use S04; do not infer that the master’s programme
document creates a prerequisite. If the sources appear to conflict, preserve
Analytics as the curricular identity and record the tension rather than
silently resolving it.

Do not conduct external research and do not modify the benchmark corpus or
S01--S04 outputs.

Every allocation in the map must be traceable to a finding or constraint in
the synthesis. Preserve a decision log inside the output: state the source
sections consulted, the allocation rule used, and any interpretation or
unresolved tension. A future executor must be able to rerun the task from the
same local input and determine why a capability was assigned to a course.

## Course-identity audit rule

For each course document, apply the ordered course-identity audit questions in
the repository-level `AGENTS.md`. Record the terminal analytical product and
the specific line question it answers. Do not treat a course title or a list
of contributing techniques as evidence that its Analytics identity has been
preserved.

For Prescriptive Analytics, distinguish a policy for a recurrent decision from
a one-off analytical aid. Optimization, simulation, decision trees,
multicriteria analysis, and predictive estimates may contribute to policy
design or validation; they do not independently define the course's terminal
product. Its distinctive terminal product is a governed, computable policy:
observable context and data → feasible action under objectives, constraints,
and safeguards → execution or accountable human approval → recorded outcomes,
monitoring, and revision. State a decision cadence and response need without
assuming that every policy is instantaneous or fully automated. Keep policy
design and validation in Prescriptive Analytics; defer general product
engineering, deployment infrastructure, and maintenance architecture to
Productos de datos.

For Productos de datos, make its implementation identity explicit: it is the
DataOps/MLOps line of the Analytics curriculum. Its terminal product is an
analytical capability made reproducible, testable, deployable, observable,
secure, recoverable, and governable for its intended users. It operates a
descriptive, predictive, or prescriptive capability; it does not repeat the
analysis, prediction, or policy design that originated that capability. Treat
DataOps/MLOps practices as functional means to sustain Analytics, not as a
generic course in software engineering, enterprise Data Engineering, cloud
platforms, or a vendor toolchain.

## Required output

Create exactly these six files in `design/synthesis/`:

- `s05-diseno-fundamentos.md`
- `s05-diseno-data.md`
- `s05-diseno-descriptiva.md`
- `s05-diseno-predictiva.md`
- `s05-diseno-prescriptiva.md`
- `s05-diseno-productos.md`

Each file is a **course-content design document** and must include:

1. `# Diseño de contenido: <nombre del curso>`;
2. purpose and scope boundaries;
3. for postgraduate courses, an explicit **entry-profile boundary** grounded in
   the programme document: what heterogeneous professional trajectories are
   admitted, what equivalent preparation may be expected, and how institutional
   leveling differs from a prerequisite among these six courses;
4. the applicable map-ready Analytics capabilities derived from the
   synthesis, with contributing disciplines described only functionally;
5. a section headed **“Al finalizar el curso, el estudiante es capaz de…”**
   containing a concise set of macro-level, integrated capability statements.
   Each statement must identify its broad content object and cite the relevant
   S04 finding identifiers. Do not decompose these statements into detailed
   algorithm, software, activity, unit, or week inventories;
6. the course's responsibility for each applicable capability, using explicit
   labels for principal, recurring, contextual, and out-of-scope treatment;
7. a profile of that course, including its distinctive content responsibility
   and what it deliberately does not own;
8. explicit content boundaries and unresolved scope decisions; and
9. an audit-readiness boundary identifying what the document can support and what
   remains pending until later design stages; and
10. a construction record containing: task identifier, course identifier, and execution date;
   exact local input path; source revision or content fingerprint when
   available; capability-allocation rules; section-level traceability to the
   synthesis; unresolved decisions; and the result of the quality checks.
11. a concise **course-identity audit** recording the terminal analytical
    product, the applicable line question from `AGENTS.md`, the contributing
    disciplines used functionally, and any unresolved risk of disciplinary
    relabelling.

## Bidirectional audit traceability

Assign every content allocation a stable course identifier, formatted
`<course-id>.CNN` (for example, `predictiva.C04`). For every allocation,
record its role, the exact stable finding identifier from S04, and the
rationale for the allocation. Do not use section-level citations alone when a
stable S04 finding identifier is available.

Each course document must contain both:

1. a **forward traceability table**: course-content identifier → role → S04
   finding identifier → allocation rationale; and
2. a **reverse traceability table**: applicable S04 finding identifier → one
   or more course-content identifiers in that course.

The execution must also produce, within each construction record, the complete
set of S04 finding identifiers considered, the subset allocated to that course,
and the reason any remaining finding is not applicable to that course.

On a later execution against a different S04 fingerprint, record an explicit
change log of added, removed, or reassigned course-content identifiers. The
documents are derived outputs: regenerate them from S04 rather than manually
merging historical allocations.

## Quality checks

Before completion, verify that:

- the six files collectively give every capability from the consolidated
  synthesis a visible home;
- no course is made a prerequisite by implication;
- no contributing discipline becomes a course-organizing identity;
- each course names a clear macro-level final capability rather than only
  generic labels or roles;
- the course-identity audit identifies a terminal analytical product and does
  not infer identity from course titles or technique inventories;
- detailed techniques, tools, activities, units, and weeks remain deferred;
- optional undergraduate courses are not assumed by postgraduate courses;
- the map does not claim that any course already earns a 10/10 audit score;
- pedagogical format, assessment, and delivery design are not inferred or
  designed.
- every non-trivial course allocation has a recorded rationale traceable to
  `design/synthesis/s04-synthesis.md`;
- each construction record is sufficient for a later independent audit or
  regeneration without relying on conversational memory.
- every course-content identifier has an exact S04 finding reference and a
  recorded allocation rationale;
- every applicable S04 finding is represented in at least one S05 document or
  has an explicit out-of-scope rationale;
- forward and reverse traceability agree within each document and across all
  six documents.
