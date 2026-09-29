# S03 — Review and Synthesize Curriculum Benchmarks

## Objective

Produce an independent, evidence-based synthesis of the curriculum benchmark corpus in `design/benchmarks/`.

The purpose of this task is to determine what the available authoritative,
institutional, governmental, literature-derived, and professional-learning
evidence collectively reveals about the **structure, boundaries, competencies,
progression, and applied orientation of Analytics education**.

This task is **benchmark synthesis**, not final curriculum design.

The output will later be compared with equivalent syntheses produced independently by other LLM agents and integrated in a subsequent task.

---

## Governing instructions

Read and comply with the repository-level `AGENTS.md` before performing this task.

In particular, preserve the disciplinary identity of the project as **Analytics**.

Machine Learning, Statistics, Operations Research and Optimization, Data Science, Data Engineering, Databases, Business Intelligence, Artificial Intelligence, and related fields may contribute concepts, methods, techniques, and tools.

Do not allow the internal curricular logic of any contributing discipline to redefine the target curriculum.

---

## Input corpus

Analyze the complete benchmark corpus under:

`design/benchmarks/`

The corpus currently contains four evidence families. These directory names are the canonical local taxonomy for this task:

### 1. Authoritative benchmarks

`design/benchmarks/authoritative/`

These materials include externally authored frameworks, competency references, certification blueprints, and academically grounded reports. Use them primarily to understand:

- conceptual foundations;
- disciplinary framing;
- competency structures;
- educational rationale;
- enduring knowledge;
- curricular principles.

### 2. Institutional benchmarks

`design/benchmarks/institutional/`

These materials represent university, executive, continuing-education, or comparable professional-education offerings.

They may provide evidence about:

- course scope;
- market-facing curriculum structures;
- learning outcomes;
- sequencing;
- instructional emphasis;
- technologies;
- applied orientation.

### 3. Governmental benchmarks

`design/benchmarks/governmental/`

These materials document public policy, publicly funded training, or national
digital-skills initiatives. They may provide context about local priorities,
audiences, delivery models, and the public positioning of competencies.

Do not treat them as international authoritative standards, and do not let a
government programme's technology list define Analytics. Preserve their
distinct evidentiary role in the synthesis.

### 4. Professional-learning syntheses

The following task-generated syntheses reconstruct provider evidence and are
inputs alongside the primary benchmark corpus:

- `design/synthesis/s01-datacamp.md`;
- `design/synthesis/s02-pluralsight.md`.

Treat them as derived professional-learning evidence, not as primary benchmark
documents.

Do **not** repeat the DataCamp or Pluralsight web research performed in S01 and S02.

### 5. Literature-derived benchmarks

`design/benchmarks/literature-derived/`

These materials are locally curated references derived from literature and related source material. Treat them as evidence of the perspectives and practices they document, not automatically as external curriculum standards or as a replacement for authoritative evidence.

---

## Corpus policy

Read the relevant contents of all four evidence families before drawing cross-corpus conclusions.

Do not base the synthesis primarily on filenames, document titles, abstracts, tables of contents, or isolated excerpts when the underlying document contains relevant substantive material.

The purpose is to understand the corpus sufficiently to identify meaningful patterns across sources.

### Local corpus first

The benchmark corpus is the evidence base for this task.

Do not perform additional web research to expand, replace, or update the benchmark corpus.

If a local benchmark identifies an uncertainty or limitation, preserve that limitation rather than attempting to repair it through external research.

### Do not modify benchmark sources

Files under `design/benchmarks/` are inputs.

Do not modify them during this task.

---

## Independence requirement

This task will be executed independently by multiple LLM agents.

Your synthesis must represent **your own analysis of the benchmark corpus**.

Do not read, inspect, compare, summarize, or use synthesis files produced by other agents.

In particular, ignore any existing files matching patterns such as:

- `s03-synthesis-chatgpt.md`;
- `s03-synthesis-claude.md`;
- `s03-synthesis-gemini.md`;
- `s03-synthesis-*.md`;
- `s04-synthesis.md`.

The later integration task is responsible for comparing independent syntheses.

Maintaining independence at this stage is mandatory.

---

## Output selection

Determine which agent/model is executing the task and create exactly one corresponding output:

- ChatGPT / Codex → `design/synthesis/s03-synthesis-chatgpt.md`
- Claude / Claude Code → `design/synthesis/s03-synthesis-claude.md`
- Gemini / Gemini CLI → `design/synthesis/s03-synthesis-gemini.md`

Do not create more than one synthesis file.

Do not modify synthesis files belonging to other agents.

If the executing environment does not permit reliable identification of the model family, stop and report the ambiguity rather than selecting an output file arbitrarily.

---

## Analytical perspective

The central analytical object is **Analytics education**.

The purpose is not merely to count topics across documents.

Analyze how the evidence collectively represents:

- the identity of Analytics;
- its relationship with adjacent and contributing disciplines;
- the capabilities expected from learners;
- the progression from foundations to more advanced analytical work;
- the relationship between data, analysis, decisions, and action;
- the role of tools and technologies;
- the relationship between conceptual understanding and professional practice.

Do not assume in advance that any single benchmark provides the correct architecture.

---

## Evidence-family distinction

The four evidence families have different functions and must not be treated as interchangeable.

### Authoritative evidence

Use authoritative benchmarks primarily to understand:

- conceptual foundations;
- disciplinary framing;
- competency structures;
- educational rationale;
- enduring knowledge;
- curricular principles.

### Institutional evidence

Use institutional benchmarks primarily to understand:

- how universities operationalize professional learning;
- compact curriculum structures;
- applied scope;
- market-facing competencies;
- instructional priorities.

### Professional-learning evidence

Use professional benchmarks primarily to understand:

- professional role definitions;
- job-oriented competencies;
- skill progression;
- applied workflows;
- current tools and technologies;
- distinctions among professional profiles.

### Literature-derived evidence

Use literature-derived benchmarks primarily to understand:

- process, operational, organizational, or historical perspectives documented in the local corpus;
- examples and cases;
- additional context for interpreting the other evidence families;
- areas of concentrated evidence or perspective.

Do not assume that one evidence family automatically has priority over the others.

When evidence families disagree, preserve and analyze the disagreement.

---

## Research questions

The synthesis must address the following questions.

### 1. What is the educational identity of Analytics?

Determine how the corpus collectively characterizes Analytics.

Look for evidence concerning:

- its purpose;
- characteristic activities;
- expected capabilities;
- relationship between analysis and decision-making;
- relationship between technical and contextual knowledge;
- relationship with professional practice.

Do not force a single definition when the corpus supports multiple interpretations.

Instead, distinguish:

- strong convergence;
- partial convergence;
- disagreement;
- unresolved questions.

---

### 2. What distinguishes Analytics from adjacent fields?

Examine how the corpus positions Analytics relative to fields such as:

- Data Science;
- Machine Learning;
- Statistics;
- Operations Research and Optimization;
- Data Engineering;
- Databases;
- Business Intelligence;
- Artificial Intelligence.

Identify:

- shared foundations;
- overlapping competencies;
- distinctive emphases;
- different expected outputs;
- different levels of methodological depth;
- different professional orientations.

Follow `AGENTS.md`.

The objective is not to defend disciplinary boundaries for their own sake.

The objective is to understand what makes the educational architecture recognizably **Analytics** rather than an abbreviated curriculum from a contributing discipline.

---

### 3. What capabilities recur across the corpus?

Identify recurring learner capabilities.

Do not begin from a predetermined competency taxonomy.

Allow competency groupings to emerge from the evidence.

Possible forms of capability may concern:

- understanding;
- obtaining or preparing data;
- analyzing;
- modeling;
- interpreting;
- communicating;
- evaluating;
- deciding;
- implementing;
- using analytical tools.

These examples are illustrative, not mandatory categories.

For each major capability, assess:

- strength of evidence;
- evidence families supporting it;
- differences in interpretation across sources;
- apparent educational importance.

---

### 4. What knowledge areas recur across the corpus?

Identify major knowledge areas supported by the benchmarks.

Distinguish between:

- foundational knowledge;
- enabling knowledge;
- analytical methods;
- contextual or decision-oriented knowledge;
- specialized or optional knowledge,

when the evidence supports such distinctions.

Do not include a topic merely because it is conventional within a contributing discipline.

Its relevance must be supported by the benchmark corpus in the context of Analytics.

---

### 5. What learning progression is supported?

Analyze evidence concerning sequencing and progression.

Look for patterns such as movement from:

- foundations toward application;
- simple toward more complex analytical tasks;
- data understanding toward modeling;
- analysis toward interpretation;
- interpretation toward decisions or action;
- guided exercises toward integrated problems.

These are examples, not a required sequence.

Distinguish:

- progression explicitly stated in sources;
- progression recurring structurally across benchmarks;
- progression inferred analytically.

Identify competing sequencing models when they exist.

---

### 6. How important is professional practice?

Determine how strongly the corpus supports practice-oriented learning.

Analyze evidence concerning:

- exercises;
- cases;
- projects;
- realistic datasets;
- workflows;
- labs;
- professional outputs;
- communication;
- decision contexts;
- integrated analytical tasks.

Determine whether practice appears primarily as:

- reinforcement after conceptual instruction;
- the organizing mechanism for learning;
- assessment;
- professional simulation;
- some combination of these.

---

### 7. What role should tools and technologies play?

Analyze how technologies appear across the benchmark corpus.

Distinguish where possible between:

- durable conceptual capabilities;
- enabling tools;
- widely recurring technologies;
- provider-specific technologies;
- transient or rapidly changing technologies;
- specialized technologies.

Do not infer that a technology belongs in the eventual curriculum merely because it appears frequently.

At this stage, document the evidence and its implications rather than selecting a final technology stack.

---

### 8. What does professional evidence add to authoritative and institutional evidence?

Explicitly compare authoritative and institutional benchmarks with DataCamp and Pluralsight professional evidence.

Identify where professional evidence:

- reinforces authoritative principles;
- operationalizes abstract competencies;
- introduces additional practical capabilities;
- places different emphasis on tools;
- suggests different sequencing;
- reveals professional role distinctions;
- conflicts with authoritative framing.

Do not assume that professional evidence is inherently more current or that authoritative evidence is inherently more decisive.

Analyze what each contributes.

---

### 9. What do literature-derived benchmarks add?

Analyze the relationship between the literature-derived benchmarks and the authoritative, institutional, and professional benchmarks.

Identify:

- areas of strong alignment;
- distinctive strengths or depth;
- areas receiving more attention than external evidence would suggest;
- areas receiving less attention;
- process, operational, organizational, or historical perspectives;
- useful cases or analytical patterns;
- perspectives that are concentrated and should not automatically constrain later design.

Do not treat a literature-derived source as a substitute for evidence from the other families merely because it provides more detail.

---

### 10. Where does the corpus disagree?

Actively search for disagreement rather than reporting only consensus.

Identify disagreements concerning:

- disciplinary boundaries;
- competencies;
- topic importance;
- methodological depth;
- sequencing;
- programming expectations;
- mathematical expectations;
- tools;
- professional orientation;
- balance between concepts and practice.

For each important disagreement, explain which evidence families or sources support the different positions.

Do not resolve disagreements without sufficient evidence.

---

### 11. What appears core, supporting, specialized, or uncertain?

Based on the complete corpus, classify major findings into four analytical categories:

#### Core

Strongly supported across multiple independent sources or evidence families and central to Analytics education.

#### Supporting

Clearly useful to Analytics but primarily enabling another core capability.

#### Specialized

Relevant to particular roles, contexts, technologies, or advanced applications rather than necessarily universal.

#### Uncertain or contested

Evidence is weak, inconsistent, conflicting, or insufficient to establish curricular centrality.

This classification is analytical.

It is **not yet the final course syllabus**.

---

## Cross-source synthesis

Do not produce a sequence of document summaries.

The final output must synthesize evidence **across sources**.

Individual documents should be referenced when necessary to support findings, but the primary organization must reflect patterns found across the corpus.

For important findings, indicate whether support comes from:

- authoritative benchmarks;
- institutional benchmarks;
- professional learning;
- literature-derived benchmarks;
- multiple evidence families.

Pay particular attention to convergence across **independent evidence families**, not merely repetition within one provider or document collection.

---

## Weight of evidence

Use qualitative evidence weighting.

Consider:

- independence of sources;
- number of evidence families supporting a finding;
- explicitness of the evidence;
- relevance to Analytics;
- depth of treatment;
- consistency across sources;
- whether apparent repetition originates from the same underlying framework.

Do not mechanically count occurrences.

Ten references derived from the same curricular tradition do not necessarily provide stronger independent evidence than convergence across several distinct evidence families.

---

## Evidence traceability

Important synthesis claims must remain traceable to the benchmark corpus.

When making major claims:

- identify the relevant source or sources;
- identify the evidence family;
- distinguish source statements from your synthesis;
- avoid attributing an interpretation to a source that does not explicitly make it.

Use document names, sections, page numbers, or other locators when available and useful.

Do not invent missing bibliographic information.

---

## Required output structure

Create the appropriate `design/synthesis/synthesis-<agent>.md` using the following structure.

### `# Benchmark Synthesis`

### `## 1. Scope and method`

Describe:

- benchmark corpus analyzed;
- evidence families;
- synthesis approach;
- important limitations.

State that the synthesis was produced independently without consulting other agents' synthesis files.

### `## 2. Analytics as an educational domain`

Synthesize what the corpus indicates about the identity, purpose, and educational orientation of Analytics.

Distinguish convergence, disagreement, and unresolved issues.

### `## 3. Analytics and contributing disciplines`

Analyze the relationship between Analytics and:

- Data Science;
- Machine Learning;
- Statistics;
- Operations Research and Optimization;
- Data Engineering;
- Databases;
- Business Intelligence;
- Artificial Intelligence;

where supported by the corpus.

Focus on the **function** each field serves within Analytics rather than reproducing the internal curriculum of the contributing discipline.

### `## 4. Recurring capabilities`

Present the major learner capabilities emerging from the corpus.

For each, indicate:

- meaning;
- supporting evidence;
- evidence families;
- strength of convergence;
- important variations.

### `## 5. Knowledge architecture`

Synthesize the major knowledge areas and their relationships.

Distinguish foundations, enabling knowledge, analytical methods, contextual knowledge, and specialization where the evidence supports doing so.

### `## 6. Learning progression`

Present the sequencing and progression patterns supported by the corpus.

Include competing models or unresolved sequencing questions where relevant.

### `## 7. Practice and authentic analytical work`

Analyze:

- exercises;
- cases;
- projects;
- datasets;
- workflows;
- communication;
- decision contexts;
- integrated analytical work.

Explain the pedagogical functions that practice appears to serve.

### `## 8. Tools and technologies`

Synthesize the technology landscape without selecting a final stack.

Distinguish durable capabilities from particular implementations where possible.

### `## 9. Authoritative, institutional, and professional perspectives`

Compare:

- authoritative benchmarks;
- institutional benchmarks;
- DataCamp and Pluralsight professional benchmarks.

Identify important convergence and divergence.

### `## 10. Literature-derived perspectives`

Compare the literature-derived benchmarks with the authoritative, institutional, and professional benchmark evidence.

Identify alignment, distinctive strengths, gaps, and concentrated or potentially non-generalizable perspectives.

Do not redesign the curriculum in this section.

### `## 11. Areas of convergence`

Identify findings with strong cross-source or cross-family support.

Explain why the evidence is strong.

### `## 12. Areas of disagreement or uncertainty`

Document meaningful disagreements, weak evidence, unresolved questions, and competing curricular interpretations.

Do not suppress disagreement to create artificial consensus.

### `## 13. Core, supporting, specialized, and uncertain elements`

Provide a consolidated classification of major elements as:

- core;
- supporting;
- specialized;
- uncertain or contested.

For each classification, provide the evidence rationale.

### `## 14. Implications for subsequent curriculum design`

Identify the **constraints and questions that the evidence creates for the next design stage**.

Examples include:

- capabilities that later design should account for;
- disciplinary-boundary constraints;
- sequencing questions;
- tensions requiring explicit design decisions;
- areas where evidence strongly constrains later choices;
- areas where designers retain substantial discretion.

Do **not** produce:

- a final syllabus;
- weekly schedule;
- module sequence;
- course title;
- final learning outcomes;
- final technology stack;
- final assessment structure.

Those belong to subsequent curriculum-design tasks.

### `## 15. Evidence map`

Provide a compact mapping from the major synthesis findings to the principal benchmark sources supporting them.

The purpose is traceability, not bibliography.

---

## Quality checks

Before completing the task, verify that:

- all four evidence families were examined;
- the analysis used substantive document content rather than primarily filenames or summaries;
- no external research was used to expand the corpus;
- DataCamp and Pluralsight were analyzed from their local benchmark documents rather than researched again;
- synthesis files from other agents were not consulted;
- the synthesis is organized around cross-source findings rather than document-by-document summaries;
- Analytics remains the organizing educational domain;
- contributing disciplines were analyzed according to their function within Analytics;
- Data Science was not automatically treated as synonymous with Analytics;
- Machine Learning did not become the organizing curriculum;
- Operations Research and Optimization did not become the organizing curriculum;
- Statistics did not become the organizing curriculum;
- Data Engineering did not become the organizing curriculum;
- Business Intelligence did not become the organizing curriculum;
- tools were not mistaken for curriculum identity;
- authoritative, institutional, and professional evidence were explicitly compared;
- literature-derived evidence was explicitly compared with the other evidence families;
- disagreements and uncertainties were preserved;
- evidence strength was assessed qualitatively rather than by simple frequency;
- major claims remain traceable to benchmark sources;
- no final curriculum was designed;
- exactly one agent-specific synthesis file was created.

---

## Completion condition

The task is complete when exactly one of the following appropriate files exists as the output of this execution:

- `design/synthesis/s03-synthesis-chatgpt.md`
- `design/synthesis/s03-synthesis-claude.md`
- `design/synthesis/s03-synthesis-gemini.md`

and that file satisfies the requirements above.
