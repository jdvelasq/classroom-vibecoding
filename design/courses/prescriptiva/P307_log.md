# Log — P307

## S02.P307.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P307_decision_informada_por_pronosticos/` (tres archivos de `data/`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, tres CSV de `submission/`, `tests/test_activity.py`); relación con P300, P302 y P304.
- **Trazabilidad revisada:** P307 → `prescriptiva.C01`–`C05`; C01 parcial, C02 sustentada, C03 y C05 no evidenciadas, C04 mínima.
- **Highlights:** añadidos H01–H04 (escenarios y gobierno como datos; valor y quiebre; guardia antes de maximizar; política persistida).
- **Ambigüedades:** (1) la guardia de servicio no cambia la decisión: 110 es también el máximo sin restricción y está en el borde (0,25); (2) `order_comparison.csv` en `submission/` no lo produce el código actual; (3) notebook de dos celdas sin evidencia visual, importando `main` desde `src/` vacío; (4) no hay pronóstico construido: el título «informada por pronósticos» descansa en escenarios dados; (5) trazabilidad a cinco capacidades excede la evidencia; (6) posible duplicación técnica con P300/P302 y solapamiento con P304.
- **Superficies / contrato / dependencias:** S01–S05; pruebas de forma; recibe patrón de P300/P302; no habilita actividades posteriores.
- **Auditoría de Analytics:** auditoría no resuelta para el producto prescriptivo completo: hay acción factible, guardia, dueño, cadencia y gatillo, pero faltan excepción, validación (líneas base, sensibilidad) y monitoreo de resultados.
