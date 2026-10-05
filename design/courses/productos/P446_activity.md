# P446 — Runbook: procedimiento escrito para una alerta de frescura

## Actividad actual implementada

**Implementación:** `implementation/productos/P446_runbook/`.

### Preguntas analíticas actuales

- ¿Qué debe hacer quien atiende una alerta de frescura para no publicar un reporte con datos vencidos?

`RUNBOOK.md` contiene cuatro pasos: confirmar que la alerta es de frescura, verificar la fecha del último dato, **no publicar un reporte nuevo si el dato sigue vencido** y solicitar la actualización de la fuente registrando la acción. `professor/main.py` (`get_runbook`) devuelve ese texto sólo para el síntoma `freshness_alert` y lanza `ValueError` para cualquier otro; `main()` copia el procedimiento a `submission/freshness_alert_runbook.md`. `data/incident.json` (`incident-002`, `freshness_alert`, `open`) existe pero el código no lo lee: el síntoma está escrito en `main()`. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** responder a una alerta sin depender de memoria individual (docstring); el operador se nombra genéricamente.
- **Producto terminal:** procedimiento recuperable por síntoma, copiado como evidencia.
- **Uso y límite:** fija una salvaguarda sobre el producto (no publicar con dato vencido). No conecta el procedimiento con un reporte de frescura real (P439, P442) ni con el incidente del propio `data/`; no registra que la acción se tomó.
- **Disciplinas contribuyentes:** operación de sistemas (runbooks) al servicio de proteger la publicación de un reporte analítico.

### Highlights de contribución

- **H01 — Convierte la frescura en una salvaguarda de publicación (caso y datos):** el paso 3 del runbook liga la condición del dato con una consecuencia sobre el producto analítico: no publicar. Es la primera vez en la secuencia que una alerta de frescura (P439, P442) tiene una acción prescrita. Límite: el reporte afectado no se nombra y `data/incident.json` no interviene, de modo que no hay particularidad del caso más allá del síntoma. Sin este hito, las alertas de frescura no tendrían respuesta definida.
- **H02 — Asocia síntoma y procedimiento con rechazo explícito:** `get_runbook` sólo admite `freshness_alert`; la prueba de profesor exige que el texto contenga «No publique un reporte nuevo» y «Solicite la actualización de la fuente», y que un síntoma desconocido sea rechazado. `tests/test_activity.py` sólo exige el archivo copiado. Sin este hito, la salvaguarda del runbook no estaría protegida por pruebas.

### Inventario técnico de implementación

- **Introduce:** runbook en Markdown recuperado por síntoma y rechazo de síntomas no cubiertos.
- **Aplica en nuevo caso:** la alerta de frescura de P439 como disparador operativo.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Salvaguarda de publicación | H01 | Paso «No publique un reporte nuevo» | Reporte no nombrado; sin registro de ejecución. |
| Síntoma → procedimiento | H02 | `get_runbook` con `ValueError` | Un único síntoma cubierto. |

### Relación técnica con actividades anteriores

Nueva aplicación de la alerta de frescura de P439 y P442: de detectar a responder. No consume `freshness_report.json` ni `observability_report.json`. El incidente de `data/` se numera `incident-002`, mientras P447, posterior, produce `incident-001`; no hay relación de artefactos entre ambos y P447 no remite a este runbook. Posible solapamiento con P447 (respuesta a incidentes) que requiere decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Salvaguarda de publicación | S01, S02 | `implementation/productos/P446_runbook/RUNBOOK.md`; `implementation/productos/P446_runbook/data/incident.json`; `implementation/productos/P446_runbook/professor/main.py` | `incident.json` no se usa. |
| H02 — Síntoma y rechazo | S03, S04 | `implementation/productos/P446_runbook/professor/main.py`: `get_runbook`; `implementation/productos/P446_runbook/professor/test_main.py`; `implementation/productos/P446_runbook/submission/freshness_alert_runbook.md` | La prueba de estudiante no verifica contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Procedimiento | `RUNBOOK.md` | Cuatro pasos; un síntoma. |
| S02 | Incidente de entrada | `data/incident.json` | Presente pero no leído por el código. |
| S03 | Recuperación y entrega | `professor/main.py`; `submission/freshness_alert_runbook.md` | Copia literal del runbook. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: frases clave y rechazo; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** recupera el runbook para `freshness_alert` y lo copia a `submission/`.
- **`submission/`:** `freshness_alert_runbook.md`, idéntico a `RUNBOOK.md`.
- **Pruebas:** las de profesor verifican dos frases del procedimiento y el rechazo de síntomas desconocidos; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C04` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P439:** el síntoma de frescura como concepto; ningún artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P446 mapea `productos.C04` (documentación para uso responsable) y `productos.C05` (incidentes, recuperación). Ambas se sostienen en el runbook y su salvaguarda. El producto de Analytics protegido es un «reporte» genérico; la actividad sirve a la publicación responsable sin identificar qué capacidad se protege.
