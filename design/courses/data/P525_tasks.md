# P525 — Propuestas de mejora

**Línea base:** `P525_activity.md` (entrada S02 más reciente: `S02.P525.01`).

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
- **Interacciones:** ninguna dentro de P525 (única propuesta). Si en la
  discusión se aprueba además que P525 ejercite la lectura por periodo, ésta
  debería apoyarse en la regla de ausencias que esta T01 deja registrada.
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
