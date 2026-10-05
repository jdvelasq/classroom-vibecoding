# Log — P430

## S02.P430.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P430_idempotency/` (`professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/daily_report.json`, `tests/test_activity.py`, `data/`); P425, P428 y P429 para relación; P435, P450, P451 para el registro recurrente.
- **Trazabilidad revisada:** P430 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (reejecución idempotente), H02 (caso y datos como límite).
- **Ambigüedades:** la docstring habla de «clave estable» pero la identidad es la ruta del archivo, no `report_date`; el riesgo `high` de la fábrica 2 es literal y contradice la regla de P425 aplicada a `daily_operations.csv`; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; recibe vocabulario de P425; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo moderado (pregunta 5): patrón de ingeniería de pipelines sin capacidad calculada.

## S03.P430.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
