# P525 — Propuestas de mejora

**Línea base:** `P525_activity.md` (entrada S02 más reciente: `S02.P525.02`).

## T01 — Verificar el índice temporal antes de particionar: clave única, días o meses faltantes y si un día ausente es cero o dato faltante

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/sas-forecasting.md` pp. 17, 30, 69 y 93 — «Statistical forecasting models assume that the data points in a series occur at evenly spaced points in time», con las advertencias «Gaps were detected in the values of the Time ID variable» y «The Time ID variable has duplicate values»; con valores faltantes en el identificador temporal «you cannot proceed» (p. 93); los datos transaccionales «might be recorded at no fixed interval» y «must be transformed into a suitable form prior to analysis» (p. 17); la interpretación de los faltantes es un parámetro explícito («Missing-value interpretation setting for the time ID», p. 69; `setmissing = missing`, p. 30) (Claude, 2026-10-05). Fuente *professional-learning*: señal de práctica; la materialidad la sostiene el límite de H03 que registró S02.
- **Qué gana el estudiante:** antes de reorganizar una serie temporal,
  comprobar que su índice es una serie: clave única, periodos consecutivos y
  una regla declarada para los periodos ausentes. Hoy P525 sólo verifica que
  la suma de filas se conserva (H03); S02 registra que «no se verifica que
  sean consecutivos» los 23 meses y que la unidad de análisis y las columnas
  distintas de `date` no están documentadas. Con el cambio, el estudiante
  confirma la clave de la serie (por ejemplo estación × fecha, si existe una
  columna de estación), detecta días o meses ausentes dentro del rango y
  registra si un día ausente significa cero o dato no observado. Aprende un
  contraste que ningún taller del curso enseña: la ausencia de una fila no
  equivale a un valor cero, y la decisión condiciona cualquier periodo que
  se recupere después. Es la primera evidencia de calidad propia de una
  serie de tiempo en el curso (`data.C03`, hoy apoyada sólo en la
  conservación de filas). No resuelve la auditoría de identidad no resuelta
  de P525 (falta de pregunta analítica y lectura por periodo no ejercitada).
- **Anclas actuales:** H01 (llave de partición derivada de `date`), H03
  (conservación de filas y resumen); superficies S01 (dataset sin unidad ni
  procedencia documentadas), S02 (particionamiento y verificación), S03
  (`lake_summary.csv`) y S04 (prueba de sólo existencia). Dependencia
  «Recibe de P524» (Parquet como formato), sin cambios.
- **Alternativas menores descartadas:** anotar en markdown que los meses
  podrían no ser consecutivos no da evidencia. Rellenar los días ausentes
  con cero o interpolarlos sería tomar la decisión sin respaldo de la
  procedencia, que S01 no documenta.
- **Contrato de no regresión:** se conservan H01–H03, la derivación de
  `year` y `month`, el diseño `year=YYYY/month=MM`, el borrado idempotente,
  la aserción de conservación de filas y `lake_summary.csv` con su esquema
  actual. La verificación se añade antes de particionar y no modifica ni
  imputa filas. La prueba existente se mantiene.
- **Interacciones:** se refuerza con T02 (lectura por periodo): si ambas
  se aprueban, esta T01 se ejecuta primero, y T02 se apoya en la regla de
  ausencias que esta T01 deja registrada.
- **Criterio de aceptación:** S05 encuentra, antes de la escritura de
  particiones, una verificación de clave única, de días y meses faltantes en
  el rango observado y de la interpretación de un día ausente, persistida en
  `submission/time_index_check.csv`, con una prueba que verifica el archivo.
  La interpretación procede de la documentación de la fuente o del profesor,
  o queda declarada como «no documentada»; nunca la elige la herramienta. Un
  highlight nuevo o modificado de H03 recoge la verificación. H01–H03 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P525_particionamiento_parquet/

0. Inspecciona primero professor/notebook.ipynb, notebooks/notebook.ipynb,
   data/cta_daily_station_totals.parquet, submission/ y tests/. Si la
   implementación no coincide con design/courses/data/P525_activity.md,
   detente e informa sin modificar nada. CONFIRMA LA ESTRUCTURA DEL DATASET:
   lista columnas, dtypes y número de filas (100800 según lake_summary.csv)
   y determina si hay una columna de estación (identificador o nombre) y
   cuál es la columna de conteo. Decide la clave así:
   a. si hay columna de estación, la clave es (estación, date);
   b. si la única columna temporal e identificadora es date, la clave es
      date; en ese caso comprueba si date se repite: si se repite y no hay
      otra columna que lo explique, detente e informa (la unidad de análisis
      no sería determinable).
   Registra en el informe de S04 qué caso aplicó.
1. No cambies la derivación de year y month, el diseño de directorios, el
   borrado idempotente, la aserción de conservación ni lake_summary.csv.
2. Antes de la celda que escribe particiones, añade una sección
   «Verificar el índice temporal»:
   a. CLAVE: cuenta las filas con clave duplicada. Si hay duplicados, no
      los elimines ni agregues: muéstralos en una tabla breve, detente e
      informa.
   b. HUECOS: entre la fecha mínima y máxima, compara los días esperados con
      los observados (por estación si la clave la incluye; reporta el total
      de pares estación-día ausentes y cuántas estaciones tienen alguno) y
      verifica que los meses entre el primero y el último sean consecutivos.
      Muestra la tabla o gráfico más pequeño que haga visibles los huecos.
   c. AUSENCIAS: cuenta las filas con conteo explícitamente igual a cero
      como evidencia para la discusión, sin concluir de ella la regla.
      La interpretación de un día ausente (cero o dato no observado) debe
      venir de la documentación de la fuente o del texto que el profesor
      haya aprobado en la discusión de esta T01 (registrado en
      P525_log.md). Si no existe, usa el valor "no documentada". No
      imputes, no rellenes con cero y no interpoles.
   d. Explica en markdown, en 3–5 líneas, por qué una fila ausente no
      equivale a cero y cómo esa regla afectaría un total por periodo
      recuperado de las particiones.
3. Persiste submission/time_index_check.csv con una fila y columnas
   key_columns, rows, duplicate_keys, date_min, date_max, expected_days,
   missing_days (o missing_station_days si la clave incluye estación),
   stations_with_gaps (vacío si no aplica), months_expected,
   months_observed, explicit_zero_rows, absent_day_interpretation.
4. Añade a tests/ una prueba que verifique que time_index_check.csv existe,
   tiene esas columnas, duplicate_keys es 0, months_observed es menor o
   igual que months_expected y absent_day_interpretation no está vacío. La
   prueba debe ser independiente de la profundidad del taller en la
   distribución. No elimines la prueba existente.
5. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
6. No añadas pregunta analítica ni lectura con poda de particiones (fuera de
   esta T01). No modifiques otras actividades, traceability.yaml ni design/.
```

## T02 — Leer un periodo tocando sólo sus archivos y verificar que coincide con filtrar el conjunto completo

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` p. 58 — BDS-Distributed Data Storage: «Big Data applications benefit from approaches to data storage that are scalable, accommodate vast amounts of data, possibly straddling various machines, and yet facilitating processing within an appropriate time frame», con «Retrieval issues» entre los conocimientos de nivel T2 (Claude, 2026-10-05). Fuente *authoritative*: expectativa general; la materialidad la sostiene el límite de evidencia que registró S02 (recuperación declarada y no ejercitada).
  - `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` p. 46 — «MANAGING DATA VOLUME»: «Add Partition key date/time type column», «Set date range filter to use RangeStart & RangeEnd parameters» y «Load only data needed for development into the local copy of the model» (Claude, 2026-10-05). Fuente *professional-learning*: señal de práctica (llave temporal de partición para leer sólo un rango); no prescribe la herramienta ni el refresco incremental.
- **Qué gana el estudiante:** demostrar el uso que justifica una partición.
  El propio notebook declara el propósito «recuperar períodos analíticos sin
  leer todo el conjunto», pero S02 registra que «no hay lectura filtrada,
  poda de particiones ni medición» (S02.P525.01) y lo conserva como límite
  de evidencia en S02.P525.02. Con el cambio, el estudiante elige un periodo
  (un trimestre con sus tres meses presentes), lo lee sólo desde los
  directorios `year=…/month=…` que le corresponden, verifica que las filas y
  el total de la columna de conteo coinciden con filtrar por `date` el
  `frame` completo, y registra cuántos archivos leyó frente al total (por
  ejemplo 3 de 23). Aprende que una partición vale por la lectura que
  permite, que la llave de H01 se elige para esa lectura y que una lectura
  parcial debe comprobarse contra la completa antes de usarla. Ningún taller
  del curso lee datos particionados: P524 compara formatos por tamaño y P525
  sólo escribe. **Límite que no se resuelve:** esta T02 no resuelve el
  límite «sin pregunta analítica» que S02 registra para P525 (no hay
  pregunta ni usuario del periodo recuperado); ejercita la finalidad simple
  que el taller ya declara. Lo que la pone en alcance es la aclaración del
  profesor (2026-10-05): el curso está entre la ingeniería de datos y la
  analítica, y formatos y particionamiento pertenecen a él como puente.
- **Anclas actuales:** H01 (llave de partición derivada de `date`), H02
  (diseño `year=…/month=…` reproducible) y H03 (conservación de filas y
  `lake_summary.csv`), que se conservan; superficies S02
  (particionamiento y verificación, «sin lectura por periodo»), S03
  (`lake_summary.csv`, una fila) y S04 (prueba de sólo existencia).
  Dependencia «Recibe de P524» (Parquet), sin cambios.
- **Alternativas menores descartadas:** afirmar en markdown que la
  partición permite leer un periodo repite el propósito sin demostrarlo.
  Leer con filtros de partición de una biblioteca concreta (`filters=` de
  pyarrow) acercaría el ejercicio a la herramienta; la lectura por ruta
  hace visible el mecanismo y basta. Medir tiempos de lectura añadiría una
  medición dependiente del equipo sobre 23 archivos pequeños; el conteo de
  archivos leídos es la evidencia estable. Persistir el conjunto
  particionado fuera de `temp/` no es necesario para esta verificación.
- **Contrato de no regresión:** se conservan H01–H03, la derivación de
  `year` y `month`, el diseño de directorios, el borrado idempotente, la
  aserción de conservación de filas y `lake_summary.csv` con su esquema
  actual. El conjunto particionado sigue en `temp/`; sólo la verificación
  pasa a `submission/`. Si T01 se aprueba, `time_index_check.csv` y su
  prueba se conservan. La prueba existente se mantiene.
- **Interacciones:** se refuerza con T01 y la ejecución es T01 primero:
  T02 lee después de la escritura y usa la clave, la columna de conteo y la
  regla de días ausentes que T01 deja registradas (si la regla es «no
  documentada», el total leído se reporta como suma de filas observadas,
  sin imputar). Si T01 no se aprueba, S04 identifica la columna de conteo
  en el paso 0 de esta T02. Capacidad: P525 tiene tres highlights y ambas
  propuestas añaden una sección breve cada una; el riesgo de capacidad es
  bajo.
- **Criterio de aceptación:** S05 encuentra, después de la escritura de
  particiones, una lectura de un trimestre que sólo abre los archivos de sus
  tres directorios, con una vista pequeña de los archivos leídos frente al
  total, y su comparación con el filtro del `frame` completo, persistidas en
  `submission/period_read_check.csv` con una prueba que verifica el archivo.
  Un highlight nuevo recoge la lectura por periodo; H01–H03 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P525_particionamiento_parquet/

0. Inspecciona primero professor/notebook.ipynb, notebooks/notebook.ipynb,
   data/cta_daily_station_totals.parquet, submission/ y tests/. Si la
   implementación no coincide con design/courses/data/P525_activity.md, o
   con lo que P525 T01 dejó implementado si fue aprobada y ejecutada,
   detente e informa sin modificar nada. Si T01 está aprobada y no se ha
   ejecutado, detente: T01 va primero. Identifica la columna de conteo (la
   que T01 registró o, si T01 no se aprobó, la columna numérica de totales
   que confirme la inspección); si no hay una columna de conteo
   identificable, usa sólo filas y registra value_column vacío.
1. No cambies la derivación de year y month, el diseño de directorios, el
   borrado idempotente, la aserción de conservación, lake_summary.csv ni lo
   añadido por T01.
2. Después de la celda que escribe particiones, añade «Leer un periodo»:
   a. Elige el primer trimestre calendario cuyos tres meses estén presentes
      en las particiones. Si no hay ninguno, usa el primer mes presente e
      infórmalo.
   b. Construye la lista de archivos sólo con las rutas
      year=YYYY/month=MM de ese periodo y léelos (pd.read_parquet por
      archivo y concat). Muestra en una tabla breve los archivos leídos y
      el total de archivos del conjunto.
   c. Filtra el frame completo por date dentro del periodo y compara filas
      y total de la columna de conteo con lo leído (con tolerancia de
      redondeo si es flotante). Si no coinciden, detente e informa.
   d. Explica en markdown, en 3–5 líneas, por qué la llave year/month
      permite leer sólo esos archivos, qué se ahorra frente a leer todo y
      por qué la lectura parcial se verifica contra la completa.
3. Persiste submission/period_read_check.csv con una fila y columnas
   dataset, period_start, period_end, partition_files_read,
   partition_files_total, rows_read, rows_expected, value_column,
   value_total_read, value_total_expected, matches.
4. Añade a tests/ una prueba que verifique que period_read_check.csv existe,
   tiene esas columnas, partition_files_read es menor que
   partition_files_total, rows_read es igual a rows_expected y matches es
   verdadero. La prueba debe ser independiente de la profundidad del taller
   en la distribución. No elimines pruebas existentes.
5. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
6. No añadas pregunta analítica, no midas tiempos, no muevas el conjunto
   particionado fuera de temp/ y no modifiques otras actividades,
   traceability.yaml ni design/.
```
