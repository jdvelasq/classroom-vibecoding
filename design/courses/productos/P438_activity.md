# P438 — Backfill: selección de un período histórico explícito para reprocesar

## Actividad actual implementada

**Implementación:** `implementation/productos/P438_backfill/`.

### Preguntas analíticas actuales

- ¿Qué eventos entran en un reproceso histórico declarado por rango de fechas, sin afectar períodos vecinos?

`data/events.json` tiene tres eventos con `id` y `date` (2026-09-20, 2026-09-21, 2026-09-24). `professor/main.py` define `select_backfill(start_date, end_date, events)`, que conserva los identificadores con fecha dentro del rango inclusivo. `main` fija el rango 2026-09-20 a 2026-09-21 y persiste `submission/backfill_selection.json` con el rango y `event_ids: [1, 2]`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** delimitar un reproceso; responsable y motivo no evidenciados.
- **Producto terminal:** `submission/backfill_selection.json`, rango declarado y eventos seleccionados.
- **Uso y límite:** muestra que un reproceso se acota y registra antes de ejecutarse. No se reprocesa nada: no hay cálculo que se rehaga ni resultado que se reemplace; el rango está fijo en el código; los eventos no tienen contenido.
- **Disciplinas contribuyentes:** reproceso histórico (backfill) en pipelines.

### Highlights de contribución

- **H01 — Acota el reproceso a un rango inclusivo declarado:** filtro `start_date <= date <= end_date`; la prueba de profesor exige incluir los extremos y excluir los días anterior y posterior, y su docstring declara que el rango «evita que un reproceso correctivo altere fechas vecinas». Continúa P437, que decide *cuándo* reprocesar, con *qué* reprocesar. Sin este hito, el reproceso histórico no tendría alcance explícito.
- **H02 — Registra el alcance junto con la selección (caso y datos como límite):** el artefacto conserva `start_date`, `end_date` y los identificadores, de modo que el reproceso es auditable. Los eventos sólo tienen fecha; no hay indicador cuyo valor cambie al reprocesar, y la relación con el registro tardío de P437 no está en el código. La particularidad del caso se limita al orden temporal; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** selección por rango inclusivo de fechas; registro del alcance del reproceso.
- **Reutiliza:** patrón de función con entrada inyectable.
- **Aplica en nuevo caso:** eventos fechados sin contenido.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Rango de reproceso | H01 | Filtro inclusivo por fecha | Comparación de cadenas; rango fijo. |
| Registro del alcance | H02 | Rango + ids persistidos | Sin ejecución del reproceso. |

### Relación técnica con actividades anteriores

Secuencia temática P436 (incremental) → P437 (tardío) → P438 (rango de reproceso), cada una con datos propios y sin artefactos compartidos. P438 no reutiliza la idempotencia de P430, que sería relevante al reprocesar; la relación queda no evidenciada.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Rango inclusivo | S02, S04 | `implementation/productos/P438_backfill/professor/main.py`: `select_backfill`; `implementation/productos/P438_backfill/professor/test_main.py` | Sin reproceso efectivo. |
| H02 — Alcance registrado | S01, S03 | `implementation/productos/P438_backfill/data/events.json`; `implementation/productos/P438_backfill/submission/backfill_selection.json` | Eventos sin contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Eventos | `data/events.json` | Tres eventos con fecha. |
| S02 | Selección | `professor/main.py` | Rango literal en `main`. |
| S03 | Registro del reproceso | `submission/backfill_selection.json` | Selección, no resultado reprocesado. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** selecciona eventos del rango y registra rango y selección.
- **`submission/`:** `backfill_selection.json`.
- **Pruebas:** `test_01` exige el archivo; la prueba de profesor verifica la inclusividad del rango. No verifican un reproceso.
- **Trazabilidad:** P438 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P437:** la acción `backfill` como motivo conceptual; sin artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P438 está mapeada a `productos.C02` y `productos.C05`. C05 (recuperación) se sostiene en un reproceso acotado y registrado; C02 parcialmente. Auditoría de identidad (pregunta 5): sin capacidad analítica que se corrija, el taller se lee como patrón genérico de ingeniería de datos. Riesgo de identidad registrado; P436–P438 son candidatas a decisión de combinación.
