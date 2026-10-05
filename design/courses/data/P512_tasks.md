# P512 — Propuestas de mejora

**Línea base:** `P512_activity.md` (entrada S02 más reciente: `S02.P512.02`).

## T01 — Derivar el modelo dimensional de las preguntas (matriz pregunta–medida–dimensión–grano), conservar `Order ID` como dimensión degenerada, declarar qué medidas son aditivas y verificar que el mart reproduce `order_count` de P500

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` pp. 5, 7, 10–11 y 18 — «The grain declaration becomes a binding contract on the design» (p. 5); «some measures are completely non-additive, such as ratios. A good approach for nonadditive facts is, where possible, to store the fully additive components» (p. 7); el número de factura sigue siendo una clave válida a grano línea: «This degenerate dimension is placed in the fact table with the explicit acknowledgment that there is no associated dimension table» (pp. 10–11); en esquemas cabecera/línea «all the header-level dimension foreign keys and degenerate dimensions should be included on the line-level fact table» (p. 18). Sustenta conservar `Order ID` en el hecho y declarar la aditividad de cada medida (Claude, 2026-10-05). Fuente *authoritative*: respalda el principio de diseño, no un temario de data warehouse.
  - `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` pp. 14, 30–31 y 53 — el modelo se deriva de «What business questions are being answered?» y «How are records identified & how are tables related?» (p. 14); los requisitos se escriben como preguntas («What is the Sales Amount grouped by Year or Month or Day…», p. 30) y se traducen en una «DIMENSIONAL MATRIX» de hechos × dimensiones (p. 31) que se amplía cuando cambian las preguntas (p. 53) (Claude, 2026-10-05). Fuente *professional-learning*: ilustra la práctica de la matriz; la materialidad la sostienen los defectos registrados por S02.
- **Qué gana el estudiante:** derivar un esquema de datos de requisitos
  analíticos (`data.C01`) y comprobar que el esquema los cumple, en lugar de
  construir un mart a partir de las tablas disponibles. Hoy el mart omite
  `orders`: `fact_sales` no tiene `Order ID` y la métrica `order_count` de
  P500 (y con ella `average_order_value`) no es reconstruible, límite que S02
  registró. Con una matriz breve que lista, para preguntas que ya existen en
  el curso, la medida, su regla de agregación, las dimensiones y el grano
  requeridos, el estudiante ve antes de construir que contar órdenes exige
  una clave de orden a grano línea; la resuelve conservando `Order ID` como
  dimensión degenerada (no como dimensión de orden: en P511 H01 `Order ID`
  no es clave de `orders`, p. ej. `86838` con dos `Ship Date`); declara que
  ventas y utilidad son aditivas, que las órdenes distintas no se suman entre
  meses o categorías y que el valor promedio por orden se calcula como
  cociente de componentes en el grano atómico; y verifica que el mart
  reproduce `order_count` mensual de P500. Corrige un defecto real (el mart
  no responde una métrica ya definida en el curso) y hace explícito el
  contraste aditivo/no aditivo que hoy sólo está implícito en P500 H02.
  **Foco de la propuesta:** requisitos de datos (grano, claves,
  reconstructibilidad), no diseño de BI. Ni la matriz ni el mart deben
  crecer hacia medidas de tablero, jerarquías o visualización.
- **Anclas actuales:** H01 (dimensión de fecha; la unión `many_to_one` con
  `orders` que ya usa es el punto donde se toma `Order ID`), H02 (hecho a
  grano línea separado de dimensiones), H03 (mart persistido y consulta en
  estrella); superficies S02 (sin dimensión de orden), S03 (mart sin
  restricciones; consulta no persistida) y S04 (pruebas de sólo existencia);
  dependencia «Recibe de P511» (tablas y manifiesto, S01). Referencia de
  conciliación: P500 H02 (fórmulas derivadas del grano línea). Auditoría:
  «C01 sólo en la pregunta de organización» y pregunta 5 (lectura como taller
  de modelado dimensional).
- **Alternativas menores descartadas:** declarar en markdown que
  `order_count` no es reconstruible deja el defecto y no ejercita C01.
  Añadir sólo `Order ID` al hecho corrige el síntoma, pero el estudiante no
  aprende a detectar desde las preguntas qué columna falta ni por qué una
  cuenta distinta no se suma. Añadir una dimensión `dim_order` completa
  enseñaría algo incorrecto en este caso, porque `Order ID` no identifica una
  fila única de `orders`.
- **Contrato de no regresión:** se conservan H01–H03, la pregunta actual, las
  cuatro tablas de S01 y su manifiesto, `dim_date`, `dim_customer`,
  `dim_product`, la aserción `len(fact_sales) == len(order_lines)`, la
  consulta año × mes × categoría y `submission/superstore_mart.db` con sus
  cuatro tablas. `fact_sales` gana una columna (`Order ID`); ninguna columna
  existente se elimina ni se renombra. La prueba existente se mantiene. No se
  rehace `dim_date` como calendario completo (señal marginal en ambas
  fuentes; fuera de esta T01).
- **Interacciones:** ninguna dentro de P512 (única propuesta). Frontera con
  otros cursos: BI pertenece a descriptiva y `descriptiva/P150`–`P154`
  también construyen un mart; **posible duplicación con `descriptiva/P151`,
  a discutir en el curso** antes de aprobar. Si la discusión concluye que el
  modelado dimensional como tal pertenece a descriptiva, esta T01 sigue
  teniendo objeto sólo en su parte de requisitos de datos (matriz, clave
  degenerada, conciliación con P500); si P512 se fusiona o retira, la
  conciliación con P500 debe migrar al taller resultante. P511, P514 y P515
  comparten S01 y no se tocan.
- **Criterio de aceptación:** S05 encuentra (1) en el notebook, antes de
  construir las tablas, una matriz pregunta–medida–dimensión–grano para las
  preguntas existentes de P512, P511 y P500, persistida en `submission/`, con
  la aditividad de cada medida declarada; (2) `Order ID` en `fact_sales` del
  mart, sin dimensión asociada y sin cambio en el número de filas; (3) una
  consulta persistida que reproduce, mes a mes, el `order_count` de P500 con
  `COUNT(DISTINCT "Order ID")`, con una columna de coincidencia en `True` para
  todos los meses; y (4) pruebas que verifican la matriz, la columna y la
  conciliación. Un highlight nuevo o modificado de H02 recoge la clave
  degenerada y la aditividad. H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P512_superstore_warehouse/

0. Inspecciona primero professor/notebook.ipynb, data/*.csv,
   data/source_manifest.json, submission/superstore_mart.db y tests/. Si la
   implementación no coincide con design/courses/data/P512_activity.md,
   detente e informa sin modificar nada. Confirma que orders.csv contiene
   Order ID y order_context_key, que order_lines.csv contiene
   order_context_key y que la unión many_to_one con orders de H01 existe.
   Inspecciona también, sólo para leer valores,
   implementation/data/P500_superstore_metricas/submission/
   monthly_sales_metrics.csv y anota month y order_count. Si P500 no expone
   order_count por mes, detente e informa.
1. No cambies la pregunta, las tablas de data/, el manifiesto, dim_date,
   dim_customer, dim_product, la aserción de filas ni la consulta año × mes
   × categoría.
2. MATRIZ DE REQUISITOS: al inicio del notebook, después de la pregunta,
   añade una celda que construya un DataFrame con una fila por par
   pregunta–medida y columnas question_id, source_activity, question,
   measure, aggregation, additivity (additive | non_additive | ratio_of_
   components), dimensions, grain, required_columns. Usa sólo preguntas que
   ya existen en el curso, con su texto literal: la de P512, la de P511
   (segmento, región, categoría) y la de P500 (ventas, utilidad, número de
   órdenes y valor promedio por orden por mes). No inventes preguntas,
   usuarios ni decisiones. Persístela en submission/requirements_matrix.csv.
   Añade 2–4 líneas en markdown que señalen qué columna exigida por la
   matriz no estaría en el mart actual (Order ID) y por qué una cuenta
   distinta de órdenes no puede sumarse entre meses o categorías.
3. CLAVE DEGENERADA: en la unión many_to_one existente con orders (H01),
   conserva Order ID en fact_sales. No crees dim_order. Mantén la aserción
   len(fact_sales) == len(order_lines). Explica en markdown, en 2–3 líneas,
   por qué Order ID queda en el hecho sin tabla de dimensión (en orders.csv
   no es única: ver el manifiesto y P511).
4. CONCILIACIÓN: con una consulta SQL sobre superstore_mart.db
   (fact_sales JOIN dim_date) calcula por año-mes COUNT(DISTINCT "Order ID")
   y, como cociente de componentes, SUM(Sales) / COUNT(DISTINCT "Order ID").
   Compara order_count con los valores de P500 anotados en el paso 0,
   escritos en el notebook como referencia explícita con su origen (no leas
   archivos de otra actividad en tiempo de ejecución: el taller se distribuye
   por separado). Persiste submission/order_metrics_check.csv con columnas
   month, order_count_mart, order_count_p500, average_order_value_mart,
   match. Si algún mes no coincide, detente e informa la diferencia; no
   ajustes datos ni la definición para forzar la coincidencia.
5. Añade a tests/ pruebas que verifiquen: requirements_matrix.csv existe
   con las columnas del paso 2 y al menos una fila non_additive;
   fact_sales en superstore_mart.db tiene la columna Order ID y el mismo
   número de filas que order_lines; order_metrics_check.csv tiene match
   verdadero en todas las filas. Las pruebas deben ser independientes de la
   profundidad del taller en la distribución. No elimines la prueba
   existente.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades (P500, P511, P514, P515 incluidas),
   traceability.yaml ni design/. No añadas medidas de tablero, jerarquías,
   calendario completo ni visualizaciones.
```
