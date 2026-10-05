# P520 — Agregación clave–valor de turnos por conductor

## Actividad actual implementada

**Implementación:** `implementation/data/P520_mapreduce_basico/`.

### Preguntas analíticas actuales

- ¿Cuántas horas, millas y semanas de trabajo acumuló cada conductor?

La pregunta abre la segunda celda del notebook del profesor, que la sitúa en «todos los turnos de la operación de transporte». `data/timesheet.csv` es el mismo archivo de P519 (1768 filas, 24437 bytes; grano conductor-semana según sus columnas). El notebook copia de P519 `map_pairs`, `group_by_key` y `reduce_by_key`, define un mapper y un reducer del caso, escribe en comentario la consulta SQL equivalente y persiste `submission/driver_metrics.csv`: 34 conductores con `total_hours`, `total_miles`, `weeks` y `mean_hours` (primera fila: `10, 3232.0, 147150.0, 52, 62.15`). No se documenta procedencia de los datos ni usuario de la respuesta. El notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta declarada; usuario y decisión no evidenciados («operación de transporte» sin más precisión).
- **Producto terminal:** tabla de una fila por conductor con totales, conteo de semanas y horas medias por semana.
- **Uso y límite:** describe la actividad acumulada por conductor en el registro disponible. No compara conductores ni explica diferencias; el periodo que cubren las 52 semanas y la procedencia no están documentados.
- **Disciplinas contribuyentes:** modelo clave–valor y SQL como especificación declarativa, al servicio de un resumen por entidad.

### Highlights de contribución

- **H01 — Especifica el resultado con SQL y lo construye con operadores clave–valor:** el comentario `SELECT driverId, SUM("hours-logged"), SUM("miles-logged"), COUNT(*) AS weeks FROM timesheet GROUP BY driverId` fija el resultado esperado antes de aplicar `group_by_key` y `reduce_by_key`. La consulta no se ejecuta, la equivalencia no se verifica y la salida añade `mean_hours`, ausente de la consulta; además el SQL aparece después del mapper, no antes. Primera vinculación en el curso entre la secuencia SQL (P504–P507) y el modelo de P519. Sin este hito, los operadores no tendrían una especificación contra la cual leerlos.
- **H02 — Compone un valor (horas, millas, 1) por turno para obtener totales y medias en una sola reducción (caso y datos):** cada fila es una semana de un conductor con medidas aditivas; `map_timesheet_record` emite `(driverId, (hours, miles, 1))` y `summarize_driver_metrics` suma los tres componentes y calcula `mean_hours = total_hours / weeks` desde los totales, no como promedio de promedios. `weeks` es un conteo de filas: equivale a semanas sólo si hay una fila por conductor y semana, condición que no se verifica (todas las filas visibles muestran 52). Sin este hito, el paso de turnos a conductores no haría visible por qué las medidas aditivas y el conteo permiten agregar por partes.
- **H03 — Aplica sin cambios los operadores genéricos al registro completo y persiste la tabla por entidad:** las funciones de P519 se reutilizan sobre 1768 filas; la salida se ordena por `int(pair[0])` porque la clave se lee como texto, y se escribe con `DictWriter`. Sin este hito, P519 quedaría como demostración sin aplicación.

### Inventario técnico de implementación

- **Introduce:** valor compuesto con contador para derivar medias; SQL como especificación en comentario.
- **Reutiliza:** `map_pairs`, `group_by_key`, `reduce_by_key` (P519, copia literal); lectura y escritura con `csv`.
- **Aplica en nuevo caso:** agregación por clave al registro completo de turnos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| SQL como especificación | H01 | `GROUP BY driverId` en comentario | No ejecutado; difiere de la salida en `mean_hours`. |
| Valor compuesto con contador | H02 | `(hours, miles, 1)` y media desde totales | Unicidad conductor-semana supuesta. |
| Tabla por entidad | H03 | `driver_metrics.csv`, 34 filas | Sin comparación ni lectura de diferencias. |

### Relación técnica con actividades anteriores

Mismos datos y operadores que P519 con nueva exigencia: pasar de cuatro registros a la operación completa y responder una pregunta. Respecto de P504–P507, el `GROUP BY` deja de ejecutarse en SQLite y se reconstruye con operadores. Coincide con `dig/case-selection.md` (agregación por `driverId` de horas, millas y semanas; SQL acotado); `mean_hours` no figura en ese diseño.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — SQL como especificación | S02 | `implementation/data/P520_mapreduce_basico/professor/notebook.ipynb`: celda con la consulta comentada | Equivalencia no comprobada. |
| H02 — Valor compuesto | S01, S02, S03 | `implementation/data/P520_mapreduce_basico/data/timesheet.csv`; `implementation/data/P520_mapreduce_basico/professor/notebook.ipynb`: `map_timesheet_record`, `summarize_driver_metrics`; `implementation/data/P520_mapreduce_basico/submission/driver_metrics.csv` | Duplicados conductor-semana no controlados. |
| H03 — Aplicación completa | S02, S03 | `implementation/data/P520_mapreduce_basico/professor/notebook.ipynb`: primera y última celda; `implementation/data/P520_mapreduce_basico/submission/driver_metrics.csv` | Operadores copiados, no importados. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/timesheet.csv` | Idéntico a P519 y P521; sin procedencia. |
| S02 | Especificación y operadores | `professor/notebook.ipynb` | SQL en comentario; funciones copiadas de P519. |
| S03 | Producto | `submission/driver_metrics.csv` | Sin `questions.json`. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Vacío. |

### Contrato de evidencia actual

- **Notebook o código:** debe producir una pareja reducida por conductor con totales, semanas y media, ordenada por identificador numérico.
- **`submission/`:** `driver_metrics.csv` con 34 conductores.
- **Pruebas:** `test_01_submission_contains_driver_metrics` sólo verifica que exista el archivo.
- **Trazabilidad:** `data.C01`, `data.C02`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** P519: operadores (copia literal) y `timesheet.csv` idéntico.
- **Habilita para Pyyy:** P521 repite el mismo mapper y un reducer equivalente sin `mean_hours`; no lee `driver_metrics.csv`.

## Trazabilidad y auditoría

Entrada revisada: P520 → `data.C01`, `data.C02`, `data.C05`. `data.C01` se sostiene parcialmente: la pregunta determina la entidad (conductor) y las medidas, aunque no se documentan restricciones de la fuente. Auditoría: el producto es un resumen descriptivo por entidad y MapReduce sirve para construirlo; el riesgo de leerse como lección de procesamiento distribuido es bajo porque todo es local y la pregunta es explícita, pero la respuesta no se interpreta.
