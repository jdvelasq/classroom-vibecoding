# P303 — Políticas y supervisión humana: aprobar, rechazar o escalar solicitudes

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P303_politicas_y_supervision_humana/`.

### Preguntas analíticas actuales

- ¿Qué recomendación recurrente debe emitirse para cada solicitud de crédito, cuándo debe escalarse y quién conserva la autoridad de decisión?

`data/applications.csv` contiene seis solicitudes (filas = solicitud; columnas = probabilidad de incumplimiento ya estimada, monto solicitado y documentación completa). La probabilidad se trata como evidencia dada: no se estima ni se valida. La procedencia no está documentada. Por primera vez en el curso la unidad de decisión es la **entidad individual** (cada solicitud) y la cadencia es «cada solicitud recibida». El producto es una tabla de decisiones con acción, razón y autoridad por solicitud, más un contrato versionado.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** recomendación por solicitud de crédito; autoridades declaradas: analista de crédito, supervisor de crédito y gestor de documentación.
- **Producto terminal:** `review_policy.csv` (decisión por solicitud con versión, cadencia, plazo, modo, acción, razón, autoridad, gatillo y resultado a monitorear) y `policy_contract.json` (acciones posibles, salvaguardas, gatillo y resultados a monitorear).
- **Uso y límite:** permite mostrar cómo una regla con precedencias enruta cada caso a una acción y a una autoridad. No justifica los umbrales (0,08, 0,30 y 10.000) ni los declara en el contrato; no evalúa consecuencias ni errores de la regla; no automatiza la decisión crediticia.
- **Disciplinas contribuyentes:** reglas condicionales vectorizadas con pandas; la probabilidad de incumplimiento proviene de un modelo predictivo no presente.

### Highlights de contribución

- **H01 — Enruta cada solicitud a una acción y a una autoridad por precedencia:** `apply_review_policy` aplica primero documentación incompleta (escala al gestor de documentación), después monto superior al límite delegable (escala al supervisor) y sólo entonces el riesgo (aprobar si < 0,08, rechazar si > 0,30, escalar en la franja intermedia). Primera regla por entidad en el curso (P300–P302 eligen entre alternativas agregadas); sin este hito, la autoridad humana sería un campo fijo y no una consecuencia de la situación.
- **H02 — Separa el puntaje predictivo de la acción mediante límites delegables:** con los datos visibles, A01 (0,04; 4.000) recibe «recomendar_aprobación», A02 y A03 (0,11 y 0,19) se escalan por «riesgo intermedio» al analista y A04 (0,28; 15.000) se escala al supervisor por monto (`review_policy.csv`). La particularidad del dataset —probabilidad, monto y documentación coexisten por solicitud— hace que una misma probabilidad no determine la acción. Sin este hito, el umbral de riesgo parecería suficiente para decidir.
- **H03 — Registra cada recomendación con su razón y versión:** cada fila lleva `policy_version` «P303-v1», `reason`, `human_authority`, `review_trigger` y `outcome_to_monitor`. Primera aparición de un registro de decisión por entidad con versión de política; sin él, no podría reconstruirse por qué se escaló un caso.
- **H04 — Declara salvaguardas no negociables en el contrato:** «no se automatiza la decisión crediticia», «la documentación incompleta siempre escala» y «los montos superiores al límite delegable requieren supervisor». La prueba exige que `safeguards` y `review_trigger` no estén vacíos. Sin este hito, la supervisión humana quedaría implícita.

### Inventario técnico de implementación

- **Introduce:** regla por entidad con máscaras booleanas y precedencia explícita; enrutamiento a autoridades distintas; versión de política en cada registro.
- **Extiende:** contrato JSON de P302 con lista de acciones posibles y resultados a monitorear.
- **Reutiliza:** separación `professor/main.py` + notebook; persistencia en `submission/`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Aprobar / rechazar / escalar | H01–H02 | Precedencia documentación → monto → riesgo | Umbrales sin justificación ni sensibilidad. |
| Autoridad por motivo | H01, H03 | `human_authority` por fila | No se registra la decisión humana final. |
| Registro versionado | H03 | `policy_version` en `review_policy.csv` | Una sola versión; sin historial. |
| Salvaguardas | H04 | `safeguards` en el contrato | Declarativas. |

### Relación técnica con actividades anteriores

Nuevo mecanismo al servicio del mismo producto (política gobernada): P300 y P302 seleccionan una alternativa agregada; P303 aplica una regla a cada solicitud. Comparte con P300 el modo «recomendación con aprobación humana», pero lo diferencia por motivo y autoridad. No duplica actividades previas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Precedencia y autoridad | S02 | `implementation/prescriptiva/P303_politicas_y_supervision_humana/professor/main.py`: `apply_review_policy` | Umbrales fijos en código; no aparecen en el contrato. |
| H02 — Puntaje vs acción | S01, S02, S03 | `implementation/prescriptiva/P303_politicas_y_supervision_humana/data/applications.csv`; `implementation/prescriptiva/P303_politicas_y_supervision_humana/submission/review_policy.csv` | Sólo A01–A04 son visibles completas en el volcado; no se puede confirmar que alguna solicitud reciba «recomendar_rechazo». |
| H03 — Registro versionado | S03 | `submission/review_policy.csv`: `policy_version`, `reason`, `human_authority` | No registra la decisión humana ni el resultado. |
| H04 — Salvaguardas | S03, S04 | `professor/main.py`: `policy_contract`; `implementation/prescriptiva/P303_politicas_y_supervision_humana/submission/policy_contract.json`; `implementation/prescriptiva/P303_politicas_y_supervision_humana/tests/test_activity.py` | La prueba exige campos no vacíos, no su contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset de solicitudes | `data/applications.csv` | Seis filas; probabilidad dada; procedencia no documentada. |
| S02 | Regla y precedencias | `professor/main.py`: `apply_review_policy` | Umbrales 0,08 / 0,30 / 10.000 sin derivación. |
| S03 | Producto/registro y contrato | `submission/review_policy.csv`, `submission/policy_contract.json` | Contrato sin umbrales numéricos ni límite delegable explícito. |
| S04 | Pruebas | `tests/test_activity.py` | Columnas y campos no vacíos. |
| S05 | Interfaz notebook–código | `professor/notebook.ipynb` (importa desde `src/`); `src/` sólo con `.gitkeep` | `main.py` está en `professor/`. |

### Contrato de evidencia actual

- **Notebook o código:** tres celdas: importación, aplicación de la regla con escritura de artefactos y vista de acción/razón/autoridad.
- **`submission/`:** `review_policy.csv` (seis solicitudes) y `policy_contract.json`.
- **Pruebas:** exigen ambos archivos, seis columnas en la política y `safeguards`/`review_trigger` no vacíos; no verifican la acción asignada a cada solicitud.
- **Trazabilidad:** P303 mapea `prescriptiva.C01` y `C04`.

### Dependencias en la secuencia

- **Recibe de P302:** contrato JSON con salvaguardas y gatillo; de P300, el modo de recomendación con aprobación humana.
- **Habilita para P306:** la regla por entidad con registro y autoridad reaparece en `decision_register.csv` de P306 (estado `review_required`/`pending_approval`); la relación es de práctica, no de artefacto.

## Trazabilidad y auditoría

P303 está mapeada a `prescriptiva.C01` y `C04`; la evidencia sostiene sobre todo C04 (modo proporcional, escalamiento por excepción y trazabilidad por decisión) y C01 (cadencia, acciones, salvaguardas y gatillo). Coincide con el producto previsto («regla de aprobar, rechazar o escalar»). El producto de Analytics es una regla de decisión por entidad gobernada por autoridad humana; conecta contexto observable con acción, aunque sin validación de umbrales, consecuencias ni monitoreo ejecutado.
