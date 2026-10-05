# P439 — Data freshness: alerta por antigüedad de la fuente

## Actividad actual implementada

**Implementación:** `implementation/productos/P439_data_freshness/`.

### Preguntas analíticas actuales

- ¿Los datos de la fuente son suficientemente recientes para usarse en una decisión operativa, según una antigüedad máxima declarada?

`data/source_status.json` declara `data_as_of` 2026-09-20, `checked_at` 2026-09-24 y `maximum_age_days` 1. `professor/main.py` define `assess_freshness`, que calcula la antigüedad en días con `date.fromisoformat` y alerta si supera el máximo. `submission/freshness_report.json` registra `{"age_days": 4, "maximum_age_days": 1, "alert": true}`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** la docstring del módulo habla de «una decisión operativa», no identificada.
- **Producto terminal:** `submission/freshness_report.json`, señal de frescura con umbral.
- **Uso y límite:** permite advertir que una capacidad se alimenta de datos vencidos. El umbral de 1 día no se justifica por un uso; la alerta no bloquea ni cambia ninguna salida; la fuente es un estado declarado, no metadatos leídos de un archivo real.
- **Disciplinas contribuyentes:** monitoreo de calidad de datos (frescura).

### Highlights de contribución

- **H01 — Convierte la antigüedad de la fuente en una alerta con umbral explícito:** diferencia de fechas con `date.fromisoformat` (no comparación de cadenas, a diferencia de P436–P438) y `alert = age > maximum_age_days`. La prueba de profesor exige que la antigüedad igual al límite no alerte y que la superior sí. Primera señal de calidad de datos de entrada con umbral temporal; sigue el patrón umbral–alerta de P422 y P423 (deriva y desempeño), ahora sobre la fuente. Sin este hito, una capacidad podría publicar resultados con datos vencidos sin advertencia.
- **H02 — Caso y datos (límite):** la frescura depende de dos fechas declaradas en un JSON; no hay fuente de datos real cuya fecha se lea ni capacidad que consuma la alerta. El umbral (1 día) se distingue del usado en la prueba (3 días) sin razón documentada. La implementación no revela una particularidad del caso que fije el umbral; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** cálculo de antigüedad en días; umbral de frescura con límite inclusivo.
- **Reutiliza:** patrón umbral → `alert` de P422–P423.
- **Aplica en nuevo caso:** estado de una fuente.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Frescura con umbral | H01 | `age_days > maximum_age_days` | Umbral sin justificación de uso. |
| Estado de la fuente | H02 | JSON con fechas declaradas | Sin fuente real ni consumidor. |

### Relación técnica con actividades anteriores

Misma técnica (umbral y alerta) de P422 y P423 con nueva exigencia: vigilar la entrada por tiempo, no por distribución ni por desempeño. Frente a P436–P438, introduce aritmética de fechas real. No comparte artefactos con actividades previas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Alerta de frescura | S02, S04 | `implementation/productos/P439_data_freshness/professor/main.py`: `assess_freshness`; `implementation/productos/P439_data_freshness/professor/test_main.py`; `implementation/productos/P439_data_freshness/submission/freshness_report.json` | Alerta sin efecto. |
| H02 — Caso como límite | S01 | `implementation/productos/P439_data_freshness/data/source_status.json` | Fechas declaradas. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Estado de la fuente | `data/source_status.json` | Fechas y umbral declarados. |
| S02 | Evaluación | `professor/main.py` | Umbral leído del dato; sin acción. |
| S03 | Reporte | `submission/freshness_report.json` | Tres campos. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** calcula antigüedad y alerta, y guarda el reporte.
- **`submission/`:** `freshness_report.json`.
- **Pruebas:** `test_01` exige el archivo; las pruebas de profesor verifican el límite inclusivo y la alerta. No verifican el contenido entregado.
- **Trazabilidad:** P439 mapea `productos.C02`, `productos.C03` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P422, P423:** el patrón umbral–alerta; sin artefacto.
- **Habilita para P442:** P442 reutiliza los campos `age_days` y `maximum_age_days` como señal `freshness` dentro de un reporte de observabilidad integrado (con datos propios).

## Trazabilidad y auditoría

P439 está mapeada a `productos.C02`, `C03` y `C05`. C03 (validar datos frente al uso operativo) y C05 (monitoreo) se sostienen en la alerta; el «uso operativo» no está especificado. C02 tiene sustento débil. Auditoría de identidad (pregunta 5): la práctica es pertinente para una capacidad analítica, pero sin fuente ni consumidor identificados es un patrón genérico de calidad de datos; riesgo moderado.
