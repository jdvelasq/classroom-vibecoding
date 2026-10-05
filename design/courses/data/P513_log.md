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
