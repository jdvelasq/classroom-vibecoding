# P510 — Valoraciones de cursos DataCamp

## Actividad actual implementada

**Implementación:** `implementation/data/P510_datacamp_valoraciones/`.

### Preguntas analíticas actuales

- ¿Qué cursos y tecnologías tienen mayor adopción y mejor valoración para priorizar una oferta educativa?

La pregunta abre `professor/notebook.ipynb`. La fuente es `data/datacamp_application.sql` (59367 líneas, 1.3 MB): un volcado generado con TablePlus 2.6 de la base `datacamp_application`. No hay manifiesto: procedencia, fecha, licencia y escala de `rating` no están documentadas. El volcado usa el calificador de esquema `"public".` del motor de origen; el notebook lo elimina con `str.replace` y ejecuta el script con `sqlite3.executescript` sobre una base temporal (`temp/datacamp.db`). La fuente tiene dos granos (curso en `courses`; calificación de un usuario a un curso en `rating`) y el producto cambia al grano curso. `submission/course_ratings.csv` contiene 100 cursos; los primeros son «Introduction to Python» (python, 14950 calificaciones, promedio 4.6), «Intermediate Python for Data Science» (6507; 4.58) e «Intro to SQL for Data Science» (sql, 6054; 4.69). El resumen por lenguaje se muestra en la última celda pero no se persiste. El notebook del estudiante no tiene celdas y no hay `src/`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** priorizar una oferta educativa (declarado en la pregunta); usuario u organización concreta no evidenciados.
- **Producto terminal:** `submission/course_ratings.csv`, tabla a grano curso con lenguaje, número y promedio de calificaciones.
- **Uso y límite:** permite ordenar cursos por volumen de calificaciones y promedio. «Adopción» se aproxima por el número de calificaciones, no por inscripciones o finalizaciones. `COALESCE(ROUND(AVG(r.rating), 2), 0)` asigna 0 a un curso sin calificaciones, de modo que «sin evidencia» se confunde con la valoración mínima. No existe una regla explícita que combine adopción y valoración en una prioridad; el orden persistido es lexicográfico (`rating_count DESC, average_rating DESC`).
- **Disciplinas contribuyentes:** SQL relacional (carga de un volcado, `LEFT JOIN`, agregación) al servicio de una tabla comparativa de cursos.

### Highlights de contribución

- **H01 — Carga un volcado SQL de otro motor y lo adapta a SQLite (caso y datos):** la fuente no es un CSV ni una base SQLite lista, sino un script de respaldo con sintaxis de esquema ajena (`"public".`); el notebook lo reescribe antes de `executescript` y muestra el conteo de filas por tabla con `UNION ALL` para confirmar la carga. Primera fuente del curso entregada como volcado (P503 construía la base desde un CSV; P504–P508 recibían `scopus_proptech.db` ya construida). Sin este hito, el curso no ejercitaría el acceso a datos que llegan como respaldo de una base operativa y la adaptación de dialecto que eso exige.
- **H02 — Cambia de grano calificación→curso sin descartar cursos sin calificaciones:** `courses c LEFT JOIN rating r USING(course_id)` con `COUNT(r.user_id)` conserva todos los cursos y `COALESCE` asigna `'unknown'` a lenguajes nulos. Primer `LEFT JOIN` del curso (las vistas de P503 y las consultas de P505–P508 usan uniones internas). Sin este hito, la agregación eliminaría en silencio la oferta sin evidencia; su costo visible es el 0 imputado como promedio.
- **H03 — Concilia el agregado con la fuente antes de persistirlo:** `assert len(course_ratings) == 100`, `assert course_ratings.rating_count.sum() == source_ratings` (número de filas de `rating`) y `average_rating.between(0, 5)`. Primera conciliación explícita entre una salida agregada y su tabla fuente en el curso. Sin este hito, el estudiante no vería cómo comprobar que resumir no perdió ni duplicó registros.

### Inventario técnico de implementación

- **Introduce:** carga de volcado con `sqlite3.executescript`; adaptación textual del dialecto; `LEFT JOIN` con `COALESCE`; conciliación de conteos entre grano fuente y grano agregado.
- **Reutiliza:** SQLite y `pd.read_sql_query` (P503–P507); `GROUP BY` con `COUNT` y `AVG`; persistencia de la respuesta en CSV.
- **Aplica en nuevo caso:** primer dominio fuera de Superstore y Scopus (oferta educativa).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Ingesta de volcado SQL | H01 | `str.replace` del calificador de esquema + `executescript` | Adaptación textual ad hoc; sin manifiesto de procedencia. |
| Cambio de grano con unión externa | H02 | `LEFT JOIN` + `COUNT(r.user_id)` + `COALESCE` | Promedio 0 para cursos sin calificaciones. |
| Conciliación agregado–fuente | H03 | Tres `assert` previos a `to_csv` | El 100 está fijado en el código; la escala 0–5 es supuesta. |

### Relación técnica con actividades anteriores

Nuevo caso y nueva forma de llegada de los datos. Misma técnica SQL de agregación que P505–P507, con nueva exigencia de evidencia: conservar entidades sin hechos y conciliar el resultado con la fuente. A diferencia de P503, no se diseña el esquema: se recibe de la base operativa. No hay duplicación evidente con P500–P508.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Volcado adaptado a SQLite | S01, S02 | `implementation/data/P510_datacamp_valoraciones/data/datacamp_application.sql` (cabecera TablePlus); `implementation/data/P510_datacamp_valoraciones/professor/notebook.ipynb`: celda de carga y conteos | No se documenta el motor de origen ni se verifica que no haya otras incompatibilidades de dialecto. |
| H02 — `LEFT JOIN` y cambio de grano | S03, S04 | `implementation/data/P510_datacamp_valoraciones/professor/notebook.ipynb`: consulta `query`; `implementation/data/P510_datacamp_valoraciones/submission/course_ratings.csv` | Las filas inspeccionadas no muestran si existen cursos con 0 calificaciones. |
| H03 — Conciliación | S04, S05 | `implementation/data/P510_datacamp_valoraciones/professor/notebook.ipynb`: celda de `assert`; `implementation/data/P510_datacamp_valoraciones/tests/test_activity.py` | La prueba no repite la conciliación; sólo exige el archivo. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: volcado DataCamp | `data/datacamp_application.sql` | Sin manifiesto; escala de `rating` no documentada. |
| S02 | Representación: carga y adaptación de dialecto | `professor/notebook.ipynb` (celda 2); `temp/datacamp.db` | Reemplazo textual de una sola cadena. |
| S03 | Método: consulta de agregación | `professor/notebook.ipynb` (celda 3) | `COALESCE(..., 0)` para promedio ausente; orden sin regla de prioridad. |
| S04 | Producto: tabla a grano curso | `submission/course_ratings.csv` | Resumen por lenguaje no persistido. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia del CSV. |
| S06 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** reescribe y carga el volcado, muestra conteos por tabla, agrega a grano curso con `LEFT JOIN`, concilia con `rating` y persiste.
- **`submission/`:** `course_ratings.csv` (100 cursos; `course_id`, `title`, `programming_language`, `rating_count`, `average_rating`). No hay `questions.json`.
- **Pruebas:** `test_01` verifica que existe `course_ratings.csv`; no verifica columnas, número de filas, conciliación ni orden.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de P503–P507:** práctica de consultar SQLite desde pandas y agregar con `GROUP BY`; no consume artefactos.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P510 está mapeada a `data.C01`–`data.C05`. C01 se evidencia en la pregunta y la elección del grano curso; C02 en la carga y agregación; C03 de forma parcial (conciliación de conteos, rango de promedios), sin examinar faltantes de lenguaje ni el sesgo de usar calificaciones como adopción; C04 de forma débil (sin manifiesto ni documentación de la decisión de imputar 0); C05 en el uso de SQLite como medio. El producto es una tabla comparativa para una decisión declarada; SQL sirve a ese producto. Auditoría 5: la actividad podría leerse como ejercicio de SQL de agregación si no se explicita la regla de priorización; el riesgo es moderado porque la pregunta y el cambio de grano están ligados a la decisión.
