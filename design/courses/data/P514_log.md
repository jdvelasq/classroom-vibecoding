# Log — P514

## S01.P514.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró ETL por etapas como diferencia técnica frente a P511.

## S02.P514.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P514_superstore_etl/` (`data/`, `professor/main.py`, `src/main.py`, `submission/`, `tests/test_activity.py`); P511 y P513 para relaciones; P515 para contraste.
- **Trazabilidad revisada:** P514 → `data.C01`–`data.C05`.
- **Highlights:** añadidos H01 (integración organizada en `extract`/`transform`/`publish`), H02 (reporte de filas por etapa con granos distintos; caso y datos).
- **Preservado:** pregunta, etapas raw/staging/curated, joins validados heredados, reporte de etapas y relación de extensión con P511.
- **Corregido:** «introduce publicación de datos curados» se precisa: staging y curated son el mismo DataFrame escrito dos veces, sin transformación entre ellas; el detalle publicado es igual al de P511.
- **Añadido:** raw = 5926 como suma de cuatro granos; estado constante; respuesta más gruesa que la de P511; posible duplicación con P511; interfaz del estudiante en `src/main.py`.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** duplicación de producto con P511 y de pregunta con P515, pendiente de decisión de curso.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P511; habilita la forma de reporte y la pregunta para P515.
- **Auditoría de Analytics:** no resuelta; lo nuevo es la organización ETL y el producto no cambia respecto de P511.

## S03.P514.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Transformation (p. 73: «Data Transformation pipeline») y SDM (p. 120: «Data lifecycle») — sin respaldo para el contraste ETL/ELT: el documento no lo trata; no aporta argumento a la auditoría pendiente.

## S03.P514.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 (merge/join, transform) (p. 5) — ya cubierta por P511 H01–H03; P514/P515 repiten la técnica (duplicación ya registrada por S02).

## S03.P514.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - transformaciones y uniones necesarias (p. 15 «CAP-P.3.5.1 Identify the transformations and merge/joins that may be necessary to solve an analytics problem») — ya cubierta: P511 H01–H03.

## S03.P514.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - esquema de eventos de error y dimensión de auditoría (pp. 23–24) — ya cubierta por P516 H02 (reglas con dimensión y conteo) y P514 H02 (reporte por etapa); como esquema dimensional del *back room* es fuera de alcance.

## S03.P514.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - rol «Data storage and access» (ETL, batch y streaming; p. 37) — fuera de alcance: el documento lo describe como un rol diferenciado cercano a ingeniería, lo que confirma el riesgo de identidad ya registrado. No justifica ampliar ETL/ELT.

## S03.P514.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - arquitectura del propio estudio «Medallion (bronze–silver–gold)» (p. 129) con «Capa Bronze: ingesta y preservación de datos crudos. Capa Silver: procesos de validación, normalización y verificación de calidad. Capa Gold: … indicadores» (p. 131); BI con «stack claro (ETL, SQL, herramientas de visualización)» (p. 290). Categoría: ya cubierta / fuera de alcance. Raw/curado y ETL/ELT ya existen (P513 H02, P514 H01, P515 H03, P525); su riesgo de identidad (S02) no se resuelve con evidencia de demanda, y añadir capas medallion sería arquitectura de plataforma.

## S03.P514.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.

## S03.P514.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.12

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Programa ejecutivo de 11 semanas sin código: sesgos en decisiones, análisis descriptivo, Big Data, experimentación, predictivo, prescriptivo y cuestiones ético-jurídicas. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.13

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo-técnico sobre historia de la web y la nube, contenedores, PKI, DevOps, serverless y cloud native, con casos (Microsoft, GE, Netflix, AWS). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.14

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-leadership.md` (`source_sha256`: 235857392770856bcd7abd1476039c10eae9928b8dadbb3243d1fb302364cb06).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo de 8 semanas sobre ecosistema de datos para líderes: IA, plataformas de datos, SQL y diseño de bases para líderes, nube, gobierno, ética y organización. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.15

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa en línea de 12 semanas: fundamentos de Python y estadística, aprendizaje no supervisado, regresión y predicción, clasificación y pruebas de hipótesis, aprendizaje profundo, sistemas de recomendación y modelos gráficos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.16

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-designing-and-building-ai-products-and-services.md` (`source_sha256`: 7f03ea5bc4d7561d0a019afb448d1229fb61642a39a8f385048c5381580ff57d).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - curso en línea de 8 semanas sobre el proceso de diseño de productos de IA (cuatro etapas, modelo de Lawler), fundamentos de ML y deep learning, HCI, «superminds» y *capstone* de propuesta de producto de IA. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P514.17

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-digital-platforms.md` (`source_sha256`: 7fc18c63d4b4afa1629c58320f509a5b9f7c442f9e6149231b755327952fc28b).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Curso ejecutivo sobre estrategia de plataformas digitales y mercados de dos lados: efectos de red, precios, arquitectura técnica, APIs y estándares, regulación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
