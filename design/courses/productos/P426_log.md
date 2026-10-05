# Log — P426

## S02.P426.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P426_api_container/` (`Dockerfile`, `.dockerignore`, `HOW_TO_RUN_ME.txt`, `requirements.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/score_response.json`, `tests/test_activity.py`); digests de P418, P425; `structure-audit.md` (manifiesto local).
- **Trazabilidad revisada:** P426 → `productos.C02`, `C04`, `C05`; C05 sin evidencia.
- **Highlights:** añadidos H01 (servicio en contenedor frente al lote de P418) y H02 (borde 4500 y estrictez de tipo; caso y datos con regla sin procedencia).
- **Ambigüedades:** el docstring afirma que el contenedor entrega la misma decisión, pero las pruebas no ejecutan el contenedor. Lógica duplicada de P425. La plantilla `src/main.py` no expone el `app` que espera el `CMD` del `Dockerfile`, y las instrucciones no lo indican.
- **Superficies / contrato / dependencias:** S01–S05; recibe de P425 y P418; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; despliegue con herramienta sobre regla arbitraria.
