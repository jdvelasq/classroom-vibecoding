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
