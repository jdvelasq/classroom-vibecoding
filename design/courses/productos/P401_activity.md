# P401 — Code testing con pytest: totales de conductores certificados

## Actividad actual implementada

**Implementación:** `implementation/productos/P401_code_testing_pytest/`.

### Preguntas analíticas actuales

- ¿Cuántas horas y millas acumula cada conductor certificado, y cómo se comprueba con `pytest` que la transformación que lo calcula conserva esa regla?

`data/drivers.csv` tiene una fila por conductor (34 filas según el conteo de líneas) con `driverId`, `name`, `ssn`, `location`, `certified` y `wage-plan`. `data/timesheet.csv` tiene una fila por conductor y semana (1768 filas) con `hours-logged` y `miles-logged`. `build_certified_driver_totals` agrega horas y millas por conductor, filtra `certified == "Y"` y une ambas tablas; `submission/certified_driver_totals.csv` tiene 32 filas (`driverId`, `name`, `total_hours`, `total_miles`). No hay notebook, instrucciones ni procedencia documentada.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** totales de horas y millas por conductor certificado; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/certified_driver_totals.csv`, generado por una transformación pandas probada.
- **Uso y límite:** muestra cómo proteger con `pytest` una transformación con filtro y unión. No permite inferir carga laboral, cumplimiento ni pago: no hay período, umbral ni uso declarado del total.
- **Disciplinas contribuyentes:** pruebas automatizadas y transformación tabular con pandas.

### Highlights de contribución

- **H01 — Declara las columnas requeridas como precondición de la transformación:** `DRIVER_COLUMNS` y `TIMESHEET_COLUMNS` se verifican con `issubset` y la función lanza `ValueError` si faltan. Extiende P400, donde la entrada sólo se tipaba al leer. Sin este hito, una entrada sin las columnas necesarias fallaría con un error de pandas poco interpretable. La prueba no ejercita esta rama.
- **H02 — Prueba con `pytest` una transformación con DataFrames mínimos:** `test_01_aggregates_only_certified_drivers` construye dos conductores (uno certificado, otro no) y tres turnos, y exige un único registro `{driverId: 1, name: "Ana", total_hours: 14, total_miles: 420}`: verifica a la vez la suma por conductor y la exclusión del no certificado. Cambia de clase `unittest` (P400) a función con `assert`; importa con `sys.path.insert`. Sin este hito, la secuencia no mostraría el estilo de prueba que usan las evaluaciones del curso.
- **H03 — Combina dos granularidades y un atributo sensible (caso y datos):** conductor frente a conductor-semana obliga a agregar `timesheet` antes de unir para no repetir filas; la unión `inner` descarta conductores sin turnos; los nombres con guion (`hours-logged`) exigen agregación por nombre. `drivers.csv` contiene `ssn` y `location`; la transformación sólo propaga `driverId` y `name`, pero el código no declara que la exclusión sea deliberada y el nombre se publica en `submission/`. Sin este hito, el caso sería intercambiable con P400; el tratamiento de identificadores sensibles queda como límite no discutido.

### Inventario técnico de implementación

- **Introduce:** `pytest` con `assert` sobre `to_dict("records")`; precondición de columnas con `ValueError`.
- **Extiende:** la separación transformación/orquestación de P400, ahora con pandas.
- **Aplica en nuevo caso:** `groupby().agg` con agregaciones nombradas, filtro booleano y `merge(how="inner")`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Precondición de esquema | H01 | Subconjunto de columnas requerido | Sin prueba de la rama de error. |
| Prueba de transformación | H02 | `pytest` con DataFrames construidos | Un solo caso; vive en `professor/`. |
| Unión de granularidades | H03 | Agregar antes de unir; filtro de certificación | Sin período ni procedencia. |
| Atributo sensible en la fuente | H03 | `ssn`, `location` presentes; no propagados | Exclusión no declarada; nombre publicado. |

### Relación técnica con actividades anteriores

Misma técnica que P400 (regla aislada probada) con nuevo marco (`pytest`), nueva biblioteca (pandas) y nuevo caso. La diferencia técnica sustantiva es la unión de dos tablas y la precondición de columnas. Posible duplicación con P400: ambas prueban una agregación y su contribución distinguible es el cambio de marco de pruebas; requiere decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Precondición | S02 | `implementation/productos/P401_code_testing_pytest/professor/main.py`: `DRIVER_COLUMNS`, `TIMESHEET_COLUMNS`, `build_certified_driver_totals` | No probada. |
| H02 — Prueba `pytest` | S03, S05 | `implementation/productos/P401_code_testing_pytest/professor/test_main.py`: `test_01_aggregates_only_certified_drivers` | No evalúa al estudiante. |
| H03 — Granularidades y sensibilidad | S01, S02, S04 | `implementation/productos/P401_code_testing_pytest/data/drivers.csv`; `implementation/productos/P401_code_testing_pytest/data/timesheet.csv`; `implementation/productos/P401_code_testing_pytest/submission/certified_driver_totals.csv` | La implementación no discute privacidad ni procedencia. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/drivers.csv`; `data/timesheet.csv` | Incluye `ssn` y `location`; sin procedencia. |
| S02 | Transformación | `professor/main.py` | Agregar, filtrar, unir `inner`. |
| S03 | Prueba de la transformación | `professor/test_main.py` | Un caso; fuera de `tests/`. |
| S04 | Producto | `submission/certified_driver_totals.csv` | Publica `name`. |
| S05 | Prueba de evaluación | `tests/test_activity.py` | Sólo existencia. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` valida columnas, agrega, filtra, une y persiste.
- **`submission/`:** `certified_driver_totals.csv` con 32 conductores.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista el CSV. `professor/test_main.py` verifica suma y filtro en un caso mínimo; no verifica la precondición de columnas ni la unión con conductores sin turnos.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** práctica de P400 (regla aislada de la E/S y probada).
- **Habilita para Pyyy:** no evidenciada dentro de P402–P413.

## Trazabilidad y auditoría

Entrada revisada: P401 → `productos.C02`, `productos.C05`. C02 se sostiene parcialmente (transformación verificable); C05 no se evidencia. El producto es una tabla descriptiva sin usuario ni decisión. La actividad se lee como entrenamiento en `pytest` con un caso de ejemplo (pregunta de auditoría 5). La presencia de `ssn` en el dato sin tratamiento explícito es una condición del caso que la actividad no convierte en práctica.
