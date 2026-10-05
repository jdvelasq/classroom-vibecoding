# P434 — Contract versioning: compatibilidad declarada entre versiones de contrato

## Actividad actual implementada

**Implementación:** `implementation/productos/P434_contract_versioning/`.

### Preguntas analíticas actuales

- ¿Puede un consumidor que espera cierta versión del contrato integrarse con la versión vigente del producto?

`data/contract.json` declara la versión `2.0`, los campos requeridos `factory_id` y `risk` y la lista `compatible_with: ["1.0", "2.0"]`. `professor/main.py` define `is_compatible(consumer_version, contract)`, que responde si la versión del consumidor está en esa lista, y persiste el resultado para dos versiones fijas: `submission/compatibility.json` = `{"1.0": true, "3.0": false}`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decidir si un consumidor puede integrarse; el consumidor no se identifica.
- **Producto terminal:** `submission/compatibility.json`, tabla de compatibilidad por versión consumidora.
- **Uso y límite:** muestra que la compatibilidad se declara en el contrato y no se supone. `required_fields` no se usa: no se comprueba que un registro cumpla el contrato, ni qué cambió entre 1.0 y 2.0. La compatibilidad es pertenencia a una lista, no una regla semántica de versionado.
- **Disciplinas contribuyentes:** gestión de contratos de datos/API.

### Highlights de contribución

- **H01 — Decide la integración por la compatibilidad declarada, no por suposición:** `is_compatible` consulta `compatible_with`; la prueba de profesor exige `True` para 1.0 y 2.0 y `False` para 3.0, y su docstring afirma que «la versión del consumidor, no una suposición, determina si puede integrarse». Primera aparición de versiones de contrato en el curso; P425 definía un contrato de API sin versión. Sin este hito, un cambio de contrato rompería consumidores sin señal previa.
- **H02 — Caso y datos (límite):** el contrato nombra `factory_id` y `risk`, el vocabulario del indicador de riesgo por fábrica de P425 y P430, pero no hay registros ni historial de versiones: la diferencia entre 1.0 y 2.0 no se describe en esta actividad (P435 la materializa por separado). No hay particularidad del dato que condicione la regla; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** contrato JSON con versión y lista de compatibilidad; función de compatibilidad parametrizable.
- **Reutiliza:** vocabulario `factory_id`/`risk`.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Compatibilidad declarada | H01 | Pertenencia a `compatible_with` | Sin semántica de versión; `required_fields` sin uso. |
| Contrato del indicador | H02 | Versión 2.0 con `factory_id`, `risk` | Sin registros que lo cumplan o violen. |

### Relación técnica con actividades anteriores

Nueva exigencia sobre el contrato de P425: de «qué recibe y responde» a «qué versiones acepta». No consume el contrato de P425 (cuyos campos son `daily_units_produced`, `risk`, `threshold`), por lo que la relación es conceptual. Complementaria con P435, que migra un registro de v1 a v2; ambas comparten `factory_id`/`risk` sin compartir artefactos.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Compatibilidad declarada | S02, S04 | `implementation/productos/P434_contract_versioning/professor/main.py`: `is_compatible`; `implementation/productos/P434_contract_versioning/professor/test_main.py`; `implementation/productos/P434_contract_versioning/submission/compatibility.json` | Lista fija; versiones consumidoras literales. |
| H02 — Caso como límite | S01 | `implementation/productos/P434_contract_versioning/data/contract.json` | `required_fields` sin uso. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Contrato | `data/contract.json` | Una versión vigente; sin registro de cambios. |
| S02 | Regla de compatibilidad | `professor/main.py` | Pertenencia a lista; versiones 1.0 y 3.0 fijas. |
| S03 | Resultado | `submission/compatibility.json` | Dos versiones. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** evalúa la compatibilidad de las versiones 1.0 y 3.0 contra el contrato.
- **`submission/`:** `compatibility.json`.
- **Pruebas:** `test_01` exige el archivo; la prueba de profesor verifica la regla con un contrato en memoria. No verifican `required_fields`.
- **Trazabilidad:** P434 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P425:** la noción de contrato de la capacidad; no recibe artefactos.
- **Habilita para P435:** la noción de versiones 1.0/2.0 del registro `factory_id`/`risk`; no hay consumo de artefactos.

## Trazabilidad y auditoría

P434 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en la integración segura entre versiones; C05 (mantenimiento) parcialmente. El contrato es evidencia natural de `productos.C01` (contrato operativo), no mapeada. Auditoría de identidad (pregunta 5): el vocabulario de riesgo por fábrica ancla el contrato en una capacidad del curso, pero sin usuario ni registros el taller puede leerse como técnica genérica de versionado de APIs; riesgo moderado.
