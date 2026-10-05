# P122 — Propuestas de mejora

**Línea base:** `P122_activity.md` (entrada S02 más reciente: `S02.P122.01`).

## T01 — Inspeccionar atípicos y extremos del KPI de días frente a lo programado antes de resumir con promedios

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` p. 15 — CAP-P.3.6.1 «Identify how to recognize issues with the data based on data quality gaps, including missing data, accuracy, completeness, consistency, timeliness, validity, uniqueness, and outliers» y CAP-P.3.6.2 «Identify patterns and characteristics of a multivariate dataset from data profiling outputs»: los atípicos son una dimensión de calidad que el analista debe reconocer al evaluar los datos (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general, no un procedimiento.
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md` pp. 71, 76 y 79 — el nodo Data Audit da «a comprehensive first look at the data» con estadísticos e histogramas por campo y permite «specify treatments for missing values, outliers, and extreme values» (p. 71); «The Quality tab in the audit report displays information about outliers, extremes, and missing values» (p. 76); los atípicos se tratan con «either coerce, discard, or nullify» (p. 79): auditar la distribución y los extremos de cada campo es un paso estándar antes de analizar (Claude, 2026-10-04). Fuente *professional-learning*: sólo se toma la práctica de auditar; el tratamiento automático (coerce/discard/nullify, imputación C&RT) queda fuera porque contradice la regla de no imputación de H05.
- **Qué gana el estudiante:** decidir, con evidencia de la cola, si un
  promedio de días resume bien el cumplimiento. Hoy la tabla de calidad de
  H01 sólo tabula faltantes y valores distintos, H02 muestra un histograma
  con referencia en cero y H03 deja observable que el promedio de días y la
  proporción a tiempo divergen (Truck: −9,92 días y 0,839 a tiempo; Air
  Charter: −19,04 días y 0,885) porque anticipos compensan retrasos, pero
  el notebook no localiza los valores extremos que producen esa divergencia
  ni decide qué hacer con ellos. Con un perfil por modo (percentiles, caja,
  conteo de atípicos y extremos), la lista de los envíos más extremos y una
  decisión declarada (conservar e informar; no imputar ni recortar en
  silencio), el estudiante ve cuánto de cada promedio depende de pocas
  líneas y convierte el histograma en una decisión de calidad antes de
  concluir. Ninguna actividad del curso inspecciona atípicos, aunque la
  capacidad C02 nombra la exploración de distribuciones, atípicos o calidad
  antes de concluir.
- **Anclas actuales:** H01 (grano y tabla de calidad), H02 (KPI
  `DeliveryDaysVsSchedule` derivado de dos fechas, histograma), H03
  (proporción frente a promedio), H05 (regla de no imputación), H06 (modo
  faltante conservado con `dropna=False`); superficies S01 (dataset y
  grano), S02 (definición de cumplimiento), S05 (`submission/`) y S06
  (pruebas, que hoy exigen exactamente ocho CSV).
- **Alternativas menores descartadas:** comentar el contraste de H03 en
  markdown lo haría visible, pero no le daría al estudiante la evidencia de
  qué líneas lo producen ni una decisión explícita sobre ellas. Ampliar la
  tabla de faltantes a más columnas no toca la distribución. Sustituir el
  promedio por la mediana en los resúmenes persistidos cambiaría H03 y los
  artefactos; la propuesta añade el perfil sin cambiar ningún KPI.
- **Contrato de no regresión:** se conservan H01–H07, la conversión de
  fechas, la definición de `IsLate` (más de 0 días), el valor expuesto, la
  cobertura de flete y la regla de no imputación, los umbrales 50/20/30 y
  los ocho CSV actuales con su esquema y contenido. Ningún registro se
  elimina, recorta ni imputa en los KPI persistidos; cualquier cálculo sin
  extremos se presenta sólo como sensibilidad, rotulado como tal. La única
  prueba existente que cambia es la del conjunto exacto de CSV, que se
  amplía sin quitar ninguno.
- **Interacciones:** ninguna dentro de P122 (única propuesta). Capacidad:
  extensión local de H01–H03; no cambia caso, preguntas ni tablas
  obligatorias.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo (o H01
  extendido) en el que (1) `DeliveryDaysVsSchedule` se perfila por modo,
  incluido el modo faltante, con percentiles, caja y conteo de valores
  fuera de cercas declaradas; (2) se listan los envíos más extremos con su
  país, modo, fechas y valor; (3) una lectura explícita dice si el promedio
  de cada modo cambia de forma relevante sin los extremos y declara la
  decisión: los KPI se conservan con todos los registros y no se imputa ni
  recorta; y (4) `submission/delivery_days_profile.csv` y
  `submission/delivery_days_extremes.csv` existen con pruebas que los
  recomputan. H01–H07 siguen presentes y los ocho CSV originales no
  cambian.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P122_supply_chain/

0. Inspecciona primero professor/notebook.ipynb, data/supply_chain.csv,
   submission/ y tests/test_activity.py. Si la implementación no coincide
   con design/courses/descriptiva/P122_activity.md (o ya inspecciona
   atípicos de DeliveryDaysVsSchedule), detente e informa sin modificar
   nada. Calcula, por modo, Q1, Q3, IQR y cuántos envíos quedan fuera de
   Q1 − 3·IQR / Q3 + 3·IQR, y compara media y mediana. Si ningún modo tiene
   envíos fuera de esas cercas y media y mediana difieren en menos de un
   día en todos los modos, detente e informa: la propuesta no tendría
   evidencia en este caso.
1. No cambies la conversión de fechas, DeliveryDaysVsSchedule, IsLate, las
   secciones existentes, los umbrales ni los ocho CSV actuales.
2. Después de la sección de H03 añade «Atípicos y extremos del
   cumplimiento»:
   a. Por Shipment Mode (con dropna=False, como en H06) y para el total:
      n, media, mediana, p05, p25, p75, p95, mínimo, máximo, conteo fuera
      de las cercas de 1,5·IQR (atípicos) y de 3·IQR (extremos). Declara en
      markdown que las cercas son una convención de Tukey elegida para
      describir, no una regla de error.
   b. Diagrama de caja de DeliveryDaysVsSchedule por modo, con la
      referencia en cero de H02.
   c. Lista los 20 envíos con mayor |DeliveryDaysVsSchedule| (ambos
      signos): ID, Country, Shipment Mode, fecha programada, fecha real,
      DeliveryDaysVsSchedule, Line Item Value.
   d. Como sensibilidad, calcula la media por modo sin los envíos fuera de
      3·IQR y muéstrala junto a la media con todos; no la uses en ningún
      KPI ni CSV existente.
   e. Explica en markdown, en 4–6 líneas: qué modos tienen colas largas y
      de qué signo, si los extremos explican la divergencia de H03 entre
      promedio y proporción a tiempo, y la decisión: se conservan todos
      los registros, no se imputan ni recortan, porque sin documentación
      de la fuente no hay evidencia de que un extremo sea un error de
      captura. No atribuyas causas a los retrasos.
3. Persiste submission/delivery_days_profile.csv con columnas
   shipment_mode, n, mean, median, p05, p25, p75, p95, min, max,
   n_outliers_1_5iqr, n_extremes_3iqr, mean_without_extremes (fila «ALL»
   para el total; el modo faltante con un rótulo explícito), y
   submission/delivery_days_extremes.csv con columnas ID, country,
   shipment_mode, scheduled_date, delivered_date, delivery_days_vs_schedule,
   line_item_value.
4. En tests/test_activity.py amplía la prueba del conjunto exacto de CSV
   con los dos archivos nuevos (sin quitar los ocho actuales) y añade
   pruebas que recompongan delivery_days_profile.csv desde
   data/supply_chain.csv (n por modo suma el total de envíos; mediana y
   percentiles coinciden) y verifiquen que delivery_days_extremes.csv tiene
   20 filas ordenadas por |delivery_days_vs_schedule| descendente. No
   elimines pruebas existentes.
5. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
6. No modifiques otras actividades, traceability.yaml ni design/.
```
