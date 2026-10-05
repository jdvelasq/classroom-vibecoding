# P154 — Propuestas de mejora

**Línea base:** `P154_activity.md` (entrada S02 más reciente: `S02.P154.02`).

## T01 — Definir un criterio de atención que use el grano mensual de la capa de consumo y declarar la no aditividad de `orders`

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` p. 46 — AP-Visualization incluye «Dashboards and interactive visualisation» y la habilidad «Implement an effective visualization, given a set of data that has to be used for a particular purpose»: lo que alimenta un tablero se diseña para un propósito declarado (Claude, 2026-10-04). Fuente *authoritative*: respaldo general; no prescribe el criterio.
  - `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` pp. 176 y 219 — se valora «diseñar cuadros de mando (dashboards) efectivos, transmitir hallazgos (insights) mediante visualizaciones apropiadas» (p. 176) y la competencia de BI es «Construir dashboards e informes visuales para la toma de decisiones» (p. 219) (Claude, 2026-10-04). Fuente *governmental*: sólo pertinencia laboral; la fila de p. 219 nombra plataformas (Power BI, Tableau), que no se prescriben.
  - `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` p. 23 — en la «Ficha mínima de cada indicador», «Línea base y meta: situación inicial y resultado esperado» y «Decisión asociada: la acción que puede desencadenar su resultado»: un indicador señala atención frente a una referencia, no por su volumen (Claude, 2026-10-04). Fuente *literature-derived*: práctica de definición de indicadores, no prescripción de gestión.
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` pp. 7 y 9 — «Semi-additive measures can be summed across some dimensions, but not all… some measures are completely non-additive», con la recomendación de guardar los componentes aditivos y calcular la medida al final (p. 7); y «sales actuals can be consolidated with sales forecasts in a single fact table to make the task of analyzing actuals versus forecasts simple and fast» (p. 9) (Claude, 2026-10-04). Fuente *authoritative*: respalda la declaración de no aditividad y la opción de brecha frente a una meta.
- **Qué gana el estudiante:** definir y aplicar un criterio de atención que
  sólo la capa de consumo permite calcular, y reconocer qué métricas de esa
  capa no se pueden sumar. Hoy «¿Qué región y categoría deben recibir
  atención en el dashboard de ventas?» se responde reagregando la tabla de
  serving por región y categoría y ordenando por ventas netas. El resultado
  reproduce `region_category_sales.csv` de P151 (S04; H04, límite «el
  resultado repite P151»): el grano mensual que justifica la capa de consumo
  no interviene y «atención» equivale a «mayor volumen». Además, `orders` es
  `COUNT(DISTINCT order_id)` por celda y no es aditiva entre celdas, pero el
  manifiesto no lo advierte (H01, límite; S02). Con el cambio, el estudiante
  formula un criterio de atención (por ejemplo, el cambio del último mes
  frente a un período de referencia, o la brecha frente a una línea base o
  meta), lo calcula desde `dashboard_sales`, persiste su lectura y deja en
  el contrato de consumo qué métricas pueden sumarse.
- **Anclas actuales:** H01 (grano de consumo y aditividad; `orders` no
  advertida), H03 (manifiesto de serving), H04 (respuesta desde serving sin
  recálculo en la presentación; repite P151); superficies S02 (grano y
  métricas), S03 (manifiesto), S04 (pregunta y respuesta) y S05 (pruebas
  `test_04`, `test_05`).
- **Alternativas menores descartadas:**
  - Sólo escribir que «atención» significa mayor volumen: dejaría la
    respuesta duplicada con P151 y sin uso del grano mensual.
  - Construir una interfaz de dashboard (Streamlit u otra): P124 H04 ya
    enseña un tablero filtrable con funciones separadas de la interfaz.
    Repetirlo agregaría una segunda contribución sin corregir el defecto (la
    falta de criterio). Se descarta.
  - Sólo añadir la nota de no aditividad: corrige el contrato, pero no la
    respuesta que repite P151.
- **Contrato de no regresión:** se conservan H01–H03, `dashboard_sales.csv`,
  `bi_serving.db` (una tabla, igual al CSV), la reconciliación de
  `net_sales` y `test_02`–`test_03`. `priority_region_category.csv` y su
  gráfico se conservan como contexto de volumen, con su prueba. Sustitución
  explícita: la pregunta de atención pasa a responderse con el artefacto
  nuevo, que se deriva también de `dashboard_sales` (H04 se mantiene: no se
  recalcula desde el hecho). `serving_manifest.csv` gana una columna; las
  existentes y los textos que exige `test_04` no cambian.
- **Interacciones:** con P153 T02 (fuera de este archivo): si se aprueba, el
  criterio puede ser la brecha frente a la línea base definida allí,
  recalculada aquí con la misma definición desde `dashboard_sales`, porque
  P154 no lee artefactos de P153. Si se rechaza, el criterio usa un período
  de referencia dentro de la misma capa. Con P150 T01: mientras el bloque
  conserve el calendario sintético uniforme, todo criterio que compare meses
  señala variaciones del generador, no señales comerciales, y la lectura
  persistida debe decirlo. Si se aprueba la alternativa del generador de
  P150 T01, el criterio pasa a tener un patrón documentado que detectar.
  Capacidad: un solo cambio local en P154; no añade interfaz.
- **Criterio de aceptación:** S05 encuentra (1) un criterio de atención
  explícito, con parámetros aprobados por el profesor, calculado desde
  `dashboard_sales` y que usa la dimensión mes; (2) un artefacto en
  `submission/` con las celdas región–categoría, su valor de referencia, su
  valor actual, la brecha y la marca de atención, más una lectura persistida
  con respuesta y límite; (3) una celda de evidencia que muestra que sumar
  `orders` entre celdas supera los pedidos distintos del hecho, y la regla
  de no aditividad en `serving_manifest.csv`; y (4) pruebas que recalculan
  el criterio y verifican la nota. H01–H04 siguen presentes; H01 y H04
  pierden sus límites actuales.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P154_ventas_dashboard/

0. Inspecciona primero professor/notebook.ipynb, data/sales_mart.db,
   submission/ (cinco archivos, en especial serving_manifest.csv y
   questions.json) y tests/. Calcula la suma de orders en
   dashboard_sales.csv y COUNT(DISTINCT order_id) del hecho. Si la suma no
   supera el conteo distinto, informa que la no aditividad no es observable
   con estos datos (la nota sigue siendo necesaria; la celda de evidencia
   del paso 3 se omite). Si la implementación no coincide con
   design/courses/descriptiva/P154_activity.md, detente e informa.
1. No cambies serving_query, dashboard_sales.csv, bi_serving.db, la
   reconciliación ni priority_region_category.csv.
2. CRITERIO: no inventes el criterio ni sus parámetros. Usa el criterio
   aprobado por el profesor en la discusión de esta T01 (registrado en
   P154_log.md): tipo (cambio del último mes frente a un período de
   referencia, o brecha frente a la línea base de P153 T02 o a una meta),
   medida (net_sales o units_sold, nunca orders sumada), período de
   referencia y umbral o número de celdas señaladas. Si no existe, detente
   y pídelo.
3. NO ADITIVIDAD: añade una celda de evidencia con la suma de orders entre
   celdas frente a COUNT(DISTINCT order_id) del hecho, y 2–3 líneas que
   expliquen que un pedido con líneas de varias categorías se cuenta en
   varias celdas; para totales de pedidos hay que recontar desde el hecho.
4. Calcula el criterio sólo desde dashboard_sales (no desde fact_sales):
   para cada región–categoría, valor de referencia, valor actual, brecha
   (absoluta y relativa) y marca de atención según el umbral. Si el
   criterio usa la línea base de P153 T02, recalcúlala aquí con la misma
   definición sobre dashboard_sales.
5. Grafica la brecha por región–categoría desde el artefacto (barras
   ordenadas, marcando las celdas señaladas) y escribe en markdown, en 3–5
   líneas, qué celdas reciben atención y por qué, en qué se diferencia del
   ranking de volumen y el límite: con el calendario sintético actual la
   variación mensual refleja el generador, no señales comerciales.
6. Persiste:
   - submission/attention_region_category.csv con columnas region,
     category, measure, reference_value, current_value, gap, gap_pct,
     attention (booleano).
   - submission/analysis_conclusions.csv con columnas pregunta, respuesta,
     límite (patrón de descriptiva/P125 H06).
   - serving_manifest.csv con una columna nueva aggregation_rules que diga
     que net_sales y units_sold se suman entre celdas y que orders no se
     suma (se recuenta desde el hecho).
   - questions.json: la pregunta literal existente apunta ahora a
     attention_region_category.csv (conserva la estructura del archivo).
7. Pruebas en tests/test_activity.py, sin eliminar ninguna:
   - Amplía test_01 con los dos archivos nuevos sin quitar los existentes.
   - test_04 se mantiene; añade una comprobación de que aggregation_rules
     menciona orders y la palabra «no».
   - test_05 conserva la pregunta literal y el recálculo de
     priority_region_category.csv.
   - Añade una prueba que recalcula attention_region_category.csv desde
     dashboard_sales.csv con el criterio y los parámetros aprobados, y que
     verifica que analysis_conclusions.csv tiene sus columnas y un límite
     que menciona «sintétic».
   - Si el paso 0 confirmó la sobrecuenta, añade una prueba de que la suma
     de orders en dashboard_sales.csv supera los pedidos distintos de
     data/sales_mart.db.
8. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
9. No construyas una interfaz de dashboard. No modifiques otras
   actividades, traceability.yaml ni design/.
```
