# Log — P508

## S01.P508.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`.
- **Estado:** inicial. Se inspeccionaron datos, notebooks, entregables, pruebas
  y trazabilidad.
- **Decisión:** se creó el mapa y se registró como límite no inferir el uso de
  SQLAlchemy sin inspección granular del notebook.

## S02.P508.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P508_scopus_sqlalchemy/` (`data/`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` completo, `tests/test_activity.py`); contraste con `implementation/data/P505_scopus_sql_intermedio/submission/sources_by_documents.csv` y con el manifiesto de P501.
- **Trazabilidad revisada:** P508 → `data.C01`, `data.C02`, `data.C04`, `data.C05`; C01 y C04 débiles.
- **Preservado:** pregunta, entregables CSV y base de entrega, transición de consulta a artefacto de consumo.
- **Corregido:** la descripción previa dejaba sin confirmar el uso de SQLAlchemy; el notebook usa `create_engine`, `text()`, parámetros nombrados, conexiones con `with` y `dispose()`. Pruebas: sólo existencia.
- **Highlights añadidos:** H01 (engine), H02 (parámetro de periodo; highlight obligatorio de caso y datos), H03 (extracto verificado por reconsulta). IDs nuevos.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** consumidor «otra aplicación» no identificado; portabilidad del engine declarada, no demostrada; pregunta solapada con P505 y patrón de base de entrega solapado con P501.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P503–P505; no habilita una actividad posterior de forma demostrable.
- **Auditoría de Analytics:** riesgo alto de lectura como entrenamiento en herramienta (SQLAlchemy).

## S03.P508.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CCF-The Web (p. 67: «Awareness of web application vulnerabilities and security attacks (e.g., SQL injection…)») — marginal: H02 ya usa parámetros nombrados (`:first_year`, `params=`); como mucho, una aclaración verbal.

## S03.P508.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - definición del marco INFORMS en siete dominios con sus tareas (sin subtareas); el dominio III describe identificar datos requeridos y disponibles, hacerlos utilizables (limpiar, armonizar, transformar, unir, validar, evaluar calidad), privacidad y seguridad, gobierno, inventario y documentación para procesos repetibles. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P500_log.md`.

## S03.P508.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.4.4.1 características del *stack* (bases, nube, *open source*) (p. 18) — ya cubierta por la frontera de herramientas (P500 H03, P508 H01); profundizar sería identidad de herramienta.
