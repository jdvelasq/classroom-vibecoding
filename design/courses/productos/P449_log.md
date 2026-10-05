# Log — P449

## S02.P449.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P449_cost_monitoring/` (`data/costs.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/cost_report.json`, `tests/test_activity.py`); contexto de P439, P442, P445.
- **Trazabilidad revisada:** P449 → `productos.C05`.
- **Highlights:** añadidos H01 (acumulado vs. presupuesto, caso y datos como límite), H02 (suma decimal). El valor 3.6999999999999997 con `float` se comprobó ejecutando la suma de los valores de `data/costs.json`.
- **Ambigüedades:** costos sin unidad, periodo ni capacidad; solapamiento estructural con P445.
- **Superficies / contrato / dependencias:** S01–S05; dependencia sólo de práctica.
- **Auditoría de Analytics:** no resuelta; riesgo de control de gasto genérico.
