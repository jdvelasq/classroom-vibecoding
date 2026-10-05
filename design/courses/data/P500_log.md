# Log — P500

## S01.P500.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`
- **Estado:** inicial
- **Inspeccionado:** `professor/main.py`, `data/superstore_orders.csv`,
  `submission/`, `tests/test_activity.py`, `traceability.yaml`.
- **Decisión:** se creó el mapa de la actividad implementada y se registró la
  falta de un manifiesto local de procedencia.
- **Trazabilidad:** se revisaron `data.C01` a `data.C05`.
- **Auditoría:** producto analítico de métricas comerciales preserva identidad
  de Analytics.

## S02.P500.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P500_superstore_metricas/` (`data/superstore_orders.csv`, `professor/main.py`, `src/main.py`, `submission/metric_contract.json`, `submission/monthly_sales_metrics.csv`, `submission/questions.json`, `tests/test_activity.py`); contraste con `implementation/data/P501_superstore_serving/submission/sales_detail.csv` y la lectura de `implementation/data/P513_superstore_batch/`.
- **Trazabilidad revisada:** P500 → `data.C01`–`data.C05`; las cinco tienen evidencia.
- **Preservado:** pregunta, grano línea-de-orden, contrato de métrica, frontera de herramienta y auditoría de producto descriptivo.
- **Corregido:** la descripción previa afirmaba que el código «verifica» los faltantes de `Product Base Margin` y hacía una «reconciliación previa a la salida»: los faltantes son texto fijo del contrato y no hay reconciliación, sólo aserciones. Se precisó que `submission/` contiene tres artefactos y que las pruebas sólo comprueban existencia.
- **Highlights añadidos:** H01 (convención regional de lectura), H02 (fórmulas derivadas del grano; highlight obligatorio de caso y datos), H03 (métricas independientes de herramienta), H04 (compuerta de calidad). IDs nuevos; no existían highlights previos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** `encoding="latin1"` sobre un archivo con BOM UTF-8 (indicado por el prefijo `ï»¿` eliminado): el contrato persiste una codificación incorrecta y los textos no ASCII se decodifican mal (visible en P501); P513 usa `utf-8-sig`. La no unicidad de `Row ID` se afirma sin comprobarse. Sin procedencia del CSV. `src/main.py` sin instrucciones.
- **Superficies / contrato / dependencias:** S01–S07 declaradas; contrato separado entre código, `submission/`, prueba de existencia y trazabilidad; habilita a P501 (misma lectura y agregación) y el patrón `questions.json`.
- **Auditoría de Analytics:** producto descriptivo mensual con métricas auditables; pandas es habilitador. Riesgo de identidad bajo.

## S03.P500.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
- **Señales de alcance de curso** (registradas sólo en este log):
  - DG-Data Acquisition (p. 70: «minimize the deviation between the collected data and the real objects»; disposición de equilibrio exactitud/eficiencia) — marginal: el curso ya deriva requisitos desde preguntas (P500 H02, P517 H02); no aporta una capacidad nueva.
  - PR-Economic Considerations (p. 107: «Argue the case for what data an organization should routinely gather; design a related data collection process») — marginal: variante de `data.C01` ya ejercida (P500, P516, P517); el costo/valor de datos no tiene caso en el curso.
  - DG-Data Privacy and Security (p. 74: GDPR, Privacy Shield, HIPAA, GLBA, leyes estatales de EE. UU.) y PR-Legal Considerations e Intellectual Property (pp. 109–110) — fuera de alcance: detalle jurídico de otras jurisdicciones; a lo sumo una mención del marco local en la documentación de la candidata P526.
  - DPSIA/DP-Cryptography, Communication Protocols, Data Security (pp. 84–89) y Analysis for Security (pp. 92–94) — fuera de alcance: seguridad informática y ML para seguridad, no habilitación de datos para un propósito analítico.
  - CCF-Storage, Operating System, Networks, Compilers (pp. 64–68) — fuera de alcance: fundamentos de sistemas sin efecto sobre las capacidades `data.C01`–`C05`.
  - PDA-Programming (p. 114: «Manipulate data from selected sources (e.g., databases, spreadsheets, text documents, XML) utilizing appropriate techniques (e.g., database queries, API calls, regular expressions)») y cap. 6 (p. 38: «basic education in computing (programming, databases, use of the Internet)») — ya cubierta: CSV (P500), volcado SQL (P510), base relacional (P503), API/JSON (P518), Parquet (P524).
  - SDM (p. 121: «Execute a basic Data (Science) Lifecycle on a simple data product»; SDM-Software Testing) — marginal: las pruebas de participación son una decisión explícita de `AGENTS.md`, no un defecto que el benchmark corrija.
  - DM-Data Preparation, ingeniería de variables (p. 76: «feature extraction and representation; feature selection and feature generation») y DM-Information Extraction (p. 77, E) — fuera de alcance: pertenecen a los cursos predictivos o a procesamiento de texto avanzado.

## S03.P500.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.1 «Identify and prioritize data needs» (p. 5) — ya cubierta (P500 H02, P517 H02).
- **Señales de alcance de curso** (registradas sólo en este log):
  - Task 3.3 «Create a data management plan» (p. 5) — marginal: los manifiestos y contratos (P500 H03, P501 H02, P511 manifiesto, P517) ya cubren lo pertinente; un plan formal sería gestión de proyecto.
  - dominios I–II y IV–VII (pp. 4–7) — fuera de alcance (P001 y cursos de línea).

## S03.P500.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.1.1 «Identify data needs, sources, and acquisition sequence» (p. 13) — ya cubierta por P500 H02 y P517 H02.
  - CAP-E.4.4.1 características del *stack* (bases, nube, *open source*) (p. 18) — ya cubierta por la frontera de herramientas (P500 H03, P508 H01); profundizar sería identidad de herramienta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - CAP-E.3.6.3 visualizaciones comunes (p. 15) y dominios I–II, IV–VII (pp. 7–12, 17–25) — fuera de alcance: encuadre, métodos, modelos, despliegue y ciclo de vida pertenecen a P001 y a los cursos de línea.

## S03.P500.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - derivar necesidades de datos de la pregunta (p. 13 «CAP-P.3.1.1 Identify an appropriate sequencing and prioritization of data needed, including sources»; p. 10 «CAP-P.2.2.1 Identify why analytics element(s) would be classified as an input, output, both, or neither») — ya cubierta: P500 H02, P503 (entidades desde la pregunta), P506 H02, P517 H02 (contrato mínimo derivado de la pregunta).
- **Señales de alcance de curso** (registradas sólo en este log):
  - gobernanza, plan de gestión de datos, arquitectura de datos y 4V (p. 14 «CAP-P.3.2.4 Identify the appropriate data architecture»; «CAP-P.3.3.1 Identify the consequences of a poor data strategy, poor data governance…»; «CAP-P.3.2.7 … 4 Vs») — fuera de alcance: arquitectura y gobierno empresarial son frontera explícita del curso (`s05-diseno-data.md`).
  - pila tecnológica y debilidades de la hoja de cálculo (p. 18 «CAP-P.4.4.2 Identify the weaknesses of a spreadsheet analytics model») — marginal: `data.C05` ya trata herramientas como habilitadores (P500 `tool_boundary`).
  - datos incorrectos en producción, documentación para audiencias (p. 23 «CAP-P.6.6.1 Identify causes of incorrect data in production systems»; p. 25 «CAP-P.7.6.1 Identify the types of documentation needed for various audiences») — fuera de alcance (productos de datos) / ya cubierta (P501 H02: interfaz y consumidor por salida).
  - dominios I–II y IV–VII (encuadre, métodos, modelos, despliegue, ciclo de vida) — fuera de alcance de `data`.

## S03.P500.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - matriz de bus, arquitectura de bus empresarial, dimensiones conformadas, hechos de tiempo real, supertipo/subtipo (pp. 13–14, 24) — fuera de alcance: arquitectura empresarial excluida por `s05-diseno-data.md`.

## S03.P500.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Missing and conflicting data» (p. 45) frente a «Product Base Margin tiene 16 valores faltantes», escrito como texto fijo — marginal respecto de este documento: defecto ya registrado por S02 (S03 «faltantes […] no verificados»); el documento no añade un argumento específico.
- **Señales de alcance de curso** (registradas sólo en este log):
  - necesidad de datos reales y «messy» y de preguntas mal planteadas, no «canned» (pp. 38–39) — ya cubierta: Superstore con BOM y convenciones regionales (P500 H01, P513 H01), Scopus (P503), Vermont con granos mezclados (P516 H01), volcado de otro motor (P510 H01).
  - «Think about how a data processing workflow might be affected by data issues» y «Ingest, clean, and then wrangle» (p. 40) — ya cubierta (P500 H04, P511 H02, P516–P517, P526 H01).
  - flujo de trabajo y reproducibilidad: documentación, notebooks, análisis reproducible (pp. 46–47) — ya cubierta por `data.C04` (P501 H02, P502 H03, P503 H01, P517 H04). El control de versiones (p. 47) queda fuera de alcance como tema del curso: ya opera como infraestructura de distribución (GitHub Actions).
  - «Record retention policies» (p. 45) — fuera de alcance: gobernanza organizacional sin caso; sólo se recoge, como condición de uso, dentro de la candidata P502.
  - ética entretejida en todo el currículo (Rec. 2.4, pp. 22 y 50; juramento pp. 137–138) — fuera de alcance como actividad nueva: no hay caso y desplazaría talleres. Sus vehículos locales y materiales son las candidatas P519 (privacidad) y P502 (permisos y crédito de fuentes).
  - ausencia generalizada de manifiestos de procedencia (S01 «sin procedencia» en P500, P501, P510, P516, P519–P526) — marginal como señal de este documento: `AGENTS.md` ya exige preservar procedencia y restricciones. Es un defecto de cumplimiento de implementación más que una contribución nueva de aprendizaje; P502 concentra la parte conceptual.
  - dashboards para monitorear una base que evoluciona (p. 45) — fuera de alcance (Descriptiva y productos de datos).
  - evaluación del aprendizaje en ocho pasos de Jordan (p. 89) — fuera de alcance de S03 (la evaluación es participación con `pytest` por convención).

## S03.P500.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Calidad: aplicación de reglas de limpieza (tiempos mínimos, duplicados), control de completitud, consistencia de escalas» (p. 238); «Trazabilidad y gobernanza: separación clara entre evidencia empírica … y supuestos de negocio» (p. 41). Categoría: ya cubierta. Controles de calidad ejecutables (P500 H04), reglas nombradas con dimensión y conteo (P516 H02), contrato y decisiones persistidas (P517 H02–H04).
  - «Pensamiento analítico: Formular preguntas correctas, encontrar patrones, interpretar métricas y KPIs» para Analista de Datos (p. 219). Categoría: ya cubierta. Contrato de métrica independiente de la herramienta (P500 H03) y grano derivado de la pregunta (P500 H02).
- **Señales de alcance de curso** (registradas sólo en este log):
  - proyectos académicos con «requisitos completamente definidos, sin integración con sistemas existentes» (p. 183); «los problemas llegan incompletos, contradictorios» (p. 177). Categoría: marginal. Señal pedagógica general de pertinencia de `data.C01`; la debilidad de C01 en talleres con preguntas dadas (P505, P508, P518) ya está registrada por S02 y el documento no especifica práctica.
  - Excel avanzado, Power BI/Tableau, «Storytelling con datos», «Presentación de informes» (pp. 96, 102, 176, 218–220). Categoría: fuera de alcance. Visualización y comunicación de hallazgos pertenecen a Descriptiva; herramientas BI no definen identidad (`data.C05`).
  - ML en producción con «data cleaning, normalización», «model drift, data drift», MLOps (p. 176); roles emergentes LLMOps, Knowledge Engineer («ETL, vector DB + knowledge graphs, calidad de datos», p. 160), Synthetic Data Engineer (p. 334). Categoría: fuera de alcance. Productos de datos/IA y construcción de modelos, fronteras explícitas del curso; los datos sintéticos además están restringidos por `AGENTS.md`.
  - cloud, contenedores, CI/CD, IaC, DevSecOps (pp. 175–176); certificaciones Azure/AWS/Databricks/Snowflake (pp. 79–80). Categoría: fuera de alcance. Infraestructura y operación; la familia governmental no prescribe herramientas.

## S03.P500.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - pertinencia laboral del análisis de datos (p. 2 «3. Análisis de Datos» entre las temáticas priorizadas; p. 2 «enfocado en las áreas más demandadas por el mercado: datos, programación, ciberseguridad…»; p. 1 «dominio de áreas como la inteligencia artificial (IA) y el análisis de datos») — ya cubierta: respalda la existencia del curso como optativo, sin definir estándar ni contenidos (familia governmental).
  - formato bootcamp intensivo (p. 2 «carecen de acreditación por entidades educativas convencionales, no siguen planes de estudio estándar») — fuera de alcance: modalidad de formación no aplicable a un curso de pregrado.

## S03.P500.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - calidad y representatividad de datos como causa de fallas (p. 5, Módulo 2 «Calidad de datos, representatividad y por qué fallan los modelos») — ya cubierta en lo que corresponde a `data.C03` (P516 H01–H03, P510 H03); el vínculo con fallas de modelos es de Predictiva.
  - obtención y gestión de datos para ML (p. 5 «Obtención y gestión de datos para machine learning») — marginal: enunciado de temario sin práctica; adquisición y estructuración ya ejercitadas (P503, P510, P518).
  - privacidad y sesgos (p. 6, Módulo 8 «Consideraciones de política y riesgo: sesgos, propiedad intelectual, privacidad y alucinaciones») — marginal: la minimización de atributos sensibles se propone desde CRISP-DM (P519); aquí es un tema ejecutivo de IA generativa.
  - gobernanza y estrategia de IA, equipos, robótica, visión, PLN (pp. 5–6) — fuera de alcance de `data`.

## S03.P500.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «principles and practices of managing data at scale» y «a focus on ensuring reliable, scalable operationalization» (p. 1). Categoría: fuera de alcance. Escala y operacionalización confiable son la frontera excluida (operaciones distribuidas, pipelines productivos, MLOps; pertenecen a productos de datos). El curso de Berkeley es explícitamente de Data Engineering y su posición —después de un curso de ciencia de datos y con prerrequisitos de programación— contrasta con un optativo de pregrado sin prerrequisitos subordinado a Analytics (`s05-diseno-data.md`); la ficha institutional ilustra otra operacionalización, no impone identidad.
  - «collaboration» como etapa del ciclo de vida (p. 1). Categoría: marginal. Mención sin práctica concreta; la documentación reproducible ya está en `data.C04` (manifiestos P501/P511, linaje P502, contrato P517).

## S03.P500.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «differential privacy» como tópico (p. 1). Categoría: fuera de alcance. Es una técnica de inferencia/publicación con garantías formales que exige base probabilística ausente en un optativo sin prerrequisitos; la ficha no la operacionaliza. La preocupación de privacidad del curso (`ssn` en P519–P521, `user_id`/`user_session` en P526) es de procedencia y minimización, ya escalada por S02 en esos logs, no de privacidad diferencial.
  - «modeling and decision-making life cycle in data science including its human, social, and ethical implications» (p. 1). Categoría: marginal. Enunciado genérico de catálogo, sin práctica ni evidencia concreta; la dimensión responsable ya está en `data.C04` y no cambia lo que el estudiante hace en ningún Pxxx.
  - «basics of experimental design», «causal inference», «permutation testing», «false discovery rate», «Thompson sampling», «Q-learning» (p. 1). Categoría: fuera de alcance. Inferencia, causalidad y decisión secuencial pertenecen a los cursos descriptivo/predictivo/prescriptivo, no a la preparación de datos.

## S03.P500.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Las cuatro “V” del Big Data: volumen, variedad, velocidad y veracidad» (p. 7) — marginal: marco conceptual; veracidad como calidad ya se ejerce en P516–P517.
  - experimentación, ML, redes neuronales, prescriptivo y sesgos de decisión (p. 6–8) — fuera de alcance: pertenecen a otros cursos.

## S03.P500.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Containers and Keys ... container orchestration ... Public Key Infrastructure» (p. 13); «Serverless», «Cloud Native ... Kubernetes» (p. 14–15) — fuera de alcance: infraestructura y arquitectura, excluidas por la frontera del curso.
  - métricas DevOps «Wait Time, Deployment Frequency, Service Restoration Time, and Failure Rate» (p. 14) — fuera de alcance: operación de software/productos de datos.
  - «Mobile and IoT: Everyone Generating Data» (p. 13) — marginal: contexto histórico sin práctica ni caso asociado.

## S03.P500.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Apply best practices in data governance and cybersecurity» (p. 7); «Data Governance and Compliance», «Ethics – AI Bias and Fairness» (p. 15) — marginal: enunciados sin práctica; la documentación responsable del curso (C04) ya se ejerce en P500 H03, P502 y P517; sesgo de modelos de IA es de otros cursos.
  - «Leverage existing company data for success and derive value from dormant data» (p. 7); «Artisan vs. Factory» (p. 14) — fuera de alcance: estrategia organizacional sin caso ni datos.

## S03.P500.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión y predicción, clasificación y pruebas de hipótesis, aprendizaje profundo, sistemas de recomendación y modelos gráficos. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Python, NumPy, pandas y visualización como fundamentos (p. 6 «Python for Data Science / Numpy / Pandas / Data Visualization») — ya cubierta como habilitador (pandas en P500, P511, P516); `data.C05` impide que la herramienta sea identidad.
  - preprocesamiento y representación de datos para modelos (p. 7 «Beyond K-means: Data and pre-processing»; p. 5 «Choose how to represent your data when making predictions») — fuera de alcance: representación para predicción es de Predictiva; la elección de representación para almacenamiento ya está en P524.
  - estadística descriptiva e inferencial, clustering, regresión, clasificación, deep learning, recomendación, redes (pp. 6–11) — fuera de alcance de `data`.

## S03.P500.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre el proceso de diseño de productos de IA (cuatro etapas, modelo de Lawler), fundamentos de ML y deep learning, HCI, «superminds» y *capstone* de propuesta de producto de IA. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Analyze technical and operational requirements to build AI models» (p. 6); costos y requisitos técnicos de un plan de desarrollo de IA (p. 6) — fuera de alcance: requisitos de productos de IA (curso de productos de datos/IA), no requisitos de datos para una pregunta.
  - ML, deep learning, HCI, GANs, GPT-3 (pp. 4, 6–7) — fuera de alcance.
  - ejercicios en Jupyter Notebook (p. 8) — marginal: práctica de herramienta ya presente en el curso.

## S03.P500.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo sobre estrategia de plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura técnica, APIs y estándares, regulación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Growing the Platform: Ensuring Quality and Robustness — Gating – Establishing Quality» (p. 15) — fuera de alcance: calidad de participantes de la plataforma, no calidad de datos.
  - «Modeling Network Effects» (p. 15) — fuera de alcance: modelado de dinámica de mercados, sin relación con C01–C05.

## S03.P500.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso de educación profesional del MIT: ecuaciones diferenciales y métodos numéricos, modelado espacial (EDP), optimización y modelado guiado por datos, de la optimización al ML (regresión, regularización, clasificación), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos industriales. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Parameter Estimation and Nonlinear Least Squares», «Regression Problems», «Regularization», «Logistic Regression», «Assessing Model Fit» (p. 2) — fuera de alcance: construcción y evaluación de modelos, propias del curso predictivo; el curso `data` excluye «la construcción completa de modelos».
  - «Monte Carlo Simulation», «Probabilistic Forecasting», «Sensitivity Forecasting», «Simulating Rare Events» (p. 2) — fuera de alcance: análisis predictivo/prescriptivo.
  - «Ordinary Differential Equations», «The Forward Euler Method», «Partial Differential Equations», «Linear Systems: Direct and Indirect Methods» (p. 1) — fuera de alcance: modelado y simulación numérica, sin relación con adquisición, estructuración, calidad o documentación de datos.
  - casos «Aurora Flight Sciences», «Schlumberger», «BASF» (p. 2) — fuera de alcance: el calendario no describe ningún trabajo sobre datos que pueda contrastarse con un taller; la familia institucional sólo ilustra posibilidades.
  - el documento no contiene ninguna señal sobre acceso, integración, calidad, procedencia, metadatos, privacidad o formatos de datos; no hay contraste posible con P500–P526.

## S03.P500.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa profesional de 6 meses orientado al empleo como data engineer: Python, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, streaming (Kafka, MQTT), seguridad web y ML/RL; evaluación por portafolio en GitHub. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - propósito del programa (p. 2: «the data must be configured, warehoused, and made accessible, and data engineers are responsible for building the infrastructure»); objetivos de seguridad de red, JWT, Java/Spring, Node.js (p. 8, p. 10) — fuera de alcance: identidad de Data Engineering/software, explícitamente fuera de la frontera del curso (`s05-diseno-data.md`).
  - CDC con Debezium y bases MongoDB/Cassandra/Redis/Firebase en contenedores (p. 8: «Perform change data capture (CDC)»; p. 10: «perform CDC in different types of databases») — fuera de alcance: operación de sistemas y pipelines productivos.
  - pipelines con NiFi, Hadoop, Spark y Airflow (p. 11: «create data pipelines for big data processing. You will use PySpark to query big data») — fuera de alcance: Big Data y orquestación; `case-selection.md` excluye PySpark/Hive/Pig como contenido.
  - módulos de ML, RL y redes profundas (p. 9, p. 11, p. 12) — fuera de alcance: pertenecen a Predictiva/otros cursos.

## S03.P500.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de 6 meses con cinco partes (fundamentos de data science, optimización, ML, ML avanzado, despliegue), casos (retail, análisis facial, Filatoi Riuniti, BlueBike) y *capstone* de portafolio; herramientas Python y Google Colab. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Module 16: Fairness and Bias Issues in Data-Driven Predictions» (p. 8) y caso de algoritmos de análisis facial «detect, diagnose, and mitigate biases» (p. 10) — fuera de alcance: sesgo de modelos predictivos (curso predictivo); el sesgo de datos del curso ya aparece como límite en P510 sin caso propio.
  - «Survey the essentials of data science including data, models, processes» (p. 7); prerrequisito «familiar with Excel datasets» (p. 6) — marginal: no especifica prácticas de datos.
  - «applying techniques such as data augmentation, transfer learning, and data filtering» (p. 11) — fuera de alcance (preparación para ML).
  - clustering, regresión, optimización, redes neuronales, NLP, «Data, Models, and Decisions» (pp. 7–9) — fuera de alcance (cursos de línea).

## S03.P500.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh, estudios de trade-off, modelos de valor, generación de espacios de diseño, tradespace, frente de Pareto y sensibilidad. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - modelos de valor y caracterización de diseños mediante atributos organizados en jerarquías (p. 2: «characterize a design using attributes and how to organize attributes in hierarchies for evaluation and summation») — fuera de alcance: modelado de valor para decidir entre alternativas (prescriptiva/ingeniería de sistemas); no trata requisitos ni preparación de datos.
  - generación y evaluación de espacios de diseño, tradespace, frente de Pareto, sensibilidad y robustez (pp. 3–4) — fuera de alcance: pertenecen a la línea prescriptiva.
  - pre-evaluación y post-evaluación para medir la línea base del estudiante (pp. 1, 4) — fuera de alcance de S03 por Pxxx: es diseño de evaluación del curso, no refuerzo de un taller; la evaluación de los Pxxx está fijada en `pytest` por `AGENTS.md`.
  - reparto de tareas entre modelos y personas (p. 4: «task allocation between models and people») — fuera de alcance: autoridad humana en decisiones, tema de prescriptiva.

## S03.P500.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo), mapeo de atributos de prototipo y producto, decisiones de fabricación y análisis de costo-valor. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Assess data gathered from concept prototypes to make smart decisions» (p. 5); «Part B: Participants will assess the data results for the different processes used» (p. 8) — fuera de alcance: evaluación de resultados de pruebas de fabricación, sin relación con preparación, calidad o documentación de datos para Analytics.
  - procesos de fabricación serial/paralela, DFM, costo de prototipos (pp. 6–7) — fuera de alcance (ingeniería de manufactura). La coincidencia léxica «serial y paralelo» no tiene relación con P522.
