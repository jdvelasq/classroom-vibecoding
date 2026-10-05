# Log — P420

## S02.P420.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P420_experiment_tracking/` (`HOW_TO_RUN_ME.txt`, `requirements.txt`, `data/winequality-red.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/experiments/` con dos corridas e `index.json`, `tests/test_activity.py`); digests de P403, P406, P419, P421, P422, P424.
- **Trazabilidad revisada:** P420 → `productos.C02`, `C03`, `C05`; C03 débil.
- **Highlights:** añadidos H01 (partición fija), H02 (corrida recuperable), H03 (índice comparativo) y H04 (objetivo ordinal tratado como clases y KNN sin escalado; caso y datos).
- **Ambigüedades:** procedencia del dataset no documentada en la actividad. `config.json` omite hiperparámetros. Los modelos de P420 no son consumidos por P421/P424, que usan pickles de origen no declarado. Pruebas de estudiante sólo verifican `index.json`.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P419 y P406 (prácticas); habilita P422 sólo por dominio compartido, sin artefacto.
- **Auditoría de Analytics:** parcialmente resuelta; capacidad de trazabilidad de modelos sin usuario ni decisión.
