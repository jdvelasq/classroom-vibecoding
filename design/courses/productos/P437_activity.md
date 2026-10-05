# P437 — Late arriving data: clasificación de un registro tardío para reproceso

## Actividad actual implementada

**Implementación:** `implementation/productos/P437_late_arriving_data/`.

### Preguntas analíticas actuales

- ¿Un registro que llega hoy pertenece a un período ya procesado y exige un reproceso histórico, o puede cargarse con la ejecución actual?

`data/arrival.json` describe un registro con `event_date` 2026-09-20, `arrival_date` 2026-09-24 y `current_processing_date` 2026-09-24. `professor/main.py` define `classify_arrival`, que marca `late` si `event_date < current_processing_date` y asigna la acción `backfill` o `current_load`. `submission/arrival_classification.json` registra `{"late": true, "action": "backfill"}`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decidir entre reproceso histórico y carga actual; el responsable no se identifica.
- **Producto terminal:** `submission/arrival_classification.json`, clasificación y acción para un registro.
- **Uso y límite:** muestra que la fecha del evento y la de procesamiento son distintas y que esa diferencia dirige la acción. `arrival_date` se lee pero no interviene en la regla; cualquier evento con fecha anterior a la de procesamiento se trata como tardío, sin tolerancia ni ventana; la comparación es de cadenas ISO. El reproceso no se ejecuta.
- **Disciplinas contribuyentes:** manejo de datos tardíos en pipelines temporales.

### Highlights de contribución

- **H01 — Separa la fecha del evento de la fecha de procesamiento (caso y datos):** el registro tiene tres fechas y la docstring declara que «separar la fecha del evento de su llegada evita perder correcciones históricas». La regla usa `event_date` frente a `current_processing_date`. Esta particularidad temporal impide tratar el registro como una fila más de la carga del día. Límite: `arrival_date` no participa, de modo que la noción de «llegada tardía» se reduce a «evento pasado». Sin este hito, un registro de un período cerrado se mezclaría con el período actual.
- **H02 — Deriva una acción operativa de la clasificación:** `action` toma `backfill` o `current_load`; la prueba de profesor verifica ambos casos. Primera aparición de una decisión de reproceso en el curso; contrasta con P436, que sólo procesa eventos posteriores a la marca. Sin este hito, el registro tardío sería descartado o mal asignado sin señal.

### Inventario técnico de implementación

- **Introduce:** distinción `event_date`/`current_processing_date`; clasificación binaria con acción.
- **Reutiliza:** patrón de función con entrada inyectable y lectura por defecto desde `data/`.
- **Aplica en nuevo caso:** un registro con fechas, sin contenido analítico.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Tiempo de evento frente a procesamiento | H01 | Comparación de fechas | `arrival_date` sin uso; sin ventana de tolerancia. |
| Acción de reproceso | H02 | `backfill`/`current_load` | Reproceso no ejecutado. |

### Relación técnica con actividades anteriores

Caso complementario de P436: P436 procesa lo posterior a una marca; P437 decide qué hacer con lo anterior. No comparten artefactos. P438 selecciona un rango para reproceso, pero no consume la clasificación de P437; la fecha del evento (2026-09-20) cae dentro del rango persistido por P438, coincidencia no conectada en el código.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Evento frente a procesamiento | S01, S02 | `implementation/productos/P437_late_arriving_data/data/arrival.json`; `implementation/productos/P437_late_arriving_data/professor/main.py`: `classify_arrival` | `arrival_date` no interviene. |
| H02 — Acción operativa | S02, S03, S04 | `implementation/productos/P437_late_arriving_data/professor/test_main.py`; `implementation/productos/P437_late_arriving_data/submission/arrival_classification.json` | Un solo registro. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Registro de llegada | `data/arrival.json` | Un registro; tres fechas. |
| S02 | Regla de clasificación | `professor/main.py` | Usa dos de tres fechas. |
| S03 | Clasificación entregada | `submission/arrival_classification.json` | Sin identificador de registro. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** clasifica el registro y guarda la acción.
- **`submission/`:** `arrival_classification.json`.
- **Pruebas:** `test_01` exige el archivo; las pruebas de profesor verifican `backfill` para un evento anterior y `current_load` para uno del mismo día. No verifican el uso de `arrival_date`.
- **Trazabilidad:** P437 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P436:** contraste conceptual (procesamiento por tiempo); sin artefacto.
- **Habilita para P438:** la acción `backfill` motiva la selección de rango de P438; sin consumo de artefactos.

## Trazabilidad y auditoría

P437 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en la integración correcta de registros tardíos; C05 (corrección/recuperación) en la decisión de reproceso. Auditoría de identidad (pregunta 5): no hay medida ni indicador cuyo valor histórico cambie con el reproceso; el taller se lee como patrón genérico de ingeniería de datos. Riesgo de identidad registrado.
