# S05 — Map the consolidated Analytics synthesis to the courses

Read and comply with the repository-level `AGENTS.md` before execution.

## Objective

Translate the evidence-backed capabilities and boundaries in
`design/synthesis/s04-synthesis.md` into a visible allocation across these six
courses:

- Pregrado: Fundamentos de analítica; Fundamentos de data para analítica.
- Posgrado: Analítica descriptiva y visualización de datos; Analítica
  predictiva; Analítica prescriptiva; Productos de datos.

This is a content-allocation task. It determines each course's principal and
recurring responsibility for Analytics capabilities; it is not a weekly plan,
theory redesign, workshop design, lab design, assessment design, or final
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

Use only `design/synthesis/s04-synthesis.md` as the evidence base. Do not conduct
external research and do not modify the benchmark corpus or S01--S04 outputs.

Every allocation in the map must be traceable to a finding or constraint in
the synthesis. Preserve a decision log inside the output: state the source
sections consulted, the allocation rule used, and any interpretation or
unresolved tension. A future executor must be able to rerun the task from the
same local input and determine why a capability was assigned to a course.

## Required output

Create exactly these six files in `design/synthesis/`:

- `s05-diseno-fundamentos.md`
- `s05-diseno-data.md`
- `s05-diseno-descriptiva.md`
- `s05-diseno-predictiva.md`
- `s05-diseno-prescriptiva.md`
- `s05-diseno-productos.md`

Each file must include:

1. purpose and scope boundaries;
2. a canonical set of map-ready Analytics capabilities derived from the
   synthesis, with contributing disciplines described only functionally;
3. the course's responsibility for each applicable capability, using explicit
   labels for principal, recurring, contextual, and out-of-scope treatment;
4. a profile of that course, including its distinctive content responsibility
   and what it deliberately does not own;
5. explicit content boundaries and unresolved scope decisions; and
6. an audit-readiness boundary identifying what the map can support and what
   remains pending until later design stages; and
7. a construction record containing: task identifier, course identifier, and execution date;
   exact local input path; source revision or content fingerprint when
   available; capability-allocation rules; section-level traceability to the
   synthesis; unresolved decisions; and the result of the quality checks.

## Quality checks

Before completion, verify that:

- the six files collectively give every capability from the consolidated
  synthesis a visible home;
- no course is made a prerequisite by implication;
- no contributing discipline becomes a course-organizing identity;
- optional undergraduate courses are not assumed by postgraduate courses;
- the map does not claim that any course already earns a 10/10 audit score;
- pedagogical format, assessment, and delivery design are not inferred or
  designed.
- every non-trivial course allocation has a recorded rationale traceable to
  `design/synthesis/s04-synthesis.md`;
- each construction record is sufficient for a later independent audit or
  regeneration without relying on conversational memory.
