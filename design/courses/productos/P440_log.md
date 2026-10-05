# Log — P440

## S02.P440.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P440_data_reconciliation/` (`data/source.json`, `data/target.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/reconciliation.json`, `tests/test_activity.py`); P402 y P417 para relación.
- **Trazabilidad revisada:** P440 → `productos.C02`, `productos.C03`, `productos.C05`.
- **Highlights:** añadidos H01 (total de control; caso y datos), H02 (veredicto agregado).
- **Ambigüedades:** métricas declaradas, no calculadas; medida `amount` ajena a los casos del curso; sin tolerancia ni localización de la diferencia; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; recibe práctica de P402; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): control genérico sin capacidad analítica.

## S03.P440.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
