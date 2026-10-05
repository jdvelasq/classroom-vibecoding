# P442 — Observabilidad de datos: reporte integrado de frescura, volumen y esquema

## Actividad actual implementada

**Implementación:** `implementation/productos/P442_data_observability/`.

### Preguntas analíticas actuales

- ¿Está sano, en conjunto, el insumo de datos según sus señales de frescura, volumen y esquema?

`data/signals.json` es un único objeto con cinco campos: edad del dato (`age_days: 2`) y su máximo (`maximum_age_days: 1`), filas recibidas (`rows: 80`) y su mínimo (`minimum_rows: 100`), y un booleano `schema_valid: true`. `professor/main.py` (`build_observability_report`) evalúa tres comprobaciones y declara `healthy` sólo si todas se cumplen. `submission/observability_report.json` registra `freshness: false`, `volume: false`, `schema: true` y `healthy: false`. No hay dataset subyacente: las señales llegan ya resumidas y no se nombra qué conjunto de datos ni qué capacidad analítica observan. El estudiante recibe `src/main.py` con `raise NotImplementedError`, sin `HOW_TO_RUN_ME.txt` y con `notebooks/` vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** priorizar la operación con una vista integrada (docstring de `build_observability_report`); usuario y decisión concreta no evidenciados.
- **Producto terminal:** reporte JSON con tres comprobaciones y un veredicto de salud.
- **Uso y límite:** permite ver de una vez qué contrato de señal falla. No calcula las señales (edad, filas y validez de esquema llegan dadas), no conserva historia ni tendencia y no indica qué acción tomar ni a qué producto afecta.
- **Disciplinas contribuyentes:** Data Engineering (observabilidad de datos) al servicio de la confiabilidad del insumo de una capacidad no nombrada.

### Highlights de contribución

- **H01 — Declara cada señal junto a su umbral (caso y datos):** el insumo no es una tabla sino un registro de señales donde cada medida viaja con su límite (`age_days`/`maximum_age_days`, `rows`/`minimum_rows`); el esquema llega como booleano ya evaluado. Esa forma obliga a tratar la observabilidad como comparación contra contratos declarados y no como inspección de filas. Límite: no hay particularidad del dato analítico observado; las señales no remiten a ningún dataset del curso. Sin este hito no quedaría explícito que cada señal tiene un contrato propio.
- **H02 — Integra señales heterogéneas en un veredicto único:** `healthy = all(checks.values())` combina frescura (ya tratada aislada en P439), volumen y esquema. El reporte persistido muestra dos fallas simultáneas con esquema válido, lo que hace visible que una señal sana no basta. Extiende P439–P441, que evalúan una sola condición cada una. Sin este hito, la secuencia terminaría en controles aislados sin vista conjunta.
- **H03 — Fija la inclusividad de los umbrales en pruebas:** `professor/test_main.py` comprueba que `age_days == maximum_age_days` y `rows == minimum_rows` se consideran sanos, y que un esquema inválido basta para `healthy: false`. `tests/test_activity.py` sólo exige que exista el reporte. Sin este hito, el borde de cada contrato quedaría implícito.

### Inventario técnico de implementación

- **Introduce:** reporte de observabilidad con varias comprobaciones nombradas y veredicto agregado.
- **Extiende:** la comparación edad/umbral de P439 a un conjunto de señales.
- **Reutiliza:** patrón función pura + `main()` que persiste JSON en `submission/`, y pruebas de profesor con entradas inyectadas (P439–P441).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Señal con contrato | H01 | Medida y umbral en el mismo registro | Señales dadas; no se calculan desde datos. |
| Salud integrada | H02 | `all()` sobre frescura, volumen y esquema | Sin ponderación, historia ni severidad. |
| Bordes del contrato | H03 | Pruebas de umbral inclusivo y esquema roto | La prueba de actividad sólo verifica existencia. |

### Relación técnica con actividades anteriores

Misma técnica (comparación con umbral) que P439 (frescura), P440 (conciliación) y P441 (cuarentena), con nueva exigencia de producto: un veredicto conjunto. Los valores de frescura no coinciden con P439 (`age_days` 2 aquí, 4 en `P439/submission/freshness_report.json`) y no se consume ningún artefacto previo. Posible solapamiento con P439 en la comprobación de frescura; requiere decisión posterior de curso. `dig/structure-audit.md` registra que la solución de P442 se trasladó de `scripts/` a `professor/`.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Señal con umbral | S01, S02 | `implementation/productos/P442_data_observability/data/signals.json`; `implementation/productos/P442_data_observability/professor/main.py`: `build_observability_report` | No se sabe qué dataset ni qué capacidad se observa. |
| H02 — Veredicto integrado | S02, S03 | `implementation/productos/P442_data_observability/professor/main.py`; `implementation/productos/P442_data_observability/submission/observability_report.json` | Un solo instante; sin acción asociada. |
| H03 — Bordes en pruebas | S04 | `implementation/productos/P442_data_observability/professor/test_main.py`; `implementation/productos/P442_data_observability/tests/test_activity.py` | La prueba del estudiante no verifica contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Señales de entrada | `data/signals.json` | Cinco campos dados; esquema como booleano. |
| S02 | Evaluación | `professor/main.py` | Tres comprobaciones fijas; `all()` como regla. |
| S03 | Reporte entregado | `submission/observability_report.json` | Un instante; sin historia. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: bordes; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** `build_observability_report` evalúa frescura, volumen y esquema y calcula `healthy`; `main()` persiste el reporte.
- **`submission/`:** `observability_report.json` con tres comprobaciones y veredicto.
- **Pruebas:** las de profesor verifican umbrales inclusivos y que un esquema inválido vuelve no sano el reporte; `test_01` sólo verifica que el archivo exista.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P439:** la práctica de comparar edad del dato con un máximo; no recibe artefactos.
- **Habilita para P446:** no evidenciada como artefacto; P446 trata una alerta de frescura sin consumir este reporte.

## Trazabilidad y auditoría

P442 mapea `productos.C02` y `productos.C05`. C05 (observar) se sostiene en el reporte integrado; C02 sólo por la función persistida. El reporte no observa una capacidad analítica identificable: las señales no remiten a la tabla de fábricas ni a otro producto del curso. Auditoría pregunta 5: la actividad puede leerse como observabilidad genérica de datos; falta conectar las señales con el producto cuya confiabilidad protegen.
