# P513 — Ingestión batch Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P513_superstore_batch/`.

### Preguntas analíticas actuales

- No hay una pregunta analítica persistida: ni `professor/main.py` ni `submission/` la declaran; la evidencia se centra en ingerir dos lotes trimestrales.

Los datos son dos lotes derivados del extracto `datalabs/commerce/superstore-orders.csv`, separados por trimestre de `Order Date` sin inventar ni modificar valores (`data/source_manifest.json`): `superstore_orders_2015_q1.csv` (1012 filas) y `superstore_orders_2015_q2.csv` (940). La suma, 1952, coincide con las líneas del CSV de P500, aunque el código no lo verifica. Los lotes conservan las 25 columnas originales, el separador `;`, la marca BOM inicial y las fechas `d/m/yy`, pero usan punto decimal (`0.01`, `500.98`), a diferencia de P500 (coma decimal). `professor/main.py` descubre los lotes con `glob("superstore_orders_*.csv")` ordenado, los lee con `sep=";"`, `encoding="utf-8-sig"` y `decimal=","`, escribe cada uno como Parquet en `temp/raw/` y persiste `submission/ingestion_report.csv` con nombre, filas, estado y ruta. El bloque `format` del manifiesto no es visible completo en la evidencia inspeccionada. El estudiante trabaja sobre `src/main.py`, que sólo lanza `NotImplementedError`; `notebooks/` no contiene notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** zona raw en `temp/raw/*.parquet` (no persistida en `submission/`) y `submission/ingestion_report.csv` (2 filas, ambas `SUCCESS`).
- **Uso y límite:** el reporte permite saber qué lotes se leyeron y cuántas filas tenía cada uno. No permite afirmar que la ingestión conservó los tipos: con `decimal=","` sobre valores con punto decimal, pandas lee `Discount`, `Unit Price`, `Shipping Cost`, `Profit`, `Sales` y similares como texto (comportamiento comprobado de `read_csv`), y así quedarían en Parquet. `status` es una constante `"SUCCESS"`: no hay rama de error, validación de esquema ni conciliación entre lotes y total.
- **Disciplinas contribuyentes:** prácticas de ingeniería de datos (lotes, zona raw, Parquet) sin un producto analítico declarado al que sirvan.

### Highlights de contribución

- **H01 — Lee lotes con BOM y declara el formato en la lectura (caso y datos):** los lotes traen BOM UTF-8 y `;`; `encoding="utf-8-sig"` elimina la marca sin el arreglo manual de P500 (que lee en `latin1` y quita `"ï»¿"` del nombre de columna, lo que además produce texto mal decodificado como `Accentâ¢` en `submission/sales_detail.csv` de P501). La misma declaración de formato incluye `decimal=","`, que contradice el punto decimal de los lotes. Primera lectura del CSV fuente de Superstore con decodificación UTF-8 correcta en el curso. Sin este hito no se vería que el contrato de formato debe ajustarse a cada entrega; el defecto decimal muestra el costo de no verificar tipos después de leer.
- **H02 — Descubre lotes por patrón y los aterriza sin transformar en Parquet:** `sorted(DATA_DIR.glob(...))`, `assert batches` y `to_parquet` por lote en una zona `temp/raw/`. Primera aparición de Parquet y de entregas múltiples en el curso; P518 y P524 vuelven a usar Parquet sin referencia a P513. Sin este hito, el curso no ejercitaría la recepción de una fuente que llega fragmentada por periodo.
- **H03 — Registra la ingestión por lote:** `ingestion_report.csv` con `source_name`, `row_count`, `status` y `raw_path`. Extiende el linaje declarativo de P502 (fuente→destino escrito a mano) a un registro producido por la ejecución. Sin este hito, no quedaría evidencia persistente de qué lotes entraron; su límite es el estado constante.

### Inventario técnico de implementación

- **Introduce:** descubrimiento de archivos con `glob`; lectura con `utf-8-sig`; escritura Parquet; reporte de ingestión por lote.
- **Reutiliza:** patrón de script `professor/main.py` con `src/main.py` vacío para el estudiante (P500–P502); caso Superstore.
- **No ejercita:** validación de tipos o esquema tras la lectura, conciliación de filas con la fuente, manejo de fallos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Contrato de formato en la lectura | H01 | `sep`, `encoding="utf-8-sig"`, `decimal` en `read_csv` | `decimal=","` no coincide con los lotes. |
| Zona raw en Parquet | H02 | `temp/raw/*.parquet` | No persistida; tipos no verificados. |
| Reporte de ingestión | H03 | `submission/ingestion_report.csv` | `status` constante; sin conciliación. |

### Relación técnica con actividades anteriores

Mismo caso y mismas filas que P500, con nueva forma de entrega (dos lotes) y sin pregunta. La lectura cambia de `latin1` + coma decimal a `utf-8-sig` + coma decimal sobre archivos con punto decimal. No se relaciona con P511–P512 (tablas derivadas) ni usa su manifiesto de claves. Es la actividad del bloque Superstore con menor vínculo a un producto analítico.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Formato en la lectura | S01, S02 | `implementation/data/P513_superstore_batch/data/superstore_orders_2015_q1.csv`; `implementation/data/P513_superstore_batch/professor/main.py`; `implementation/data/P500_superstore_metricas/professor/main.py`; `implementation/data/P501_superstore_serving/submission/sales_detail.csv` | Los Parquet no están persistidos; el efecto sobre tipos se infiere del comportamiento de `read_csv`, no de un archivo. |
| H02 — Lotes a Parquet | S02, S03 | `implementation/data/P513_superstore_batch/professor/main.py`; `implementation/data/P513_superstore_batch/data/source_manifest.json` | Sólo dos lotes; ningún caso de lote faltante o malformado. |
| H03 — Reporte por lote | S03, S04 | `implementation/data/P513_superstore_batch/submission/ingestion_report.csv`; `implementation/data/P513_superstore_batch/tests/test_activity.py` | `SUCCESS` no se deriva de ninguna verificación. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: lotes trimestrales | `data/superstore_orders_2015_q*.csv`; `data/source_manifest.json` | Punto decimal, BOM y `;`. |
| S02 | Representación: lectura y aterrizaje raw | `professor/main.py` | `decimal=","` incompatible con los datos. |
| S03 | Producto: reporte de ingestión | `submission/ingestion_report.csv` | Ruta raw en `temp/`, fuera de la entrega. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia del reporte. |
| S05 | Interfaz del estudiante y pregunta | `src/main.py`; `notebooks/` | Stub sin enunciado; ninguna pregunta analítica. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` lee cada lote, escribe Parquet y genera el reporte.
- **`submission/`:** `ingestion_report.csv` (q1: 1012; q2: 940; ambos `SUCCESS`). No hay `questions.json` ni datos ingeridos.
- **Pruebas:** `test_01` verifica que existe el reporte; no verifica filas, tipos ni Parquet.
- **Trazabilidad:** `data.C02`–`data.C05` (sin C01).

### Dependencias en la secuencia

- **Recibe de P500:** caso y filas de Superstore (los lotes particionan esas 1952 líneas); no consume artefactos.
- **Habilita para Pyyy:** no evidenciada. El formato de reporte (fuente, filas, estado, ruta) reaparece en P518, sin referencia explícita.

## Trazabilidad y auditoría

P513 está mapeada a `data.C02`–`data.C05`; la ausencia de C01 es coherente con la falta de pregunta. C02 se evidencia (lectura y aterrizaje); C03 queda débil y contradicha por el defecto de tipos no detectado; C04 en manifiesto y reporte; C05 en el uso de Parquet como medio. Auditoría 5: es la actividad del rango P510–P517 que más claramente puede describirse como práctica de ingeniería de datos (ingestión batch a zona raw) sin producto analítico; la auditoría queda no resuelta hasta que se declare qué análisis habilita la ingestión. Se conserva la escalación de S01.
