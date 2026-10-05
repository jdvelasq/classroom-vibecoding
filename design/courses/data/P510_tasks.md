# P510 — Propuestas de mejora

**Línea base:** `P510_activity.md` (entrada S02 más reciente: `S02.P510.02`).

## T01 — No convertir en 0 el promedio de los cursos sin calificaciones: separar ausencia estructural (conteo 0) de valor desconocido (promedio nulo) y documentar la decisión

- **Estado:** pendiente de discusión
- **Tipo:** método/evidencia (corrección de un defecto)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` p. 76 — en DM-Data Preparation, «Munging data - dealing with errors in data, gaps in data, cleansing data, validating data» y la habilidad «Illustrate the impact and resolution of issues that may arise with datasets»: tratar los vacíos del dato y mostrar el efecto de su resolución (Claude, 2026-10-05). Fuente *authoritative*: expectativa general.
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` p. 15 — CAP-E.3.5.2: «Identify common issues in data wrangling, such as missing values, duplicates, redundancy, incorrect/mismatched data types, corrupt data, and default data»: un 0 puesto por `COALESCE` es un dato por defecto que se lee como valoración (Claude, 2026-10-05). Fuente *authoritative* (examen de nivel inicial).
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` p. 15 — CAP-P.3.6.1: «Identify how to recognize issues with the data based on data quality gaps, including missing data» y CAP-P.3.5.2: «Identify how to correct common issues with data»: refuerzo genérico del reconocimiento y la corrección del faltante (Claude, 2026-10-05). Fuente *authoritative*; peso bajo, no aporta un argumento específico.
- **Qué gana el estudiante:** decidir qué significa la ausencia según la
  medida cuando cambia de grano. En el `LEFT JOIN` calificación → curso (H02),
  un curso sin filas en `rating` tiene `rating_count = 0`, que es un hecho
  conocido (ausencia estructural), pero su promedio no es 0 sino desconocido.
  Hoy `COALESCE(ROUND(AVG(r.rating), 2), 0)` lo convierte en la peor
  valoración posible, en una tabla destinada a priorizar una oferta
  educativa, y H03 lo da por válido con `average_rating.between(0, 5)`. El
  propio S02 lo registra como límite («“sin evidencia” se confunde con la
  valoración mínima») y H02 lo nombra como su «costo visible». Con la
  corrección, el estudiante deja el promedio nulo, conserva el conteo 0,
  comprueba cuántos cursos están en esa situación y documenta la decisión
  (`data.C04`, hoy débil). Es el menor cambio (nivel 2): una expresión SQL,
  una aserción y una nota de decisión; no cambia caso, grano ni producto.
- **Anclas actuales:** H02 (`LEFT JOIN` que conserva cursos sin hechos), H03
  (conciliación y rango); superficies S03 (consulta de agregación con
  `COALESCE(..., 0)`), S04 (`course_ratings.csv`), S05 (pruebas). H01 no se
  toca.
- **Alternativas menores descartadas:** declarar el límite en texto ya está
  hecho en S02 y no cambia lo que el producto persiste. Imputar otro valor
  (media global, mediana) sustituiría un dato por defecto por otro sin
  evidencia del curso; sólo sería aceptable como decisión explícita del
  profesor y además del nulo, no en su lugar.
- **Contrato de no regresión:** se conservan H01–H03, la carga del volcado y
  la adaptación de dialecto, el `LEFT JOIN`, `COUNT(r.user_id)`, el
  `COALESCE` a `'unknown'` de lenguajes nulos (otra decisión, no se toca), el
  grano curso, las aserciones `len == 100` y de conciliación de conteos, y
  `course_ratings.csv` con sus cinco columnas y su orden
  (`rating_count DESC, average_rating DESC`). Se sustituye sólo la imputación
  a 0 del promedio por un nulo, y la aserción de rango se aplica a los
  promedios no nulos; la evidencia es al menos equivalente porque se añade la
  comprobación de que el nulo ocurre exactamente cuando el conteo es 0. La
  prueba existente se mantiene.
- **Interacciones:** sin otras `Txx` en P510. Se reforzaría con una futura
  regla explícita de priorización (S02 registra que no existe); esa regla no
  es parte de esta T01. El sesgo de usar el número de calificaciones como
  «adopción» queda como límite declarado en la nota, no como cambio.
  Capacidad: cambio pequeño en un taller de tres highlights.
- **Criterio de aceptación:** S05 encuentra (1) la consulta sin
  `COALESCE(..., 0)` sobre el promedio, con `average_rating` nulo
  exactamente cuando `rating_count = 0`; (2) una celda que muestra cuántos
  cursos tienen 0 calificaciones y el mínimo y máximo observados de `rating`;
  (3) una nota markdown que documenta la decisión y su límite; (4) H03
  modificado (rango sobre no nulos más la regla nulo ⇔ conteo 0) y pruebas
  que lo verifiquen sobre `course_ratings.csv`. Si hoy no hay cursos sin
  calificaciones, el CSV no cambia y la regla queda explícita y probada.
  H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P510_datacamp_valoraciones/

0. Inspecciona primero professor/notebook.ipynb (celdas de carga, consulta y
   aserciones), data/datacamp_application.sql, submission/course_ratings.csv
   y tests/test_activity.py. Si la consulta no usa
   COALESCE(ROUND(AVG(r.rating), 2), 0) con LEFT JOIN, o la implementación no
   coincide con design/courses/data/P510_activity.md, detente e informa sin
   modificar nada. Tras cargar la base temporal, calcula y anota: número de
   cursos sin filas en rating, y MIN y MAX de rating.rating. Si no hay cursos
   sin calificaciones, continúa: el cambio queda como regla explícita sin
   efecto en el resultado actual, y la nota del paso 4 debe decirlo. Si el
   mínimo observado de rating es 0, dilo en la nota: el 0 imputado sería
   además indistinguible de una calificación real.
1. No cambies la carga del volcado, el COALESCE de programming_language, el
   grano, las columnas ni el orden de course_ratings.csv, ni las aserciones
   len == 100 y de conciliación de conteos.
2. CONSULTA: sustituye COALESCE(ROUND(AVG(r.rating), 2), 0) por
   ROUND(AVG(r.rating), 2) AS average_rating. Conserva
   COUNT(r.user_id) AS rating_count. Mantén ORDER BY rating_count DESC,
   average_rating DESC y verifica que los nulos quedan al final (en SQLite
   NULL es menor que cualquier valor; si tu versión lo admite, puedes
   escribir NULLS LAST para hacerlo explícito).
3. ASERCIONES: reemplaza average_rating.between(0, 5) por la misma regla
   sobre average_rating.dropna(), y añade
   assert (course_ratings.average_rating.isna()
           == (course_ratings.rating_count == 0)).all().
   Muestra en una celda el número de cursos con rating_count == 0.
4. NOTA DE DECISIÓN: añade una celda markdown de 4–6 líneas que explique que
   rating_count = 0 es una ausencia conocida y average_rating nulo un valor
   desconocido; por qué no se usa 0 (se leería como la peor valoración en
   una tabla de priorización); que la escala de rating no está documentada y
   se informa el rango observado; y que el número de calificaciones es sólo
   una aproximación a la adopción.
5. Si la celda final de resumen por lenguaje promedia average_rating,
   comprueba que ignora los nulos (pandas mean lo hace por defecto) y
   menciónalo en la nota; no lo persistas (no es parte de esta T01).
6. Persiste course_ratings.csv con el mismo esquema; el promedio nulo se
   escribe como campo vacío.
7. Añade a tests/ pruebas que lean submission/course_ratings.csv y
   verifiquen: las cinco columnas actuales; 100 filas; ninguna fila con
   rating_count == 0 y average_rating == 0; average_rating nulo si y sólo si
   rating_count == 0; promedios no nulos entre 0 y 5. No elimines la prueba
   existente.
8. Ejecuta el notebook completo y las pruebas sin errores.
9. No modifiques otras actividades, traceability.yaml ni design/.
```
