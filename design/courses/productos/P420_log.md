# Log — P420

## S02.P420.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P420_experiment_tracking/` (`HOW_TO_RUN_ME.txt`, `requirements.txt`, `data/winequality-red.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/experiments/` con dos corridas e `index.json`, `tests/test_activity.py`); digests de P403, P406, P419, P421, P422, P424.
- **Trazabilidad revisada:** P420 → `productos.C02`, `C03`, `C05`; C03 débil.
- **Highlights:** añadidos H01 (partición fija), H02 (corrida recuperable), H03 (índice comparativo) y H04 (objetivo ordinal tratado como clases y KNN sin escalado; caso y datos).
- **Ambigüedades:** procedencia del dataset no documentada en la actividad. `config.json` omite hiperparámetros. Los modelos de P420 no son consumidos por P421/P424, que usan pickles de origen no declarado. Pruebas de estudiante sólo verifican `index.json`.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P419 y P406 (prácticas); habilita P422 sólo por dominio compartido, sin artefacto.
- **Auditoría de Analytics:** parcialmente resuelta; capacidad de trazabilidad de modelos sin usuario ni decisión.

## S03.P420.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ML-General (p. 97: «Explain how to efficiently transition a model into production») — ya cubierta: seguimiento, registro, monitoreo y reversión.

## S03.P420.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 7.2 «Recalibrate and maintain the analytics solution» (p. 7) — marginal: reversión sin reentrenar (P424 H01) y corridas recuperables (P420 H02) cubren la mecánica; el recalibrado es un método predictivo, fuera de la frontera del curso.

## S03.P420.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Blueprint del examen de entrada CAP-E derivado del INFORMS Analytics Framework: siete dominios con tareas y subtareas evaluables (p. 6: Deployment 9 %, Lifecycle Management 8 %); varias subtareas de despliegue y mantenimiento figuran como «Not tested at this level». Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
