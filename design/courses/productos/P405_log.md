# Log — P405

## S02.P405.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P405_logs/` (`data/machine_throughput_export.csv`, `professor/main.py`, `src/main.py`, `submission/pipeline.log` como binario, `tests/test_activity.py`); `structure-audit.md`.
- **Trazabilidad revisada:** P405 → `productos.C02`, `productos.C05`. C05 mínimo; C02 débil.
- **Highlights:** añadidos H01 (ciclo de vida instrumentado), H02 (caso y datos: insumo sin particularidad como límite).
- **Ambigüedades:** contenido de `pipeline.log` no verificable en el digest; sin prueba de profesor ni instrucciones; el total es global y no por fábrica como en P400; el log se sobrescribe en cada ejecución.
- **Superficies / contrato / dependencias:** S01–S05; recibe filas de P402.
- **Auditoría de Analytics:** no resuelta: se lee como entrenamiento en `logging` sobre un cálculo trivial.
