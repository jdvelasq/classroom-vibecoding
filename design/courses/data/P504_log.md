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
