# P451 — Retroalimentación de usuarios: señal de utilidad ligada a la respuesta evaluada

## Actividad actual implementada

**Implementación:** `implementation/productos/P451_user_feedback/`.

### Preguntas analíticas actuales

- ¿Cómo se registra si una respuesta del producto analítico fue útil para su consumidor, junto con la respuesta que se evaluó?

`data/product_response.json` contiene una respuesta del producto: fábrica 2, riesgo `high`. `professor/main.py` (`capture_feedback`) arma un registro con la respuesta, un booleano `useful` y un comentario. `main()` escribe en `submission/feedback.json` `useful: true` y el comentario «Permitió priorizar la inspección.», ambos escritos en el código: no provienen de un usuario. No se registra quién responde ni cuándo, y no hay agregación de señales. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** conectar la salida analítica con su adopción (docstring); consumidor no identificado.
- **Producto terminal:** un registro de retroalimentación por respuesta.
- **Uso y límite:** fija la forma de un registro que mantiene juntas la salida y su valoración. El contenido persistido es simulado y no puede leerse como evidencia de adopción; no hay mecanismo que use la señal para mejorar el producto.
- **Disciplinas contribuyentes:** gestión de producto al servicio de la mejora de un indicador de riesgo.

### Highlights de contribución

- **H01 — Liga la valoración a la respuesta exacta que la provocó (caso y datos):** el registro embebe la respuesta (`factory_id`, `risk`) en lugar de una referencia, de modo que la señal se interpreta con la salida que el consumidor vio. La prueba de profesor exige esa unión. Límite: el comentario y la utilidad persistidos son texto fijo del código, no observaciones de uso; la respuesta repite el `high` de la fábrica 2 de P430/P450. Sin este hito, la utilidad quedaría desvinculada de la salida evaluada.
- **H02 — Conserva la señal negativa:** la segunda prueba de profesor exige que `useful: False` y «No llegó a tiempo.» se preserven sin filtrar. `tests/test_activity.py` sólo exige el archivo. Sin este hito, el registro podría sesgarse hacia valoraciones positivas.

### Inventario técnico de implementación

- **Introduce:** registro de retroalimentación con respuesta embebida, utilidad y comentario.
- **Aplica en nuevo caso:** la respuesta de riesgo por fábrica como objeto valorado.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Señal ligada a respuesta | H01 | Respuesta embebida en el registro | Contenido simulado en el código. |
| Señal negativa conservada | H02 | Prueba de `useful: False` | Sin agregación ni uso de la señal. |

### Relación técnica con actividades anteriores

Mismo resultado de riesgo por fábrica que P430 y P450, con nuevo producto: valoración del consumidor. La respuesta no se toma del servicio de P425/P426 (cuya respuesta incluye `threshold`). Patrón de registro muy cercano a P450 (dato dado + decisión/valoración escrita en el código); posible solapamiento estructural.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Señal ligada a respuesta | S01, S02, S03 | `implementation/productos/P451_user_feedback/data/product_response.json`; `implementation/productos/P451_user_feedback/professor/main.py`: `capture_feedback`; `implementation/productos/P451_user_feedback/submission/feedback.json` | Valoración simulada. |
| H02 — Señal negativa | S04 | `implementation/productos/P451_user_feedback/professor/test_main.py`; `implementation/productos/P451_user_feedback/tests/test_activity.py` | La prueba del estudiante no verifica contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Respuesta evaluada | `data/product_response.json` | Una respuesta; no proviene del servicio. |
| S02 | Captura | `professor/main.py` | Utilidad y comentario escritos en el código. |
| S03 | Registro entregado | `submission/feedback.json` | Un registro; sin usuario ni fecha. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: unión y señal negativa; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** une respuesta, utilidad y comentario y persiste el registro.
- **`submission/`:** `feedback.json`.
- **Pruebas:** las de profesor verifican el registro completo y la conservación de una señal negativa; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C04` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P430/P450:** el contenido `factory_id: 2`, `risk: high`, repetido sin lectura de artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P451 mapea `productos.C04` («retroalimentación operativa») y `productos.C05` («mejorar»). C04 se sostiene en la forma del registro; C05 no se ejerce, porque la señal no alimenta ninguna mejora. El producto de Analytics valorado es el indicador de riesgo por fábrica; la valoración es simulada.
