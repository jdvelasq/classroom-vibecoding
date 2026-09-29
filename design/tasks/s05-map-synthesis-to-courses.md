# S05 — Map the consolidated Analytics synthesis to the courses

Read and comply with the repository-level `AGENTS.md` before execution.

## Objective

Translate the evidence-backed capabilities and boundaries in
`design/synthesis/s04-synthesis.md` into a visible allocation across these six
courses:

- Pregrado: Fundamentos de analítica; Fundamentos de data para analítica.
- Posgrado: Analítica descriptiva y visualización de datos; Analítica
  predictiva; Analítica prescriptiva; Productos de datos.

This is a curriculum-architecture task. It determines each course's principal
and recurring responsibility for Analytics capabilities; it is not yet a
weekly plan, a theory redesign, a workshop design, a lab design, or a final
international audit. Its construction must itself be auditable and
reproducible from the declared local inputs.

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
- The current design scope is the future layer of guided in-person workshops.
  Theory, flipped-class materials, and evaluative labs are incomplete and
  must be marked pending rather than inferred.

## Source policy

Use only `design/synthesis/s04-synthesis.md` as the evidence base. Do not conduct
external research and do not modify the benchmark corpus or S01--S04 outputs.

Every allocation in the map must be traceable to a finding or constraint in
the synthesis. Preserve a decision log inside the output: state the source
sections consulted, the allocation rule used, and any interpretation or
unresolved tension. A future executor must be able to rerun the task from the
same local input and determine why a capability was assigned to a course.

## Required output

Create exactly one file: `design/curriculum/s05-course-capability-map.md`.

It must include:

1. purpose and scope boundaries;
2. a canonical set of map-ready Analytics capabilities derived from the
   synthesis, with contributing disciplines described only functionally;
3. a course-responsibility matrix using explicit labels for principal,
   recurring, contextual, and out-of-scope treatment;
4. a short profile for every course, including its distinctive responsibility,
   what it deliberately does not own, and its relationship to portfolio-ready
   guided workshops;
5. shared progression and learner-access rules; and
6. an audit-readiness boundary identifying what the map can support and what
   remains pending until theory and evaluative labs are designed; and
7. a construction record containing: task identifier and execution date;
   exact local input path; source revision or content fingerprint when
   available; capability-allocation rules; section-level traceability to the
   synthesis; unresolved decisions; and the result of the quality checks.

## Quality checks

Before completion, verify that:

- every capability from the consolidated synthesis has a visible home;
- no course is made a prerequisite by implication;
- no contributing discipline becomes a course-organizing identity;
- optional undergraduate courses are not assumed by postgraduate courses;
- the map does not claim that any course already earns a 10/10 audit score;
- workshop scope is not confused with evaluative labs or theory.
- all non-trivial course allocations have a recorded rationale traceable to
  `design/synthesis/s04-synthesis.md`;
- the construction record is sufficient for a later independent audit or
  regeneration without relying on conversational memory.
