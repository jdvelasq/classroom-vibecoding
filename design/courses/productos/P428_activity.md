# P428 — Schedule: ejecución periódica local de un reporte por fábrica

## Actividad actual implementada

**Implementación:** `implementation/productos/P428_schedule/`.

### Preguntas analíticas actuales

- ¿Cómo se ejecuta de forma periódica, sin intervención manual, el cálculo de unidades producidas por fábrica, y qué límite tiene hacerlo con un proceso local?

`data/daily_operations.csv` tiene cuatro filas (dos fábricas × dos máquinas) con `factory_id`, `machine_id` y `daily_units_produced`; no tiene columna de fecha. `professor/main.py` separa `build_report` (suma por `factory_id` más una marca `executed_at` en UTC) de `generate_report` (lee, calcula y sobrescribe `submission/scheduled_report.json`) y agenda esta última con `schedule.every(10).seconds` dentro de un ciclo `while True`. `HOW_TO_RUN_ME.txt` declara el límite: si se cierra la terminal o se apaga el computador, la programación deja de ejecutarse. El reporte persistido muestra `{"1": 9303, "2": 9300}` con `executed_at` `2026-09-28T19:06:49.774446+00:00`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; no se nombra quién consume el reporte ni qué decisión apoya.
- **Producto terminal:** `submission/scheduled_report.json`, un total por fábrica con la marca de la última ejecución.
- **Uso y límite:** muestra que una capacidad descriptiva puede refrescarse por agenda y que la agenda local depende de un proceso vivo. No hay historial de ejecuciones (cada corrida sobrescribe la anterior), ni manejo de fallos, ni relación entre la cadencia de 10 segundos y la frecuencia con que cambian los datos.
- **Disciplinas contribuyentes:** automatización de tareas con la biblioteca `schedule`; la agregación con pandas es la misma de actividades previas.

### Highlights de contribución

- **H01 — Separa el cálculo analítico de la agenda que lo dispara:** `build_report` es una función pura sobre un `DataFrame` y `professor/test_main.py` la verifica (`{"A": 250, "B": 300}` y sufijo `+00:00`) «sin ejecutar la agenda». La docstring declara que la frecuencia «no debe ocultar el cálculo que automatiza». Sin este hito, la automatización y la lógica quedarían acopladas y la agregación no sería comprobable de forma aislada.
- **H02 — Programa una ejecución periódica y declara el límite de la solución local (caso y datos):** `schedule.every(10).seconds.do(generate_report)` con `run_pending` en un ciclo; `HOW_TO_RUN_ME.txt` afirma que la programación termina con la terminal. El dato es un extracto estático de cuatro filas sin fecha: la periodicidad no se justifica por la llegada de datos nuevos, y cada ejecución reproduce el mismo total. La particularidad del caso, por tanto, no condiciona la cadencia; se registra como límite. Primera aparición de ejecución programada en el curso. Sin este hito, la secuencia no mostraría la diferencia entre ejecutar a demanda y ejecutar por agenda.
- **H03 — Marca cada ejecución con un instante en UTC:** `executed_at` con `datetime.now(timezone.utc)` hace visible en el artefacto cuándo se refrescó la capacidad. El reporte conserva sólo la última marca. Sin este hito, un consumidor no podría distinguir un reporte refrescado de uno antiguo.

### Inventario técnico de implementación

- **Introduce:** biblioteca `schedule`; ciclo `run_pending` con `time.sleep(1)`; marca temporal UTC en el reporte.
- **Reutiliza:** `data/daily_operations.csv` y la agregación por fábrica de P400, P412, P413, P417 y P418; prueba de profesor que carga `main.py` con `importlib`.
- **Aplica en nuevo caso:** ninguno; mismo extracto de operación.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Separación cálculo/agenda | H01 | Función pura `build_report` probada sin agenda | Prueba de profesor; la prueba de actividad sólo exige el archivo. |
| Agenda local | H02 | `schedule.every(10).seconds`, ciclo activo, límite declarado | Cadencia sin justificación por los datos; sin manejo de fallos. |
| Marca de ejecución | H03 | `executed_at` en UTC | Sin historial; se sobrescribe. |

### Relación técnica con actividades anteriores

Misma pregunta y mismo dato que P400, P412, P413, P417 y P418 (totales 9303 y 9300 por fábrica) con un nuevo mecanismo de ejecución. Frente a P413 (Makefile) y P415–P416 (GitHub Actions), que disparan el trabajo por orden explícita o evento, P428 introduce disparo por tiempo. El valor analítico del producto no cambia; la contribución es exclusivamente de modo de ejecución. La reiteración de la misma agregación por fábrica en muchas actividades es una posible duplicación de caso que requiere decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Cálculo separado de la agenda | S02, S04 | `implementation/productos/P428_schedule/professor/main.py`: `build_report`; `implementation/productos/P428_schedule/professor/test_main.py` | La prueba usa datos propios, no el CSV. |
| H02 — Agenda local y su límite | S01, S02 | `implementation/productos/P428_schedule/professor/main.py`: `main`; `implementation/productos/P428_schedule/HOW_TO_RUN_ME.txt`; `implementation/productos/P428_schedule/data/daily_operations.csv` | La agenda no se prueba; cadencia arbitraria. |
| H03 — Marca de ejecución | S03 | `implementation/productos/P428_schedule/submission/scheduled_report.json` | Una sola marca; sin historial. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/daily_operations.csv` | Cuatro filas, sin fecha; idéntico a actividades previas. |
| S02 | Cálculo y agenda | `professor/main.py`; `requirements.txt` | Cadencia fija de 10 s; sin manejo de errores; manifiesto local (`pandas==2.2.3`, `schedule==1.2.2`). |
| S03 | Reporte entregado | `submission/scheduled_report.json` | Se sobrescribe en cada ejecución. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | La agenda no se verifica. |
| S05 | Interfaz del estudiante | `src/main.py`; `HOW_TO_RUN_ME.txt` | Plantilla con `NotImplementedError`. |

### Contrato de evidencia actual

- **Notebook o código:** calcula totales por fábrica con marca UTC y los regenera cada 10 segundos mientras el proceso vive.
- **`submission/`:** `scheduled_report.json` (totales y `executed_at`).
- **Pruebas:** `tests/test_activity.py::test_01` exige que exista el reporte. `professor/test_main.py` verifica la agregación y la zona horaria de la marca. Ninguna verifica la periodicidad ni que hubo más de una ejecución.
- **Trazabilidad:** P428 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P400, P412, P413, P417, P418:** el mismo `daily_operations.csv` (copia) y la agregación por fábrica.
- **Habilita para P429:** el mismo cálculo sobre el mismo archivo, reorganizado como tareas de un flujo; no hay consumo de artefactos.

## Trazabilidad y auditoría

P428 está mapeada a `productos.C02` y `productos.C05` en `implementation/productos/traceability.yaml`. C02 (automatización de una capacidad reproducible) se sostiene en la agenda y en la separación cálculo/agenda. C05 se apoya sólo en la marca `executed_at`; no hay monitoreo, recuperación ni historial. Auditoría de identidad (pregunta 5): la capacidad analítica operada es una suma por fábrica sin usuario ni decisión, y la cadencia no se deriva de ninguna necesidad del uso; el taller puede leerse como entrenamiento en una biblioteca de agendamiento. Riesgo de identidad registrado.
