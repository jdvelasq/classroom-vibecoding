# P526 — Eventos de comercio electrónico: llegada tardía y conversión por sesión

## Actividad actual implementada

**Implementación:** `implementation/data/P526_eventos/`.

### Preguntas analíticas actuales

- ¿Cuántas sesiones convierten y qué ingreso representan sin confundir el orden de llegada con el comportamiento real?

La pregunta es un comentario al inicio de `professor/main.py` (no hay notebook de profesor). `data/events.csv.gz` (2171 bytes) contiene 112 eventos con `event_time` (texto UTC, 2019-12-01 en las filas visibles), `event_type` (`view`, `cart`, `purchase`…), producto, categoría (`category_code` vacío en las filas visibles), marca, `price`, `user_id` y `user_session`. La procedencia no se documenta en la actividad. `replay_arrivals` simula llegada desordenada moviendo los dos primeros eventos de cada bloque de ocho al final del bloque; `mark_late_events` marca como tardío el evento cuyo `event_time` es anterior al máximo ya visto; `summarize_sessions` agrega por sesión. Persiste `submission/event_replay.csv` (112 eventos con `arrival_position` e `is_late`), `submission/session_conversion.csv` (16 sesiones) y `submission/event_summary.csv` (112 eventos, 28 tardíos, 16 sesiones, 8 convertidas, tasa 0.5). `src/main.py` levanta `NotImplementedError`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta declarada; usuario y decisión no evidenciados.
- **Producto terminal:** tabla de conversión e ingreso por sesión y resumen de métricas, acompañados de la reproducción de llegadas con marca de tardanza.
- **Uso y límite:** define conversión e ingreso al grano sesión y deja rastro de qué eventos llegaron tarde. La tasa 0.5 describe 16 sesiones de una muestra cuyo criterio de selección no se documenta; no permite inferir conversión de una población. El desorden es simulado: los 28 tardíos resultan de la regla de reordenamiento (14 bloques × 2), no de llegadas observadas. Como la agregación por sesión no depende del orden, las métricas no cambian con la llegada tardía y el código no contrasta con un cálculo que sí dependa del orden de llegada (por ejemplo, una ventana cerrada por tiempo de procesamiento); la «confusión» que la pregunta menciona no se muestra.
- **Disciplinas contribuyentes:** procesamiento de eventos (tiempo de evento frente a orden de llegada) al servicio de una métrica de conversión.

### Highlights de contribución

- **H01 — Separa tiempo de evento y orden de llegada en cada registro (caso y datos):** los eventos tienen marca temporal propia y pueden llegar desordenados; `mark_late_events` añade `arrival_position` y calcula `is_late = event_time < latest_event_time` con un máximo acumulado. La comparación textual es válida porque `event_time` tiene formato fijo `YYYY-MM-DD HH:MM:SS UTC`. `event_replay.csv` persiste ambas dimensiones. Primera aparición en el curso de la distinción entre tiempo de evento y tiempo de procesamiento. Sin este hito, el curso trataría el orden de un archivo como el orden de los hechos.
- **H02 — Simula de forma determinista y declarada la llegada tardía sobre eventos dados:** `replay_arrivals` reordena cada bloque de ocho (`batch[2:] + batch[:2]`) con el comentario «Una fuente distribuida puede entregar una parte antigua después del resto del lote». La simulación es reproducible y su efecto es exactamente 28 tardíos. La marca supone que el archivo de origen está ordenado por `event_time`, lo que no se verifica. Sin este hito, no habría tardanza que marcar con estos datos.
- **H03 — Define conversión e ingreso al grano sesión y los persiste con su resumen:** `summarize_sessions` cuenta eventos y tardíos por `user_session`, suma `price` de los eventos `purchase` y define `converted = revenue > 0`; `event_summary.csv` deriva la tasa de conversión. La definición supone una unidad por evento de compra (no hay columna de cantidad) y trataría como no convertida una compra de precio cero. Sin este hito, la métrica de conversión quedaría implícita.

### Inventario técnico de implementación

- **Introduce:** marca de tardanza por máximo acumulado de tiempo de evento; simulación determinista de desorden; agregación por sesión con `defaultdict`; métrica de conversión y tasa.
- **Reutiliza:** lectura de CSV comprimido con `gzip` (P522); agregación por clave (idea de P519–P520, sin sus operadores).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Tiempo de evento vs. llegada | H01 | `arrival_position`, `is_late` en `event_replay.csv` | Sin marca de agua ni tolerancia de tardanza. |
| Desorden simulado | H02 | Rotación de dos eventos por bloque de ocho | Tardanza construida, no observada. |
| Conversión por sesión | H03 | `session_conversion.csv`; `event_summary.csv` | 16 sesiones; selección de muestra no documentada; métricas invariantes al orden. |

### Relación técnica con actividades anteriores

Nuevo caso y nueva particularidad (tiempo de evento) con una pregunta analítica explícita, la única del tramo P522–P526. Reutiliza la agregación por clave del bloque MapReduce sin sus operadores. Aporta un dominio distinto de Superstore, Scopus, Vermont y conductores. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Tiempo de evento vs. llegada | S01, S02, S04 | `implementation/data/P526_eventos/professor/main.py`: `mark_late_events`; `implementation/data/P526_eventos/submission/event_replay.csv` | Orden de origen supuesto. |
| H02 — Desorden simulado | S02 | `implementation/data/P526_eventos/professor/main.py`: `replay_arrivals`; `implementation/data/P526_eventos/submission/event_summary.csv` | No describe una fuente real. |
| H03 — Conversión por sesión | S03, S04 | `implementation/data/P526_eventos/professor/main.py`: `summarize_sessions`, `main`; `implementation/data/P526_eventos/submission/session_conversion.csv`; `implementation/data/P526_eventos/submission/event_summary.csv` | Sin inferencia poblacional. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/events.csv.gz` | 112 eventos; identificadores de usuario y sesión; sin procedencia ni restricción documentadas. |
| S02 | Simulación y marca de tardanza | `professor/main.py`: `replay_arrivals`, `mark_late_events` | Bloques de ocho fijos. |
| S03 | Métrica de conversión | `professor/main.py`: `summarize_sessions` | `revenue > 0` como conversión. |
| S04 | Producto | `submission/event_replay.csv`; `submission/session_conversion.csv`; `submission/event_summary.csv` | `event_replay.csv` copia `user_id` y `user_session`. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia. |
| S06 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin notebook. |

### Contrato de evidencia actual

- **Notebook o código:** debe reordenar llegadas, marcar tardíos, agregar por sesión y escribir tres archivos.
- **`submission/`:** reproducción de 112 eventos, 16 sesiones y cinco métricas de resumen.
- **Pruebas:** `test_01_submission_contains_event_analysis` sólo verifica que existan los tres archivos.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** práctica de agregación por clave (P519–P520) y lectura `gzip` (P522), sin archivo compartido.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P526 → `data.C01`–`data.C05`. `data.C01` se sostiene (pregunta → grano sesión y definición de conversión); `data.C03` por la marca de tardanza; `data.C04` por la reproducción persistida. La sensibilidad de `user_id`/`user_session` no está documentada en la implementación (`dig/case-selection.md` menciona una muestra privada, como contexto). Auditoría: es el taller del tramo final con producto analítico más claro (métrica de conversión con definición explícita); el procesamiento de eventos sirve a esa métrica. El límite es que la amenaza analítica que motiva la pregunta no se demuestra.
