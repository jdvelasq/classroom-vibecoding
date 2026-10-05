# P453 — Enmascaramiento de datos: correo reducido en un reporte de riesgo de cliente

## Actividad actual implementada

**Implementación:** `implementation/productos/P453_data_masking/`.

### Preguntas analíticas actuales

- ¿Cómo se comparte una salida con nivel de riesgo sin exponer el correo completo de la persona?

`data/customers.csv` tiene una sola fila: `customer_id` 1, `email` `ana@example.com`, `risk` `high`. `professor/main.py` lee sólo la primera fila (`next(csv.DictReader(...))`), enmascara el correo conservando la primera letra y el dominio (`mask_email`) y devuelve `customer_id` y `risk` sin cambios. `submission/masked_report.json` registra `a***@example.com`. El caso cambia de entidad: clientes en lugar de fábricas; el significado de `risk` para un cliente no se documenta. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** compartir una salida operativa sin revelar más de lo necesario (docstring); destinatario no identificado.
- **Producto terminal:** reporte de una fila con identificador directo enmascarado.
- **Uso y límite:** reduce la exposición del correo. Conserva el dominio y el `customer_id` sin seudonimizar, por lo que no permite afirmar anonimización; procesa una sola fila.
- **Disciplinas contribuyentes:** privacidad de datos al servicio de la distribución de un resultado de riesgo.

### Highlights de contribución

- **H01 — Introduce un identificador personal en la salida analítica (caso y datos):** por primera vez en el bloque la entidad es una persona con correo; esa condición, ausente en el caso de fábricas, es la que exige enmascarar antes de compartir. El riesgo se conserva intacto porque es el contenido útil del reporte. Límite: `customer_id` queda en claro y el dominio se mantiene; la fila única no ejercita volumen ni casos irregulares. Sin este hito, el curso no trataría datos personales en un producto distribuido.
- **H02 — Reduce el correo a inicial y dominio, verificado:** la prueba de profesor exige `a***@example.com` para `ana.gomez@example.com` y que la parte local no aparezca. No se prueban correos sin `@` ni varias filas; `tests/test_activity.py` sólo exige el archivo. Sin este hito, la regla de enmascaramiento no estaría fijada.

### Inventario técnico de implementación

- **Introduce:** enmascaramiento de correo con conservación parcial y lectura con `csv.DictReader`.
- **Aplica en nuevo caso:** una salida de riesgo por cliente.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Dato personal en salida | H01 | Correo y riesgo por cliente | Una fila; `customer_id` en claro. |
| Regla de enmascaramiento | H02 | Inicial + `***@` + dominio | Dominio conservado; sin casos irregulares. |

### Relación técnica con actividades anteriores

Complementa P427 (no exponer un secreto) y P452 (limitar quién consume) con la reducción del contenido entregado. Nuevo caso (clientes) sin relación de datos con el riesgo por fábrica de P450–P452; posible discontinuidad de caso que requiere decisión posterior.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Dato personal en salida | S01, S02, S03 | `implementation/productos/P453_data_masking/data/customers.csv`; `implementation/productos/P453_data_masking/professor/main.py`: `create_masked_report`; `implementation/productos/P453_data_masking/submission/masked_report.json` | Riesgo de cliente sin definición. |
| H02 — Regla verificada | S02, S04 | `implementation/productos/P453_data_masking/professor/main.py`: `mask_email`; `implementation/productos/P453_data_masking/professor/test_main.py` | No se prueban entradas irregulares. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datos de clientes | `data/customers.csv` | Una fila; correo de ejemplo. |
| S02 | Enmascaramiento | `professor/main.py` | Sólo primera fila; sólo correo. |
| S03 | Reporte entregado | `submission/masked_report.json` | `customer_id` en claro. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: regla; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** lee la primera fila, enmascara el correo y persiste el reporte.
- **`submission/`:** `masked_report.json`.
- **Pruebas:** la de profesor verifica la salida enmascarada y la ausencia de la parte local; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C04` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna demostrable.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P453 mapea `productos.C04` y `productos.C05` («privacidad»); C05 se sostiene. El producto analítico protegido es una salida de riesgo por cliente que no se produce ni se define en el curso. Auditoría pregunta 5: sin vínculo con una capacidad del curso, la actividad puede leerse como ejercicio genérico de enmascaramiento.
