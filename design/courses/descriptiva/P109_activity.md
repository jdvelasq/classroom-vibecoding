# P109 — Anonimización de perfiles de clientes con SQLite

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P109_anonimizacion_sql/`.

### Preguntas analíticas actuales

- ¿Cómo compartimos perfiles de clientes sin permitir su reidentificación mediante cuasi-identificadores? (declarada en la primera celda del notebook del profesor).
- ¿Cuántos registros anonimizados son candidatos para cada perfil de la fuente auxiliar? (inferida de la consulta de ataque).

Usa los mismos `raw.csv` (600 clientes) y `auxiliary.csv` (20 perfiles) que P108. El notebook carga ambas tablas en `temp/anonimizacion.db`, registra la seudonimización HMAC como función SQL y produce en una única sentencia `CREATE TABLE ... AS SELECT` el estado final de P108: tarjeta enmascarada, seudónimo, grupo de edad, región y grupo ocupacional. Una consulta con CTE aplica las mismas generalizaciones a la tabla auxiliar y cuenta candidatos por nombre. La entrega es `submission/anonymized.csv`, idéntica en contrato (y en tamaño, 44.230 bytes) a la de P108.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta declarada sobre compartir perfiles; destinatario y uso analítico no evidenciados.
- **Producto terminal:** capacidad de datos: el mismo conjunto compartible de P108, producido con reglas SQL.
- **Uso y límite:** las reglas de anonimización quedan legibles en una sola consulta y la verificación de enlace en otra. A diferencia de P108, no hay demostración del ataque ingenuo, verificación paso a paso ni comparación de utilidad. Hereda los límites de P108: `annual_spend` exacto, clave en el código, riesgo evaluado sólo con 20 perfiles y sin garantía formal.
- **Disciplinas contribuyentes:** privacidad de datos y bases de datos (SQL con `CASE`, CTE, funciones definidas por el usuario).

### Highlights de contribución

- **H01 — Formula explícitamente la pregunta que orienta la transformación:** la primera celda abre con «¿Cómo compartimos perfiles de clientes sin permitir su reidentificación mediante cuasi-identificadores?», y cada celda posterior comienza con la razón del paso. Es la primera pregunta declarada en P100–P109. Sin este hito, la anonimización se presentaría como receta técnica y no como respuesta a una condición de uso.
- **H02 — Declara todas las reglas de anonimización en una sola transformación SQL:** `CREATE TABLE anonymized_customers AS SELECT` combina `printf('********%04d', ... % 10000)` para la máscara, `pseudonymize(document_id)` registrada con `create_function`, y expresiones `CASE` para edad, región (directamente desde la ciudad, sin el nivel departamento de P108) y grupo ocupacional. Misma política final que P108 con nueva implementación. Sin este hito, las reglas seguirían dispersas en pasos sucesivos.
- **H03 — Evalúa el riesgo residual con una consulta de enlace:** una CTE (`auxiliary_groups`) aplica a la tabla auxiliar las mismas reglas `CASE`, une con `JOIN ... USING (age_group, region, occupation_group)` y cuenta `candidate_records` por nombre, ordenando de menor a mayor. Contrasta con P108, que medía únicos tras cada paso. Sin este hito, la entrega SQL carecería de verificación de riesgo. Límite: al ser un `INNER JOIN`, los perfiles sin candidatos no aparecen; sólo se muestra `head()` y no se persiste.
- **H04 — Preserva el orden de los registros porque el contrato lo exige (caso y datos):** la prueba compara `annual_spend` y la máscara posición a posición con `raw.csv`, pero una tabla SQL no garantiza orden. El notebook añade `row_id` con `reset_index(names="row_id")` al cargar, lo arrastra a la tabla anonimizada y exporta con `ORDER BY row_id`, sin incluirlo en la entrega. Sin este hito, una salida correcta en contenido podría fallar o desalinearse respecto del origen.
- **H05 — Localiza la raíz de la actividad de forma portable:** `find_activity_root()` recorre el directorio actual y sus padres hasta encontrar `data/` y `submission/`, en lugar de usar rutas relativas `../`. Primera aparición en la secuencia; sin este hito el notebook dependería del directorio desde el que se ejecute.

### Inventario técnico de implementación

- **Introduce:** `reset_index(names=...)` como clave de orden, `printf` y aritmética modular en SQLite, `CASE ... WHEN ... BETWEEN`, `JOIN ... USING`, búsqueda portable de la raíz con `pathlib`.
- **Reutiliza de P107:** `create_function` para exponer una función Python en SQL; **de P104:** CTE, `to_sql`, `read_sql_query`; **de P108:** reglas finales, clave HMAC y formato del seudónimo.
- **No incluye:** ataque ingenuo, generalización iterativa, conteo de únicos por paso ni comparación de utilidad (presentes en P108).
- **Interfaz de estudiante:** `notebooks/notebook.ipynb` vacío.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Pregunta de uso declarada | H01 | Pregunta en la primera celda | `professor/notebook.ipynb`; sin destinatario. |
| Reglas de anonimización en SQL | H02 | `CASE`, `printf`, UDF HMAC en `CREATE TABLE AS SELECT` | `professor/notebook.ipynb`, `submission/anonymized.csv`; clave en el código. |
| Verificación de enlace en SQL | H03 | CTE + `JOIN USING` + `COUNT(*)` por nombre | Notebook; sin persistencia; omite perfiles sin candidatos. |
| Orden y portabilidad | H04, H05 | `row_id`, `ORDER BY`; `find_activity_root()` | Notebook; prueba posicional en `tests/test_activity.py`. |

### Relación técnica con actividades anteriores

Misma pregunta, mismos datos y mismo contrato que P108 con nueva implementación, en paralelo a P103→P104 y P106→P107. A diferencia de P107, aquí las reglas de generalización sí se escriben en SQL; sólo la seudonimización es una función Python. Pierde respecto de P108 la demostración del ataque ingenuo y el contraste riesgo-utilidad, y gana una pregunta declarada, una política en una sola consulta y portabilidad de rutas. El producto duplica el de P108; la decisión sobre su coexistencia corresponde a una revisión de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Pregunta declarada | S02, S06 | `implementation/descriptiva/P109_anonimizacion_sql/professor/notebook.ipynb`: primera celda y comentarios iniciales | No identifica destinatario ni uso. |
| H02 — Reglas en una consulta SQL | S02, S04 | `implementation/descriptiva/P109_anonimizacion_sql/professor/notebook.ipynb`: `create_function("pseudonymize", ...)`, `CREATE TABLE anonymized_customers`; `implementation/descriptiva/P109_anonimizacion_sql/submission/anonymized.csv` | Clave en el código. |
| H03 — Consulta de enlace | S03 | `implementation/descriptiva/P109_anonimizacion_sql/professor/notebook.ipynb`: `attack_candidates` | No se persiste; no se citan conteos. |
| H04 — Orden de registros | S01, S04, S05 | `implementation/descriptiva/P109_anonimizacion_sql/professor/notebook.ipynb`: `reset_index(names="row_id")`, `ORDER BY row_id`; `implementation/descriptiva/P109_anonimizacion_sql/tests/test_activity.py`: `test_02` | La prueba no indica la razón del orden. |
| H05 — Raíz portable | S06 | `implementation/descriptiva/P109_anonimizacion_sql/professor/notebook.ipynb`: `find_activity_root()` | Sólo en el notebook del profesor. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y carga a SQLite | `data/raw.csv`; `data/auxiliary.csv`; `temp/anonimizacion.db` | Iguales a P108; base versionada. |
| S02 | Reglas SQL de anonimización | `professor/notebook.ipynb` | Reglas `CASE` duplicadas en la consulta de ataque; clave en el código. |
| S03 | Verificación de riesgo | `professor/notebook.ipynb` (`attack_candidates`) | `INNER JOIN`; sólo `head()`. |
| S04 | Producto compartible | `submission/anonymized.csv` | Mismo contrato que P108. |
| S05 | Pruebas | `tests/test_activity.py` | Idénticas en contenido a P108. |
| S06 | Interfaz y portabilidad | `notebooks/notebook.ipynb`; `find_activity_root()` | Notebook de estudiante vacío. |

### Contrato de evidencia actual

- **Notebook o código:** carga tablas, registra `pseudonymize`, crea `anonymized_customers`, consulta candidatos y exporta ordenado por `row_id`.
- **`submission/`:** `anonymized.csv` (600 filas, seis columnas; mismas primeras filas que P108).
- **Pruebas:** las mismas de P108 (forma, máscaras, seudónimos, dominios, igualdad posicional de `annual_spend`). No verifican uso de SQL, riesgo de reidentificación ni la consulta de ataque.
- **Trazabilidad:** P109 mapea sólo `descriptiva.C05`.

### Dependencias en la secuencia

- **Recibe de P108:** datos, reglas finales, clave y formato del seudónimo, contrato de prueba; **de P107:** `create_function`; **de P104:** CTE y `read_sql_query`.
- **Habilita para Pyyy:** no evidenciada mediante artefacto; los talleres P120 en adelante usan otros datos y no reutilizan el conjunto anonimizado.

## Trazabilidad y auditoría

P109 está mapeada a `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. El respaldo es el mismo que en P108 para la dimensión responsable (reglas explícitas y verificación de enlace), con menor evidencia de contraste riesgo-utilidad. La pregunta declarada acerca la actividad a un contexto de uso, pero no identifica usuario ni decisión. El producto es una capacidad de datos; aislada, la actividad es una práctica de privacidad con SQL, y su relación con la descripción posterior no queda evidenciada en el curso.
