# Log — P445

## S02.P445.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P445_service_level/` (`data/executions.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/service_level.json`, `tests/test_activity.py`); contexto de P428, P429, P439, P442.
- **Trazabilidad revisada:** P445 → `productos.C04`, `productos.C05`.
- **Highlights:** añadidos H01 (disponibilidad por ejecuciones, caso y datos), H02 (meta inclusiva).
- **Ambigüedades:** capacidad medida, periodo y autor de la meta no evidenciados; la actividad encaja con `productos.C01` (nivel de servicio), no mapeada, y su vínculo con C04 no es visible.
- **Superficies / contrato / dependencias:** S01–S05; dependencia sólo de práctica.
- **Auditoría de Analytics:** no resuelta; riesgo de SLO genérico sin capacidad analítica identificada.

## S03.P445.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - PR-Legal (p. 109: «Recovery mechanisms and maintaining 100% operation»); BDS (p. 58: «Data backup») — ya cubierta: P445 H01–H02, P448 H01–H02.

## S03.P445.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
