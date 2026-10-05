# Log — P424

## S02.P424.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P424_model_rollback/` (`REGISTRY.json`, `MODEL_V1.pkl` y `MODEL_V2.pkl` (sólo tamaño), `HOW_TO_RUN_ME.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/production/`, `tests/test_activity.py`); digests de P406, P421, P423, P448.
- **Trazabilidad revisada:** P424 → `productos.C02`, `C03`, `C05`; C03 sin evidencia.
- **Highlights:** añadidos H01 (reversión por copia verificada por bytes), H02 (registro de reversión auditable) y H03 (versiones indistinguibles y sin motivo; caso y datos como límite).
- **Ambigüedades:** `REGISTRY.json` no se actualiza tras la reversión; v1 y v2 tienen igual tamaño y origen no declarado; no se registra motivo; esquema de registro distinto al de P421; la alerta de P423 no se usa.
- **Superficies / contrato / dependencias:** S01–S05; recibe prácticas de P421; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; recuperación genérica sin capacidad analítica identificable.

## S03.P424.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - ML-General (p. 97: «Explain how to efficiently transition a model into production») — ya cubierta: seguimiento, registro, monitoreo y reversión.

## S03.P424.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 7.2 «Recalibrate and maintain the analytics solution» (p. 7) — marginal: reversión sin reentrenar (P424 H01) y corridas recuperables (P420 H02) cubren la mecánica; el recalibrado es un método predictivo, fuera de la frontera del curso.

## S03.P424.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Recalibrate and maintain the analytics solution» (p. 24, Tarea 7.2) — sin señal: ambas subtareas «Not tested at this level»; promoción y reversión ya en P421 y P424.
