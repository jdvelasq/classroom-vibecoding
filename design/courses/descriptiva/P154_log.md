# Log — P154

## S02.P154.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P154_ventas_dashboard/` (`data/sales_mart.db`, `professor/generate_data.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` con cinco archivos, `tests/`); contraste con `implementation/descriptiva/P151_ventas_mart/submission/region_category_sales.csv` y con P124 (dashboard Streamlit).
- **Trazabilidad revisada:** P154 → `descriptiva.C01`, `C02`, `C03`, `C05`; `audit-against-design.md` omite C01.
- **Highlights añadidos:** H01 (grano de consumo y aditividad; obligatorio de caso y datos), H02 (CSV y SQLite consistentes), H03 (manifiesto de serving), H04 (respuesta desde serving sin recálculo en presentación).
- **Ambigüedades:** no existe dashboard pese al nombre; `orders` (`COUNT DISTINCT` por celda) no es aditiva y el manifiesto no lo advierte (reproduciendo el generador, la suma de `orders` supera el número de pedidos distintos); «deben recibir atención» se responde con ranking de volumen; la respuesta reproduce la de P151 (posible duplicación); notebook de estudiante vacío.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; recibe esquema y patrón de reconciliación de P151/P152; ninguna actividad posterior consume `bi_serving.db`.
- **Auditoría de Analytics:** producto = capacidad de consumo BI, no descripción interpretada. Pregunta 5 no resuelta: el bloque P150–P154 (tabla → mart → OLAP → KPI → serving) sigue la lógica de un pipeline BI sobre datos sintéticos, con una pregunta por taller, sin usuario observable ni conclusiones persistidas.
