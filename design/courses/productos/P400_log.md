# Log — P400

## S02.P400.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P400_code_testing_unittest/` (`data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/factory_totals.csv`, `tests/test_activity.py`); contexto en `s05-diseno-productos.md` y `structure-audit.md`.
- **Trazabilidad revisada:** P400 → `productos.C02`, `productos.C05`. C05 sin evidencia observable.
- **Highlights:** añadidos H01 (regla aislada), H02 (prueba `unittest`), H03 (caso y datos: ausencia de particularidad como límite).
- **Ambigüedades:** la prueba de lógica vive en `professor/` y no forma parte de la evaluación; no hay `HOW_TO_RUN_ME.txt` ni notebook para el estudiante; el dato no tiene procedencia y la variable `daily_units_produced` no tiene fecha.
- **Superficies / contrato / dependencias:** S01–S06 declaradas; la prueba de evaluación sólo verifica existencia; habilita P408 y P412–P414 por reutilización del indicador y del archivo.
- **Auditoría de Analytics:** no resuelta. El indicador es trivial y sin usuario; la actividad se lee como práctica genérica de pruebas unitarias (pregunta 5).
