# P450 — Revisión humana: autorización explícita de una recomendación de inspección

## Actividad actual implementada

**Implementación:** `implementation/productos/P450_human_review/`.

### Preguntas analíticas actuales

- ¿Queda autorizada la acción recomendada sólo cuando una persona la aprueba explícitamente?

`data/recommendation.json` contiene una recomendación: fábrica 2, riesgo `high`, acción `inspect_machine`. `professor/main.py` (`review_recommendation`) recibe una decisión humana y devuelve la recomendación, la decisión y `action_authorized`, verdadero sólo si la decisión es exactamente `approve`. El bloque `__main__` registra una aprobación en `submission/review.json`. No se registra quién revisa, cuándo ni por qué. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** conservar responsabilidad humana sobre una acción operacional (docstring); revisor no identificado.
- **Producto terminal:** registro de revisión que une recomendación, decisión y autorización.
- **Uso y límite:** permite que la acción derivada de un indicador quede condicionada a una aprobación. La recomendación llega dada: su procedencia no se evidencia y el registro no conserva identidad, momento ni justificación de la revisión.
- **Disciplinas contribuyentes:** gobierno de decisiones al servicio del uso responsable de un indicador de riesgo.

### Highlights de contribución

- **H01 — Separa la recomendación del indicador de la acción autorizada (caso y datos):** la entrada une entidad (fábrica 2), nivel de riesgo y acción operativa (`inspect_machine`); es la primera vez en el bloque que el producto de riesgo se traduce en una acción sobre una entidad. El valor `high` para la fábrica 2 aparece también en P430 y P452, pero no se deriva en el curso: aplicando la regla de P425 (`high` si `daily_units_produced < 4500`) a las filas de la fábrica 2 en `daily_operations.csv` (4700 y 4600) resultaría `low`. Sin este hito, el indicador no tendría un punto de control humano antes de actuar.
- **H02 — Autoriza sólo ante aprobación explícita:** `action_authorized = decision == "approve"`; cualquier otra cadena deja la acción sin autorizar. La prueba de profesor verifica aprobación y rechazo y que la recomendación se conserve intacta; `tests/test_activity.py` sólo exige el archivo. Sin este hito, la automatización podría ejecutar la acción por omisión.

### Inventario técnico de implementación

- **Introduce:** registro de revisión humana con autorización por lista blanca de una sola decisión.
- **Aplica en nuevo caso:** el reporte de riesgo por fábrica (P430) como recomendación accionable.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Recomendación accionable | H01 | Fábrica, riesgo y acción | Procedencia no evidenciada; inconsistente con la regla de P425. |
| Autorización humana | H02 | `approve` como única decisión autorizante | Sin revisor, fecha ni motivo. |

### Relación técnica con actividades anteriores

Nuevo producto (autorización) sobre el mismo resultado de riesgo por fábrica que P430 (`factory_id: 2`, `risk: high`) y que reaparece en P451 y P452. No consume ningún artefacto previo. La regla de riesgo de P425/P426 no reproduce ese resultado con el insumo del curso, lo que requiere decisión posterior.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Recomendación accionable | S01 | `implementation/productos/P450_human_review/data/recommendation.json`; `implementation/productos/P430_idempotency/professor/main.py`; `implementation/productos/P425_api_contract/professor/main.py`: `classify_risk`; `implementation/productos/P432_duckdb_transformation/data/daily_operations.csv` | El origen del riesgo `high` no se evidencia. |
| H02 — Autorización explícita | S02, S03, S04 | `implementation/productos/P450_human_review/professor/main.py`: `review_recommendation`; `implementation/productos/P450_human_review/professor/test_main.py`; `implementation/productos/P450_human_review/submission/review.json` | Decisión fija `approve` en `__main__`. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Recomendación de entrada | `data/recommendation.json` | Una recomendación dada. |
| S02 | Revisión | `professor/main.py` | Sin `main()`; decisión escrita en el código. |
| S03 | Registro entregado | `submission/review.json` | Sin revisor, fecha ni motivo. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: aprobar/rechazar; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** combina recomendación y decisión y calcula la autorización.
- **`submission/`:** `review.json` con una aprobación.
- **Pruebas:** las de profesor verifican que sólo `approve` autoriza y que `reject` no; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C04` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P430:** el resultado `factory_id: 2`, `risk: high` como contenido repetido; no se lee su archivo.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P450 mapea `productos.C04` («revisión humana») y `productos.C05`; C04 se sostiene. El producto de Analytics es el indicador de riesgo por fábrica convertido en acción revisable; el control humano sirve a su uso responsable. Límite: el indicador no se produce ni se reconcilia con la regla del curso.
