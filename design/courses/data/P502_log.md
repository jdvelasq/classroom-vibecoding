# Log — P502

## S01.P502.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`
- **Estado:** inicial
- **Inspeccionado:** `professor/main.py`, `submission/`, pruebas y
  `traceability.yaml`.
- **Decisión:** se creó el mapa de catálogos y linaje; se registró que los
  productos presentes son generados por material de profesor.
- **Trazabilidad:** `data.C03`–`data.C05` revisadas.
- **Auditoría:** el producto sigue una pregunta de negocio y preserva
  Analytics como identidad.

## S02.P502.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P502_superstore_linaje/` (`data/superstore_orders.csv`, `professor/main.py`, `src/main.py`, `submission/data_catalog.csv`, `submission/column_catalog.csv`, `submission/lineage.csv`, `submission/questions.json`, `tests/test_activity.py`); contraste con `implementation/data/P501_superstore_serving/submission/serving_manifest.csv`.
- **Trazabilidad revisada:** P502 → `data.C03`, `data.C04`, `data.C05`; C03 parcial, C05 débil.
- **Preservado:** pregunta, tres artefactos de documentación, grano y consumidor por dataset, y la constatación previa de que no hay pipeline ejecutable.
- **Corregido:** la descripción previa decía que P502 «reutiliza artefactos Superstore»; el código no lee el CSV ni los archivos de P501: catálogo y linaje son literales escritos a mano.
- **Highlights añadidos:** H01 (catálogo de datasets), H02 (roles de columnas), H03 (cambio de grano en el linaje; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** `data/superstore_orders.csv` presente sin uso; ubicación `submission` remite a P501; consumidor «Privado» sin explicación (¿restricción de uso?); catálogo de columnas parcial; linaje no verificable contra el código.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P501 nombres y granos; no habilita una actividad posterior de forma demostrable.
- **Auditoría de Analytics:** documentación que sirve a la auditabilidad de métricas; riesgo de documentación formal desconectada de los datos.

## S03.P502.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DI-Methods (p. 91: «Understand how to use the integrity models in multiple data ownership domains to ensure provenance») — ya cubierta en lo pertinente: linaje con cambio de grano (H03); el resto es seguridad.

## S03.P502.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.4.3 «lineage, traceability, and version control of data» (p. 15) — ya cubierta por P502 H03 y P503 H01; versionado de datos como práctica es marginal.
  - CAP-E.3.2.2 roles de gobierno (owner, steward, custodian) (p. 14) — marginal: vocabulario organizacional sin caso; el consumidor «Privado» de P502 es un defecto de S02, no una señal de este documento.

## S03.P502.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - linaje y trazabilidad (p. 15 «CAP-P.3.4.3 Identify the purpose of lineage, traceability, and version control of data») — ya cubierta: P502 H03 (cambio de grano por paso de linaje), P503 H01 (consulta preservada).

## S03.P502.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P502.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Arquitecto de Datos que define «un data warehouse corporativo, algunos data marts» hasta «lagos de datos, arquitecturas híbridas …, gobernanza, linaje, seguridad» (p. 290); Líder de BD que participa en «arquitectura de datos y gobierno de información» (p. 286). Categoría: ya cubierta / fuera de alcance. Mart mínimo (P512 H02–H03) y linaje con cambio de grano (P502 H03) ya existen; lagos y gobierno corporativo son arquitectura empresarial, excluida.

## S03.P502.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.

## S03.P502.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión y predicción, clasificación y pruebas de hipótesis, aprendizaje profundo, sistemas de recomendación y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre el proceso de diseño de productos de IA (cuatro etapas, modelo de Lawler), fundamentos de ML y deep learning, HCI, «superminds» y *capstone* de propuesta de producto de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo sobre estrategia de plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura técnica, APIs y estándares, regulación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso de educación profesional del MIT: ecuaciones diferenciales y métodos numéricos, modelado espacial (EDP), optimización y modelado guiado por datos, de la optimización al ML (regresión, regularización, clasificación), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos industriales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa profesional de 6 meses orientado al empleo como data engineer: Python, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, streaming (Kafka, MQTT), seguridad web y ML/RL; evaluación por portafolio en GitHub. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de 6 meses con cinco partes (fundamentos de data science, optimización, ML, ML avanzado, despliegue), casos (retail, análisis facial, Filatoi Riuniti, BlueBike) y *capstone* de portafolio; herramientas Python y Google Colab. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh, estudios de trade-off, modelos de valor, generación de espacios de diseño, tradespace, frente de Pareto y sensibilidad. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo), mapeo de atributos de prototipo y producto, decisiones de fabricación y análisis de costo-valor. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos presenciales cortos (3–5 días): Data Science for Business Professionals/Beginners/Intermediate, Advanced and Predictive Analytics, masterclasses ejecutivas y *fast tracks*, centrados en visualización con PowerBI, R/Python, estadística, regresión, ML y series de tiempo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo combinado (en línea + 3,5 días en campus) sobre estrategia, liderazgo, innovación, futuros y gobernanza de IA generativa y agéntica para directivos con más de 10 años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses en español con cinco cursos de ocho semanas: Data Engineering, Ciencia de Datos con Python, Estadística, IA y ML, y Storytelling y visualización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «el uso de metadatos para la investigación a través de ejercicios de modelación aplicables en distintos aspectos de la realidad» (p. 79) — ya cubierta: mención incidental sobre recursos didácticos, sin contenido técnico; la documentación de datos con catálogo y linaje ya está en P502 H01–H03 (`data.C04`). No aporta nada sobre qué metadatos ni cómo.

## S03.P502.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - circular de la Dirección Académica de la Sede Manizales. Establece una «Ruta de Armonización Curricular» en cuatro etapas: marco normativo, pertinencia y resultados de aprendizaje, organización curricular, e implementación y evaluación continua. La orienta al Acuerdo 02 de 2020 del CESU (resultados de aprendizaje) y al Acuerdo 033 de 2007 del CSU, en las dimensiones macro, meso y microcurricular. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso de posgrado de minería de datos aplicada a datos de salud (EHR), con un proyecto por entregables (propuesta, reporte de recolección de datos, reporte de preparación, informe final) y un survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de pregrado sin prerrequisitos que combina modelado relacional, normalización, SQL, NoSQL/MongoDB, BI y visualización con Excel/Access/Tableau, más un proyecto final en equipo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa online de 12 semanas, con ruta con o sin código, sobre IA generativa, prompts, RAG, agentes con herramientas y memoria (LangChain, LangGraph, MCP), sistemas multiagente, su evaluación y protección. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - syllabus de posgrado en almacenes de datos: repaso de bases de datos y modelado ER, modelado dimensional Kimball (hechos, dimensiones, SCD, trampas), universos de SAP Business Objects, reportes Web Intelligence y Tableau; explícitamente sin ETL. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de módulo de posgrado (15 créditos, 10 semanas): de datos crudos a patrones para predicción y decisión; temario de herramientas, estadística, bases de datos y calidad, regresión, matrices, clustering, clasificación, estructuras para big data, privacidad y grafos; evaluación con proyecto (35 %), ejercicios y examen (50 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lámina única que enumera los métodos y herramientas del programa: recolección de datos (encuestas, NPS, autorreportes; recolección pasiva; medios), A/B testing, correlación y causalidad, pronóstico, regresión, simulación (Analysis ToolPak, Solver), visualización e interpretación, optimización y árboles de decisión. Es sólo una lista de títulos, sin contenido, nivel ni evidencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - listado de un módulo de orientación y nueve módulos de un programa ejecutivo de Business Analytics organizado por la secuencia descriptiva → predictiva → prescriptiva → aplicación, cada uno con una frase de resultado; no detalla contenidos, datos, herramientas ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Recorrido histórico de RDBMS/SQL (1970) a la IA agéntica (2026): data warehouse, ETL, BI, KDD, OLAP, CRISP-DM, data science, Hadoop/MapReduce, data lake, NoSQL, DataOps, MLOps y modelos fundacionales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación organizacional que enumera problemas de Data Analytics/Data Science (objetivos cambiantes, silos, formatos no optimizados, mala calidad y desconfianza en los datos, trabajo manual), mitos y brechas de conocimiento (DA ≠ desarrollo de software, data literacy, el modelo «omnisciente») y falta de soporte (objetivos poco claros, acceso a fuentes y permisos, paso a producción). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - diagnóstico de activos de datos: «Inventario y significado. Identificar fuentes, dominios, definiciones, metadatos y trazabilidad» (p. 8) — ya cubierta por P502 H01–H03 (catálogo, roles de columna, linaje).

## S03.P502.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - evolución KDD→CRISP-DM→ASUM/TDSP/CRISP-ML(Q)/INFORMS y un ciclo de proyecto analítico (problema de negocio, problema analítico, entendimiento y preparación de datos, diseño, evaluación, operación, mejora continua, gobernanza y ética transversal) ilustrado con un caso de abandono de clientes. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Presentación que traslada lean manufacturing, lean software y lean startup a la analítica: desperdicios, value stream mapping, entrega rápida, teoría de restricciones y análisis de causa raíz aplicados a la calidad de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - reproducibilidad como principio (p. 10 «Make it reproducible», «Analytics is code») — ya cubierta: `data.C04`; P503 H01 (consulta junto al export), P502 H03 (linaje), P500 H03 (contrato persistido).

## S03.P502.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - reproducibilidad determinista y control de versiones (p. 10 «El pipeline es determinístico con resultados reproducibles»; «El sistema de control de versiones permite manejar los cambios») — ya cubierta en lo que toca al curso: P503 H01 (consulta preservada), P502 H03 (linaje); el control de versiones del código es práctica transversal del repositorio, no contenido de `data`.

## S03.P502.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - herramientas de catálogo (Alation, Collibra, Wikis) y Data Governance como «Gestión del catalogo de datos y resultados de los modelos» (p. 2). Categoría: ya cubierta. P502 H01–H03 (inventario con grano, consumidor y linaje); nombrar productos comerciales no cambia lo que el estudiante hace.

## S03.P502.43

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - material de clase sobre DataOps: desarrollo tradicional frente a ML, deuda técnica, pruebas de datos y lógica, control de versiones, ambientes múltiples, contenedores, arquitectura canónica (raw lake → refined → data science), agile data warehousing, data lake y esquemas para análisis. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.44

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Láminas de clase sobre DataOps: pruebas automatizadas en cada etapa del pipeline (acceso, transformación, modelado, visualización), tipos de prueba de datos (entradas, lógica de negocio, salidas; *balance tests* de ubicación, históricos y control estadístico de procesos) y una tabla de severidad → acción. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.45

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - problemas «Artifactos no reproducibles», «El código y la data crecen independientemente» y «Falta de trazabilidad para el entrenamiento y monitoreo de modelos» (p. 2) — ya cubierta en lo que toca al curso: catálogo y linaje (P502 H01–H03), contrato persistido (P500 H03) y consulta preservada (P503 H01); trazabilidad de modelos es MLOps, excluido.

## S03.P502.46

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Revisión sistemática por expansión de citas de 18 metodologías (CRISP-DM, TDSP, ASUM-DM, DMME, MAISTRO…) que deriva PRODIG8: seis dimensiones de ejecución, gobierno y ética transversal y mejora continua. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.47

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - nivel de medición y rol por campo; campos 0/1 que deben tratarse como nominales («gender, are more accurately viewed as a nominal field», p. 72); identificador único sin uso analítico («cardid … Typeless», p. 321) — ya cubierta: H02 asigna roles analíticos a las columnas.

## S03.P502.48

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - informe de recolección y de descripción (p. 18 «write a data collection report»; p. 19 «How large is the database (in numbers of rows and columns)?») — ya cubierta: P502 H01 (inventario con grano, ubicación, consumidor) y P501 H02 (manifiesto de interfaces).

## S03.P502.49

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/knime-quickstart-guide.md` (`source_sha256`: 2f768a51f41938c9f7946a47c9d5230647e92cb0462378f49816c09f67613833).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - flujo de transformación como grafo de nodos con entradas y salidas explícitas (p. 3 «Nodes are the basic processing units of a workflow. Each node has a number of input- and/or output ports») — ya cubierta: P502 H03 (linaje por paso con cambio de grano) y P514 H01 (funciones de etapa); el documento sólo describe la interfaz de la herramienta.

## S03.P502.50

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/microsoft-sql-server-data-mining.md` (`source_sha256`: f4f47fd27416eaa5ac320918e941dbc61d0001ba6fa691e1ac56ea49db47e6b1).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - folleto comercial de antes del lanzamiento de SQL Server 2005 Analysis Services Data Mining. Enumera casos de uso (canasta de mercado, churn, segmentación, pronóstico, calidad de datos, texto), la integración con Integration, OLAP y Reporting Services, asistentes, el lenguaje DMX, los algoritmos y la arquitectura empresarial. Es una señal de herramienta de 2005, no curricular. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.51

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` (`source_sha256`: 992a830c9173ff435cacf89e961713aeb8488d80ae74c5bd3ca267e1e5460b88).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Manual de producto de Oracle: proceso de minería (definición del problema → preparación → modelo → despliegue), formato de *case table* (registro único vs. multirregistro/anidado), preparación automática y embebida (binning, normalización, outliers), tratamiento de faltantes vs. dispersión y preparación de texto. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.52

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/perceptual-edge-dashboard-design-requirements-questionnaire.md` (`source_sha256`: b2fda9a2366e49604d91b330424c4fdf5d9ee294068f4c8b998f1a188fb30a6c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Cuestionario de ocho preguntas para levantar requisitos antes de diseñar un dashboard: frecuencia de actualización, usuarios, preguntas y acciones, ítems de datos y su nivel de detalle, ítems clave, agrupaciones, comparaciones de contexto y umbrales de excepción. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P502.53

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` (`source_sha256`: 5d936194154a3c8774fd7df35e28c7a427fb9d4348130b86ae9c6ec58946548f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Object Naming Conventions» (p. 35); «Certified Reports on Certified Datasets», «Data steward owns source data & validates dataset trustworthiness» (p. 20, p. 91) — marginal/fuera de alcance: P502 ya documenta catálogo y linaje; certificación y administración de espacios de trabajo son gobierno organizacional y BI.
