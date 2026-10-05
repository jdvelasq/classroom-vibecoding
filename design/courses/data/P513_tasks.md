# P513 — Propuestas de mejora

**Línea base:** `P513_activity.md` (entrada S02 más reciente: `S02.P513.02`).

## T01 — Verificar tipos y rangos después de leer y conciliar el total de filas de los lotes con la fuente

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 73 y 92 — DG-Data Cleaning incluye la habilidad «Evaluate data quality» (p. 73) y DPSIA/DI-Data corruption and data validation enumera «Validation methods including input validation, data type validation, range and constraint validation, and cross-reference validation» (p. 92): las tres comprobaciones de esta T01 (tipo, rango y conciliación cruzada con la fuente) (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general de validar después de leer.
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` p. 15 — CAP-E.3.5.2 «Identify common issues in data wrangling, such as missing values, duplicates, redundancy, incorrect/mismatched data types, corrupt data, and default data» y CAP-E.3.4.3 «Identify characteristics of lineage, traceability, and version control of data»: el tipo incorrecto es un problema de nivel inicial que el analista debe identificar (Claude, 2026-10-05). Fuente *authoritative*: objetivo de examen de nivel inicial, no temario.
  - `design/benchmarks-md/literature-derived/dataops-06-definition.md` pp. 4 y 9 — «Entradas — Verifica las entradas en cada paso del pipeline» (Conteo, Conformidad, Balance, Verificación de los campos), «Salidas — Verifica los resultados de una operación» (Completitud, Verificación de rango) y tests sobre «tipo de dato» (p. 4); «Se inician por tests simples y se aumenta complejidad» (p. 9) (Claude, 2026-10-05). Fuente *literature-derived*: refuerzo metodológico, no fuente autónoma.
  - `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` p. 4 — tabla de pruebas de «Entradas»: «Verificación de la cantidad de registros», «Validación del tipo de campo», «Validación del rango de valores de un campo», ante la pregunta «¿Están los datos de entrada libres de errores?», y severidad «Error | Detención del pipeline» (Claude, 2026-10-05). Fuente *literature-derived*: contexto metodológico; sustenta que el estado se derive de las comprobaciones.
- **Qué gana el estudiante:** aprender que declarar el formato en la lectura
  no basta: hay que comprobar después de leer que los datos quedaron como se
  esperaba. Hoy P513 lee con `decimal=","` lotes que usan punto decimal, de
  modo que `Sales`, `Profit`, `Discount`, `Unit Price`, `Shipping Cost` y
  similares quedan como texto en Parquet sin que nada lo detecte (corrección
  de S02.P513.02); el reporte marca `status = "SUCCESS"` como constante y la
  suma 1012 + 940 = 1952 no se verifica. Con una verificación mínima por
  lote (tipo numérico de las medidas, `Discount` en [0, 1] como ya exige P500
  H04, `Order Date` interpretable con `%d/%m/%y` y dentro del trimestre que
  nombra el archivo, mismas columnas en ambos lotes) y una conciliación del
  total de filas con la fuente, el defecto se hace visible, obliga a corregir
  la declaración de formato y el estado pasa a ser el resultado de una
  comprobación. Da evidencia propia a `data.C03`, hoy «débil y contradicha».
  **Límite explícito:** esta T01 no resuelve la auditoría de identidad no
  resuelta de P513 (no hay pregunta analítica ni análisis que la ingestión
  habilite); no debe leerse como justificación de conservar la ingestión
  batch por sí misma.
- **Anclas actuales:** H01 (formato declarado en la lectura; el propio
  highlight dice que «el defecto decimal muestra el costo de no verificar
  tipos después de leer»), H02 (descubrimiento por patrón y aterrizaje
  Parquet), H03 (reporte por lote; «su límite es el estado constante»);
  superficies S01 (lotes con punto decimal), S02 (`decimal=","`
  incompatible), S03 (`ingestion_report.csv`) y S04 (prueba de sólo
  existencia). Dependencia «Recibe de P500» (los lotes particionan sus 1952
  líneas).
- **Alternativas menores descartadas:** cambiar sólo `decimal=","` por
  `decimal="."` corrige el síntoma, pero el estudiante no aprende a detectar
  el error, y el próximo formato mal declarado volvería a pasar inadvertido.
  Aclarar el defecto en texto no cambia lo que el taller ejercita.
- **Contrato de no regresión:** se conservan H01–H03, el descubrimiento con
  `glob` ordenado y `assert batches`, `encoding="utf-8-sig"`, el aterrizaje
  Parquet en `temp/raw/` y las columnas actuales de `ingestion_report.csv`
  (`source_name`, `row_count`, `status`, `raw_path`), a las que se añaden
  columnas de verificación. Se sustituye la constante `SUCCESS` por un estado
  derivado y `decimal=","` por la declaración que la verificación muestre
  correcta. La prueba existente se mantiene. No se añaden pregunta, usuario
  ni decisión.
- **Interacciones:** ninguna dentro de P513 (única propuesta). Depende de la
  decisión pendiente sobre la identidad de P513: si se rediseña, se fusiona o
  se retira, las comprobaciones deben migrar al taller resultante. P518
  reutiliza la forma del reporte (fuente, filas, estado, ruta) sin referencia
  explícita; no se toca.
- **Criterio de aceptación:** S05 encuentra en `professor/main.py` una
  verificación por lote, ejecutada después de leer y antes de escribir
  Parquet, de tipos numéricos de las medidas, del rango de `Discount`, de las
  fechas dentro del trimestre del lote y de la igualdad de columnas entre
  lotes; una conciliación del total de filas con la fuente; un `status`
  derivado de esas comprobaciones; y la lectura corregida. Debe estar
  respaldado por `ingestion_report.csv` con columnas de verificación, un
  archivo de conciliación en `submission/` y pruebas. Un highlight nuevo o
  modificado de H03 recoge el estado derivado; H01 se actualiza para decir
  que la declaración de formato se verifica. H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P513_superstore_batch/

0. Inspecciona primero professor/main.py, src/main.py,
   data/superstore_orders_2015_q*.csv, data/source_manifest.json,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/data/P513_activity.md, detente e informa sin modificar
   nada. Lee los lotes con la declaración actual y confirma que las columnas
   numéricas quedan como texto; si ya quedan numéricas, detente e informa
   (el defecto no existiría). Revisa el bloque format y si el manifiesto
   declara el total de filas de la fuente.
1. No cambies el descubrimiento con glob, utf-8-sig, el aterrizaje Parquet
   en temp/raw/ ni las columnas actuales del reporte.
2. VERIFICACIÓN POR LOTE: añade en professor/main.py una función que, para
   un DataFrame leído y el nombre del lote, devuelva un diccionario de
   comprobaciones booleanas:
   a. types_ok: las columnas de medida (al menos Sales, Profit, Discount,
      Unit Price, Shipping Cost, Quantity Ordered New si existe; confirma
      los nombres en el paso 0) tienen dtype numérico;
   b. discount_in_range: Discount entre 0 y 1 (regla ya usada en P500);
   c. dates_in_batch_period: Order Date se interpreta con format="%d/%m/%y"
      sin nulos y todas las fechas caen en el trimestre que nombra el
      archivo;
   d. columns_match: las columnas coinciden con las del primer lote.
   No inventes otras reglas de rango; si quieres añadir una, debe estar
   respaldada por los datos o por una regla ya presente en el curso.
3. CORRECCIÓN: corrige la declaración decimal según lo que muestra la
   verificación (punto decimal en los lotes) y, si el manifiesto declara un
   separador decimal distinto, informa la contradicción en vez de editar el
   manifiesto.
4. ESTADO DERIVADO: status = "SUCCESS" sólo si todas las comprobaciones del
   lote son verdaderas; en otro caso "FAILED" y ese lote no se escribe en
   temp/raw/. Añade las columnas types_ok, discount_in_range,
   dates_in_batch_period y columns_match a ingestion_report.csv. Si algún
   lote falla, escribe el reporte y termina con error (detención).
5. CONCILIACIÓN: compara la suma de row_count de los lotes con el total de
   la fuente. Usa el total declarado en source_manifest.json si existe; si no,
   declara en main.py una constante con el total de la fuente (1952 líneas
   del extracto datalabs/commerce/superstore-orders.csv, el mismo que lee
   P500) y un comentario breve con ese origen. Persiste
   submission/ingestion_reconciliation.csv con columnas batches,
   batch_rows_total, source_rows, match.
6. Añade a tests/ pruebas que verifiquen: ingestion_report.csv tiene las
   columnas nuevas y status coherente con ellas en cada fila;
   ingestion_reconciliation.csv tiene match verdadero. Las pruebas deben ser
   independientes de la profundidad del taller en la distribución. No
   elimines la prueba existente.
7. Ejecuta professor/main.py y las pruebas de la actividad sin errores.
8. No añadas pregunta analítica, usuario ni decisión (decisión de identidad
   pendiente). No modifiques otras actividades (P500, P518 incluidas),
   traceability.yaml ni design/.
```
