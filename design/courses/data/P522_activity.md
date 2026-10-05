# P522 — MapReduce con procesos paralelos sobre vuelos

## Actividad actual implementada

**Implementación:** `implementation/data/P522_mapreduce_multiprocessing/`.

### Preguntas analíticas actuales

- No hay pregunta analítica declarada. El código calcula vuelos no cancelados por aeropuerto de origen y mide el tiempo de ejecución con uno y con varios procesos; ninguna celda o comentario enuncia para qué se necesita ese conteo.

`data/flights.csv.gz` (2515210 bytes) es un archivo binario cuyo contenido no se expone en el resumen; el código sólo usa las columnas `Cancelled` y `Origin`. No hay procedencia, periodo ni manifiesto. `professor/main.py` (no hay notebook de profesor) abre con «Estas son las funciones que definimos en la actividad anterior», copia `map_pairs`, `group_by_key` y `reduce_by_key`, divide las filas en `max(4, cpu_count * 4)` archivos contiguos en `temp/input/`, ejecuta map y reducción local por archivo con `ProcessPoolExecutor`, combina los parciales y compara con una corrida de un proceso. Persiste `submission/origin_flights.csv` (82 orígenes; p. ej. `ABQ, 2027`) y `submission/benchmark.csv` (`1, 0.331056 s, 1.0`; `14, 0.121603 s, 2.722`). `src/main.py` levanta `NotImplementedError`; `notebooks/` sólo tiene `.gitkeep`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** conteo de vuelos operados por origen y una medición de aceleración.
- **Uso y límite:** muestra que una reducción asociativa puede repartirse entre procesos sin cambiar el resultado. La medición es una corrida única, depende del equipo (14 procesos en el archivo persistido) e incluye el arranque del pool; no permite generalizar sobre rendimiento. El conteo por origen no se interpreta y su periodo es desconocido.
- **Disciplinas contribuyentes:** computación paralela y modelo MapReduce; no subordinados a un producto analítico declarado.

### Highlights de contribución

- **H01 — Excluye vuelos cancelados dentro del mapper (caso y datos):** cada fila es un vuelo con bandera de cancelación; `map_flight` devuelve `[(Origin, 1)]` sólo si `record["Cancelled"] == "0"` y una lista vacía en otro caso, de modo que el mapper actúa también como filtro y la medida es vuelos operados, no programados. La comparación literal con `"0"` depende de cómo esté codificada la bandera en el CSV, lo que no se valida. Sin este hito, el conteo mezclaría vuelos que no ocurrieron.
- **H02 — Reduce localmente cada partición y combina los parciales:** `map_partition` aplica map, agrupación y `sum_flights` dentro de cada archivo y `run_mapreduce` vuelve a agrupar y sumar los pares parciales. Es válido porque la suma es asociativa y conmutativa; funcionalmente es una agregación local previa al shuffle, aunque el término «combiner» no aparece hasta P523. Es la primera vez en el curso que el código divide un archivo en particiones de entrada (P513 recibía lotes ya separados). Sin este hito, el paso de operadores locales a ejecución repartida no tendría evidencia.
- **H03 — Verifica que la paralelización no altera el resultado:** `assert single_result == parallel_result` compara listas ordenadas de la corrida de un proceso y de `cpu_count` procesos antes de persistir. Sin este hito, la aceleración no tendría una comprobación de corrección asociada.
- **H04 — Mide tiempo y aceleración de forma persistida:** `perf_counter` alrededor de `run_mapreduce` (excluye `prepare_partitions`) y `benchmark.csv` con `seconds` y `speedup`. Es la única medición de rendimiento entre P500 y P526. Sin este hito, el costo de coordinar procesos no sería observable.

### Inventario técnico de implementación

- **Introduce:** lectura de CSV comprimido con `gzip.open`; partición de entrada en archivos contiguos; `ProcessPoolExecutor.map`; reducción en dos niveles; medición con `perf_counter`; limpieza con `shutil.rmtree`.
- **Reutiliza:** `map_pairs`, `group_by_key`, `reduce_by_key` (copia de P519).
- **Aplica en nuevo caso:** conteo por clave a vuelos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Filtro en el mapper | H01 | Lista vacía para cancelados | Codificación de la bandera no validada. |
| Reducción en dos niveles | H02 | Parciales por partición + reducción final | Particiones por posición, no por clave. |
| Equivalencia secuencial–paralela | H03 | `assert` de igualdad | Una sola comparación. |
| Medición de aceleración | H04 | `benchmark.csv` | Una corrida; dependiente del equipo; incluye arranque. |

### Relación técnica con actividades anteriores

Mismos operadores que P519–P521 con nuevo dato (vuelos) y nueva exigencia (ejecución en procesos). Abandona el caso de conductores sin explicarlo. P524 usa otro `flights.csv.gz` (319006 bytes), de modo que no hay continuidad de archivo demostrable. `dig/case-selection.md` describe el bloque MapReduce sólo hasta P521 y excluye la operación de plataformas distribuidas como contenido; P522 queda fuera del diseño documentado y se acerca a esa frontera al convertir la aceleración en producto.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Filtro de cancelados | S01, S03 | `implementation/data/P522_mapreduce_multiprocessing/professor/main.py`: `map_flight`; `implementation/data/P522_mapreduce_multiprocessing/data/flights.csv.gz` | Contenido del archivo no inspeccionable aquí. |
| H02 — Reducción en dos niveles | S02, S03 | `implementation/data/P522_mapreduce_multiprocessing/professor/main.py`: `prepare_partitions`, `map_partition`, `run_mapreduce` | `temp/` debe existir: `mkdir()` sin `parents`. |
| H03 — Equivalencia | S04, S05 | `implementation/data/P522_mapreduce_multiprocessing/professor/main.py`: `main`; `implementation/data/P522_mapreduce_multiprocessing/submission/origin_flights.csv` | No probado en `tests/`. |
| H04 — Aceleración | S04, S05 | `implementation/data/P522_mapreduce_multiprocessing/submission/benchmark.csv` | Valores no reproducibles entre equipos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/flights.csv.gz` | Sin procedencia ni periodo. |
| S02 | Partición de entrada | `professor/main.py`: `prepare_partitions`; `temp/input/` | `max(4, cpu_count * 4)` archivos contiguos. |
| S03 | Mapper y reducer | `professor/main.py`: `map_flight`, `sum_flights`, `map_partition` | Comparación textual con `"0"`. |
| S04 | Ejecución y medición | `professor/main.py`: `run_mapreduce`, `main` | Corrida única. |
| S05 | Producto | `submission/origin_flights.csv`; `submission/benchmark.csv` | Sin `questions.json`. |
| S06 | Pruebas | `tests/test_activity.py` | Sólo existencia. |
| S07 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin notebook. |

### Contrato de evidencia actual

- **Notebook o código:** debe particionar, ejecutar con uno y varios procesos, comprobar igualdad y escribir resultado y medición.
- **`submission/`:** `origin_flights.csv` (82 orígenes) y `benchmark.csv` (dos filas).
- **Pruebas:** `test_01_submission_contains_mapreduce_results` sólo verifica que existan ambos archivos.
- **Trazabilidad:** `data.C02`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** P519: tres operadores centrales (copia).
- **Habilita para Pyyy:** no evidenciada; P523 redefine los mismos operadores y nombra explícitamente el combiner.

## Trazabilidad y auditoría

Entrada revisada: P522 → `data.C02`, `data.C05`. El filtro de cancelados es una decisión de calidad de la medida (`data.C03`) no mapeada. `data.C05` («herramientas como habilitadores») queda tensionado: aquí la herramienta y su rendimiento son el producto. Auditoría (pregunta 5): el taller se lee como introducción a computación paralela tipo Big Data, dentro de la frontera excluida («operaciones distribuidas»), sin pregunta ni uso analítico del conteo; auditoría no resuelta.
