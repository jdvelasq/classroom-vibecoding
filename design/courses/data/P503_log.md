# Log — P503

## S01.P503.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`
- **Estado:** inicial
- **Inspeccionado:** `data/`, notebooks, `submission/`, pruebas y
  `traceability.yaml`.
- **Decisión:** se creó un mapa conservador, distinguiendo preguntas y
  entregables explícitos de la secuencia de notebook aún por detallar.
- **Trazabilidad:** `data.C01`–`data.C05` revisadas.
- **Pendiente:** lectura granular de celdas de notebook para completar la
  experiencia guiada.

## S02.P503.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P503_scopus_relacional/` (`data/scopus.csv.gz` —binario—, `data/search_string.txt`, `professor/notebook.ipynb` celda a celda, `notebooks/notebook.ipynb`, `submission/` completo, `tests/test_activity.py`); tamaños de `data/scopus_proptech.db` en P504–P508.
- **Trazabilidad revisada:** P503 → `data.C01`–`data.C05`; todas con evidencia.
- **Preservado:** tres preguntas, base `scopus_proptech.db`, tres respuestas agregadas, papel de puente hacia P504–P508 (ahora sustentado por tamaño de archivo idéntico).
- **Completado / corregido:** se realizó la lectura granular pendiente del notebook: normalización multivalor, decisiones de identidad y faltantes, DDL con integridad referencial y vistas. Se registró que el notebook del estudiante no tiene celdas y que las pruebas sólo comprueban existencia.
- **Highlights añadidos:** H01 (procedencia de la consulta), H02 (multivalor a muchos a muchos; highlight obligatorio de caso y datos), H03 (identidad y faltantes), H04 (integridad referencial), H05 (vistas como respuesta). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** sin fecha de export ni condiciones de uso de Scopus; `documents_by_year.csv` empieza en 1969, lo que sugiere documentos poco pertinentes que no se examinan; corte `LIMIT 20` con empates; tabla `keywords` sin uso en P503 (la usa P507).
- **Superficies / contrato / dependencias:** S01–S07; habilita P504–P508.
- **Auditoría de Analytics:** representación consultable del corpus al servicio de preguntas descriptivas; riesgo moderado de lectura como taller de bases de datos.

## S03.P503.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DI-Logical integrity (p. 90: «Entity integrity, referential integrity, domain integrity, user-defined integrity») — ya cubierta por H04 (PK, FK, `NOT NULL`, `UNIQUE`, `PRAGMA foreign_keys`). DM-Information Retrieval (p. 82: «The concept of a search strategy; the related role of narrowing and broadening»; «Create and use a relational database structure using SQL») — ya cubierta por H01 (consulta preservada) y H02–H05; el vacío de pertinencia del corpus (desde 1969) no se apoya en este documento, que trata la recuperación por eficiencia y no la validación de un corpus. DPSIA/DI-Security threats (p. 91: «Data provenance assurance») — marginal: el export sin fecha ni condiciones (S01) es un defecto de manifiesto ya registrado, no un cambio de aprendizaje.

## S03.P503.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P503.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.6 «Identify characteristics of a normalized dataset» (p. 14) — ya cubierta por P503 H02–H04.
  - CAP-E.3.4.3 «lineage, traceability, and version control of data» (p. 15) — ya cubierta por P502 H03 y P503 H01; versionado de datos como práctica es marginal.

## S03.P503.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - derivar necesidades de datos de la pregunta (p. 13 «CAP-P.3.1.1 Identify an appropriate sequencing and prioritization of data needed, including sources»; p. 10 «CAP-P.2.2.1 Identify why analytics element(s) would be classified as an input, output, both, or neither») — ya cubierta: P500 H02, P503 (entidades desde la pregunta), P506 H02, P517 H02 (contrato mínimo derivado de la pregunta).
  - características de una base relacional (p. 14 «CAP-P.3.2.6 Identify basic characteristics of a relational database») — ya cubierta: P503 H02–H04.
  - sesgo de la fuente (p. 15 «CAP-P.3.4.1 Identify the techniques appropriate in acquiring the data and identify data source bias») — marginal: la pertinencia del corpus recuperado y la presencia de términos de búsqueda en el ranking ya están escaladas en S02 (P503 auditoría; P507 S01); el documento no aporta caso ni método concreto para enseñarlo.

## S03.P503.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - dimensiones multivaluadas y tablas puente (p. 21) — ya cubierta por P503 H02 (relaciones muchos a muchos normalizadas).

## S03.P503.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - considerar si los datos disponibles son apropiados para la pregunta (p. 39) y los datos observacionales como «found artifacts» no aleatorios (p. 44), aplicados a la pertinencia del corpus Scopus — ya cubierta en lo esencial (P503 H01 consulta preservada, P504 H03 heterogeneidad documental, P507 H02 palabras clave que condicionan el ranking). Ampliar a la evaluación estadística de selección es fuera de alcance (Estadística o Descriptiva).

## S03.P503.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SQL como segunda tecnología más pedida (p. 79: «Python (12,12 %), SQL (11,11 %) y AWS (10,75 %)»); «SQL avanzado» en el dominio «Data & features» (p. 96) y entre las habilidades emergentes (p. 231: «SQL avanzado (1.296)»); certificación «SQL / Bases de datos» 5,11 % (p. 79). Categoría: ya cubierta. Confirma pertinencia laboral de la secuencia SQL (esquema P503, filtros P504, `JOIN` P505, CTE P506, ventanas P507, parametrización P508, volcado y agregación P510). No aporta argumento para ampliarla; tampoco resuelve el riesgo de leer P504–P507 como progresión de un curso de SQL (auditoría S02), que es de identidad y no de demanda.
  - «muchos candidatos presentan consultas SQL básicas, pero carecen de la comprensión de modelado de datos avanzado, … normalización vs. desnormalización» (p. 175); «construir modelos lógicos de datos» como pilar crítico para Data Analyst (p. 252). Categoría: ya cubierta. Normalización de multivalor con PK/FK (P503 H02, H04), tabla plana integrada (P511 H01–H03) y hecho–dimensiones que contrasta con la tabla plana (P512 H02) ya ejercen el contraste.
  - «optimización de queries, índices, … transacciones ACID, sharding, replicación ni estrategias de respaldo y recuperación» (p. 175); líder de BD con «clusters, replicación, alta disponibilidad, múltiples motores» (p. 286). Categoría: fuera de alcance. Administración de bases de datos e ingeniería; no sirven a requisitos, calidad o documentación de datos para una pregunta.
  - el estudio homologa títulos y habilidades en «Dominio Canónico» (pp. 80–82, 96; glosario p. 346: «Forma de agrupar muchas habilidades similares en categorías generales»), incluso con mapeos discutibles («Analista Blockchain → Analista de Datos», p. 82). Categoría: marginal. Es una práctica del procesamiento del estudio, no una señal curricular; la falta de unificación de variantes de palabras clave en P503 S02 / P507 S01 ya está registrada por S02 y requiere una fuente que la justifique como contenido, no una ilustración de una agencia.
  - «muestra voluntaria (no probabilística)» como limitación declarada (p. 238). Categoría: marginal. La falta de criterio de muestra (P526 S01) y de pertinencia del corpus (auditoría P503) ya está registrada por S02; aquí sólo se recoge dentro de la candidata de P526.

## S03.P503.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P503.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P503.10

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «the entire life cycle of data management and science, ranging from data preparation to exploration, visualization and analysis, to machine learning and collaboration» (p. 1). Categoría: ya cubierta / fuera de alcance. La preparación (lectura con formato declarado, integración validada, estructuración, calidad, contratos, linaje) ya se ejerce en P500–P517; exploración, visualización, análisis y ML pertenecen a los otros cursos de la línea.

## S03.P503.11

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado de inferencia y decisión en ciencia de datos (frecuentista/bayesiana, diseño experimental, causalidad, bandits, control, privacidad diferencial, ML), con prerrequisitos de probabilidad y Data C100. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
