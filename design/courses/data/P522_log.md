# Log — P522

## S02.P522.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P522_mapreduce_multiprocessing/` (`data/flights.csv.gz` sólo como binario, `professor/main.py`, `src/main.py`, `submission/origin_flights.csv`, `submission/benchmark.csv`, `tests/test_activity.py`); P519–P521 y P524 para contraste; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P522 → `data.C02`, `data.C05`; C03 (filtro de cancelados) no mapeado; C05 tensionado.
- **Highlights:** añadidos H01 (filtro de cancelados en el mapper; caso y datos), H02 (reducción en dos niveles), H03 (equivalencia secuencial–paralela), H04 (medición de aceleración).
- **Ambigüedades:** sin pregunta analítica; procedencia y periodo de vuelos no documentados; `temp/` no aparece en la implementación y `TEMP_DIR / "input"` se crea con `mkdir()` sin `parents` (posible fallo de ejecución); benchmark de una corrida dependiente del equipo; sin notebook de profesor; P522 no figura en el diseño del bloque MapReduce de `case-selection.md`, que llega sólo a P521.
- **Superficies / contrato / dependencias:** S01–S07; recibe operadores de P519; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; lectura de computación paralela/Big Data sin producto analítico.
