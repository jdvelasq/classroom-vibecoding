# Log — P516

## S01.P516.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró el alcance de `zipcode=0` como límite crítico.

## S02.P516.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P516_vermont_calidad/` (`data/vermont.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/quality_report.csv`, `tests/test_activity.py`); P500, P510, P511 para relaciones; P517 para dependencia.
- **Trazabilidad revisada:** P516 → `data.C01`, `data.C03`, `data.C04`; coherente.
- **Highlights:** añadidos H01 (granos mezclados por total estatal; caso y datos), H02 (calidad como reglas con dimensión y conteo), H03 (clave compuesta y dominio como unidad de análisis).
- **Preservado:** pregunta, cinco reglas, clave (`zipcode`, `agi_stub`), `zipcode = 0` como riesgo de alcance.
- **Corregido:** la descripción previa hablaba de «perfilado»; el notebook evalúa reglas sobre 5 de 147 columnas, no perfila el extracto.
- **Añadido:** 1476 × 147; ausencia de procedencia, año y diccionario; defecto de estado (sólo la regla de alcance puede no ser `PASS`); diagnóstico sin conjunto filtrado; prueba de sólo existencia.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** la interpretación de `zipcode = 0` se apoya sólo en un comentario.
- **Superficies / contrato / dependencias:** S01–S05; habilita datos y reglas para P517.
- **Auditoría de Analytics:** diagnóstico de aptitud para una pregunta; sin riesgo de identidad relevante.

## S03.P516.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Cleaning (pp. 73–74: «The dimensions of data quality»; «Various forms for data quality rules such as functional dependencies (FD)…»; «suitable for its intended use») — ya cubierta: reglas nombradas por dimensión (H02), clave compuesta y dominio (H03), aptitud para la pregunta (H01). La falta de diccionario y procedencia (S01) es marginal desde este documento (CCF p. 66: «Files: data, metadata» es genérico).

## S03.P516.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T02.
- **Señales descartadas relevantes:**
  - Task 3.6 «Assess data quality and identify relationships in the data» (p. 5) — ya cubierta por P516 H02–H03.

## S03.P516.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - CAP-E.3.6.1 «accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» y 3.6.4 métodos de evaluación (p. 15) — ya cubierta por P516 H02; atípicos se integran en la candidata de perfil.
  - CAP-E.3.7.1 y 3.8.1 (p. 16) — ya cubierta por P516 H01 (alcance que cambia la pregunta) y P517 H01; la parte no cubierta va a las candidatas.

## S03.P516.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - limitaciones a partir de atributos, contexto y metadatos (p. 14 «CAP-P.3.2.1 Identify data limitations and constraints based on data attributes, data context, and metadata, and propose appropriate course of actions») — ya cubierta en lo esencial por H01–H03; la verificación de metadatos se propone desde CRISP-DM.
  - perfilado multivariado (p. 15 «CAP-P.3.6.2 Identify patterns and characteristics of a multivariate dataset from data profiling outputs») — marginal: perfilar las 147 columnas contradice el contrato mínimo derivado de la pregunta (P517 H02); el perfilado exploratorio es de Descriptiva.

## S03.P516.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - esquema de eventos de error y dimensión de auditoría (pp. 23–24) — ya cubierta por P516 H02 (reglas con dimensión y conteo) y P514 H02 (reporte por etapa); como esquema dimensional del *back room* es fuera de alcance.

## S03.P516.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «use simple graphics to check data for artifacts, snafus, and inconsistencies» y «Data consistency checking» (pp. 45–46) — marginal: `AGENTS.md` ya exige celdas de evidencia visual y las reglas nombradas de P516 (H02) son el mecanismo de consistencia. Extender a las 147 columnas sin diccionario no tiene caso riguroso.

## S03.P516.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad: aplicación de reglas de limpieza (tiempos mínimos, duplicados), control de completitud, consistencia de escalas» (p. 238); «Trazabilidad y gobernanza: separación clara entre evidencia empírica … y supuestos de negocio» (p. 41). Categoría: ya cubierta. Controles de calidad ejecutables (P500 H04), reglas nombradas con dimensión y conteo (P516 H02), contrato y decisiones persistidas (P517 H02–H04).

## S03.P516.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.

## S03.P516.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «¿Qué opinas de los datos que encontraste?» y «Limpieza de datos» (p. 7); «Sé capaz de recopilar, limpiar y describir los datos que tienes» (p. 6) — ya cubierta en P516 (aptitud de una fuente para una pregunta); como mucho refuerza la candidata de procedencia de P516 derivada de UNF, sin aportar práctica concreta propia.

## S03.P516.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión y predicción, clasificación y pruebas de hipótesis, aprendizaje profundo, sistemas de recomendación y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre el proceso de diseño de productos de IA (cuatro etapas, modelo de Lawler), fundamentos de ML y deep learning, HCI, «superminds» y *capstone* de propuesta de producto de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo sobre estrategia de plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura técnica, APIs y estándares, regulación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso de educación profesional del MIT: ecuaciones diferenciales y métodos numéricos, modelado espacial (EDP), optimización y modelado guiado por datos, de la optimización al ML (regresión, regularización, clasificación), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos industriales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa profesional de 6 meses orientado al empleo como data engineer: Python, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, streaming (Kafka, MQTT), seguridad web y ML/RL; evaluación por portafolio en GitHub. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de 6 meses con cinco partes (fundamentos de data science, optimización, ML, ML avanzado, despliegue), casos (retail, análisis facial, Filatoi Riuniti, BlueBike) y *capstone* de portafolio; herramientas Python y Google Colab. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh, estudios de trade-off, modelos de valor, generación de espacios de diseño, tradespace, frente de Pareto y sensibilidad. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo), mapeo de atributos de prototipo y producto, decisiones de fabricación y análisis de costo-valor. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Evaluate constraints on the use of data. Assess data structure and data lifecycle» (p. 7) — ya cubierta en lo pertinente por P516–P517; ciclo de vida organizacional fuera de alcance.

## S03.P516.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo combinado (en línea + 3,5 días en campus) sobre estrategia, liderazgo, innovación, futuros y gobernanza de IA generativa y agéntica para directivos con más de 10 años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Extraer los datos de fuentes fiables» (p. 5) — ya cubierta en espíritu por P516; la parte no cubierta (procedencia) está en la candidata P516 de CAP-E.

## S03.P516.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - informe de la Dirección Nacional de Programas Curriculares de Pregrado de la UNAL sobre cuatro talleres participativos con 17 programas de pregrado (p. 8) acerca de qué es el currículo, pertinencia frente al contexto, integración de docencia/investigación/extensión, prácticas pedagógicas (fines, contenidos, estrategias, recursos, evaluación) y propuestas para superar el «currículo endogámico». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - circular de la Dirección Académica de la Sede Manizales. Establece una «Ruta de Armonización Curricular» en cuatro etapas: marco normativo, pertinencia y resultados de aprendizaje, organización curricular, e implementación y evaluación continua. La orienta al Acuerdo 02 de 2020 del CESU (resultados de aprendizaje) y al Acuerdo 033 de 2007 del CSU, en las dimensiones macro, meso y microcurricular. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P516.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de pregrado sin prerrequisitos que combina modelado relacional, normalización, SQL, NoSQL/MongoDB, BI y visualización con Excel/Access/Tableau, más un proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa online de 12 semanas, con ruta con o sin código, sobre IA generativa, prompts, RAG, agentes con herramientas y memoria (LangChain, LangGraph, MCP), sistemas multiagente, su evaluación y protección. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - syllabus de posgrado en almacenes de datos: repaso de bases de datos y modelado ER, modelado dimensional Kimball (hechos, dimensiones, SCD, trampas), universos de SAP Business Objects, reportes Web Intelligence y Tableau; explícitamente sin ETL. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad y limpieza de datos (p. 2: «Problems found in realistic data: errors, missing values, lack of consistency, and techniques for addressing them»; p. 2: «coping with missing and dirty data») — ya cubierta: P500 H04 (controles ejecutables), P510 H03 y P511 H02 (conciliación y cardinalidad), P516 H01–H03 (reglas con dimensión).

## S03.P516.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lámina única que enumera los métodos y herramientas del programa: recolección de datos (encuestas, NPS, autorreportes; recolección pasiva; medios), A/B testing, correlación y causalidad, pronóstico, regresión, simulación (Analysis ToolPak, Solver), visualización e interpretación, optimización y árboles de decisión. Es sólo una lista de títulos, sin contenido, nivel ni evidencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Module 1 (p. 1: «Identify effective methods for collecting data on customer behavior and use it to make better decisions for your business») — ya cubierta / marginal: es la única señal de adquisición de datos del documento y se queda en una frase. Obtener datos de comportamiento y definir una métrica a un grano explícito ya lo hace P526 (H01 tiempo de evento frente a llegada, H03 conversión por sesión), y derivar qué datos sirven a una pregunta lo hacen P516 (aptitud de un extracto para una pregunta) y P517 (contrato mínimo derivado de la pregunta), en `data.C01`. Sin métodos concretos (instrumentos, muestreo, diseño de recolección), la señal no cambia lo que hace el estudiante en ningún taller; el criterio de selección de la muestra de P526, no documentado, ya está registrado en su S02.

## S03.P516.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Recorrido histórico de RDBMS/SQL (1970) a la IA agéntica (2026): data warehouse, ETL, BI, KDD, OLAP, CRISP-DM, data science, Hadoop/MapReduce, data lake, NoSQL, DataOps, MLOps y modelos fundacionales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «La poca calidad de los datos sigue siendo un desafío serio», «Existencia de errores en los datos», «Malos datos arruinan buenos reportes», «Falta de confianza en los datos» (p. 2). Categoría: ya cubierta. Controles ejecutables que condicionan la salida (P500 H04), diagnóstico de aptitud con reglas nombradas (P516 H01–H03) y contrato que clasifica cambios por su efecto en el análisis (P517 H02–H04). Es diagnóstico organizacional, sin práctica nueva.
  - en ML/DA «La lógica y los datos son críticos», «El testeo se basa en precisión no en ejemplos», «Se usan datos de producción» (p. 4). Categoría: fuera de alcance / ya cubierta. El contraste con la programación tradicional apunta a pruebas de modelos y a producción (otros cursos/productos de datos); las pruebas sobre datos ya existen como aserciones de calidad (P500 H04, P516 H02).

## S03.P516.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad y disponibilidad. Evaluar la adecuación al uso» (p. 8); brecha de datos «identificadores incompatibles y registros incompletos» (p. 11) — ya cubierta por P516 (aptitud para una pregunta) y P511 H01 (claves que no identifican).

## S03.P516.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - dimensiones de calidad «exactitud, completitud, consistencia, actualidad, validez, relevancia y unicidad» (p. 13) — ya cubierta parcialmente por P516 H02 (completitud, validez, unicidad, alcance); añadir dimensiones por catálogo sería marginal.

## S03.P516.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - causa raíz «no hay suficientes pruebas que garanticen que los datos defectuosos no entren en las pipelines o las bases de datos» y «Porque no entienden cómo usan los datos los consumidores» (p. 10) — ya cubierta: controles ejecutables que condicionan la salida (P500 H04), reglas de calidad como reporte (P516 H02) y contrato derivado del uso analítico (P517 H02). Aporta contexto, no una práctica nueva.

## S03.P516.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad como prioridad y monitoreo (p. 10 «Quality is paramount», «Monitor quality and performance») — ya cubierta: P516 H02, P517 H03–H04; el monitoreo continuo es de productos de datos.

## S03.P516.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación que define DataOps como combinación de Agile, Lean y DevOps para la calidad del dato; siete pasos de implementación (pruebas en cada etapa, control de versiones, ramas, ambientes, contenedores, parametrización, «trabajar sin miedo»), diferencias con DevOps, MLOps y ciclo de vida de ciencia de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Tests de datos» en el desarrollo (p. 5); «Robustez: por el uso de tests» (p. 2); «Monitoreo de la lógica de negocio y validez de los datos» (p. 10). Categoría: ya cubierta. Controles de calidad ejecutables que bloquean la salida (P500 H04), reglas nombradas con dimensión y conteo (P516 H02) y contratos ejercitados con lotes perturbados (P517 H04). La debilidad transversal «Pruebas: sólo existencia» ya está registrada por S02 en cada Pxxx; esta presentación organizacional no aporta un argumento nuevo para corregirla.

## S03.P516.43

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - material de clase sobre DataOps: desarrollo tradicional frente a ML, deuda técnica, pruebas de datos y lógica, control de versiones, ambientes múltiples, contenedores, arquitectura canónica (raw lake → refined → data science), agile data warehousing, data lake y esquemas para análisis. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.44

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P516.45

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Diapositivas sobre estructuras de equipos para DataOps (pequeños, Big Data, híbridos, a gran escala; por función, por dominio, centralizados/descentralizados), roles y habilidades (perfiles T, Pi, M, E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.46

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - dimensiones de calidad «completeness, accuracy, timeliness, consistency, and representativeness» (p. 15) — ya cubierta: P516 H02 expresa reglas por dimensión (completeness, validity, uniqueness, scope). Añadir dimensiones sin caso que las exija sería marginal; la representatividad del corpus Scopus (P503–P507) es límite ya registrado por S02.

## S03.P516.47

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - filtrar campos con porcentaje de calidad bajo un umbral (p. 79: «filter any fields with a quality percentage below a specified threshold») — marginal y contraria al diseño: P516/P517 derivan las reglas de la pregunta (P517 H02, contrato de seis de 147 columnas) en vez de juzgar todas las columnas por completitud.
  - códigos centinela documentados en el diccionario («Credit_rating … 9=missing values», p. 27) — marginal: el guía sólo los lista para datos de demostración; la falta de diccionario de Vermont ya está registrada en S01 y la señal no aporta caso ni método.

## S03.P516.48

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** refuerza T02.
- **Señales descartadas relevantes:**
  - chequeo de plausibilidad (p. 21 «Have you conducted a plausibility check for values?») y tipología de problemas (p. 20) — ya cubierta: H02 (reglas nombradas con dimensión) y H03 (dominio).

## S03.P516.49

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - guía de inicio de una versión antigua (2.x) de KNIME: construir un flujo de nodos (File Reader → K-Means → Color Manager → tabla y dispersión), estados de nodo, puertos, preferencias, exportación de flujos y meta nodos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.50

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data Quality. Determine missing values and anomalies in your data as it is entered or loaded into your data warehouse» (p. 1) — ya cubierta: reglas nombradas de calidad (P516 H02) y contrato de aceptación de lotes (P517 H02–H04). Que la señal venga de un producto no basta para imponer una técnica.
  - Integration Services para «flag outliers, separate data, and fill in missing values based on the predictive analytics of the data mining algorithms» (p. 1) — fuera de alcance: imputación predictiva dentro de un pipeline productivo (frontera con Predictiva y con productos de datos). El tratamiento de faltantes del curso se aborda desde la documentación y la decisión (ver la candidata P510 de NASEM).

## S03.P516.51

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data Gathering and Preparation» — evaluar qué tan bien los datos atienden el problema e identificar problemas de calidad (p. 19: «you can determine how well it addresses the business problem [...] identify data quality problems») — ya cubierta: P516 es exactamente un diagnóstico de aptitud para una pregunta (H01–H03).
  - outliers válidos vs. errores que exigen conocimiento del dominio (p. 130: «in some cases, especially in the business arena, outliers may be perfectly valid [...] Domain knowledge is usually needed to determine outlier handling») — marginal: sería una regla más en el reporte de calidad de P516 (H02) sin cambiar la capacidad; el documento lo plantea como preparación para modelos.

## S03.P516.52

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/perceptual-edge-dashboard-design-requirements-questionnaire.md` (`source_sha256`: b2fda9a2366e49604d91b330424c4fdf5d9ee294068f4c8b998f1a188fb30a6c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cuestionario de ocho preguntas para levantar requisitos antes de diseñar un dashboard: frecuencia de actualización, usuarios, preguntas y acciones, ítems de datos y su nivel de detalle, ítems clave, agrupaciones, comparaciones de contexto y umbrales de excepción. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.53

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` (`source_sha256`: 5d936194154a3c8774fd7df35e28c7a427fb9d4348130b86ae9c6ec58946548f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Taller práctico de BI empresarial: requisitos de negocio → preparación en Power Query → modelo dimensional → medidas DAX → visualización → despliegue y gobierno (pipelines, datasets certificados). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P516.54

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-data-mining.md` (`source_sha256`: 6396a7c9e3efce998f0bbb9907cacb228244737c80bdebcdae17ce913b7f6ce9).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - exploración para detectar errores, faltantes y distribuciones a transformar (p. 7 «identificar los problemas de calidad de los datos como los errores, valores faltantes o distribuciones de datos que necesitan transformarse») — ya cubierta en lo esencial (P516 H02); la parte de transformación para modelar es de Predictiva.

## S03.P516.55

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/sas-forecasting.md` (`source_sha256`: 7cabe87e23ff9469d7b4b9e17582dd694b8ac329ed0975bf9a26e3dcb26b5569).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - exploración de muchas series para detectar atípicos, faltantes, series cortas e intermitentes (p. 88) — marginal/fuera de alcance: P516 ya expresa calidad como reglas nombradas; intermitencia y series cortas importan para elegir métodos de pronóstico (predictiva).
