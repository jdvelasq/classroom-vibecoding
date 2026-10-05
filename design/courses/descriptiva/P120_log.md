# Log — P120

## S02.P120.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P120_retail_sales/` (`data/sales.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con `questions.json` y nueve CSV, `tests/conftest.py`, `tests/test_activity.py`); P100–P109 como contexto de secuencia.
- **Trazabilidad revisada:** P120 → `descriptiva.C01`, `C02`, `C03` en `implementation/descriptiva/traceability.yaml`; coherente con la evidencia. C04 y C05 no mapeados ni evidenciados de forma explícita.
- **Highlights añadidos:** H01–H08 (preguntas enlazadas, grano y consistencia, devolución binaria a valor neto, dos tasas, magnitud y tasa en un gráfico, umbral de volumen y matriz, riesgo vs prioridad, persistencia verificada). Highlight obligatorio de caso y datos: H03.
- **Cambios realizados:** creación de `P120_activity.md`; no se modificó la implementación ni se crearon propuestas.
- **Ambigüedades:** procedencia de `sales.csv` no documentada (real o sintética); tasa global de devolución cercana a 0,5 no comentada en el notebook; las pruebas no verifican `questions.json`; la pregunta de medios de pago no fija criterio de «requiere investigación»; diferencias entre categorías de alrededor de un punto se presentan sin incertidumbre.
- **Cambios de IDs:** ninguno (primera asignación).
- **Superficies, contrato y dependencias:** S01–S06 declaradas; contrato separa notebook, diez archivos de `submission/` y pruebas; dependencias demostrables con P103/P104 (patrón de resumen y prueba) y hacia P121/P122 (plantilla y `questions.json`).
- **Auditoría de Analytics:** el producto es un diagnóstico descriptivo de devoluciones por segmento; pandas y Plotly sirven a ese producto. Responde qué, dónde y cuándo con evidencia persistida; usuario y decisión concreta no evidenciados.

## S03.P120.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T02.
- **Señales descartadas relevantes:**
  - métodos de validación «input validation, data type validation, range and constraint validation, and cross-reference validation» (DPSIA/DI, p. 92) — ya cubierta: P102 H01, P124 H02 y P120 H02 (identidad `Quantity × Price = TotalAmount`).
  - *scores* y *rankings* con características deseables (DM-Proximity, p. 75) — ya cubierta: umbrales de volumen y separación entre riesgo y prioridad (P120 H06–H07, P121 H05, P122 H04/H06).

## S03.P120.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - Task 3.6 «Assess data quality and identify relationships in the data» (p. 5) — ya cubierta: P120 H02, P121 H02, P122 H01, H05.

## S03.P120.03

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** refuerza T01.
- **Señales descartadas relevantes:**
  - brechas de calidad «accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» y métodos para evaluarla (CAP-E.3.6.1, 3.6.4, p. 15) — ya cubierta: P120 H02, P121 H02, P122 H01 y H05.
