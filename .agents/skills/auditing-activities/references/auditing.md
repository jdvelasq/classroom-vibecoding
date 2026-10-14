# Auditing the activities of a course

The method for the audit phase of `auditing-activities`. It keeps the
method of the former S03 task (propose improvements to a course from a
benchmark) and changes only its input: instead of one benchmark document,
the audit reads what the course must cover according to the design chain
02 → 03 → 04. The file contract is in `format.md`.

## Purpose

For one course, the audit answers:

> ¿Lo que el curso debe cubrir justifica cambiar algo que mejore **de forma
> material** lo que el estudiante aprende en algún taller, sin regresión de
> lo que ya funciona y sin que el taller deje de ser un problema corto y
> bien definido?

The audit only **proposes**. It does not modify the implementation or the
`activity.md` of any activity. Its proposals wait for david's discussion and
nothing is executed without his explicit approval. "No proposal" is a valid
and frequent result.

## Input

`audit_status.py <curso>` prints everything the audit needs:

- the **targets**: the learning outcomes the matrix assigns to the course,
  with their level and contribution, or the course outcomes of an
  undergraduate course;
- the **items**: the knowledge and skills of the targets' competencies, each
  with a stable id (`C002.HAB03`);
- the activities of the course, with their highlights, surfaces,
  traceability entry, proposals and previous decisions; and
- the open course proposals.

Read also, for each target, its source file: the learning outcome in
`03-learning-outcomes/outcomes/RAnn.md` or the course outcome in
`04-curriculum/undergraduate/<curso>.md`. Its **Evaluación** says what the
student must produce. The level fixes what the course owes:

- **introduce**: the course presents the performance and the student
  practices it, guided, on parts of the product;
- **desarrolla**: the student produces the product with partial autonomy on
  a case prepared by the professor and gets feedback;
- **domina**: the course evaluates the complete product of the outcome under
  the conditions its statement sets. A `domina` target usually calls for a
  course decision when no activity ends in that product, because one short
  activity rarely holds a complete product.

For each activity, read its `activity.md`, its `log.md` and its
`tasks/Pxxx_tasks.md`; read `tasks/course_tasks.md`. Do not read the
implementation: `activity.md` is the auditable reading of it. Do not read
benchmarks or the web.

### Preconditions

- Every activity of the course must have a valid description. If
  `audit_status.py` lists blocked activities, describe or fix them first.
- If the course has no targets, `audit_status.py` stops: the curriculum must
  be mapped first with `mapping-curriculum`.

## Decision criteria

### 1. Materiality

A signal produces a proposal **only** if it:

- changes what the student is able to **do or understand** at the end of
  the workshop (a capability, a contrast, a form of evidence or a product it
  does not exercise today); or
- corrects a **real defect**: something wrong, misleading or obsolete in
  what the workshop teaches.

Variations of something already covered (another business question when
the existing ones serve the pedagogical aim, another equivalent dataset,
another library for the same thing), the mere naming of a technique in a
competency, or novelty by itself produce no proposal.

### 2. No regression

What already works is in the highlights `HNN`, surfaces `SNN` and
dependencies of each `activity.md`. Every proposal states which it keeps
and, if it replaces one, why and with what at least equivalent evidence.
Prefer the smallest change that achieves the benefit:

1. clarify or make visible something that already exists;
2. extend locally without changing case, product or contracts;
3. change the activity materially;
4. create a new activity.

The burden of justification grows in that order.

### 3. Identity and limit of the workshop

Each workshop teaches something concrete, technically and pedagogically;
that identity is in its question, product and highlights. An activity is a
typical, clear and well-defined problem solved in a short session; a long
activity loses its purpose. A proposal that **reinforces** that
contribution without lengthening it is a point change (b). A proposal that
**adds a second, different contribution**, or that lengthens the activity,
is not embedded: it becomes a course decision (c). A workshop cannot grow
without limit; state in every point change why it stays short.

### 4. Sequence

Groups advance at different paces and some do not reach the last
workshops. A new activity or a change of order states which activities it
displaces and what a slower group would lose.

### 5. Previous rejections

Before proposing, look in the logs for `DEC` entries and in the tasks files
for rejected proposals. Do not propose an equivalent one again unless the
course outcomes give a different argument; then cite the rejection and say
what changed.

## Method

1. **Read the signals**: every target and every item.
2. **Contrast each signal** with the descriptions: first with the external
   comparison index, then with `HNN` and `SNN`. Never with the workshop's
   title.
3. **Classify each signal** in one category of `format.md`: covered (with
   its anchors `Pxxx:HNN`), marginal, previously rejected, out of scope
   (it displaces the Analytics identity, belongs to another course, or lacks
   a case and data to teach it rigorously), improvement of an existing
   activity, or new activity.
4. **Decide each activity**: `igual` (a), `puntual` (b) or `curso` (c). An
   activity that serves no target of the course is a course decision.
   Record which targets and competencies it serves: they become its
   traceability entry.
5. **Integrate** with existing proposals: if an open proposal is
   equivalent, reinforce it (`refuerza`) instead of duplicating it.
6. **Review interactions**: the proposals of one activity are discussed and
   executed together; state which depend on, compete with or reinforce each
   other.
7. **Write the audit** as JSON (below), check it and apply it.

## The audit file

Write it in the scratchpad, not in the repository. Every text is in
Spanish.

```json
{
  "curso": "descriptiva",
  "executor": "Claude",
  "fecha": "2026-10-14",
  "senales": [
    {"id": "RA02", "categoria": "cubierta", "anclas": ["P103:H03"]},
    {"id": "C002.CON04", "categoria": "fuera de alcance", "razon": "…"},
    {"id": "C002.HAB01", "categoria": "marginal", "razon": "…", "actividad": "P103"},
    {"id": "C002.HAB03", "categoria": "mejora", "actividad": "P103", "propuesta": "exposicion"},
    {"id": "C003.HAB02", "categoria": "actividad nueva", "propuesta": "producto-completo"}
  ],
  "actividades": [
    {
      "actividad": "P103",
      "decision": "puntual",
      "resultados": ["RA02"],
      "competencias": ["C002"],
      "razon": "Una oración: por qué esta decisión.",
      "propuestas": [{
        "clave": "exposicion",
        "titulo": "…", "tipo": "método", "que_gana": "…",
        "anclas": ["H01", "S02"], "alternativas": "…", "no_regresion": "…",
        "limite": "…", "interacciones": "…", "aceptacion": "…",
        "instrucciones": "…"
      }],
      "refuerza": ["T01"]
    },
    {"actividad": "P121", "decision": "curso", "resultados": [], "competencias": [],
     "razon": "…", "curso": "producto-completo"}
  ],
  "nuevas": [{
    "clave": "producto-completo", "tipo": "actividad nueva", "titulo": "…",
    "contribucion": "…", "posicion": "…", "efecto": "…", "caso": "…",
    "producto": "…", "aceptacion": "…"
  }],
  "refuerza": ["N01"]
}
```

- `senales` holds every target and item, once each. `actividad` is
  optional on a discarded signal; it attributes the signal to that
  activity's log.
- `propuesta` and `curso` cite the `clave` of a new proposal, or the id of
  an open one (`T01` of that activity, `N01` of the course).
- An activity of another course is cited with its path, `descriptiva/P103`,
  and its anchors as `descriptiva/P103:H01`.

## Discussion and decisions (outside the skill)

David discusses **all** the proposals of an activity together, because they
interact. When he decides:

- **approved:** the entry stays in `Pxxx_tasks.md` with state «aprobada»
  until it is executed;
- **rejected:** the entry leaves `Pxxx_tasks.md` and is recorded in the
  activity's `log.md` as `DEC.Pxxx.NN` with the proposal, its sources and
  the reason. A rejected course decision stays in `course_tasks.md` with
  state «rechazada» and its reason.

Later audits treat both as previous rejections.

## Before applying

After `check_audit.py` reports no errors, confirm what it cannot check:

- every proposal passes materiality and says what the student gains;
- every point change keeps the activity a short, well-defined problem;
- every proposal is anchored to existing `HNN`/`SNN`, or, if it is a course
  decision, states position, distinct contribution and effect on the
  sequence;
- existing proposals were reinforced, not duplicated;
- previous rejections were consulted;
- every proposal has a no-regression contract, an acceptance criterion and
  execution instructions; and
- the Analytics identity of `AGENTS.md` is preserved: no activity, and no
  proposed activity, reads as an abbreviated course in one contributing
  discipline.
