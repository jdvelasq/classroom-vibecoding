# Log — P404

## S02.P404.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P404_model_input_testing_pytest/` (`ESTIMATOR.pkl` como binario, `data/training_inputs.csv`, `data/new_inputs.csv`, `professor/main.py`, `professor/notebook.ipynb`, `professor/test_main.py`, `src/main.py`, `submission/input_distribution_report.json`, `tests/test_activity.py`); comparación con P403.
- **Trazabilidad revisada:** P404 → `productos.C02`, `productos.C03`, `productos.C05`. C03 sostenido; C05 parcial.
- **Highlights:** añadidos H01 (interfaz del artefacto), H02 (detector de compatibilidad), H03 (caso y datos: entradas nuevas de la misma fuente y desplazamiento sintético), H04 (pruebas de aceptación y rechazo).
- **Ambigüedades:** «modelo de priorización» sin objeto ni usuario; `new_inputs.csv` coincide con el holdout de P403, por lo que la compatibilidad es esperable por construcción; umbral 0,15 y contaminación 0,05 sin justificación; reporte persistido distinto del notebook.
- **Superficies / contrato / dependencias:** S01–S06; recibe artefacto y filas de P403.
- **Auditoría de Analytics:** resuelta con reservas: compuerta de insumos de un modelo sin semántica de uso declarada.
