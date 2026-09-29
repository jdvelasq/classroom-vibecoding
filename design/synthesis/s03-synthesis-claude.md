# Benchmark Synthesis

**Task:** `design/tasks/s03-review-benchmarks.md`
**Executor:** Claude (Claude Code)
**Date:** 2026-09-29
**Governing instructions:** `AGENTS.md` — Analytics is the curricular identity; the other fields are contributing disciplines.

---

## 1. Scope and method

### 1.1 Corpus analyzed

The corpus has 38 documents in five evidence families. It covers every file in `design/benchmarks/` plus the two professional-learning syntheses the task designates as inputs. The source identifiers below are used throughout.

The task text refers to "four evidence families" but defines five (authoritative, institutional, governmental, professional-learning, literature-derived). All five are treated here as distinct families.

**Authoritative (5 documents, 3 independent bodies)**

| ID | Document | Nature |
|---|---|---|
| A1 | `acm-computing-competencies-undergraduate-data-science-2021.pdf` | ACM Data Science Task Force body of knowledge. Eleven knowledge areas with T1/T2/Elective tiers and knowledge/skills/dispositions. Includes academic and industry surveys and chapters on program design and graduate characteristics. |
| A2 | `national-academies-data-science-for-undergraduates-2018.pdf` | National Academies consensus report. Covers "data acumen" key concept areas, data-scientist roles, educational modalities, ethics and a data science oath, findings and recommendations. |
| A3 | `informs-analytics-framework-2024.pdf` | INFORMS Analytics Framework: seven domains and 43 tasks spanning the analytics lifecycle, derived from a job-task analysis. |
| A4 | `informs-cap-essentials-blueprint.pdf` | CAP-Essentials exam blueprint. Subtasks and domain weights at entry level. |
| A5 | `informs-cap-pro-blueprint.pdf` | CAP-Pro exam blueprint. Subtasks and domain weights for "moderately complex" problems. |

A3–A5 come from one framework, so they count as **one** independent voice (INFORMS).

**Institutional (19 documents)**

| ID | Document | ID | Document |
|---|---|---|---|
| I1 | Berkeley Exec Ed, *IA: Estrategias y Aplicaciones de Negocio* | I11 | MIT xPRO, *Professional Certificate in Data Engineering* |
| I2 | Berkeley DATA C101 *Data Engineering* (catalogue entry) | I12 | MIT xPRO, *Professional Certificate in Data Science and Analytics* |
| I3 | Berkeley DATA C102 *Data, Inference, and Decisions* (catalogue entry) | I13 | MIT, *Quantitative Methods in Systems Engineering* |
| I4 | Cambridge Judge, *Business Analytics: Tomar decisiones a partir de los datos* | I14 | MIT xPRO, *Rapid Prototyping Methodologies* |
| I5 | MIT PE, *Cloud & DevOps* | I15 | PwC Business School, *Data & Analytics Academy Curriculum* |
| I6 | MIT PE, *Data Leadership* | I16 | Stanford Online, *AI for Senior Executives* |
| I7 | MIT IDSS, *Data Science and Machine Learning: Making Data-Driven Decisions* | I17 | USC ITP 249, *Introduction to Data Analytics* (syllabus) |
| I8 | MIT xPRO, *Designing and Building AI Products and Services* | I18 | UT Austin McCombs / Great Learning, *Agentic AI for Business Applications* |
| I9 | MIT PE, *Digital Platforms* | I19 | Warwick CS910, *Foundations of Data Analytics* (module spec) |
| I10 | MIT, *Machine Learning, Modeling, and Simulation Principles* | | |

**Governmental (1 document)**

| ID | Document | Nature |
|---|---|---|
| G1 | `governmental/mintic-talento-tech-2024-2026.pdf` | Colombian Ministry of ICT (MinTIC) project sheet for *Talento Tech*: 159-hour digital-skills bootcamps; six prioritised themes; target of 94,696 participants over 2024–2026; regional distribution; cohort calendar; inclusion targeting. |

**Professional-learning (2 derived syntheses)**

| ID | Document | Nature |
|---|---|---|
| P1 | `design/synthesis/s01-datacamp.md` | Task-generated reconstruction of DataCamp analyst and data-scientist tracks and certifications. Claims are labelled provider-stated [P], structural [S] or inference [I]. |
| P2 | `design/synthesis/s02-pluralsight.md` | Task-generated reconstruction of Pluralsight analytics and data-science paths, with the same labelling. |

**Literature-derived (12 documents)**

| ID | Document |
|---|---|
| L1 | `conf-origen-y-evolucion-business-analytics.pdf`: a historical account from RDBMS (1970) to agentic AI (2026) |
| L2–L11 | `dataops-01` … `dataops-10`, one lecture series. L2 problems, L3 data strategy, L4 methodologies, L5 lean, L6 agile, L7 DataOps definition, L8 CDO, L9 data engineer/scientist, L10 data quality, L11 organization |
| L12 | `prodig8-strategies-executing-analytics-projects.pdf`: Velasquez, Gallego & Cadavid (Universidad Nacional de Colombia), *Strategies for Executing Analytics Projects: Toward a Unified Framework of Methodologies*. A conceptual synthesis of 18 analytics-project methodologies into the PRODIG8 model. |

### 1.2 Method

- **Full reading.** Text was extracted from every PDF and the substantive content was read. Where documents were long (A1, A2, L12), the reading covered all findings, recommendations, knowledge-area specifications and result sections, not only tables of contents.
- **Image-only content was read visually:**
  - I18 (whole brochure);
  - G1's image tables (regional quota table; second cohort calendar);
  - A1's survey charts (Appendix B) could not be read, so only its narrative survey summary (A1 Ch. 2) was used.
- **P1 and P2 were used exactly as written in the local corpus.** No DataCamp or Pluralsight research was repeated.
- **Cross-source organization.** The synthesis is organized around findings that recur across sources, not around documents. Each claim is traced to source IDs, with locators (domain or task numbers, knowledge-area codes, modules, pages, sections) where useful.
- **Qualitative weighting.** Evidence was weighed by independence, the number of evidence families, explicitness, depth, relevance to Analytics, and shared origin. For example:
  - eight MIT brochures, many delivered by the same third-party providers, are not eight independent confirmations;
  - A3–A5 count as one voice;
  - L2–L11 count as one perspective;
  - L4 and L12 share a lifecycle structure (see 10.6).
- **Source statements vs synthesis.** Findings attributed to a source restate what the source says. Text labelled **Interpretation** is my synthesis.
- **Independence.** This synthesis was produced independently. No synthesis file by another agent, and no `s03-synthesis-*.md` or `s04-synthesis.md` file, was read, inspected or used. Such files were deleted in the working tree and were not opened.
- **How this run was conducted.** The same Claude session earlier executed a related task on the same PDFs and earlier versions of this task. Reading of the unchanged benchmark PDFs from that session was reused after checking that page counts and timestamps were unchanged. The two new documents (G1, L12) were read in full for this run. No external web research was performed.

### 1.3 Important limitations

1. **Thin authoritative base.** Only three independent authoritative bodies are present. Two of them (A1, A2) address *undergraduate data science*, not Analytics. The only framework that names Analytics as its object (A3–A5) is a professional-certification framework, not an educational one.
2. **Recency.** A2 (2018) and A1 (2021) predate generative and agentic AI.
3. **Institutional skew.**
   - 15 of 19 institutional documents are executive or professional brochures; only I2, I3, I17 and I19 are credit-bearing courses.
   - 8 of 19 are MIT.
   - Brochures show that a topic is included, rarely how deep it goes or how it is assessed.
   - Some sources are adjacent to Analytics rather than about it: I14 (physical prototyping), I9 (platform strategy), I5 (cloud/DevOps), I13 (systems-engineering tradespace).
4. **Governmental evidence is a single project sheet.** G1 names "Análisis de Datos" as a theme but specifies **no curriculum content, competencies or learning outcomes** for it. It informs policy positioning, audience, delivery format and scale — not what Analytics education contains. Its stated goal (94,696 people) and its regional quota table (30,175 + 39,713 + 19,890 = 89,778 certificates) do not reconcile within the document. This is recorded, not resolved.
5. **Professional evidence is second-hand and partial.** P1 and P2 are task-generated reconstructions of public pages. Both documents state their own limits (no complete catalogue; ordered display ≠ prerequisite; assessment internals not inspected). Both were also framed around an Analytics-vs-Data Science comparison, and that framing may shape what they foreground.
6. **Literature-derived concentration.**
   - Ten of the twelve literature-derived documents belong to one DataOps series. They give depth on process, operations and organization, but none on analytical methods.
   - L12 is conceptual and, by its own account, "has not yet been empirically evaluated" (L12 §6). Its corpus is English-only, from Scopus, 2010–2025.
   - L12's corresponding author (Juan D. Velasquez, Universidad Nacional de Colombia) has the same name as this repository's git author. If they are the same person, L12 represents the project team's own methodological perspective rather than an external benchmark. This bears on how much independent weight it should carry.

---

## 2. Analytics as an educational domain

### 2.1 What the corpus says Analytics is for

**Strong convergence: Analytics exists to improve decisions and actions using data.** Four of the five families state this explicitly:

- **Authoritative.** A3 describes applying analytics to "problems, questions, and opportunities enabling impactful business, research, medical, and other decisions" (p. 3). Its Domain I requires determining whether a problem is "amenable to an analytics solution" before anything else.
- **Institutional.**
  - I4 is titled "*tomar decisiones a partir de los datos*" and starts from decision traps and biases.
  - I17 frames the course as learning "to leverage data to make critical business decisions".
  - I19 describes going "from raw data to a deeper understanding… to support making predictions and decision making".
  - I7's subtitle is "Making Data-Driven Decisions".
  - I12 promises the ability to "optimize the decision-making process".
- **Professional.** P1's analyst role is answering business questions, calculating and reporting metrics, and making recommendations. P2's analyst foundation includes "data-driven problem solving" and stakeholder work.
- **Literature-derived.**
  - L1 (p. 2) gives the chain "*Datos → Analítica → Conocimiento → Decisiones → Valor*". L1 (p. 4) adds that analytics "does not eliminate uncertainty; it converts it into an informed decision".
  - L4 (p. 24) states "*Resultado analítico → Decisión → Acción → Resultado de negocio*", and L3 (p. 10) says data create value only "when they modify a decision, an action, a process, a product or a service".
  - L12 calls analytics "no longer an auxiliary function but a central driver of value creation" (p. 3). It holds that deployment requires "integrating predictive and prescriptive outputs directly into organizational decision workflows" (§4.7).

**The governmental family frames Analytics differently.** G1 lists "Análisis de Datos" as one of six digital-skill themes, alongside programming, AI, blockchain, cloud architecture and cybersecurity (p. 2). The justification is **employability and closing the digital-talent gap** (pp. 1–3), not decision-making.

**Interpretation:** the corpus supports its most defensible identity claim through four independent families. **Analytics is defined by its orientation to decision and action, not by a method family.** This is what separates it most consistently from the contributing disciplines (Section 3). The governmental evidence does not contradict this; it positions the field at a different level, as a labour-market skill.

### 2.2 Characteristic activities: a lifecycle, not a technique

**Strong convergence: Analytics work is an iterative, end-to-end lifecycle.**

- **A3–A5:** seven domains, "from initial business problem framing through data collection, model development, deployment, and maintenance" (A3 p. 3). The weights (A4/A5 p. 6) give problem framing (Domains I–II) about 32%, data 19%, method selection 15–16%, model development 15–16%, and deployment plus lifecycle management 17–19%. **Only about a sixth of the professional practice INFORMS assesses is "building models".**
- **A2:** the data science life cycle — "posing a question; collecting, cleaning, and storing data; developing tools and algorithms; performing exploratory analysis and visualization; making inferences and predictions; making decisions; and communicating results". It calls for "repeated exposure" to this cycle.
- **A1:** "doing machine learning" as a process, from the client's question to presented insights (ML-General, T1).
- **P2:** *The Data Analysis Workflow* is a core course of the analyst foundation, and the Data Science Foundations path runs from business problem to deployment and maintenance.
- **L4 and L12:**
  - L4: KDD → CRISP-DM → successors. The full lifecycle is problem → analytical problem → data → preparation → design → evaluation → operation → improvement, with governance running through all of it.
  - L12 derives a comparable architecture from 18 methodologies. Six core execution dimensions (Project Scope Definition, Data Understanding, Data Preparation, Project Design, Model Evaluation, Operation and Maintenance) are joined by Governance and Ethics as "transversal control" and Continuous Improvement as "adaptive feedback" (§4, Fig. 2).
  - L12 (p. 5) reports that the methodologies converge on five principles: "structured phases that translate business problems into analytical tasks", "iteration and feedback", "cross-functional collaboration", "data quality and reproducibility", and "increasing concern for ethical and governance dimensions".
- **I17:** the final project runs "identify a problem → collect → prepare/clean → analyze → visualize/dashboards/models → insights → solutions".

**Interpretation:** L12 and L4 share a structure, and L12 explicitly discusses the INFORMS process (p. 5). The lifecycle convergence among A3, L4 and L12 is therefore partly one tradition, not three independent confirmations. A2, A1 and P2 provide the independent support.

### 2.3 Where the corpus diverges on identity

The corpus supports **several distinct interpretations** of Analytics, and they should not be collapsed into one:

| Interpretation | Characterization | Principal support |
|---|---|---|
| **(a) Decision-science / lifecycle Analytics** | Analytics covers descriptive, diagnostic, predictive **and prescriptive** work and the full lifecycle from problem framing to lifecycle management. Business framing and deployment are integral. | A3–A5; I4; I12; I15; L1 ("Business Analytics… integrates data, mathematical, statistical and computational methods, with simulation, optimization and decision support", p. 36); L4; L12 |
| **(b) Analyst-role Analytics** | Analytics is the *data analyst* role: querying, cleaning, EDA, descriptive and inferential statistics, visualization, metrics, reports and dashboards, stakeholder communication. Predictive modelling and ML mark the step to Data Science. | P1 (analyst vs data-scientist tracks and certifications); P2 (Analytics Foundations vs Data Science Foundations); I17; A2's "business analysis" role (making sense of data "without necessarily relying on programming skills") |
| **(c) Analytics as the business-context label for Data Science** | "Those interested in the business context… generally use the term 'analytics'" (A1 §1.1). Analytics is not a separate discipline, just DS applied to business. | A1; implicitly I19 (a CS department module in a "Data Analytics" MSc, taught with data-mining and ML content) |
| **(d) Managerial / leadership Analytics** | Analytics as an organizational capability to commission, govern and exploit, needing literacy rather than technical execution. | I4 (no coding), I1, I6, I16, I15 masterclass ("Why analytics is every leader's problem"); L3, L8 |
| **(e) Data analysis as a short-cycle digital employability skill** | "Análisis de Datos" is one digital skill among several technology themes, acquired quickly through intensive, practice-based bootcamps for job placement. | G1 (pp. 1–3); partially P1 and P2 (no-prerequisite entry tracks) |

**Interpretation:** These interpretations are not mutually exclusive. The largest tension is between (a) and (b):

- Under (a), predictive and prescriptive modelling are part of Analytics.
- Under (b), the professional evidence places predictive modelling on the Data Science side of the boundary (P1: Data Science certification "adds modelling"; P2: Data Science "explicitly add[s] model lifecycle").

Prescriptive analytics (optimization and decision analysis) appears centrally in (a) and is **absent** from (b) (P1 §6 and P2 §6 record OR/optimization as "[Limit]" — not a verified common component).

Interpretation (e) matters for context rather than content. It shows that, in the corpus's only local public-policy source, data analysis is framed as a technology skill for employability and inclusion, not as a decision discipline.

### 2.4 Technical and contextual knowledge

**Strong convergence: technical capability must be combined with contextual understanding.**

- A1 Ch. 6 says graduates must understand "the mission, challenges, and constraints of the application domain so as to guide the focus of the analysis and the selection of methods".
- A2 makes "domain-specific considerations" a key concept area.
- A3 Domains I–II require stakeholder perspectives, business cases and baselines.
- P1 adds "business acumen" as a certified competency at the Data Scientist level.
- L1 (p. 61) lists domain analytics (HR, finance, marketing, inventory, demand, customer).
- L12 §4.2 says "domain expertise plays a decisive role" in interpreting data.

**Partial convergence on proportion.** The balance between the two varies from almost entirely contextual to almost entirely technical:

- Almost entirely contextual: I4, I16 (explicitly non-technical).
- Almost entirely technical: I11, I19, I10.

### 2.5 Unresolved identity questions

- Is predictive modelling *within* Analytics (A3, I4, I12, I15, L1, L12) or the *boundary* with Data Science (P1, P2)?
- Is prescriptive analytics a defining component (A3, I12, I15, L1, L4, L12) or specialized (absent from A1, A2, P1, P2)?
- Is operationalization, meaning deployment and monitoring, an Analytics responsibility or a supporting one?
  - A3 frames the analyst as supporting deployment.
  - L7–L10 and L12 treat it as part of the analytics lifecycle.
  - P2 assigns it to Data Science.
- Is Analytics a discipline requiring sustained education (A1, A2, L12 "mature interdisciplinary domain", §5.1)? Or a skill acquirable in 159-hour bootcamps (G1)?
- Is the target learner an executor or a consumer/commissioner of analytics? The corpus contains both kinds of program.

---

## 3. Analytics and contributing disciplines

The analysis below looks at the **function** each field serves inside Analytics, according to the corpus.

### 3.1 Data Science

- **Shared foundations.** P1 lists the same four competency areas for analyst and data-scientist certifications: data management, exploratory analysis, statistical experimentation and data communication. P2 finds business problem, data work, EDA and communication in both foundations. A1 and A2 describe "data science" with a lifecycle close to A3's.
- **Differentiation in the corpus.**
  - Data Science adds modelling and ML, "programming for data science" and business acumen (P1 §4–5).
  - It adds the model lifecycle (build/evaluate/deploy/maintain) and assumes 1–3 years of analyst or engineer experience (P2 §4).
  - It carries heavier computing expectations: A1's knowledge areas include OS, networks, compilers, big-data systems and software testing.
- **Function within Analytics.** Data Science supplies modelling depth and computational practice.

**Interpretation:** the corpus does **not** support treating Data Science and Analytics as synonyms. The professional evidence differentiates them. A3 defines an analytics lifecycle with no reliance on a data-science identity. Only A1 conflates them, and it does so explicitly from a computing perspective. L12 uses "analytics project" and "data science project" largely interchangeably when citing failure statistics (p. 3). The literature's terminology is not consistent either.

### 3.2 Machine Learning

- **Evidence.** ML is the most frequently present method family (A1 ML/DM; A2; I4, I7, I10, I12, I15, I19; P1 in data-science tracks; P2 in Data Science Foundations).
- **Function within Analytics.** ML is one of several means to the predictive part of the lifecycle.
  - A4/A5 treat it as a class of predictive methods chosen in Domain IV against the problem, the data and the resources.
  - L4 (pp. 18–19) is explicit: "*El modelo no es la solución*". A model identifies 10,000 at-risk customers, but the budget covers 1,000, so a decision layer is needed.
  - L12 places modelling within "Project Design", which uses "multiple statistical, computational, and machine learning techniques" (§4.4). ML is one phase of eight.
  - L2 lists "confusing model success with maximum accuracy" as a failure mode.
- **Interpretation.** ML's frequency reflects market salience, not structural centrality. In the frameworks that describe Analytics as a whole (A3, L4, L12), ML occupies a bounded position within a larger decision process.

### 3.3 Statistics

- **Evidence.**
  - Statistics is part of the *analyst* core in P1 (sampling, hypothesis testing, "statistical experimentation") and P2 (descriptive/inferential statistics, hypothesis testing in business context).
  - A2 lists variability, uncertainty, inference, confounding, causal inference and experiments among its foundations.
  - Institutional sources: I3, I4 (effect size, confidence intervals, experimentation), I7 (causal inference), I15 (inference, GLM, A/B testing), I19.
- **Function within Analytics.** Statistics provides reasoning under uncertainty, experimentation, and valid inference about effects and decisions. A2 insists on moving from randomized trials to "approaches that are applicable for nonrandomized studies" because business data are "found artifacts".
- **Interpretation.** Statistics is the contributing discipline with the most **independent** multi-family support as a *foundation*: authoritative, institutional and professional sources all place it early and centrally. The literature-derived and governmental families are silent on statistical method.

### 3.4 Operations Research and Optimization

- **Evidence.**
  - Prescriptive analytics is one of the analytics types INFORMS requires candidates to recognize, select, build (decision variables, constraints, objectives), verify and diagnose (A4/A5 tasks 4.1, 5.1–5.4).
  - Institutional support: I12 (five optimization modules), I15 (optimization and simulation; the decision-analytics masterclass "from predictions to prescriptions and actions"), I4 (two prescriptive modules), I10 (Monte Carlo simulation, optimization methods), I13 (trade studies, value models, Pareto fronts, sensitivity).
  - A2 lists "optimization" as a key mathematical concept.
  - Literature-derived: L1, L4, L12 ("predictive and prescriptive outputs" in decision workflows).
- **Absence.** P1 and P2 record no substantial optimization component in analyst or data-scientist paths. A1 includes only combinatorial/heuristic optimization algorithms (PDA T2) and planning and search. G1 does not mention it.
- **Function within Analytics.** Where present, OR converts predictions into choices under constraints — the step from "what will happen" to "what should we do".
- **Interpretation.** This is the sharpest cross-family disagreement in the corpus (see Section 12). The decision-oriented definition of Analytics that the corpus most strongly supports (Section 2.1) implies a decision layer. Yet the job-market professional evidence does not operationalize it.

### 3.5 Data Engineering

- **Evidence.**
  - A3's Data domain (19%) covers data needs, sources, architectures, management plans, acquisition, lineage and version control, and cleaning/joining.
  - A1 DG (mostly T1) and BDS; A2 "data storage and access" as a distinct role.
  - I11 is a whole certificate; I2 is a course.
  - P1 and P2 place Data Engineer as a separate role family (P2 names it an origin role for Data Science).
  - L7–L10 (pipelines, testing, environments) and L9 (canonical vs DataOps architecture).
  - L12 treats infrastructure as "a cross-cutting concern rather than a separate dimension" (Table 2, row 12).
- **Function within Analytics.** Data engineering supplies usable, trustworthy, accessible data and repeatable pipelines. The analyst needs to *specify, evaluate and use* data infrastructure: A4/A5 ask candidates to identify strengths and weaknesses of data architectures, not to build them.
- **Interpretation.** The professional evidence locates pipeline and platform work *beside* the analyst role (P1 §6: "locates platform/pipeline specialization beside, rather than as the definition of, the analyst/data-scientist structures").

### 3.6 Databases

- **Evidence.** SQL and relational concepts recur more consistently than any other technical element across families:
  - A4 (normalized datasets), A5 (relational database characteristics), A1 DG, A2 ("modern databases");
  - I17 (ER modelling, normalization, SQL, joins, subqueries, NoSQL), I19, I15, I6 (SQL for leaders), I11;
  - P1 (an entire SQL analyst career track and a Business Analyst skill track; SQL in the Data Scientist certification), P2 (SQL among analyst languages);
  - L1 (RDBMS history and SQL examples).
- **Function within Analytics.** Databases give access to organizational data and the ability to express business questions as queries and metrics. P1 describes SQL as a way to "answer business questions, calculate metrics, produce reports".

### 3.7 Business Intelligence

- **Evidence.**
  - I17 (BI systems, warehouses/marts, dashboards), I15 (PowerBI/Tableau/Qlik across courses), I6 (data reporting, modern data stack);
  - P1 (Tableau and Power BI as adjacent or specialized analyst variants), P2 (BI tools course in the analyst foundation; Tableau/Power BI certifications as adjacent);
  - A2 (dashboards for "situational awareness for decision makers");
  - L1 (BI 1.0 in 1989, BI 2.0 self-service in 1996, then the move from BI to analytics);
  - L12 (dashboards as core monitoring deliverables in Operation and Maintenance, §4.7).
- **Function within Analytics.** BI covers descriptive monitoring, reporting and self-service exploration.
- **Interpretation.** L1 presents Business Analytics as *extending* BI "by incorporating predictive and prescriptive models" (p. 36). This historical framing is echoed by A3's inclusion of predictive and prescriptive analytics. BI therefore appears as a *component* of Analytics (its descriptive layer), not its identity. The professional evidence (P1, P2) places BI closer to the core of the analyst role than the authoritative evidence does.

### 3.8 Artificial Intelligence

- **Evidence.**
  - A1 has an AI knowledge area (knowledge representation, probabilistic models, planning and search) and a deep-learning area (T2).
  - Generative and agentic AI appear only in:
    - institutional sources (I18 whole program; I16, I1, I8, I6, I12);
    - professional specializations (P2 *Generative AI for Data Science*; Azure language-model optimization in DP-100);
    - literature (L1: foundation models, AI-augmented analytics, agentic AI; L12 §6 notes generative AI "may redefine governance expectations").
  - G1 lists AI and data analysis as **separate** themes (p. 2).
- **Function within Analytics.** The corpus shows AI in two functions:
  - as **analytical method** (deep learning and NLP for unstructured data);
  - as **augmentation or automation of analytical work** (P2: GenAI "across a Data Science workflow"; L1: "AI begins to execute analytical tasks"; I18: agents automating business workflows).
- **Interpretation.**
  - P2 explicitly treats GenAI as "a specialized workflow augmentation… it does not define the general foundation path".
  - G1 also keeps AI distinct from data analysis.
  - Executive programmes built around AI (I1, I16, I18) are *AI* programmes for business audiences, not Analytics programmes.
  - The corpus does not support AI redefining Analytics. It does support AI changing how analytical work is performed.

### 3.9 Summary: what makes an architecture recognizably Analytics

Each item below states the recurring evidence.

1. **Decision orientation governs method selection.** A3 Domain IV; A4/A5 4.1–4.2; L4 p. 16: "*Pregunta → tipo de analítica → familia de métodos*"; L12 §4.5 (deployment decisions based on "predictive accuracy and the capacity to generate measurable business value").
2. **The descriptive → diagnostic → predictive → prescriptive span is a single organizing framework.** A4/A5 4.1.1; I4; I12; I15 masterclass; L1 p. 37; L4 p. 16. Contributing disciplines each tend to cover only part of it.
3. **The full lifecycle, with governance transversal.** It includes framing, validation, deployment and value tracking. A3; L4; L12.
4. **Communication to non-experts and stakeholder alignment as competencies.** A1 PR T1; A2; A3–A5; P1; P2.

**Interpretation:** a curriculum that is recognizably Analytics under AGENTS.md would show these four integrating properties, whichever contributing-discipline content it selects.

---

## 4. Recurring capabilities

The capabilities below emerged from the corpus rather than from a predetermined taxonomy. For each, "families" are Authoritative (A), Institutional (I), Governmental (G), Professional (P) and Literature-derived (L). G1 specifies no capabilities, so it rarely appears here.

### C1. Framing problems for analysis

- **Meaning:** understand a business or organizational need; identify stakeholders; decide whether it is amenable to analytics; translate it into an analytical question with assumptions, constraints, success measures and a baseline.
- **Evidence:**
  - A3–A5 Domains I–II (about a third of the exam weight).
  - A2 ("ability to understand client needs"; framing questions well).
  - A1 Ch. 6 ("knowledge and goal acquisition").
  - I8 (Lawler model), I13 (framing early decisions, value models), I15 ("analytics must be problem-driven").
  - P1 (certification practical begins with "review a business problem"), P2 (DS Foundations begins with "identifying/understanding business problems").
  - L4 (business problem → analytical problem; avoid "drive-by analytics"), L6/L7 (epic hypothesis statements).
  - L12 §4.1: "a business analytics project must always start with an explicit and multidimensional scope definition that integrates business needs, technical feasibility, and stakeholder alignment"; scope treated as "iterative, evolving".
- **Families:** A, I, P, L.
- **Convergence:** strong.
- **Variation:** INFORMS treats framing as a formal, assessable domain. Professional sources treat it as a first step, and executive programmes as a strategic judgement. L12 widens it to include feasibility, ethics and "whether AI is the appropriate solution".

### C2. Obtaining, integrating and managing data

- **Meaning:** identify data needs and sources, acquire data, query (SQL), join and integrate, understand data structures and architectures, and document lineage.
- **Evidence:** A3–A5 Domain III; A1 DG; A2 data management and curation; I17, I19, I11, I15, I6; P1 (SQL track, "data management" competency), P2 (reading and working with data, joins); L1, L3, L9; L12 §4.2–4.3 (collection, integration, harmonization).
- **Families:** A, I, P, L.
- **Convergence:** strong.
- **Variation:** the depth runs from conceptual (I6, A4) through query-level (I17, P1) to engineering (I11). A1 expects algorithm development for data governance, well beyond what other families expect.

### C3. Assessing and preparing data

- **Meaning:** evaluate data quality (accuracy, completeness, consistency, timeliness, validity, uniqueness), clean, transform, handle missing data and outliers, and construct features.
- **Evidence:**
  - A4/A5 3.5–3.6; A1 DG-Data Cleaning (T1); A2 ("more than 70 percent" of project effort).
  - I4, I15, I19; I1 ("data quality, representativeness and why models fail").
  - P1 and P2 (cleaning and wrangling recur in every analyst route).
  - L10 (data tests, statistical process control), L7, L4.
  - L12 §4.2–4.3 (quality dimensions; preparation "iterative, adaptive, and highly path-dependent"; "resource-intensive").
- **Families:** A, I, P, L.
- **Convergence:** strong.
- **Variation:** literature-derived evidence frames quality as documented, automated process control. The other families frame it as analyst diagnosis.

### C4. Exploring, describing and visualizing data

- **Meaning:** use descriptive statistics, data profiling, EDA, and sound visual displays and dashboards to understand data and detect problems.
- **Evidence:** A2 (EDA, grammar of graphics, dashboards); A1 AP (T1); A4/A5 3.6.2–3.6.3; I17, I15, I7, I4; P1 (EDA and visualization in every analyst route), P2 (visualization course; EDA); L1 (BI); L12 §4.2 (exploratory reports, "descriptive dashboards" as intermediate deliverables).
- **Families:** A, I, P, L.
- **Convergence:** strong.

### C5. Reasoning with uncertainty and evidence

- **Meaning:** sampling; estimation; hypothesis testing; experimentation (A/B testing); confounding and causal reasoning; distinguishing correlation from effect.
- **Evidence:**
  - A2 (the strongest statement).
  - I3, I4 (a whole module on experimentation), I7 (causal inference), I12 (interpretability and causality), I15 ("Why experiments are the foundation of analytics").
  - P1 ("statistical experimentation" as a certified competency), P2 (hypothesis testing in business context).
  - L5 (validated learning, split tests; indirect).
- **Families:** A, I, P.
- **Convergence:** strong for inference and hypothesis testing; partial for causal inference (A2, I3, I7, I12 only).

### C6. Selecting analytical approaches

- **Meaning:** match the question to a type of analytics and a family of methods, given data, time, resources and technology; justify the choice.
- **Evidence:**
  - A3–A5 Domain IV (15–16%), including "technical and business benefits of one methodology over another" (A5 4.2.1).
  - A1 ML T1 ("For a given data-driven question, explain why a particular approach is appropriate").
  - L4 p. 16. L12 §4.4 (multiple candidate models critically evaluated). I12 ("apply, interpret, and explain key analytical frameworks").
- **Families:** A, I, L.
- **Convergence:** moderate. The capability is explicit in the authoritative and literature-derived evidence, but the professional evidence rarely names it.
- **Interpretation:** it is nonetheless central to the decision orientation (Section 3.9).

### C7. Building and evaluating predictive models

- **Meaning:** specify inputs and outputs; train, validate and test; use appropriate metrics; diagnose overfitting and bias; interpret output.
- **Evidence:**
  - A1 ML/DM (T1 core); A2 (modeling and assessment); A4/A5 5.1–5.4.
  - Institutional: nearly universal.
  - P1 (data-scientist tracks), P2 (DS Foundations).
  - L12 §4.4–4.5 (evaluation against "technical and business success criteria", validation on unseen data).
  - L1 (historical), L9 (ML technical debt).
- **Families:** A, I, P, L.
- **Convergence:** strong that the capability matters; *disputed* as to whether it belongs to the Analytics core or to Data Science (Section 2.3).

### C8. Prescribing and deciding

- **Meaning:** formulate decisions (decision variables, constraints, objectives); optimize; simulate; analyze trade-offs, risk and sensitivity; turn predictions into actions; account for decision biases.
- **Evidence:** A3–A5 (prescriptive tasks); A2 (optimization in maths); I12, I15, I4 (including behavioural biases), I10, I13, I3 (decision theory); L4 (churn case), L1, L12 (prescriptive outputs in decision workflows, §4.7).
- **Families:** A (INFORMS only), I, L. **Absent in P and G.**
- **Convergence:** moderate and contested (see Section 12).

### C9. Interpreting and communicating results

- **Meaning:** explain results, assumptions and limitations to non-technical audiences; tell stories with data; produce reports, dashboards and presentations; document.
- **Evidence:**
  - A1 PR-Communication (T1: "situation reports for senior managers"), A2 (jargon-free writing, presentation), A3–A5 (5.6, 6.2, 7.6; A5 5.6.1 "most appropriate non-technical explanation").
  - I17 ("Tell compelling stories with data"), I12, I15.
  - P1 ("communicating insights to stakeholders"; Data Scientist certification requires a recorded presentation), P2 (*Communicating with Data*; results for technical and non-technical stakeholders).
  - L11 (data storytelling for data product owners).
  - L12 treats communication as "an output/activity rather than a new execution dimension" (Table 2, row 17), embedded in documentation and stakeholder deliverables.
- **Families:** A, I, P, L.
- **Convergence:** strong. It is the capability with the most uniform support across families.
- **Variation:** its *status* differs. It is a first-tier competency in A1, A2, P1 and P2, but a cross-phase output in L12.

### C10. Validating, deploying and sustaining solutions

- **Meaning:** business validation; production requirements; deployment testing; monitoring against baselines; recalibration; tracking value and side effects over time.
- **Evidence:**
  - A3–A5 Domains VI–VII (17–19%); A1 ML T2 (transition to production).
  - I2 ("reliable, scalable operationalization"), I11, I12 (Part 5), I18 (testing and evaluating agentic systems).
  - P2 (DS Foundations "deploy/maintain"; DP-100 endpoints and monitoring).
  - L4 (monitoring, degradation, retrain/replace/retire), L7–L10 (DataOps), L1 (MLOps).
  - L12 §4.7–4.8: "deployment is understood not as a final step but as the beginning of an ongoing operational lifecycle"; monitoring, retraining, human-in-the-loop.
- **Families:** A, I, P, L.
- **Convergence:** strong that it matters. The disagreement is over *whose* capability it is (Section 12).

### C11. Acting responsibly

- **Meaning:** privacy, confidentiality and security; bias and fairness; transparency; governance roles; legal awareness; unintended consequences.
- **Evidence:**
  - A2 Rec. 2.4 (ethics "woven into the… curriculum from the beginning and throughout"), A1 PR and DPSIA (T1), A3–A5 (sensitive data, biased training data, ethical risks, side effects).
  - I4 (GDPR, anonymization), I12 (fairness module), I19 (differential privacy), I6, I16, I18.
  - P2 (privacy and ethics in the analyst foundation; fairness and SHAP labs in DP-100; responsible use in GenAI).
  - L3 (responsible use; governance as decision rights), L4 (transversal governance).
  - L12 §4.6: "Governance and Ethics" as a transversal control dimension "rather than a discrete or final step", aligned with EU Trustworthy AI guidelines.
- **Families:** A, I, P, L.
- **Convergence:** strong on importance; divergent on placement (Section 12). P1 does not visibly treat it — an absence, possibly a limitation of the reconstruction.

### C12. Working with tools and computational workflows

- **Meaning:** use at least one analytical language or environment; reproducible workflows; version control; notebooks; evaluate a technology stack; learn new tools.
- **Evidence:**
  - A2 (workflow and reproducibility), A1 PDA/SDM (T1), A4/A5 4.4 (technology stack; spreadsheet strengths and weaknesses).
  - Tool use appears in all technical institutional programmes.
  - P1 (Python/R/SQL routes), P2 (SQL/Python/R comparison; Excel/Alteryx paths).
  - L7 (version control, environments, tests), L1 (open data science ecosystem).
  - G1 (programming as a separate prioritized theme).
- **Families:** A, I, P, L, (G).
- **Convergence:** strong for *some* computational proficiency; weak for *which* tools (Section 8).

### C13. Collaborating and working within organizations

- **Meaning:** teamwork across multidisciplinary roles; conflict resolution; stakeholder and sponsor alignment; working in agile/lean analytics processes; understanding roles.
- **Evidence:**
  - A1 PR-Teamwork (T1), A2 (multidisciplinary teams), A3–A5 (sponsor and stakeholder alignment recurs in Domains I, II and VI).
  - I17 (team project with peer evaluation), executive programmes (I1, I6, I16).
  - G1 (bootcamp pedagogy includes "desafíos individuales y en equipo", agile methodologies and collaboration, p. 1).
  - P2 (stakeholder work; "soft skills").
  - L6, L8 (relational coordination), L11 (team structures, T/Pi/M-shaped skills).
  - L12 ("cross-functional collaboration" as a convergent principle; project management "embedded across" the lifecycle, Table 2, row 13).
- **Families:** A, I, G, P, L.
- **Convergence:** strong at the level of teamwork. Organizational design and management methods are concentrated in L and in executive institutional programmes.

### C14. Creating and demonstrating value

- **Meaning:** build a business or value case; estimate costs and benefits; prioritize; measure realized value; revalidate the business case.
- **Evidence:** A3–A5 (1.5, 7.4; A5 1.5.4 trade-offs of benefits and costs), A1 PR-Economic (T2); I15 masterclass, I8 (organization case), I16, I1; L3 (value case with NPV/ROI, prioritization, roadmap), L6 (benefit estimation, MVP); L12 §4.1 (success criteria extending "toward business impact, adoption, satisfaction").
- **Families:** A, I, L.
- **Convergence:** moderate. It is explicit in INFORMS and the literature; P1 names "business acumen" only generically.

---

## 5. Knowledge architecture

The corpus supports a layered architecture. **Interpretation:** the layers below are my synthesis. The sources do not present a single layered model, but the layers reflect how the sources position knowledge.

### 5.1 Foundational knowledge

- **Statistical reasoning:** variability, sampling, inference, testing, experimentation. Sources: A2; A1 (as required complement); I3, I4, I7, I15, I19; P1, P2.
- **Quantitative and mathematical foundations:** probability, linear algebra, calculus, optimization, graphs.
  - A2 lists the concepts "important for all students": set theory and logic, multivariate functions, probability, linear algebra, networks and graph theory, optimization.
  - A1 Ch. 3 names calculus, discrete structures, probability, statistics and linear algebra. Ch. 6 names "multivariate calculus, linear algebra, optimization, and graph theory".
  - Institutional support is uneven: I19, I10, I7, I15 ("Math for Modelers"). I4, I1 and I16 assume no maths.
  - P2 notes that DS needs "mathematical… knowledge". P1 and G1 are silent.
- **Data concepts:** data types, structures, relational model, data quality dimensions. Sources: A1 DG, A4/A5 Domain III, A2; I17, I19; P1, P2; L12 §4.2.
- **Analytical-process concepts:** analytics types (descriptive, diagnostic, predictive, prescriptive); lifecycle models (IAF, CRISP-DM, KDD, PRODIG8). Sources: A3–A5; L1, L4, L12; I4, I12, I15.

### 5.2 Enabling knowledge

- **Computation and programming:** algorithmic thinking, a scripting language, data structures. Sources: A1 PDA; A2 computational foundations; P1, P2; G1 (programming theme); most technical institutional programmes.
- **Data management and engineering:** SQL, databases, integration and ETL, warehouses and lakes, pipelines. Sources: A1 DG/BDS; A3; I11, I17; L1, L9.
- **Reproducible workflow and software practice:** version control, documentation, testing, notebooks, environments. Sources: A2, A1 SDM; L7; L12 (documentation artefacts, reproducibility principle); I11.
- **Visualization and reporting technology:** BI tools, plotting libraries. Sources: I15, I17; P1, P2.
- **Scalable and cloud infrastructure:** Sources: A1 BDS (T2); I5, I11; P2 (Spark specialization); G1 (cloud architecture theme); L1. L12 treats infrastructure as cross-cutting.

### 5.3 Analytical methods

- **Descriptive and exploratory methods** (EDA, profiling, summary metrics, segmentation): A, I, P and L families.
- **Inferential and experimental methods:** A2; I3, I4, I7, I15; P1, P2.
- **Predictive modelling:** regression, classification, clustering, dimension reduction, ensembles, validation. Sources: A1, A2, A4/A5; I (nearly all technical programmes); P (data-science side); L12.
- **Prescriptive methods:** optimization, simulation, decision analysis. Sources: A3–A5; I4, I10, I12, I13, I15; L4, L12.
- **Advanced / unstructured-data methods:** deep learning, NLP, recommenders, networks, time series. Sources: A1 (T2/E), A2; I7, I12, I15, I1; P2 specializations.

### 5.4 Contextual and decision-oriented knowledge

- **Problem framing and business understanding:** A3; L4, L12; I4, I8, I13.
- **Value, cost and benefit, prioritization:** A3, A1 PR-Economic; L3; I15.
- **Decision-making under uncertainty and cognitive biases:** I4 (decision traps, sunk cost, risk aversion), I16 (scenario planning), I13; L2 ("decisions still based on experience and intuition").
- **Ethics, privacy, governance and law:** A1, A2, A3–A5; I4, I6, I12, I16, I19; P2; L3, L4, L12.
- **Organizational context:** data strategy, analytics maturity, team structures, agile/lean analytics, project methodology. Sources: L2–L12; I1, I6, I15, I16; A1 PR (teamwork, economics).
- **Domain knowledge:** A1 (at least one domain context; a majority of surveyed programmes require one); A2; L1; L12; delivered through cases in I4, I7, I12.
- **Policy and societal context:** digital-talent gaps, inclusion and regional equity (G1: targeting of ethnic groups, women, people with disabilities, victims; regional quotas). Only G1 supplies this, and only as context.

### 5.5 Specialized or optional knowledge

The evidence for each item is concentrated or role-specific:

- **Time series and forecasting:** I15 (full course), I10; A1 DM-Time Series is *Elective*.
- **Networks and graphs:** I7, I19, I15; A2 as maths.
- **Recommender systems:** I7, I12, I3, I4.
- **Text mining and NLP:** I15, I12, I1; A1 DM (T2/E).
- **Big data platforms, streaming and IoT:** I11; P2 (Spark); A1 BDS (T2/E); L12 (DMME sensor-based contexts, as an engineering specialization).
- **Deep learning:** A1 (T2), I7, I12, I1, I4.
- **Generative and agentic AI:** I18, I16, I1; P2 specialization; L1.
- **MLOps and cloud ML platforms:** P2 (DP-100), I5, L1, L7, L12 §4.8.
- **Survival analysis, Bayesian hierarchical models, reinforcement learning:** I15; I3; I3/I11/I4/A1 respectively.
- **Systems-engineering tradespace, rapid prototyping, digital platforms:** I13, I14, I9.
- **Adjacent digital themes (blockchain, cybersecurity):** G1 lists them beside data analysis; A1 DPSIA covers security. They are not Analytics content.

### 5.6 Relationships among layers

- **Methods serve decisions.** Several sources make explicit that methods are chosen for the question, and that analytical outputs matter only when they feed decisions: A3 Domain IV; L4 p. 16; L12 §4.5; I15 ("from descriptions to predictions… to prescriptions and actions").
- **Data work precedes and constrains modelling, iteratively.** A3 Task 3.8 ("validate and update the business and analytics problem statements" after data findings); A2 (garbage in, garbage out); L4; L12 §4.2–4.4 (bidirectional interaction between modelling and data work).
- **Context and ethics span all layers rather than forming a final layer.** A2 Rec. 2.4, A1 Ch. 7, L4 p. 27, L12 §4.6. **Interpretation:** this is a relationship claim, not a placement claim, and institutional practice often contradicts it (Section 12).

---

## 6. Learning progression

### 6.1 Progression explicitly stated in sources

| Statement | Source |
|---|---|
| Analyst learning progresses "from language basics to advanced analysis". The Associate Data Scientist route runs Python essentials → EDA and statistical hypothesis testing → predictive ML. | P1 [P] |
| Paths are "step-by-step" with Skill IQ placement and module skipping. The Data Science foundation *presupposes* 1–3 years as analyst or engineer. | P2 [P] |
| T1 for all graduates, T2 for most, E for electives. Compulsory classes are T1/T2; later electives are T2/E. A final-year major project that integrates several classes is an E item. An early motivational introductory course is recommended. | A1 Ch. 3–4 |
| An integrated approach should be "introduced in their first courses and remain a consistent theme"; "repeated exposure to the data science life cycle"; "experiential learning at multiple time points". | A2 Ch. 2 |
| Essentials → Pro: simple → intermediate → moderately complex problems; univariate → multivariate profiling; train/test split → cross-validation; "identify" → "identify the most appropriate". Several deployment and lifecycle subtasks are "not tested" at the Essentials level. | A4 vs A5 |
| Explicit prerequisite chains: Introduction to Statistical Methods → Regression/Multivariate → GLM → Time Series. The intermediate course requires the beginner course plus 3 months of post-training application. | I15 |
| Beginner programming path vs "no prior engineering experience" managerial paths. | I1, I4, I18 |
| Entry via an admission and knowledge test; 159-hour intensive cohorts of about three months. | G1 (pp. 2, 4) |
| Methodologies evolved from sequential pipelines to iterative, governance-aware lifecycles. Phases are "not a strictly linear sequence" but a "controlled lifecycle". | L12 §4, §5 |

### 6.2 Progression recurring structurally across benchmarks

- **Foundations (language, statistics, data handling) before modelling.** P1, P2; I7 (Python/statistics weeks 1–2, then unsupervised, regression, classification, deep learning); I11 (Python/SQL → engineering → big data/ML); I12 (fundamentals → optimization → ML → advanced ML → deployment).
- **Data handling before analysis before communication and projects.** I17 (data modelling → SQL → NoSQL → BI → visualization → project); P1 analyst tracks; P2 Analytics Foundations (practical application grouping last).
- **Descriptive → predictive → prescriptive.** I4 (descriptive M2 → predictive M5–6 → prescriptive M7–8); I12 (a partial variant, with optimization placed before ML); I15 masterclass; L1 (historical sequence BI → data mining → business analytics).
- **Lifecycle order as course order.** P2 DS Foundations (problem → collection → cleaning → EDA → modelling → communication → deployment); L4; L12 execution dimensions.
- **Integrative project at the end.** I1, I8, I12, I14, I16, I17, I19; A1 (final-year project).

### 6.3 Progression inferred analytically

**Interpretation:** across families, the recurring movement is:

1. handling data;
2. describing and exploring it;
3. inferring and predicting;
4. deciding and prescribing (where present);
5. delivering and sustaining solutions (where present).

Communication and ethics are applied throughout this movement *in principle*, but they are often taught late *in practice*. Complexity also grows along a second axis: from guided exercises (P1 in-browser exercises; I10 per-module assignments) to integrated, ill-posed problems (A2; capstones).

L12's insistence that the lifecycle is iterative rather than linear supports a spiral reading of the sequence. Its authors do not claim this as a pedagogical sequence.

### 6.4 Competing sequencing models

| Model | Logic | Supporting sources |
|---|---|---|
| **Foundations-first** | Tools, maths and statistics before application | P1, P2; I7, I11; A1/A2 undergraduate structures |
| **Whole-cycle-early (spiral)** | Experience the complete lifecycle early, then deepen repeatedly | A2 (explicit); I18 (project weeks after each block); I12 (portfolio built across modules); I1/I16 (one project developed through every module); L12 (iterative lifecycle, by analogy) |
| **Problem/decision-first** | Start with decisions, problems and biases, then bring in data and methods | I4 (Module 1: decision biases); A3 (Domain I first); L4 and L12 (scope definition first); I13 (framing early decisions) |
| **Analytics-type ladder** | Descriptive → predictive → prescriptive | I4; I15; L1; A4/A5 analytics typology |
| **Lifecycle-ordered** | Follow the order of project phases | P2 DS Foundations; I17; L4; L12 |
| **Role ladder** | Analyst → data scientist → specialist | P1 (associate → data scientist certification); P2 (analyst experience required for DS); A4 → A5 |
| **Intensive bootcamp** | Compressed, practice-led cohort after an admission test | G1; partially I18 (12 weeks with project weeks) |

Unresolved sequencing questions evidenced by the corpus:

- **Where ethics goes:**
  - "from the beginning and throughout" (A2, A1);
  - a late module (I4 M9, I12 M16, I6 M8, I16 Phase IV);
  - transversal (L4, L12).
- **Where optimization goes:** before ML (I12) or after prediction (I4, I15, L4).
- **Programming entry point:** none required (I4, I1, I16); an optional code or no-code track (I18); introductory with no prerequisites (P1, P2 Analytics); an admission/knowledge test (G1); assumed (P2 DS, P2 Spark).
- **Where deployment goes:** included only for advanced or professional levels (A4 marks several deployment subtasks "not tested at this level"; P2 places it in DS rather than Analytics foundations), or integrated as a normal lifecycle phase (L4, L12, A3).

---

## 7. Practice and authentic analytical work

### 7.1 Forms of practice evidenced

| Form | Evidence | Families |
|---|---|---|
| **Integrative projects and capstones** | A1 (major final project; "a comprehensive project to bring all the pieces together"); A2 (capstones as high-impact practices; "longer-term projects involving interim reports"). Institutional: I1, I8, I9, I12, I14, I16 (capstones); I17 (team project); I19 (project, 35%); I18 (three project weeks); I15 (guided project; action-learning projects). Professional: P1 (projects and portfolio; certification practical). | A, I, P |
| **Simulated real work situations** | G1: the classroom "simulates real work situations" with individual and team challenges; "Learning by doing"; mentors; agile methodologies (p. 1). A2: ill-posed problems. P1: certification practical. | G, A, P |
| **Realistic, messy data and ill-posed questions** | A2: "insufficient… to be handed a 'canned' data set"; "ill-posed questions and 'messy' data". A1 §4.2: "real data used in an appropriate context". P1: real-world datasets (Netflix, public schools, crime, sales, manufacturing). I17: teams collect their own data. | A, I, P |
| **Case studies** | I4 (Netflix, UPS ORION, Google Oxygen, TalkTalk, Carter Racing, SmartService); I7 ("50+ case studies"); I12 (BlueBike, Filatoi Riuniti, facial analysis); I10 (Aurora, Schlumberger, BASF); I5, I6, I1, I9, I18 (15+ cases). L1 (House of Cards, Moneyball, UPS); L3 (predictive maintenance); L4 (churn, running through the whole lecture); L12 (application contexts such as supply chain, curriculum analytics and predictive maintenance, cited from its methodologies). A2: case studies for ethics. | I, L, A |
| **Exercises and labs** | P1 (in-browser coding exercises; practice challenges); P2 (labs in specialization and certification paths; "cannot be claimed" for every foundation path); I17 (a lab each session); I11, I8 (Jupyter exercises); I10 (graded assignments per module). | I, P |
| **Portfolios** | I7 (3 projects), I11 (GitHub), I12, I18; P1 (portfolio). | I, P |
| **Professional outputs** | Reports, dashboards and recommendations (P1; I17; I15); business validation reports (A4/A5 6.2); situation reports for senior managers (A1 PR T1); executive summaries and AI project proposals (I8, I16, I1); presentations (P1 recorded presentation; I14, I16); project charters and data description, exploration and quality reports (L12 §4.1–4.2). | A, I, P, L |
| **Team work and peer evaluation** | I17 (2–3 members; peer evaluation 25% of the project grade); A1 (team software project, SDM T1); A2 (multidisciplinary teams); G1 (team challenges). | A, I, G |

### 7.2 Pedagogical functions practice serves

The corpus shows practice serving **all four** functions. Different evidence families emphasize different ones:

1. **Reinforcement after instruction.**
   - P1: in-browser exercises after lessons.
   - I10, I13: a graded assignment per module.
   - I15: a day-end test.
   - This is the dominant form in professional and short institutional offerings.
2. **Organizing mechanism.**
   - G1: bootcamp pedagogy is explicitly built on "learning by doing", "resolving practical problems" and a classroom that simulates the workplace.
   - I1 and I16: a single project developed throughout the programme.
   - I18: project weeks structure the calendar.
   - I12: assignments accumulate into the capstone portfolio.
   - I14: the capstone spans modules 5–8.
   - A2 is the authoritative voice for organizing learning around repeated full-cycle practice.
3. **Assessment.**
   - I17: homework and labs 30%, project 10%, exams 60%.
   - I19: project 35%, problem sets 15%, exam 50%.
   - P1: certification practical ("review a business problem, validate data and calculate metrics", auto-graded) and a Data Scientist recorded presentation.
   - P2: Skill IQ, practice exams.
   - A4/A5: an entire exam blueprint of lifecycle subtasks.
   - G1: admission and knowledge test; completion certificates ("constancias").
4. **Professional simulation.**
   - G1 (explicit).
   - P1 certification practical.
   - L4: a stakeholder request ("what was our retention rate last year?") reframed into a decision problem.
   - I4 and I15: management-decision cases.
   - A2: ill-posed problems.

**Interpretation:** practice is *universally present* but *unevenly positioned*:

- Authoritative evidence (A2 especially) treats practice as the primary means of developing data acumen.
- Governmental evidence treats practice as *the* pedagogy.
- Professional evidence treats it mainly as reinforcement and certification.
- Institutional executive programmes treat it as organizing, through a personal capstone.
- Literature-derived evidence supplies worked decision cases (L4) and lifecycle deliverables (L12). These show *why* practice must reach decisions, deployment and governance rather than stopping at models (L4 p. 3: "a good model does not guarantee a good analytics project"; L12 p. 3 cites that "approximately 87% of data science projects never reach production").

Assessment detail is thin across the corpus: few sources publish weights or rubrics.

---

## 8. Tools and technologies

### 8.1 Durable conceptual capabilities (tool-independent)

These capabilities recur independently of any particular technology:

- querying and joining relational data;
- data cleaning and validation;
- reproducible, version-controlled and documented workflows;
- visualization principles;
- model validation;
- evaluating a technology stack.

On the last point, A4/A5 4.4 cover databases, analytics software, networking, security, on-premise vs cloud and open-source vs proprietary, and the strengths and weaknesses of spreadsheet models.

The authoritative sources explicitly favour durable capability over specific tools:

- A2: "It is more important for students to learn how to follow the information technology frontier than to master the details of today's architecture."
- A1 Ch. 6: "be able to learn new languages and new libraries when needed".
- A1 Ch. 7: "different communities prefer different languages".

L12 criticises early methodologies' "tool-oriented design" (p. 4) and describes a transition "from tool-centered, static process models" (§5).

### 8.2 Technology landscape

| Category | Technologies | Where they appear | Status (interpretation) |
|---|---|---|---|
| **Query / relational** | SQL, PostgreSQL, MySQL, SQLite | A4/A5 (relational concepts), A2, A1; I17, I19, I11, I6, I15; P1 (SQL track; DS certification), P2; L1 | **Widely recurring, cross-family.** The most consistent technical element in the corpus. |
| **Analytical languages** | Python (pandas, NumPy, Matplotlib, Seaborn, scikit-learn, statsmodels); R (tidyverse, ggplot2) | A1 (Python, R named); A2 (R and Python); I7, I11, I12, I18 (Python); I15, I19 (R and Python); P1 (parallel Python and R routes); P2 (SQL/Python/R compared; Python path) | **Widely recurring.** The *choice* between Python and R is not settled; P1 and P2 both treat them as alternatives. |
| **Spreadsheets** | Excel, Access | I17; I15 (prerequisite); I12 (prerequisite familiarity); P2 (Excel for Data Analysts); A4/A5 (spreadsheet models) | **Recurring enabling tool**, especially at entry level. |
| **BI / dashboards** | Tableau, Power BI, Qlik | I17, I15; P1 (adjacent or specialized), P2 (BI course; certifications adjacent) | **Recurring but vendor-specific.** Professional sources position vendors as variants. |
| **Notebooks and environments** | Jupyter, Google Colab, RStudio | A2 (R Markdown, Jupyter); I7, I11, I12, I18; P2 (RStudio); L1 | Recurring enabling tools. |
| **Version control and software practice** | Git/GitHub, Docker, CI/CD | A2 (version control); A1 SDM; I11, I5; L7, L9; L12 (TDSP's "automation, version control, and continuous integration", p. 4) | Recurring in engineering-oriented sources; durable as a *practice*. |
| **Low-code / no-code** | Alteryx, n8n, visual automation; Weka | P2 (Alteryx); I18 (no-code track); I6 (no-code models); I19 (Weka); L1 (trend) | Emerging or alternative route; contested (Section 12). |
| **Big data and distributed** | Hadoop, Spark, Hive, Kafka, Airflow, NiFi, Dask | A1 Ch. 7 (Spark/Hadoop clusters); I11; P2 (Spark specialization); L1 | **Specialized.** |
| **Cloud and ML platforms** | AWS, Azure ML, AutoML, Kubernetes, serverless | I5; P2 (DP-100); A4/A5 (cloud vs on-prem as a concept); G1 ("Arquitectura en la nube" as a theme) | **Specialized / provider-specific.** |
| **Deep learning frameworks** | TensorFlow, Keras, PyTorch | A1 DL (T2); I11, I12 | Specialized. |
| **GenAI / agent tooling** | ChatGPT, LLM APIs, LangChain, LangGraph, LangSmith, MCP, vector databases, RAG | I18; P2 (GenAI path); I6; L1 | **Transient and rapidly changing.** Named frameworks are version-bound. |
| **Adjacent technology domains** | Blockchain, cybersecurity, cloud architecture | G1 (prioritised themes beside data analysis); I5; A1 DPSIA | **Not Analytics content.** Policy lists group them with data analysis, but no family treats them as Analytics. |
| **Legacy or niche** | SAS, MongoDB, Cassandra, gnuplot, Perl, Java, Node.js, Mapbox, ThingsBoard | I17, I19, I11 | Provider- or course-specific. |

### 8.3 Implications documented (not selected)

1. **Proficiency in *some* analytical computing environment and in SQL-style querying is expected across families.** The *specific* environment varies by role and provider.
2. **Two parallel access routes to Analytics exist in the corpus:** code-based and low-code/no-code (Excel, Alteryx, BI tools, n8n). Executive programmes go further and teach *about* tools without using them (I4 "no requiere codificación").
3. **Tool frequency is a poor proxy for curricular importance.**
   - Tableau and Power BI are frequent in institutional and professional sources, yet P1 and P2 both place them as adjacent or specialized variants.
   - GenAI tools are highly salient but, in P2, are explicitly a specialization.
   - G1's list of trending technology themes (blockchain, cloud, cybersecurity) must not be read as a definition of Analytics. The task instructions say so, and nothing else in the corpus places those themes inside Analytics.
4. **Tool evaluation and selection is itself an assessed capability** in the only analytics-specific authoritative framework (A4/A5 4.3–4.4).

---

## 9. Authoritative, institutional, and professional perspectives

This section also positions the governmental family (9.7), because the required structure has no separate governmental section.

### 9.1 Where professional evidence reinforces authoritative principles

- **Lifecycle and workflow.** P2's *Data Analysis Workflow* course and DS Foundations ordering mirror A2's life cycle and A3's domains.
- **Communication.** P1 certification (communicating insights; recorded presentation) and P2 (*Communicating with Data*; technical and non-technical stakeholders) operationalize A1 PR-Communication T1 and A3–A5 5.6.
- **Statistics as foundation.** P1 "statistical experimentation" and P2 "descriptive and inferential statistics, hypothesis testing" match A2's statistical foundations.
- **Ethics and privacy.** P2's analyst foundation includes privacy and ethics, matching A1 and A2. P1 is silent in the reconstruction.
- **Business problem as starting point.** P1 practical ("review a business problem"); P2 DS Foundations ("identifying/understanding business problems"). Both correspond to A3 Domain I.

### 9.2 Where professional evidence operationalizes abstract competencies

- **Concrete tools.** A2's "modern databases" and "workflows" become SQL/PostgreSQL window functions, pandas, dplyr and ggplot2 in P1.
- **Measurable professional output.** A3's "document and communicate findings" becomes "calculate metrics, produce reports and dashboards, make recommendations" (P1 Business Analyst).
- **Placement and progression.** P2's Skill IQ placement and module skipping put into practice A1's tiering and A2's "multiple pathways for students of different backgrounds" (Finding 4.1).

### 9.3 Where professional evidence adds capabilities or emphasis

- **Role differentiation.** Analyst vs associate data scientist vs data scientist vs ML engineer vs data engineer (P1, P2). A2 also names roles (infrastructure, storage and access, modelling and ML, visualization, business analysis), but only professional evidence ties them to distinct learning structures.
- **Career-oriented portfolios and certification** (P1). Institutional professional programmes echo this (I7, I11, I12 career services and portfolios).
- **Tool-specific specialization as modular add-ons** (P2: Excel, Alteryx, Spark, Azure paths).
- **Low-code analyst workflows** (P2 Alteryx: "repeatable/automated workflows").

### 9.4 Where professional evidence diverges from authoritative framing

1. **Prescriptive analytics and optimization are absent** from professional role structures (P1 §6, P2 §6). INFORMS treats them as one of the analytics types, and A2 lists optimization as a key concept.
2. **Predictive modelling is placed outside Analytics** (P1, P2), whereas A3–A5 include predictive model development in Analytics practice.
3. **Deployment is Data Science work** in P2, while A3 includes deployment and lifecycle management in Analytics practice (17–19% of exam weight).
4. **Maths.** Professional analyst routes have no stated maths prerequisites (P1 "no prerequisites"). A1 and A2 require substantial maths. P2 names maths only for DS.
5. **Breadth vs. modularity.** Authoritative sources describe integrated wholes; A1 warns that "a random collection of the three elements does not constitute a meaningful Data Science program". Professional sources are modular and role-specific, and P2 allows skipping modules.
6. **Durable concepts vs named tools.** A2 favours following the frontier. Professional tracks are organized by tool and language (Python vs R vs SQL routes).

### 9.5 Institutional evidence in this comparison

Institutional evidence **spans both positions**:

- **Business-school and executive programmes (I4, I12, I15)** align with INFORMS. They cover descriptive → predictive → prescriptive analytics, business framing, experimentation and organizational issues.
- **Credit-bearing and technical programmes (I17, I19, I2, I3)** align more with the analyst and data-science views: databases, statistics, mining and ML. The exception is I3, which is explicitly about "inference and decisions" (decision-making, causal inference, optimal control).
- **AI and leadership programmes (I1, I6, I16, I18)** introduce content that neither authoritative nor professional analyst evidence treats as core: AI strategy, agentic systems, futures thinking.

**Interpretation:** institutional evidence is not a middle ground. It shows the *range* of market-facing interpretations, and it is the family in which the decision-oriented identity is most often operationalized with prescriptive content.

### 9.6 Relative contribution of each family

- **Authoritative:** the conceptual scope (A1, A2), a lifecycle definition of analytics practice with relative weights (A3–A5), and educational principles (integration, ethics throughout, real data, capstones).
- **Institutional:** compact operationalizations, applied cases, and the most direct evidence of prescriptive and decision content in teaching.
- **Professional:** role boundaries, entry-level progression, tool modularity, certification-style assessment.

None of the three alone would support the synthesis. The professional evidence is *not* inherently more current in scope: it omits optimization and says nothing about agentic AI beyond one GenAI path. The authoritative evidence is *not* inherently decisive either: it predates GenAI and is largely about data science rather than Analytics.

### 9.7 Governmental evidence in relation to the other families

G1 adds a distinct kind of evidence — **local public-policy positioning** — that no other family supplies:

- **Audience and purpose.** Mass upskilling (94,696 target) of young people and adults for employability, with explicit inclusion targeting and regional distribution across all Colombian departments (pp. 2–3).
- **Delivery model.** 159-hour bootcamps, in-person and virtual, in cohorts of about three months, preceded by an admission and knowledge test (pp. 2, 4).
- **Pedagogy.** "Learning by doing", simulation of real work situations, individual and team challenges, agile methods, mentors, learner-centred (p. 1). This converges with A2's emphasis on real problems and with professional-learning practice. It is the most explicit statement in the corpus of practice as the *organizing* mechanism.
- **Positioning of the field.** Data analysis is one of six "most demanded" digital themes. Bootcamps are described as operating "outside traditional educational systems", "lack[ing] accreditation" and "not follow[ing] standard curricula" (p. 2).

**Divergence from the other families:**

- G1 frames data analysis as a *technology skill*, not a decision discipline (compare Section 2.1).
- It specifies no competencies. Its alignment with any content is therefore unknowable from the document.

**Interpretation:** G1 constrains *context* (audience, format, national priorities) far more than *content*. Following the task instruction, it is not treated as an international standard, and its technology list does not define Analytics.

---

## 10. Literature-derived perspectives

### 10.1 Areas of strong alignment

- **Lifecycle and decision orientation.**
  - L4's lifecycle (problem → analytical problem → data → preparation → design → evaluation → operation → continuous improvement, with transversal governance) aligns closely with A3's seven domains and A2's life cycle. L4's end-to-end churn case is the most concrete illustration in the corpus of A3 Domains I–VII.
  - L12 aligns with the same lifecycle. It also explicitly discusses the INFORMS Analytics Process as "a professional standard of practice widely adopted in industry" (p. 3) and as "a governance-oriented bridge between business objectives and technical execution" (p. 5).
- **Data quality.** L10 and L12 §4.2–4.3 align with A4/A5 3.6 and A2's emphasis on cleaning. They add automated testing (L10) and documentation artefacts (L12).
- **Ethics and governance as transversal.** L4 pp. 27–29 and L12 §4.6 align with A2 Rec. 2.4 and A1 Ch. 7.
- **Historical positioning of Analytics relative to BI, data mining and data science.** L1 aligns with A1 §2.2 (INFORMS business analytics curriculum) and A3's analytics types.

### 10.2 Distinctive strengths and depth

- **Systematic methodological synthesis** (L12).
  - PRODIG8 is the only document in the corpus that systematically derives an analytics-project architecture from a defined literature base: a Scopus forward-citation expansion, 699 records → 18 methodologies (Table 1).
  - It separates *execution* (six dimensions), *control* (Governance and Ethics) and *adaptation* (Continuous Improvement).
  - It records which methodologies end at deployment (CRISP-DM, SEMMA) and which extend to operation (TDSP, MAISTRO) (p. 5).
- **Operationalization and DataOps practice** (L7–L10): tests at every pipeline stage, version control, branch/merge, multiple environments, containers, parameterization, statistical process control. No other family treats these at this depth. A3 Domains VI–VII state the *what*; L7–L10 and L12 §4.7–4.8 supply the *how*.
- **Data strategy as a decision system** (L3): diagnosis → value opportunities → capability gaps → objectives → initiatives → governance, architecture and responsible use → value case and prioritization → roadmap → execution → evaluation.
- **Management of analytics work** (L5, L6; L12 on agile/CRISP-DM hybrids): lean waste in analytics, value stream mapping, theory of constraints, Scrum/Kanban/SAFe, the DataOps manifesto.
- **Organizational design** (L8, L11): relational coordination, team structures, T/Pi/M-shaped profiles.
- **Failure analysis** (L2; L12 p. 3): myths and real problems. L12 cites that about 87% of data science projects "never reach production" and that over 80% of organizations lack a formal methodology. These are secondary citations of Saltz & Krasteva (2022).
- **Historical perspective** (L1): 50 years of analytics technologies and concepts, ending in foundation models, AI-augmented analytics and agentic AI.

### 10.3 Areas receiving more attention than the other families would suggest

- Agile, lean, DataOps and project-methodology management (eleven documents including L12), compared with limited treatment elsewhere (A1 SDM project management T2; I5 DevOps).
- Organizational structure and CDO-level concerns. Only executive institutional programmes approach this.
- Data strategy. It is echoed by I6 and I16 but otherwise absent.
- Operation, maintenance and continuous improvement. These are heavily weighted in L and INFORMS but assigned to Data Science by P2 and deferred by A4.

### 10.4 Areas receiving less attention

- **Analytical methods of every kind:** statistics, ML, optimization, visualization design. The literature-derived family is essentially silent on method content beyond historical naming (L1), method-type mapping (L4 p. 16), and generic references to "statistical, computational, and machine learning techniques" (L12 §4.4).
- **Mathematical foundations:** absent.
- **Communication and storytelling:** appears only as role skills (L11). L12 treats communication as an output rather than a dimension.
- **Education and learning progression:** none of the literature-derived sources addresses how to teach. L12 notes only that PRODIG8 "can inform… methodological curricula in analytics education and professional certification" (p. 27).

### 10.5 Useful cases and analytical patterns

- Churn: retention request → decision problem → prediction + optimization under budget → deployment → degradation → governance issues (L4).
- Predictive maintenance: data strategy, gap analysis and capability objectives (L3). Also sensor-based DMME contexts (L12).
- Netflix *House of Cards*, Moneyball, UPS ORION: value of analytics for decisions (L1).
- The "5 whys" analysis of slow analytics delivery (L5).
- The epic hypothesis statement for anti-money-laundering ML (L6/L7).
- PRODIG8's **execution–control–adaptation** pattern, and its **structural reconciliation operations** (add, rename, merge, split). The latter are an analytical pattern for comparing methodologies (L12 §3.3).

### 10.6 Concentrated perspectives that should not automatically constrain later design

- The ten DataOps documents come from **one series and one perspective**. That perspective is valuable for operational maturity, but its volume reflects how the corpus was curated, not independent convergence.
- **L4 and L12 share one lifecycle structure.**
  - L4's phases — business problem, data understanding, data preparation, project design ("*Diseño del proyecto*"), model and solution evaluation, operation and maintenance, continuous improvement, and transversal governance and ethics (L4 pp. 9–29) — correspond almost one-to-one to PRODIG8's eight dimensions.
  - They should be read as one methodological perspective, not two confirmations.
  - L12's possible authorship link to the project (Section 1.3, item 6) increases the need to weigh this perspective as internal rather than external.
- **L12 is conceptual and unvalidated by its own account.** Its corpus is English-only, and it acknowledges that generative AI "may redefine governance expectations" (§6).
- **Internal tensions should be preserved and not generalized.** L2 lists "following CRISP-DM and waterfall models" as a real problem. L1 and L4 present CRISP-DM as foundational, and L12 calls it "the conceptual backbone of modern analytics methodologies" while noting its limits (p. 4).
- The DataOps emphasis on organizational and process management relates most to operating analytics teams at scale. Its relevance to every analytics learner is **not established** by the other families.

---

## 11. Areas of convergence

Each finding below is supported by at least three families and by independent sources within them. Shared origin is noted where relevant.

1. **Decision and action orientation defines Analytics.**
   - A: A3 (p. 3, Domain I).
   - I: I4, I7, I12, I17, I19.
   - P: P1 (business questions, recommendations), P2 (data-driven problem solving).
   - L: L1, L3, L4, L12.
   - Why strong: explicit statements in four families, from sources with distinct origins (a professional society, universities, commercial providers, a lecture series, a methodology review). G1 is the exception: it frames the field as an employability skill.
2. **The analytics lifecycle is the organizing frame for professional practice.**
   - A: A2, A3–A5.
   - I: I17 project structure; I12.
   - P: P2 workflow course and DS ordering.
   - L: L4, L6, L12.
   - Why strong: A2 and P2 are independent of the INFORMS/PRODIG8 tradition. L12 adds a systematic consolidation of 18 external methodologies.
3. **Data acquisition, quality and preparation are foundational and effort-intensive.**
   - A: A1 T1; A2 ("70 percent"); A4/A5 (Data is the highest-weighted domain).
   - I: I17, I19, I15.
   - P: P1, P2 (repeated in every analyst route).
   - L: L10, L12.
4. **Statistical reasoning, including hypothesis testing and experimentation, is a shared foundation of analyst and data-science preparation.** A: A2. I: I3, I4, I7, I15, I19. P: P1, P2.
5. **Communication to non-technical stakeholders is a core, assessed capability.**
   - A: A1 T1; A2; A3–A5 (repeatedly).
   - I: I17, I12.
   - P: P1 (certification presentation), P2.
   - L: L11, L12 (as output).
6. **SQL / relational data access recurs.** A: A4/A5, A1, A2. I: I17, I19, I6, I11, I15. P: P1, P2. L: L1.
7. **Responsible analytics matters, and governance runs across the lifecycle.**
   - A: A1, A2, A3–A5.
   - I: I4, I12, I19, I6, I16.
   - P: P2.
   - L: L3, L4, L12.
8. **Learning should involve realistic, integrative, applied work.**
   - A: A1 (capstone, real data), A2 (messy data, capstones).
   - I: capstones in 7+ programmes.
   - G: G1 (learning by doing; simulated work).
   - P: P1 (projects, practicals).
   - L: case-based lectures L1, L3, L4.
   - This finding has the broadest family support: all five families.
9. **Predictive modelling is important somewhere in the Analytics/Data Science space.** All method-bearing families agree. The *placement* is disputed (Section 12).
10. **Tools are enabling, not defining.**
    - A: A2, A1 (explicit).
    - P: P1 (language alternatives; "does not establish that any one is universally necessary"), P2 (programming *comparison* course; tool paths as modular specialization).
    - L: L12 (critique of "tool-oriented design").

---

## 12. Areas of disagreement or uncertainty

| # | Disagreement | Position 1 (sources) | Position 2 (sources) | Assessment |
|---|---|---|---|---|
| D1 | **Is prescriptive analytics / optimization part of Analytics' core?** | Yes: A3–A5 (prescriptive tasks in Domains IV–V), A2 (optimization as a key mathematical concept), I4, I12, I15, I10, I13, L1, L4, L12 | Not visible: P1, P2 (optimization "not a substantial verified common component"), A1 (only algorithmic optimization), G1, I7, I11, I17, I19 | **Contested.** It is the component most tied to the decision-oriented identity, yet absent from job-market role structures. |
| D2 | **Is predictive modelling inside Analytics or the Data Science boundary?** | Inside: A3–A5, I4, I12, I15, I19, L1, L12 | Boundary: P1 (certification "adds modelling"), P2 (DS "adds model lifecycle") | **Contested.** It reflects role-level vs. field-level definitions. |
| D3 | **Who owns deployment and lifecycle management?** | Analytics supports it: A3 ("actively support"); A4 marks several deployment subtasks "not tested" | Part of the analytics lifecycle: L7–L10, L12, I2, I11; Data Science owns it: P2 | **Contested.** Depends on role and organizational model (L11). |
| D4 | **Programming expectations** | None: I4, I1, I16; optional or no-code: I18, P2 (Alteryx/Excel paths) | Required: A1 (one or two languages; Linux; clusters), A2, I11, I19; P1 (language-based tracks), P2 DS (Python/Scala prerequisites); G1 treats programming as a separate prioritized theme | **Contested.** The corpus supports both code and no-code routes into analytics practice. |
| D5 | **Mathematical expectations** | Substantial: A1 (calculus, linear algebra, discrete maths, probability), A2 (all-student maths list; "math for data science" course), I10, I19 | Minimal or unstated: P1, P2 analyst paths, I4, I1, I16, I17, G1 | **Contested.** A2 itself suggests streamlined, tool-supported maths pathways. |
| D6 | **Where and how ethics is taught** | Pervasive from the start: A2 Rec. 2.4, A1 Ch. 7, L4, L12 | Late or dedicated module: I4 M9, I12 M16, I6 M8, I16 Phase IV; P2 one course | **Disagreement between principle and practice.** |
| D7 | **Lifecycle methodology** | CRISP-DM as foundation or backbone: L1, L4, L12 (with extensions) | CRISP-DM/waterfall as a problem: L2; A3 proposes its own framework; L12 proposes PRODIG8 as a unified successor; L4 lists successors (CRISP-ML(Q), Agile CRISP-DM) | **Partial.** The corpus agrees on an iterative lifecycle, not on a methodology. |
| D8 | **Technical vs managerial orientation** | Build analytics: I11, I19, I10, P1, P2 | Commission and govern analytics: I4, I1, I6, I16, I15 masterclass, L3, L8 | **Both evidenced.** A2 names both kinds of role. The target learner is undetermined. |
| D9 | **Role of BI** | Central to the analyst role: P2 (BI tools course in the foundation), I17, I15 | Descriptive layer superseded or extended by analytics: L1; peripheral in A1/A2 | **Partial.** |
| D10 | **Role of generative and agentic AI** | Transformative for analytics work: L1, I18, I16 | Specialization: P2; separate theme: G1; absent: A1, A2, A3–A5, P1; L12 flags it as a future revision need | **Uncertain.** Authoritative evidence predates the topic. |
| D11 | **Causal inference** | Early and essential: A2, I7, I3, I12 | Absent: A1, P1, P2 (hypothesis testing only), most technical programmes | **Uncertain / under-evidenced.** |
| D12 | **Concepts vs practice balance** | Concept-integrated, with capstones: A1, A2 | Practice as the pedagogy: G1; practice-dense and tool-first: P1 (in-browser exercises), I11 (portfolio per section); decision-case-dense: I4, L4 | **Varies by family.** Practice is universal; its function differs (Section 7.2). |
| D13 | **Employer vs academic priorities** | Academics: security and privacy required | Employers did not report security and privacy as required; they wanted more computing than statistics (A1 §2.3) | Recorded within A1. A1 interprets it as reflecting the applicant pool. |
| D14 | **Discipline vs short-cycle skill** | A sustained, integrated discipline: A1 (degree programmes; "a random collection… does not constitute a meaningful program"), A2 (majors, minors), L12 ("mature interdisciplinary domain", §5.1) | A skill acquirable in 159 intensive hours outside standard curricula: G1; entry-level professional tracks of 36–39 hours (P1) | **Contested at the level of educational format and depth.** |
| D15 | **Status of communication** | A first-tier, assessed competency: A1 PR T1, A2, A5 5.6.1, P1, P2 | An output or activity within lifecycle phases, not a dimension: L12 Table 2 (row 17) | **Partial.** Both views agree on importance; they differ on its structural status. |

**Weak evidence (not disagreement):**

- Assessment design, including rubrics, weights and how to assess ethics or communication.
- Depth expectations for methods beyond A1's tiers and A4 vs A5.
- Specialized methods: time series, networks, text, spatial data.
- Visualization design principles, which appear only as mentions in A1 and A2.
- Graduate-level expectations: no authoritative source addresses graduate or continuing education directly.
- The competency content of the one governmental programme.
- Empirical validation of the one systematically derived process model (L12).

---

## 13. Core, supporting, specialized, and uncertain elements

This classification is analytical. It is **not** a syllabus.

### 13.1 Core

Strongly supported across multiple independent families and central to Analytics' identity:

| Element | Rationale |
|---|---|
| Decision- and action-oriented problem framing (C1) | A, I, P, L; the most weighted INFORMS domains; the defining identity claim (Section 2.1) |
| Analytics lifecycle as the organizing frame, iterative rather than linear | A2, A3–A5; P2; I17; L4, L12 |
| Obtaining, integrating and querying data, including SQL/relational concepts (C2) | Cross-family; the most consistent technical element |
| Data quality assessment and preparation (C3) | A1 T1, A2, A4/A5; P1, P2; L10, L12 |
| Exploratory, descriptive analysis and visualization (C4) | A, I, P, L |
| Statistical reasoning, inference and experimentation (C5, excluding advanced causal methods) | A2; I3, I4, I7, I15; P1, P2 |
| Selecting analytical approaches matched to questions (C6) | A3–A5 Domain IV; A1 ML T1; L4, L12. *Moderate direct support*, but constitutive of the decision orientation |
| Interpreting and communicating results to stakeholders (C9) | The most uniform cross-family support |
| Responsible analytics, with governance across the lifecycle (C11) | A, I, P, L on importance; A2, A1 Ch. 7, L4 and L12 on transversality |
| Computational proficiency in *some* analytical environment, plus reproducible and documented workflow habits (C12, as capability rather than tool) | A, I, P and L on proficiency; A2, L7 and L12 on reproducibility |
| Integrated, practice-based work on realistic problems | All five families |

### 13.2 Supporting

Clearly useful, but primarily enabling core capabilities:

| Element | Rationale |
|---|---|
| Mathematical foundations (probability, linear algebra, calculus, optimization concepts) | Required by A1 and A2 to enable methods; depth contested (D5) |
| Programming, data structures and algorithmic thinking | Enables C2–C7; A1 PDA, A2; G1 programming theme |
| Database design and data architecture awareness | A4/A5 architecture identification, A1 DG; enables C2 |
| Software-engineering practice (version control, testing, environments) | A1 SDM, A2, L7; enables reproducibility and deployment |
| BI and dashboard tooling | Enables C4 and C9; vendor-specific (P1, P2) |
| Spreadsheets | Entry-level enabling tool (I15, I17, P2; A4/A5) |
| Teamwork and collaboration (C13) | A1 T1, A2, G1, L12; enables delivery |
| Value and business-case reasoning (C14) | A3–A5, L3, L12; enables framing and prioritization |
| Domain knowledge | A1, A2, L12 require it; delivered through cases |
| Knowledge of lifecycle methodologies (CRISP-DM, IAF, PRODIG8 and others) | Enables C1–C10 coordination; L4, L12, A3; no single methodology is endorsed across families (D7) |

### 13.3 Specialized

Relevant to particular roles, contexts or advanced applications:

| Element | Rationale |
|---|---|
| Deep learning, NLP, computer vision | A1 T2; several institutional; P2 specializations |
| Time series and forecasting | I15, I10; A1 Elective |
| Networks and graphs; recommender systems | I7, I12, I19, I15 |
| Big-data platforms, streaming, distributed processing, sensor/IoT analytics | A1 BDS T2/E; I11; P2 Spark; L12 (DMME contexts) |
| Cloud ML platforms and MLOps tooling | P2 DP-100; I5; L1; L12 §4.8 |
| Data engineering pipelines at production scale | I11, I2; P1/P2 separate role family |
| Organizational design, data strategy, agile/lean management of analytics | L2–L12; executive institutional programmes |
| AI strategy and leadership | I1, I6, I16 |
| Systems-engineering tradespace, rapid prototyping, digital platforms | I13, I14, I9 (adjacent) |
| Blockchain, cybersecurity, cloud architecture as themes | G1 (adjacent policy themes); not Analytics content |

### 13.4 Uncertain or contested

| Element | Why |
|---|---|
| **Prescriptive analytics (optimization, simulation, decision analysis)** | Strong in INFORMS, business programmes, L4 and L12; absent in professional, governmental and data-science authorities (D1). Closely tied to Analytics' identity. |
| **Placement of predictive modelling / ML** | Everyone agrees it is important; its status as core Analytics vs the Data Science boundary is disputed (D2) |
| **Deployment, monitoring and lifecycle management as learner capability** | Heavy INFORMS weight and L depth; P2 assigns it to DS; A4 defers it to higher levels (D3) |
| **Causal inference beyond basic experimentation** | A2 insists on it; few others include it (D11) |
| **Generative and agentic AI** | High salience in recent institutional and literature-derived sources; specialization in P2; a separate theme in G1; absent from authoritative sources (D10) |
| **Required programming and mathematical depth** | D4, D5 |
| **Low-code / no-code routes as legitimate primary routes** | P2 (Alteryx), I18, I4 vs A1/A2 expectations |
| **Educational format: sustained discipline vs short-cycle bootcamp** | D14 |
| **Dispositions** (A1 CC2020 list) | Isolated evidence (A1 only) |

---

## 14. Implications for subsequent curriculum design

The evidence creates the constraints and questions below. It does not supply a design.

### 14.1 Capabilities later design should account for

- **The core list in 13.1**, especially the capabilities that other families under-represent but that define Analytics:
  - problem framing (C1);
  - approach selection (C6);
  - interpretation and communication (C9);
  - value reasoning (C14).
- **A decision layer.** The corpus's defining claim (Section 2.1) implies that analytical results must connect to decisions and actions. Designers must decide *how* that connection is taught — through prescriptive methods, decision analysis, experimentation, or decision-oriented cases. They cannot omit it without contradicting the identity the corpus supports.
- **Governance as transversal rather than terminal.** Supported by A2, A1, L4 and L12. It contradicts common institutional practice, so a design decision is needed.

### 14.2 Disciplinary-boundary constraints (per AGENTS.md)

- Organizing around the ML lifecycle alone would align with the professional *Data Science* structures (P1, P2), not with the Analytics identity. The corpus's most frequent method family (ML) is not its organizing principle (Section 3.2).
- Organizing around SQL, BI and dashboards alone would align with the analyst-role interpretation (2.3b). It would omit the predictive and prescriptive span that A3–A5, the business-school institutional programmes and L1/L4/L12 treat as characteristic.
- Organizing around optimization alone would reflect OR's internal logic. The corpus shows optimization serving decisions *after* framing and data work (L4, I4, I15).
- Organizing around data pipelines alone would replicate the separate data-engineering role family (P1, P2, I11).
- Organizing around a project methodology alone (for example PRODIG8 or CRISP-DM) would give process structure but no analytical-method content, since the literature-derived family is method-silent (10.4). It would also over-weight one concentrated perspective (10.6).
- Adopting a governmental theme list (G1) as scope would import adjacent technology domains (blockchain, cybersecurity, cloud) that no family treats as Analytics.
- **Verification test suggested by the evidence:** does the architecture display the four integrating properties in 3.9 (decision orientation governing method choice; the analytics-type span; the full lifecycle with transversal governance; stakeholder communication)?

### 14.3 Sequencing questions requiring explicit decisions

1. Foundations-first vs whole-cycle-early (spiral) vs problem-first vs intensive practice-led formats (Section 6.4). All are evidenced, and A2 explicitly supports early whole-cycle exposure.
2. Whether ethics and governance are taught pervasively (the authoritative and literature position) or in a module (common institutional practice) (D6).
3. Where prescriptive content sits relative to predictive content (I12 before; I4, I15, L4 after).
4. At what level deployment and lifecycle management enter (A4 vs A5; P2; L12).

### 14.4 Tensions requiring explicit design decisions

- **Target learner:** builder vs commissioner of analytics (D8). This determines programming and maths depth (D4, D5).
- **Educational format and depth:** sustained programme vs short-cycle skill acquisition (D14). This is relevant where the local public-policy context (G1) prioritises mass, intensive, employability-oriented training.
- **Code vs no-code routes** (D4; P2 Alteryx; I18 tracks).
- **Breadth vs depth.** Integrated wholes (A1, A2) vs modular, role-specific structures (P1, P2).
- **Currency vs durability of tools.** A2's "follow the frontier" vs professional tool-specific tracks (Section 8).
- **Status of GenAI/agentic AI:** as method, as augmentation of analytical work, or as specialization (D10).
- **Weight given to the DataOps/PRODIG8 perspective,** given its concentration and possible closeness to the project team (1.3, 10.6).

### 14.5 Areas where the evidence strongly constrains choices

- A curriculum lacking realistic, integrative, decision-oriented practice would contradict all five families.
- A curriculum lacking data quality and preparation, communication or responsible-analytics content would contradict cross-family convergence.
- Treating tools as the curriculum identity would contradict A1, A2, P1, P2 and L12's own caveats.

### 14.6 Areas where designers retain substantial discretion

- the specific languages and tools (Python vs R; BI vendor; cloud provider);
- the selection among specialized methods (13.3);
- the lifecycle methodology to teach (CRISP-DM, IAF, PRODIG8 or others) (D7);
- the depth of big-data, cloud and MLOps content;
- whether and how to respond to the local policy context (G1);
- assessment structure, for which the evidence is thin.

---

## 15. Evidence map

| Finding | Principal sources | Families |
|---|---|---|
| Analytics defined by decision/action orientation | A3 p. 3 & Domain I; I4; I7; I12; I17; I19; P1 §3; P2 §3; L1 pp. 2, 4, 36; L3 p. 10; L4 p. 24; L12 p. 3, §4.7 | A, I, P, L |
| Data analysis framed as a digital employability skill | G1 pp. 1–3 | G |
| Lifecycle as organizing frame; modelling is only a minority of practice | A3; A4/A5 p. 6 weights; A2 Ch. 2 life cycle; P2 *Data Analysis Workflow*, DS Foundations ordering; L4; L12 §4, Fig. 2, p. 5 principles; I17 project | A, I, P, L |
| Five competing interpretations of Analytics' identity | A1 §1.1; A3; P1 §5; P2 §5; I4; I16; L1; G1 | A, I, G, P, L |
| DS ≠ Analytics; DS adds modelling/programming/model lifecycle | P1 §4–5; P2 §4–5; A1 §1.1 (conflation); A3 | A, P |
| ML is bounded within a decision process | A4/A5 4.1–4.2; L4 pp. 18–19; L12 §4.4–4.5; L2 p. 3 | A, L |
| Statistics as the shared foundation | A2 statistical foundations; P1 §3–5; P2 §3; I3, I4, I7, I15, I19 | A, I, P |
| Prescriptive/OR contested | A4/A5 4.1, 5.2; A2 maths; I4 M7–8; I12 M9–13; I15; I10; I13; L4 p. 18; L12 §4.7 vs P1 §6, P2 §6, A1, G1 | A, I, L vs P, G |
| Data work foundational and effort-intensive | A2 (70%); A1 DG T1; A4/A5 Domain III 19%; P1; P2; L10; L12 §4.2–4.3 | A, I, P, L |
| SQL as the most consistent technical element | A4 3.2.6; A5 3.2.6; I17 wks 2–7; I19; I6; I11; I15; P1 SQL tracks; P2; L1 pp. 6–7 | A, I, P, L |
| Communication as core; status contested | A1 PR-Communication T1; A2; A5 5.6.1, 7.6.1; P1 DS certification presentation; P2 *Communicating with Data*; I17; L12 Table 2 row 17 | A, I, P, L |
| Ethics and governance transversal in principle; placement disputed | A2 Rec. 2.4; A1 Ch. 7, PR, DPSIA; A3–A5; I4 M9; I12 M16; I6 M8; P2; L3 p. 18; L4 pp. 27–29; L12 §4.6 | A, I, P, L |
| Deployment ownership disputed | A3 Domain VI ("support"); A4 "not tested" subtasks; P2 DS Foundations; L7–L10; L12 §4.7–4.8; I2; I11 | A, I, P, L |
| Practice universal; functions differ; practice as organizing pedagogy | A2 (canned data insufficient; capstones); A1 §4.1; G1 p. 1; P1 §8; P2 §8; I1, I12, I14, I16, I17, I18, I19; L4 | A, I, G, P, L |
| Competing sequencing models | P1 §7; P2 §7; A1 tiers; A2 Ch. 2; A4 vs A5; I4; I7; I12; I15 prerequisites; I18; G1 pp. 2, 4; L4; L12 | A, I, G, P, L |
| Tools enabling, not defining; durable over specific | A2 ("follow the information technology frontier"); A1 Ch. 6–7; A4/A5 4.4; P1 §10.5; P2 §9–10; L12 p. 4, §5 | A, P, L |
| Programming and maths expectations contested | A1 Ch. 3, 6; A2 maths list; I4 ("no requiere codificación"); I1; I18 two tracks; P1 "no prerequisites"; P2 DS 1–3 yrs; G1 | A, I, G, P |
| Discipline vs short-cycle skill | A1 Ch. 2, 4; A2 Finding 3.1; L12 §5.1 vs G1 p. 2; P1 track durations | A, L vs G, P |
| GenAI/agentic AI emerging and uncertain | I18; I16; I1; I6; I12; P2 GenAI path; G1 (AI as separate theme); L1 pp. 57–60; L12 §6; absent A1–A5 | I, G, P, L |
| DataOps/methodology/organizational depth concentrated in L; L4 and L12 share one structure | L2–L12; L4 pp. 9–29 vs L12 §4; I5; I6; I16; A1 SDM T2 | L, I (A partial) |
| Evidence limits | Section 1.3 (A1/A2 dates; 8/19 MIT; G1 single sheet without competencies; P1/P2 stated limits; L2–L11 single series; L12 unvalidated and possibly internal) | — |
