# P430 — Idempotency: reporte diario que no se duplica al reejecutar

## Actividad actual implementada

**Implementación:** `implementation/productos/P430_idempotency/`.

### Preguntas analíticas actuales

- ¿Cómo evitar que reintentar una tarea diaria produzca una segunda versión del mismo resultado?

`professor/main.py` define `generate_daily_report`, que construye un reporte literal `{"report_date": "2026-09-24", "factory_id": 2, "risk": "high"}`; si `submission/daily_report.json` ya existe, devuelve su contenido sin reescribirlo, y si no existe lo escribe. No hay `data/` sustantivo ni `HOW_TO_RUN_ME.txt`. El reporte persistido coincide con el literal.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; el reporte nombra un riesgo de fábrica sin decisión asociada.
- **Producto terminal:** `submission/daily_report.json`, un registro diario de riesgo por fábrica escrito una sola vez.
- **Uso y límite:** muestra el patrón «si el resultado existe, reutilízalo». El riesgo no se calcula: es un literal. La «clave estable» que menciona la docstring no se usa: la identidad del resultado es la ruta del archivo, no `report_date`, de modo que un reporte de otro día en la misma ruta también se reutilizaría.
- **Disciplinas contribuyentes:** diseño de tareas reejecutables (idempotencia) en pipelines.

### Highlights de contribución

- **H01 — Convierte una reejecución en reutilización del resultado persistido:** `generate_daily_report` consulta `OUTPUT_PATH.exists()` antes de escribir. `professor/test_main.py` sobrescribe el archivo tras la primera llamada y comprueba que la segunda devuelve el contenido sobrescrito (`risk: low`) y no recalcula (`risk: high`). Primera aparición de idempotencia en el curso; complementa el reintento declarado en P429. Sin este hito, reintentar podría duplicar o alterar un resultado ya publicado.
- **H02 — Caso y datos (límite):** el resultado es un literal sin dato de origen; la fecha `2026-09-24` y el riesgo `high` para la fábrica 2 no se derivan de ningún archivo. Con la regla de P425 (`high` si `daily_units_produced < 4500`), las máquinas de la fábrica 2 en `daily_operations.csv` (4700 y 4600) serían `low`; la implementación no conecta ambos. No hay particularidad del dato que condicione la clave de idempotencia; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** comprobación de existencia antes de escribir como mecanismo de idempotencia; prueba con `monkeypatch` de la ruta de salida y `tmp_path`.
- **Reutiliza:** vocabulario `factory_id`/`risk` de P425–P426.
- **Aplica en nuevo caso:** reporte diario de riesgo (literal).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Idempotencia por existencia | H01 | `OUTPUT_PATH.exists()` y retorno del persistido | Clave = ruta, no fecha; sin escritura atómica. |
| Reporte diario | H02 | Registro de riesgo con fecha | Literal, no calculado. |

### Relación técnica con actividades anteriores

Nuevo mecanismo al servicio de la confiabilidad de ejecución: P428 sobrescribe en cada corrida y P429 declara reintentos; P430 muestra cómo un reintento no altera lo publicado. No hay dato compartido con P428–P429. El riesgo `high` de la fábrica 2 reaparece en P435, P450 y P451 sin cálculo que lo sustente.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Reejecución idempotente | S02, S04 | `implementation/productos/P430_idempotency/professor/main.py`: `generate_daily_report`; `implementation/productos/P430_idempotency/professor/test_main.py` | No usa `report_date` como clave. |
| H02 — Caso como límite | S01, S03 | `implementation/productos/P430_idempotency/professor/main.py` (literal); `implementation/productos/P430_idempotency/submission/daily_report.json` | Riesgo no derivado de datos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Entrada | `data/` (sólo `.gitkeep`); literal en `professor/main.py` | Sin dato de origen. |
| S02 | Lógica idempotente | `professor/main.py` | Clave implícita en la ruta. |
| S03 | Reporte | `submission/daily_report.json` | Un solo día. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** escribe el reporte sólo si no existe; si existe, lo devuelve.
- **`submission/`:** `daily_report.json`.
- **Pruebas:** `test_01` exige el archivo. La prueba de profesor verifica la reutilización tras una reejecución. Ninguna verifica la clave por fecha ni el contenido del riesgo.
- **Trazabilidad:** P430 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P425:** vocabulario `factory_id`/`risk`; no recibe artefactos.
- **Habilita para Pyyy:** no evidenciada como artefacto; el registro `factory 2 / high` reaparece en P435 sin dependencia demostrable.

## Trazabilidad y auditoría

P430 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en la reejecución segura de una tarea; C05 (recuperación) se apoya en el mismo mecanismo. El producto de Analytics nombrado (riesgo de fábrica) no se produce: es un literal. Auditoría de identidad (pregunta 5): el patrón es de ingeniería de pipelines y no opera una capacidad calculada; riesgo moderado, atenuado por el vocabulario de riesgo compartido con P425.
