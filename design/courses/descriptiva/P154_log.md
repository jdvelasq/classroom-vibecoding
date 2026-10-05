# Log — P154

## S02.P154.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P154_ventas_dashboard/` (`data/sales_mart.db`, `professor/generate_data.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/` con cinco archivos, `tests/`); contraste con `implementation/descriptiva/P151_ventas_mart/submission/region_category_sales.csv` y con P124 (dashboard Streamlit).
- **Trazabilidad revisada:** P154 → `descriptiva.C01`, `C02`, `C03`, `C05`; `audit-against-design.md` omite C01.
- **Highlights añadidos:** H01 (grano de consumo y aditividad; obligatorio de caso y datos), H02 (CSV y SQLite consistentes), H03 (manifiesto de serving), H04 (respuesta desde serving sin recálculo en presentación).
- **Ambigüedades:** no existe dashboard pese al nombre; `orders` (`COUNT DISTINCT` por celda) no es aditiva y el manifiesto no lo advierte (reproduciendo el generador, la suma de `orders` supera el número de pedidos distintos); «deben recibir atención» se responde con ranking de volumen; la respuesta reproduce la de P151 (posible duplicación); notebook de estudiante vacío.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; recibe esquema y patrón de reconciliación de P151/P152; ninguna actividad posterior consume `bi_serving.db`.
- **Auditoría de Analytics:** producto = capacidad de consumo BI, no descripción interpretada. Pregunta 5 no resuelta: el bloque P150–P154 (tabla → mart → OLAP → KPI → serving) sigue la lógica de un pipeline BI sobre datos sintéticos, con una pregunta por taller, sin usuario observable ni conclusiones persistidas.

## S02.P154.02

- **Fecha / curso / executor:** 2026-10-04 / `descriptiva` / Claude; **estado:** incremental.
- **Origen:** aclaración del profesor: *business intelligence* es un predecesor que, por su importancia, está contenido en la analítica descriptiva (como la minería de datos en la predictiva).
- **Cambio en la auditoría de Analytics:** la auditoría dejaba la pregunta 5 no resuelta por tratarse de una capa de consumo BI. Se corrige: BI forma parte de la analítica descriptiva y la frontera excluye la capacitación en una plataforma BI, no BI como tal; se conservan como límites la falta de criterio de atención, de interfaz y de lectura.
- **Highlights, superficies y dependencias:** sin cambios; no se renumeran IDs.

## S03.P154.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** propone T01.
- **Señales descartadas relevantes:**
  - es un cuerpo de conocimiento de computación para pregrados de ciencia de datos, con 11 áreas de conocimiento y competencias de nivel T1/T2/E. Para descriptiva aportan sobre todo AP (presentación y visualización para clientes), DG/DM-Data Preparation (calidad, integración y limpieza, EDA, enmarcar la pregunta), DPSIA (privacidad e integridad) y PR/cap. 6 (comunicar resultados interpretados y sus límites a no especialistas). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
