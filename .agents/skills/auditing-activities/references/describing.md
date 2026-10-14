# Describing an activity

The method for the description phase of `auditing-activities`. It keeps
the method of the former S02 task (describe and audit the implemented
activities of a course). The file contract is in `format.md`.

The implemented activity is the baseline. This phase **describes**; it does
not redesign, accept improvements, search the web or modify the
implementation. It does not create, edit or use proposals as evidence. It
does not create, delete, rename, merge or reorder activities, and it does
not inspect or modify other courses.

Only activities without `activity.md` are described. An existing
description is not regenerated unless david asks for it; then the run is
incremental (step 6).

## Guiding principle: contribution, not inventory

The description must let a later audit decide whether to keep, improve,
combine or replace a workshop. Each activity answers, with evidence:

> ¿Qué capacidad concreta se empieza a ejercer, se extiende, se contrasta o
> se aplica de una forma nueva aquí, y qué se perdería de la secuencia si
> este taller no existiera?

"Usa Python", "enseña regresión", "incluye un notebook", a library name or
the business question repeated are not enough. Contribution is expressed as
**highlights**, kept apart from the technique inventory.

## Steps

For each activity to describe, in order, inspect its substantive content: data,
manifests and provenance notes; instructions, notebooks, code and professor
material; `submission/`, contracts and visualizations; tests; the course
`traceability.yaml`; and its previous description and log, if they exist.

1. **Case.** Reconstruct the analytical questions as bullets, and the user,
   decision, entity, time, data and provenance only when the implementation
   shows them; mark what is unspecified. Identify what the dataset imposes
   on the problem: unit of analysis, structure, label, granularity,
   imbalance, missing values, time order, noise, sensitivity, simulation,
   required transformation or use restriction. When the orientation of a
   table or matrix defines the unit of analysis, state what rows and columns
   represent and what reading that allows: rows = days and columns = hours
   group daily patterns, not independent hourly observations.
2. **Product.** Reconstruct the current terminal product and check the
   Analytics identity with the audit questions of `AGENTS.md`: contributing
   disciplines serve the product; they do not organize it.
3. **Practices.** Inventory what is actually exercised: data,
   transformations, functions and methods, patterns, validations, tests,
   persistence, delivery or operation. An import is not a practice.
4. **Sequence.** Contrast the activity with the earlier Pxxx of the course.
   The same business question does not prove duplication; look for the
   analytical, technical, data, evidence or product change.
5. **Highlights first**, then the technique inventory and the external
   comparison index. Every important claim has a concrete backing path. The
   index records present coverage; it does not treat an absence as a
   deficit or propose a topic.
6. **Incremental run.** Keep what was verified, correct what the evidence
   contradicts and record ambiguities. Do not rewrite for style or delete a
   previous conclusion without a documented reason.

### Highlights

A highlight is a contribution milestone, not a label. It has:

1. a verb for what is learned to do or to verify;
2. a specific mechanism ("codifica una nominal con `OneHotEncoder` sin
   imponer orden", not "usa sklearn");
3. the observable evidence: notebook, function, test, output, contract or
   visualization;
4. its place in the sequence: first appearance, extension, contrast or new
   application; and
5. the capability that would be lost without it.

Prefer the precision of "muestra que una MLP de una entrada compite con una
regresión lineal de la misma entrada" to "introduce MLP". Quote a number
only if it is in a persisted artifact or a verifiable output. If evidence is
missing, do not invent the highlight: record it as a limit or ambiguity.
Their number is not fixed; each justifies a distinguishable contribution.
They are neither proposals nor claims about real student achievement.

At least one highlight, marked `(caso y datos)`, links an evidenced
particularity of the case or dataset with the practice it demands:

> ¿Qué hace que este problema no sea intercambiable con un CSV genérico y
> cómo cambia esa condición la representación, validación, interpretación
> o límite del producto?

"Usa un CSV", "trabaja con datos reales" or the dataset name are not
highlights. If the implementation reveals no particularity, record the
absence as a limit.

Ids `H01`, `H02`… follow the pedagogical sequence and are stable: if a
highlight splits, it keeps its id and the new part gets a new one; if it
turns out unsupported, keep the id and record the correction in the log.
Every highlight links to at least one existing surface `SNN`; if it cannot,
the surface list is incomplete.

### Surfaces, contract and dependencies

They record the change interface of the current activity, not proposals:
the existing components that could change (case/dataset, representation,
method, validation, product, test, interface or sequence) with their paths;
what the notebook does, what `submission/` persists, what the tests really
check and what traceability maps; and only the dependencies between Pxxx
that can be shown. A plausible but unshown dependency is marked
«no evidenciada».

### Log entry

Append `## S02.Pxxx.NN` to the activity's `log.md`, with the id the
inventory gives and the content `format.md` lists. Create the log with `# Log — Pxxx` if
it does not exist. Never edit earlier entries. If a previous description
still has the inherited section «Mejoras aceptadas pendientes de
implementación», remove it when it is empty; if it has content, keep it and
record it as an ambiguity.

## Before saving

After `check_activities.py` reports no errors, confirm by reading what the
script cannot check:

- each Pxxx was read from its content, not its name;
- each highlight explains a sequential contribution and has evidence;
- the product, its limits and the contributing disciplines were stated
  without inventing user, decision or context;
- the comparison index holds only current mechanisms, data, products and
  evidence, with no gaps or proposals;
- surfaces, contract and dependencies describe what exists, not proposals;
- questions, inventory, highlights and traceability do not contradict each
  other;
- the traceability entry was reviewed, or its absence recorded;
- no case, provenance, technique, competency, product or achievement was
  invented; and
- only the `activity.md` and `log.md` of the described activities changed.
