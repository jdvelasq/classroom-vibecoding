# Log — P401

## S02.P401.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P401_code_testing_pytest/` (`data/drivers.csv`, `data/timesheet.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/certified_driver_totals.csv`, `tests/test_activity.py`).
- **Trazabilidad revisada:** P401 → `productos.C02`, `productos.C05`. C05 sin evidencia.
- **Highlights:** añadidos H01 (precondición de columnas), H02 (prueba `pytest`), H03 (caso y datos: dos granularidades y atributos sensibles).
- **Ambigüedades:** `drivers.csv` contiene `ssn` y `location` sin documentación de procedencia ni de restricciones de uso; el producto publica `name`. La rama `ValueError` no se prueba. Conteos de filas tomados del número de líneas del digest.
- **Superficies / contrato / dependencias:** S01–S06; evaluación sólo por existencia; recibe la práctica de P400; no habilita una actividad posterior de forma demostrable.
- **Auditoría de Analytics:** no resuelta. Posible duplicación con P400 (misma estructura, distinto marco de pruebas); se lee como entrenamiento en herramienta.
