# Log — P417

## S02.P417.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P417_pipeline_integration_test/` (`data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/factory_totals.json`, `tests/test_activity.py`, `requirements.txt`); digests de P400, P401, P413, P414.
- **Trazabilidad revisada:** P417 → `productos.C02`, `productos.C05`; C05 sin evidencia.
- **Highlights:** añadidos H01 (prueba sobre el artefacto publicado) y H02 (caso trivial como límite de la integración; caso y datos).
- **Ambigüedades:** el «pipeline» es una función de tres pasos; no hay componentes cuya integración pueda fallar. Posible duplicación con `tests/test_report.py` de P413–P414. La prueba del profesor escribe en `submission/` real. Sin `HOW_TO_RUN_ME.txt` ni instrucciones para la plantilla.
- **Superficies / contrato / dependencias:** S01–S04; recibe de P400/P412–P414; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; prueba de software genérica.

## S03.P417.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - SDM-Software Testing (pp. 121–122: unit, integration, «Regression/Continuous», system, security; «Use or extract representative data … to test algorithms on a small scale») — ya cubierta: unitarias (P400–P401), datos (P402), modelo (P403), regresión del resultado conocido (P412 H03), integración del flujo (P417 H01).

## S03.P417.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 6.6 «Actively support deployment validation and verification, including production data flows» (p. 7) — ya cubierta: verificación del artefacto publicado de extremo a extremo (P417 H01) y conciliación origen-destino antes de publicar (P440 H02).

## S03.P417.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «deployment validation and verification, including production data flows» (p. 23, Tarea 6.6) — subtarea no evaluada; ya cubierta por la verificación del artefacto publicado (P417 H01) y la conciliación origen–destino (P440 H01–H02).
