# Log — P439

## S02.P439.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P439_data_freshness/` (`data/source_status.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/freshness_report.json`, `tests/test_activity.py`); P422, P423, P436–P438 y P442 para relación.
- **Trazabilidad revisada:** P439 → `productos.C02`, `productos.C03`, `productos.C05`; C02 débil.
- **Highlights:** añadidos H01 (alerta de frescura con umbral), H02 (caso como límite).
- **Ambigüedades:** umbral de 1 día sin justificación de uso (la prueba usa 3); la alerta no tiene efecto; fechas declaradas, no leídas de una fuente; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; recibe patrón de P422–P423; habilita P442 (campos de frescura).
- **Auditoría de Analytics:** riesgo moderado: práctica pertinente sin fuente ni consumidor.

## S03.P439.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
