# Log — P417

## S02.P417.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P417_pipeline_integration_test/` (`data/daily_operations.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/factory_totals.json`, `tests/test_activity.py`, `requirements.txt`); digests de P400, P401, P413, P414.
- **Trazabilidad revisada:** P417 → `productos.C02`, `productos.C05`; C05 sin evidencia.
- **Highlights:** añadidos H01 (prueba sobre el artefacto publicado) y H02 (caso trivial como límite de la integración; caso y datos).
- **Ambigüedades:** el «pipeline» es una función de tres pasos; no hay componentes cuya integración pueda fallar. Posible duplicación con `tests/test_report.py` de P413–P414. La prueba del profesor escribe en `submission/` real. Sin `HOW_TO_RUN_ME.txt` ni instrucciones para la plantilla.
- **Superficies / contrato / dependencias:** S01–S04; recibe de P400/P412–P414; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; prueba de software genérica.
