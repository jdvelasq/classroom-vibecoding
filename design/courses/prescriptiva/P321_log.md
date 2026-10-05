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

## S03.P321.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Design situation reports for senior managers …» y «Communication … must be underpinned by an evidence-based approach to decision making … where the reasons for decisions may require clarification» (PR-Communication, pp. 104–105), más la entrega de resultados «in the client's terminology» (cap. 6, p. 39). Categoría: ya cubierta por el registro operativo con supuesto, alternativa no elegida, indicador y responsable (H01–H03). La falta de evidencia que sustente la recomendación ya es un límite de S02 que este documento no especifica.

## S03.P321.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P321.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
