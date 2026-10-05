# P405 — Logs: registro persistente de una ejecución del cálculo de producción

## Actividad actual implementada

**Implementación:** `implementation/productos/P405_logs/`.

### Preguntas analíticas actuales

- ¿Qué eventos de una ejecución deben quedar registrados para poder explicar después un resultado de producción inesperado o una ejecución interrumpida?

`data/machine_throughput_export.csv` tiene tres filas con el esquema máquina-día de P402. `professor/main.py` configura `logging` hacia `submission/pipeline.log` (nivel INFO, formato `%(asctime)s %(levelname)s %(message)s`, sobrescritura en cada ejecución) y emite cuatro eventos: `pipeline_started`, `input_loaded source=… rows=…`, `production_calculated total_units=…` y `pipeline_completed`. El total es la suma de todas las filas, no un total por fábrica. `submission/pipeline.log` (249 bytes) aparece como binario en el digest; su contenido no es verificable aquí. No hay instrucciones ni prueba del profesor.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** investigar a posteriori una ejecución; usuario no evidenciado.
- **Producto terminal:** `submission/pipeline.log`, rastro de eventos de una ejecución.
- **Uso y límite:** permite distinguir una ejecución completa de una interrumpida y conocer fuente y volumen leídos. No registra advertencias ni errores, no captura excepciones y no conserva historial entre ejecuciones (`filemode="w"`).
- **Disciplinas contribuyentes:** instrumentación de software con `logging` al servicio de la observabilidad de un cálculo.

### Highlights de contribución

- **H01 — Instrumenta el ciclo de vida de una ejecución con eventos clave=valor:** eventos de inicio y fin delimitan la ejecución («distinguir una ejecución completa de una interrumpida»); el evento de carga registra `source` y `rows` porque «ayudan a explicar un resultado inesperado»; el del cálculo, `total_units`. `force=True` reemplaza cualquier configuración previa del registro. Primera práctica de observabilidad del curso. Sin este hito, el resultado no tendría rastro de cómo se produjo.
- **H02 — Registra volumen y fuente de un insumo sin particularidad propia (caso y datos, límite):** el dato es un subconjunto de tres filas del extracto de P402; los únicos hechos del caso que entran al log son nombre de archivo, número de filas y suma total. No se registra la decisión de aceptación de P402 ni se valida el insumo; la granularidad máquina-día no cambia lo que se registra. Sin este hito no se vería qué parte del caso se considera evidencia operativa; con él queda visible que el caso es intercambiable.

### Inventario técnico de implementación

- **Introduce:** `logging.basicConfig` con archivo, nivel, formato y `force=True`; mensajes con formato diferido (`%s`); eventos de inicio, carga, cálculo y fin.
- **Reutiliza:** esquema máquina-día de P402.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Log de ejecución | H01 | Cuatro eventos INFO con marca de tiempo | Sin WARNING/ERROR ni excepciones. |
| Métricas de volumen | H01, H02 | `rows` y `total_units` en el log | Sin umbrales ni alertas. |

### Relación técnica con actividades anteriores

Nueva práctica (registro de eventos) sobre el esquema de P402. No reutiliza la validación ni las funciones aisladas de P400–P402: todo ocurre en `main`. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Ciclo de vida | S02, S03 | `implementation/productos/P405_logs/professor/main.py`: `main`; `implementation/productos/P405_logs/submission/pipeline.log` | Contenido del log no visible en el digest. |
| H02 — Insumo sin particularidad | S01, S02 | `implementation/productos/P405_logs/data/machine_throughput_export.csv` | Tres filas; procedencia no documentada. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/machine_throughput_export.csv` | Tres filas. |
| S02 | Instrumentación | `professor/main.py` | Cuatro eventos INFO; sobrescribe el log. |
| S03 | Producto | `submission/pipeline.log` | Un archivo de una ejecución. |
| S04 | Prueba | `tests/test_activity.py` | Sólo existencia; no ejecuta código. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe emitir los cuatro eventos en un archivo persistente.
- **`submission/`:** `pipeline.log`.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista el log; no verifica eventos, orden ni formato. Según `structure-audit.md`, la prueba requiere ejecutar antes `professor/main.py`. No hay prueba del profesor.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P402:** filas iniciales del extracto máquina-día (sin reutilizar su validación).
- **Habilita para Pyyy:** no evidenciada dentro de P406–P413.

## Trazabilidad y auditoría

Entrada revisada: P405 → `productos.C02`, `productos.C05`. C05 se sostiene mínimamente (rastro observable de una ejecución); C02 débilmente. El producto de Analytics es un rastro de ejecución de una suma sin usuario declarado; el taller se lee como introducción a `logging` (pregunta de auditoría 5), sin vínculo con una decisión o con la validación previa.
