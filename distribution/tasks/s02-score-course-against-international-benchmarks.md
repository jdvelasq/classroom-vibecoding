# S02 — Score a course against international benchmarks

Read and comply with the repository-level `AGENTS.md` before execution.

## Objective

Produce a transparent, evidence-bounded score out of 10 for one implemented
course against the international benchmark corpus. The score is an internal
design-audit judgment, not an accreditation decision or a claim about any
external institution's endorsement.

## Inputs for `descriptiva`

- `design/synthesis/s04-synthesis.md`;
- `design/synthesis/s05-diseno-descriptiva.md`;
- `implementation/descriptiva/traceability.yaml`;
- `implementation/descriptiva/audit-against-design.md`;
- the common and course-specific P activities referenced by the traceability
  file;
- the institutional and authoritative PDFs under `design/benchmarks/`; and
- the published course site, only as evidence of the shared flipped-classroom
  layer.

## Rubric (100 points)

| Dimension | Weight |
|---|---:|
| Analytics identity, decision framing, and scope boundaries | 15 |
| Descriptive exploration, visualization, interpretation, and epistemic limits | 20 |
| Data preparation, access, and durable technical fluency | 10 |
| Authentic cases, integrated practice, and portfolio evidence | 15 |
| Responsible, reproducible, and documented work | 10 |
| Assessment evidence and learner feedback | 15 |
| Delivery readiness, accessibility, and scalable student workflow | 5 |
| Governance, bidirectional traceability, and continuous improvement | 10 |

## Required method

1. Score only evidence that exists at audit time. Do not award points for
   future LABs, a future distribution template, or anticipated teaching
   quality.
2. Report both the score for the currently implemented P sequence and the
   whole-course score. The latter must account for pending course phases.
3. State the evidence, limitation, and reason for the score in every row.
4. Preserve Analytics as the identity. Do not reward breadth in BI, databases,
   statistics, ML, or AI when it displaces the decision-connected Analytics
   purpose.
5. Identify the exact conditions required to reach 10/10. A score of 10 must
   be supported by implemented and independently auditable evidence across all
   rubric dimensions.

## Output

Create `implementation/<course-id>/international-benchmark-audit.md`, with
the rubric, score, evidence links, limitations, comparisons to the local
benchmark corpus, and a dated construction record.
