# Log — P520

## S02.P520.01

- **Fecha:** 2026-10-04; **curso / executor:** `data` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/data/P520_mapreduce_basico/` (`data/timesheet.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/driver_metrics.csv`, `tests/test_activity.py`); P519 para operadores y datos; `dig/case-selection.md` como contexto.
- **Trazabilidad revisada:** P520 → `data.C01`, `data.C02`, `data.C05`; C01 parcial.
- **Highlights:** añadidos H01 (SQL como especificación), H02 (valor compuesto con contador; caso y datos), H03 (aplicación completa y persistencia).
- **Ambigüedades:** SQL no ejecutado y distinto de la salida (`mean_hours`); el SQL aparece después del mapper, a diferencia de «primero la pregunta y su SQL» de `case-selection.md`; `weeks` cuenta filas sin verificar unicidad conductor-semana; procedencia de datos no documentada.
- **Contraste con `case-selection.md`:** conforme en pregunta, datos y SQL acotado; añade `mean_hours`.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P519; P521 repite la agregación sin consumir el archivo.
- **Auditoría de Analytics:** producto descriptivo por entidad con pregunta explícita; MapReduce como habilitador; sin interpretación de resultados.
