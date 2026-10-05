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
