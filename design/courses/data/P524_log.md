# Log — P524

## S02.P524.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P524_seleccion_formato_datos/` (`data/flights.csv`, `data/flights.json`, `data/flights.csv.gz` y `data/flights.parquet` como binarios, `data/sales.*`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/format_comparison.csv`, `tests/test_activity.py`); P513, P518 y P522 para contraste.
- **Trazabilidad revisada:** P524 → `data.C02`–`data.C05`; C03 débil.
- **Highlights:** añadidos H01 (mismas filas), H02 (costo de representación de un registro ancho con nulos; caso y datos), H03 (tabla de decisión).
- **Ambigüedades:** propiedades booleanas constantes; comparación mezcla formato y compresión y omite el CSV comprimido de entrada; JSON fuera del `assert`; el notebook escribe sus salidas en `data/`; `sales.csv/json/parquet` sin uso y sin procedencia; procedencia de vuelos no documentada.
- **Superficies / contrato / dependencias:** S01–S05; recibe: ninguna demostrable; habilita P525 sólo como práctica.
- **Auditoría de Analytics:** riesgo moderado; formatos sin uso analítico, vinculados a la estructura de los datos.
