# P211 — Propuestas de mejora

**Línea base:** `P211_activity.md` (descripción S02 vigente; log histórico
`S01.P211.*`).

## T01 — Evaluar el pronóstico con orígenes móviles (backtesting)

- **Estado:** pendiente de discusión
- **Tipo:** método/evaluación
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/sas-forecasting.md` pp. 99–100
    — «use rolling simulations to evaluate ex-ante forecast performance over
    several forecast origins»: la simulación con horizonte móvil «mimic[s]
    how the forecast model performs over time» (Claude, 2026-10-04).
  - `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md`
    p. 97 — «Backtesting de modelos» figura entre las habilidades de modelado
    y analítica que demanda el mercado laboral colombiano (Claude,
    2026-10-04).
- **Qué gana el estudiante:** distinguir una ventaja estable de un modelo de
  una ventaja que depende de dónde se puso el único corte. Hoy P211 compara
  Ridge contra la línea base estacional sobre un solo bloque de doce meses
  retenidos (H02–H03). Con varios orígenes de pronóstico, el estudiante ve
  la distribución de errores de cada modelo a lo largo del tiempo y puede
  decir si Ridge supera a la línea base de forma sistemática. Ningún taller
  temporal del curso (P210, P211, P216) evalúa con más de un origen.
- **Anclas actuales:** H02 (protege un año de decisiones mensuales con
  estado conocido al cierre previo), H03 (contraste con la línea base
  estacional); superficies S02 (features y Ridge) y S03 (línea base y
  evaluación).
- **Alternativas menores descartadas:** aclarar que un solo corte puede ser
  engañoso no permite verificarlo. Hacerlo en P216 tocaría nueve notebooks y
  trece highlights. P211 tiene un solo modelo contra una sola línea base, lo
  que permite enseñar el mecanismo con un cambio local.
- **Contrato de no regresión:** se conservan H01–H04, la reconstrucción del
  calendario fiscal, la regla de usar sólo estado conocido al cierre previo,
  y los artefactos `forecast`, `model_metrics.csv`, gráfico y supuestos con
  su esquema actual. La evaluación con el bloque final de doce meses sigue
  siendo la evaluación principal; los orígenes móviles se añaden.
- **Interacciones:** T02 usa los errores de los orígenes móviles para
  construir intervalos de predicción; si se aprueba T02 sin T01, T02 debe
  usar su alternativa de regresión cuantílica.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo que compara
  Ridge y la línea base estacional sobre varios orígenes de pronóstico
  consecutivos, reentrenando con la información disponible en cada origen,
  y reporta la distribución del error por modelo y la fracción de orígenes
  en que Ridge gana. Debe estar respaldado por notebook, un CSV en
  `submission/` y una prueba.

### Instrucciones de ejecución

```text
Actividad: implementation/predictiva/P211_pronostico_congestion_servicio/

0. Inspecciona primero el notebook de profesor, los CSV de la SSA,
   submission/ y tests/. Si la evaluación actual ya reentrena el modelo en
   cada mes del bloque retenido (orígenes móviles con reajuste), detente e
   informa: la propuesta estaría cubierta. Si la implementación no coincide
   con design/courses/predictiva/P211_activity.md, detente e informa.
1. No cambies la evaluación principal sobre los últimos doce meses ni sus
   artefactos.
2. Añade una sección «Evaluación con orígenes móviles»:
   a. Define al menos 12 orígenes mensuales consecutivos antes y dentro del
      bloque final (sin usar datos posteriores a cada origen).
   b. En cada origen, reajusta Ridge (mismas features, rezagos y
      preprocesamiento) sólo con datos hasta ese origen y pronostica un
      paso adelante; calcula también el pronóstico de la línea base
      estacional. Puedes generar los orígenes con
      sklearn.model_selection.TimeSeriesSplit(n_splits=12, test_size=1)
      (ventana expansiva) en lugar de un bucle manual, siempre que los
      rezagos y la línea base de cada origen se construyan sólo con datos
      anteriores a él; si el cálculo de rezagos lo impide, usa el bucle.
   c. Registra el error absoluto de cada modelo por origen.
   d. Grafica los errores por origen para ambos modelos y resume MAE,
      mediana y fracción de orígenes en que Ridge gana.
   e. Explica en markdown, en 3–5 líneas, si la ventaja es estable y qué
      aporta esta evaluación frente al único bloque retenido.
3. Persiste submission/rolling_origin_errors.csv con columnas origin,
   model, forecast, actual, abs_error.
4. Añade a tests/ una prueba que verifique que el archivo existe, tiene esas
   columnas, ambos modelos y al menos 12 orígenes, y que ningún origen usa
   un valor real posterior a su fecha. No elimines pruebas existentes.
5. Ejecuta el notebook completo y las pruebas sin errores.
6. No modifiques otras actividades, traceability.yaml ni design/.
```

## T02 — Acompañar el pronóstico de congestión con un intervalo de predicción

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/sas-forecasting.md` pp. 7 y
    143 — los mejores métodos de la competencia M4 se destacan también por
    producir «precise prediction intervals»; la regresión cuantílica modela
    cuantiles condicionales (por ejemplo, el percentil 90) en vez de la media
    (Claude, 2026-10-04).
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-applications-guide.md`
    pp. 172–174 — pronósticos con intervalos de confianza que se abren a lo
    largo del horizonte (Claude, 2026-10-04).
  - `design/benchmarks-md/institutional/mit-machine-learning-modeling-and-simulation-principles.md`
    p. 2 — unidad de «Probabilistic Forecasting» (Claude, 2026-10-04).
  - `design/benchmarks-md/professional-learning/sas-stat.md` pp. 11–12 — distingue los límites de confianza para el valor esperado (CLM) de los límites para un valor individual (CLI), más anchos: la incertidumbre de una predicción individual no es la de la media estimada (Claude, 2026-10-04).
- **Qué gana el estudiante:** entregar un pronóstico que diga cuánto puede
  desviarse, no sólo su valor central. Para anticipar presión de servicio,
  lo relevante suele ser cuán alta puede llegar la espera (un cuantil
  superior), no su promedio. Hoy todos los pronósticos del curso son
  puntuales y S02 registra «sin incertidumbre» o «sin intervalos» como
  límite en P208–P211 y P216.
- **Anclas actuales:** H03 (contraste con la línea base), H04 (entrega
  operacional sin convertirla en política); superficies S03 (línea base y
  evaluación: «No hay incertidumbre») y S04 (entrega y pruebas).
- **Alternativas menores descartadas:** declarar el límite ya está hecho y no
  da al estudiante una forma de cuantificarlo.
- **Contrato de no regresión:** se conservan H01–H04 y el pronóstico puntual
  de Ridge con su esquema actual; el intervalo se añade como columnas
  nuevas. H04 se mantiene: el intervalo informa la presión posible, no fija
  una política de capacidad.
- **Interacciones:** depende de T01 si se usan los errores de los orígenes
  móviles; si T01 se rechaza, usar regresión cuantílica sobre las mismas
  features.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo con un
  intervalo de predicción (por ejemplo, 80 %) para cada mes pronosticado,
  la cobertura empírica del intervalo en el bloque retenido y una lectura
  explícita de su uso y su límite. Debe estar respaldado por notebook, CSV,
  gráfico y una prueba.

### Instrucciones de ejecución

```text
Actividad: implementation/predictiva/P211_pronostico_congestion_servicio/

0. Inspecciona primero el notebook de profesor, submission/ y tests/. Si la
   implementación no coincide con design/courses/predictiva/P211_activity.md
   o ya produce intervalos de predicción, detente e informa.
1. No cambies el pronóstico puntual ni sus artefactos.
2. Construye un intervalo de predicción del 80 % para cada mes del bloque
   retenido:
   - Si T01 está implementada: usa los cuantiles 10 % y 90 % de los errores
     de Ridge en los orígenes móviles anteriores a cada mes (intervalo
     empírico).
   - Si no: ajusta sklearn.linear_model.QuantileRegressor (alpha=0) con las
     mismas features para los cuantiles 0.1 y 0.9, sólo con entrenamiento.
3. Calcula la cobertura empírica (fracción de meses retenidos cuyo valor
   real cae dentro del intervalo) y grafica pronóstico, intervalo y valores
   reales.
4. Explica en markdown, en 3–5 líneas, qué significa el intervalo para
   anticipar presión de servicio, por qué la cobertura observada puede
   diferir del 80 % y que el intervalo no fija una política de capacidad.
5. Persiste submission/forecast_intervals.csv con columnas month, forecast,
   lower_80, upper_80, actual, y el gráfico en submission/.
6. Añade a tests/ una prueba que verifique el archivo, sus columnas,
   lower_80 <= forecast <= upper_80 y la presencia del gráfico. No elimines
   pruebas existentes.
7. Ejecuta el notebook completo y las pruebas sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
