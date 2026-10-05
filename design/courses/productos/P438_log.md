# Log — P438

## S02.P438.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P438_backfill/` (`data/events.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/backfill_selection.json`, `tests/test_activity.py`); P430, P436 y P437 para relación.
- **Trazabilidad revisada:** P438 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (rango inclusivo), H02 (alcance registrado; caso como límite).
- **Ambigüedades:** no hay reproceso efectivo; rango literal; sin conexión con P437 ni con la idempotencia de P430; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; relación conceptual con P437.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5); P436–P438 candidatas a combinación.

## S03.P438.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P438.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
