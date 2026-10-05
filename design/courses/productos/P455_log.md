# Log — P455

## S02.P455.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P455_data_retention/` (`data/events.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/retention_result.json`, `tests/test_activity.py`); contexto de P436–P439.
- **Trazabilidad revisada:** P455 → `productos.C05`.
- **Highlights:** añadidos H01 (corte reproducible, caso y datos con límite), H02 (borde del corte).
- **Ambigüedades:** eventos sin significado ni relación con el caso de fábricas; plazo de 90 días sin fundamento; no hay eliminación ni archivo efectivo.
- **Superficies / contrato / dependencias:** S01–S05; dependencia sólo de práctica.
- **Auditoría de Analytics:** no resuelta; riesgo de regla genérica de ciclo de vida.

## S03.P455.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P455.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
