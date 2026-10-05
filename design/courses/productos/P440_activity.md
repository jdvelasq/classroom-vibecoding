# P440 — Data reconciliation: conciliación de conteo y total de control

## Actividad actual implementada

**Implementación:** `implementation/productos/P440_data_reconciliation/`.

### Preguntas analíticas actuales

- ¿La salida de datos conserva lo que había en el origen antes de publicarse, tanto en número de filas como en un total de control?

`data/source.json` declara `rows: 100`, `total_amount: 1500`; `data/target.json`, `rows: 100`, `total_amount: 1450`. `professor/main.py` define `reconcile`, que compara ambas métricas y declara `reconciled` sólo si todas coinciden. `submission/reconciliation.json` registra `rows: true`, `total_amount: false`, `reconciled: false`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decidir si una salida puede publicarse; el consumidor no se identifica.
- **Producto terminal:** `submission/reconciliation.json`, resultado de conciliación por control.
- **Uso y límite:** muestra que coincidir en filas no basta y que un total de control detecta una pérdida de valor. Las métricas son resúmenes declarados, no calculados de tablas reales; no se localiza la diferencia (50 unidades) ni se bloquea una publicación; la igualdad es exacta, sin tolerancia.
- **Disciplinas contribuyentes:** controles de calidad de datos entre origen y destino.

### Highlights de contribución

- **H01 — Exige un total de control además del conteo de filas (caso y datos):** el caso está construido para que `rows` coincida y `total_amount` no; la docstring declara que «coincidir en filas no basta». Esta configuración es la particularidad del dato y exige comparar una medida agregada, no sólo cardinalidad. Límite: los totales son declarados y la medida `amount` no pertenece a ningún caso del curso. Sin este hito, una transformación que altera valores sin perder filas pasaría como correcta.
- **H02 — Condiciona la aprobación a todos los controles:** `reconciled = all(checks.values())`; la prueba de profesor verifica aprobación con controles iguales y rechazo con un total distinto en una unidad. Primera conciliación origen–destino del curso; extiende la validación de un conjunto de datos de P402 a la comparación entre dos etapas. Sin este hito, la publicación no tendría una condición verificable de conservación.

### Inventario técnico de implementación

- **Introduce:** controles de conciliación (filas y total) con veredicto agregado.
- **Reutiliza:** patrón de función con entradas inyectables.
- **Aplica en nuevo caso:** resúmenes origen/destino genéricos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Total de control | H01 | Filas iguales, total distinto | Resúmenes declarados; sin tolerancia. |
| Veredicto de publicación | H02 | `all(checks)` | No bloquea ninguna salida real. |

### Relación técnica con actividades anteriores

Nueva exigencia de evidencia frente a P402 (validación de un archivo) y P417 (prueba de integración que compara la salida esperada): aquí se comparan dos etapas por métricas de control. No usa el dato de operación de fábricas, que permitiría conciliar `daily_operations.csv` con los totales por fábrica producidos en P428–P433.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Total de control | S01, S02 | `implementation/productos/P440_data_reconciliation/data/source.json`; `implementation/productos/P440_data_reconciliation/data/target.json`; `implementation/productos/P440_data_reconciliation/professor/main.py`: `reconcile` | Totales declarados. |
| H02 — Veredicto | S02, S03, S04 | `implementation/productos/P440_data_reconciliation/professor/test_main.py`; `implementation/productos/P440_data_reconciliation/submission/reconciliation.json` | Sin efecto sobre una publicación. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Resúmenes origen/destino | `data/source.json`; `data/target.json` | Métricas declaradas. |
| S02 | Conciliación | `professor/main.py` | Igualdad exacta; dos controles. |
| S03 | Resultado | `submission/reconciliation.json` | Sin magnitud de la diferencia. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** compara filas y total y guarda el veredicto.
- **`submission/`:** `reconciliation.json`.
- **Pruebas:** `test_01` exige el archivo; las pruebas de profesor verifican aprobación y rechazo. No verifican el contenido entregado.
- **Trazabilidad:** P440 mapea `productos.C02`, `productos.C03` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P402:** la práctica de validar datos antes de usarlos; sin artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P440 está mapeada a `productos.C02`, `C03` y `C05`. C03 se sostiene en la validación de la salida antes de publicar; C02 y C05 parcialmente. Auditoría de identidad (pregunta 5): con resúmenes genéricos (`amount`) ajenos a los casos del curso, el taller se lee como control genérico de data engineering; riesgo de identidad registrado.
