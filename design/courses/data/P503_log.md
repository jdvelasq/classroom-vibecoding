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
