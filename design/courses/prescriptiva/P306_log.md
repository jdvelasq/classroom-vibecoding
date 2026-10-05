# Log — P306

## S02.P306.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P306_credit_campaign_targeting/` (`data/campaign.csv`, `data/synthetic_truth.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, siete artefactos de `submission/`, `tests/test_activity.py`); relación con P303 y P305.
- **Trazabilidad revisada:** P306 → `prescriptiva.C02`, `C04`, `C05`; sustentadas; C01 y C03 ejercidas sin mapeo.
- **Highlights:** añadidos H01–H08 (validación sin filtración; riesgo vs efecto; valor y selección exacta; cuatro reglas; especificación del modelo; rendimientos decrecientes; banda y monitoreo; registro vs validación).
- **Ambigüedades:** (1) la evaluación de políticas usa una verdad sintética no disponible en operación; no se estima el valor de la política con resultados observados; (2) la política se aplica al mismo lote de prueba que sirve para evaluarla; (3) la operación propuesta no conserva grupo de control, aunque el monitoreo pide «retención observada por lote»; (4) banda de revisión ±0,50 y costo 5 sólo en código; (5) el nombre «credit campaign» frente a un caso de retención; el diseño prevé restricción de exposición y se implementa cupo de capacidad; (6) la prueba sólo exige un archivo cualquiera; (7) generador de los datos sintéticos no visible.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P303/P305; formato `monitoring_plan.csv` reaparece en P308.
- **Auditoría de Analytics:** política prescriptiva gobernada con insumo causal, autoridad, banda de excepción, cadencia semanal y monitoreo con acciones; la identidad se preserva, con la reserva de que la validación es sintética.
