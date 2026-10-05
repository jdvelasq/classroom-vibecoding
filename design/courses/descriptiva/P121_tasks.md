# P121 — Propuestas de mejora

**Línea base:** `P121_activity.md` (entrada S02 más reciente: `S02.P121.01`).

## T01 — Separar tendencia y patrón estacional antes de responder la pregunta estacional

- **Estado:** pendiente de discusión
- **Tipo:** método
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/sas-forecasting.md` pp. 36–37 y 89 — «Associated with each time series is a seasonal cycle […] The typical seasonality assumption might not always hold» (p. 36); una serie se descompone en tendencia, ciclo, componente estacional e irregular, y «Businesses such as retailers need to distinguish short-term seasonal effects from long-term trends»; la descomposición clásica «uses a series of moving averages» (p. 37); Time Series Studio ofrece «standard graphs and tables for autocorrelation and seasonal decomposition analysis» (p. 89): separar estación y tendencia es práctica habitual antes de afirmar un patrón estacional (Claude, 2026-10-04). Fuente *professional-learning*, única: sólo atestigua que la práctica es habitual; la materialidad viene del límite que P121 ya declara en H06 y S03.
- **Qué gana el estudiante:** responder con evidencia la segunda pregunta
  del taller («¿la evolución de las aerolíneas de mayor volumen revela un
  patrón estacional?»). Hoy H06 junta los tres años en una tasa por mes del
  año y la estacionalidad «se juzga visualmente y sin separar años»
  (límite declarado en H06, S03 y en el índice de comparación). Con esa
  vista, un mes alto puede deberse a un solo año atípico o a la tendencia
  de la serie, y el estudiante no tiene cómo distinguirlo. Con un índice
  estacional calculado año por año (tasa de demora del mes frente a la tasa
  del mismo año, ambas reconstruidas desde sumas) el estudiante comprueba si
  el patrón se repite en cada año; con una descomposición clásica de la
  serie nacional de 36 meses, opcional, lee la tendencia sin la
  estacionalidad. Pasa de «se ve un patrón» a «el patrón se repite en los
  tres años (o no)». Ningún taller del curso compara años ni descompone una
  serie.
- **Anclas actuales:** H06 (serie nacional frente a tasa por mes del año),
  H03 (tasas reconstruidas tras sumar, con su denominador: demora sobre
  operados), H01 (agregados aditivos), H07 (CSV recomputados por las
  pruebas); superficies S03 (vistas temporales y calendario), S05
  (`submission/`) y S06 (pruebas, que hoy exigen exactamente seis CSV).
- **Alternativas menores descartadas:** declarar mejor el límite ya está
  hecho en S02 y no permite al estudiante verificarlo. Desagregar la tabla
  `seasonality.csv` actual por año cambiaría un artefacto que las pruebas
  recomputan; es preferible añadir una tabla nueva. Empezar por una
  descomposición clásica sola es frágil con 36 meses: la media móvil
  centrada 2×12 pierde seis meses en cada extremo y deja sólo 24 meses de
  razones estacionales (dos por mes del año); por eso el índice año por año
  es el núcleo y la descomposición es opcional.
- **Contrato de no regresión:** se conservan H01–H07, ambos agregados, la
  conciliación (`assert_frame_equal` y su prueba), `add_rates`, el umbral de
  25.000 vuelos y los seis CSV actuales con su esquema y contenido,
  incluidos `monthly_national_kpis.csv` y `seasonality.csv`. Ninguna tasa se
  obtiene promediando tasas de celdas. Se añaden un CSV, una figura y una
  lectura en markdown; la única prueba existente que cambia es la que exige
  el conjunto exacto de CSV, que se amplía con el archivo nuevo sin quitar
  ninguno.
- **Interacciones:** ninguna dentro de P121 (única propuesta). Capacidad:
  extensión local de una sección ya existente (H06); no añade caso ni
  pregunta.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo o H06
  modificado en el que (1) el índice estacional se calcula por año y mes
  del año, para la serie nacional y para las cinco aerolíneas de mayor
  volumen de H06, como razón entre la tasa de demora del mes y la del año,
  ambas desde sumas de demorados y operados; (2) una figura con una línea
  por año permite ver si el patrón se repite; (3) una lectura de 3–6 líneas
  dice qué meses quedan por encima o por debajo de la tasa anual en todos
  los años y cuáles dependen de un solo año, y declara el límite de 36
  meses; y (4) `submission/seasonal_index_by_year.csv` existe y una prueba
  lo recomputa desde `flights_by_carrier_month.csv.gz`. H01–H07 siguen
  presentes y los seis CSV originales no cambian.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P121_vuelos/

0. Inspecciona primero professor/notebook.ipynb, data/
   (flights_by_carrier_day_hour.csv.gz, flights_by_carrier_month.csv.gz),
   submission/ y tests/test_activity.py. Si la implementación no coincide
   con design/courses/descriptiva/P121_activity.md (en particular, si la
   vista estacional ya separa años o ya descompone la serie), detente e
   informa sin modificar nada. Verifica que cada una de las cinco
   aerolíneas de H06 y la serie nacional tienen los 36 meses con vuelos
   operados > 0; si a alguna le faltan meses, detente e informa cuáles: el
   índice por año no sería comparable para ella.
1. No cambies los datos, la conciliación, add_rates, el umbral de 25.000,
   las secciones existentes ni los seis CSV actuales.
2. Después de la sección de H06 añade «Patrón estacional año por año»:
   a. Desde flights_by_carrier_month.csv.gz, suma demorados y operados por
      (año, mes) para la serie nacional y por (aerolínea, año, mes) para las
      cinco aerolíneas de H06 (las mismas, con el mismo criterio de
      volumen). Calcula delay_rate = demorados / operados con add_rates o
      con la misma definición.
   b. Suma demorados y operados por (ámbito, año) y calcula la tasa anual
      del mismo modo. Nunca promedies tasas mensuales para obtenerla.
   c. seasonal_index = delay_rate del mes / tasa anual del mismo año y
      ámbito (índice multiplicativo: > 1 significa mes peor que su año).
   d. Grafica, para la serie nacional y para cada aerolínea (facetas), el
      índice contra el mes del año con una línea por año.
   e. Explica en markdown, en 3–6 líneas: qué meses quedan por encima de 1
      en los tres años, cuáles sólo en uno, si el patrón de H06 se sostiene
      año a año, y el límite: tres ciclos son poca evidencia de
      recurrencia; el índice describe, no explica causas.
3. OPCIONAL (decídelo según tiempo de taller; si lo haces, sólo para la
   serie nacional): descomposición clásica multiplicativa de la tasa
   nacional mensual con período 12. Usa
   statsmodels.tsa.seasonal.seasonal_decompose(model="multiplicative",
   period=12) sólo si statsmodels ya está en el requirements.txt raíz; si
   no, calcula la media móvil centrada 2×12 con pandas. No añadas
   dependencias. Grafica la tendencia y explica en 2–3 líneas que pierde
   seis meses en cada extremo y deja 24 meses de razones estacionales.
4. Persiste submission/seasonal_index_by_year.csv con columnas scope
   («national» o el código de aerolínea), year, month, delayed, operated,
   delay_rate, annual_delay_rate, seasonal_index. Guarda la figura del paso
   2d en submission/ (PNG o HTML).
5. En tests/test_activity.py amplía la prueba que exige el conjunto exacto
   de CSV para incluir seasonal_index_by_year.csv (sin quitar los seis
   actuales) y añade una prueba que recomponga el archivo desde
   data/flights_by_carrier_month.csv.gz, verifique las columnas, los seis
   ámbitos, los tres años × doce meses por ámbito y que
   seasonal_index == delay_rate / annual_delay_rate. No elimines pruebas
   existentes.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades, traceability.yaml ni design/.
```
