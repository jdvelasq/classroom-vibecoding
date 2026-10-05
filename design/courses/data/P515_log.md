# Log — P515

## S01.P515.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se confirmó contraste ELT con P514 y se preservó la pregunta común.

## S02.P515.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P515_superstore_elt/` (`data/`, `professor/main.py`, `src/main.py`, `submission/`, `tests/test_activity.py`); P511, P512 y P514 para relaciones.
- **Trazabilidad revisada:** no existe entrada P515 en `implementation/data/traceability.yaml`; escalada.
- **Highlights:** añadidos H01 (transformación en el motor tras cargar raw), H02 (uniones SQL por claves contextuales homónimas sin validación de cardinalidad; caso y datos), H03 (capas raw y curada en un mismo artefacto).
- **Preservado:** pregunta común con P514, carga raw, CTAS en SQLite, reporte de filas y contraste ETL/ELT.
- **Corregido:** la descripción previa afirmaba trazabilidad `data.C01`–`data.C05`; la entrada no existe. Se precisa que la tabla curada selecciona sólo cuatro columnas de contexto.
- **Añadido:** ausencia de validación de cardinalidad en SQL; coincidencia con P514 salvo precisión flotante, no verificada por código; estado constante; capas raw dentro de la entrega; interfaz del estudiante en `src/main.py`.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** falta de entrada de trazabilidad; duplicación de pregunta y respuesta con P514.
- **Superficies / contrato / dependencias:** S01–S06 (S06 = trazabilidad ausente); recibe de P511, P512, P514; no habilita dependencias evidenciadas.
- **Auditoría de Analytics:** no resuelta; la contribución se reduce a un contraste técnico de Data Engineering.

## S03.P515.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Transformation (p. 73: «Data Transformation pipeline») y SDM (p. 120: «Data lifecycle») — sin respaldo para el contraste ETL/ELT: el documento no lo trata; no aporta argumento a la auditoría pendiente.
