# P200 — Propuestas de mejora

**Línea base:** `P200_activity.md` (descripción S02 vigente; log histórico
`S01.P200.*`).

## T01 — Encuadrar el primer producto predictivo: decisión, medida de éxito y línea base ingenua

- **Estado:** incoporado
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md`
    pp. 4–5 — Tasks 1.1–1.3 (enunciar el problema de negocio, identificar
    *stakeholders*, decidir si admite solución analítica), 2.1 (reformularlo
    como problema analítico), 2.4 («Define primary measures of success») y
    2.5 («Identify baseline performance of the current state») (Claude,
    2026-10-04).
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` pp. 7–11 — objetivos de examen de nivel inicial: identificar *stakeholders*, la parte poco clara de un enunciado de negocio, las medidas primarias de éxito y «how to measure the baseline values of the primary measures of success of the current state» (Task 2.5) (Claude, 2026-10-04).
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` pp. 7–11 — nivel intermedio: CAP-P.2.4.2 (verificar si se cumplen las medidas de éxito), CAP-P.2.5.1 («Identify current baseline performance and how it relates to expected performance as measured by the primary measures of success») y CAP-P.5.6.1 (explicación no técnica de los resultados) (Claude, 2026-10-04).
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 40 y 48 — el flujo de trabajo empieza por «formulating good questions» y la comunicación exige «Ability to understand client needs» (Claude, 2026-10-04).
  - `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` pp. 9 y 11 — «Todo proyecto de Analítica comienza con un problema de negocio»: formular el problema con partes interesadas y criterios de éxito, «Definir la línea base, los criterios de éxito, los costos y los beneficios», y traducirlo en un problema analítico «orientado a una decisión» (objetivo = métrica + acción + resultado esperado) (Claude, 2026-10-04).
  - `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` pp. 13–14 y 18–19 — en PRODIG8 la definición de alcance fija «success criteria that capture both business and analytical perspectives», y la evaluación del modelo se hace «against predefined technical and business success criteria» con «systematic comparisons against benchmarks» (Claude, 2026-10-04).
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` pp. 9–10 — fase de entendimiento del negocio de CRISP-DM: describir la solución actual, especificar las preguntas de negocio y los beneficios esperados, y acordar «Business Success Criteria» antes de modelar (Claude, 2026-10-04).
  - `design/benchmarks-md/professional-learning/sas-data-mining.md` p. 7 — «Paso 1: Convierta una Pregunta de Negocio en una Hipótesis Analítica»: una meta general («reducir el abandono») debe volverse un resultado bien definido para el modelo (Claude, 2026-10-04).
- **Qué gana el estudiante:** desde el primer producto predictivo del curso,
  aprende a decir para qué decisión sirve la predicción, con qué medida se
  juzga el éxito y contra qué referencia trivial debe compararse. Hoy P200
  predice MPG sin usuario ni decisión («no hay decisión de flota
  evidenciada») y su línea base es una regresión con `Horsepower` (H04), no
  un predictor ingenuo del estado actual (por ejemplo, la media de
  entrenamiento). Los talleres temporales posteriores sí comparan contra
  persistencia o estacionalidad (P210, P211, P213), pero el hábito nunca se
  establece en el primer producto, y P201, P203, P219, P221 y P223 tampoco
  lo usan. Sin una línea base ingenua, un MSE no dice si el modelo aporta
  algo.
- **Anclas actuales:** H01 (primer producto predictivo), H04 (línea base
  interpretable), H09 (comparación de capacidad); superficies S01 (caso y
  dataset) y S03 (familias y especificaciones de modelo); dependencia
  «Habilita para P201, P203, P204, P219, P221 y P223».
- **Alternativas menores descartadas:** aclarar en el texto que no hay
  decisión evidenciada ya está hecho en S02 y no cambia lo que el estudiante
  practica. Agregar sólo la línea base ingenua, sin el encuadre, enseñaría el
  mecanismo pero no por qué se elige esa medida de éxito.
- **Contrato de no regresión:** se conservan H01–H10, el dataset y su
  preparación, la partición, las especificaciones comparadas, la MLP y todos
  los artefactos persistidos con su esquema actual. Las pruebas existentes se
  mantienen. Se añade una fila de línea base ingenua a la comparación de MSE
  y un encuadre breve al inicio. Ninguna especificación existente se
  sustituye.
- **Interacciones:** ninguna dentro de P200. Si se aprueba, conviene decidir
  en la discusión si las actividades que dependen de P200 (P201, P203, P221,
  P223) deben reutilizar el hábito de la línea base ingenua; eso sería una
  propuesta por actividad, no parte de esta T01.
- **Criterio de aceptación:** S05 encuentra (1) un encuadre explícito al
  inicio del notebook con usuario o decisión, medida de éxito y error
  tolerable, definidos por el profesor y no inventados por la herramienta; y
  (2) un highlight nuevo que compara todas las especificaciones contra un
  predictor ingenuo sobre la misma partición, con la fila correspondiente en
  `model_comparison.csv` y una prueba que verifique su presencia. H01–H10
  siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/predictiva/P200_regresion_basica/

0. Inspecciona primero professor/notebook.ipynb, data/auto_mpg.csv,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/predictiva/P200_activity.md, detente e informa la
   discrepancia sin modificar nada.
1. ENCUADRE: no inventes usuario ni decisión. Usa el texto que el profesor
   haya aprobado en la discusión de esta T01 (registrado en P200_log.md). Si
   no existe, detente y pídelo. Insértalo como celda markdown al inicio:
   pregunta de negocio, quién usa la predicción, medida de éxito (MSE y su
   lectura en unidades de MPG) y error que haría inútil el producto.
2. LÍNEA BASE INGENUA: con la misma partición existente, ajusta
   sklearn.dummy.DummyRegressor(strategy="mean") sólo con entrenamiento y
   calcula su MSE de prueba.
3. Añade esa fila a la comparación existente y a
   submission/model_comparison.csv, sin cambiar las filas ni columnas
   actuales.
4. Añade en markdown 2–4 líneas que interpreten cuánto mejora cada modelo
   frente a la línea base ingenua.
5. Añade a tests/ una prueba que verifique que model_comparison.csv contiene
   la fila de la línea base y que su MSE es mayor o igual que el del mejor
   modelo. No elimines pruebas existentes.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades, traceability.yaml ni design/.
```

## T02 — Diagnosticar la especificación lineal con residuos y transformar la respuesta

- **Estado:** incorporado
- **Tipo:** método/diagnóstico
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/sas-stat.md` p. 9 — en el
    gráfico de residuos contra valores predichos, «A fan-shaped trend might
    indicate the need for a variance-stabilizing transformation. A curved
    trend (such as a semicircle) might indicate the need for a quadratic term
    in the model» (Claude, 2026-10-04).
  - `design/benchmarks-md/professional-learning/sas-stat.md` pp. 13 y 15 — el
    panel de diagnósticos de la regresión lineal de la población de EE. UU.
    «indicate[s] an inadequate model»: el patrón cuadrático de los residuos
    contra el predicho y contra el regresor indica que debe añadirse un
    término cuadrático (Claude, 2026-10-04).
  - `design/benchmarks-md/professional-learning/sas-stat.md` pp. 144 y
    149–151 — Example 79.1: «Since the variation in salaries is much greater
    for higher salaries, it is appropriate to apply a log transformation»;
    los residuos contra cada regresor, con suavizado loess, revelan falta de
    ajuste en `yr_major` y `cr_hits`, que se corrige con términos de grado 2
    (R² de 0.587 a 0.787) (Claude, 2026-10-04).
- **Qué gana el estudiante:** decidir la especificación de un modelo lineal a
  partir de evidencia en los datos, no por ensayo de filas de MSE. Hoy P200
  añade `Horsepower_squared` y `Weight_x_Horsepower` (H07) y compara MSE,
  pero nada en el taller muestra por qué esos términos, ni qué queda sin
  explicar. Con residuos contra predicho y contra cada regresor, el
  estudiante ve la curvatura (que justifica el término cuadrático de H07) y
  el abanico de varianza (que sugiere modelar log(MPG)). Además aprende que
  una predicción en log debe devolverse a MPG antes de compararla con las
  demás. Ningún taller del curso grafica residuos (P200, P211, P216, P219,
  P221 y P223 sólo comparan métricas), ni transforma la variable de salida:
  P216 usa `TransformedTargetRegressor` con `MinMaxScaler`, que escala sin
  cambiar la forma de la respuesta.
- **Anclas actuales:** H04 (línea base con `Horsepower`, su curva y MSE),
  H07 (flexibilidad lineal con términos derivados), H09 (comparación de
  capacidad); superficie S03 (familias y especificaciones de modelo, que
  deben mantenerse comparables sobre la misma partición y MSE).
- **Alternativas menores descartadas:** explicar en markdown por qué se
  añaden los términos de H07 no permite al estudiante verificarlo en sus
  datos. Ubicarlo en P221 (que reutiliza Auto MPG) o en P223 lo alejaría de
  H07, que es donde la especificación se decide, y mezclaría el diagnóstico
  con la identidad de selección o regularización de esas actividades.
- **Contrato de no regresión:** se conservan H01–H10, la partición, el
  preprocesamiento, todas las especificaciones actuales y sus filas en
  `model_comparison.csv`, la MLP y los artefactos persistidos con su esquema
  actual. El diagnóstico se añade antes de H07 y la motiva; no reemplaza
  ninguna especificación. La transformación log(MPG) se añade como una fila
  nueva, con su MSE calculado en MPG.
- **Interacciones:** compatible con T01; ambas añaden filas a
  `model_comparison.csv`. Si se aprueban ambas, conviene ejecutar T01 primero
  para que la fila log(MPG) se lea también frente a la línea base ingenua.
  Capacidad: P200 es la puerta de entrada del curso y ya tiene diez
  highlights; con T01 y T02 conviene decidir en la discusión si alguna parte
  queda como sección final que un grupo lento puede completar en la sesión
  siguiente.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que (1)
  los residuos de la especificación lineal base, contra el predicho y contra
  `Horsepower` y `Weight`, se usan para justificar la curvatura de H07 y una
  transformación de la respuesta; y (2) un modelo con log(MPG) se compara con
  los demás sobre la misma partición y en MPG. Debe estar respaldado por
  notebook, un gráfico de residuos en `submission/`, la fila nueva en
  `model_comparison.csv` y una prueba. H01–H10 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/predictiva/P200_regresion_basica/

0. Inspecciona primero professor/notebook.ipynb, data/auto_mpg.csv,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/predictiva/P200_activity.md, detente e informa. Grafica los
   residuos de prueba de la especificación lineal base; si no muestran
   curvatura ni varianza creciente con el predicho, detente e informa: la
   propuesta no tendría evidencia en este caso.
1. No cambies la partición, el preprocesamiento, las especificaciones
   existentes ni sus filas en model_comparison.csv.
2. Antes de la sección de H07, añade «Diagnóstico con residuos»:
   a. Para la regresión lineal base con todas las entradas, grafica residuos
      contra valores predichos y contra Horsepower y Weight (con una curva
      suavizada, por ejemplo lowess de statsmodels o una media móvil).
   b. Explica en markdown, en 3–5 líneas, qué indica una curva (falta un
      término no lineal, que H07 añade a continuación) y qué indica un
      abanico (varianza que crece con el nivel: sugiere transformar la
      respuesta).
3. Después de H07, añade «Transformar la respuesta»:
   a. Ajusta sklearn.compose.TransformedTargetRegressor(
      regressor=<pipeline de la regresión lineal base con el mismo
      preprocesador>, func=np.log, inverse_func=np.exp) sólo con
      entrenamiento.
   b. Calcula su MSE de prueba en MPG (las predicciones ya vuelven a MPG) y
      grafica de nuevo sus residuos contra el predicho.
   c. Explica en 2–4 líneas si la transformación corrige el abanico y la
      curvatura, y por qué el MSE debe compararse en MPG y no en log.
4. Añade la fila (por ejemplo, linear_log_target) a
   submission/model_comparison.csv sin cambiar filas ni columnas actuales, y
   guarda submission/residual_diagnostics.png con los gráficos del paso 2.
5. Añade a tests/ una prueba que verifique la fila nueva, que su MSE es
   finito y positivo, y que el PNG existe. No elimines pruebas existentes.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades, traceability.yaml ni design/.
```
