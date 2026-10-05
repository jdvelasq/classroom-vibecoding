# P107 — Limpieza de datos con SQLite

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P107_limpieza_sql/`.

### Preguntas analíticas actuales

- No hay una pregunta analítica declarada. La pregunta operativa es la de P106: ¿cómo obtener una tabla de compras con valores canónicos, fechas ISO y magnitudes comparables, ahora mediante una base SQLite?

Usa el mismo `data/ventas.csv` de P106. El script del profesor lee todo como texto, normaliza los encabezados, carga una tabla `raw_sales` en `temp/ventas.db`, registra ocho funciones Python como funciones SQL y crea `cleaned_sales` con una única sentencia `CREATE TABLE ... AS SELECT`. El resultado se exporta a `submission/ventas.csv`. Las reglas de limpieza residen en las funciones Python; SQL actúa como capa declarativa que las orquesta columna por columna.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** capacidad de datos: la misma tabla limpia de P106, con importes, precios y unidades como números de punto flotante.
- **Uso y límite:** conserva el dato crudo y el limpio como tablas separadas dentro de una base local. Hereda los límites de P106 (sin fuente verdadera, ambigüedad de fechas). La columna `country` se asigna como constante `'COL'`, no se deriva del dato.
- **Disciplinas contribuyentes:** bases de datos (SQLite, funciones definidas por el usuario) y preparación de datos.

### Highlights de contribución

- **H01 — Ingiere todo como texto para controlar explícitamente faltantes y conversiones (caso y datos):** el archivo mezcla vacíos, `N/A`, números con separadores ambiguos y unidades; `pd.read_csv(..., dtype=str, keep_default_na=False)` impide que pandas infiera tipos o convierta `N/A` en faltante, y cada función `normalize_*` decide qué valores son nulos (`""`, `N/A`, `nan`) y cuándo convertir a `float`. Contrasta con P106, que dependía de la inferencia por defecto de pandas. Sin este hito, el tratamiento de faltantes quedaría implícito en el lector.
- **H02 — Declara la limpieza como una consulta SQL sobre funciones registradas:** `database.create_function` registra `normalize_supplier`, `normalize_city`, `normalize_date`, `normalize_number`, `normalize_discount`, `normalize_unit_price`, `normalize_weight` y `normalize_units`; `CREATE TABLE cleaned_sales AS SELECT` aplica una función por columna junto con `CAST` y `TRIM`. `raw_sales` permanece intacta. Sin este hito no aparecería la separación entre capa cruda y capa limpia en una base de datos. Límite: la lógica de limpieza no está escrita en SQL.
- **H03 — Canoniza por clave en minúsculas en lugar de enumerar variantes:** `SUPPLIER_NAMES` usa como clave el nombre normalizado en minúsculas, de modo que las variantes que difieren sólo en mayúsculas colapsan en una entrada; la ciudad usa el mismo patrón. Frente a los diccionarios de P106, reduce el número de variantes a mantener. Límite: un valor desconocido pasa con su forma original; el país no se normaliza sino que se fija como `'COL'`, por lo que la aserción de país de la prueba se cumple por construcción.
- **H04 — Mantiene el contrato de salida de P106 con otra implementación:** la prueba es idéntica a la de P106; el CSV resultante cumple las mismas invariantes con representación distinta (`480000.0` frente a `480000`). Sin este hito no habría contraste entre dos implementaciones del mismo producto. Límite: las pruebas no detectan diferencias de tipo ni de valores entre ambas.

### Inventario técnico de implementación

- **Introduce:** lectura como texto sin valores NA por defecto, `sqlite3.Connection.create_function`, `CREATE TABLE ... AS SELECT` con funciones definidas por el usuario, `with sqlite3.connect(...)`, eliminación previa de la base con `unlink(missing_ok=True)`.
- **Extiende de P106:** las mismas reglas (separadores de fecha, años de dos dígitos, regla día/mes > 12, conversión g/kg/ton, descuento > 1 como porcentaje) reescritas como funciones escalares por valor.
- **Reutiliza de P104:** `to_sql` y `pd.read_sql_query`.
- **No incluye:** script de diagnóstico (a diferencia de P106).
- **Interfaz de estudiante:** `src/main.py` es un esqueleto con `NotImplementedError`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Control explícito de faltantes | H01 | `dtype=str`, `keep_default_na=False`, nulos decididos por función | `professor/main.py`; sin prueba de faltantes. |
| Capa cruda y capa limpia en SQLite | H02 | UDF registradas y `CREATE TABLE AS SELECT` | `professor/main.py`, `temp/ventas.db`; lógica en Python. |
| Canonización por clave normalizada | H03 | Diccionario con claves en minúsculas | `professor/main.py`; país constante. |
| Contrato compartido con P106 | H04 | Prueba idéntica | `tests/test_activity.py`; no compara implementaciones. |

### Relación técnica con actividades anteriores

Misma pregunta, mismos datos y mismo contrato que P106 con nueva implementación, en paralelo a la relación P103 → P104. A diferencia de P104, donde las agregaciones se escriben en SQL, aquí SQL sólo orquesta funciones Python; el contraste de herramienta es más débil que el nombre sugiere. Existe solapamiento de producto con P106 que corresponde decidir a una revisión de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Ingesta como texto | S01, S02 | `implementation/descriptiva/P107_limpieza_sql/data/ventas.csv`; `implementation/descriptiva/P107_limpieza_sql/professor/main.py`: `read_csv(..., dtype=str, keep_default_na=False)`, funciones `normalize_*` | No hay prueba específica de faltantes. |
| H02 — Limpieza declarada en SQL | S02, S03 | `implementation/descriptiva/P107_limpieza_sql/professor/main.py`: `create_function`, `CREATE TABLE cleaned_sales AS SELECT`; `implementation/descriptiva/P107_limpieza_sql/temp/ventas.db` | Las reglas residen en Python. |
| H03 — Canonización por clave en minúsculas | S02, S05 | `implementation/descriptiva/P107_limpieza_sql/professor/main.py`: `SUPPLIER_NAMES`, `normalize_city`, `'COL' AS country`; `implementation/descriptiva/P107_limpieza_sql/tests/test_activity.py` | La prueba de país no puede fallar con esta implementación. |
| H04 — Contrato compartido con P106 | S04, S05 | `implementation/descriptiva/P107_limpieza_sql/submission/ventas.csv`; `implementation/descriptiva/P107_limpieza_sql/tests/test_activity.py`; `implementation/descriptiva/P106_limpieza_pandas/tests/test_activity.py` | No se comparan valores entre P106 y P107. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sucio | `data/ventas.csv` | Igual a P106; sin procedencia ni fuente limpia. |
| S02 | Funciones de normalización | `professor/main.py` | Python por valor; país constante. |
| S03 | Base local cruda/limpia | `temp/ventas.db` | Versionada; se recrea en cada ejecución. |
| S04 | Producto limpio | `submission/ventas.csv` | Números como `float`. |
| S05 | Pruebas | `tests/test_activity.py` | Idéntica a P106; no hay `conftest.py`. |
| S06 | Interfaz de estudiante | `src/main.py` | Esqueleto; sin instrucciones ni notebook. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe crear `raw_sales` y `cleaned_sales` en `temp/ventas.db` y exportar la tabla limpia.
- **`submission/`:** `ventas.csv` (103 registros, 11 columnas).
- **Pruebas:** las mismas invariantes que P106. No ejecutan el código, no verifican el uso de SQLite ni la canonización de proveedores, importes o fechas válidas.
- **Trazabilidad:** P107 mapea `descriptiva.C02` y `descriptiva.C05`.

### Dependencias en la secuencia

- **Recibe de P106:** datos, reglas de limpieza y contrato de prueba; **de P104:** práctica de `to_sql` y `read_sql_query`.
- **Habilita para P109:** la práctica de registrar una función Python en SQLite con `create_function` reaparece en P109 (`pseudonymize`); no hay artefacto compartido.

## Trazabilidad y auditoría

P107 está mapeada a `descriptiva.C02` y `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`, con el mismo respaldo que P106: calidad de datos para C02 y respaldo débil para C05. El producto es idéntico al de P106 y la contribución distinguible es de bases de datos (UDF, separación crudo/limpio). La actividad no responde la pregunta descriptiva del curso; aislada, es preparación de datos con SQLite.
