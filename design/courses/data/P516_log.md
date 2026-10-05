# Log — P516

## S01.P516.01

- **Fecha:** 2026-10-03; **curso / executor:** `data` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se registró el alcance de `zipcode=0` como límite crítico.

## S02.P516.02

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** incremental.
- **Rutas inspeccionadas:** `implementation/data/P516_vermont_calidad/` (`data/vermont.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/quality_report.csv`, `tests/test_activity.py`); P500, P510, P511 para relaciones; P517 para dependencia.
- **Trazabilidad revisada:** P516 → `data.C01`, `data.C03`, `data.C04`; coherente.
- **Highlights:** añadidos H01 (granos mezclados por total estatal; caso y datos), H02 (calidad como reglas con dimensión y conteo), H03 (clave compuesta y dominio como unidad de análisis).
- **Preservado:** pregunta, cinco reglas, clave (`zipcode`, `agi_stub`), `zipcode = 0` como riesgo de alcance.
- **Corregido:** la descripción previa hablaba de «perfilado»; el notebook evalúa reglas sobre 5 de 147 columnas, no perfila el extracto.
- **Añadido:** 1476 × 147; ausencia de procedencia, año y diccionario; defecto de estado (sólo la regla de alcance puede no ser `PASS`); diagnóstico sin conjunto filtrado; prueba de sólo existencia.
- **Sección heredada:** eliminada «Mejoras aceptadas pendientes de implementación» (declaraba que no había).
- **Ambigüedades:** la interpretación de `zipcode = 0` se apoya sólo en un comentario.
- **Superficies / contrato / dependencias:** S01–S05; habilita datos y reglas para P517.
- **Auditoría de Analytics:** diagnóstico de aptitud para una pregunta; sin riesgo de identidad relevante.

## S03.P516.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DG-Data Cleaning (pp. 73–74: «The dimensions of data quality»; «Various forms for data quality rules such as functional dependencies (FD)…»; «suitable for its intended use») — ya cubierta: reglas nombradas por dimensión (H02), clave compuesta y dominio (H03), aptitud para la pregunta (H01). La falta de diccionario y procedencia (S01) es marginal desde este documento (CCF p. 66: «Files: data, metadata» es genérico).
