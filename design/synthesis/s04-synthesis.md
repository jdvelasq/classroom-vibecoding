# Consolidated Benchmark Synthesis

## 1. Scope and integration method

This consolidation integrates the independent S03 syntheses produced by
ChatGPT/Codex, Claude, and Gemini:

- `synthesis-chatgpt.md`
- `synthesis-claude.md`
- `synthesis-gemini.md`

It compares their conclusions rather than treating them as votes or ranking
them by model. A finding is treated as strongest when the syntheses agree and
their reasoning remains traceable to diverse underlying evidence families:
authoritative, institutional, professional-learning, and literature-derived.
Repeated reference to the same source family is not treated as independent
confirmation.

After the S03 consolidation, the approved master's thesis *Strategies for
Executing Analytics Projects: Toward a Unified Framework of Methodologies*
(PRODIG8) was added to the literature-derived benchmark family. It is used
here as an additional, clearly identified academic synthesis of
analytics-project methodologies; it does not alter or resolve disagreements
among the three agent syntheses. One inventory discrepancy remains visible:
ChatGPT and Claude
describe 37 corpus items (5 authoritative, 19 institutional, 11
literature-derived, and 2 professional), while Gemini describes 36. The
consolidation does not resolve that discrepancy without reopening the corpus.

## 2. Convergent account of Analytics

The strongest shared account is that **Analytics is decision- and
action-connected work with data**. It begins with a consequential question,
stakeholders, assumptions, and success criteria; it includes obtaining and
assessing suitable data, applying and evaluating appropriate methods,
interpreting results, communicating them, and enabling responsible use. Where
an analytical solution is operationalized, the view extends to monitoring,
adaptation, and review of consequences.

This account is broader than reporting, dashboard construction, model fitting,
or data-pipeline construction. The three syntheses agree that those activities
may be important contributions, but none defines the whole educational domain.
They also agree that the boundary between Analytics and Data Science is not
uniformly drawn across the corpus: some sources foreground decision support and
BI, while others include predictive modelling, optimization, or data-science
practice. That variation must be preserved rather than collapsed into a single
label.

## 3. Analytics and contributing disciplines

The syntheses converge on a functional, rather than ownership-based,
relationship with contributing disciplines:

| Contributing discipline | Function within Analytics | Consolidated boundary |
|---|---|---|
| Statistics | Description, uncertainty, inference, experimentation, and valid interpretation. | Foundational reasoning, but not a complete Analytics architecture. |
| Data Science | Programming, statistical modelling, predictive methods, and sometimes model lifecycle. | Overlaps strongly; professional sources often distinguish it by greater modelling/programming/deployment depth. |
| Machine Learning | Predictive, unsupervised, and advanced modelling methods. | Important repertoire, not the organizing curriculum. |
| Operations Research and Optimization | Prescriptive analysis, simulation, value modelling, and constrained decisions. | Closely related to decision orientation, but unevenly represented and not universally core. |
| Data Engineering and Databases | Reliable data access, structure, quality, integration, scale, and reusable infrastructure. | Enables analytical work; production-scale ownership is role-dependent. |
| Business Intelligence | Querying, metrics, visualization, dashboards, reporting, and communication. | A substantial applied layer, but insufficient by itself to define Analytics. |
| Artificial Intelligence | Advanced methods, generative/agentic capabilities, products, governance, and risk. | Emerging and specialized in the available evidence. |

This preserves the governing identity: Analytics organizes the relationship
among problem, data, methods, interpretation, and action. No contributing
discipline should supply an independent syllabus that displaces that
integration.

## 4. Recurring capabilities and knowledge architecture

The following capabilities have cross-synthesis and cross-family support:

1. **Frame analytical problems and decisions.** Clarify context, stakeholders,
   scope, constraints, assumptions, value, and success measures.
2. **Obtain, prepare, assess, and steward data.** Include data access, SQL or
   equivalent querying, integration, documentation, quality, and fitness for
   purpose.
3. **Explore and reason from evidence.** Use description, visualization,
   statistical reasoning, inference, experimentation, and interpretation of
   uncertainty.
4. **Select, apply, and evaluate methods.** Match techniques to the question
   and data; assess validity, limitations, and consequences rather than merely
   run a method.
5. **Communicate and support use.** Explain assumptions and results to
   stakeholders through appropriate visual, written, and decision-oriented
   outputs.
6. **Act responsibly.** Address privacy, security, integrity, fairness, bias,
   governance, and possible adverse effects.
7. **Work reproducibly and, where appropriate, across a lifecycle.** Document,
   test, validate, and maintain work at a depth appropriate to the role.

The consolidated knowledge architecture has five related layers: foundations
(domain, data, statistical/mathematical, computational, and ethical
reasoning); data and computing enablers; analytical methods; decision and
human context; and specialized or operational extensions. The three syntheses
agree that this is an architecture of relationships, not a list of topics to
be covered at identical depth. PRODIG8 reinforces this relational reading for
analytics-project execution: project scope, data understanding and preparation,
project design, model evaluation, and operation and maintenance form an
execution lifecycle, while governance and ethics are transversal and continuous
improvement supplies feedback. It is an analytic framework for organizing
project work, not a prescribed course sequence.

## 5. Learning progression and authentic practice

The evidence supports a recurring movement from understanding a question and
data, through analysis and interpretation, to communication and decision or
action. Professional paths make variants of this progression explicit: analyst
routes commonly move from tools and data work to EDA/statistics and applied
outputs; data-science routes add more modelling and, sometimes, deployment.
INFORMS and literature-derived process material make feedback, implementation,
and lifecycle review more visible.

This is not evidence for one universal sequence. The syntheses identify
competing, defensible patterns: foundations-first, whole-lifecycle exposure
early, problem-first learning, and iterative/spiral models. The later design
stage must choose deliberately among them.

The added thesis lends specific support to treating governance, ethics, and
feedback as features that cut across project work rather than as a terminal
stage. Its framework is suitable as a lens for examining the coherence of
project-based learning, but it does not determine learning progression or the
scope required of every learner.

Authentic work is a strong convergence: real or messy data, cases, projects,
labs, communication, and integrated outputs recur across the four evidence
families. Practice serves different purposes—reinforcement, integration,
assessment, and professional simulation—so the evidence supports its presence
but not a single activity or assessment format.

## 6. Tools, technologies, and implementation context

The syntheses agree that durable capability should take priority over a fixed
technology stack. SQL or relational data access, Python, R, spreadsheets,
visualization and BI tools, databases, and common data/ML libraries recur, but
their required depth and substitutions vary by learner and role.

Distributed platforms, cloud services, MLOps/DataOps tooling, specialized BI
products, deep-learning ecosystems, and vendor certifications are enabling or
specialized context rather than common foundations. Generative and agentic AI
are salient in recent institutional, professional, and literature-derived
material, but lack support in the older authoritative material; they remain an
emerging area rather than a settled curricular requirement.

## 7. Convergences, differences, and unique contributions

### Strong, source-supported convergence

- Analytics connects data work to decision, action, and stakeholder context.
- Data acquisition, preparation, quality, and querying are foundational.
- Exploration, visualization, statistical reasoning, and interpretation are
  essential to trustworthy work.
- Communication with non-technical stakeholders is a substantive capability.
- Responsible practice—privacy, fairness, governance, integrity, and
  consequences—cannot be an optional afterthought.
- Integrated work with realistic problems and data is educationally important.
- Tools enable the work but do not determine curricular identity.

### Source-dependent convergence

The end-to-end lifecycle, including deployment, monitoring, and ongoing value
review, has strong support in INFORMS and concentrated detail in DataOps and
technical pathways. The three syntheses agree on its importance, but differ in
how broadly it should apply to every learner. Likewise, predictive modelling
is important across the corpus, while its placement within a shared Analytics
foundation versus a Data Science specialization remains unresolved.

### Useful single-synthesis contributions

Claude supplies the most explicit inventory of disagreements and makes the
role-level distinction between analyst, builder, and commissioner especially
clear. ChatGPT supplies a compact five-layer knowledge architecture and a
clear distinction between durable capability and tool choice. Gemini gives a
particularly detailed source-to-finding map. These differences are
complementary; none is a reason to privilege a model rather than the evidence
it traces.

### Material disagreements

- Whether prescriptive analytics, optimization, and simulation are core or
  specialized.
- Whether predictive modelling belongs to common Analytics foundations or the
  Data Science boundary.
- The appropriate ownership and depth of deployment and lifecycle management.
- Required programming and mathematical depth, including code/no-code routes.
- Whether ethics is embedded throughout learning or treated as a dedicated
  component.
- The status of causal inference, BI, GenAI/agentic AI, and specialized
  methods.

## 8. Uncertainties and evidence limitations

The underlying evidence is uneven. Authoritative sources represent relatively
few independent bodies and differ in audience and date. Institutional material
is often brochure-level, concentrated in a small set of providers, and mixes
undergraduate, executive, and technical audiences. The literature-derived
material is heavily concentrated in a DataOps perspective. Professional
benchmarks make role structures and tools visible but do not establish a
complete educational rationale or universal proficiency threshold.

The PRODIG8 thesis is an approved master's thesis and a systematic synthesis of
18 methodological documents, but its proposed framework remains conceptual.
Its corpus was retrieved from Scopus, is limited to English-language material,
and does not empirically validate the framework against completed analytics
projects. It therefore strengthens the literature-derived account of
project-execution architecture without serving as independent empirical
validation or an authoritative standard.

Consequently, the consolidation cannot settle a target learner, a universal
mathematical or programming threshold, a required tool stack, a standard
assessment model, or a universal sequencing model. It also cannot treat the
apparent absence of a topic from a source as proof of irrelevance.

## 9. Constraints for the next design stage

Subsequent design must preserve Analytics as an integrated, decision-oriented
educational domain. It cannot become an abbreviated Machine Learning,
Statistics, Data Engineering, Business Intelligence, or Operations Research
curriculum.

It must account for problem framing, data quality and stewardship, reasoning
with evidence, method selection and evaluation, interpretation and
communication, responsible practice, and authentic integrated work. It must
also make explicit decisions about target learner, programming and mathematics
depth, code/no-code expectations, the scope of predictive and prescriptive
methods, lifecycle/deployment depth, ethics integration, and tool portability.

The evidence constrains these decisions but does not make them. It does not
justify a final course sequence, technology stack, assessment structure, or
module plan at this stage.

## 10. Traceability map

| Consolidated finding | Agent-specific syntheses | Principal underlying evidence families cited there |
|---|---|---|
| Analytics connects data, decisions, and action | ChatGPT §§2, 11; Claude §§2, 11; Gemini §§2, 11 | Authoritative, institutional, professional, literature-derived |
| Data stewardship and quality are foundational | ChatGPT §§4, 11; Claude §§4, 11, 13; Gemini §§4, 5, 11 | All four families |
| Statistical reasoning, visualization, and interpretation recur | ChatGPT §§4–5, 11; Claude §§4–5, 11; Gemini §§4–5, 11 | Authoritative, institutional, professional; literature-derived support varies |
| Communication and stakeholder use are core | ChatGPT §§4, 11; Claude §§4, 11, 13; Gemini §§4, 11 | All four families |
| Authentic integrated work matters | ChatGPT §7; Claude §§7, 11, 14; Gemini §§7, 11 | All four families |
| Tools are enabling rather than curricular identity | ChatGPT §8; Claude §§8, 11, 14; Gemini §§8, 11 | Authoritative and professional, reinforced institutionally |
| Predictive and prescriptive scope remains contested | ChatGPT §§12–14; Claude §§12–14; Gemini §§12–14 | Varies by authoritative, institutional, and professional sources |
| Lifecycle, deployment, and operations are role-dependent | ChatGPT §§6, 10, 12; Claude §§12–14; Gemini §§6, 12, 14 | INFORMS, technical institutional, professional, and DataOps material |
| Project execution links execution, governance/ethics, and improvement functions | Added PRODIG8 thesis (literature-derived) | Systematic synthesis of 18 analytics-project methodologies; conceptual framework, not empirical validation |
