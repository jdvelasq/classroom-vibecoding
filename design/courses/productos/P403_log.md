# Log — P403

## S02.P403.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P403_model_testing_pytest/` (`ESTIMATOR.pkl` como binario, `data/model_test_set.csv`, `professor/main.py`, `professor/notebook.ipynb`, `professor/test_main.py`, `src/main.py`, `submission/model_test_report.json`, `tests/test_activity.py`).
- **Trazabilidad revisada:** P403 → `productos.C02`, `productos.C03`, `productos.C05`. C03 sostenido; C05 indirecto.
- **Highlights:** añadidos H01 (artefacto congelado), H02 (compuerta de umbrales), H03 (familias de pruebas en notebook), H04 (caso y datos: clase asimétrica y objetivo sin semántica).
- **Ambigüedades:** significado de `target` y procedencia de modelo y datos no documentados (los nombres de variables coinciden con los del conjunto Breast Cancer Wisconsin, sin que la implementación lo declare); umbrales sin justificación; reporte persistido de `main.py` distinto del notebook; las pruebas de interfaz y reproducibilidad no están en `pytest`.
- **Superficies / contrato / dependencias:** S01–S06; habilita P404 (mismo artefacto y filas).
- **Auditoría de Analytics:** resuelta con reservas: habilitación de un modelo, sin usuario ni semántica del producto.
