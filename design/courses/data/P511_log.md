# Log — P511

## S01.P511.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Evidencia:** manifiesto, notebooks, entregables, pruebas y trazabilidad.
- **Decisión:** mapa creado; se confirmó integración many-to-one y preservación de grano.

## S02.P511.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P511_superstore_integracion/` (`data/*.csv`, `data/source_manifest.json`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/`, `tests/test_activity.py`); P500–P503 para relaciones.
- **Trazabilidad revisada:** P511 → `data.C01`–`data.C05`; C05 mínima.
- **Highlights:** añadidos H01 (claves contextuales porque `Order ID` no es clave; caso y datos), H02 (uniones `many_to_one` validadas y conservación del grano), H03 (agregación posterior a la integración con detalle y respuesta persistidos).
- **Preservado:** pregunta, cuatro fuentes, claves sustitutas, validación many-to-one, preservación del grano y doble entrega.
- **Corregido:** la descripción previa decía que la pregunta «se parece a P500»; P500 responde evolución mensual, la comparación pertinente es `category_sales` de P501.
- **Añadido:** conteos de filas por tabla; ejemplo de `Order ID` repetido; columnas `Customer ID_x/_y` en la salida; fechas como texto; utilidad negativa visible no interpretada; pruebas de sólo existencia; duplicación con P514.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** el generador de las tablas derivadas no está en la actividad; las claves contextuales impiden contar clientes o productos únicos.
- **Superficies / contrato / dependencias:** S01–S06; recibe caso de P500–P502; habilita datos y práctica para P512, P514, P515.
- **Auditoría de Analytics:** integración al servicio de una descripción trazable; sin riesgo de identidad relevante.

## S03.P511.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Integration (pp. 71–72: «schema mapping», «data mapping», «challenges brought by heterogeneous data sources») — ya cubierta: claves contextuales y validación de cardinalidad (H01, H02).

## S03.P511.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 (merge/join, transform) (p. 5) — ya cubierta por P511 H01–H03; P514/P515 repiten la técnica (duplicación ya registrada por S02).

## S03.P511.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.5.1 «merging/joining data across sources may require business rules» (p. 15) — ya cubierta por P511 H01 (claves contextuales) y H02.

## S03.P511.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - transformaciones y uniones necesarias (p. 15 «CAP-P.3.5.1 Identify the transformations and merge/joins that may be necessary to solve an analytics problem») — ya cubierta: P511 H01–H03.

## S03.P511.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - prohibición de unir dos tablas de hechos y *drill across*; claves foráneas nulas → fila por defecto (pp. 7, 20) — ya cubierta (P511 H02 valida cardinalidad) o marginal (no hay dos hechos en el curso); la falta de validación en P515 es un defecto ya registrado por S02, no una señal nueva de este documento.

## S03.P511.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco autorizado de la NASEM para la formación de pregrado en ciencia de datos. Define la «data acumen» y diez áreas conceptuales (entre ellas gestión y curaduría de datos, flujo de trabajo y reproducibilidad, ética) y pide que la ética atraviese todo el currículo. Respalda expectativas generales, no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «muchos candidatos presentan consultas SQL básicas, pero carecen de la comprensión de modelado de datos avanzado, … normalización vs. desnormalización» (p. 175); «construir modelos lógicos de datos» como pilar crítico para Data Analyst (p. 252). Categoría: ya cubierta. Normalización de multivalor con PK/FK (P503 H02, H04), tabla plana integrada (P511 H01–H03) y hecho–dimensiones que contrasta con la tabla plana (P512 H02) ya ejercen el contraste.
  - «Integración de fuentes» como habilidad del dominio «Data & features» (p. 96; p. 231: «Integración de fuentes (133)»); «integrar fuentes de datos y permitir políticas basadas en evidencia» (p. 291). Categoría: ya cubierta. Integración por claves contextuales con cardinalidad validada (P511 H01–H02) y conciliación del agregado con la fuente (P510 H03).

## S03.P511.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.

## S03.P511.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión y predicción, clasificación y pruebas de hipótesis, aprendizaje profundo, sistemas de recomendación y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre el proceso de diseño de productos de IA (cuatro etapas, modelo de Lawler), fundamentos de ML y deep learning, HCI, «superminds» y *capstone* de propuesta de producto de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo sobre estrategia de plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura técnica, APIs y estándares, regulación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.18

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md` (`source_sha256`: 79b1abc97cbce8aa37117c6fb9022e96fe2a7afea71e9407286566f162bd5f9f).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso de educación profesional del MIT: ecuaciones diferenciales y métodos numéricos, modelado espacial (EDP), optimización y modelado guiado por datos, de la optimización al ML (regresión, regularización, clasificación), métodos probabilísticos (Monte Carlo, pronóstico probabilístico, eventos raros) y casos industriales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.19

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-engineering.md` (`source_sha256`: 25a5f3fc44350ec6a04b328ea85fcbc347805ed3ed9311582307cecb053d9245).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa profesional de 6 meses orientado al empleo como data engineer: Python, SQL, ETL, CDC, contenedores, Hadoop/Spark/Airflow, streaming (Kafka, MQTT), seguridad web y ML/RL; evaluación por portafolio en GitHub. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.20

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-professional-certificate-data-science-and-analytics.md` (`source_sha256`: 4479888772ec5aa0a0019963427debfe459a378a742332ed677c0bf147ee18ec).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de 6 meses con cinco partes (fundamentos de data science, optimización, ML, ML avanzado, despliegue), casos (retail, análisis facial, Filatoi Riuniti, BlueBike) y *capstone* de portafolio; herramientas Python y Google Colab. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.21

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` (`source_sha256`: 6f42b0cf5be3ac717cded9a3cdf6aa391b812103fa356ef39928b589232a13c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Calendario de un curso en línea de cuatro semanas sobre decisiones tempranas de diseño en ingeniería de sistemas: método de Pugh, estudios de trade-off, modelos de valor, generación de espacios de diseño, tradespace, frente de Pareto y sensibilidad. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.22

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-rapid-prototyping-methodologies.md` (`source_sha256`: 842362a7d12ef4fcb716b15b734a97d4b3b133bf916bc5d3814910fd1bad9e35).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre prototipado rápido de productos físicos (impresión 3D, corte láser, CNC, moldeo), mapeo de atributos de prototipo y producto, decisiones de fabricación y análisis de costo-valor. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.23

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/pwc-data-and-analytics-academy.md` (`source_sha256`: 7ea6edc72e56ac52fe8e9d400e862a4f8364403ab96014337267bbb15e9fd9cc).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo de cursos presenciales cortos (3–5 días): Data Science for Business Professionals/Beginners/Intermediate, Advanced and Predictive Analytics, masterclasses ejecutivas y *fast tracks*, centrados en visualización con PowerBI, R/Python, estadística, regresión, ML y series de tiempo. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.24

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/stanford-ai-strategy-governance.md` (`source_sha256`: 6804f61aea9b63a25cd8d0ecfbaceb1ef72c6cc55808a2f9a0195e97eec46e9a).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo combinado (en línea + 3,5 días en campus) sobre estrategia, liderazgo, innovación, futuros y gobernanza de IA generativa y agéntica para directivos con más de 10 años de experiencia. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.25

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/uchicago-data-science-business.md` (`source_sha256`: 1cb81bb95eb1f98571222705505c67810c28fe4e8f8f5acb78fd300f295b4330).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - certificado en línea de diez meses en español con cinco cursos de ocho semanas: Data Engineering, Ciencia de Datos con Python, Estadística, IA y ML, y Storytelling y visualización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.26

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-armonizacion-ejercicio-piloto.md` (`source_sha256`: 1f567c2f6e310549350ac1cc4b882d8cad05f44f23a2c1eaf0a0ec597dc0b6f5).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - informe de la Dirección Nacional de Programas Curriculares de Pregrado de la UNAL sobre cuatro talleres participativos con 17 programas de pregrado (p. 8) acerca de qué es el currículo, pertinencia frente al contexto, integración de docencia/investigación/extensión, prácticas pedagógicas (fines, contenidos, estrategias, recursos, evaluación) y propuestas para superar el «currículo endogámico». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.27

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unal-lineamientos-armonizacion-curricular.md` (`source_sha256`: 0a5ef2b6b086003d2c8fabd9c68ed20f4cc44045f4fff0ef43467836b884d17e).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - circular de la Dirección Académica de la Sede Manizales. Establece una «Ruta de Armonización Curricular» en cuatro etapas: marco normativo, pertinencia y resultados de aprendizaje, organización curricular, e implementación y evaluación continua. La orienta al Acuerdo 02 de 2020 del CESU (resultados de aprendizaje) y al Acuerdo 033 de 2007 del CSU, en las dimensiones macro, meso y microcurricular. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.28

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` (`source_sha256`: cd9a1e72271e37452be9a425519dc29793017dc7885d3762186f609799cd4a72).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso de posgrado de minería de datos aplicada a datos de salud (EHR), con un proyecto por entregables (propuesta, reporte de recolección de datos, reporte de preparación, informe final) y un survey paper. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.29

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/usc-introduction-to-data-analytics.md` (`source_sha256`: 6f6328e7a65605f64f761ce7e25f666a786620b4adce460f661ac159574d6962).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Combining data in SQL ... JOIN and UNION», «INNER, RIGHT, FULL OUTER, EXCEPTION and CROSS JOINs», «COALESCE» (p. 6) — ya cubierta: P510 H02 (`LEFT JOIN` + `COALESCE` conservando cursos sin calificación) y P511 H02 (cardinalidad validada). La pérdida silenciosa de claves en la unión de P521 (H02) es un defecto ya registrado por S02; el listado de tipos de JOIN de USC no aporta evidencia adicional.

## S03.P511.30

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/ut-austin-agentic-ai-business-applications.md` (`source_sha256`: ab39264039fbf3a76b5310aa59491c73d31b41adf2e8674a661261eb184ff484).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa online de 12 semanas, con ruta con o sin código, sobre IA generativa, prompts, RAG, agentes con herramientas y memoria (LangChain, LangGraph, MCP), sistemas multiagente, su evaluación y protección. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P511.31

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` (`source_sha256`: 72dc78abd90b10b2b9a299bb856c79f05470804368732ad6f516b77dfc3d2891).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - trampas de abanico y abismo en uniones (p. 3 «Identifying Fan traps / Resolving Fan traps», «Identifying Chasm traps») — ya cubierta: el riesgo que modelan (doble conteo al unir por relaciones uno a muchos) está en P511 H02 (`validate="many_to_one"` + conservación del grano) y P505 H02 (autoría completa sobre muchos a muchos); la formulación como «trampa» es propia de diseño de universos BI.

## S03.P511.32

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` (`source_sha256`: 6614428fdf3c7486e7f09a9e7f2f5fb98bb359b024197bb84fd7ad19021057b2).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - calidad y limpieza de datos (p. 2: «Problems found in realistic data: errors, missing values, lack of consistency, and techniques for addressing them»; p. 2: «coping with missing and dirty data») — ya cubierta: P500 H04 (controles ejecutables), P510 H03 y P511 H02 (conciliación y cardinalidad), P516 H01–H03 (reglas con dimensión).
