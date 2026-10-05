# Log — P441

## S02.P441.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P441_data_quarantine/` (`data/records.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/quarantine.json`, `tests/test_activity.py`); P402 y P440 para relación.
- **Trazabilidad revisada:** P441 → `productos.C02`, `productos.C03`, `productos.C05`; C02 débil.
- **Highlights:** añadidos H01 (cuarentena con motivo), H02 (caso como límite).
- **Ambigüedades:** una sola regla; válidos y cuarentena en el mismo archivo; sin reingreso; `amount` genérico desconectado del caso de fábricas; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; recibe práctica de P402; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): patrón genérico de data engineering.
