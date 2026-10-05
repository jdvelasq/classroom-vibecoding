# P103 — Propuestas de mejora

**Línea base:** `P103_activity.md` (entrada S02 más reciente: `S02.P103.01`).

## T01 — Verificar la exposición y la distribución semanal antes de comparar totales por conductor

- **Estado:** pendiente de discusión
- **Tipo:** método/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 75–76 y 80 — DM-Proximity incluye «Use of scores and rankings; desirable characteristics of scores and ranking regimes» y «Normalization of data to support comparison» (p. 75); DM-Data Preparation pide «profiling data» y las habilidades «Use summary statistics and visualizations in exploratory data analysis to make inferences» e «Illustrate the impact and resolution of issues that may arise with datasets» (p. 76); DM-Outlier Detection añade que hay que conocer el dominio para decidir «whether there are (legitimate) exceptional cases» (p. 80): un ranking sólo compara lo comparable y se apoya en el perfil previo de los datos (Claude, 2026-10-04). Fuente *authoritative*: respalda una expectativa general de exploración antes de rankear, no un procedimiento concreto.
- **Qué gana el estudiante:** en el primer taller tabular del curso aprende
  que un ranking de totales supone una exposición igual y que ese supuesto
  se comprueba antes de publicar el ranking. Hoy P103 suma horas y millas
  por conductor (H01, H03) y grafica los diez con más millas (H04) sin
  verificar cuántas semanas aporta cada conductor (límite declarado de H01:
  «No se verifica que todos los conductores tengan el mismo número de
  semanas») ni mirar cómo se distribuyen las horas y millas semanales. S02
  lo resume: la exploración «se limita a medias, sumas y extremos, sin
  distribución ni calidad de datos». Con una tabla de semanas por conductor
  y una vista de la distribución semanal, el estudiante decide con
  evidencia si el top 10 de totales es legítimo o si debe expresarse por
  semana, e identifica semanas atípicas (p. ej., semanas con cero horas o
  valores extremos) que pesan en los totales.
- **Anclas actuales:** H01 (reconciliación de granularidades; su límite
  sobre el número de semanas), H02 (comparación con la media propia), H03
  (resumen verificado), H04 (ranking visual); superficies S02
  (transformaciones y agregaciones), S03 (resumen persistido), S04
  (visualización) y S05 (pruebas); dependencia «Habilita para P104 y P105».
- **Alternativas menores descartadas:** declarar en markdown que el ranking
  supone exposición igual no permite al estudiante comprobarlo. Dejar la
  distribución para P122 (histograma) y P125 (caja) la ejerce sobre otros
  casos, pero el ranking engañoso quedaría enseñado aquí sin
  verificación; la extensión es local y no cambia caso ni producto.
- **Contrato de no regresión:** se conservan H01–H04, `data/`,
  `submission/summary.csv` con sus columnas actuales (`driverId`,
  `hours-logged`, `miles-logged`, `name`) y `test_02`, que lo recalcula
  desde `data/`; también `top10_drivers.png`. Las pruebas existentes no se
  eliminan. Si la exposición es igual para todos, el ranking por totales se
  mantiene y se declara el supuesto verificado; si difiere, el ranking por
  totales se conserva y se añade su versión normalizada por semana, sin
  sustituirlo. La verificación queda en un artefacto nuevo, fuera del
  contrato que P104 reproduce en SQLite.
- **Interacciones:** ninguna dentro de P103. Fuera de P103: P104 hereda el
  contrato de `submission/` y la estructura de pruebas (no cambia, porque
  el artefacto es nuevo y `summary.csv` no se toca; replicar la verificación
  en P104 sería una decisión aparte). P105 T01 usa el resultado de P103
  como referencia; como `summary.csv` no cambia, ambas propuestas son
  compatibles.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que,
  antes del ranking, (1) se cuentan las semanas registradas por conductor y
  se declara si la exposición es igual; (2) se muestra la distribución
  semanal de horas y millas con una vista mínima (histograma o caja) y se
  comentan las semanas atípicas; y (3) se concluye en markdown si el top 10
  de totales es comparable o debe leerse por semana. Debe estar respaldado
  por el notebook, `submission/driver_exposure.csv` y una prueba que lo
  recalcule desde `data/`. H01–H04 siguen presentes y `test_02` pasa sin
  cambios.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P103_drivers_pandas/

0. Inspecciona primero professor/notebook.ipynb, data/drivers.csv,
   data/timesheet.csv, submission/ y tests/test_activity.py. Si la
   implementación no coincide con design/courses/descriptiva/P103_activity.md,
   detente e informa la discrepancia sin modificar nada. Si el notebook ya
   cuenta semanas por conductor y muestra la distribución semanal antes del
   ranking, detente e informa: la propuesta estaría cubierta.
1. No cambies data/, el cálculo ni las columnas de submission/summary.csv,
   top10_drivers.png ni test_02.
2. Antes de la celda del ranking, añade una sección «¿Son comparables los
   totales?»:
   a. Cuenta las semanas por conductor (timesheet.groupby("driverId")
      ["week"].nunique()) y comprueba si hay semanas duplicadas por
      conductor. Muestra una tabla ordenada con los conductores de menos y
      más semanas.
   b. Muestra la distribución de hours-logged y miles-logged por semana con
      la vista más pequeña que lo haga visible (un histograma o una caja por
      variable) e identifica en una tabla breve las semanas extremas
      (p. ej., cero horas o los valores más altos), sin eliminarlas.
   c. Calcula millas y horas por semana trabajada por conductor.
   d. En markdown (3–5 líneas): si todos los conductores tienen el mismo
      número de semanas, declara que el ranking por totales es comparable y
      por qué; si no, explica cuánto cambia el ranking al normalizar por
      semana. No inventes causas de las semanas atípicas: descríbelas.
3. Si la exposición difiere entre conductores, añade junto al gráfico
   existente un segundo ranking por millas por semana; no reemplaces
   top10_drivers.png.
4. Persiste submission/driver_exposure.csv con columnas driverId,
   weeks_logged, hours_per_week, miles_per_week (una fila por conductor,
   sin índice).
5. Añade a tests/test_activity.py una prueba que verifique que el archivo
   existe, tiene esas columnas y 34 filas, y que weeks_logged y
   miles_per_week coinciden con un recálculo desde data/timesheet.csv. Sigue
   el patrón de rutas de las pruebas existentes para que sea independiente
   de la profundidad de distribución. No elimines pruebas existentes.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades (en particular P104 y P105),
   traceability.yaml ni design/.
```
