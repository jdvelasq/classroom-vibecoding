# P429 — Prefect: flujo orquestado de carga y resumen por fábrica

## Actividad actual implementada

**Implementación:** `implementation/productos/P429_prefect/`.

### Preguntas analíticas actuales

- ¿Cómo se organiza el cálculo de unidades por fábrica como un flujo de tareas con dependencias explícitas y un punto de recuperación?

`professor/main.py` declara dos tareas Prefect —`load_operations` con `@task(retries=1)` y `summarize_operations`— y un `@flow` `operations_flow` que encadena ambas y escribe `submission/prefect_report.json`. El dato es el mismo `data/daily_operations.csv` de cuatro filas de P428. `HOW_TO_RUN_ME.txt` indica que «en clase se observa» que las dos funciones son tareas independientes dentro del flujo. El reporte persistido contiene `{"1": 9303, "2": 9300}`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/prefect_report.json` con totales por fábrica, producido por un flujo orquestado.
- **Uso y límite:** hace visible la descomposición de una capacidad en tareas con dependencia y una política de reintento declarada. El reintento nunca se ejercita: no hay fallo provocado, ni prueba, ni registro persistido de estados de tareas; el reporte no conserva marca de ejecución (a diferencia de P428).
- **Disciplinas contribuyentes:** orquestación de flujos con Prefect; agregación con pandas reutilizada.

### Highlights de contribución

- **H01 — Descompone una capacidad en tareas con dependencia declarada:** `operations_flow` pasa la salida de `load_operations` a `summarize_operations`; la docstring del flujo afirma que «declara la dependencia entre cargar datos y producir el indicador». Extiende P428 (una función agendada) a un grafo de dos tareas. Sin este hito, la secuencia no mostraría la unidad de orquestación por tarea.
- **H02 — Declara una política de recuperación en la tarea de carga:** `@task(retries=1)` en `load_operations`; `HOW_TO_RUN_ME.txt` la presenta como «política de recuperación». La política queda declarada, no demostrada. Sin este hito, el reintento como decisión operativa no aparecería antes de los talleres de incidentes.
- **H03 — Verifica la lógica de una tarea fuera del orquestador:** `professor/test_main.py` invoca `summarize_operations.fn(...)` y obtiene `{"north": 12, "south": 11}`; la docstring declara que cada tarea conserva «una responsabilidad verificable fuera del orquestador». Continúa la separación cálculo/ejecución de P428 H01 con el mecanismo propio de Prefect.
- **H04 — Caso y datos (límite):** el extracto de cuatro filas sin fecha y sin fallos posibles no impone ninguna condición que exija orquestación ni reintentos; el mismo total se obtiene en P400–P428. La implementación no revela una particularidad del caso que cambie la representación o validación; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** decoradores `@task` y `@flow` de Prefect; `retries`; acceso a la función subyacente con `.fn` en pruebas.
- **Reutiliza:** `daily_operations.csv`, agregación por fábrica, formato `{"factory_totals": ...}` de P413 y P417.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Flujo de tareas | H01 | `@flow` que encadena dos `@task` | Dos tareas lineales; sin paralelismo ni ramas. |
| Reintento | H02 | `retries=1` | Declarado, no ejercitado ni probado. |
| Prueba de tarea aislada | H03 | `summarize_operations.fn` | Sólo la tarea de resumen. |
| Caso | H04 | Mismo extracto estático | Sin particularidad que justifique orquestar. |

### Relación técnica con actividades anteriores

Misma pregunta y dato que P428 y anteriores, con nuevo mecanismo de ejecución (orquestador en lugar de agenda). P429 no agenda el flujo, de modo que P428 y P429 cubren piezas separadas (cuándo y cómo) que no se integran. Frente a P405 (logs), Prefect produciría estados observables, pero ninguno se persiste. La repetición del mismo cálculo es posible duplicación de caso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Tareas con dependencia | S02 | `implementation/productos/P429_prefect/professor/main.py`: `operations_flow` | Grafo trivial. |
| H02 — Reintento declarado | S02, S05 | `implementation/productos/P429_prefect/professor/main.py`: `load_operations`; `implementation/productos/P429_prefect/HOW_TO_RUN_ME.txt` | Ningún fallo provocado. |
| H03 — Tarea probada aislada | S04 | `implementation/productos/P429_prefect/professor/test_main.py` | No prueba el flujo ni la carga. |
| H04 — Caso como límite | S01, S03 | `implementation/productos/P429_prefect/data/daily_operations.csv`; `implementation/productos/P429_prefect/submission/prefect_report.json` | Ausencia de particularidad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/daily_operations.csv` | Idéntico a P428. |
| S02 | Flujo y tareas | `professor/main.py`; `requirements.txt` | Dos tareas; `prefect>=3,<4` en manifiesto local. |
| S03 | Reporte | `submission/prefect_report.json` | Sin marca de ejecución ni estados. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del reporte; una tarea. |
| S05 | Interfaz del estudiante | `src/main.py`; `HOW_TO_RUN_ME.txt` | Plantilla vacía; observación del flujo sólo en clase. |

### Contrato de evidencia actual

- **Notebook o código:** carga y resume en un flujo de dos tareas y escribe el reporte.
- **`submission/`:** `prefect_report.json`.
- **Pruebas:** `test_01` exige el archivo; la prueba de profesor verifica la suma de `summarize_operations`. No verifican el reintento, la dependencia ni el estado del flujo.
- **Trazabilidad:** P429 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P428:** mismo dato y agregación; separación cálculo/ejecución.
- **Habilita para Pyyy:** no evidenciada; ninguna actividad posterior inspeccionada usa Prefect.

## Trazabilidad y auditoría

P429 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en la integración del cálculo en un flujo; C05 sólo en un reintento declarado y no ejercitado. Auditoría de identidad (pregunta 5): sin usuario, decisión ni condición del dato que exija orquestar, el taller se lee como introducción a Prefect. Riesgo de identidad registrado.
