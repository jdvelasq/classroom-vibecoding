# Log — P523

## S02.P523.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P523_mapreduce_particionamiento/` (`data/truck_events.csv.gz` sólo como binario, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/partition_loads.csv`, `submission/shuffle_comparison.csv`, `tests/test_activity.py`); P519 y P522 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P523 → `data.C02`, `data.C03`, `data.C05`; C03 no sustentado (sesgo de carga, no de evidencia), a escalar.
- **Highlights:** añadidos H01 (sesgo por clave; caso y datos), H02 (particionador determinista), H03 (agregación local, con defecto de modelado).
- **Ambigüedades:** el «combiner» se indexa por partición de destino y su cifra (5) equivale a la salida final, no a pares enviados al shuffle; `hot_key_load` es carga de partición, no de una clave; operadores de P519 copiados sin uso; semántica de `eventKey` y procedencia no documentadas; P523 no figura en el diseño de `case-selection.md`.
- **Superficies / contrato / dependencias:** S01–S06; recibe práctica de P522; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; internos de procesamiento distribuido sin producto analítico.
