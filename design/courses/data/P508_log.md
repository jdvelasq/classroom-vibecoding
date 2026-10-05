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
