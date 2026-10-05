# Log — P402

## S02.P402.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P402_data_testing_pytest_pandas/` (`data/*.csv`, `professor/main.py`, `professor/notebook.ipynb`, `professor/test_main.py`, `src/main.py`, `submission/validation_report.json`, `tests/test_activity.py`).
- **Trazabilidad revisada:** P402 → `productos.C02`, `productos.C05`. No mapea `productos.C03`, aunque la actividad lo evidencia directamente; C05 sin evidencia.
- **Highlights:** añadidos H01 (contrato), H02 (caso y datos: llave derivada de la granularidad máquina-día), H03 (reporte persistido), H04 (pruebas de aceptación y rechazo).
- **Ambigüedades:** el reporte persistido proviene de `main.py`, no del notebook (faltan `rows`, `contract_columns`, `business_key`); mensajes de llave duplicada distintos entre ambos; procedencia del extracto no documentada; el notebook del profesor permanece aunque la modalidad del estudiante es Python.
- **Superficies / contrato / dependencias:** S01–S06; evaluación sólo por existencia; habilita P405 (subconjunto del extracto).
- **Auditoría de Analytics:** resuelta con reservas: compuerta de insumos con usuario declarado; falta conexión con el indicador protegido y la acción ante rechazo.
