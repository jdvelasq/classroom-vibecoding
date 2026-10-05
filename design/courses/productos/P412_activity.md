# P412 — Ambiente reproducible: ejecutar y verificar el indicador por fábrica en un ambiente declarado

## Actividad actual implementada

**Implementación:** `implementation/productos/P412_repro_environment/`.

### Preguntas analíticas actuales

- ¿Se obtiene el mismo indicador por fábrica cuando el código se ejecuta en un ambiente aislado con la dependencia declarada, y con qué versiones se produjo?

`HOW_TO_RUN_ME.txt` crea `.venv` con `python3 -m venv`, instala `requirements.txt` (`pandas==2.2.3`), ejecuta `python3 -m unittest discover -s tests -p "test_*.py" -v` y luego `python3 src/main.py`. `professor/main.py` suma `daily_units_produced` por fábrica sobre el mismo `data/daily_operations.csv` de P400 y escribe `submission/environment_report.json` con `python_version` (3.9.6), `pandas_version` (2.2.3) y `factory_totals` (9303 y 9300). `tests/test_environment_report.py` ejecuta `src/main.py` y compara los totales con los valores conocidos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** reproducir el indicador por fábrica en un ambiente declarado; usuario no evidenciado en esta actividad.
- **Producto terminal:** `submission/environment_report.json`, indicador acompañado de las versiones que lo produjeron.
- **Uso y límite:** permite atribuir un resultado a un ambiente y detectar si cambia. No demuestra que un ambiente distinto altere el resultado, no fija la versión de Python y la dependencia declarada es una sola.
- **Disciplinas contribuyentes:** gestión de ambientes de Python (`venv`, `pip`) y pruebas de regresión al servicio de la reproducibilidad del indicador.

### Highlights de contribución

- **H01 — Aísla la ejecución en un ambiente con dependencia fijada:** `python3 -m venv .venv`, activación local a la terminal, `python3 -m pip install --requirement requirements.txt` con `pandas==2.2.3`; `.venv` «no se entrega ni se sube al repositorio». Primera declaración de ambiente del curso. Sin este hito, el resultado dependería de paquetes globales del equipo.
- **H02 — Registra la procedencia del resultado junto al indicador:** el reporte guarda `python_version` y `pandas_version` además de `factory_totals`; el persistido declara 3.9.6 y 2.2.3. Primera vez que la evidencia del curso incluye el ambiente de ejecución. Sin este hito, un resultado persistido no podría atribuirse a las versiones que lo produjeron.
- **H03 — Verifica el resultado conocido del producto como prueba de regresión:** `EnvironmentReportTest.test_factory_totals` ejecuta `src/main.py` con `sys.executable` y exige `[{factory_id: 1, total_units_produced: 9303}, {factory_id: 2, total_units_produced: 9300}]`. Es la primera prueba en `tests/` que ejecuta el código del estudiante y verifica valores; está escrita con `unittest` y es descubrible por `pytest`. Sin este hito, la reproducibilidad sería una afirmación sin comprobación.
- **H04 — Reutiliza un indicador fijo como referencia (caso y datos, límite):** el dato y el cálculo son los de P400 («Resume una métrica conocida para concentrar el taller en el ambiente»); el caso no impone ninguna particularidad, y la columna cambia de `total_units` (P400) a `total_units_produced`. Sin este hito no se vería que el valor conocido sirve de referencia de regresión; con él queda visible que el contrato de salida del mismo indicador no es estable entre actividades.

### Inventario técnico de implementación

- **Introduce:** `venv`, activación y desactivación, `pip install --requirement`, `requirements.txt` local con versión fijada, registro de versiones en el reporte, prueba que ejecuta el programa por `subprocess`.
- **Reutiliza:** `daily_operations.csv` y agregación por fábrica de P400, ahora con pandas.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Ambiente aislado | H01 | `venv` + `requirements.txt` fijado | Python no fijado. |
| Procedencia de ejecución | H02 | Versiones en el reporte | Dos versiones. |
| Prueba de regresión | H03 | `subprocess` + totales esperados | Valores fijos de cuatro filas. |
| Contrato de salida | H04 | `total_units_produced` | Difiere de P400. |

### Relación técnica con actividades anteriores

Misma pregunta y dato que P400 con nueva exigencia de evidencia (ambiente declarado y versiones registradas). La prueba pasa del profesor (P400–P404) a `tests/`, sobre el código del estudiante. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Ambiente | S02, S03 | `implementation/productos/P412_repro_environment/HOW_TO_RUN_ME.txt`; `implementation/productos/P412_repro_environment/requirements.txt` | Compatibilidad con el `requirements.txt` raíz no verificable aquí. |
| H02 — Procedencia | S04, S05 | `implementation/productos/P412_repro_environment/professor/main.py`: `main`; `implementation/productos/P412_repro_environment/submission/environment_report.json` | Versiones del equipo que generó la evidencia. |
| H03 — Regresión | S06 | `implementation/productos/P412_repro_environment/tests/test_environment_report.py`: `test_factory_totals` | Sobrescribe el reporte al ejecutarse. |
| H04 — Indicador de referencia | S01, S04 | `implementation/productos/P412_repro_environment/data/daily_operations.csv`; `implementation/productos/P412_repro_environment/professor/main.py`: `summarize_by_factory` | Sin particularidad de datos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/daily_operations.csv` | Igual a P400. |
| S02 | Declaración de ambiente | `requirements.txt` | Una dependencia fijada. |
| S03 | Instrucciones | `HOW_TO_RUN_ME.txt` | Comandos para macOS/Linux (`source`). |
| S04 | Indicador y reporte | `professor/main.py` | Docstrings en todas las funciones. |
| S05 | Producto | `submission/environment_report.json` | Versiones + totales. |
| S06 | Pruebas | `tests/test_environment_report.py`; `tests/test_activity.py` | Una verifica valores; la otra existencia. |
| S07 | Interfaz del estudiante | `src/main.py` | Plantilla vacía. |

### Contrato de evidencia actual

- **Notebook o código:** calcula el indicador, registra versiones e imprime y persiste el reporte.
- **`submission/`:** `environment_report.json` con versiones y totales.
- **Pruebas:** `tests/test_environment_report.py::test_factory_totals` ejecuta `src/main.py` y verifica los totales; no verifica las versiones registradas ni que se use el ambiente aislado. `tests/test_activity.py::test_01` sólo exige que exista el reporte.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P400:** `daily_operations.csv` (mismo contenido) y la agregación por fábrica.
- **Habilita para P413 y P414:** el mismo `requirements.txt` (`pandas==2.2.3`) y el mismo dato; la prueba por `subprocess` del valor conocido reaparece en `tests/test_report.py`.

## Trazabilidad y auditoría

Entrada revisada: P412 → `productos.C02`, `productos.C05`. C02 se sostiene (ejecución reproducible y verificable); C05 débilmente (registro de procedencia de la ejecución). El producto es el indicador de P400 vuelto reproducible; la práctica de ambientes sirve a ese indicador, aunque su trivialidad hace que el taller se lea como introducción a `venv` (pregunta de auditoría 5). El `requirements.txt` local es un artefacto del contrato de ejecución; `structure-audit.md` sólo documenta la excepción de P426.
