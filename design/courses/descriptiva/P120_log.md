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
