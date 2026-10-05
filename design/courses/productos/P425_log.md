# Log — P425

## S02.P425.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P425_api_contract/` (`HOW_TO_RUN_ME.txt`, `requirements.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/score_examples.json`, `tests/test_activity.py`); digests de P400, P423, P426 y búsqueda de «risk» en P430–P455.
- **Trazabilidad revisada:** P425 → `productos.C02`, `C04`, `C05`; C05 sin evidencia; C01 evidenciada pero no mapeada.
- **Highlights:** añadidos H01 (contrato con errores explicables), H02 (ejemplos ejecutados) y H03 (regla de umbral sin procedencia; caso y datos).
- **Ambigüedades:** umbral 4500 sin origen; las cuatro filas de `daily_operations.csv` serían `low`. La validación admite negativos y booleanos. `tests/test_activity.py` no verifica contenido. Vocabulario «factory risk» recurrente en P430–P452 sin artefacto común.
- **Superficies / contrato / dependencias:** S01–S05; recibe: ninguna; habilita P426 (lógica copiada).
- **Auditoría de Analytics:** parcialmente resuelta; mecanismo de la línea sobre una regla arbitraria.
