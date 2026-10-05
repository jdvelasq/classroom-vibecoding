# P447 — Respuesta a incidentes: de alerta de monitoreo a incidente con dueño y prioridad

## Actividad actual implementada

**Implementación:** `implementation/productos/P447_incident_response/`.

### Preguntas analíticas actuales

- ¿Cómo se convierte una alerta de cambio en la entrada de producción en un incidente rastreable con responsable y prioridad?

`data/monitoring_alert.json` describe `alert-001` sobre la variable `alcohol`, severidad `high`, con el mensaje «La entrada de producción cambió frente a la referencia». `professor/main.py` (`build_incident`) produce un incidente con `incident_id` fijo (`incident-001`), `alert_id` copiado, `status: open`, `owner: data-operations`, prioridad `P1` si la severidad es `high` y `P2` en otro caso, `initial_action: review_input_data` y `created_at`. `submission/incident.json` registra ese incidente con prioridad `P1`. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** que una alerta no se pierda entre registros (docstring); responsable declarado: `data-operations`.
- **Producto terminal:** registro de incidente abierto con dueño, prioridad y acción inicial.
- **Uso y límite:** permite pasar de una señal técnica a una responsabilidad asignada. No hay ciclo de vida (cierre, resolución, causa), el identificador es constante para cualquier alerta y la acción inicial no depende de la alerta.
- **Disciplinas contribuyentes:** gestión de incidentes al servicio de la operación de un modelo monitoreado.

### Highlights de contribución

- **H01 — Recibe la alerta sobre la variable que más se desplazó (caso y datos):** la alerta señala `alcohol`, que en `P422_model_monitoring/submission/monitoring_report.json` es la variable con mayor diferencia estandarizada (3.66) del caso de calidad de vinos (P420 y P422). La continuidad es conceptual: el JSON de alerta está escrito a mano con campos (`alert_id`, `severity`) que el reporte de P422 no produce, y la actividad vuelve al caso de vinos dentro de un bloque centrado en fábricas. Sin este hito, el monitoreo de P422 terminaría en una lista de alertas sin respuesta operativa.
- **H02 — Asigna dueño y prioridad desde la severidad:** la prueba de profesor exige `P1`, dueño `data-operations` y estado `open` para severidad alta, y `P2` para severidad media. `tests/test_activity.py` sólo exige el archivo. Sin este hito, la severidad no tendría consecuencia sobre la urgencia de atención.

### Inventario técnico de implementación

- **Introduce:** registro de incidente con dueño, prioridad derivada de severidad y acción inicial.
- **Aplica en nuevo caso:** la alerta de deriva de entrada de P422 como disparador.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Alerta de deriva → incidente | H01 | Alerta sobre `alcohol` | Alerta escrita a mano; no consume P422. |
| Prioridad por severidad | H02 | `high` → `P1`; otra → `P2` | Id constante; sin cierre ni causa. |

### Relación técnica con actividades anteriores

Nueva aplicación del monitoreo de P422: de detectar a responder. Frente a P446 (runbook), P447 abre un incidente pero no remite a ningún procedimiento; P446 usa `incident-002` y P447 `incident-001`, sin relación de artefactos. Posible solapamiento P446/P447 en «respuesta operativa» que requiere decisión posterior de curso. La vuelta al caso de vinos rompe la continuidad del caso de fábricas usado en P443, P444, P448, P450–P452 y P454.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Alerta del caso de vinos | S01 | `implementation/productos/P447_incident_response/data/monitoring_alert.json`; `implementation/productos/P422_model_monitoring/submission/monitoring_report.json` | Relación por nombre de variable, no por artefacto. |
| H02 — Prioridad por severidad | S02, S03, S04 | `implementation/productos/P447_incident_response/professor/main.py`: `build_incident`; `implementation/productos/P447_incident_response/professor/test_main.py`; `implementation/productos/P447_incident_response/submission/incident.json` | Dueño y acción fijos en el código. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Alerta de entrada | `data/monitoring_alert.json` | Escrita a mano; caso de vinos. |
| S02 | Construcción del incidente | `professor/main.py` | Id, dueño y acción constantes. |
| S03 | Incidente entregado | `submission/incident.json` | Sólo estado `open`. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: prioridad y dueño; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** lee la alerta, construye el incidente, lo persiste e imprime.
- **`submission/`:** `incident.json`.
- **Pruebas:** las de profesor verifican prioridad según severidad, dueño y estado; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C04` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P422:** la noción de alerta por variable desplazada; ningún artefacto.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P447 mapea `productos.C04` y `productos.C05`; C05 nombra «incidentes» y se sostiene. C04 (uso responsable) sólo por la asignación de dueño. El producto operado es el modelo de calidad de vinos de P420 y P422, identificable por la variable de la alerta, lo que mantiene la conexión con una capacidad analítica aunque sin consumir sus artefactos.
