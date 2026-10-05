# Log — P424

## S02.P424.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P424_model_rollback/` (`REGISTRY.json`, `MODEL_V1.pkl` y `MODEL_V2.pkl` (sólo tamaño), `HOW_TO_RUN_ME.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/production/`, `tests/test_activity.py`); digests de P406, P421, P423, P448.
- **Trazabilidad revisada:** P424 → `productos.C02`, `C03`, `C05`; C03 sin evidencia.
- **Highlights:** añadidos H01 (reversión por copia verificada por bytes), H02 (registro de reversión auditable) y H03 (versiones indistinguibles y sin motivo; caso y datos como límite).
- **Ambigüedades:** `REGISTRY.json` no se actualiza tras la reversión; v1 y v2 tienen igual tamaño y origen no declarado; no se registra motivo; esquema de registro distinto al de P421; la alerta de P423 no se usa.
- **Superficies / contrato / dependencias:** S01–S05; recibe prácticas de P421; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; recuperación genérica sin capacidad analítica identificable.
