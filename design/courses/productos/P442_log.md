# Log — P442

## S02.P442.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P442_data_observability/` (`data/signals.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/observability_report.json`, `tests/test_activity.py`); contexto de P439–P441.
- **Trazabilidad revisada:** P442 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (señal con umbral, caso y datos), H02 (veredicto integrado), H03 (bordes en pruebas).
- **Ambigüedades:** las señales no remiten a ningún dataset o capacidad del curso; la frescura duplica parcialmente P439 sin consumir su reporte; sin `HOW_TO_RUN_ME.txt` ni notebook para el estudiante.
- **Superficies / contrato / dependencias:** S01–S05 declaradas; dependencia de práctica con P439; habilitación no evidenciada.
- **Auditoría de Analytics:** no resuelta; riesgo de observabilidad genérica sin producto analítico observado.

## S03.P442.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P442.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P442.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - dimensiones de calidad «accuracy, completeness, consistency, timeliness, validity, uniqueness» (p. 15, CAP-E.3.6.1) — ya cubierta: contrato de datos (P402 H01), frescura (P439 H01), observabilidad integrada (P442 H02).
