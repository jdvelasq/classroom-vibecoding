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

## S03.P500.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos presenciales cortos (3–5 días): Data Science for Business Professionals/Beginners/Intermediate, Advanced and Predictive Analytics, masterclasses ejecutivas y *fast tracks*, centrados en visualización con PowerBI, R/Python, estadística, regresión, ML y series de tiempo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «practical application with large data sets containing missing values and outliers» dentro de GLM (p. 8) — fuera de alcance (contexto de modelado predictivo); el tratamiento de faltantes como requisito de datos ya se discute en P500/P510.
  - visualización/dashboards con PowerBI/Tableau, regresión, ML, series de tiempo, optimización (pp. 4–14) — fuera de alcance (cursos descriptivo, predictivo y prescriptivo); la familia institutional ilustra, no impone.

## S03.P500.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo combinado (en línea + 3,5 días en campus) sobre estrategia, liderazgo, innovación, futuros y gobernanza de IA generativa y agéntica para directivos con más de 10 años de experiencia. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - cultura de excelencia en datos (p. 16 «Creating a culture of data excellence»; p. 5 «Data excellence») — marginal: título de sesión sin contenido operativo; no cambia ninguna capacidad `data.C01`–`C05`.
  - configurar flujos y decisiones para ML (p. 16 «Configuring workflows and decisions for machine learning (ML)») — fuera de alcance (Predictiva/Prescriptiva y organización).
  - gobernanza, riesgo, controles empresariales y confianza (p. 17 «AI Governance, Enterprise Controls and Program Wrap-Up») — fuera de alcance: gobierno empresarial es frontera del curso.
  - estrategia, modelos de negocio, futuros, liderazgo (pp. 3–19) — fuera de alcance.

## S03.P500.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses en español con cinco cursos de ocho semanas: Data Engineering, Ciencia de Datos con Python, Estadística, IA y ML, y Storytelling y visualización. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Aplicar las herramientas de inteligencia empresarial (BI) … paneles de Tableau» (p. 6); estadística, ML, *storytelling* (pp. 7–8) — fuera de alcance (descriptiva y otros cursos).
  - el programa nombra su primer curso «Data Engineering» (p. 5) — contexto institucional; no impone identidad: el curso `data` excluye explícitamente Data Engineering.

## S03.P500.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - informe de la Dirección Nacional de Programas Curriculares de Pregrado de la UNAL sobre cuatro talleres participativos con 17 programas de pregrado (p. 8) acerca de qué es el currículo, pertinencia frente al contexto, integración de docencia/investigación/extensión, prácticas pedagógicas (fines, contenidos, estrategias, recursos, evaluación) y propuestas para superar el «currículo endogámico». Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - evaluación enfocada en la resolución de problemas y en el «saber hacer», con seguimiento por porcentajes de avance y no sólo del producto final (p. 82: «la evaluación debería adoptar una orientación sobre el seguimiento del “saber hacer”»; «debería expresarse como un seguimiento a diferentes porcentajes de su avance») — fuera de alcance: es una orientación institucional general de política de evaluación; los Pxxx son talleres guiados evaluados con `pytest` de participación (AGENTS.md), y la evaluación sumativa del saber hacer corresponde a los `Lxxx`, no a S03 sobre talleres. No cambia lo que el estudiante hace en ningún Pxxx concreto.
  - autoevaluación y coevaluación (p. 69: «Incluir autoevaluación y coevaluación»; p. 82: «dos componentes hasta ahora dejados de lado en los mecanismos de evaluación: autoevaluación y coevaluación») — fuera de alcance: decisión de diseño de evaluación del curso/programa, no una capacidad de datos ni un defecto de un taller; un documento institutional ilustra posibilidades, no impone instrumentos.
  - aprendizaje anclado a problemas reales y contexto (p. 72: «Apuntar a problemas reales»; p. 82: «conexión con el contexto a partir del abordaje de temas relevantes en el momento actual») — ya cubierta como principio: la identidad del curso (`data.C01`, pregunta → requisitos de datos) y `case-selection.md` ya exigen casos reales y trazables con pregunta analítica. Los talleres sin pregunta (P513, P518, P519, P522–P525) ya están registrados como auditorías no resueltas en S02; esta señal genérica no aporta un argumento ni un caso nuevo para resolverlos.
  - recursos «simulaciones, casos de estudio», «laboratorios virtuales», «repositorio de software» (p. 72) y aulas híbridas/virtualidad (pp. 72, 80) — marginal: medios didácticos genéricos; el curso ya opera con talleres en código, datasets en repositorio y distribución por GitHub.
  - participación de egresados para leer el mercado laboral y la pertinencia del perfil (pp. 106–107) y objetivos medibles de la armonización (p. 110) — fuera de alcance: gobernanza curricular de programa, no contenido de un taller.
  - «Diferencias entre administración, contaduría, economía» y «No sólo la aplicación de modelos económicos» (p. 72) — fuera de alcance: notas de mapa mental de otros programas; sin relación con datos para analítica.

## S03.P500.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - circular de la Dirección Académica de la Sede Manizales. Establece una «Ruta de Armonización Curricular» en cuatro etapas: marco normativo, pertinencia y resultados de aprendizaje, organización curricular, e implementación y evaluación continua. La orienta al Acuerdo 02 de 2020 del CESU (resultados de aprendizaje) y al Acuerdo 033 de 2007 del CSU, en las dimensiones macro, meso y microcurricular. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - resultados de aprendizaje como «declaraciones expresas de lo que se espera que un estudiante conozca y demuestre» (p. 2) — fuera de alcance de S03: es gobernanza del diseño (S04.F11). `s05-diseno-data.md` ya fija las capacidades `data.C01`–`C05` y deja pendientes los RAA. El documento no aporta contenido de datos que cambie un taller.
  - dimensión microcurricular, es decir didácticas y evaluación de aprendizajes (p. 2), y diseño de «mecanismos de monitoreo y evaluación» de los RA (p. 3) — fuera de alcance de S03: afecta la trazabilidad RAP/RAA y la evaluación del curso, no lo que el estudiante hace en un Pxxx. La evaluación de talleres ya está fijada (participación con `pytest`).
  - pertinencia frente a «las exigencias y necesidades del medio, la actualidad de las áreas de conocimiento» (p. 3) — marginal: principio institucional genérico sin señal disciplinar concreta. La familia institutional ilustra, no impone.

## S03.P500.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso de posgrado de minería de datos aplicada a datos de salud (EHR), con un proyecto por entregables (propuesta, reporte de recolección de datos, reporte de preparación, informe final) y un survey paper. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - temario de minería de datos — probabilidad, regresión, asociación, clasificación, clustering, text mining (p. 9; p. 1: «data preprocessing and sampling methods, data distributions and uncertainty, statistics, regression, time-series analysis, predictions and clustering») — fuera de alcance: pertenece a Descriptiva/Predictiva.
  - «Getting to Know your Data» y «Data Preprocessing» (p. 9, semanas 2–3; TB2 caps. 2–3) — ya cubierta en su sentido de C02/C03 (perfilado y reglas en P516, limpieza e identidad en P503 H03, tipos y formato regional en P500 H01); el preprocesamiento orientado a modelado (normalización, discretización, reducción) es de Predictiva.
  - «Data Mining Project Deliverable 1 – Proposal ... describes the dataset, repository from where the dataset will be obtained, define the problem» (p. 6) — ya cubierta en el principio de C01 (pregunta → datos) de P500/P516/P526; sin proyecto integral en el curso por diseño de talleres guiados.
  - desafíos de datos clínicos de historias electrónicas (p. 1: «characteristics and analytic challenges on dealing with clinical data from electronic health records») — fuera de alcance: no hay caso ni datos trazables en `datalabs/`/catálogo que permitan enseñarlo con rigor, y añade sensibilidad de datos de salud.
  - survey paper y simposio (p. 6–7) — fuera de alcance: forma de evaluación ajena a talleres `Pxxx` con `pytest`.

## S03.P500.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Syllabus de pregrado sin prerrequisitos que combina modelado relacional, normalización, SQL, NoSQL/MongoDB, BI y visualización con Excel/Access/Tableau, más un proyecto final en equipo. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - objetivo «Pose questions, collect relevant data, analyze data, interpret data and provide insights» (p. 1) y proyecto «identify a problem to solve, collect the necessary data, prepare, clean and format the data» (p. 2–3) — ya cubierta en el principio de C01 (pregunta → requisitos de datos) que siguen P500, P510, P516–P517 y P526; el proyecto integral de análisis y dashboards pertenece a Descriptiva.
  - «Use MS Excel, MS Access, SQL, NoSQL, MongoDB and leading industry tools» (p. 1) — fuera de alcance: organización por herramientas contraria a C05.

## S03.P500.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa online de 12 semanas, con ruta con o sin código, sobre IA generativa, prompts, RAG, agentes con herramientas y memoria (LangChain, LangGraph, MCP), sistemas multiagente, su evaluación y protección. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Elementos clave de RAG (segmentación de datos, embeddings, almacén vectorial, recuperación, mejora, generación)» (p. 11) — fuera de alcance: preparación de datos para sistemas de IA generativa; no corresponde a C01–C05 ni hay caso en el curso.
  - «Seguridad y privacidad de los datos», «Registro de la toma de decisiones para una mayor transparencia», «Control de acceso e identidad» (p. 13) — fuera de alcance: protección de sistemas agénticos; la privacidad de identificadores en datos del curso ya está registrada por S02 (P519, P526).
  - «Pruebas unitarias», «Métricas de evaluación (precisión, latencia, robustez)», «Fundamentación, validación y veracidad» (p. 13) — fuera de alcance: evaluación de agentes, no de datos.
  - casos de agentes para análisis de datos financieros, salud y documentos legales (p. 14–16) — fuera de alcance: productos de IA, otro curso.

## S03.P500.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - syllabus de posgrado en almacenes de datos: repaso de bases de datos y modelado ER, modelado dimensional Kimball (hechos, dimensiones, SCD, trampas), universos de SAP Business Objects, reportes Web Intelligence y Tableau; explícitamente sin ETL. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - universos BI, seguridad por fila, reportes Web Intelligence y Tableau (p. 3 «What is a Universe»; p. 4 «Row level security», «Data Blending», «Building dashboards») — fuera de alcance: herramientas BI y comunicación de resultados pertenecen a Descriptiva/productos de datos; una señal institucional no impone herramientas.
  - contraste OLTP/estrella (p. 3 «OLTP vs. Star schema based universes») — marginal: el contraste ER (P503) / dimensional (P512) ya existe en la secuencia.

## S03.P500.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad y limpieza de datos (p. 2: «Problems found in realistic data: errors, missing values, lack of consistency, and techniques for addressing them»; p. 2: «coping with missing and dirty data») — ya cubierta: P500 H04 (controles ejecutables), P510 H03 y P511 H02 (conciliación y cardinalidad), P516 H01–H03 (reglas con dimensión).
- **Señales de alcance de curso** (registradas sólo en este log):
  - herramientas de línea de comandos (sort, count, join) y gnuplot/Perl (p. 2) — marginal: otra herramienta para operaciones ya cubiertas (data.C05).
  - estadística, regresión, SVD/PCA, clustering, clasificación, grafos (p. 2) — fuera de alcance: pertenecen a Descriptiva/Predictiva.
  - proyecto con peso 35 % y examen 50 % (p. 4) — fuera de alcance: la evaluación de `Pxxx_` está fijada por `AGENTS.md` (pytest de participación).

## S03.P500.33

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-methods-tools.md` (`source_sha256`: b1a7e1792ffe99353bb4b6f278489f4595ea4bd612dca9453bcf91efaebd9d45).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - lámina única que enumera los métodos y herramientas del programa: recolección de datos (encuestas, NPS, autorreportes; recolección pasiva; medios), A/B testing, correlación y causalidad, pronóstico, regresión, simulación (Analysis ToolPak, Solver), visualización e interpretación, optimización y árboles de decisión. Es sólo una lista de títulos, sin contenido, nivel ni evidencia. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Data Collection Methods — Descriptive Data Collection: Surveys, Net Promoter Score (NPS), and Self-Reports» (p. 1) — fuera de alcance: ningún taller usa datos de encuesta o autorreporte, y una lámina institucional sin contenido no basta para justificar un caso nuevo; además, diseñar instrumentos de encuesta no es habilitar datos existentes (`data.C01`–`C04`). Si en el futuro se incorpora una fuente de encuesta trazable del `catalog/`, sus sesgos de autorreporte entrarían en `data.C03`, pero hoy no hay caso ni datos.
  - «A/B Testing», «Correlation and Causation», «Forecasting» (tendencia, estacionalidad, suavizado exponencial), «Regression Analysis», «Simulation Toolkit» (Analysis ToolPak, Solver), «Optimization Models», «Decision Trees» (p. 1) — fuera de alcance: análisis descriptivo, predictivo y prescriptivo pertenecen a los otros cursos según `s05-diseno-data.md`; además, son herramientas de Excel que no imponen tema (familia institucional).
  - «Data Visualization and Interpretation» (p. 1) — fuera de alcance: la comunicación de hallazgos corresponde a Analítica Descriptiva; en `data` la evidencia visual es un medio de verificación (`AGENTS.md`), no un objetivo.

## S03.P500.34

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/wharton-business-analytics-program-modules.md` (`source_sha256`: 60bdb1bc81fa186446b82e893dd9058e3bfb02774b7dc7319bbd137d7d38f315).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - listado de un módulo de orientación y nueve módulos de un programa ejecutivo de Business Analytics organizado por la secuencia descriptiva → predictiva → prescriptiva → aplicación, cada uno con una frase de resultado; no detalla contenidos, datos, herramientas ni evaluación. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Module 9 (p. 1: «create a plan to put data to work in your organization») — marginal: formulación genérica de `data.C01`/`data.C05` (datos al servicio de una finalidad); no aporta producto ni práctica nueva. Un plan organizacional de datos se acerca a estrategia/gobierno de datos empresarial, fuera de la frontera del curso.
  - Modules 2–8 (p. 1: pronóstico con datos históricos; predicciones; simulación; predicción de desempeño de empleados con «hiring, internal mobility, and attrition»; optimización; árboles de decisión) — fuera de alcance: análisis descriptivo, predictivo y prescriptivo pertenecen a los otros cursos de la línea. El caso de personal (Module 6) traería datos sensibles de empleados sin caso trazable en el repositorio.
  - ausencia de un módulo de datos en un programa de Business Analytics — fuera de alcance como inferencia: un documento institutional de una página no permite concluir nada sobre el alcance de un curso de fundamentos de datos; sólo ilustra que el programa subordina los datos a las preguntas de cada línea, coherente con la identidad ya fijada en `s05-diseno-data.md`.

## S03.P500.35

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` (`source_sha256`: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Los tests sobre los datos en cada paso garantizan la calidad de la salida» (p. 54) — ya cubierta: P500 H04, P517 H04.
- **Señales de alcance de curso** (registradas sólo en este log):
  - DataOps, MLOps, producto de datos (pp. 44, 53–55) — fuera de alcance: productos de datos y operación.

## S03.P500.36

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-01-the-problem.md` (`source_sha256`: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «La poca calidad de los datos sigue siendo un desafío serio», «Existencia de errores en los datos», «Malos datos arruinan buenos reportes», «Falta de confianza en los datos» (p. 2). Categoría: ya cubierta. Controles ejecutables que condicionan la salida (P500 H04), diagnóstico de aptitud con reglas nombradas (P516 H01–H03) y contrato que clasifica cambios por su efecto en el análisis (P517 H02–H04). Es diagnóstico organizacional, sin práctica nueva.
  - en ML/DA «La lógica y los datos son críticos», «El testeo se basa en precisión no en ejemplos», «Se usan datos de producción» (p. 4). Categoría: fuera de alcance / ya cubierta. El contraste con la programación tradicional apunta a pruebas de modelos y a producción (otros cursos/productos de datos); las pruebas sobre datos ya existen como aserciones de calidad (P500 H04, P516 H02).
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Data Literacy es la habilidad de leer tablas y grafos, entenderlos para concluir correctamente y saber cuando se está potencialmente desinformado» (p. 6). Categoría: marginal / fuera de alcance. Leer y concluir pertenece a Descriptiva; «saber cuando se está desinformado» es la intuición de `data.C03`, ya ejercida en P516 (granos mezclados que confunden agregados) y P526 (tiempo de evento frente a orden de llegada).
  - «No se tienen las habilidades para llevar un modelo a producción», «laptop analytics», «fricciones con el equipo de TI», «Formación de DS focalizada en los algoritmos y no en la creación de un producto de datos operativo» (pp. 3, 9). Categoría: fuera de alcance. Pipelines productivos y operación son frontera excluida del curso (pertenecen a productos de datos).
  - CRISP-DM y cascada, decisiones por intuición, liderazgo y cultura, «Se debe buscar la gente correcta no educarla» (pp. 2, 5, 7). Categoría: fuera de alcance. Perspectiva de gestión organizacional, sin contenido de preparación de datos para un estudiante de pregrado.

## S03.P500.37

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` (`source_sha256`: e13a6b75b08f67349d770566a9bd1323925b4ddbed28854b902339f7510d6c42).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Ficha mínima de cada indicador» con definición, línea base y meta, fuente y método, responsable, frecuencia y decisión asociada (p. 23) — ya cubierta en lo que corresponde al curso por P500 H03 (contrato con fórmula y grano); responsable, meta, frecuencia y decisión son gestión de indicadores organizacionales, fuera de alcance.
- **Señales de alcance de curso** (registradas sólo en este log):
  - ciclo de vida completo del dato (captura→eliminación segura, p. 5) — marginal/fuera: el curso cubre adquisición–preparación–documentación; archivo y eliminación son gestión organizacional.
  - gobierno de datos (derechos de decisión, modelos centralizado/federado, p. 16), arquitectura (warehouse, lake, lakehouse, mesh «patrones posibles, no etapas obligatorias», p. 17) — fuera de alcance (arquitectura empresarial); la advertencia de p. 17 sólo confirma la frontera ya fijada para P512/P525.
  - caso de valor, VPN/ROI, priorización de portafolio, hoja de ruta, ejecución y evaluación de la estrategia (pp. 19–23) — fuera de alcance: gestión estratégica, no preparación de datos para una pregunta.

## S03.P500.38

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` (`source_sha256`: bce80eb1dc39c20fedbd6bc579395cec5b808e3bfa84772a72a57669d1600d3c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identificar las necesidades de datos. Determinar qué información requiere el problema analítico» (p. 13) — ya cubierta por P500 H02 y P517 H02 (contrato mínimo derivado de la pregunta).
- **Señales de alcance de curso** (registradas sólo en este log):
  - problema de negocio/problema analítico, 5W, partes interesadas (pp. 9–11) — fuera de alcance como contenido propio (P001 y cursos de línea); el déficit recurrente «sin usuario ni decisión» de varios Pxxx no se resuelve con esta fuente sin desplazar la identidad del curso.
  - descriptiva/predictiva/prescriptiva, diseño y evaluación de modelos, despliegue, monitoreo de *drift*, recalibración (pp. 16–26) — fuera de alcance (otros cursos y productos de datos).
  - sesgos y equidad, impacto social (p. 29) — fuera de alcance como evaluación de modelos; el sesgo de datos ya aparece como límite en P510 (calificaciones como adopción) sin caso que permita enseñarlo con rigor aquí.

## S03.P500.39

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-04-lean-thinking.md` (`source_sha256`: 51589d340c528ac102f01d9b5405b50121d52fbda3586fb8653ebf88048a0b36).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - causa raíz «no hay suficientes pruebas que garanticen que los datos defectuosos no entren en las pipelines o las bases de datos» y «Porque no entienden cómo usan los datos los consumidores» (p. 10) — ya cubierta: controles ejecutables que condicionan la salida (P500 H04), reglas de calidad como reporte (P516 H02) y contrato derivado del uso analítico (P517 H02). Aporta contexto, no una práctica nueva.
- **Señales de alcance de curso** (registradas sólo en este log):
  - value stream mapping, colas, control estadístico de procesos, teoría de restricciones (p. 7–9); capas del ciclo de vida de datos con cómputo distribuido, contenedores y orquestación (p. 12) — fuera de alcance: gestión de procesos y operación de productos de datos.

## S03.P500.40

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-05-agile.md` (`source_sha256`: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - presentación sobre gestión de proyectos: cascada frente a ágil, Scrum, XP, Kanban, escalamiento (SAFe, Scrum of Scrums, DAD), manifiesto DataOps, ciclo de vida analítico y prácticas ágiles para DataOps (épicas, MVP). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - ciclo de vida con adquisición, exploración y preparación de datos (p. 11 «Data acquisition, Data exploration, Data preparation, Feature engineering, Data pipeline development») — ya cubierta en sus etapas de datos (P503, P510, P511, P516); el resto (despliegue, entrenamiento) fuera de alcance.
  - hipótesis de épica que declara fuentes a integrar (p. 13 «Integrating — Sources and data types — Financial transactions and customer identity data») — marginal: derivar fuentes de un objetivo ya se ejerce como requisitos desde la pregunta (P517 H02, P500 H02); el formato de épica es gestión de portafolio.
  - Scrum, XP, Kanban, SAFe, roles y ceremonias (pp. 2–9, 12–14) — fuera de alcance: gestión de proyectos y organización de equipos no son capacidades `data.C01`–`C05`.

## S03.P500.41

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-06-definition.md` (`source_sha256`: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - pruebas de lógica de negocio y de datos antes de entregar (p. 4 «Tests para verificar los datos (lógica de negocio, tipo de dato, outliers, tendencias, consistencia, …)»; p. 9 «Hay al menos un test en cada paso») — ya cubierta: P500 H04 (compuerta de calidad), P510 H03 (conciliación agregado–fuente, el «balance»), P511 H02 (cardinalidad), P516 H02 (reglas nombradas).
- **Señales de alcance de curso** (registradas sólo en este log):
  - ramas, múltiples ambientes, contenedores, CI/CD, orquestación (pp. 11–17) — fuera de alcance: pipelines productivos y operación son frontera explícita del curso.
  - MLOps (p. 20 «Model serving», «Monitoreo del desempeño, incidentes y reentrenamiento») — fuera de alcance (productos de datos/MLOps).
  - cadena de suministro de datos y equipos (p. 19 «No se puede crear un dataset por cada idea nueva»; p. 18) — fuera de alcance: organización de equipos de datos.
  - principios de código fuente (p. 22 «Modularidad • Funciones dedicadas a una sola tarea … Testing • Control de versiones • Logging») — ya cubierta por la sección «Code clarity» de `AGENTS.md`; no es contenido del curso.

## S03.P500.42

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-07-cdo.md` (`source_sha256`: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Tests de datos» en el desarrollo (p. 5); «Robustez: por el uso de tests» (p. 2); «Monitoreo de la lógica de negocio y validez de los datos» (p. 10). Categoría: ya cubierta. Controles de calidad ejecutables que bloquean la salida (P500 H04), reglas nombradas con dimensión y conteo (P516 H02) y contratos ejercitados con lotes perturbados (P517 H04). La debilidad transversal «Pruebas: sólo existencia» ya está registrada por S02 en cada Pxxx; esta presentación organizacional no aporta un argumento nuevo para corregirla.
- **Señales de alcance de curso** (registradas sólo en este log):
  - priorización de resultados por entrevistas y «Oportunidad = Importancia + max(0, Importancia - Satisfacción)» (p. 7). Categoría: fuera de alcance. Es gestión de mejoras de un equipo de datos, no derivación de requisitos de datos desde una pregunta analítica (`data.C01`); no hay caso ni producto de datos donde aplicarlo.
  - «Corrección de errores en las fuentes de datos», «Preparación de datasets» como trabajo no planificado (p. 4); «Errores en datos» como cuello de botella (p. 6). Categoría: marginal. Contexto organizacional que confirma la pertinencia de `data.C03`, ya ejercida en P516–P517; no especifica práctica alguna.
  - coordinación relacional, Kanban, teoría de restricciones, trampas del CDO, etapas «Data Desert → Boutique → Waterfall → DataOps Analytics» (pp. 3, 6, 9, 11). Categoría: fuera de alcance. Perspectiva de gestión y madurez organizacional, sin contenido de preparación de datos para un estudiante de pregrado.

## S03.P500.43

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-08-data-scientids.md` (`source_sha256`: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - material de clase sobre DataOps: desarrollo tradicional frente a ML, deuda técnica, pruebas de datos y lógica, control de versiones, ambientes múltiples, contenedores, arquitectura canónica (raw lake → refined → data science), agile data warehousing, data lake y esquemas para análisis. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - «Tests de lógica y de datos», «Pruebas de validación de la data y la lógica de negocio» (pp. 6–7) — marginal: las reglas y aserciones de P500 H04, P511 H02, P516 H02 y P517 ya ejercen validación de datos al servicio de una pregunta; las pruebas automatizadas de pipeline son DataOps.
  - control de versiones, ramificación, ambientes dev/test/prod, Docker, orquestación (Airflow, Jenkins) (pp. 4, 6, 11) — fuera de alcance (operación de pipelines, MLOps).
  - «Los dashboards son tan valiosos como la data detrás de ellos, la cual usualmente es de baja calidad» (p. 12) — contexto: confirma el propósito del curso; no implica cambio.

## S03.P500.44

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` (`source_sha256`: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - pruebas de salida «Precios positivos», «Rangos esperados de los datos» (p. 4) — ya cubierta: H04 condiciona la salida a controles de calidad ejecutables; los faltantes y `Row ID` no verificados (S03) son variantes locales.
- **Señales de alcance de curso** (registradas sólo en este log):
  - tipos de prueba de software —unitarias, integración, funcionales, regresión, desempeño, humo— (p. 2) — fuera de alcance: prácticas de desarrollo y despliegue de pipelines productivos (DataOps), frontera del curso; además, en el curso `pytest` evalúa participación, no corrección (AGENTS.md).
  - *Value pipeline* / *Innovation pipeline*, ambientes de desarrollo idénticos a producción, proceso de liberación de código (p. 3) — fuera de alcance: operación de productos de datos.
  - *Statistical process control* / *time balance tests*, monitoreo continuo de patrones anómalos (p. 5) — fuera de alcance: monitoreo en producción (curso de productos de datos); sin caso con flujo continuo.
  - notificación automática y análisis de impacto de cambios entre equipos (pp. 2, 5) — fuera de alcance: gobierno operativo.
  - «Cada vez que algo falla se agrega una nueva prueba» (p. 2) — marginal: práctica de proceso, no cambia una capacidad de taller.

## S03.P500.45

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/dataops-10-organization.md` (`source_sha256`: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - rol DataOps con «Automatización de la calidad» y «Frameworks para tests de datos» (p. 5) — ya cubierta: P500 H04 condiciona la salida a aserciones ejecutables y P517 H02–H04 declara y ejercita un contrato de datos; automatizar en orquestación es pipeline productivo, fuera de la frontera.
- **Señales de alcance de curso** (registradas sólo en este log):
  - responsabilidades del analista de datos «Consulta, Limpieza, Exploración, Interpretación» (p. 5) — ya cubierta: consulta (P503–P508), limpieza y calidad (P500, P516) a lo largo de la secuencia; no indica una capacidad ausente.
  - estructuras de equipo, roles (product owner de datos, arquitecto, plataforma) y perfiles de habilidades (pp. 2–8) — fuera de alcance: organización de equipos de datos (productos de datos / gestión), sin contenido enseñable en un taller de preparación de datos; la familia literature-derived aporta contexto organizacional, no prescripción curricular.
  - herramientas listadas por rol (SQL, Talend, Hadoop, Hive, Spark, Tableau…; p. 5) — fuera de alcance: lista de herramientas; Hadoop/Hive/Spark contradicen la frontera fijada en `case-selection.md`.

## S03.P500.46

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` (`source_sha256`: 74f7fec85a90b098b365b0973449130a20a396b33adf06ec85e63e9c88250dcf).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «detecting missing values, duplicate records, or inconsistencies may prompt additional data acquisition or preprocessing» (p. 15) — ya cubierta: P503 H03 (identidad y faltantes antes de cargar), P500 H04.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Project Scope Definition — traducir objetivos de negocio a formulaciones con «inputs, outputs, constraints, and quantitative evaluation criteria» (p. 14) — ya cubierta en el principio de C01 (P500, P516–P517, P526); los talleres sin pregunta (P513, P518, P519, P522–P525) ya están escalados por S02.
  - Project Design, Model Evaluation, Operation and Maintenance, Continuous Improvement (pp. 17–22) — fuera de alcance: modelado, despliegue y monitoreo pertenecen a otros cursos.

## S03.P500.47

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` (`source_sha256`: 8f6bf519db1df06d80482cb26bfe9a642fa60ac8e2f40a283b70c00c418e01fd).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - distinción entre almacenamiento y medición («storage is different from Measurement», p. 83) e instanciación de valores (p. 84) — ya cubierta: P500 H01 y P513 H01 declaran el formato en la lectura; el defecto de tipos de P513 se trata con dataops-09, no con esta guía.
  - conversión de fecha ajustando el formato por defecto («Change the default date format to match the format of the Date field», p. 163) — ya cubierta: P512 H01 (dimensión de fecha desde `d/m/yy`) y P500 H01 (convención regional).
- **Señales de alcance de curso** (registradas sólo en este log):
  - Data Audit como «comprehensive first look»: estadísticos, histogramas y pestaña Quality con faltantes, *outliers* y extremos por campo (pp. 71, 74, 76–77) — marginal: perfilado de herramienta; el curso ya trata faltantes y reglas de calidad derivadas de la pregunta (P503 H03, P516 H02). Señal de herramienta que por sí sola no impone tema.
  - imputación de faltantes por C&RT o por media (p. 77: «impute or replace missing values … including the C&RT algorithm»; p. 148: «Impute when … Blank and Null values … Fixed As … Mean») y tratamiento de *outliers* «coerce, discard, or nullify» (p. 79) — fuera de alcance: preparación para un modelo (curso predictivo); el documento no aporta criterio para juzgar o documentar la imputación, que es lo que interesaría a `data.C03`/`C04`.
  - Automated Data Preparation «without needing to have prior knowledge of the statistical concepts involved» (p. 63), justificada por la exactitud del modelo (p. 68) — fuera de alcance y contraria a la identidad: la preparación automática no justificada choca con `data.C02` («de forma justificable»); ilustra el riesgo de que la herramienta organice el curso.
  - CRISP-DM como organización de proyectos (pp. 7, 20) — fuera de alcance como propuesta: marco metodológico de minería de datos, mencionado sin contenido sobre datos; no cambia un taller.
  - SQL/in-database modeling, generación de SQL (pp. 7, 18, 21) — fuera de alcance: modelado en el motor.
  - descarte de registros con objetivo nulo (p. 206: «Cases where the target has a null value are of no use when building the model») y filtrado de campos por importancia predictiva (pp. 147, 213) — fuera de alcance: preparación orientada al modelo.
  - derivación de atributos sobre series concatenadas y descarte del primer registro de cada serie «to avoid large (incorrect) jumps … at boundaries» (p. 230) — fuera de alcance: ingeniería de atributos para modelado, sobre datos ficticios (p. 227).

## S03.P500.48

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` (`source_sha256`: 809c02dec1cb9a61cff3fd52c4082bda09f6baa912367759af7f026e7b409571).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - coding schemes y unidades no estándar (p. 18 «one data set may use _M_ and _F_ … while another may use the numeric values _1_ and _2_»; p. 20 «Coding inconsistencies») — ya cubierta: H01 hace explícita la convención regional (separador, coma decimal).
- **Señales de alcance de curso** (registradas sólo en este log):
  - fase de formateo para el algoritmo, partición entrenamiento/prueba, normalización (p. 23 «Splitting into training and test data sets»; p. 25 «Do the data need be normalized before modeling?»; pp. 26–27) — fuera de alcance: pertenece a Predictiva.
  - objetivos de negocio, criterios de éxito, glosario de términos (pp. 9–13; p. 13 «if "churn" for your business has a particular and unique meaning, it is worth explicitly stating that») — ya cubierta: P500 H03 (métricas definidas con independencia de la herramienta), P506 H02 (operacionalización de un concepto), P526 H03.
  - restricciones legales y de acceso a datos (p. 12 «Have you verified all legal constraints on data usage?») — marginal como señal autónoma: el vacío de manifiestos de procedencia ya está registrado en S02 de casi todas las actividades; se concreta sólo en la candidata P519.
  - modelado, evaluación, despliegue, monitoreo (caps. 5–7, pp. 29–42) — fuera de alcance.
