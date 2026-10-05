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

## S03.P505.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PDA (p. 112: «Write appropriate database queries») y DM-IR (p. 82) — ya cubierta: secuencia SQL sobre el corpus. La desambiguación de autores (DG-Data Cleaning, p. 73: «entity resolution») es marginal para P506: identidad por ID Scopus ya decidida en P503 H03.

## S03.P505.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P505.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - blueprint del examen CAP-E derivado del INFORMS Analytics Framework: siete dominios (pesos: Data 19 %) con subtareas de nivel inicial; el dominio III cubre necesidades y fuentes de datos, plan de gestión, adquisición, preparación, calidad, documentación y actualización del problema. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.
