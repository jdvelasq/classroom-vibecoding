# Log — P422

## S02.P422.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P422_model_monitoring/` (`data/reference.csv`, `data/production.csv`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/monitoring_report.json`, `tests/test_activity.py`, `requirements.txt`); digests de P404, P420, P423.
- **Trazabilidad revisada:** P422 → `productos.C02`, `C03`, `C05`; C03 y C05 sustentados.
- **Highlights:** añadidos H01 (señal de deriva por variable), H02 (desplazamiento concentrado en un caso construido; caso y datos) y H03 (exclusión de la etiqueta).
- **Ambigüedades:** procedencia de `production.csv` no documentada (filas repetidas, enteros en `alcohol`). No se carga modelo pese al nombre. Las pruebas usan `quality` como variable, que `main()` excluye. Solapamiento conceptual con P404. Sin `HOW_TO_RUN_ME.txt`.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P420 (dominio) y P404 (patrón); habilita: no evidenciada.
- **Auditoría de Analytics:** parcialmente resuelta; vigila insumos sin usuario ni modelo.
