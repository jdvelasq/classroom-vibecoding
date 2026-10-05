# P521 — Unión de métricas de conductores con el registro maestro

## Actividad actual implementada

**Implementación:** `implementation/data/P521_mapreduce_avanzado/`.

### Preguntas analíticas actuales

- ¿Qué conductores tienen mayor actividad una vez que relacionamos sus métricas con el registro maestro?

Usa los mismos `data/timesheet.csv` (1768 filas) y `data/drivers.csv` (34 filas) de P519. El notebook copia los operadores de P519, incluido `inner_join_by_key`; recalcula horas, millas y semanas por conductor con el mismo mapper de P520; transforma el maestro en pares `(driverId, {"name": ...})`; une ambas colecciones y ordena por `total_miles` descendente. Persiste `submission/driver_activity.csv` con 34 filas (primera: `11, Jamie Engesser, 3642.0, 179300.0, 52`). La consulta SQL equivalente aparece como comentario. El notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta declarada; usuario y decisión no evidenciados.
- **Producto terminal:** ranking de conductores por millas acumuladas, con nombre legible.
- **Uso y límite:** identifica quién acumula más millas en el registro. «Mayor actividad» se operacionaliza sólo como millas; con horas el orden cambia (en los archivos persistidos, el conductor 14 tiene 2781 horas y el 33, 2759, pero el 33 aparece tercero y el 14 no está entre los cinco primeros). El maestro incluye `wage-plan` (`miles`/`hours`) y `certified`, que no se usan.
- **Disciplinas contribuyentes:** unión por clave y SQL como especificación, al servicio de un ranking descriptivo.

### Highlights de contribución

- **H01 — Reduce el registro semanal al grano del maestro antes de unir (caso y datos):** los turnos están a grano conductor-semana (1768 filas) y el maestro a grano conductor (34); el notebook reduce primero (`summarize_driver_metrics`) y después une, de modo que cada atributo del maestro se combina una vez por conductor. La celda de reducción lo declara: «conserva driverId como clave para relacionar el resultado con otra fuente». Sin este hito, la unión se aprendería sin la decisión de grano que evita repetir el maestro por semana.
- **H02 — Une métricas y maestro con una regla de combinación explícita:** `inner_join_by_key(driver_metric_pairs, driver_name_pairs, combine_driver_activity)` y `combine_driver_activity` fusiona diccionarios (`{"driverId", **driver, **metrics}`). Extiende la unión de P519 de dos a 34 conductores. No se comparan conteos antes y después: una clave ausente se descartaría sin aviso. Sin este hito, las métricas de P520 seguirían identificadas sólo por un número.
- **H03 — Ordena por una medida para responder «mayor actividad»:** `driver_activity.sort(key=lambda record: record["total_miles"], reverse=True)` en correspondencia con `ORDER BY metrics.total_miles DESC` del SQL comentado. La elección de millas como medida no se justifica. Sin este hito, la unión no produciría una respuesta a la pregunta.

### Inventario técnico de implementación

- **Extiende:** unión por clave de P519 a toda la población; SQL comentado de P520 a `INNER JOIN` con `ORDER BY`.
- **Reutiliza:** `map_pairs`, `group_by_key`, `reduce_by_key`, `inner_join_by_key` (copia literal de P519); mapper y reducer de P520 (sin `mean_hours`).
- **Introduce:** mapeo del maestro a pares con valor diccionario; ordenamiento de registros por medida.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Reducción antes de unión | H01 | Grano conductor-semana → conductor → unión | Cardinalidad no verificada. |
| Unión con regla explícita | H02 | `inner_join_by_key` + `combine_driver_activity` | Pérdidas por clave ausente no reportadas. |
| Ranking por medida | H03 | `driver_activity.csv` ordenado por millas | Medida elegida sin justificación; `wage-plan` ignorado. |

### Relación técnica con actividades anteriores

Misma pregunta de dominio que P520 con nuevo paso (unión y orden). La agregación se repite íntegra en lugar de leer `driver_metrics.csv` de P520, y la unión con nombres ya se había mostrado en P519 sobre dos conductores; el incremento propio es pequeño: unión a escala completa y orden. Posible duplicación con P519–P520 que requiere decisión posterior. Coincide con `dig/case-selection.md` (unión, agregación y ordenamiento sencillo); el SQL comentado selecciona `drivers.name` pero la salida incluye también `driverId`, y la afirmación «los operadores producen el mismo resultado» no se comprueba.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Grano antes de unir | S01, S02 | `implementation/data/P521_mapreduce_avanzado/data/timesheet.csv`; `implementation/data/P521_mapreduce_avanzado/data/drivers.csv`; `implementation/data/P521_mapreduce_avanzado/professor/notebook.ipynb`: celdas de reducción | Unicidad de `driverId` en el maestro no verificada. |
| H02 — Unión explícita | S02, S03 | `implementation/data/P521_mapreduce_avanzado/professor/notebook.ipynb`: `map_driver_record`, `combine_driver_activity`, `inner_join_by_key`; `implementation/data/P521_mapreduce_avanzado/submission/driver_activity.csv` | 34 filas en ambos lados; no se ejercita una ausencia. |
| H03 — Ranking | S02, S03 | `implementation/data/P521_mapreduce_avanzado/professor/notebook.ipynb`: última celda; `implementation/data/P521_mapreduce_avanzado/submission/driver_activity.csv`; `implementation/data/P520_mapreduce_basico/submission/driver_metrics.csv` | Ranking por una sola medida. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datasets | `data/timesheet.csv`; `data/drivers.csv` | Idénticos a P519; `ssn` y `location` presentes sin uso. |
| S02 | Operadores, unión y orden | `professor/notebook.ipynb` | Agregación repetida de P520. |
| S03 | Producto | `submission/driver_activity.csv` | Sin `questions.json`. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Vacío. |

### Contrato de evidencia actual

- **Notebook o código:** debe reducir turnos a conductores, unir con nombres y ordenar por millas.
- **`submission/`:** `driver_activity.csv` (34 conductores ordenados por `total_miles`).
- **Pruebas:** `test_01_submission_contains_driver_activity` sólo verifica que exista el archivo; no verifica orden, columnas ni cardinalidad.
- **Trazabilidad:** `data.C01`, `data.C02`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** P519: operadores, incluida la unión, y datos idénticos; P520: mapper y reducer (sin consumir su archivo).
- **Habilita para Pyyy:** no evidenciada; P522 cambia de dataset y sólo copia los tres operadores centrales.

## Trazabilidad y auditoría

Entrada revisada: P521 → `data.C01`, `data.C02`, `data.C05`. `data.C01` se apoya en la decisión de grano antes de unir; la operacionalización de «actividad» no se justifica. Auditoría: producto descriptivo (ranking) con pregunta explícita; la unión sirve a la respuesta. Riesgo de identidad bajo, pero riesgo de duplicación con P519–P520.
