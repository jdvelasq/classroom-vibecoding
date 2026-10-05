# Log — P515

## S01.P515.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se confirmó contraste ELT con P514 y se preservó la pregunta común.

## S02.P515.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P515_superstore_elt/` (`data/`, `professor/main.py`, `src/main.py`, `submission/`, `tests/test_activity.py`); P511, P512 y P514 para relaciones.
- **Trazabilidad revisada:** no existe entrada P515 en `implementation/data/traceability.yaml`; escalada.
- **Highlights:** añadidos H01 (transformación en el motor tras cargar raw), H02 (uniones SQL por claves contextuales homónimas sin validación de cardinalidad; caso y datos), H03 (capas raw y curada en un mismo artefacto).
- **Preservado:** pregunta común con P514, carga raw, CTAS en SQLite, reporte de filas y contraste ETL/ELT.
- **Corregido:** la descripción previa afirmaba trazabilidad `data.C01`–`data.C05`; la entrada no existe. Se precisa que la tabla curada selecciona sólo cuatro columnas de contexto.
- **Añadido:** ausencia de validación de cardinalidad en SQL; coincidencia con P514 salvo precisión flotante, no verificada por código; estado constante; capas raw dentro de la entrega; interfaz del estudiante en `src/main.py`.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** falta de entrada de trazabilidad; duplicación de pregunta y respuesta con P514.
- **Superficies / contrato / dependencias:** S01–S06 (S06 = trazabilidad ausente); recibe de P511, P512, P514; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** no resuelta; la contribución se reduce a un contraste técnico de Data Engineering.

## S03.P515.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Transformation (p. 73: «Data Transformation pipeline») y SDM (p. 120: «Data lifecycle») — sin respaldo para el contraste ETL/ELT: el documento no lo trata; no aporta argumento a la auditoría pendiente.

## S03.P515.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 (merge/join, transform) (p. 5) — ya cubierta por P511 H01–H03; P514/P515 repiten la técnica (duplicación ya registrada por S02).

## S03.P515.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P515.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P515.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - prohibición de unir dos tablas de hechos y *drill across*; claves foráneas nulas → fila por defecto (pp. 7, 20) — ya cubierta (P511 H02 valida cardinalidad) o marginal (no hay dos hechos en el curso); la falta de validación en P515 es un defecto ya registrado por S02, no una señal nueva de este documento.

## S03.P515.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - rol «Data storage and access» (ETL, batch y streaming; p. 37) — fuera de alcance: el documento lo describe como un rol diferenciado cercano a ingeniería, lo que confirma el riesgo de identidad ya registrado. No justifica ampliar ETL/ELT.

## S03.P515.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - arquitectura del propio estudio «Medallion (bronze–silver–gold)» (p. 129) con «Capa Bronze: ingesta y preservación de datos crudos. Capa Silver: procesos de validación, normalización y verificación de calidad. Capa Gold: … indicadores» (p. 131); BI con «stack claro (ETL, SQL, herramientas de visualización)» (p. 290). Categoría: ya cubierta / fuera de alcance. Raw/curado y ETL/ELT ya existen (P513 H02, P514 H01, P515 H03, P525); su riesgo de identidad (S02) no se resuelve con evidencia de demanda, y añadir capas medallion sería arquitectura de plataforma.

## S03.P515.08

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - proyecto nacional de bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas y cronograma de cohortes 2024–2026. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P515.09

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - programa ejecutivo en línea de dos meses sobre IA para líderes de negocio: fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, organización y futuro de la IA, con proyecto final de plan de negocio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
