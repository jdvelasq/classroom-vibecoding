# P502 — Catálogo y linaje de datos Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P502_superstore_linaje/`.

### Preguntas analíticas actuales

- ¿Cuál es el linaje desde Superstore hasta las interfaces que responden ventas mensuales y ventas por categoría?

`professor/main.py` construye tres tablas como literales de pandas y las persiste: `data_catalog.csv` (cuatro datasets con descripción, grano, ubicación y consumidor), `column_catalog.csv` (seis columnas con descripción y rol) y `lineage.csv` (tres relaciones fuente → destino con su transformación). Los datasets catalogados son la fuente `superstore_orders` y las tres interfaces de P501. `data/superstore_orders.csv` está presente, pero el código no lo lee ni abre los artefactos de P501: catálogo y linaje se escriben a mano. No hay notebook; `src/main.py` sólo lanza `NotImplementedError`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** documentar de dónde provienen las interfaces que responden dos preguntas de ventas; usuario y decisión no evidenciados.
- **Producto terminal:** documentación de datos: catálogo de datasets, catálogo parcial de columnas y linaje declarativo.
- **Uso y límite:** permite a un lector saber qué grano tiene cada interfaz y de qué fuente sale. No verifica que el linaje corresponda al código que produjo las interfaces, no cubre todas las columnas publicadas y no registra procedencia externa de la fuente.
- **Disciplinas contribuyentes:** prácticas de gobierno y documentación de datos (catálogo, linaje) al servicio de la auditabilidad de métricas.

### Highlights de contribución

- **H01 — Inventaría los datasets con grano, ubicación y consumidor:** `build_data_catalog` registra la fuente (`location` = `data`, `consumer` = «Privado») y las tres interfaces de P501 (`submission`, `sales_serving.db`; «Analista», «Dashboard»). Extiende el manifiesto de P501 al incluir la fuente. Sin este hito, la fuente quedaría fuera de la documentación de las interfaces. Límite: la ubicación `submission` de `sales_detail` remite al `submission/` de P501, no al de P502, y el valor «Privado» no se explica.
- **H02 — Asigna roles analíticos a las columnas:** `build_column_catalog` clasifica `Order ID` como clave de negocio, `Order Date` como dimensión temporal, `Sales` y `Profit` como métricas fuente, `average_order_value` como métrica derivada y `Product Category` como dimensión de análisis. Primera tipificación de roles en el curso. Límite: seis columnas; faltan, entre otras, `Product Name` (parte de la llave de P500), `Customer ID`, `Region`, `Discount` de `sales_detail` y `profit`/`order_count` de los agregados.
- **H03 — Registra el cambio de grano en cada paso de linaje (caso y datos):** la fuente es «una fila por producto dentro de una orden» y `lineage.csv` describe dos transformaciones que cambian el grano (agregación mensual, agregación por categoría) y una que lo conserva (selección de campos); `data_catalog.csv` declara el grano de origen y de destino. Con líneas de orden, cada métrica publicada depende de esa agregación, y el linaje la hace auditable. Sin este hito, el paso de línea a mes o a categoría quedaría implícito en el código de P501. Límite: el linaje no nombra las fórmulas (`nunique` de órdenes) ni se deriva del código.

### Inventario técnico de implementación

- **Introduce:** catálogo de datasets, catálogo de columnas con roles y tabla de linaje fuente-destino-transformación, persistidos como CSV.
- **Reutiliza:** nombres y granos de las interfaces de P501; `questions.json`.
- **No ejercita:** lectura de datos, extracción automática de metadatos ni verificación del linaje.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Catálogo de datasets | H01 | Grano, ubicación y consumidor por dataset | Literal; «Privado» sin explicación. |
| Roles de columnas | H02 | Clave, dimensión, métrica fuente y derivada | Seis columnas de un conjunto mayor. |
| Linaje con cambio de grano | H03 | Tres aristas fuente → destino | Declarativo; no verificado contra P501. |

### Relación técnica con actividades anteriores

Misma fuente y mismas interfaces de P501 con nueva exigencia de evidencia: documentar origen y transformación. El manifiesto de P501 ya declaraba grano y consumidor de las tres interfaces; P502 añade la fuente, roles de columnas y aristas de linaje. El solapamiento con el manifiesto es parcial y no constituye duplicación del producto, aunque ambos son literales de código que pueden divergir sin que nada lo detecte.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Catálogo de datasets | S02, S04 | `implementation/data/P502_superstore_linaje/professor/main.py`: `build_data_catalog`; `implementation/data/P502_superstore_linaje/submission/data_catalog.csv` | Literal; no comprueba existencia de los datasets. |
| H02 — Roles de columnas | S02, S04 | `implementation/data/P502_superstore_linaje/professor/main.py`: `build_column_catalog`; `implementation/data/P502_superstore_linaje/submission/column_catalog.csv` | Cobertura parcial de columnas. |
| H03 — Cambio de grano en el linaje (caso y datos) | S01, S03, S04 | `implementation/data/P502_superstore_linaje/professor/main.py`: `build_lineage`; `implementation/data/P502_superstore_linaje/submission/lineage.csv`; `implementation/data/P502_superstore_linaje/submission/data_catalog.csv` | No vinculado con el código de P501. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/superstore_orders.csv` | Presente pero no leído. |
| S02 | Catálogos | `professor/main.py`: `build_data_catalog`, `build_column_catalog` | Literales escritos a mano. |
| S03 | Linaje | `professor/main.py`: `build_lineage` | Tres aristas; sin fórmula ni verificación. |
| S04 | Producto | `submission/data_catalog.csv`; `submission/column_catalog.csv`; `submission/lineage.csv`; `submission/questions.json` | Archivo de respuesta: `lineage.csv`. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia de cuatro archivos. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin notebook ni instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe escribir los tres catálogos y la pregunta; no procesa datos.
- **`submission/`:** `data_catalog.csv` (4 datasets), `column_catalog.csv` (6 columnas), `lineage.csv` (3 aristas), `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige existencia; no verifica coherencia entre catálogo, linaje y artefactos de P501. Pasa con los archivos del profesor presentes.
- **Trazabilidad:** `data.C03`, `data.C04`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P501:** nombres, ubicaciones y granos de `sales_detail`, `monthly_sales` y `category_sales` (como texto, sin lectura de archivos); de P500, la métrica `average_order_value`.
- **Habilita para Pyyy:** no evidenciada en P503–P508.

## Trazabilidad y auditoría

Entrada revisada: P502 → `data.C03`, `data.C04`, `data.C05`. `data.C04` tiene evidencia directa (catálogo y linaje). `data.C03` sólo se apoya parcialmente: el linaje documenta procedencia interna, pero no se evalúa calidad, faltantes ni procedencia externa; vacío a escalar. `data.C05` es débil: no hay declaración explícita sobre herramientas. El producto es documentación que hace auditables las métricas de P500–P501; no hay usuario ni decisión. Pregunta 5: el riesgo no es de ingeniería sino de documentación formal desconectada de los datos, porque el linaje no se deriva ni se contrasta con el código. Riesgo de identidad bajo a moderado.
