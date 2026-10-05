# Log — P452

## S02.P452.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P452_access_control/` (`data/access_policy.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/factory_risk_report.json`, `tests/test_activity.py`); contexto de P427, P430, P450, P454.
- **Trazabilidad revisada:** P452 → `productos.C04`, `productos.C05`.
- **Highlights:** añadidos H01 (política por recurso, caso y datos), H02 (rechazo explícito).
- **Ambigüedades:** reporte fijo en el código con el `high` no derivado de la fábrica 2; sin autenticación ni registro; `data_analyst` y recurso ausente no probados.
- **Superficies / contrato / dependencias:** S01–S05; dependencia de práctica con P427.
- **Auditoría de Analytics:** resuelta con límite; autorización al servicio del reporte de riesgo.

## S03.P452.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DS (p. 88: «Implement access control mechanisms to restrict data leaks»); DP-Information Systems (p. 86: «Outline what information should be provided to a computer entity, balancing usability and privacy») — ya cubierta: P452 H01–H02; la minimización de contenido entregado queda en P453.
