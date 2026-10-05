# Log — P429

## S02.P429.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P429_prefect/` (`HOW_TO_RUN_ME.txt`, `data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `requirements.txt`, `src/main.py`, `submission/prefect_report.json`, `tests/test_activity.py`); P428 y P405 para relación.
- **Trazabilidad revisada:** P429 → `productos.C02`, `productos.C05`; C05 apoyado sólo en `retries=1`.
- **Highlights:** añadidos H01 (tareas con dependencia), H02 (reintento declarado), H03 (tarea probada con `.fn`), H04 (caso y datos como límite).
- **Ambigüedades:** el reintento nunca se ejercita ni se prueba; no se persisten estados de Prefect; P428 (agenda) y P429 (flujo) no se integran; `requirements.txt` local con `prefect>=3,<4` no documentado como excepción; mismo cálculo 9303/9300.
- **Superficies/contrato/dependencias:** S01–S05; recibe de P428; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): se lee como formación en Prefect sin capacidad analítica con usuario.

## S03.P429.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
