# P445 — Nivel de servicio: disponibilidad observada frente a una meta

## Actividad actual implementada

**Implementación:** `implementation/productos/P445_service_level/`.

### Preguntas analíticas actuales

- ¿Cumple la operación la meta de servicio acordada según las ejecuciones observadas?

`data/executions.json` contiene tres números: ejecuciones exitosas (18), totales (20) y meta (0.95). `professor/main.py` (`evaluate_service_level`) define la disponibilidad como exitosas/totales y la compara con la meta con `>=`. `submission/service_level.json` registra `availability: 0.9`, `target: 0.95`, `met: false`. No se declara periodo de medición, qué capacidad se ejecuta, quién acordó la meta ni qué consecuencia tiene incumplirla. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decidir si la operación cumple lo acordado (docstring); usuario y acuerdo no evidenciados.
- **Producto terminal:** evaluación de nivel de servicio con indicador, meta y cumplimiento.
- **Uso y límite:** permite declarar incumplimiento con una regla explícita. No identifica la capacidad medida, la ventana temporal ni la acción ante el incumplimiento; con 20 ejecuciones no se expresa incertidumbre del indicador.
- **Disciplinas contribuyentes:** ingeniería de confiabilidad (SLI/SLO) al servicio del contrato operativo de una capacidad no nombrada.

### Highlights de contribución

- **H01 — Define disponibilidad como proporción de ejecuciones exitosas (caso y datos):** la unidad observada es la ejecución de una tarea, no el tiempo en línea de un servicio; el indicador resulta de dos conteos. Esta elección hace del nivel de servicio una propiedad de un proceso por lotes. Límite: el dato no dice de qué tarea ni de qué periodo son las 20 ejecuciones. Sin este hito, «nivel de servicio» quedaría sin indicador operacional.
- **H02 — Compara con meta inclusiva y deja el veredicto persistido:** `met = availability >= target`; la prueba de profesor exige cumplimiento exacto en 99/100 frente a 0.99 e incumplimiento en 0.98. El reporte persistido muestra un incumplimiento (0.9 < 0.95). `tests/test_activity.py` sólo exige existencia. Sin este hito, el borde de la meta quedaría ambiguo.

### Inventario técnico de implementación

- **Introduce:** indicador de nivel de servicio con meta y cumplimiento.
- **Reutiliza:** comparación con umbral declarado (P439, P442) y persistencia JSON.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Indicador de servicio | H01 | Exitosas/totales | Sin ventana ni capacidad identificada. |
| Meta y cumplimiento | H02 | `>=` con borde probado | Sin consecuencia ni incertidumbre. |

### Relación técnica con actividades anteriores

Misma técnica de umbral que P439, P442 y (después) P449, aplicada a un nuevo objeto: la operación de la capacidad y no el dato. No consume ejecuciones registradas por P428 (programación) ni P429 (Prefect); los conteos son propios. Contrato de servicio cercano a `productos.C01`, que nombra «nivel de servicio».

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Disponibilidad por ejecuciones | S01, S02 | `implementation/productos/P445_service_level/data/executions.json`; `implementation/productos/P445_service_level/professor/main.py`: `evaluate_service_level` | No se sabe qué tarea ni qué periodo. |
| H02 — Meta inclusiva | S02, S03, S04 | `implementation/productos/P445_service_level/submission/service_level.json`; `implementation/productos/P445_service_level/professor/test_main.py` | La prueba del estudiante no verifica valores. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Conteos y meta | `data/executions.json` | Tres números; sin periodo. |
| S02 | Evaluación | `professor/main.py` | Un indicador; regla `>=`. |
| S03 | Reporte entregado | `submission/service_level.json` | Sin acción asociada. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: borde; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** calcula disponibilidad y la compara con la meta.
- **`submission/`:** `service_level.json`.
- **Pruebas:** las de profesor verifican borde exacto e incumplimiento; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C04` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P439/P442:** la práctica de evaluar contra umbral declarado; ningún artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P445 mapea `productos.C04` y `productos.C05`. El nivel de servicio forma parte explícita de `productos.C01` («nivel de servicio y criterios de éxito») en `dig/s05-diseno-productos.md`, que no está mapeada; la relación con C04 (uso responsable mediante interfaces, acceso, revisión) no es evidente. Requiere revisión de la entrada. Auditoría pregunta 5: sin capacidad identificada, la actividad puede leerse como cálculo genérico de SLO.
