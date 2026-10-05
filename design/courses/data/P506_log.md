# Log — P506

## S01.P506.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`.
- **Estado:** inicial; se inspeccionaron datos, notebooks, entregables, pruebas
  y `traceability.yaml`.
- **Decisión:** se creó descripción conservadora y se registró como límite la
  falta de extracción granular de la consulta.
- **Trazabilidad:** `data.C01`–`data.C03`, `data.C05` revisadas.

## S02.P506.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P506_scopus_sql_avanzado/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` completo, `tests/test_activity.py`); contraste con `implementation/data/P505_scopus_sql_intermedio/submission/authors_by_documents.csv`.
- **Trazabilidad revisada:** P506 → `data.C01`, `data.C02`, `data.C03`, `data.C05`; C03 sin evidencia explícita.
- **Preservado:** pregunta, entregable, condición temporal de continuidad y relación con P504–P505.
- **Completado:** se extrajo la consulta (dos CTE, `COUNT(DISTINCT publication_year)`, umbral `>= 3`) pendiente en la pasada previa; pruebas sólo de existencia; notebook del estudiante sin celdas.
- **Highlights añadidos:** H01 (CTE encadenadas), H02 (continuidad como años activos; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** umbral de 3 años y corte 2020 sin justificación; 2026 posiblemente incompleto; `data.C03` mapeada sin evidencia.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P503–P505; habilita P507 (CTE y periodo).
- **Auditoría de Analytics:** operacionalización con propósito analítico; riesgo moderado por encuadre de temario SQL.

## S03.P506.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PDA (p. 112: «Write appropriate database queries») y DM-IR (p. 82) — ya cubierta: secuencia SQL sobre el corpus. La desambiguación de autores (DG-Data Cleaning, p. 73: «entity resolution») es marginal para P506: identidad por ID Scopus ya decidida en P503 H03.
