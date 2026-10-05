# Log — P303

## S02.P303.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P303_politicas_y_supervision_humana/` (`data/applications.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, `submission/review_policy.csv`, `submission/policy_contract.json`, `tests/test_activity.py`); relación con P300 y P302.
- **Trazabilidad revisada:** P303 → `prescriptiva.C01`, `C04`; sustentadas.
- **Highlights:** añadidos H01–H04 (precedencia y autoridad; puntaje vs acción; registro versionado; salvaguardas).
- **Ambigüedades:** (1) el volcado muestra sólo cinco de seis solicitudes y la fila A05 de `review_policy.csv` truncada; no se puede confirmar que la rama «recomendar_rechazo» se ejercite (ninguna solicitud visible con documentación completa y monto ≤ 10.000 supera 0,30); (2) umbrales 0,08, 0,30 y 10.000 sólo en código, ausentes del contrato; (3) el notebook importa `main` desde `src/`, vacío; (4) procedencia de las solicitudes y de la probabilidad no documentada.
- **Superficies / contrato / dependencias:** S01–S05; prueba de columnas y campos no vacíos; recibe de P300/P302; práctica retomada en P306.
- **Auditoría de Analytics:** regla prescriptiva por entidad con autoridad humana y escalamiento; faltan validación de umbrales y monitoreo ejecutado. Identidad de Analytics preservada.

## S03.P303.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify steps needed to ensure that a decision-making system is auditable» (PR-On Automation, p. 110). Categoría: ya cubierta por el registro por solicitud con versión, razón y autoridad (H03) y las salvaguardas declaradas (H04).

## S03.P303.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
