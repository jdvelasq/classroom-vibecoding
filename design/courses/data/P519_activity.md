# P519 — Operadores clave–valor sobre un extracto de turnos de conductores

## Actividad actual implementada

**Implementación:** `implementation/data/P519_mapreduce_operators/`.

### Preguntas analíticas actuales

- No hay pregunta analítica; la primera celda declara un propósito técnico: «Este taller muestra cómo operan los operadores clave–valor antes de aplicarlos a un caso analítico».

`data/timesheet.csv` tiene 1768 filas (`driverId`, `week`, `hours-logged`, `miles-logged`), una por conductor y semana según las cabeceras; `data/drivers.csv` tiene 34 filas (`driverId`, `name`, `ssn`, `location`, `certified`, `wage-plan`). La procedencia no está documentada en la actividad. El notebook del profesor filtra un extracto de cuatro registros (conductores 10 y 11, semanas 1–2), define operadores genéricos que reciben la regla del caso como función y muestra la salida de cada paso. Persiste `submission/operator_walkthrough.csv` con dos filas: `10, George Vetticaden, 140.0` y `11, Jamie Engesser, 133.0`. El notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados (taller técnico declarado).
- **Producto terminal:** traza persistida de una agregación y una unión por clave sobre cuatro registros.
- **Uso y límite:** permite seguir a mano cómo pares clave–valor se agrupan, reducen y unen. No responde nada sobre la operación de transporte; dos conductores y dos semanas no describen a la flota.
- **Disciplinas contribuyentes:** modelo de cómputo MapReduce y programación funcional en Python puro, como preparación de P520–P521; según la aclaración del profesor (2026-10-05), el procesamiento clave–valor introductorio pertenece al curso como puente hacia la analítica.

### Highlights de contribución

- **H01 — Separa el operador genérico de la regla del caso:** `map_pairs(records, mapper)`, `group_by_key(pairs)` y `reduce_by_key(grouped_values, reducer)` no conocen el dominio; `map_timesheet_hours` y `sum_driver_hours` sí. Cada celda deja visible su salida (`hour_pairs`, `hours_by_driver`, `total_hour_pairs`), incluido el agrupamiento que representa el shuffle. Primera aparición en el curso; P520–P523 copian literalmente estas funciones. Sin este hito, los talleres siguientes reutilizarían operadores no explicados.
- **H02 — Reduce el caso a un extracto legible con una llave compartida entre fuentes (caso y datos):** el registro de turnos está a grano conductor-semana y el maestro a grano conductor; ambos comparten `driverId`. El filtro `driverId in {"10","11"}` y `week <= 2` deja cuatro filas cuya suma puede verificarse contra las primeras líneas de `timesheet.csv` (70 + 70 = 140.0 para el conductor 10). Esa llave común es la que permite pasar de la agregación a la unión. Sin este hito, los operadores se demostrarían sobre datos sin relación entre fuentes.
- **H03 — Une dos colecciones de pares por clave con una regla de combinación explícita:** `inner_join_by_key(left_pairs, right_pairs, joiner)` construye `dict(right_pairs)` y descarta claves sin pareja; `combine_driver_hours` decide la forma del registro de salida. Es la primera unión fuera de SQL/pandas en el curso. El uso de `dict` supone que la clave derecha es única: un duplicado se sobrescribiría sin aviso. Sin este hito, P521 no tendría el operador de unión que reutiliza.
- **H04 — Encadena operadores complementarios sobre la misma colección:** `filter_records` (semana 1), `map_values` (horas / 10), `union_pairs` y `sort_by_key` producen `sorted_pairs`. La transformación `/ 10` no tiene significado declarado en el caso, `union_pairs` se aplica con una lista vacía y `flat_map_pairs` (idéntica a `map_pairs`) y `left_outer_join_by_key` se definen sin ejercitarse. Sin este hito, el catálogo de operaciones quedaría reducido a map, shuffle, reduce y join.

### Inventario técnico de implementación

- **Introduce:** operadores de orden superior `map_pairs`, `group_by_key`, `reduce_by_key`, `inner_join_by_key`; operadores complementarios `filter_records`, `map_values`, `union_pairs`, `sort_by_key`; lectura con `csv.DictReader`; escritura con `csv.DictWriter`; búsqueda de la raíz por presencia de `data/` y `submission/`.
- **Define sin ejercitar:** `flat_map_pairs`, `left_outer_join_by_key`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Operadores clave–valor locales | H01 | Funciones que reciben mapper/reducer | Python puro; sin distribución ni tolerancia a fallas. |
| Extracto inspeccionable | H02 | Cuatro registros, dos fuentes, llave `driverId` | Procedencia de los datos no documentada. |
| Unión por clave | H03 | `inner_join_by_key` con `dict` | Unicidad de la derecha implícita. |
| Encadenamiento de operadores | H04 | `sorted_pairs` | Transformación `/ 10` sin significado; dos operadores sin uso. |

### Relación técnica con actividades anteriores

Nuevo método (modelo clave–valor) sin pregunta propia; los datos de conductores no aparecen en P500–P518. Respecto de las uniones SQL de P503–P508, la unión se reconstruye como operador explícito. Coincide con el diseño de `dig/case-selection.md` (operaciones genéricas visibles con un extracto pequeño del mismo dominio; sin PySpark); los nombres son `map_pairs`/`reduce_by_key` en lugar de `mapPairs`/`reduceByKey`.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Operador y regla | S02 | `implementation/data/P519_mapreduce_operators/professor/notebook.ipynb`: celdas de `map_pairs`, `group_by_key`, `reduce_by_key` | Sin salida persistida de pasos intermedios. |
| H02 — Extracto y llave compartida | S01, S02 | `implementation/data/P519_mapreduce_operators/data/timesheet.csv`; `implementation/data/P519_mapreduce_operators/data/drivers.csv`; primera celda del notebook | `drivers.csv` incluye `ssn` y `location`, no usados ni documentados. |
| H03 — Unión por clave | S02, S03 | `implementation/data/P519_mapreduce_operators/professor/notebook.ipynb`: `inner_join_by_key`, `combine_driver_hours`; `implementation/data/P519_mapreduce_operators/submission/operator_walkthrough.csv` | No se ejercita una clave ausente o duplicada. |
| H04 — Operadores complementarios | S02 | `implementation/data/P519_mapreduce_operators/professor/notebook.ipynb`: celda de operadores complementarios | Resultado no persistido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datasets | `data/timesheet.csv`; `data/drivers.csv` | Sin procedencia; columnas `ssn` y `location` presentes. |
| S02 | Operadores y reglas del caso | `professor/notebook.ipynb` | Copiados literalmente por P520–P523. |
| S03 | Producto | `submission/operator_walkthrough.csv` | Dos filas; sin `questions.json`. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia del archivo. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Vacío. |

### Contrato de evidencia actual

- **Notebook o código:** debe mostrar cada operador con su entrada y salida y producir la unión de horas totales con nombres.
- **`submission/`:** `operator_walkthrough.csv` (dos conductores, horas totales de dos semanas).
- **Pruebas:** `test_01_submission_contains_operator_walkthrough` verifica sólo que el archivo exista; no verifica columnas ni valores.
- **Trazabilidad:** `data.C02`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna demostrable.
- **Habilita para Pyyy:** P520 y P521 copian `map_pairs`, `group_by_key`, `reduce_by_key` (y P521 `inner_join_by_key`) bajo «Estas son las funciones que definimos en la actividad anterior» y usan los mismos `timesheet.csv` y `drivers.csv` (mismos tamaños); P522 y P523 copian las tres funciones centrales.

## Trazabilidad y auditoría

Entrada revisada: P519 → `data.C02`, `data.C05`; coherente con un taller técnico de preparación. Auditoría (pregunta 5): aislado, es una lección de modelo de cómputo sin producto analítico. Tras la aclaración del profesor (2026-10-05), el procesamiento clave–valor introductorio pertenece al curso como puente, de modo que ese carácter no es por sí solo un problema de identidad; se conserva como límite que el taller no tiene producto propio y que su finalidad analítica depende de que P520–P521 lo usen para responder preguntas, lo que sí ocurre. La presencia de `ssn` en un dataset distribuido al estudiante requiere revisión de procedencia y sensibilidad.
