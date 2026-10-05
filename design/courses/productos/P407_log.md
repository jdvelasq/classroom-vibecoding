# Log — P407

## S02.P407.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P407_config_file/` (`CONFIG.json`, `ESTIMATOR.pkl` y `data/*/sentences.csv.gz` como binarios, `professor/main.py`, `src/main.py`, `submission/metrics.json`, `tests/test_activity.py`); comparación con P406.
- **Trazabilidad revisada:** P407 → `productos.C02`, `productos.C03`, `productos.C05`. C03 y C05 sin evidencia nueva.
- **Highlights:** añadidos H01 (configuración por archivo validada), H02 (caso y datos: caso repetido de P406 como límite).
- **Ambigüedades:** posible duplicación con P406; sin `HOW_TO_RUN_ME.txt` para el estudiante (P406 sí lo tiene); `metrics.json` idéntico al de P406, por lo que la evaluación no distingue el mecanismo.
- **Superficies / contrato / dependencias:** S01–S06; recibe todo el caso de P406.
- **Auditoría de Analytics:** no resuelta: práctica de configuración sin capacidad analítica identificada.
