# P525 — Particionamiento temporal de una serie diaria en Parquet

## Actividad actual implementada

**Implementación:** `implementation/data/P525_particionamiento_parquet/`.

### Preguntas analíticas actuales

- No hay pregunta analítica. El notebook declara: «Preparar una serie temporal real en particiones Parquet para recuperar períodos analíticos sin leer todo el conjunto».

`data/cta_daily_station_totals.parquet` (259099 bytes) tiene 100800 filas según `lake_summary.csv`; el código sólo nombra la columna `date`. El nombre del archivo sugiere totales diarios por estación, pero la unidad de análisis, las demás columnas y la procedencia no se documentan. El notebook deriva `year` y `month`, borra los Parquet previos, escribe un archivo por año-mes en `temp/lake/curated/cta_rides/year=YYYY/month=MM/rides.parquet` sin las columnas derivadas, verifica que la suma de filas coincida y persiste `submission/lake_summary.csv` (`cta_rides, "year,month", 23, 23, 100800`). El notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** un conjunto Parquet particionado por año y mes (en `temp/`, no persistido) y un resumen de una fila.
- **Uso y límite:** deja la serie organizada para leer un periodo por directorio. La recuperación de un periodo sin leer todo, que es el objetivo declarado, no se ejercita: no hay lectura filtrada, poda de particiones ni medición. Las 23 particiones son meses distintos presentes; no se verifica que sean consecutivos.
- **Disciplinas contribuyentes:** almacenamiento particionado (diseño de data lake) y pandas/pyarrow; según la aclaración del profesor (2026-10-05), formatos y particionamiento pertenecen al curso como puente hacia la analítica.

### Highlights de contribución

- **H01 — Deriva la llave de partición de la dimensión temporal de la serie (caso y datos):** `frame["date"]` se convierte con `pd.to_datetime` y de ella salen `year` y `month`; la partición coincide con la unidad en que se recuperarían periodos. `date` se conserva dentro de cada archivo, de modo que quitar `year` y `month` no pierde información. Sin este hito, la partición sería una división arbitraria y no una consecuencia de la temporalidad del dato.
- **H02 — Escribe un diseño de directorios `clave=valor` reproducible:** `groupby(["year", "month"])`, rutas `year={year}/month={month:02d}`, `mkdir(parents=True, exist_ok=True)` y borrado previo de `*.parquet` para que una nueva ejecución no deje archivos viejos (los directorios vacíos no se borran). Extiende Parquet de P524 (un archivo) a un conjunto particionado. Sin este hito, el curso no tendría una estructura física pensada para la lectura por periodo.
- **H03 — Verifica conservación de filas y resume la partición:** `assert sum(len(pd.read_parquet(file)) for file in files) == len(frame)` y `lake_summary.csv` con columnas de partición, número de particiones, archivos y filas. Sin este hito, la reorganización no dejaría evidencia persistente de que no perdió registros.

### Inventario técnico de implementación

- **Introduce:** particionamiento estilo `clave=valor` por año y mes; derivación de llaves con `.dt.year`/`.dt.month`; limpieza idempotente de archivos; resumen de conjunto particionado.
- **Extiende:** Parquet de P524 a varios archivos.
- **Reutiliza:** `assert` de conservación de filas (P524).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Partición temporal | H01 | `year`, `month` desde `date` | Unidad de análisis no documentada. |
| Diseño `clave=valor` | H02 | `temp/lake/curated/cta_rides/year=…/month=…` | En `temp/`; sin lectura con poda. |
| Conservación y resumen | H03 | `assert`; `lake_summary.csv` | Sólo conteos. |

### Relación técnica con actividades anteriores

Nuevo dato (serie diaria) y nueva exigencia sobre Parquet: de elegir formato (P524) a organizar físicamente por periodo. Junto con `temp/raw/` de P513, la ruta `lake/curated` introduce vocabulario de zonas de data lake sin que la relación esté declarada. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Partición temporal | S01, S02 | `implementation/data/P525_particionamiento_parquet/data/cta_daily_station_totals.parquet`; `implementation/data/P525_particionamiento_parquet/professor/notebook.ipynb`: segunda celda | Columnas distintas de `date` no visibles. |
| H02 — Diseño de directorios | S02 | `implementation/data/P525_particionamiento_parquet/professor/notebook.ipynb`: tercera celda | Resultado en `temp/`, no persistido ni probado. |
| H03 — Conservación y resumen | S02, S03 | `implementation/data/P525_particionamiento_parquet/professor/notebook.ipynb`: `assert`; `implementation/data/P525_particionamiento_parquet/submission/lake_summary.csv` | Sin verificación de periodos consecutivos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/cta_daily_station_totals.parquet` | Sin procedencia ni unidad documentada. |
| S02 | Particionamiento y verificación | `professor/notebook.ipynb`; `temp/lake/curated/cta_rides/` | Año-mes fijo; sin lectura por periodo. |
| S03 | Producto | `submission/lake_summary.csv` | Una fila; sin `questions.json`. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Vacío. |

### Contrato de evidencia actual

- **Notebook o código:** debe particionar por año-mes, limpiar ejecuciones previas, verificar filas y resumir.
- **`submission/`:** `lake_summary.csv` (23 particiones, 23 archivos, 100800 filas).
- **Pruebas:** `test_01_submission_contains_partition_summary` sólo verifica que exista el archivo.
- **Trazabilidad:** `data.C02`, `data.C03`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** P524: Parquet como formato de lectura analítica (práctica; sin archivo).
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P525 → `data.C02`, `data.C03`, `data.C05`. `data.C03` se apoya sólo en la conservación de filas. Auditoría (pregunta 5): la ruta `lake/curated` lo acerca a diseño de almacenamiento de data lake; tras la aclaración del profesor (2026-10-05), formatos y particionamiento pertenecen al curso como puente y el taller declara una finalidad analítica simple (recuperar periodos), de modo que ese carácter ya no deja por sí solo la auditoría sin resolver. Se conserva como límite de evidencia que el propósito está declarado pero no se demuestra (no hay lectura filtrada, poda de particiones ni medición) y que el conjunto particionado no se persiste. Riesgo de identidad bajo a moderado (antes moderado a alto).
