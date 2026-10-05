# Log — P107

## S02.P107.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P107_limpieza_sql/` (`data/ventas.csv`, `professor/main.py`, `src/main.py`, `submission/ventas.csv`, `temp/ventas.db`, `tests/test_activity.py`). Comparado con P106 y P104.
- **Trazabilidad revisada:** entrada P107 → `descriptiva.C02`, `descriptiva.C05`.
- **Highlights añadidos:** H01 (ingesta como texto con faltantes explícitos; highlight de caso y datos), H02 (limpieza como `CREATE TABLE AS SELECT` sobre UDF), H03 (canonización por clave en minúsculas), H04 (contrato compartido con P106).
- **Ambigüedades:** la limpieza está en Python y SQL sólo la orquesta; `country` es la constante `'COL'`, por lo que la aserción de país se cumple por construcción; no hay `tests/conftest.py` (presente en P100–P106); producto duplicado con P106 con tipos distintos no detectados por la prueba.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P106 y P104; habilita la práctica `create_function` de P109.
- **Auditoría de Analytics:** producto = capacidad de datos idéntica a P106; contribución de bases de datos. Mapeo C02 (calidad) sustentado, C05 débil.

## S03.P107.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - dimensiones de calidad de datos, entity resolution, limpieza basada en reglas y dependencias funcionales (DG-Data Cleaning, pp. 73–74) — ya cubierta: P106 H01–H05 (función por defecto, canonización con diagnóstico de colisiones, invariantes de dominio) y P107 H01–H03. Nombrar las dimensiones de calidad o formalizar FD/CFD sería marginal (vocabulario, no capacidad nueva).
  - transformación (estandarización, normalización, codificación, unidades; DG-Data Transformation, p. 73) — ya cubierta: P106 H04 lleva magnitudes a una unidad común.

## S03.P107.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» (p. 5) — ya cubierta: P106 H01–H05, P107 H01–H04, P150 H02.

## S03.P107.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E: siete dominios del INFORMS Analytics Framework con sus tareas y subtareas evaluables y pesos (framing de negocio 16 %, framing analítico 16 %, datos 19 %, metodología 16 %, desarrollo 16 %, despliegue 9 %, ciclo de vida 8 %). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P107.04

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - limpiar, armonizar, transformar, unir y validar (p. 15: Task 3.5) — ya cubierta: P106 H01–H04, P107 H01–H03, P150 H02 (`validate="many_to_one"`), P121 H02 (conciliación).

## S03.P107.05

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Data preparation, especially data cleansing and data transformation», «Missing and conflicting data» (p. 45) — ya cubierta (P106 H01–H05; P107 H01).

## S03.P107.06

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «SQL avanzado», «Integración de fuentes», «Python aplicado», «Excel avanzado» en el dominio «Data & features» (p. 96); SQL 11,11 % de requerimiento (p. 79) — ya cubierta: SQL con vistas, ventanas y CTE (P104 H02–H04), UDF y capa cruda/limpia (P107 H02), consultas en estrella (P151 H04); integración de fuentes en P150 H01–H02.
  - procesamiento en capas Bronze/Silver/Gold con «validación, normalización y verificación de calidad» (p. 131); reglas de limpieza «tiempos mínimos, duplicados», «control de completitud» (p. 238) — ya cubierta: separación crudo/limpio (P107 H02), limpieza por columna e invariantes (P106 H01, H05).

## S03.P107.07

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-talento-tech-2024-2026.md` (`source_sha256`: 333d1b4607a362a98c821c8d2a1f47246cddab2330c6e0d48d762b23b2f050e4).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de proyecto de inversión pública: bootcamps de 159 horas en habilidades digitales (programación, IA, análisis de datos, blockchain, nube, ciberseguridad) con meta de 94.696 personas formadas en 2024–2026, distribución regional, cronograma de cohortes y focalización poblacional. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P107.08

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto comercial de un programa ejecutivo en línea de dos meses sobre IA para negocios: ocho módulos (fundamentos de ML, redes neuronales, visión y PLN, robótica, estrategia, equipos, futuro de la IA) y un proyecto final de plan de negocio; dirigido a líderes y gerentes. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P107.09

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c101-data-engineering.md` (`source_sha256`: b64f52095176ee5a0f8d29e8b325f57bf095c51caef4a36305f009d193fa1623).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ciclo «from data preparation to exploration, visualization and analysis» (p. 1) — ya cubierta: preparación y calidad (P106 H01–H05, P107 H01–H02), exploración y visualización al servicio de un diagnóstico (P120 H02–H05, P121 H02–H04, P122 H01–H05). La ficha no da detalle que permita contrastar más.

## S03.P107.10

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/berkeley-data-c102-data-inference-and-decisions.md` (`source_sha256`: 2f5c3a7016507b31af6506ae03143ec5ead25c5130bbbfaf5c285bf9f4e6e345).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Ficha de catálogo de un curso de pregrado en Data Science (antes Statistics 102). Cubre fundamentos probabilísticos de la inferencia y el ciclo de modelado y decisión, con sus implicaciones humanas, sociales y éticas. Sólo lista temas: no tiene resultados de aprendizaje, casos ni evaluación. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.

## S03.P107.11

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/cambridge-business-analytics.md` (`source_sha256`: b401576ede0eec3a72a79e913adb4e63676fb30b9f4c59056a575672372d46b0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Limpieza de datos» (p. 7) — ya cubierta: P106 H01–H05, P107 H01–H03.

## S03.P107.12

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-cloud-and-devops.md` (`source_sha256`: 7d00048d4be79c14cf76a35a041d0bc0885881653cfb874bbea898ecf0107192).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto de un curso en línea sobre computación en la nube y DevOps: historia de la web, Node.js, contenedores y PKI, DevOps y sus métricas, casos de migración a la nube, *serverless*, corporación ágil y *cloud native*. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
