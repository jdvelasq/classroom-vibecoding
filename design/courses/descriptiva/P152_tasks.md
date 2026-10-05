# P152 — Propuestas de mejora

**Línea base:** `P152_activity.md` (entrada S02 más reciente: `S02.P152.02`).

## T01 — Persistir la lectura de la navegación OLAP: qué medida define al líder, por qué se corta en Norte y qué significa «explican»

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 39, 46 y 75 — al presentar resultados, el graduado debe «explain and interpret the numerical conclusions in the client’s terminology» (p. 39); AP-Visualization incluye «Inference based on visualization» e «Implement an effective visualization, given a set of data that has to be used for a particular purpose» (p. 46); DM-Proximity, «Use of scores and rankings; desirable characteristics of scores and ranking regimes» (p. 75): un ranking depende de la medida que lo ordena y su lectura debe hacerse explícita (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa de interpretar, no un formato.
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` pp. 20–21 — CAP-P.5.3.1 «Identify the correct interpretation of a descriptive/diagnostic analytics model output» (p. 20); Task 5.6 «Document and communicate model findings, including assumptions, limitations, and constraints» y CAP-P.5.6.1 «the most appropriate non-technical explanation of the results» (p. 21) (Claude, 2026-10-04). Fuente *authoritative*.
  - `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` pp. 96 y 219 — la competencia de pensamiento analítico del analista de datos/BI es «Formular preguntas correctas, encontrar patrones, interpretar métricas y KPIs» (p. 219), y «Storytelling con datos» y «Presentación de informes» figuran como habilidades de «Comunicación analítica» (p. 96) (Claude, 2026-10-04). Fuente *governmental*: aporta sólo pertinencia laboral; la materialidad descansa en el defecto observado.
- **Qué gana el estudiante:** entender que «liderar» depende de la medida que
  ordena el ranking, declarar cuál guía la navegación y escribir qué
  significa cada respuesta y qué no significa. Hoy el *slice* de Norte
  muestra que Servicios lidera ventas netas (92853.0) y Oficina lidera
  unidades (180), pero el notebook no lo comenta (H03, límite). El
  *drill-down* toma en silencio la primera fila ordenada por ventas netas
  (H04). El corte en Norte no tiene criterio (S02) y «explican» se responde
  como descomposición aditiva sin advertir que no es causa. No hay
  conclusión escrita (S03). P152 es, según S02, la actividad del bloque más
  cercana a la pregunta descriptiva; sin lectura persistida, el producto se
  reduce a tres consultas correctas. Con el cambio, el estudiante pasa de
  tablas a afirmaciones con evidencia y límite.
- **Anclas actuales:** H03 (contraste de medidas en el *slice*; límite «el
  notebook no lo hace explícito»), H04 (*drill-down* encadenado a la
  primera fila), H02 (*roll-up* reconciliado, cuya serie mensual hereda el
  calendario uniforme); superficies S02 (consultas; Norte sin criterio), S03
  (producto y preguntas sin conclusión) y S04 (pruebas `test_01`–`test_05`).
- **Alternativas menores descartadas:**
  - Sólo una celda markdown: no deja evidencia persistida ni verificable.
  - Cambiar el corte a una región elegida por un criterio, o añadir el
    contraste de líderes para todas las regiones: cambiaría consultas,
    artefactos y pruebas (`test_03`, `test_04`) para algo que una lectura
    declarada ya resuelve. Se descarta.
  - Hacer un segundo *drill-down* por unidades: duplicaría la consulta; basta
    con nombrar en la lectura hacia dónde iría la navegación con la otra
    medida.
- **Contrato de no regresión:** se conservan H01–H04, las tres consultas
  (*roll-up*, *slice* en Norte, *drill-down* parametrizado), la
  reconciliación del total, los cuatro artefactos actuales con su esquema y
  `test_02`–`test_05`. No cambia el corte ni la medida que guía el
  *drill-down*; se hace explícita. Se añade un artefacto de lectura y su
  prueba; `test_01` se amplía con ese archivo.
- **Interacciones:** ninguna dentro de P152. Depende de P150 T01 sólo en la
  redacción del límite del *roll-up*: si el bloque conserva el calendario
  sintético, la lectura de la serie mensual por región debe declarar que no
  admite lectura estacional. Si se aprueba la alternativa del generador de
  P150 T01, los valores citados aquí cambian y la lectura debe redactarse
  con los nuevos.
- **Criterio de aceptación:** S05 encuentra (1) antes del *drill-down*, una
  celda que muestra los dos rankings del *slice* y declara qué medida define
  al líder, por qué, y hacia qué categoría iría la navegación con la otra
  medida; (2) una justificación del corte en Norte aportada por el profesor
  o, si no existe, la declaración explícita de que es un corte ilustrativo
  sin criterio de selección; (3) `submission/olap_reading.csv` con una fila
  por pregunta (respuesta, evidencia, límite), donde el límite del
  *drill-down* dice que es descomposición aditiva y no causa; y (4) una
  prueba que lo verifica derivando los líderes del archivo entregado.
  H01–H04 siguen presentes y H03 deja de tener el límite «no explícito».

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P152_ventas_olap/

0. Inspecciona primero professor/notebook.ipynb, data/sales_mart.db,
   submission/ (cuatro archivos) y tests/. Verifica en
   submission/north_category_sales.csv que el líder por ventas netas y el
   líder por unidades son categorías distintas. Si coinciden, detente e
   informa: la divergencia que motiva la propuesta no existiría. Si la
   implementación no coincide con
   design/courses/descriptiva/P152_activity.md, detente e informa.
1. No cambies las consultas, el corte en Norte, la medida de orden del
   drill-down, la reconciliación ni los cuatro artefactos actuales.
2. Entre el slice y el drill-down, añade «¿Qué categoría lidera?»:
   a. Celda de evidencia: el slice ordenado por net_sales y por units (dos
      tablas pequeñas o una con ambos rangos).
   b. Markdown de 3–5 líneas: el líder depende de la medida; el drill-down
      sigue ventas netas porque <razón>; con unidades bajaría a <categoría
      líder por unidades>. Toma ambas categorías del artefacto, no las
      escribas a mano en el código.
   c. <razón>: usa la justificación aprobada por el profesor en la
      discusión de esta T01 (registrada en P152_log.md). Si no existe,
      decláralo como convención del taller («se sigue el valor monetario;
      no hay una decisión de negocio que lo justifique») y no inventes una
      razón comercial.
3. Antes del slice, añade 1–3 líneas sobre el corte en Norte con la
   justificación aprobada por el profesor; si no existe, declara que es un
   corte ilustrativo sin criterio de selección.
4. Persiste submission/olap_reading.csv con columnas pregunta, respuesta,
   evidencia, límite; una fila por cada pregunta de questions.json, con el
   texto literal de la pregunta. Contenido mínimo:
   - roll-up: límite = el calendario es sintético y uniforme; la variación
     mensual no admite lectura estacional (ajústalo si P150 T01 cambió el
     generador).
   - slice: la respuesta nombra al líder por ventas netas y al líder por
     unidades; límite = «liderar» depende de la medida; Norte es <criterio o
     corte ilustrativo>.
   - drill-down: límite = descomposición aditiva de las ventas netas de la
     categoría; no identifica causas.
5. Pruebas en tests/test_activity.py, sin eliminar ninguna:
   - Amplía test_01 para incluir olap_reading.csv sin quitar los cuatro
     archivos existentes.
   - Añade una prueba que exige las columnas, una fila por pregunta de
     questions.json, que la respuesta del slice contenga las dos categorías
     líderes derivadas de north_category_sales.csv (por net_sales y por
     units) y que el límite del drill-down contenga «aditiv» y «caus».
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades, traceability.yaml ni design/.
```

## T02 — Comparar períodos en la navegación OLAP: mes anterior, mismo mes del año anterior y acumulado del año

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` p. 19 — «Business users often request year-to-date (YTD) values… A more reliable, extensible way to handle these assorted requests is to calculate the YTD metrics in the BI applications or OLAP cube rather than storing YTD facts in the fact table» (Claude, 2026-10-04). Fuente *authoritative*: ubica las comparaciones temporales en la capa de consulta, que es la de P152.
  - `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` pp. 30, 74 y 76 — requisito de reporte: una serie que permita elegir «Month Over Month, Month Over Month % Change, Month To Date, Prior Month, Year To Date» a lo largo de años, meses o días; grupo de cálculo de *time intelligence* con «Current», «MoM %» y «YoY %» (Claude, 2026-10-04). Fuente *professional-learning*: señal de práctica; el mecanismo se enseña en SQL/pandas, no en la plataforma.
- **Qué gana el estudiante:** responder la pregunta más frecuente de un
  usuario de BI, «¿cómo vamos frente al período anterior?», sobre el mismo
  hecho que ya navega. Hoy P152 sube a año–mes–región (H02), corta en Norte
  (H03) y baja a productos (H04), pero ninguna consulta compara un período
  con otro: no hay variación frente al mes anterior, frente al mismo mes del
  año anterior ni acumulado del año. Con el cambio, el estudiante construye
  esas comparaciones en la capa de consulta (funciones de ventana o
  desplazamientos sobre una serie mensual completa), entiende por qué el
  acumulado se calcula al consultar y no se guarda en el hecho, y aprende que
  una variación porcentual sobre una base pequeña o ausente debe tratarse
  explícitamente.
- **Anclas actuales:** H01 (jerarquía año→mes de `dim_date`), H02 (*roll-up*
  reconciliado contra el total del hecho); superficies S02 (consultas OLAP),
  S03 (producto y preguntas) y S04 (pruebas que reejecutan consultas sobre
  `data/sales_mart.db`).
- **Alternativas menores descartadas:** describir en markdown qué es una
  comparación interanual no hace que el estudiante la calcule ni que trate
  meses ausentes o bases cero.
- **Contrato de no regresión:** se conservan H01–H04, las tres consultas, sus
  CSV, el gráfico, la reconciliación y las pruebas actuales. La comparación
  se añade como cuarta consulta con su propio artefacto. Si un período no
  tiene ventas, la serie lo muestra en cero (no lo omite).
- **Interacciones:** con T01 (lectura persistida): la lectura de T01 puede
  incorporar la comparación de períodos; ambas deben ejecutarse juntas para
  no reescribir la misma celda dos veces. Con P151 T01 (fuera de este
  archivo): P152 lee `data/sales_mart.db`, cuyo `dim_date` sólo tiene días con
  ventas; esta T02 construye su propia serie mensual completa a partir del
  rango del hecho y no depende de que P151 T01 cambie el mart de referencia.
  Con P150 T01: mientras el calendario sintético sea uniforme, toda variación
  entre meses es ruido del generador; la lectura debe decirlo, y la
  comparación cobra sentido descriptivo sólo si se aprueba la alternativa
  del generador. Capacidad: P152 queda con dos propuestas; T02 puede ser la
  sección final que un grupo lento complete en la sesión siguiente.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo con ventas
  netas mensuales por región acompañadas de variación frente al mes
  anterior, frente al mismo mes del año anterior (si el rango cubre más de un
  año; si no, se declara) y acumulado del año, con meses sin ventas en cero y
  bases cero tratadas explícitamente, respaldado por notebook, un CSV en
  `submission/` y una prueba que recalcule el acumulado.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P152_ventas_olap/

0. Inspecciona primero professor/notebook.ipynb, data/sales_mart.db,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/descriptiva/P152_activity.md, o si ya calcula
   comparaciones entre períodos, detente e informa. Comprueba el rango de
   fechas del hecho: si cubre menos de 13 meses, omite la comparación
   interanual y decláralo.
1. No cambies las tres consultas existentes, sus CSV, el gráfico ni las
   pruebas actuales.
2. Añade «Comparación de períodos» después del roll-up:
   a. Construye la serie mensual por región con todos los meses del rango
      del hecho (meses sin ventas en 0).
   b. Calcula con SQL de ventana (LAG, SUM OVER PARTITION BY año) o con
      pandas: ventas del mes anterior, variación absoluta y porcentual
      frente al mes anterior, variación frente al mismo mes del año anterior
      y acumulado del año.
   c. Cuando la base sea 0, deja la variación porcentual vacía y explica por
      qué.
   d. Grafica el acumulado del año por región.
   e. Explica en markdown, en 3–5 líneas, por qué el acumulado se calcula al
      consultar y no se guarda en el hecho, y qué limita leer variaciones
      sobre este calendario sintético.
3. Persiste submission/period_comparison.csv con columnas year, month,
   region, net_sales, prev_month_net_sales, mom_change, mom_pct,
   yoy_change, ytd_net_sales.
4. Actualiza tests/: amplía la lista de archivos esperados con
   period_comparison.csv (sin quitar ninguno) y añade una prueba que
   reconstruya ytd_net_sales desde data/sales_mart.db y verifique que la
   suma de net_sales coincide con el total del hecho. No elimines pruebas
   existentes.
5. Ejecuta el notebook completo y las pruebas sin errores.
6. No modifiques otras actividades, traceability.yaml ni design/.
```
