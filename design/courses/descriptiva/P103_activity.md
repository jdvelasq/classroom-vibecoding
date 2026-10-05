# P103 — Resumen de conductores con pandas

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P103_drivers_pandas/`.

### Preguntas analíticas actuales

Las preguntas no se declaran como tales; se infieren de los comentarios de las celdas del notebook del profesor:

- ¿Cuál es la media de horas y millas registradas por cada conductor?
- ¿En qué semanas un conductor registró menos horas que su propia media?
- ¿Cuántas horas y millas acumuló cada conductor (el comentario dice «por año») y cuál fue su mínimo y máximo de horas?
- ¿Qué diez conductores registraron más millas?

Combina `data/drivers.csv` (34 conductores) con `data/timesheet.csv` (1.768 registros conductor-semana con `hours-logged` y `miles-logged`). El producto es una tabla resumen por conductor y un gráfico de barras de los diez conductores con más millas. No se declaran usuario, decisión ni procedencia.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** preguntas descriptivas implícitas en comentarios; usuario y decisión no evidenciados.
- **Producto terminal:** explicación descriptiva mínima: `submission/summary.csv` (totales de horas y millas por conductor con su nombre) y `submission/top10_drivers.png` (ranking por millas).
- **Uso y límite:** permite comparar volumen acumulado entre conductores. No permite juzgar desempeño: no hay normalización por semanas trabajadas ni por plan de pago (`wage-plan`), ni interpretación escrita. La tabla de semanas bajo la media se calcula pero no se persiste.
- **Disciplinas contribuyentes:** manipulación de datos con pandas y visualización con matplotlib, al servicio de un resumen descriptivo.

### Highlights de contribución

- **H01 — Reconcilia dos granularidades antes de unir (caso y datos):** `timesheet` tiene una fila por conductor y semana; `drivers`, una por conductor. El notebook agrega primero por `driverId` (`groupby(...).sum()`) y sólo después une con `drivers[["driverId", "name"]]`, de modo que la unidad de `summary` es el conductor. Al calcular la media de todas las columnas aparece también la media de `week`, que se elimina con `pop("week")`: un índice temporal no es una medida. Es la primera unión de tablas del curso. Sin este hito se perdería la distinción entre registro operativo y entidad descrita.
- **H02 — Compara cada registro con la media de su propio grupo:** `groupby("driverId")["hours-logged"].transform("mean")` añade la media del conductor a cada semana sin reducir filas, y el filtro conserva las semanas por debajo de ella. Contrasta `groupby().mean()` (una fila por conductor) con `transform` (todas las filas). Sin este hito, la comparación con la flota entera sustituiría a la comparación intra-conductor. Límite: no se persiste ni se prueba.
- **H03 — Persiste un resumen cuyo cálculo se verifica desde los datos:** `summary.csv` se guarda sin índice y `test_02` lo recalcula desde `data/` con `groupby`, `sum` y `merge`, comparando con `assert_frame_equal`. Es la primera prueba del curso que reconstruye un resultado analítico desde las fuentes, no sólo conteos fijos. Sin este hito el resumen sólo se comprobaría por existencia.
- **H04 — Comunica un ranking con una gráfica legible:** ordena por `miles-logged`, toma diez, usa barras horizontales con el mayor arriba (`invert_yaxis`), separador de miles en el eje, ejes superior y derecho ocultos y guarda `top10_drivers.png`. Es la primera visualización persistida del curso. Límite: la prueba sólo exige una imagen de más de 100 × 100 píxeles y el gráfico no tiene título ni etiqueta de eje.

### Inventario técnico de implementación

- **Introduce:** `pd.read_csv` con `sep`, `thousands` y `decimal` explícitos; `groupby` con `mean`, `sum`, `transform` y `agg([min, max])` (con funciones integradas de Python); filtrado booleano; `pd.merge` por clave; `sort_values` y `head`; `to_csv(index=False)`; `plot.barh` y formateo de ejes con `matplotlib.ticker.FuncFormatter`.
- **Reutiliza de P102:** `drivers.csv`; sólo `driverId` y `name` pasan al resumen, sin declarar la razón.
- **Interfaz de estudiante:** `notebooks/notebook.ipynb` vacío (0 celdas).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Agregación y unión entre granularidades | H01, H03 | `groupby` por conductor y `merge` con `drivers` | `submission/summary.csv` y `test_02`; no normaliza por semanas. |
| Comparación intra-grupo | H02 | `transform("mean")` y filtro | Notebook; sin artefacto. |
| Ranking visual | H04 | Barras horizontales ordenadas, formato de miles | `submission/top10_drivers.png`; sin título ni interpretación. |

### Relación técnica con actividades anteriores

Primer taller de exploración tabular con pandas. Reutiliza `drivers.csv` de P102 y añade `timesheet.csv`; cambia de capacidad de datos (exportación) a resumen descriptivo con visualización. No duplica P100–P102. Es el caso base que P104 y P105 reexpresan con otras herramientas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Granularidades y unión | S01, S02 | `implementation/descriptiva/P103_drivers_pandas/data/timesheet.csv`; `implementation/descriptiva/P103_drivers_pandas/data/drivers.csv`; `implementation/descriptiva/P103_drivers_pandas/professor/notebook.ipynb`: celdas de media, `pop("week")`, suma y `pd.merge` | No se verifica que todos los conductores tengan el mismo número de semanas. |
| H02 — Comparación con la media propia | S02 | `implementation/descriptiva/P103_drivers_pandas/professor/notebook.ipynb`: `transform("mean")`, `timesheet_below` | Sin persistencia ni prueba. |
| H03 — Resumen verificado | S03, S05 | `implementation/descriptiva/P103_drivers_pandas/submission/summary.csv` (p. ej., conductor 10: 3.232 horas, 147.150 millas); `implementation/descriptiva/P103_drivers_pandas/tests/test_activity.py`: `test_02` | Verifica la suma y la unión, no su interpretación. |
| H04 — Ranking visual | S04, S05 | `implementation/descriptiva/P103_drivers_pandas/professor/notebook.ipynb`: celda de gráfico; `implementation/descriptiva/P103_drivers_pandas/submission/top10_drivers.png` | La prueba no verifica contenido, orden ni rotulado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset conductores y semanas | `data/drivers.csv`; `data/timesheet.csv` | Procedencia no documentada; `drivers` conserva `ssn` y `location`. |
| S02 | Transformaciones y agregaciones | `professor/notebook.ipynb` | `agg([min, max])` usa funciones integradas; tabla bajo la media no persistida. |
| S03 | Resumen persistido | `submission/summary.csv` | Columnas `driverId`, `hours-logged`, `miles-logged`, `name`. |
| S04 | Visualización | `submission/top10_drivers.png`; celda de gráfico | Sin título ni etiquetas. |
| S05 | Pruebas | `tests/test_activity.py` | Existencia, igualdad del resumen y tamaño mínimo de imagen. |
| S06 | Interfaz de estudiante | `notebooks/notebook.ipynb` | Notebook vacío; sin instrucciones ni pregunta declarada. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/notebook.ipynb` calcula medias, semanas bajo la media, totales, mínimos/máximos, unión, ranking y gráfico.
- **`submission/`:** `summary.csv` (34 filas) y `top10_drivers.png`.
- **Pruebas:** exigen ambos archivos, recalculan el resumen desde `data/` y comprueban que la imagen sea legible y mayor de 100 × 100 píxeles. No verifican las medias, el filtro intra-grupo, el top 10 ni la interpretación.
- **Trazabilidad:** P103 mapea `descriptiva.C02` y `descriptiva.C03`.

### Dependencias en la secuencia

- **Recibe de P102:** `data/drivers.csv` (misma tabla).
- **Habilita para P104 y P105:** P104 reproduce las mismas preguntas y el mismo contrato de `submission/` en SQLite; P105 contiene el código de P103 comentado junto a cada *prompt*.

## Trazabilidad y auditoría

P103 está mapeada a `descriptiva.C02` y `descriptiva.C03` en `implementation/descriptiva/traceability.yaml`; ambas tienen respaldo: agregación y comparación intra-grupo (C02) y un ranking visual persistido (C03). La exploración se limita a medias, sumas y extremos, sin distribución ni calidad de datos. Frente a la pregunta descriptiva, responde «qué» (volumen de horas y millas) y «para quién» en el sentido de la entidad (conductor), pero no para qué usuario o decisión. Es el primer taller con un producto descriptivo reconocible; pandas y matplotlib sirven a ese producto, aunque la ausencia de pregunta declarada y de interpretación lo acerca a un ejercicio de herramienta.
