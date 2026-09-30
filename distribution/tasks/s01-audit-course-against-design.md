# S01 — Audit a distributed course against its design

Read and comply with the repository-level `AGENTS.md` before execution.

## Objective

Produce a reproducible, bidirectional audit of one course implementation and
its distributable repository against its approved course-content design. The
audit does not redesign the course, create activities, or claim an external
quality score. It establishes whether the evidence needed for a later
standards audit is present, coherent, and traceable.

## Scope and inputs

The task is parameterized by `<course-id>`. For `descriptiva`, use:

- `design/synthesis/s05-diseno-descriptiva.md` as the authoritative course
  design;
- `implementation/descriptiva/traceability.yaml` as the declared link from
  workshops to capabilities;
- `implementation/common/P001_*` through `P009_*` and
  `implementation/descriptiva/P100_*` through `P199_*` as the implementation
  inventory; and
- the future course template under `distribution/descriptiva/`, if it exists.

The public course site is the common flipped-classroom support layer. It may
be cited as delivery evidence, but it is not copied into the student template
and it does not replace workshop evidence.

## Audit questions

1. For every `descriptiva.Cxx` capability, identify the implemented workshops
   that support it and determine whether their intended evidence is visible.
2. For every workshop used by the course, trace it back to one or more design
   capabilities or record it as an explicit enabling activity.
3. Verify that the activity sequence preserves Analytics as the organizing
   identity; BI, databases, statistics, ML, and related disciplines must
   serve an Analytics decision or communication purpose.
4. If `distribution/descriptiva/` exists, verify that it contains only
   student-facing artifacts; excludes `professor/`; uses the root
   `requirements.txt`; preserves activity-local test discovery; and has a
   GitHub Actions grading workflow. If it does not yet exist, record this as
   an unverified delivery condition rather than a curriculum defect.
5. Identify design-document defects separately from implementation defects.
   Do not silently repair derived design files during an audit.

## Required output

Create `implementation/<course-id>/audit-against-design.md`. Include:

- source paths and content fingerprints when available;
- an outcome classified as `ready`, `conditionally ready`, or `not ready`;
- a forward table: design capability → workshops → evidence;
- a reverse table: workshop → design identifier or enabling rationale;
- findings divided into design, implementation, and distribution;
- an explicit statement of what has not yet been verified; and
- a follow-up checklist that distinguishes required corrections from work
  intentionally deferred to the distribution phase.

## Quality rules

- Preserve the Analytics identity defined in `AGENTS.md`.
- Do not equate a `pytest` pass with achievement of a learning outcome; it is
  technical evidence only.
- Do not count the public site, instructor-only artifacts, or future LABs as
  student-template contents.
- Do not assert a 10/10 international benchmark result. This audit is an input
  to that later determination.
- A missing future template is a delivery-phase gap, not a reason to alter the
  course-content design.
