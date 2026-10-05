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
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` pp. 21 y 26 — en la verificación de calidad de CRISP-DM: «Are the data stored in flat files? If so, are the delimiters consistent among files? Does each record contain the same number of fields?» (p. 21); «Appending data involves integrating two or more data sets with similar attributes but different records» y, tras integrar, se explora «to make sure that the data merge was performed correctly» (p. 26) (Claude, 2026-10-05). Fuente *professional-learning*: práctica de verificación de lotes anexados.
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

## T02 — Plantear la pregunta analítica que resuelve el procesamiento y mostrar cómo lo resuelve

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - Decisión del profesor en la entrevista del 2026-10-05, registrada en `design/courses/data/P500_log.md` (`Nota.P500.02`) (Claude, 2026-10-05). No proviene de un benchmark.
- **Qué gana el estudiante:** ver la ingestión por lotes como se hace
  profesionalmente: se recibe una fuente fragmentada por periodo para
  responder algo, y la respuesta se obtiene de lo que la ingestión dejó, no
  de los archivos de origen. Hoy P513 no declara pregunta, usuario ni
  decisión (S02: «Pregunta, usuario o decisión: no evidenciados»; S05 «Stub
  sin enunciado; ninguna pregunta analítica»), y la auditoría sigue no
  resuelta porque «no hay finalidad analítica declarada» (S02.P513.03). Con
  esta T02, el estudiante enuncia la pregunta antes de procesar, la responde
  leyendo de vuelta la zona raw en Parquet, persiste la respuesta ligada a
  la pregunta y escribe su lectura y su límite. Además comprueba en la
  práctica que una respuesta sobre columnas numéricas sólo es posible si la
  ingestión conservó los tipos (el defecto de `decimal=","` que corrige
  T01).
  **Pregunta sugerida (sólo sugerencia; requiere la redacción aprobada por
  el profesor):** «¿Cuánto cambiaron las ventas (`Sales`) y la utilidad
  (`Profit`) del segundo trimestre de 2015 frente al primero, según los dos
  lotes recibidos?». Se apoya en lo que S02 describe: dos lotes trimestrales
  de `Order Date` (`superstore_orders_2015_q1.csv`, 1012 filas;
  `superstore_orders_2015_q2.csv`, 940) aterrizados por lote en
  `temp/raw/*.parquet`; la respuesta es un total por lote y su variación. No
  se propone usuario ni decisión más allá de esta sugerencia.
  **Límite explícito:** esta T02 cierra el límite «sin pregunta analítica»
  que registró S02 sólo una vez ejecutada y verificada por S05; aprobarla no
  lo cierra.
- **Anclas actuales:** H02 (lotes aterrizados en Parquet, de donde se lee la
  respuesta), H03 (reporte por lote, con el que la respuesta se concilia) y
  H01 (formato declarado en la lectura, del que depende que las medidas sean
  numéricas); superficies S02 (`professor/main.py`), S03 (producto en
  `submission/`), S04 (prueba de sólo existencia) y S05 («ninguna pregunta
  analítica»). Dependencia «Recibe de P500» (caso Superstore y patrón
  `questions.json` de P500–P508), sin cambios.
- **Alternativas menores descartadas:** escribir la pregunta sólo como
  comentario o docstring hace visible una intención, pero no muestra cómo el
  procesamiento la resuelve ni deja evidencia verificable. Responderla
  leyendo de nuevo los CSV de `data/` evitaría la ingestión que el taller
  enseña; la respuesta debe salir de la zona raw.
- **Contrato de no regresión:** se conservan H01–H03, el descubrimiento con
  `glob` ordenado y `assert batches`, `encoding="utf-8-sig"`, el aterrizaje
  Parquet en `temp/raw/`, `ingestion_report.csv` con sus columnas (y las que
  añada T01) y la prueba existente (y las que añada T01). Se añaden la
  pregunta al inicio de `professor/main.py`, `submission/questions.json`,
  `submission/analysis_answer.csv`, una lectura breve con su límite y una
  prueba. No cambian los datos, el manifiesto ni las herramientas.
- **Interacciones:** depende de T01. T01 corrige la lectura decimal y hace
  que las medidas lleguen numéricas a Parquet; sin ella, `Sales` y `Profit`
  quedan como texto y no hay respuesta numérica válida. Orden de ejecución:
  T01 primero, después T02. Si sólo se aprueba T02, S04 debe detenerse en el
  paso 0 cuando las medidas sigan como texto, sin corregir la lectura dentro
  de T02. El paso 8 de T01 («No añadas pregunta analítica, usuario ni
  decisión») limita a T01 por sí misma; si se aprueban ambas, la pregunta la
  añade T02 tras T01. Esta T02 también responde a la «decisión pendiente
  sobre la identidad de P513» que T01 menciona: es el camino que el profesor
  fijó en `Nota.P500.02` (dar al taller una pregunta que el procesamiento
  resuelve), sin rediseñar, fusionar ni retirar la actividad. Capacidad: es
  un cálculo pequeño sobre los Parquet ya escritos y no cambia el caso.
- **Criterio de aceptación:** S05 encuentra (1) al inicio de
  `professor/main.py` la pregunta con la redacción aprobada por el profesor,
  idéntica a la registrada en `P513_log.md`; (2) `submission/questions.json`
  que liga esa pregunta con `analysis_answer.csv`, con la misma estructura
  de claves que el `questions.json` de P500 más `reading` y `limit`; (3)
  `analysis_answer.csv` calculado a partir de los Parquet de `temp/raw/`, con
  una fila por lote y columnas explícitas; (4) una lectura de 2–4 líneas con
  su límite; y (5) una prueba que verifica que la respuesta se deriva de lo
  procesado (conciliación por lote con `ingestion_report.csv` y coherencia
  interna de la variación), no sólo que el archivo existe. Un highlight nuevo
  (H04) recoge la pregunta y su respuesta; H01–H03 siguen presentes. Sólo
  entonces S02 puede revisar el límite «sin pregunta analítica» y la
  auditoría 5 de P513; la revisión de `data.C01` (hoy no mapeada) en
  `traceability.yaml` queda para S05.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P513_superstore_batch/

0. Inspecciona primero professor/main.py, src/main.py,
   data/superstore_orders_2015_q*.csv, data/source_manifest.json,
   submission/ y tests/, y (sólo lectura)
   implementation/data/P500_superstore_metricas/submission/questions.json
   para tomar su estructura de claves. Si la implementación no coincide con
   design/courses/data/P513_activity.md, detente e informa sin modificar
   nada. Confirma que design/courses/data/P500_log.md contiene Nota.P500.02;
   si no, detente e informa. Ejecuta professor/main.py y lee de vuelta los
   Parquet de temp/raw/: si Sales o Profit no son numéricos (T01 no
   ejecutada), detente e informa; no corrijas la lectura dentro de esta T02.
1. PREGUNTA: no inventes la pregunta, el usuario ni la decisión. Usa la
   redacción que el profesor haya aprobado en la discusión de esta T02
   (registrada en P513_log.md). La pregunta sugerida en P513_tasks.md no es
   una aprobación. Si no existe redacción aprobada, detente y pídela.
   Escríbela al inicio de professor/main.py (docstring del módulo o una
   constante QUESTION usada al escribir questions.json).
2. No cambies el descubrimiento con glob, utf-8-sig, el aterrizaje Parquet,
   las columnas de ingestion_report.csv ni las comprobaciones de T01.
3. RESPUESTA DESDE LO PROCESADO: después de escribir los Parquet, léelos de
   vuelta desde temp/raw/ (no desde data/) y, sólo para lotes con status
   SUCCESS, calcula por lote: source_name, period_start y period_end (mínimo
   y máximo de Order Date), row_count, sales_total (suma de Sales),
   profit_total (suma de Profit) y, desde el segundo lote en orden,
   sales_change_pct y profit_change_pct frente al lote anterior (vacío en el
   primero). Ajusta medidas y columnas a la redacción aprobada si difiere,
   sin añadir datos externos.
4. Persiste submission/analysis_answer.csv con esas columnas y
   submission/questions.json con la estructura de claves de P500 (pregunta y
   archivo de respuesta = analysis_answer.csv) más las claves reading y
   limit.
5. LECTURA: escribe en reading 2–4 líneas que respondan la pregunta con las
   cifras de analysis_answer.csv, y en limit el límite: son dos trimestres de
   un extracto docente de un solo año; no permiten hablar de tendencia ni de
   estacionalidad; la respuesta vale sólo si la ingestión conservó los tipos
   (comprobado por T01). No añadas interpretaciones de negocio que la
   redacción aprobada no contenga. Imprime la tabla de respuesta al final
   como evidencia visible.
6. Añade a tests/ pruebas que verifiquen: questions.json existe, contiene la
   pregunta no vacía y apunta a analysis_answer.csv; analysis_answer.csv
   tiene las columnas del paso 3; sus source_name coinciden con los de
   ingestion_report.csv con status SUCCESS y row_count coincide por
   source_name; sales_total y profit_total son numéricos y finitos;
   sales_change_pct coincide (con tolerancia) con la variación recalculada
   desde sales_total; period_start y period_end caen en el trimestre que
   nombra cada archivo. Las pruebas deben ser independientes de la
   profundidad del taller en la distribución y no deben depender de temp/.
   No elimines pruebas existentes.
7. Ejecuta professor/main.py y las pruebas de la actividad sin errores.
8. No modifiques datos, manifiesto ni herramientas; no toques otras
   actividades (P500 incluida), traceability.yaml ni design/.
```
