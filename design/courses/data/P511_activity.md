# P511 — Integración Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P511_superstore_integracion/`.

### Preguntas analíticas actuales

- ¿Qué segmentos, regiones y categorías concentran las ventas y la utilidad de Superstore?

La pregunta abre `professor/notebook.ipynb`. Los datos son cuatro tablas derivadas del extracto `datalabs/commerce/superstore-orders.csv` (URL en `data/source_manifest.json`): `orders.csv` (1857 filas), `customers.csv` (1191), `products.csv` (926) y `order_lines.csv` (1952, el mismo número de líneas que el CSV de P500). El manifiesto declara que las filas se separaron sin inventar ni modificar valores y que `Order ID` no basta como clave: por ejemplo, `86838` aparece dos veces en `orders.csv` con `Ship Date` distinto (14/05/15 y 13/05/15). Por eso las tablas se relacionan mediante claves sustitutas deterministas (`order_context_key`, `customer_context_key`, `product_context_key`) que identifican combinaciones distintas de atributos fuente, no entidades de negocio. Las tablas ya vienen en UTF-8, separadas por coma y con punto decimal; las fechas siguen como texto `d/m/yy`. El notebook reintegra las cuatro tablas al grano línea, agrega por segmento, región y categoría y persiste detalle y respuesta. `submission/sales_by_segment_region_category.csv` tiene 48 combinaciones; la primera es Small Business–East–Office Supplies (ventas 102471.89; utilidad 18035.77; 79 líneas) y entre las cinco primeras Corporate–East–Furniture combina ventas altas (70510.73) con utilidad negativa (−3052.51); el notebook no lo interpreta. El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la pregunta está en el notebook; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/superstore_enriched_sales.csv` (detalle integrado a grano línea) y `submission/sales_by_segment_region_category.csv` (ventas, utilidad y número de líneas por combinación).
- **Uso y límite:** permite identificar combinaciones con mayor volumen y su utilidad. «Concentran» se responde como ranking por ventas; no hay participación relativa ni lectura de márgenes. Los clientes y productos son «contextos», no entidades únicas: contar clientes o productos distintos con esas claves sobrestimaría. El detalle conserva columnas duplicadas `Customer ID_x` y `Customer ID_y` (ambas fuentes traen `Customer ID` y la unión no lo resuelve).
- **Disciplinas contribuyentes:** integración relacional con pandas al servicio de una descripción por segmento, región y categoría.

### Highlights de contribución

- **H01 — Reintegra tablas derivadas mediante claves contextuales porque `Order ID` no es clave (caso y datos):** el manifiesto documenta que una orden puede tener atributos distintos por línea (p. ej., fecha de envío), y la integración usa las claves sustitutas en lugar del identificador de negocio. Primera actividad del curso con fuentes Superstore separadas en tablas y con una decisión de clave documentada en un manifiesto (P500–P502 leen un único CSV desnormalizado). Sin este hito, el estudiante no vería por qué un identificador de negocio no garantiza una unión correcta.
- **H02 — Valida la cardinalidad de cada unión y conserva el grano línea:** tres `merge(..., validate="many_to_one")` encadenados desde `order_lines`, seguidos de `assert len(enriched_sales) == len(order_lines)` y de no nulidad en ventas, utilidad y dimensiones de la respuesta. Primer uso de `validate=` en el curso (P503 usa `merge(..., how="left")` sin validación). Sin este hito, una clave duplicada podría multiplicar líneas e inflar ventas sin advertencia.
- **H03 — Agrega después de integrar y entrega detalle y respuesta:** el comentario «la respuesta se agrega después de integrar las fuentes, no antes» se materializa en un `groupby` de tres dimensiones con `order_lines=("Sales", "size")` y en dos archivos persistidos, uno auditable a grano línea y otro agregado. Extiende la agregación por una dimensión de P501 (`category_sales`) a tres dimensiones de tablas distintas. Sin este hito, la respuesta no podría rastrearse hasta las líneas que la componen.

### Inventario técnico de implementación

- **Introduce:** `merge` con `validate="many_to_one"`; aserción de conservación del grano tras integrar; claves sustitutas documentadas en manifiesto.
- **Extiende:** agregación de ventas y utilidad (P500, P501) a tres dimensiones con conteo de líneas.
- **Reutiliza:** caso Superstore y grano «una fila por producto dentro de una orden» (P500–P502).
- **No ejercita:** conversión de fechas (quedan como texto) ni resolución de columnas homónimas.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Claves sustitutas por combinación de atributos | H01 | `*_context_key` y `key_decision` del manifiesto | La derivación fue hecha por el profesor; el estudiante no la construye. |
| Unión validada que preserva grano | H02 | `validate="many_to_one"` + `assert` de filas | Columnas `Customer ID_x/_y` sin resolver. |
| Detalle y agregado persistidos | H03 | Dos CSV en `submission/` | Ranking sin interpretación de margen. |

### Relación técnica con actividades anteriores

Mismo caso que P500–P502 con nueva representación de entrada: tablas normalizadas por el profesor en lugar del CSV desnormalizado con `;`, `latin1` y coma decimal. La pregunta se acerca a `category_sales` de P501, con nuevo método (integración validada) y más dimensiones. Frente a P503, la dirección es inversa: P503 descompone un export en entidades; P511 recompone tablas en una vista analítica plana. No hay duplicación con actividades anteriores; sí con P514 (ver su descripción).

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Claves contextuales | S01, S02 | `implementation/data/P511_superstore_integracion/data/source_manifest.json`; `implementation/data/P511_superstore_integracion/data/orders.csv` (Order ID 86838 repetido); `implementation/data/P511_superstore_integracion/professor/notebook.ipynb`: celda 2 | El código que generó las tablas derivadas no está en la actividad. |
| H02 — Uniones validadas | S02, S04 | `implementation/data/P511_superstore_integracion/professor/notebook.ipynb`: celdas 3 y 5; `implementation/data/P511_superstore_integracion/submission/superstore_enriched_sales.csv` | No se ejercita un caso que falle la validación. |
| H03 — Agregado tras integrar | S03, S04 | `implementation/data/P511_superstore_integracion/professor/notebook.ipynb`: celda 4; `implementation/data/P511_superstore_integracion/submission/sales_by_segment_region_category.csv` | La utilidad negativa visible no se discute. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: tablas derivadas de Superstore | `data/*.csv`; `data/source_manifest.json` | Idénticas en P512, P514 y P515. |
| S02 | Representación: integración por claves contextuales | `professor/notebook.ipynb` | `Customer ID` duplicado en la salida. |
| S03 | Método: agregación por tres dimensiones | `professor/notebook.ipynb` | Orden por ventas y utilidad; sin participación relativa. |
| S04 | Producto: detalle y respuesta | `submission/superstore_enriched_sales.csv`; `submission/sales_by_segment_region_category.csv` | Sin `questions.json`. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia de dos archivos. |
| S06 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** lee cuatro tablas, integra con validación de cardinalidad, verifica filas y no nulidad, agrega y persiste.
- **`submission/`:** `superstore_enriched_sales.csv` (1952 líneas, 28 columnas) y `sales_by_segment_region_category.csv` (48 filas).
- **Pruebas:** `test_01` y `test_02` verifican sólo que existen los dos archivos; no comprueban grano, columnas ni sumas.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de P500–P502:** caso Superstore y definición de grano (práctica y caso; no consume artefactos).
- **Habilita para P512, P514 y P515:** las mismas cuatro tablas y manifiesto (copias idénticas en sus `data/`); P514 reproduce la misma cadena de uniones validadas y publica un `superstore_enriched_sales.csv` del mismo tamaño y cabecera.

## Trazabilidad y auditoría

P511 está mapeada a `data.C01`–`data.C05`. C01 en la pregunta y la elección del grano; C02 en la integración validada; C03 en la conciencia de clave no única y la no nulidad; C04 en el manifiesto (provisto por el profesor); C05 de forma mínima. El producto es una tabla descriptiva trazable a su detalle; la integración sirve al producto. Auditoría 5: no se lee como Data Engineering; el límite es la falta de lectura analítica de la respuesta.
