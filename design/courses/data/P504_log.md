# Log — P504

## S01.P504.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`
- **Estado:** inicial
- **Inspeccionado:** `data/`, notebooks, `submission/`, pruebas y
  `traceability.yaml`.
- **Decisión:** se creó el mapa inicial y se dejó pendiente documentar la
  secuencia de consultas visible en notebooks.
- **Trazabilidad:** `data.C02` y `data.C05` revisadas.

## S02.P504.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P504_scopus_sql_basico/` (`data/scopus_proptech.db` —binario, tamaño—, `data/search_string.txt`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` completo, `tests/test_activity.py`).
- **Trazabilidad revisada:** P504 → `data.C02`, `data.C05`; con evidencia. H03 evidencia también `data.C03`, no mapeada.
- **Preservado:** dos preguntas, entregables, reutilización de base y búsqueda de P503.
- **Completado / corregido:** se documentó la secuencia de consultas pendiente (esquema, muestra, filtro, agrupación). Se corrigió que las pruebas «hacen observable el resultado»: sólo comprueban existencia. Notebook del estudiante sin celdas.
- **Highlights añadidos:** H01 (inspección del esquema), H02 (filtro de periodo al grano documento), H03 (heterogeneidad documental; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** registros de 2026 sin fecha de export; la composición por tipo no se usa en conteos posteriores; nombre «sql_basico» sigue la lógica de un temario de SQL.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P503; el filtro 2020 reaparece en P506–P508.
- **Auditoría de Analytics:** delimitación descriptiva del corpus; riesgo moderado de lectura como introducción a SQL.

## S03.P504.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PDA (p. 112: «Write appropriate database queries») y DM-IR (p. 82) — ya cubierta: secuencia SQL sobre el corpus. La desambiguación de autores (DG-Data Cleaning, p. 73: «entity resolution») es marginal para P506: identidad por ID Scopus ya decidida en P503 H03.

## S03.P504.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P504.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P504.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P504.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P504.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - considerar si los datos disponibles son apropiados para la pregunta (p. 39) y los datos observacionales como «found artifacts» no aleatorios (p. 44), aplicados a la pertinencia del corpus Scopus — ya cubierta en lo esencial (P503 H01 consulta preservada, P504 H03 heterogeneidad documental, P507 H02 palabras clave que condicionan el ranking). Ampliar a la evaluación estadística de selección es fuera de alcance (Estadística o Descriptiva).

## S03.P504.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SQL como segunda tecnología más pedida (p. 79: «Python (12,12 %), SQL (11,11 %) y AWS (10,75 %)»); «SQL avanzado» en el dominio «Data & features» (p. 96) y entre las habilidades emergentes (p. 231: «SQL avanzado (1.296)»); certificación «SQL / Bases de datos» 5,11 % (p. 79). Categoría: ya cubierta. Confirma pertinencia laboral de la secuencia SQL (esquema P503, filtros P504, `JOIN` P505, CTE P506, ventanas P507, parametrización P508, volcado y agregación P510). No aporta argumento para ampliarla; tampoco resuelve el riesgo de leer P504–P507 como progresión de un curso de SQL (auditoría S02), que es de identidad y no de demanda.
  - «optimización de queries, índices, … transacciones ACID, sharding, replicación ni estrategias de respaldo y recuperación» (p. 175); líder de BD con «clusters, replicación, alta disponibilidad, múltiples motores» (p. 286). Categoría: fuera de alcance. Administración de bases de datos e ingeniería; no sirven a requisitos, calidad o documentación de datos para una pregunta.

## S03.P504.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P504.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P504.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.
