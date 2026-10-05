# Log — P513

## S01.P513.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se creó mapa y se escaló la ausencia de pregunta analítica explícita.

## S02.P513.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P513_superstore_batch/` (`data/*.csv`, `data/source_manifest.json`, `professor/main.py`, `src/main.py`, `submission/ingestion_report.csv`, `tests/test_activity.py`); P500–P502 para relaciones; P518 y P524 para reaparición de Parquet.
- **Trazabilidad revisada:** P513 → `data.C02`–`data.C05`; sin C01, coherente con la ausencia de pregunta.
- **Highlights:** añadidos H01 (lectura de lotes con BOM y formato declarado; caso y datos), H02 (descubrimiento por patrón y aterrizaje Parquet), H03 (reporte de ingestión por lote).
- **Preservado:** ausencia de pregunta analítica, dos lotes trimestrales, Parquet en zona raw, reporte por lote y la escalación de identidad.
- **Corregido:** «lectura con contrato de formato» es parcialmente incorrecta: `decimal=","` no coincide con el punto decimal de los lotes y deja las columnas numéricas como texto (comprobado con `pandas.read_csv`).
- **Añadido:** suma 1012 + 940 = 1952 no verificada; `utf-8-sig` frente al arreglo `latin1` de P500; estado `SUCCESS` constante; Parquet no persistido; interfaz del estudiante en `src/main.py` sin enunciado.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** el bloque `format` del manifiesto no se ve completo; no se puede confirmar qué separador decimal declara.
- **Superficies / contrato / dependencias:** S01–S05; recibe caso de P500; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** no resuelta; la actividad se lee como ingestión batch de ingeniería de datos sin producto analítico.

## S03.P513.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P513.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «ensuring proper data transport across systems» (p. 5) — fuera de alcance/marginal: transporte entre sistemas es práctica de ingeniería; P513 y P518 ya tienen la auditoría de identidad no resuelta.

## S03.P513.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - CAP-E.3.2.4/3.2.5 fortalezas y elección de arquitectura de datos (p. 14) — fuera de alcance (arquitectura excluida).

## S03.P513.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-Pro derivado del INFORMS Analytics Framework: siete dominios del ciclo de vida analítico con pesos (Data 19 %) y subtareas evaluables a nivel de profesional medio. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P513.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo «oficial» de técnicas de modelado dimensional (Toolkit, 3.ª ed.): proceso de cuatro pasos, grano, hechos y dimensiones, aditividad, claves, dimensiones degeneradas, SCD, jerarquías, tablas puente, hechos tardíos y esquemas especiales. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P513.06

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` (`source_sha256`: 4fff2348bb62166f370f38d964157c160c2a88abebcfae2177b81133d779825c).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - rol «Data storage and access» (ETL, batch y streaming; p. 37) — fuera de alcance: el documento lo describe como un rol diferenciado cercano a ingeniería, lo que confirma el riesgo de identidad ya registrado. No justifica ampliar ETL/ELT.

## S03.P513.07

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` (`source_sha256`: 2c827d965818257f0506a7d1c8bc9b13599a1fc0b7fe0943340f7b4dc85123c7).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - arquitectura del propio estudio «Medallion (bronze–silver–gold)» (p. 129) con «Capa Bronze: ingesta y preservación de datos crudos. Capa Silver: procesos de validación, normalización y verificación de calidad. Capa Gold: … indicadores» (p. 131); BI con «stack claro (ETL, SQL, herramientas de visualización)» (p. 290). Categoría: ya cubierta / fuera de alcance. Raw/curado y ETL/ELT ya existen (P513 H02, P514 H01, P515 H03, P525); su riesgo de identidad (S02) no se resuelve con evidencia de demanda, y añadir capas medallion sería arquitectura de plataforma.
