# P417 — Prueba de integración del flujo: de la entrada al archivo publicado

## Actividad actual implementada

**Implementación:** `implementation/productos/P417_pipeline_integration_test/`.

### Preguntas analíticas actuales

- ¿El flujo completo, desde el CSV de entrada hasta el archivo publicado, entrega los totales por fábrica acordados?

`professor/main.py` define `run_pipeline()`: lee `data/daily_operations.csv` (cuatro filas máquina-día), suma `daily_units_produced` por `factory_id`, escribe `submission/factory_totals.json` y devuelve la ruta del archivo. `professor/test_main.py` invoca `run_pipeline()`, lee el archivo devuelto y exige `{"factory_totals": {"1": 9303, "2": 9300}}`. El docstring declara el propósito: «El flujo completo permite detectar fallas entre componentes que funcionan aislados». No hay notebook ni `HOW_TO_RUN_ME.txt`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/factory_totals.json` y una prueba que recorre lectura, agregación y escritura.
- **Uso y límite:** muestra una prueba que verifica el artefacto publicado y no sólo el valor en memoria. El «flujo» es una función de tres pasos; no hay componentes separados cuya integración pueda fallar.
- **Disciplinas contribuyentes:** pruebas de software (integración) al servicio de verificar que el indicador publicado coincide con lo acordado.

### Highlights de contribución

- **H01 — Verifica el artefacto publicado, no el cálculo aislado:** `test_01_publishes_factory_totals_from_input_to_output` usa la ruta devuelta por `run_pipeline()` y lee el JSON escrito. P400 y P401 probaban funciones de cálculo; aquí la aserción recae sobre el archivo que consumiría un usuario. Sin este hito, la secuencia no distinguiría prueba unitaria de prueba del flujo.
- **H02 — Limita la integración a un caso trivial (caso y datos):** el mismo CSV de cuatro filas y los mismos totales de P400/P412–P414; no hay transformación intermedia, validación de esquema ni segundo componente. La ausencia de particularidad es un límite: el caso no puede mostrar una falla entre componentes, que es lo que el docstring promete. Sin este hito no se perdería un mecanismo nuevo, sino la formulación explícita de la prueba de integración.

### Inventario técnico de implementación

- **Introduce:** función de flujo que devuelve la ruta del artefacto; prueba que lee el artefacto publicado.
- **Reutiliza:** dataset, agregación y valores esperados de P400/P412–P414; carga del módulo de profesor con `importlib.util`.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Prueba de extremo a extremo | H01, H02 | Lectura → agregación → JSON → aserción sobre el archivo | Un solo componente; escribe en `submission/` real. |

### Relación técnica con actividades anteriores

Misma pregunta y dato que P400 y P412–P414. Las pruebas `tests/test_report.py` de P413–P414 ya ejecutaban `src/main.py` y comprobaban el archivo publicado con los mismos valores; P417 renombra ese patrón como prueba de integración sin añadir componentes. Posible duplicación con P413–P414 que requiere decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Artefacto publicado | S02, S03 | `implementation/productos/P417_pipeline_integration_test/professor/main.py`: `run_pipeline`; `implementation/productos/P417_pipeline_integration_test/professor/test_main.py` | La prueba escribe en `submission/` real, no en un directorio temporal. |
| H02 — Caso trivial | S01 | `implementation/productos/P417_pipeline_integration_test/data/daily_operations.csv`; `implementation/productos/P417_pipeline_integration_test/submission/factory_totals.json` | No hay componentes que integrar. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/daily_operations.csv` | Cuatro filas. |
| S02 | Flujo | `professor/main.py`; `src/main.py` | Una función; plantilla sin instrucciones (`NotImplementedError`, sin `HOW_TO_RUN_ME.txt`). |
| S03 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Prueba de profesor exacta; prueba de estudiante sólo de existencia. |
| S04 | Artefacto | `submission/factory_totals.json` | JSON compacto de totales. |

### Contrato de evidencia actual

- **Notebook o código:** `run_pipeline()` lee, agrega, escribe y devuelve la ruta.
- **`submission/`:** `factory_totals.json`.
- **Pruebas:** `professor/test_main.py` verifica el contenido exacto del archivo publicado; `tests/test_activity.py` sólo su existencia. Ninguna prueba ejercita el flujo del estudiante (`src/main.py`).
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P400/P412–P414:** dataset, cálculo y valores esperados.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P417 → `productos.C02`, `productos.C05`. C02 se sostiene parcialmente (verificación de la entrega). C05 sin evidencia. Auditoría (pregunta 5): taller genérico de pruebas de software sobre un indicador trivial; riesgo de identidad no resuelto. El nombre promete integración entre componentes que la implementación no tiene.
