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

## S03.P320.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-E.1.2.2 «Identify stakeholders and bystanders» (p. 7) — marginal: P308 y P320 ya distinguen afectados (familias, grupos) de decisores; no cambia lo que el estudiante hace.

## S03.P320.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - consecuencias indirectas y efectos adversos a lo largo del tiempo (p. 8: CAP-P.1.5.6; p. 25: CAP-P.7.5.1 «Identify likely adverse consequences of implementing the analytics solution») y temas éticos en el informe de validación (p. 22: CAP-P.6.1.2) — ya cubierta en su núcleo por P320 H01–H03 (guarda de equidad que decide y gobernanza) y, como consecuencias operativas, por P304 H04 y P309 H05; el documento sólo fija una expectativa general, sin método nuevo que enseñar.

## S03.P320.05

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` (`source_sha256`: b2eb680e173ceee7cfeaba06abf06986fa09ff154010f7052ac90741d2603936).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - catálogo oficial de técnicas de modelado dimensional (proceso, grano, hechos, dimensiones, dimensiones lentamente cambiantes, esquemas especiales) para data warehouses y BI. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
