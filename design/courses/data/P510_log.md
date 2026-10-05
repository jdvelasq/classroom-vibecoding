# Log — P510

## S01.P510.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`.
- **Estado:** inicial. Se inspeccionaron volcado SQL, notebooks, entrega,
  pruebas y trazabilidad.
- **Decisión:** se creó el mapa y se registró la ausencia de contenido del
  notebook de estudiante y de manifiesto de procedencia.

## S02.P510.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P510_datacamp_valoraciones/` (`data/datacamp_application.sql`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/course_ratings.csv`, `tests/test_activity.py`); P503–P508 para relaciones.
- **Trazabilidad revisada:** P510 → `data.C01`–`data.C05`; C03 parcial y C04 débil.
- **Highlights:** añadidos H01 (volcado SQL adaptado a SQLite; caso y datos), H02 (`LEFT JOIN` y cambio de grano), H03 (conciliación agregado–fuente). No existían IDs previos.
- **Preservado:** pregunta, dos granos, `LEFT JOIN`, conciliación previa a persistir, ausencia de manifiesto y notebook de estudiante vacío.
- **Corregido:** la descripción previa hablaba de conciliar la «suma de calificaciones»; el código compara el número de calificaciones (`rating_count.sum()` contra `COUNT(*)` de `rating`).
- **Añadido:** origen TablePlus y reescritura de `"public".`; imputación de promedio 0 por `COALESCE`; resumen por lenguaje no persistido; prueba de sólo existencia; ausencia de `questions.json`.
- **Sección heredada:** se eliminó «Mejoras aceptadas pendientes de implementación» porque declaraba que no había mejoras.
- **Ambigüedades:** procedencia, fecha y escala de `rating` no documentadas; no visible si hay cursos sin calificaciones.
- **Superficies / contrato / dependencias:** S01–S06; recibe práctica de P503–P507; no habilita actividades posteriores de forma evidenciada.
- **Auditoría de Analytics:** producto tabular para una decisión declarada de priorización; SQL contribuyente. Riesgo moderado de lectura como ejercicio de SQL por falta de regla de priorización.
