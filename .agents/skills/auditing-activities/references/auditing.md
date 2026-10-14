# Auditing the activities of a course

The method for the audit phase of `auditing-activities`. It keeps the
method of the former S03 task (propose improvements to a course from a
benchmark) and changes its input: instead of a benchmark document, the
audit reads what the student must learn in the course, from its course
file in `04-curriculum/`. The file contract is in `format.md`.

## Purpose

The audit maps, in detail, what the student must learn in the course
against how the course achieves it through its activities, as their
highlights in `activity.md` describe them. For one course it answers:

> ¿Qué debe aprender el estudiante en este curso que hoy no logra ninguna
> actividad, o no al nivel que el curso le debe; qué logran las
> actividades que el curso no necesita; y qué cambio, puntual o de curso,
> lo corrige sin regresión, sin alargar los talleres y sin desdibujar la
> identidad del curso en analítica?

Two kinds of change come out of it:

- **point changes** to an activity, in its own `tasks.md`, saying exactly
  what to change; for example, adding the framing of the business problem
  to a workshop that starts from a dataset; and
- **course changes**, in the course `tasks.md`: new activities for larger
  aspects that no existing activity can hold, described in detail, and
  reorganizations (merge, move, replace, remove).

Every proposal answers to methodological, technical and pedagogical
principles, and to the identity of the course.

The audit only **proposes**. It does not modify the implementation or the
`activity.md` of any activity. Its proposals wait for david's discussion and
nothing is executed without his explicit approval. "No proposal" is a valid
and frequent result.

## Input

`audit_status.py <curso>` prints everything the audit needs:

- the **course outcomes** `<curso>/RCnn`, each with its statement, its
  assessment, the program outcomes it derives from and the **level** the
  course owes it;
- the **items**: the knowledge and skills of their competencies, each with
  a stable id (`C002.HAB03`), the detail of what the student must learn;
- the **identity**, **required knowledge** and **scope** of the course file;
- the activities of the course, with their highlights, surfaces,
  traceability entry, proposals and previous decisions; and
- the open course proposals.

Read the course file itself, `04-curriculum/postgraduate/<curso>.md` or
`04-curriculum/undergraduate/<curso>.md`, and the levels of
`04-curriculum/format.md`:

- **introduce**: the course presents the performance and the student
  practices it, guided, on parts of the product;
- **desarrolla**: the student produces the product with partial autonomy on
  a case prepared by the professor and gets feedback;
- **domina**: the course evaluates the complete product of the outcome under
  the conditions its statement sets.

For each activity, read its `activity.md`, its `log.md` if there is one,
and its `tasks.md`; read the course `tasks.md`. Do not read the
implementation: `activity.md` is the auditable reading of it. Do not read
benchmarks or the web.

### Preconditions

- Every activity of the course must have a valid description. If
  `audit_status.py` lists blocked activities, describe or fix them first.
- If the course file or its outcomes are missing, `audit_status.py` stops:
  the curriculum must be mapped first with `mapping-curriculum`.

## Identity

The identity of the course is already decided. It comes from `AGENTS.md`
(the curriculum identity and the course-identity audit questions) and from
the **Identidad** section of the course file, which applies those questions
to the course: its question, its terminal product, the role of the
contributing disciplines and the **risk**, the abbreviated course of a
contributing discipline it could be mistaken for. The audit applies these;
it does not add criteria of its own.

The course must show its identity by itself: a specialist in the
contributing discipline, predictive ML for example, should recognize the
methods and also see that they serve the course's analytical product.
Identity is lost both by what is missing (the activities never reach the
terminal product) and by what is left over (highlights that teach the
contributing discipline for its own sake). Every proposal states how it
serves the terminal product and avoids the risk.

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
is not embedded: it becomes a course change (c). State in every point change
why the activity stays short.

### 4. Sequence and sessions

Groups advance at different paces and some do not reach the last
workshops, and every new activity competes for the course's sessions. A new
activity or a change of order states what it displaces, merges or trims,
and what a slower group would lose.

### 5. Previous rejections

Before proposing, look in the logs for `DEC` entries and in the tasks files
for rejected proposals. Do not propose an equivalent one again unless the
course file gives a different argument; then cite the rejection and say
what changed.

## Method

1. **Read the signals**: every course outcome and every item.
2. **Contrast each signal** with the descriptions: first with the external
   comparison index, then with `HNN` and `SNN`. Never with the workshop's
   title.
3. **Map with levels**: anchor each signal to the highlights that work on
   it, each with the level at which it does (`introduce`, `desarrolla`,
   `domina`). A course outcome is covered only when some anchor reaches the
   level the course owes it.
4. **Classify each signal** in one category of `format.md`: covered,
   marginal, previously rejected, out of scope (it displaces the Analytics
   identity, belongs to another course by the scope of the course file, or
   lacks a case and data to teach it rigorously), improvement of an
   existing activity, or new activity. A partly covered signal keeps its
   anchors and takes the category of what is missing.
5. **Account for every highlight**: a highlight that no signal anchors is
   outside what the course must teach. Keep it, with the reason it
   technically sustains the product, or trim it with a proposal. Look here
   for the excess that pulls the course toward the risk its file names, and
   for required knowledge taught again.
6. **Decide each activity**: `igual` (a), `puntual` (b) or `curso` (c). An
   activity that serves no course outcome is a course decision. Record
   which course outcomes and competencies it serves: they become its
   traceability entry.
7. **Justify each proposal** on its methodological, technical and
   pedagogical principles and on the identity of the course.
8. **Integrate** with existing proposals: if an open proposal is
   equivalent, reinforce it (`refuerza`) instead of duplicating it.
9. **Review interactions**: the proposals of one activity are discussed and
   executed together; state which depend on, compete with or reinforce each
   other.
10. **Write the audit** as JSON (below), check it and apply it.

## The audit file

Write it in the scratchpad, not in the repository. Every text is in
Spanish.

```json
{
  "curso": "predictiva",
  "executor": "Claude",
  "fecha": "2026-10-14",
  "senales": [
    {"id": "predictiva/RC02", "categoria": "cubierta",
     "anclas": [{"hito": "P200:H02", "nivel": "introduce"}, {"hito": "P206:H03", "nivel": "domina"}]},
    {"id": "predictiva/RC01", "categoria": "mejora", "actividad": "P200", "propuesta": "encuadre",
     "anclas": [{"hito": "P205:H01", "nivel": "introduce"}]},
    {"id": "C001.CON04", "categoria": "fuera de alcance", "razon": "…"},
    {"id": "C001.HAB02", "categoria": "marginal", "razon": "…", "actividad": "P200"},
    {"id": "C006.HAB01", "categoria": "actividad nueva", "propuesta": "seguimiento"}
  ],
  "actividades": [
    {
      "actividad": "P200",
      "decision": "puntual",
      "resultados": ["predictiva/RC01", "predictiva/RC02"],
      "competencias": ["C001", "C004"],
      "razon": "Una oración: por qué esta decisión.",
      "propuestas": [{
        "clave": "encuadre",
        "titulo": "…", "tipo": "encuadre", "que_gana": "…",
        "anclas": ["H01", "S02"], "alternativas": "…", "no_regresion": "…",
        "limite": "…", "interacciones": "…",
        "metodologico": "…", "tecnico": "…", "pedagogico": "…", "identidad": "…",
        "aceptacion": "…", "instrucciones": "…"
      }],
      "refuerza": ["T01"],
      "fuera": [
        {"hito": "H04", "accion": "recortar", "propuesta": "encuadre", "razon": "…"},
        {"hito": "H05", "accion": "conservar", "razon": "…"}
      ]
    },
    {"actividad": "P220", "decision": "curso", "resultados": [], "competencias": [],
     "razon": "…", "curso": "seguimiento"}
  ],
  "nuevas": [{
    "clave": "seguimiento", "tipo": "actividad nueva", "titulo": "…",
    "contribucion": "…", "posicion": "…", "desplaza": "…", "efecto": "…",
    "caso": "…", "producto": "…",
    "metodologico": "…", "tecnico": "…", "pedagogico": "…", "identidad": "…",
    "aceptacion": "…"
  }],
  "refuerza": ["N01"]
}
```

- `senales` holds every course outcome and item, once each. `actividad` is
  optional on a discarded signal; it attributes the signal to that
  activity's log.
- `propuesta`, `curso` and a trimmed highlight's `propuesta` cite the
  `clave` of a new proposal, or the id of an open one (`T01` of that
  activity, `N01` of the course).
- An activity of another course is cited with its path, `descriptiva/P103`,
  and its anchors as `descriptiva/P103:H01`.

## Discussion and decisions (outside the skill)

David discusses **all** the proposals of an activity together, because they
interact. When he decides:

- **approved:** the entry stays in the activity's `tasks.md` with state
  «aprobada» until it is executed;
- **rejected:** the entry leaves the activity's `tasks.md` and is recorded
  in its `log.md` as `DEC.Pxxx.NN` with the proposal, its sources and the
  reason. A rejected course proposal stays in the course `tasks.md` with
  state «rechazada» and its reason.

Later audits treat both as previous rejections.

## Before applying

After `check_audit.py` reports no errors, confirm what it cannot check:

- every proposal passes materiality and says what the student gains;
- every point change says exactly what to change and keeps the activity a
  short, well-defined problem;
- every course change says what it displaces, merges or trims;
- every justification names a real methodological, technical and
  pedagogical principle, not a restatement of the change;
- every proposal is anchored to existing `HNN`/`SNN`, or, if it is a course
  change, states position, distinct contribution and effect on the
  sequence;
- existing proposals were reinforced, not duplicated, and previous
  rejections were consulted; and
- the course as a whole still answers the question and ends in the
  terminal product of its file, and no activity reads as the abbreviated
  course its file names as the risk.
