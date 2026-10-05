# P441 — Data quarantine: separación de registros inválidos con motivo de rechazo

## Actividad actual implementada

**Implementación:** `implementation/productos/P441_data_quarantine/`.

### Preguntas analíticas actuales

- ¿Cómo se protege la salida válida de registros inválidos sin perder la evidencia necesaria para corregirlos?

`data/records.json` contiene dos registros (`amount` 20 y −5). `professor/main.py` define `quarantine_invalid_records`, que separa los registros con `amount >= 0` como válidos y añade a los demás `rejection_reason: "amount_must_be_non_negative"`. `submission/quarantine.json` contiene un registro válido (id 1) y uno en cuarentena (id 2, −5, con su motivo).

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** `submission/quarantine.json`, partición válidos/cuarentena con motivo.
- **Uso y límite:** muestra que un registro inválido no contamina la salida ni desaparece sin explicación. Hay una sola regla; válidos y cuarentena se guardan en el mismo archivo; no hay flujo de corrección o reingreso; `amount` no pertenece a ningún caso del curso.
- **Disciplinas contribuyentes:** manejo de registros rechazados en pipelines de datos.

### Highlights de contribución

- **H01 — Separa registros inválidos conservando un motivo de rechazo:** dos listas por comprensión con la misma regla y `dict(record, rejection_reason=...)`; la prueba de profesor exige que el válido quede intacto y que el inválido conserve sus campos más el motivo, y su docstring declara que no debe «desaparecer sin explicación». Extiende P402, que reportaba violaciones del archivo completo (incluida la producción negativa), a una partición por registro que deja pasar lo válido. Sin este hito, la única respuesta a un dato inválido sería rechazar el lote o descartarlo en silencio.
- **H02 — Caso y datos (límite):** la regla de no negatividad tiene sentido para una cantidad, como `daily_units_produced` en P402, pero aquí se aplica a un `amount` genérico de dos registros. La implementación no revela una particularidad del caso que determine la regla ni el destino de la cuarentena; se registra como límite.

### Inventario técnico de implementación

- **Introduce:** partición válidos/cuarentena; motivo de rechazo codificado por registro.
- **Extiende:** la regla de no negatividad de P402, de violación de lote a rechazo por registro.
- **Aplica en nuevo caso:** registros genéricos con `amount`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Cuarentena con motivo | H01 | Partición y `rejection_reason` | Una regla; mismo archivo de salida. |
| Regla de dominio | H02 | `amount >= 0` | Medida genérica. |

### Relación técnica con actividades anteriores

Nueva respuesta operativa a la validación de P402 (lote rechazado frente a registros separados) y complemento de P440 (conciliación entre etapas). No comparte datos con actividades previas; la misma regla sobre `daily_units_produced` habría conectado con el caso de fábricas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Cuarentena con motivo | S02, S03, S04 | `implementation/productos/P441_data_quarantine/professor/main.py`: `quarantine_invalid_records`; `implementation/productos/P441_data_quarantine/professor/test_main.py`; `implementation/productos/P441_data_quarantine/submission/quarantine.json` | Sin flujo de corrección. |
| H02 — Caso como límite | S01 | `implementation/productos/P441_data_quarantine/data/records.json` | Dos registros genéricos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Registros | `data/records.json` | Dos registros con `amount`. |
| S02 | Regla y partición | `professor/main.py` | Una regla codificada dos veces. |
| S03 | Salida | `submission/quarantine.json` | Válidos y cuarentena juntos. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Existencia del archivo en la prueba de actividad. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** separa válidos e inválidos y guarda ambos con motivo.
- **`submission/`:** `quarantine.json`.
- **Pruebas:** `test_01` exige el archivo; la prueba de profesor verifica la partición y el motivo. No verifican el contenido entregado.
- **Trazabilidad:** P441 mapea `productos.C02`, `productos.C03` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P402:** la regla de no negatividad como práctica de validación; sin artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P441 está mapeada a `productos.C02`, `C03` y `C05`. C03 se sostiene en la validación por registro; C05 (gobierno de rechazos) parcialmente; C02 débil. Auditoría de identidad (pregunta 5): con datos genéricos ajenos a los casos del curso, el taller se lee como patrón de data engineering; riesgo de identidad registrado.
