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
