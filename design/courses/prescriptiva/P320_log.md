# Log — P320

## S02.P320.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/` (`data/policy_impacts.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, cuatro artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P300 y P306.
- **Trazabilidad revisada:** P320 → `prescriptiva.C04`, `C05`. Ambas sustentadas en el contrato.
- **Highlights:** añadidos H01–H03. H01 es el highlight obligatorio de caso y datos (grano política × grupo; la unidad de juicio es la política). Cifras de `equity_audit.csv` y `policy_correction_decisions.csv`; los totales de beneficio (21.000 y 18.000) son sumas de filas de los datos.
- **Ambigüedades:** (1) las celdas de `professor/notebook.ipynb` contienen secuencias `\n` literales en vez de saltos de línea: la primera celda es un único comentario y la segunda no es Python válido, por lo que el notebook no se ejecuta; (2) la decisión «suspend_and_correct» no va acompañada de una corrección; (3) no se audita ninguna política producida en el curso, aunque la arquitectura la define como transversal; (4) procedencia del dataset no declarada; (5) la prueba sólo verifica presencia de archivos.
- **Superficies / contrato / dependencias:** S01–S06 declaradas. Recibe sólo el patrón de contrato; no habilita dependencias demostrables.
- **Auditoría de Analytics:** producto terminal = decisión de aprobar o suspender una política con guarda, autoridad, escalamiento y gatillos. Auditoría resuelta en el contrato; incompleta frente a la arquitectura (falta la corrección).
- **Cambios de IDs:** ninguno. No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P320.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.

## S03.P320.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 7.5 efectos colaterales en el tiempo (p. 7) — marginal para P320: su auditoría de equidad ya convierte una consecuencia distributiva en guarda (H01); el seguimiento temporal se integra en la candidata de P321.
