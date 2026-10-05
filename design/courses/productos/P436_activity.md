# P436 — Watermark: procesamiento incremental desde una marca de agua

## Actividad actual implementada

**Implementación:** `implementation/productos/P436_watermark/`.

### Preguntas analíticas actuales

- ¿Qué eventos deben procesarse en esta ejecución para no reprocesar todo el historial, y hasta qué instante queda procesado el flujo después?

`data/events.json` tiene dos eventos con `id` y `timestamp` (2026-09-20T10:00Z y 2026-09-24T10:00Z); `data/watermark.json` declara `last_processed` = 2026-09-21T00:00Z. `professor/main.py` define `process_new_events`, que conserva los eventos con `timestamp` posterior a la marca y calcula la nueva marca como el máximo procesado (o mantiene la anterior si no hay eventos). `submission/watermark_result.json` registra `processed_ids: [2]` y `new_watermark: 2026-09-24T10:00:00Z`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/watermark_result.json`, selección incremental y nueva marca.
- **Uso y límite:** muestra cómo una marca persistente delimita lo nuevo. La nueva marca no se escribe de vuelta en `data/watermark.json`, de modo que una segunda ejecución reprocesaría el evento 2; los eventos no tienen contenido analítico (sólo `id` y `timestamp`) y no se agrega ni calcula nada con ellos. La comparación es lexicográfica sobre cadenas ISO 8601, válida sólo si todas comparten formato y zona.
- **Disciplinas contribuyentes:** carga incremental en ingeniería de datos.

### Highlights de contribución

- **H01 — Delimita el procesamiento incremental con una marca de agua y la avanza:** filtro `event["timestamp"] > watermark` y nueva marca `max(...)`. La prueba de profesor exige que se procesen sólo los dos eventos posteriores, que la marca avance al último y que sin eventos nuevos la marca se conserve. Primera aparición de procesamiento incremental en el curso; contrasta con P428–P433, que recalculan todo el extracto en cada ejecución. Sin este hito, la secuencia no mostraría cómo reanudar un flujo sin reprocesar el historial.
- **H02 — Caso y datos: el instante del evento define el estado del flujo:** el dato relevante no es el contenido sino el `timestamp`; la marca convierte el tiempo de los eventos en estado persistente del proceso. El caso no tiene entidad ni medida analítica y la marca no se persiste para la siguiente corrida; ambas ausencias se registran como límites.

### Inventario técnico de implementación

- **Introduce:** marca de agua persistida en JSON; filtro incremental; avance de marca con caso vacío.
- **Reutiliza:** patrón de función con entradas inyectables y lectura por defecto desde `data/`.
- **Aplica en nuevo caso:** eventos con marca temporal (sin contenido).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Marca de agua | H01, H02 | Filtro `>` y avance al máximo | No se reescribe la marca; comparación de cadenas. |
| Caso vacío | H01 | Marca conservada sin eventos nuevos | Probado en profesor. |

### Relación técnica con actividades anteriores

Nuevo mecanismo de ejecución frente a la recomputación completa de P428–P433 y frente a la idempotencia por existencia de P430: aquí el estado es un instante, no un archivo. No comparte dato con actividades previas. Sus fechas (2026-09-20, 2026-09-24) coinciden con las de P437–P439, sin artefacto común.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Incremental con marca | S02, S04 | `implementation/productos/P436_watermark/professor/main.py`: `process_new_events`; `implementation/productos/P436_watermark/professor/test_main.py`; `implementation/productos/P436_watermark/submission/watermark_result.json` | Marca no persistida en la fuente. |
| H02 — Tiempo como estado | S01, S03 | `implementation/productos/P436_watermark/data/events.json`; `implementation/productos/P436_watermark/data/watermark.json` | Eventos sin contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Eventos y marca | `data/events.json`; `data/watermark.json` | Dos eventos sin medida. |
| S02 | Selección incremental | `professor/main.py` | Comparación de cadenas; sin escritura de la marca. |
| S03 | Resultado | `submission/watermark_result.json` | Selección y marca nueva. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** selecciona los eventos posteriores a la marca y calcula la nueva marca.
- **`submission/`:** `watermark_result.json`.
- **Pruebas:** `test_01` exige el archivo; las dos pruebas de profesor verifican avance y conservación de la marca. No verifican una segunda ejecución ni la persistencia de la marca.
- **Trazabilidad:** P436 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna demostrable.
- **Habilita para P437:** no evidenciada como artefacto; P437 trata el caso complementario (evento anterior al procesamiento) con datos propios.

## Trazabilidad y auditoría

P436 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en la carga incremental; C05 (recuperación/reanudación) parcialmente, dado que la marca no se persiste. Auditoría de identidad (pregunta 5): sin entidad, medida ni capacidad analítica asociada, el taller se lee como patrón genérico de ingeniería de datos. Riesgo de identidad registrado.
