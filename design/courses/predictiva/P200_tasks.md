# P200 — Propuestas de mejora

**Línea base:** `P200_activity.md` (descripción S02 vigente; log histórico
`S01.P200.*`).

## T01 — Encuadrar el primer producto predictivo: decisión, medida de éxito y línea base ingenua

- **Estado:** pendiente de discusión
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
