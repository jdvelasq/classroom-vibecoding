# P514 — ETL Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P514_superstore_etl/`.

### Preguntas analíticas actuales

- ¿Qué segmentos y regiones concentran las ventas y la utilidad?

`professor/main.py` organiza en tres funciones (`extract`, `transform`, `publish`) la misma integración de P511 sobre las mismas cuatro tablas derivadas y el mismo manifiesto. `extract` copia cada CSV sin cambios a `temp/pipeline/raw/`; `transform` encadena los tres `merge(..., validate="many_to_one")` de P511 con la aserción de filas y la no nulidad de las columnas de la respuesta; `publish` escribe el mismo DataFrame en `temp/pipeline/staging/`, `temp/pipeline/curated/` y `submission/`, agrega por segmento y región y genera un reporte de etapas. `submission/superstore_enriched_sales.csv` tiene el mismo tamaño (493699 bytes) y cabecera, incluidas `Customer ID_x/_y`, que el de P511. `submission/sales_by_segment_region.csv` tiene 16 combinaciones; la primera es Corporate–West (ventas 203913.46; utilidad 26395.04). `pipeline_report.csv` registra raw 5926, staging 1952 y curated 1952, todos `SUCCESS`. El estudiante parte de `src/main.py` con `NotImplementedError`; `notebooks/` no contiene notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta persistida en `questions.json`; usuario y decisión no evidenciados.
- **Producto terminal:** detalle integrado, respuesta segmento × región, reporte de etapas y `questions.json`.
- **Uso y límite:** la respuesta es una agregación más gruesa de la de P511 (sin categoría). Staging y curated son copias idénticas: no hay transformación entre ellas, por lo que las etapas son nombres de directorio, no cambios observables. El estado `SUCCESS` es constante.
- **Disciplinas contribuyentes:** organización de un proceso ETL (ingeniería de datos) al servicio de la misma respuesta descriptiva de P511.

### Highlights de contribución

- **H01 — Separa la integración en funciones de extracción, transformación y publicación:** las validaciones de P511 pasan a `transform`, y la publicación escribe en directorios de etapa y en `submission/` desde un único `main()` ejecutable. Primera organización explícita del curso de una transformación en etapas nombradas. Sin este hito, el estudiante no vería la integración como un proceso repetible por etapas; su límite es que staging y curated no difieren.
- **H02 — Reporta filas por etapa en granos distintos (caso y datos):** el reporte suma en raw las filas de cuatro tablas de grano diferente (1857 órdenes + 1191 contextos de cliente + 926 contextos de producto + 1952 líneas = 5926), mientras staging y curated cuentan líneas (1952). La particularidad del caso (tablas derivadas con claves contextuales) hace que el conteo raw no sea comparable con el curado; el reporte no lo declara. Primera medición por etapa del curso (P513 cuenta por lote, no por etapa). Sin este hito, no habría evidencia persistente de que la integración conserva el grano línea; su límite es mezclar granos en una misma columna.

### Inventario técnico de implementación

- **Introduce:** funciones `extract`/`transform`/`publish`; directorios raw/staging/curated; reporte de filas por etapa.
- **Reutiliza sin cambios:** cadena de uniones validadas y aserciones de P511; datos y manifiesto de P511.
- **Reutiliza:** `questions.json` (P500–P508) y patrón `professor/main.py` + `src/main.py` vacío.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Proceso ETL en funciones | H01 | `extract`, `transform`, `publish` en `professor/main.py` | Staging = curated. |
| Reporte por etapa | H02 | `submission/pipeline_report.csv` | Raw suma granos distintos; estado constante. |

### Relación técnica con actividades anteriores

Misma técnica de integración y mismos datos que P511, con nueva forma de organización (script por etapas) y una pregunta más gruesa. El detalle publicado duplica el de P511. Es una posible duplicación que requiere decisión posterior: la contribución distinguible se reduce a la organización en etapas y al reporte. P515 repite la pregunta con la transformación dentro de SQLite.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Etapas ETL | S02, S03 | `implementation/data/P514_superstore_etl/professor/main.py`; `implementation/data/P514_superstore_etl/submission/superstore_enriched_sales.csv`; `implementation/data/P511_superstore_integracion/professor/notebook.ipynb` | Directorios de etapa en `temp/`, no entregados. |
| H02 — Filas por etapa | S01, S03, S04 | `implementation/data/P514_superstore_etl/submission/pipeline_report.csv`; `implementation/data/P514_superstore_etl/data/source_manifest.json`; `implementation/data/P514_superstore_etl/professor/main.py` (`publish`) | La no comparabilidad de granos no está declarada en la actividad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: tablas derivadas de Superstore | `data/*.csv`; `data/source_manifest.json` | Idénticas a P511, P512 y P515. |
| S02 | Método: etapas ETL | `professor/main.py` | Transformación igual a P511; staging = curated. |
| S03 | Producto: detalle, respuesta y reporte | `submission/superstore_enriched_sales.csv`; `submission/sales_by_segment_region.csv`; `submission/pipeline_report.csv`; `submission/questions.json` | Detalle igual al de P511; respuesta igual a la de P515. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia de cuatro archivos. |
| S05 | Interfaz del estudiante | `src/main.py` | Stub sin enunciado; sin notebook. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` copia raw, integra con validaciones, publica en etapas y en `submission/`, agrega y reporta.
- **`submission/`:** `superstore_enriched_sales.csv` (1952 líneas), `sales_by_segment_region.csv` (16 filas), `pipeline_report.csv` (3 etapas), `questions.json`.
- **Pruebas:** `test_01` verifica que existen los cuatro archivos; no verifica conteos, grano ni sumas.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de P511:** datos, manifiesto y la cadena de uniones validadas, reproducida literalmente.
- **Habilita para P515:** misma pregunta y misma forma de reporte (`stage`, `rows`, `status`) con la transformación trasladada a SQLite.

## Trazabilidad y auditoría

P514 está mapeada a `data.C01`–`data.C05`. C02 se evidencia (integración y publicación); C01 en la pregunta; C03 en las aserciones heredadas de P511; C04 en el reporte de etapas, con la limitación de granos mezclados; C05 en el vocabulario de etapas. Auditoría 5: el contenido nuevo es la organización ETL; el producto analítico no cambia respecto de P511 y la respuesta es más gruesa. La actividad puede describirse como ejercicio de ETL sobre un producto ya obtenido; la auditoría queda no resuelta hasta que la etapa añada una evidencia o decisión analítica distinta.
