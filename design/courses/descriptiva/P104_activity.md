# P104 — Resumen de conductores con SQLite

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P104_drivers_sqlite/`.

### Preguntas analíticas actuales

Inferidas de los comentarios de las celdas; son las mismas de P103:

- ¿Cuál es la media de horas y millas por conductor?
- ¿En qué semanas un conductor registró menos horas que su propia media?
- ¿Cuántas horas y millas acumuló cada conductor y cuál fue su rango de horas?
- ¿Qué diez conductores registraron más millas?

Usa los mismos `drivers.csv` y `timesheet.csv` que P103. Los carga en una base SQLite local (`temp/db.sqlite`), crea vistas con nombres normalizados y responde las preguntas con consultas SQL leídas en pandas. El producto es el mismo resumen y el mismo gráfico de P103, con nombres de columna en `snake_case`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** iguales a P103; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/summary.csv` (`driver_id`, `hours_logged`, `miles_logged`, `name`) y `submission/top10_drivers.png`, con los mismos valores que P103.
- **Uso y límite:** muestra que el mismo resumen descriptivo puede expresarse declarativamente y conservarse como vista. Hereda los límites de P103: sin normalización, sin interpretación, sin usuario.
- **Disciplinas contribuyentes:** bases de datos (SQL, vistas, funciones de ventana, CTE) al servicio del mismo producto descriptivo.

### Highlights de contribución

- **H01 — Reexpresa el mismo resumen con SQL declarativo y lo contrasta con pandas:** `GROUP BY` con `AVG`, `SUM`, `MIN` y `MAX` reemplaza las operaciones de P103; `test_02` calcula el resultado esperado con pandas y lo compara con el CSV producido por SQL. Misma pregunta con nueva implementación; sin este hito no habría una verificación cruzada entre herramientas.
- **H02 — Normaliza nombres incómodos con vistas sin alterar las tablas cargadas (caso y datos):** las columnas fuente usan guiones (`hours-logged`, `wage-plan`), que en SQL exigen comillas; el notebook guarda `drivers_raw` y `timesheet_raw` tal como llegan y crea las vistas `drivers` y `timesheet` con `driver_id`, `wage_plan`, `hours_logged`, `miles_logged`. Esta particularidad de los nombres cambia el contrato de salida, que la prueba exige con los nombres nuevos. Sin este hito no se vería la separación entre dato crudo y capa de consulta. Límite: la vista `drivers` sigue exponiendo `ssn` y `location`.
- **H03 — Calcula la comparación intra-grupo con una función de ventana:** `AVG(hours_logged) OVER (PARTITION BY driver_id)` reproduce el `transform("mean")` de P103 sin reducir filas, y una CTE con `WHERE hours_logged < mean_hours_logged` filtra las semanas. Sin este hito, la diferencia entre agregación que reduce y agregación que conserva filas no tendría su equivalente SQL. Límite: no se persiste ni se prueba.
- **H04 — Encapsula el resumen como vista reutilizable:** `driver_summary` une `timesheet` y `drivers` con `INNER JOIN` y agrupa por conductor; la misma vista alimenta `summary.csv` y la consulta del top 10 (`ORDER BY miles_logged DESC LIMIT 10`). La consulta a `sqlite_master` lista tablas y vistas disponibles. Sin este hito, el resumen tendría que recalcularse en cada consulta.

### Inventario técnico de implementación

- **Introduce:** `sqlite3.connect`, `DataFrame.to_sql`, `executescript` con `DROP VIEW IF EXISTS` / `CREATE VIEW`, `pd.read_sql_query`, consulta de catálogo `sqlite_master`, funciones de ventana, CTE, `INNER JOIN`, `ORDER BY ... LIMIT`, cierre explícito de la conexión.
- **Reutiliza de P103:** preguntas, datos, gráfico de barras (mismo código con `miles_logged`) y estructura de pruebas.
- **Persistencia intermedia:** `temp/db.sqlite` (40.960 bytes) versionado.
- **Interfaz de estudiante:** `notebooks/notebook.ipynb` vacío.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Agregación SQL verificada contra pandas | H01, H04 | `GROUP BY`, vista `driver_summary`, `test_02` | `submission/summary.csv`; mismos límites de P103. |
| Capa de vistas sobre datos crudos | H02 | Tablas `_raw` y vistas renombradas | Notebook; no restringe columnas sensibles. |
| Función de ventana | H03 | `AVG ... OVER (PARTITION BY ...)` y CTE | Notebook; sin artefacto. |

### Relación técnica con actividades anteriores

Misma pregunta y mismos datos que P103, con nueva implementación en SQL; el producto y el gráfico son prácticamente idénticos (sólo cambian los nombres de columna). Aporta vistas, ventanas y verificación cruzada. Existe solapamiento de producto con P103 que una revisión de curso podría querer decidir; el contraste de herramientas es la contribución distinguible.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — SQL contrastado con pandas | S02, S05 | `implementation/descriptiva/P104_drivers_sqlite/professor/notebook.ipynb`: consultas `GROUP BY`; `implementation/descriptiva/P104_drivers_sqlite/tests/test_activity.py`: `test_02` | Verifica totales, no medias ni rangos. |
| H02 — Vistas con nombres normalizados | S01, S02, S03 | `implementation/descriptiva/P104_drivers_sqlite/professor/notebook.ipynb`: `CREATE VIEW drivers`, `CREATE VIEW timesheet`; `implementation/descriptiva/P104_drivers_sqlite/submission/summary.csv` | La vista no minimiza campos sensibles. |
| H03 — Función de ventana | S02 | `implementation/descriptiva/P104_drivers_sqlite/professor/notebook.ipynb`: `OVER (PARTITION BY driver_id)`, CTE | Sin persistencia ni prueba. |
| H04 — Vista de resumen reutilizable | S02, S03, S04 | `implementation/descriptiva/P104_drivers_sqlite/professor/notebook.ipynb`: `driver_summary`, consulta top 10, `sqlite_master`; `implementation/descriptiva/P104_drivers_sqlite/submission/top10_drivers.png`; `implementation/descriptiva/P104_drivers_sqlite/temp/db.sqlite` | La prueba de la imagen sólo exige tamaño mínimo. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y carga a SQLite | `data/drivers.csv`; `data/timesheet.csv`; `temp/db.sqlite` | Mismos datos que P103; base en `temp/` versionada. |
| S02 | Consultas, vistas y ventanas | `professor/notebook.ipynb` | Rutas relativas `../temp`, `../data`; tabla bajo la media no persistida. |
| S03 | Resumen persistido | `submission/summary.csv` | Nombres en `snake_case`, exigidos por la prueba. |
| S04 | Visualización | `submission/top10_drivers.png` | Código idéntico al de P103. |
| S05 | Pruebas | `tests/test_activity.py` | Igual a P103 con renombrado de columnas. |
| S06 | Interfaz de estudiante | `notebooks/notebook.ipynb` | Vacío; sin pregunta ni instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** carga tablas crudas, crea vistas, ejecuta consultas de media, ventana, suma, rango y resumen, persiste CSV y gráfico y cierra la conexión.
- **`submission/`:** `summary.csv` (34 filas; p. ej., conductor 10: 3.232 horas, 147.150 millas, igual que P103) y `top10_drivers.png`.
- **Pruebas:** existencia de ambos archivos, igualdad del resumen con un cálculo pandas renombrado y tamaño mínimo de imagen. No verifican el uso de SQL, las vistas ni la ventana.
- **Trazabilidad:** P104 mapea `descriptiva.C02` y `descriptiva.C03`.

### Dependencias en la secuencia

- **Recibe de P103:** preguntas, datos, contrato de `submission/`, código del gráfico y estructura de pruebas.
- **Habilita para Pyyy:** la práctica de consultar SQLite con `pd.read_sql_query` reaparece en P107 y P109 (y en P150–P154 sobre otra base); no hay artefacto compartido.

## Trazabilidad y auditoría

P104 está mapeada a `descriptiva.C02` y `descriptiva.C03` en `implementation/descriptiva/traceability.yaml`; ambas tienen el mismo respaldo que en P103 (agregación y ranking visual). El producto descriptivo es idéntico al de P103; lo que cambia es la disciplina contribuyente (bases de datos). Aislada, la actividad se lee como práctica de SQL; dentro de la secuencia, su valor analítico es mostrar que el resultado no depende de la herramienta. Las mismas limitaciones de identidad de P103 (sin usuario, decisión ni interpretación) se mantienen.
