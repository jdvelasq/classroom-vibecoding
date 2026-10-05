# Log — P435

## S02.P435.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P435_schema_migration/` (`data/record_v1.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/record_v2.json`, `tests/test_activity.py`); P430, P434, P450 y P451 para relación.
- **Trazabilidad revisada:** P435 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (migración preservando el valor), H02 (caso como límite).
- **Ambigüedades:** la salida no se valida contra el contrato de P434; riesgo `high` literal; escritura en `__main__` sin función `main`; sin `HOW_TO_RUN_ME.txt`; posible combinación con P434.
- **Superficies/contrato/dependencias:** S01–S05; relación conceptual con P434.
- **Auditoría de Analytics:** riesgo moderado: migración genérica.

## S03.P435.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P435.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
