# Log — P306

## S02.P306.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P306_credit_campaign_targeting/` (`data/campaign.csv`, `data/synthetic_truth.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, siete artefactos de `submission/`, `tests/test_activity.py`); relación con P303 y P305.
- **Trazabilidad revisada:** P306 → `prescriptiva.C02`, `C04`, `C05`; sustentadas; C01 y C03 ejercidas sin mapeo.
- **Highlights:** añadidos H01–H08 (validación sin filtración; riesgo vs efecto; valor y selección exacta; cuatro reglas; especificación del modelo; rendimientos decrecientes; banda y monitoreo; registro vs validación).
- **Ambigüedades:** (1) la evaluación de políticas usa una verdad sintética no disponible en operación; no se estima el valor de la política con resultados observados; (2) la política se aplica al mismo lote de prueba que sirve para evaluarla; (3) la operación propuesta no conserva grupo de control, aunque el monitoreo pide «retención observada por lote»; (4) banda de revisión ±0,50 y costo 5 sólo en código; (5) el nombre «credit campaign» frente a un caso de retención; el diseño prevé restricción de exposición y se implementa cupo de capacidad; (6) la prueba sólo exige un archivo cualquiera; (7) generador de los datos sintéticos no visible.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P303/P305; formato `monitoring_plan.csv` reaparece en P308.
- **Auditoría de Analytics:** política prescriptiva gobernada con insumo causal, autoridad, banda de excepción, cadencia semanal y monitoreo con acciones; la identidad se preserva, con la reserva de que la validación es sintética.

## S03.P306.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - disposición «there may be multiple acceptable solutions … depending on … the need for optimality, time constraints» y CSP (AI-Planning and Search, pp. 52–53). Categoría: ya cubierta. El método se elige según la estructura del problema en P306 H03, P317 H04 y P319 H03, y la elegibilidad por par entra como restricción en P308 H01.
  - «Causal models» (T1) (AI, p. 51) y «Debate the possible effects -- both positive and negative -- of decisions arising from machine learning conclusions» (ML, p. 94). Categoría: ya cubierta por la separación entre riesgo y efecto causal y el uso del efecto como insumo de la acción (H01–H04). Profundizar en modelos causales pertenece a Predictiva.

## S03.P306.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P306.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P306.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - ninguna adicional.
