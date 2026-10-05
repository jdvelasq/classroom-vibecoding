# Log — P406

## S02.P406.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P406_config_cmd_line/` (`HOW_TO_RUN_ME.txt`, `ESTIMATOR.pkl` y `data/*/sentences.csv.gz` como binarios, `professor/main.py`, `src/main.py`, `submission/metrics.json`, `tests/test_activity.py`).
- **Trazabilidad revisada:** P406 → `productos.C02`, `productos.C03`, `productos.C05`. C03 débil; C05 sin evidencia.
- **Highlights:** añadidos H01 (parametrización con valores admitidos), H02 (caso y datos: texto con particiones etiquetadas, incluida `prod`), H03 (métricas atribuidas a su configuración).
- **Ambigüedades:** contenido, tamaño en filas, semántica de `target` y procedencia de datos y modelo no documentados; `prod` contiene etiquetas; la comparación entre conjuntos pedida en las instrucciones no se persiste; sin prueba del profesor.
- **Superficies / contrato / dependencias:** S01–S05; habilita P407 (mismo artefacto y datos).
- **Auditoría de Analytics:** no resuelta: práctica de configuración sin capacidad analítica identificada.
