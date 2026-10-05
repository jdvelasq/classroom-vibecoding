# P508 — Consulta parametrizada y extracto de entrega con SQLAlchemy

## Actividad actual implementada

**Implementación:** `implementation/data/P508_scopus_sqlalchemy/`.

### Preguntas analíticas actuales

- ¿Qué fuentes concentran documentos de proptech publicados desde 2020?

Usa `data/scopus_proptech.db` (mismo tamaño que la base de P503) y `data/search_string.txt`. `professor/notebook.ipynb` crea dos `engine` SQLAlchemy (`create_engine("sqlite:///...")`): uno de origen y otro de entrega. Inspecciona las tablas, ejecuta una consulta `text()` con el parámetro `:first_year` (valor 2020) que cuenta documentos distintos por fuente con `LIMIT 20`, escribe el resultado en la tabla `recent_sources` de `submission/scopus_delivery.db` y en `recent_sources.csv`, vuelve a consultar la base de entrega y libera ambos engines con `dispose()`. `recent_sources.csv` tiene 21 líneas; sus primeras filas difieren del ranking de todo el periodo de P505 («Sustainability (Switzerland)» baja de 8 a 6 documentos y «Property Management», 6, entra entre las cinco primeras). El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** concentración reciente de documentos por fuente; el consumidor es «otra aplicación», no identificada.
- **Producto terminal:** extracto de entrega (`scopus_delivery.db`) y CSV equivalente con el ranking de fuentes desde 2020.
- **Uso y límite:** permite separar el producto del origen y cambiar el periodo sin reescribir la consulta. No hay consumidor implementado, ni documentación del extracto (grano, origen, fecha), y el ranking comparte los límites de P505 (tipos documentales mezclados, corte en 20).
- **Disciplinas contribuyentes:** SQLAlchemy y SQLite como capa de acceso; el patrón de extracto de entrega proviene de ingeniería de software y datos.

### Highlights de contribución

- **H01 — Separa el acceso a datos del motor concreto mediante un engine:** `create_engine(f"sqlite:///{SOURCE_DATABASE}")`, conexiones en bloques `with source_engine.connect()` y `dispose()` al final; el comentario «SQLite hoy ──► SQLAlchemy engine ──► otra base compatible mañana» declara la intención. Primer uso de una capa de abstracción en el curso (P503–P507 usan `sqlite3`). Sin este hito, el curso no mostraría el acceso independiente del motor; la portabilidad, sin embargo, no se demuestra con otro motor.
- **H02 — Parametriza el periodo y muestra que cambia la respuesta (caso y datos):** `WHERE d.publication_year >= :first_year` con `params={"first_year": 2020}` separa la pregunta de su valor. En un corpus que abarca desde 1969, la ventana temporal altera la concentración por fuente: frente al ranking de todo el periodo de P505, «Sustainability (Switzerland)» pasa de 8 a 6 documentos y «Property Management» aparece entre las cinco primeras. Extiende el filtro fijo de P504 y la consulta de fuentes de P505. Sin este hito, el periodo seguiría incrustado en el SQL. Límite: el contraste con P505 no se persiste ni se comenta en el notebook.
- **H03 — Persiste un extracto separado del origen y lo verifica por reconsulta:** `recent_sources.to_sql("recent_sources", delivery_engine, if_exists="replace")` crea `scopus_delivery.db` (8192 bytes) y la celda siguiente lo consulta de nuevo «para confirmar que el artefacto puede vivir fuera del origen». Primera entrega en el curso que separa base de origen y base de producto. Sin este hito, las respuestas sólo existirían como CSV o dentro de la base completa. Límite: la verificación es visual en el notebook; ninguna prueba la repite.

### Inventario técnico de implementación

- **Introduce:** `sqlalchemy.create_engine`, `text()`, parámetros nombrados (`:first_year`, `params=`), gestión de conexiones con `with` y `dispose()`.
- **Introduce:** escritura de un DataFrame en una base de entrega independiente (`to_sql` con engine) y reconsulta de verificación.
- **Reutiliza:** consulta de fuentes con `JOIN` y `COUNT(DISTINCT ...)` (P505), filtro desde 2020 (P504), `sqlite_master` (P504), `questions.json`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Capa de acceso independiente del motor | H01 | Engine SQLAlchemy sobre SQLite | Portabilidad declarada, no demostrada. |
| Consulta parametrizada por periodo | H02 | `:first_year` = 2020 | Un solo valor ejecutado. |
| Extracto de entrega verificado | H03 | `scopus_delivery.db` con `recent_sources` | Consumidor no identificado; sin documentación del extracto. |

### Relación técnica con actividades anteriores

Misma pregunta de concentración por fuente que P503/P505, con nuevo dato (periodo desde 2020) y nueva exigencia de producto (extracto separado). El método de acceso cambia de `sqlite3` a SQLAlchemy. Frente a P501, que ya publicaba agregados en una base SQLite para un consumidor declarado, P508 repite la idea de base de entrega en otro caso; el manifiesto de P501 no tiene equivalente aquí. Posible solapamiento de producto con P501 y de pregunta con P505, a decidir a nivel de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Engine | S02 | `implementation/data/P508_scopus_sqlalchemy/professor/notebook.ipynb` (celdas `create_engine`, `connect`, `dispose`) | Sólo SQLite. |
| H02 — Parámetro de periodo (caso y datos) | S01, S02, S03 | `implementation/data/P508_scopus_sqlalchemy/professor/notebook.ipynb` (consulta `recent_sources`); `implementation/data/P508_scopus_sqlalchemy/submission/recent_sources.csv`; contraste: `implementation/data/P505_scopus_sql_intermedio/submission/sources_by_documents.csv` | Contraste hecho en esta descripción, no en la actividad. |
| H03 — Extracto verificado | S03 | `implementation/data/P508_scopus_sqlalchemy/professor/notebook.ipynb` (celdas `to_sql` y reconsulta); `implementation/data/P508_scopus_sqlalchemy/submission/scopus_delivery.db` | Base binaria; contenido descrito desde el código. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/scopus_proptech.db`; `data/search_string.txt` | Copia de la base de P503. |
| S02 | Acceso y consulta | `professor/notebook.ipynb` | Engine SQLite; parámetro único. |
| S03 | Producto de entrega | `submission/scopus_delivery.db`; `submission/recent_sources.csv`; `submission/questions.json` | Sin consumidor ni documentación del extracto. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia de tres archivos. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/notebook.ipynb` debe conectarse por engine, ejecutar la consulta parametrizada, escribir el extracto en una base separada y reconsultarlo.
- **`submission/`:** `scopus_delivery.db` (tabla `recent_sources`), `recent_sources.csv`, `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige existencia; no abre la base de entrega, no verifica la tabla, el parámetro ni la equivalencia CSV–base.
- **Trazabilidad:** `data.C01`, `data.C02`, `data.C04`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P503–P505:** base (P503), filtro desde 2020 e inspección de `sqlite_master` (P504), consulta de fuentes con `COUNT(DISTINCT ...)` (P505).
- **Habilita para Pyyy:** no evidenciada dentro de P500–P508.

## Trazabilidad y auditoría

Entrada revisada: P508 → `data.C01`, `data.C02`, `data.C04`, `data.C05`. C02 tiene evidencia. C05 se evidencia en la intención declarada de independencia del motor. C01 es débil: el parámetro separa la pregunta de su valor, pero no se derivan requisitos de datos. `data.C04` es débil: el extracto no lleva documentación de grano, origen ni fecha (a diferencia del manifiesto de P501). El producto es un extracto de entrega para un consumidor no identificado. Pregunta 5: el nombre de la actividad es el de la herramienta y su contribución distintiva (engine, conexiones, `dispose`) es técnica; la pregunta repite la de P505. Riesgo de identidad alto: puede describirse como entrenamiento en SQLAlchemy.
