# Log — P433

## S02.P433.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P433_dbt_duckdb/` (`HOW_TO_RUN_ME.txt`, `dbt_project.yml`, `models/factory_totals.sql`, `models/schema.yml`, `profiles/profiles.yml`, `seeds/daily_operations.csv`, `submission/pre54.duckdb`, `target/graph_summary.json`, `target/run_results.json`, `target/manifest.json` (encabezado), `target/compiled/`, `target/run/`, `logs/dbt.log`, `tests/test_activity.py`); P402 y P432 para relación.
- **Trazabilidad revisada:** P433 → `productos.C02`, `productos.C05`; las pruebas de datos sustentarían `productos.C03`, no mapeada.
- **Highlights:** añadidos H01 (modelo con `ref`), H02 (pruebas `not_null`/`unique`), H03 (reconstrucción con registro), H04 (caso como límite).
- **Ambigüedades:** restos de `pre54_dbt_duckdb` en `target/`; base `pre54.duckdb`; rutas absolutas del autor en `run_results.json`; sin `professor/main.py` ni plantilla `src/` (excepción documentada en `structure-audit.md`); descripción «total diario» sin fecha en el dato; la prueba de actividad no inspecciona la tabla; dbt no aparece en un manifiesto local (depende del ambiente del curso).
- **Superficies/contrato/dependencias:** S01–S07; recibe de P432; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): se lee como formación en dbt.

## S03.P433.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
