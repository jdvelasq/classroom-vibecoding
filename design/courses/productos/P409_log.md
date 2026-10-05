# Log — P409

## S02.P409.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P409_branch_merge/` (`HOW_TO_RUN_ME.txt`, `data/repository_template/product_card.md`, `data/branch_merge_case.bundle` como binario, `submission/git_log.txt`, `tests/test_activity.py`); tarjetas de P408 y P410 para continuidad.
- **Trazabilidad revisada:** P409 → `productos.C01`, `productos.C04`. C04 sin evidencia.
- **Highlights:** añadidos H01 (rama y fusión explícita), H02 (caso y datos: cambio de consumidor inconsistente con P408/P410).
- **Ambigüedades:** consumidor «equipo de mantenimiento» frente a «equipo de operaciones» en P408 y P410; uso del `.bundle` no documentado; mapeo a C04 sin revisión ni control de acceso.
- **Superficies / contrato / dependencias:** S01–S05; recibe tarjeta de P408.
- **Auditoría de Analytics:** no resuelta: práctica de Git anclada a un producto, sin decisión ni revisión.

## S03.P409.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
