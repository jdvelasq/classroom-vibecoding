# P105 — Resumen de conductores especificado con ChatGPT

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P105_drivers_chatgpt/`.

### Preguntas analíticas actuales

Las mismas de P103, ahora formuladas como instrucciones para un asistente conversacional:

- ¿Qué variables tiene cada tabla, cuál es la llave que las relaciona y qué plan de análisis es razonable?
- ¿Cuál es la media, el total y el rango de horas/millas por conductor, y en qué semanas un conductor registró menos horas que su media?
- ¿Qué diez conductores registraron más millas y cómo se representan en un gráfico?

El notebook del profesor contiene diez celdas. Cada una tiene, comentado, el código pandas de P103 y, como cadena de texto, el *prompt* en español que pide ese mismo paso a ChatGPT. Nada se ejecuta: no hay salidas, no hay artefactos en `submission/` y no hay respuestas del asistente registradas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** iguales a P103; usuario y decisión no evidenciados.
- **Producto terminal:** una secuencia de *prompts* que especifica en lenguaje natural el análisis de P103. No hay producto descriptivo persistido.
- **Uso y límite:** muestra cómo traducir cada transformación en una instrucción precisa. No evidencia que las respuestas del asistente se hayan obtenido, ejecutado ni comparado con el resultado conocido de P103.
- **Disciplinas contribuyentes:** IA generativa como asistente de codificación; pandas y matplotlib como referencia comentada.

### Highlights de contribución

- **H01 — Especifica cada transformación como instrucción verificable en lenguaje natural:** los *prompts* nombran la tabla de entrada, la operación, las columnas y el nombre de la tabla resultante (`timesheet_with_means`, `timesheet_below`, `sum_timesheet`, `min_max_timesheet`, `summary`, `top10`) y describen el gráfico (nombres en el eje vertical, el mayor arriba, archivo `top10_drivers.png`). Cada *prompt* aparece junto al código de P103 que lo resuelve. Extiende P103 a un nuevo modo de producción del mismo análisis; sin este hito, el uso del asistente no tendría una referencia contra la cual contrastarse.
- **H02 — Traslada la estructura del dataset al *prompt* (caso y datos):** las instrucciones deben hacer explícitas las condiciones que en P103 resolvía el código: la llave `driverId`, «una fila por conductor», «no incluya `week`», «conservando todos los registros originales» al añadir la media, y nombres de columna con guion. La granularidad conductor-semana frente a conductor determina el contenido de cada instrucción. Sin este hito, el *prompt* omitiría las decisiones de granularidad que cambian el resultado.
- **H03 — Introduce una salvaguarda explícita frente a datos inventados:** el primer *prompt* pide describir variables, identificar la llave y proponer un plan, con la restricción «No inventes datos ni modifiques las tablas». Es la primera aparición en el curso de un límite sobre la fuente de evidencia. Límite: no hay paso de verificación de la respuesta ni consideración sobre compartir con el asistente una tabla que contiene `ssn` y `location`, campos que P102 excluía.

### Inventario técnico de implementación

- **Introduce:** redacción de *prompts* por paso, con nombres de tablas intermedias y restricciones.
- **Reutiliza de P103 (comentado):** lectura, `groupby`, `transform`, filtros, `merge`, `to_csv`, ranking y gráfico; en `min_max_timesheet` usa `agg(["min", "max"])` con cadenas, a diferencia de P103.
- **Interfaz de estudiante:** `notebooks/notebook.ipynb` vacío; `submission/` sin artefactos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| *Prompts* emparejados con código de referencia | H01, H02 | Diez celdas con *prompt* y código P103 comentado | `professor/notebook.ipynb`; sin respuestas registradas. |
| Restricción de no inventar datos | H03 | Instrucción explícita en el primer *prompt* | `professor/notebook.ipynb`; sin verificación posterior. |

### Relación técnica con actividades anteriores

Misma pregunta y mismos datos que P103 y P104, con un nuevo medio (asistente conversacional). A diferencia de P104, no produce ni verifica un resultado: el contraste con P103 queda sólo en el emparejamiento textual *prompt*–código. No duplica la técnica, pero sí la pregunta por tercera vez.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — *Prompts* verificables | S02, S03 | `implementation/descriptiva/P105_drivers_chatgpt/professor/notebook.ipynb`: celdas 2–10 | No hay salidas del asistente ni ejecución. |
| H02 — Estructura del dataset en el *prompt* | S01, S02 | `implementation/descriptiva/P105_drivers_chatgpt/data/drivers.csv`; `implementation/descriptiva/P105_drivers_chatgpt/data/timesheet.csv`; `implementation/descriptiva/P105_drivers_chatgpt/professor/notebook.ipynb` | La precisión del *prompt* no se contrasta con un resultado. |
| H03 — Salvaguarda frente a datos inventados | S02, S04 | `implementation/descriptiva/P105_drivers_chatgpt/professor/notebook.ipynb`: celda 1; `implementation/descriptiva/P105_drivers_chatgpt/tests/test_activity.py` | La prueba sólo exige una celda en el notebook. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset compartido con el asistente | `data/drivers.csv`; `data/timesheet.csv` | `drivers.csv` contiene `ssn` y `location`. |
| S02 | *Prompts* y código de referencia | `professor/notebook.ipynb` | Código comentado; nada se ejecuta. |
| S03 | Producto y persistencia | `submission/` | Vacío salvo `.gitkeep`; no hay contrato de artefactos. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo verifica que el notebook tenga al menos una celda. |
| S05 | Interfaz de estudiante | `notebooks/notebook.ipynb` | Vacío; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** el notebook del profesor conserva los *prompts* y el código de referencia comentado; no ejecuta análisis.
- **`submission/`:** sin artefactos.
- **Pruebas:** comprueban participación (notebook con más de cero celdas). No verifican *prompts*, respuestas, código generado, resumen ni gráfico.
- **Trazabilidad:** P105 mapea `descriptiva.C02`, `descriptiva.C03` y `descriptiva.C05`.

### Dependencias en la secuencia

- **Recibe de P103:** preguntas, datos y el código completo, que aparece comentado como referencia.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P105 está mapeada a `descriptiva.C02`, `descriptiva.C03` y `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. Con la evidencia actual, ninguna de las tres queda sustentada por un artefacto: no hay exploración ejecutada (C02), no hay visualización persistida (C03) y la comunicación responsable (C05) se limita a la instrucción de no inventar datos. El mapeo excede la evidencia observable y requiere revisión. El producto es una especificación del análisis de P103, no una descripción; la actividad se centra en una herramienta contribuyente (IA generativa) y su conexión con el producto descriptivo depende de pasos de verificación que no están implementados.
