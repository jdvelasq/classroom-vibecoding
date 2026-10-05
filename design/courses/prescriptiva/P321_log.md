# Log — P321

## S02.P321.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/` (`data/recommendation.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `submission/policy_register.csv`, `tests/test_activity.py`); para relaciones, P300 y P311.
- **Trazabilidad revisada:** P321 → `prescriptiva.C04`, `C05`. Ambas sustentadas como declaración; C05 sin datos de seguimiento.
- **Highlights:** añadidos H01–H03. H01 es el highlight obligatorio de caso y datos (la entrada es una recomendación ya tomada, no observaciones).
- **Ambigüedades:** (1) la recomendación no proviene de ninguna actividad previa, aunque su contexto recuerda a P311; (2) 12 de los 17 campos del registro están escritos en el código; (3) no hay datos de seguimiento, por lo que el gatillo nunca se evalúa; (4) solapamiento posible con los contratos JSON que cierran cada taller.
- **Superficies / contrato / dependencias:** S01–S05 declaradas. Sin dependencias demostrables.
- **Auditoría de Analytics:** producto terminal = registro operativo de una política con autoridad, meta y gatillo. Auditoría parcialmente resuelta: el producto documenta una política pero no la produce ni la monitorea con evidencia.
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».
