# P514 — Propuestas de mejora

**Línea base:** `P514_activity.md` (entrada S02 más reciente: `S02.P514.02`).

## T01 — Probar el balance por etapa en un grano comparable y derivar el estado del resultado de las pruebas

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` pp. 4–5 — «Location Balance tests | Las propiedades de los datos se mantienen en cada etapa. La cantidad de datos o sus dimensiones se mantienen» (p. 5); «Los tests deben incluirse en cada etapa del pipeline», «Se debe identificar los problemas tan pronto como se posible [sic]» y severidad «Error | Detención del pipeline» (p. 4) (Claude, 2026-10-05). Fuente *literature-derived*: perspectiva metodológica; la materialidad la sostiene el defecto de granos mezclados que registró S02.
- **Qué gana el estudiante:** comprobar que un proceso por etapas conserva
  el grano y los totales de la fuente hasta la respuesta, y saber que una
  comparación de conteos sólo tiene sentido en el mismo grano. Hoy
  `pipeline_report.csv` suma en raw cuatro tablas de grano distinto
  (1857 órdenes + 1191 contextos de cliente + 926 contextos de producto +
  1952 líneas = 5926) y lo pone en la misma columna que las 1952 líneas de
  staging y curated, sin declararlo; staging y curated son el mismo
  DataFrame escrito dos veces; y `status` es la constante `SUCCESS`. Con una
  prueba de balance en el grano línea (líneas de `order_lines` en raw =
  líneas en staging = líneas en curated; suma de `Sales` y `Profit` de las
  líneas raw = suma del detalle curado = suma de la respuesta segmento ×
  región) y con el grano de cada tabla raw declarado en lugar de sumado, el
  estudiante obtiene una evidencia que hoy no existe: que la respuesta
  conserva el grano y los totales de la fuente. El estado pasa a ser el
  resultado de esa prueba. Es la evidencia que la auditoría de P514 pide
  («hasta que la etapa añada una evidencia o decisión analítica distinta»),
  aunque por sí sola no la resuelve.
- **Anclas actuales:** H01 (etapas `extract`/`transform`/`publish`; límite
  staging = curated), H02 (reporte de filas por etapa en granos distintos);
  superficies S02 (`professor/main.py`), S03 (`pipeline_report.csv` y demás
  artefactos de `submission/`) y S04 (pruebas de sólo existencia);
  dependencias «Recibe de P511» (cadena de uniones validadas) y «Habilita
  para P515» (forma de reporte `stage/rows/status`).
- **Alternativas menores descartadas:** declarar en markdown que 5926 no es
  comparable con 1952 hace visible el defecto pero no da una prueba de
  conservación. Añadir más pruebas genéricas por etapa sin fijar el grano
  repetiría la mezcla.
- **Contrato de no regresión:** se conservan H01, las tres funciones, los
  directorios raw/staging/curated, la cadena de uniones validadas y
  aserciones heredadas de P511, la pregunta, `questions.json`,
  `superstore_enriched_sales.csv` y `sales_by_segment_region.csv` con su
  esquema actual. H02 se sustituye por una versión que corrige la mezcla de
  granos: `pipeline_report.csv` conserva las columnas `stage`, `rows` y
  `status` y añade columnas de grano y de totales; la fila raw que sumaba
  5926 se reemplaza por filas por tabla con su grano declarado. La prueba
  existente se mantiene. No se intenta diferenciar staging de curated (fuera
  de esta T01).
- **Interacciones:** ninguna dentro de P514 (única propuesta).
  **Duplicación registrada por S02:** P514 y P515 duplican el producto de
  P511 (mismo detalle, misma respuesta que P515) y la decisión de curso está
  pendiente. Conviene decidir primero si P514 se conserva, se fusiona con
  P515 o se retira; si se fusiona o se retira, esta T01 pierde objeto o debe
  migrar al taller resultante. P515 hereda la forma de reporte
  `stage/rows/status`: si se aprueba esta T01 y P515 se conserva, su reporte
  quedaría con la forma anterior (una variante equivalente para P515 se
  descartó como propuesta separada y debe decidirse con la duplicación).
  Riesgo de identidad: más pruebas por etapa acercan P514 a un ejercicio de
  Data Engineering; la propuesta sólo se justifica si la prueba se presenta
  como garantía de la respuesta analítica, no como práctica de pipeline.
- **Criterio de aceptación:** S05 encuentra en `professor/main.py` una
  prueba de balance en grano línea entre raw, staging, curated y la
  respuesta (filas y sumas de `Sales` y `Profit`, con tolerancia de redondeo
  declarada), un `status` derivado de ella y un `pipeline_report.csv` que ya
  no suma granos distintos y declara el grano de cada fila; respaldado por
  pruebas. H02 queda reescrito en esos términos; H01 sigue presente.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P514_superstore_etl/

0. Inspecciona primero professor/main.py, src/main.py, data/*.csv,
   data/source_manifest.json, submission/ y tests/. Si la implementación no
   coincide con design/courses/data/P514_activity.md (en particular, si
   pipeline_report.csv no registra raw 5926 / staging 1952 / curated 1952
   con status constante), detente e informa sin modificar nada.
1. No cambies las funciones extract/transform/publish en lo que ya hacen,
   la cadena de merges con validate="many_to_one", las aserciones heredadas,
   la pregunta, questions.json ni el esquema de
   superstore_enriched_sales.csv y sales_by_segment_region.csv.
2. GRANO DECLARADO: en el reporte, reemplaza la fila raw que suma las cuatro
   tablas por una fila por tabla raw (orders, customers, products,
   order_lines) con su grano declarado en una columna grain (por ejemplo
   order_context, customer_context, product_context, order_line; confirma
   los nombres con el manifiesto). Las filas staging y curated declaran
   grain = order_line. Añade una fila answer para
   sales_by_segment_region (grain = segment_region).
3. PRUEBA DE BALANCE: añade una función que compare, en grano línea:
   a. filas de order_lines raw = filas staging = filas curated;
   b. suma de Sales y de Profit de order_lines raw = suma en curated = suma
      en la respuesta segmento × región, con una tolerancia de redondeo
      explícita (por ejemplo math.isclose con abs_tol=0.01), porque las sumas
      flotantes difieren en la última cifra (ver P515).
   Añade al reporte columnas sales_total, profit_total y balance_ok (vacías
   o no aplicables en las tablas raw que no son de grano línea).
4. ESTADO DERIVADO: status = "SUCCESS" sólo si balance_ok es verdadero para
   las filas de grano línea y la respuesta; en otro caso "FAILED". Si falla,
   escribe el reporte y termina con error.
5. Añade a tests/ pruebas que verifiquen: pipeline_report.csv tiene la
   columna grain, ninguna fila suma tablas de grano distinto, las filas de
   grano order_line tienen el mismo rows, balance_ok es verdadero y status
   coincide con él. Las pruebas deben ser independientes de la profundidad
   del taller en la distribución. No elimines la prueba existente.
6. Ejecuta professor/main.py y las pruebas de la actividad sin errores.
7. No modifiques P511, P515 ni otras actividades, traceability.yaml ni
   design/. No intentes diferenciar staging de curated.
```
