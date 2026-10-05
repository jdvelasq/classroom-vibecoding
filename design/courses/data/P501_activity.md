# P501 — Interfaces de consumo (serving) de métricas Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P501_superstore_serving/`.

### Preguntas analíticas actuales

- ¿Qué interfaces permiten responder la evolución mensual de ventas y la contribución de cada categoría?

Parte del mismo `data/superstore_orders.csv` de P500 (una fila por producto dentro de una orden) y `professor/main.py` publica tres representaciones: `sales_detail.csv` (nueve columnas al grano línea-de-orden, 1953 líneas con encabezado), y las tablas `monthly_sales` y `category_sales` dentro de `sales_serving.db` (SQLite). `serving_manifest.csv` declara para cada artefacto grano, interfaz, consumidor («Analista», «Dashboard») y propósito. `questions.json` señala `sales_serving.db` como archivo de respuesta. No hay notebook; `src/main.py` sólo lanza `NotImplementedError`. A diferencia de P500, no se ejecuta ninguna validación.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la pregunta es sobre interfaces para dos preguntas descriptivas (evolución mensual, contribución por categoría). Los consumidores «Analista» y «Dashboard» son etiquetas del manifiesto; no hay dashboard ni usuario implementado.
- **Producto terminal:** capacidad de datos: un detalle trazable y dos agregados consultables, con un manifiesto que documenta su grano y destino.
- **Uso y límite:** permite elegir la representación según la pregunta y el grano requerido. No incluye validación de los datos publicados, no verifica que los agregados reconcilien con el detalle y publica textos mal decodificados (H03).
- **Disciplinas contribuyentes:** pandas y SQLite (`to_sql`) como medios para publicar representaciones; la noción de *serving* proviene de ingeniería de datos y, según la aclaración del profesor (2026-10-05), pertenece al curso como puente hacia la analítica: aquí sirve a hacer consultables dos preguntas descriptivas.

### Highlights de contribución

- **H01 — Separa una misma fuente en representaciones de grano distinto:** `main` escribe el detalle al grano de línea y `build_monthly_sales` y `build_category_sales` cargan agregados mensual y por categoría en `sales_serving.db` con `to_sql(..., if_exists="replace")`. Extiende P500, que producía una sola tabla mensual, hacia varias salidas para preguntas diferentes. Sin este hito, el curso no mostraría que una pregunta determina la representación que se publica.
- **H02 — Documenta grano, interfaz, consumidor y propósito de cada salida:** `build_manifest` persiste `serving_manifest.csv` con cinco columnas (`artifact`, `grain`, `interface`, `consumer`, `purpose`). Primera documentación de interfaces del curso y base de los catálogos de P502. Límite: el manifiesto es un literal escrito en el código, no se deriva de los artefactos y sus consumidores no existen en la implementación.
- **H03 — Conserva la trazabilidad de línea en la interfaz de detalle (caso y datos):** como cada fila es un producto dentro de una orden, `sales_detail.csv` retiene `Order ID`, `Product Name`, `Customer ID`, `Region` y `Discount`, mientras `category_sales` sólo conserva `sales` y `profit` por categoría y `monthly_sales` cuenta órdenes con `nunique`. El manifiesto declara explícitamente estos granos. El detalle hace visible, además, el defecto de lectura heredado de P500: `Accentâ¢` en lugar de `Accent™`, porque el archivo con BOM UTF-8 se lee como `latin1`. Sin este hito, las tablas agregadas no podrían rastrearse hasta las líneas que las componen.

### Inventario técnico de implementación

- **Reutiliza:** `load_sales` de P500 y la agregación mensual (`build_monthly_sales` repite la lógica de `build_monthly_metrics` de P500).
- **Introduce:** agregación por `Product Category` ordenada por ventas; escritura en SQLite con `sqlite3.connect` y `DataFrame.to_sql`.
- **Introduce:** selección de columnas para una interfaz de detalle; manifiesto CSV de interfaces.
- **Reutiliza:** `questions.json` como enlace entre pregunta y artefacto.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Varias representaciones desde una fuente | H01 | CSV de detalle y dos tablas SQLite | Sin reconciliación entre ellas. |
| Manifiesto de interfaces | H02 | `serving_manifest.csv` con grano y consumidor | Literal en código; consumidores no implementados. |
| Detalle trazable al grano de línea | H03 | `sales_detail.csv` con llave de orden y producto | Textos no ASCII mal decodificados. |

### Relación técnica con actividades anteriores

Misma fuente y misma métrica mensual de P500 con nuevo producto: la exigencia pasa de definir una métrica a publicarla en interfaces con grano declarado. La función mensual está duplicada en código, no importada; la agregación por categoría es nueva. P501 abandona las aserciones y el contrato de P500, sin que la implementación indique por qué. No se observa duplicación de producto.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Representaciones de grano distinto | S02, S03 | `implementation/data/P501_superstore_serving/professor/main.py`: `main`, `build_monthly_sales`, `build_category_sales`; `implementation/data/P501_superstore_serving/submission/sales_serving.db` | El contenido de la base no es legible en el volcado; se describe desde el código. |
| H02 — Manifiesto de interfaces | S04 | `implementation/data/P501_superstore_serving/professor/main.py`: `build_manifest`; `implementation/data/P501_superstore_serving/submission/serving_manifest.csv` | Consumidores declarados, no implementados. |
| H03 — Trazabilidad de línea (caso y datos) | S01, S02, S03 | `implementation/data/P501_superstore_serving/submission/sales_detail.csv`; `implementation/data/P501_superstore_serving/professor/main.py`: `load_sales`, `detail_columns` | El defecto de codificación se observa en la cabecera del CSV publicado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/superstore_orders.csv` | Mismo archivo que P500; sin procedencia. |
| S02 | Representación / lectura y agregación | `professor/main.py`: `load_sales`, `build_monthly_sales`, `build_category_sales` | Código duplicado de P500; `latin1`; sin validación. |
| S03 | Producto | `submission/sales_detail.csv`; `submission/sales_serving.db`; `submission/questions.json` | Tres interfaces fijas. |
| S04 | Documentación de interfaces | `professor/main.py`: `build_manifest`; `submission/serving_manifest.csv` | Literal en código. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia de cuatro archivos. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin notebook ni instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe publicar el detalle al grano de línea, cargar dos agregados en SQLite y persistir el manifiesto.
- **`submission/`:** `sales_detail.csv`, `sales_serving.db` (tablas `monthly_sales`, `category_sales`), `serving_manifest.csv` y `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige la existencia de los cuatro archivos; no abre la base, no verifica tablas, granos, reconciliación ni codificación. Pasa con los artefactos del profesor ya presentes.
- **Trazabilidad:** `data.C02`, `data.C03`, `data.C04`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P500:** el CSV, la función de lectura y la lógica de agregación mensual; el patrón `questions.json`.
- **Habilita para P502:** los nombres `sales_detail`, `monthly_sales`, `category_sales` y `sales_serving.db` y sus granos reaparecen en el catálogo y el linaje de P502 (como literales; P502 no lee estos archivos).

## Trazabilidad y auditoría

Entrada revisada: P501 → `data.C02`, `data.C03`, `data.C04`, `data.C05`. C02 (agregación y publicación), C04 (manifiesto) y C05 (interfaces como medio para preguntas) tienen evidencia. `data.C03` no se evidencia: P501 no ejecuta ningún control de calidad ni procedencia y publica texto mal decodificado; vacío a escalar. El producto es una capacidad de datos para dos preguntas descriptivas, sin usuario real. Pregunta de auditoría 5: el vocabulario y la estructura (*serving*, base SQLite, consumidor «Dashboard») provienen de ingeniería de datos; tras la aclaración del profesor (2026-10-05), esas prácticas pertenecen al curso como puente y ya no constituyen por sí solas un riesgo de identidad, porque cada interfaz se justifica por una pregunta y un grano. Se conservan como límites: los consumidores son etiquetas sin uso implementado, no hay control de calidad (vacío C03), los agregados no se reconcilian con el detalle y se publica texto mal decodificado. Riesgo de identidad bajo (antes moderado).
