# P432 — DuckDB transformation: agregación por fábrica declarada en SQL

## Actividad actual implementada

**Implementación:** `implementation/productos/P432_duckdb_transformation/`.

### Preguntas analíticas actuales

- ¿Cómo se declara la transformación que produce los totales por fábrica como una consulta SQL revisable y repetible, ejecutada directamente sobre el CSV?

`professor/main.py` define `build_factory_totals`, que ejecuta con `duckdb.execute` una consulta parametrizada `SELECT factory_id, SUM(daily_units_produced) … FROM read_csv_auto(?) GROUP BY factory_id ORDER BY factory_id` sobre `data/daily_operations.csv` y devuelve tuplas. `main` las guarda como `submission/factory_totals.json`: `[[1, 9303], [2, 9300]]`. No hay `HOW_TO_RUN_ME.txt`; hay `requirements.txt` local con `duckdb==1.4.4`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/factory_totals.json`, totales por fábrica producidos por SQL.
- **Uso y límite:** muestra que la transformación puede declararse en SQL y aplicarse al archivo sin carga previa. La salida pierde los nombres de columna (listas posicionales), a diferencia de P412/P418, que persistían registros con nombre; el resultado numérico es idéntico al de las actividades previas.
- **Disciplinas contribuyentes:** SQL analítico embebido (DuckDB).

### Highlights de contribución

- **H01 — Declara la transformación como SQL parametrizado sobre un archivo:** consulta con `read_csv_auto(?)` y el parámetro de ruta; la docstring afirma que «puede revisarse y repetirse sin pasos manuales». La prueba de profesor la aplica a un CSV temporal con fábricas `A`/`B` y exige `[("A", 8), ("B", 12)]`, lo que verifica agrupación y orden. Primera aparición de SQL como lenguaje de transformación en el curso. Sin este hito, P433 introduciría dbt sin el paso intermedio de una consulta directa.
- **H02 — Caso y datos (límite):** el grano máquina–fábrica del extracto se colapsa a fábrica con `SUM`; es la misma transformación de P400–P431 y el extracto no tiene fecha, de modo que no hay ventana ni deduplicación que el SQL deba expresar. La implementación no revela una particularidad que cambie la representación; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** DuckDB en proceso; `read_csv_auto`; consulta parametrizada; inyección de ruta para pruebas.
- **Reutiliza:** `daily_operations.csv` y la agregación por fábrica.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Transformación SQL | H01 | `GROUP BY`/`ORDER BY` sobre `read_csv_auto` | Una consulta; sin pruebas de datos en SQL. |
| Caso | H02 | Mismo extracto estático | Salida sin nombres de columna. |

### Relación técnica con actividades anteriores

Misma pregunta, mismo dato y mismo resultado que P400, P412, P413, P417, P418, P428 y P429, con un nuevo lenguaje de transformación. Es una reimplementación más de la suma por fábrica, presente con el mismo archivo desde P400 (también en P414–P416); posible duplicación de caso que requiere decisión posterior. Prepara P433, que expresa la misma consulta como modelo dbt sobre DuckDB.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — SQL parametrizado | S02, S04 | `implementation/productos/P432_duckdb_transformation/professor/main.py`: `build_factory_totals`; `implementation/productos/P432_duckdb_transformation/professor/test_main.py` | Prueba sobre datos propios. |
| H02 — Caso como límite | S01, S03 | `implementation/productos/P432_duckdb_transformation/data/daily_operations.csv`; `implementation/productos/P432_duckdb_transformation/submission/factory_totals.json` | Ausencia de particularidad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/daily_operations.csv` | Idéntico a actividades previas. |
| S02 | Consulta | `professor/main.py`; `requirements.txt` | Una consulta; manifiesto local `duckdb==1.4.4`. |
| S03 | Salida | `submission/factory_totals.json` | Listas posicionales. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** ejecuta la consulta sobre el CSV y guarda el resultado.
- **`submission/`:** `factory_totals.json`.
- **Pruebas:** `test_01` exige el archivo; la prueba de profesor verifica la consulta sobre un CSV temporal. No verifican el contenido entregado.
- **Trazabilidad:** P432 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P400–P431:** el mismo dato y la misma agregación.
- **Habilita para P433:** la misma agregación expresada en SQL sobre DuckDB, ahora como modelo dbt.

## Trazabilidad y auditoría

P432 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en una transformación declarativa y repetible; C05 no tiene sustento observable (no hay monitoreo, linaje ni gobierno). Auditoría de identidad (pregunta 5): con el mismo cálculo trivial y sin usuario, el taller se lee como introducción a DuckDB/SQL. Riesgo de identidad registrado.
