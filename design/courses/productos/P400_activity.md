# P400 — Code testing con unittest: totales de producción por fábrica

## Actividad actual implementada

**Implementación:** `implementation/productos/P400_code_testing_unittest/`.

### Preguntas analíticas actuales

- ¿Cuántas unidades produce en total cada fábrica a partir del registro de producción diaria de sus máquinas, y cómo se comprueba que esa regla de cálculo es correcta antes de publicar el resultado?

`data/daily_operations.csv` tiene cuatro filas (`factory_id`, `machine_id`, `daily_units_produced`): dos fábricas con dos máquinas cada una. Cada fila es una máquina de una fábrica; no hay columna de fecha pese al nombre de la variable. `professor/main.py` separa lectura con conversión de tipos (`load_operations`), regla de negocio (`summarize_by_factory`), escritura (`write_summary`) y orquestación (`main`). El producto es `submission/factory_totals.csv` con totales 9303 (fábrica 1) y 9300 (fábrica 2). La regla se prueba con `unittest` en `professor/test_main.py`. No hay notebook, instrucciones (`HOW_TO_RUN_ME.txt`) ni procedencia del dato.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** total de unidades por fábrica; usuario y decisión no evidenciados en P400 (la tarjeta de P408 declara después un consumidor para `factory_totals`).
- **Producto terminal:** `submission/factory_totals.csv` (`factory_id`, `total_units`) generado por una función aislada y probada.
- **Uso y límite:** muestra cómo proteger con una prueba unitaria la regla que produce un indicador descriptivo. El indicador es una suma de cuatro valores; no permite inferir nada sobre el desempeño de las fábricas ni sobre el uso del total.
- **Disciplinas contribuyentes:** ingeniería de software (separación de responsabilidades y pruebas unitarias) al servicio de la confiabilidad de un indicador.

### Highlights de contribución

- **H01 — Aísla la regla de cálculo de la entrada y la salida:** `summarize_by_factory` recibe una lista de diccionarios y devuelve los totales ordenados por `factory_id`, sin leer archivos ni imprimir; `load_operations` convierte cada campo a `int` para «distinguir un error de entrada de un error de cálculo»; `main` sólo conecta las partes. Primera aparición en el curso de la descomposición que las actividades posteriores reutilizan (P401, P402, P412). Sin este hito, la regla del indicador no sería comprobable por separado.
- **H02 — Verifica la regla con un caso construido en `unittest`:** `TestSummarizeByFactory.test_01_sums_daily_units_for_each_factory` entrega las cuatro operaciones en orden permutado y exige exactamente `[{factory_id: 1, total_units: 9303}, {factory_id: 2, total_units: 9300}]`, de modo que comprueba agregación y orden. El módulo se carga con `importlib.util.spec_from_file_location`, sin depender de la profundidad del directorio. Primera prueba de lógica del curso. Sin este hito, el total persistido no tendría una expectativa verificable.
- **H03 — Opera un indicador sin particularidad de datos (caso y datos, límite):** el dato tiene granularidad fábrica-máquina, cuatro filas, sin tiempo ni procedencia; el producto es una suma por fábrica. La implementación no revela una condición del caso que cambie la representación o la validación: el CSV es intercambiable. Esa ausencia delimita lo que se opera aquí: una regla trivial elegida para concentrar la práctica en la prueba.

### Inventario técnico de implementación

- **Introduce:** separación lectura/regla/escritura/orquestación; prueba unitaria con `unittest.TestCase`; carga del módulo por ruta con `importlib`; persistencia del indicador en CSV con `csv.DictWriter`.
- **Aplica en nuevo caso:** agregación por clave con diccionario acumulador en Python puro.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Función pura de negocio | H01 | `summarize_by_factory` sin E/S; `main` orquesta | Sin manejo de errores de entrada. |
| Prueba unitaria | H02 | `unittest` con entrada permutada y salida exacta | Una sola prueba; vive en `professor/`. |
| Indicador persistido | H01, H03 | `factory_totals.csv` con dos totales | Dato de cuatro filas sin procedencia. |

### Relación técnica con actividades anteriores

Primera actividad P4xx (la trazabilidad incluye P001, fuera de este alcance). Introduce el indicador `factory_totals` y el archivo `daily_operations.csv` que reaparecen, idénticos, en P412–P414 y como nombre de producto en la tarjeta de P408–P411.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Regla aislada | S02, S04 | `implementation/productos/P400_code_testing_unittest/professor/main.py`: `summarize_by_factory`, `load_operations`, `write_summary`, `main`; `implementation/productos/P400_code_testing_unittest/submission/factory_totals.csv` | El estudiante sólo recibe `src/main.py` con `NotImplementedError`. |
| H02 — Prueba unitaria | S03, S05 | `implementation/productos/P400_code_testing_unittest/professor/test_main.py`: `test_01_sums_daily_units_for_each_factory` | La prueba no está en `tests/`; la evaluación sólo verifica existencia del CSV. |
| H03 — Caso sin particularidad | S01 | `implementation/productos/P400_code_testing_unittest/data/daily_operations.csv` | Sin procedencia, fecha ni usuario declarados. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/daily_operations.csv` | Cuatro filas; sin fecha ni procedencia. |
| S02 | Regla y orquestación | `professor/main.py` | Python puro; sin validación de entrada. |
| S03 | Prueba de la regla | `professor/test_main.py` | Un caso `unittest`; fuera de `tests/`. |
| S04 | Producto | `submission/factory_totals.csv` | Dos filas `factory_id,total_units`. |
| S05 | Prueba de evaluación | `tests/test_activity.py` | Sólo existencia del archivo. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin instrucciones ni notebook. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` lee, agrega, escribe y debe conservar la separación de responsabilidades.
- **`submission/`:** `factory_totals.csv` con los totales por fábrica.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista `factory_totals.csv`; no verifica columnas, valores ni que exista una prueba unitaria del estudiante. `professor/test_main.py` sí verifica valores y orden de la regla del profesor.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna demostrable dentro de P400–P413.
- **Habilita para Pyyy:** P408 (la tarjeta versiona el producto `factory_totals`); P412, P413 y P414 reutilizan el mismo `daily_operations.csv` (79 bytes, mismo contenido) y la misma agregación por fábrica.

## Trazabilidad y auditoría

Entrada revisada: P400 → `productos.C02`, `productos.C05`. C02 se sostiene parcialmente: el indicador se vuelve verificable mediante una prueba. C05 (observar, gobernar, recuperar) no se evidencia: no hay monitoreo, registro ni recuperación. El producto de Analytics es un indicador descriptivo mínimo sin usuario declarado; la actividad se lee como una práctica de pruebas unitarias de software aplicada a una suma (pregunta de auditoría 5), con riesgo de identidad hacia ingeniería de software general.
