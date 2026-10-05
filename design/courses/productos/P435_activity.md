# P435 — Schema migration: migración de un registro de contrato v1 a v2

## Actividad actual implementada

**Implementación:** `implementation/productos/P435_schema_migration/`.

### Preguntas analíticas actuales

- ¿Cómo se adapta un registro producido con el esquema v1 al esquema v2 sin perder el valor que consume el producto?

`data/record_v1.json` contiene un registro `{"factory": 2, "risk": "high"}`. `professor/main.py` define `migrate_v1_to_v2`, que renombra `factory` a `factory_id`, conserva `risk` y añade `schema_version: "2.0"`. El bloque `__main__` escribe `submission/record_v2.json` = `{"schema_version": "2.0", "factory_id": 2, "risk": "high"}`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados; la docstring de la prueba habla de «la decisión que consume el producto» sin nombrarla.
- **Producto terminal:** `submission/record_v2.json`, un registro migrado.
- **Uso y límite:** muestra una migración explícita de un campo renombrado con versión de esquema. Migra un registro, no una colección; no valida el registro contra un contrato (P434 declara `required_fields` compatibles pero no se usan aquí); no hay migración inversa ni manejo de registros mal formados.
- **Disciplinas contribuyentes:** evolución de esquemas de datos.

### Highlights de contribución

- **H01 — Migra el esquema preservando el valor analítico:** `migrate_v1_to_v2` cambia el nombre del campo de entidad y etiqueta la versión; la prueba de profesor exige igualdad exacta del registro migrado y su docstring declara que la migración «cambia el esquema sin perder la decisión». Complementa P434 (qué versiones son compatibles) con la transformación entre ellas. Sin este hito, la evolución del contrato no tendría un camino para los datos ya producidos.
- **H02 — Caso y datos (límite):** el único cambio de esquema es un renombre (`factory` → `factory_id`), que alinea el registro con los nombres de P425 y P434. El riesgo `high` de la fábrica 2 es literal, como en P430, y no se deriva de `daily_operations.csv`. No hay particularidad del dato que condicione la migración (tipos, valores faltantes, semántica cambiada); se registra como límite.

### Inventario técnico de implementación

- **Introduce:** función de migración de esquema con campo `schema_version`.
- **Reutiliza:** registro `factory_id`/`risk` de P430 y P434.
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Migración v1 → v2 | H01 | Renombre de campo y versión explícita | Un registro; sin validación ni reversa. |
| Registro de riesgo | H02 | `factory_id`, `risk` | Valor literal. |

### Relación técnica con actividades anteriores

Nueva transformación al servicio del mismo contrato conceptual de P434. P434 y P435 juntos cubren compatibilidad y migración, pero no comparten artefactos: P435 no comprueba su salida contra `data/contract.json` de P434. El mismo registro (fábrica 2, riesgo alto) aparece en P430, P450 y P451.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Migración preservando el valor | S02, S04 | `implementation/productos/P435_schema_migration/professor/main.py`: `migrate_v1_to_v2`; `implementation/productos/P435_schema_migration/professor/test_main.py`; `implementation/productos/P435_schema_migration/submission/record_v2.json` | Un solo registro. |
| H02 — Caso como límite | S01 | `implementation/productos/P435_schema_migration/data/record_v1.json` | Valor no calculado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Registro v1 | `data/record_v1.json` | Un registro. |
| S02 | Migración | `professor/main.py` | Renombre; lógica de escritura en `__main__`, sin función `main`. |
| S03 | Registro v2 | `submission/record_v2.json` | Sin validación contra contrato. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** lee el registro v1, lo migra y guarda el v2.
- **`submission/`:** `record_v2.json`.
- **Pruebas:** `test_01` exige el archivo; la prueba de profesor verifica la migración de un registro en memoria. No verifican el contenido entregado ni el cumplimiento de un contrato.
- **Trazabilidad:** P435 mapea `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P434:** versiones 1.0/2.0 y campos `factory_id`/`risk` (conceptual; sin artefacto).
- **Habilita para Pyyy:** no evidenciada; P450 y P451 usan el mismo registro con `factory_id` sin consumir `record_v2.json`.

## Trazabilidad y auditoría

P435 está mapeada a `productos.C02` y `productos.C05`. C02 se sostiene en la continuidad de integración tras un cambio de esquema; C05 (mantenimiento) parcialmente. Auditoría de identidad (pregunta 5): migración genérica de un campo renombrado, anclada sólo por el vocabulario del indicador de riesgo; riesgo moderado. Posible combinación con P434 a decidir por el curso.
