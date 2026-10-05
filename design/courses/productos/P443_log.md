# Log — P443

## S02.P443.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P443_data_lineage/` (`data/raw_operations.csv`, `professor/main.py`, `professor/test_main.py`, `requirements.txt`, `src/main.py`, `submission/factory_totals.csv`, `submission/lineage.json`, `tests/test_activity.py`); `P431_data_versioning/submission/data_manifest.json`; agregados de P412, P417, P428, P432.
- **Trazabilidad revisada:** P443 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (cambio de grano, caso y datos), H02 (huella del insumo), H03 (lo que se prueba).
- **Ambigüedades:** el linaje no registra la transformación pese al docstring; `created_at` no determinista; `requirements.txt` local no listado como excepción en `structure-audit.md`; quinta repetición del agregado por fábrica; posible solapamiento con el linaje de dbt en P433.
- **Superficies / contrato / dependencias:** S01–S05; recibe insumo demostrable de P431 (SHA-256 idéntico); habilitación no evidenciada.
- **Auditoría de Analytics:** resuelta con límite; el linaje sirve a un agregado descriptivo del caso de fábricas.
