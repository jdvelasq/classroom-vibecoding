# P524 — Selección de formato: CSV, JSON y Parquet sobre vuelos

## Actividad actual implementada

**Implementación:** `implementation/data/P524_seleccion_formato_datos/`.

### Preguntas analíticas actuales

- No hay pregunta analítica. El notebook declara un problema de representación: «Elegir una representación de datos adecuada comparando CSV, JSON y Parquet sobre el mismo subconjunto real de vuelos».

El notebook lee `data/flights.csv.gz` (319006 bytes) y escribe, en la misma carpeta `data/`, `flights.csv` (12000 filas, 29 columnas: fecha, horarios programados y reales, aerolínea, origen, destino, retrasos y cancelación; las filas visibles son de 2008), `flights.json` (orientación `records`) y `flights.parquet` (pyarrow). Comprueba que CSV y Parquet conservan el número de filas y persiste `submission/format_comparison.csv`: tamaños de 1302154 (CSV), 5924115 (JSON) y 246908 bytes (Parquet), tres propiedades booleanas y un uso principal por formato. La procedencia de los vuelos no se documenta. `data/` incluye además `sales.csv` (2000 filas), `sales.json` y `sales.parquet`, que el notebook no usa. El notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; la decisión es técnica (qué formato usar), sin uso analítico declarado.
- **Producto terminal:** tabla de comparación de formatos con un tamaño medido y propiedades declaradas.
- **Uso y límite:** documenta una elección de formato para lectura analítica. Sólo el tamaño se mide; `schema_preserved`, `human_readable` y `column_selection` se escriben como constantes. No se miden tiempos de lectura ni lectura selectiva de columnas. CSV y JSON se escriben sin compresión y Parquet con la configuración por omisión, y el `flights.csv.gz` de entrada (319006 bytes) no entra en la tabla, de modo que la diferencia de tamaño mezcla formato y compresión.
- **Disciplinas contribuyentes:** formatos de almacenamiento y pandas/pyarrow.

### Highlights de contribución

- **H01 — Fija las mismas filas antes de comparar formatos:** un único `frame` se escribe en los tres formatos y `assert len(frame) == len(pd.read_csv(csv_path)) == len(pd.read_parquet(parquet_path))` comprueba la conservación de filas («La comparación es válida porque los tres formatos parten de las mismas filas»). JSON queda fuera de la comprobación. Primera comparación controlada de representaciones en el curso. Sin este hito, las diferencias de tamaño podrían deberse a contenidos distintos.
- **H02 — Hace visible el costo de representar un registro ancho con nulos y horas codificadas (caso y datos):** cada fila es un vuelo con 29 columnas; las causas de retraso (`CarrierDelay`…`LateAircraftDelay`) aparecen vacías en las filas visibles y los horarios reales se codifican como números `hhmm` con decimal (`DepTime` 2003.0), lo que indica un entero convertido en flotante por faltantes. JSON `records` repite las 29 llaves y escribe `null` en cada fila (5924115 bytes frente a 1302154 del CSV); el CSV no conserva tipos y Parquet sí. Sin este hito, la elección de formato no se vincularía con la estructura concreta de los datos.
- **H03 — Persiste la decisión de formato como tabla revisable:** `format_comparison.csv` combina tamaño medido con propiedades y uso principal («Lectura analítica columnar» para Parquet). Las propiedades no se verifican en el código. Sin este hito, la elección quedaría sólo en la salida del notebook.

### Inventario técnico de implementación

- **Introduce:** escritura de un mismo `DataFrame` en CSV, JSON (`orient="records"`) y Parquet (`engine="pyarrow"`); comparación de tamaños con `stat().st_size`; tabla de decisión.
- **Reutiliza:** lectura de CSV comprimido; Parquet (P513, P518).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Comparación controlada | H01 | Mismo `frame`, tres escrituras, `assert` de filas | JSON no verificado. |
| Costo de representación | H02 | Tamaños por formato sobre 12000 vuelos de 29 columnas | Mezcla formato y compresión; tipos no persistidos. |
| Tabla de decisión | H03 | `format_comparison.csv` | Tres de cinco columnas son declaraciones. |

### Relación técnica con actividades anteriores

Nuevo método (comparación de formatos) sobre el dominio de vuelos que P522 usó con otro archivo (`flights.csv.gz` de 2515210 bytes); no hay continuidad de archivo. P513 y P518 ya persistían Parquet sin justificarlo; P524 hace explícita la razón. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Mismas filas | S02 | `implementation/data/P524_seleccion_formato_datos/professor/notebook.ipynb`: celdas de escritura y `assert` | El notebook sobrescribe archivos de `data/`. |
| H02 — Costo de representación | S01, S02, S03 | `implementation/data/P524_seleccion_formato_datos/data/flights.csv`; `implementation/data/P524_seleccion_formato_datos/data/flights.json`; `implementation/data/P524_seleccion_formato_datos/submission/format_comparison.csv` | Pérdida de tipos sólo visible en `frame.dtypes.head()`, no persistida. |
| H03 — Tabla de decisión | S03 | `implementation/data/P524_seleccion_formato_datos/submission/format_comparison.csv` | Propiedades constantes. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datasets | `data/flights.csv.gz`; `data/flights.*`; `data/sales.*` | Sin procedencia; `sales.*` sin uso. |
| S02 | Escritura y verificación | `professor/notebook.ipynb` | Salidas en `data/`; JSON sin verificar. |
| S03 | Producto | `submission/format_comparison.csv` | Sólo tamaño medido. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Vacío. |

### Contrato de evidencia actual

- **Notebook o código:** debe escribir los tres formatos desde el mismo `frame`, verificar filas y persistir la comparación.
- **`submission/`:** `format_comparison.csv` (tres formatos).
- **Pruebas:** `test_01_submission_contains_format_comparison` sólo verifica que exista el archivo.
- **Trazabilidad:** `data.C02`, `data.C03`, `data.C04`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna demostrable (Parquet ya usado en P513 y P518 como práctica).
- **Habilita para Pyyy:** P525 parte de un Parquet y lo particiona; la relación es de práctica, sin archivo compartido.

## Trazabilidad y auditoría

Entrada revisada: P524 → `data.C02`–`data.C05`. `data.C04` se apoya en la tabla de decisión; `data.C03` sólo en la verificación de filas, sin evaluación de calidad, a revisar. Auditoría (pregunta 5): taller de formatos de almacenamiento sin pregunta analítica; la vinculación con la estructura de los vuelos (registro ancho, nulos, tipos) es lo que lo aleja de una lección genérica de herramientas. Riesgo de identidad moderado.
