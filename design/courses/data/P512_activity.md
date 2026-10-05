# P512 — Warehouse Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P512_superstore_warehouse/`.

### Preguntas analíticas actuales

- ¿Cómo se organizan ventas y utilidad por fecha, cliente, producto y geografía sin perder el grano de línea de orden?

La pregunta abre `professor/notebook.ipynb`. Usa las mismas cuatro tablas derivadas y el mismo `source_manifest.json` que P511 (copias idénticas). Construye `dim_date` a partir de los valores distintos de `Order Date` (texto `d/m/yy` convertido con `format="%d/%m/%y"`), con `date_key` asignado por orden de aparición, año y mes; usa `customers` y `products` tal como vienen como `dim_customer` y `dim_product` (claves contextuales del manifiesto); y crea `fact_sales` añadiendo `date_key` a `order_lines`. Persiste las cuatro tablas en `submission/superstore_mart.db` y ejecuta una consulta año × mes × categoría con uniones `USING`, cuyo resultado sólo se muestra (`monthly.head()`), no se persiste. La tabla `orders` no se escribe en el mart: `Order ID`, `Ship Date`, `Order Priority` y `Ship Mode` no quedan disponibles. La geografía no es una dimensión propia; está dentro de `dim_customer`. El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta de organización de datos; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/superstore_mart.db` con `fact_sales`, `dim_date`, `dim_customer` y `dim_product`; capacidad de datos para agregaciones repetibles.
- **Uso y límite:** permite agregar ventas y utilidad por fecha de orden, atributos de cliente (incluida geografía) y producto sin volver a integrar. No permite contar órdenes distintas (la métrica `order_count` de P500 no es reconstruible) ni analizar envíos. `dim_date` sólo contiene días con órdenes, no un calendario. Las tablas se crean con `to_sql`, sin claves primarias ni foráneas declaradas.
- **Disciplinas contribuyentes:** modelado dimensional (BI) y SQLite sirven a una capacidad de consulta descriptiva.

### Highlights de contribución

- **H01 — Deriva una dimensión de fecha desde texto ambiguo `d/m/yy` (caso y datos):** las fechas de Superstore llegan como texto día/mes/año de dos dígitos; la dimensión fija el formato al convertir y deriva `year` y `month`, y el hecho la referencia por `date_key` mediante una unión `many_to_one` con `orders`. Primera dimensión temporal explícita del curso (P500 y P501 derivaban `month` dentro de la agregación). Sin este hito, las comparaciones temporales dependerían de reinterpretar la fecha en cada consulta; su límite es que la dimensión sólo cubre fechas observadas.
- **H02 — Separa hecho y dimensiones conservando el grano línea:** `fact_sales` es `order_lines` más `date_key`, con `assert len(fact_sales) == len(order_lines)`; las medidas quedan en el hecho y los atributos en las dimensiones. Contrasta con P511, que aplana todo en una tabla; y con P501, que persiste agregados ya calculados. Sin este hito, el curso no mostraría una representación que permite reagregar a otros granos sin duplicar atributos.
- **H03 — Persiste un mart y lo consulta en estrella:** cuatro tablas en SQLite y una consulta `fact_sales JOIN dim_date USING(date_key) JOIN dim_product USING(product_context_key)` agrupada por año, mes y categoría. Extiende las uniones SQL de P505–P507 (esquema bibliográfico) a un esquema hecho–dimensiones. Sin este hito, el mart no se conectaría con una consulta analítica.

### Inventario técnico de implementación

- **Introduce:** dimensión de fecha con clave sustituta; tabla de hechos con medidas a grano línea; consulta en estrella con `USING`; identificadores con espacios citados con acentos graves.
- **Extiende:** unión validada y aserción de grano (P511); conversión de fechas con formato explícito (P500).
- **Reutiliza:** persistencia con `to_sql` en SQLite (P501, P503).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Dimensión de fecha | H01 | `dim_date` (fecha, año, mes) desde `Order Date` | Sin calendario completo ni otros atributos temporales. |
| Esquema estrella mínimo | H02, H03 | Hecho + tres dimensiones en `superstore_mart.db` | Sin dimensión de orden ni de geografía; sin PK/FK declaradas. |
| Consulta en estrella | H03 | SQL año × mes × categoría | Resultado no persistido. |

### Relación técnica con actividades anteriores

Mismos datos y mismo grano que P511, con nuevo método de representación (dimensional frente a plana). Frente a P501, cambia de servir agregados a servir detalle reagregable. Frente a P503, el esquema relacional de Scopus declaraba claves primarias y foráneas; el mart de P512 no declara restricciones. La pregunta no es analítica en sentido de negocio: es una pregunta de organización de datos, cercana a la de P501.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Dimensión de fecha | S01, S02 | `implementation/data/P512_superstore_warehouse/data/orders.csv`; `implementation/data/P512_superstore_warehouse/professor/notebook.ipynb`: celda 3 | `date_key` depende del orden de aparición en `orders.csv`. |
| H02 — Hecho a grano línea | S02, S03 | `implementation/data/P512_superstore_warehouse/professor/notebook.ipynb`: celda 4 (`assert`); `implementation/data/P512_superstore_warehouse/submission/superstore_mart.db` | No se verifica integridad referencial dimensión–hecho. |
| H03 — Mart y consulta | S03, S04 | `implementation/data/P512_superstore_warehouse/professor/notebook.ipynb`: celda 4 (SQL); `implementation/data/P512_superstore_warehouse/submission/superstore_mart.db` | El resultado de la consulta no se entrega. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: tablas derivadas de Superstore | `data/*.csv`; `data/source_manifest.json` | Idénticas a P511, P514 y P515. |
| S02 | Representación: modelo dimensional | `professor/notebook.ipynb` | Sin dimensión de orden; geografía dentro de cliente. |
| S03 | Producto: mart SQLite | `submission/superstore_mart.db` | Sin restricciones declaradas; consulta no persistida. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia del archivo. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** construye `dim_date`, une el hecho con validación, verifica filas, persiste cuatro tablas y consulta en estrella.
- **`submission/`:** `superstore_mart.db` (cuatro tablas). No hay CSV de respuesta ni `questions.json`.
- **Pruebas:** `test_01` verifica que existe `superstore_mart.db`; no verifica tablas, grano ni integridad.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de P511:** las mismas tablas derivadas y la práctica de unión `many_to_one` con aserción de grano. **Recibe de P505–P507:** uniones SQL.
- **Habilita para Pyyy:** no evidenciada; ninguna actividad posterior inspeccionada consume `superstore_mart.db`.

## Trazabilidad y auditoría

P512 está mapeada a `data.C01`–`data.C05`. C02 se evidencia con claridad (estructuración dimensional); C01 sólo en la pregunta de organización; C03 en la aserción de grano; C04 en el manifiesto heredado; C05 en SQLite como medio. El producto es una capacidad de datos descriptiva, coherente con el producto terminal del curso. Auditoría 5: la pregunta es de modelado y el resultado de la consulta no se entrega, de modo que la actividad puede leerse como taller de modelado dimensional. Tras la aclaración del profesor (2026-10-05), almacenes y marts pertenecen al curso como puente hacia la analítica, por lo que esa lectura ya no es por sí sola un problema de identidad: el mart sirve a agregaciones descriptivas repetibles. Se conservan como límites que la consulta no se persiste y que la pérdida del contexto de orden (`order_count` no reconstruible, envíos fuera del mart) limita el uso analítico del mart.
