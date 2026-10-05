# Log — P437

## S02.P437.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P437_late_arriving_data/` (`data/arrival.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/arrival_classification.json`, `tests/test_activity.py`); P436 y P438 para relación.
- **Trazabilidad revisada:** P437 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (evento frente a procesamiento; caso y datos), H02 (acción de reproceso).
- **Ambigüedades:** `arrival_date` se lee pero no interviene; todo evento pasado es «tardío»; sin ventana de tolerancia; reproceso no ejecutado; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; relaciones conceptuales con P436 y P438.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): patrón genérico sin indicador afectado.

## S03.P437.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
