# Log — P505

## S01.P505.01

- **Fecha:** 2026-10-03
- **Curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Inspeccionado:** datos, notebooks, `submission/`, pruebas y trazabilidad.
- **Decisión:** mapa inicial creado; queda pendiente granularidad de notebook.
- **Trazabilidad:** `data.C01`, `data.C02`, `data.C05` revisadas.

## S02.P505.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P505_scopus_sql_intermedio/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` completo, `tests/test_activity.py`); contraste con `implementation/data/P503_scopus_relacional/submission/authors_by_documents.csv` y `sources_by_documents.csv` y sus vistas.
- **Trazabilidad revisada:** P505 → `data.C01`, `data.C02`, `data.C05`; C01 débil.
- **Preservado:** dos preguntas, entregables, reutilización de la base de P503.
- **Corregido:** la descripción previa afirmaba que P505 «añade dos perspectivas de concentración»; ambas ya estaban persistidas en P503 con el mismo contenido visible y tamaño de archivo. Pruebas: sólo existencia.
- **Highlights añadidos:** H01 (unión por tabla puente), H02 (conteo completo por coautoría; highlight obligatorio de caso y datos). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** duplicación de producto con P503 (decisión de curso pendiente); interpretación del conteo completo no declarada; empates en `LIMIT 20`.
- **Superficies / contrato / dependencias:** S01–S06 (S04 registra la duplicación); recibe de P503–P504; habilita P506 y P508.
- **Auditoría de Analytics:** sin producto nuevo; riesgo alto de lectura como lección de SQL intermedio.
