# P314 — Cuadrillas de respuesta a tormentas: reserva con recurso y criterio robusto

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P314_storm_response_crews/`.

### Preguntas analíticas actuales

- ¿Cuántas cuadrillas regulares reservar antes de una tormenta y cuántas de emergencia activar después de observar los daños?
- ¿Qué cambia si, además del costo esperado, se exige continuidad del servicio en todos los escenarios evaluados?

Usa cuatro escenarios de tormenta (`storm_scenarios.csv`: leve, moderada, severa, extrema con probabilidad 0.40, 0.30, 0.20, 0.10; carga de reparación 6, 12, 18, 24; capacidad de emergencia 6, 8, 8, 8) y parámetros de costo (`policy_parameters.csv`: regular 5, emergencia 9, interrupción 25; reservas candidatas 0–26). El notebook declara el caso sintético «para controlar escenarios, costos y capacidad». El producto es una política robusta: reserva de 16 cuadrillas, acción por escenario con autoridad y escalamiento, y contrato con plazos y monitoreo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** reserva previa a cada alerta (confirmada 72 horas antes, gerencia de operaciones) y activación de emergencia tras clasificar el escenario (jefatura de respuesta, dentro de 2 horas).
- **Producto terminal:** `storm_response_policy_contract.json` y `storm_response_policy_actions.csv` (acción, autoridad y escalamiento por escenario para x=16), respaldados por evaluación de reservas, acciones por escenario de ambas políticas y sensibilidad a la probabilidad extrema.
- **Uso y límite:** muestra el valor de poder reaccionar y el costo de garantizar servicio en el peor escenario evaluado. La garantía depende de que el escenario observado coincida con uno de los cuatro modelados; la clasificación del escenario se supone inmediata y correcta. Los costos son unidades del caso.
- **Disciplinas contribuyentes:** programación estocástica de dos etapas resuelta por enumeración con regla de recurso cerrada; criterio robusto lexicográfico. No hay solver.

### Highlights de contribución

- **H01 — Deriva la acción de segunda etapa del orden de costos:** `recourse_actions` usa capacidad regular, luego emergencia hasta su límite y sólo después acepta interrupción, justificado por `c_regular < c_emergency < c_disruption` (verificado con `assert`). Primera decisión en dos etapas del curso (P304–P313 deciden una sola vez antes de la incertidumbre); sin este hito, «reaccionar después de observar» no tendría representación.
- **H02 — Cuantifica el valor de la flexibilidad:** compara la política estática (sin recurso) con la adaptativa esperada sobre los mismos escenarios; el notebook verifica óptimos x=18 y x=12 y un ahorro verificado con `assert`. `reserve_evaluation.csv` persiste ambas curvas (p. ej. x=0: 184,8 adaptativo vs. 300 estático). Sin este hito, el recurso de emergencia sería un detalle operativo y no una razón para reservar menos.
- **H03 — Introduce un criterio robusto de servicio con desempate por mínimo compromiso:** minimiza primero la carga sin cubrir en el peor escenario y luego x; la meseta de cero interrupción empieza en 16 (15 deja 1 sin cubrir). Particularidad del dataset: la capacidad de emergencia se satura en 8 a partir de «moderada», de modo que 16 + 8 = 24 cubre exactamente la carga extrema; sin este hito, la exigencia de continuidad no tendría un criterio distinto del costo esperado.
- **H04 — Muestra que la misma reserva produce acciones distintas por escenario:** `scenario_actions.csv` persiste, para x=12, emergencia 6 en severa y 8 con 4 sin cubrir en extrema (costo 232); `storm_response_policy_actions.csv`, para x=16, emergencia 0, 0, 2 y 8 sin carga sin cubrir. Sin este hito, la política se reduciría a un número de reserva.
- **H05 — Contrasta sensibilidad del criterio esperado y del robusto:** `extreme_probability_sensitivity.csv` muestra reserva esperada 12, 12, 16, 16 para probabilidad extrema 0.05–0.30 y robusta 16 constante. Sin este hito, no se vería que el criterio robusto no depende de probabilidades y que el esperado converge a él cuando la cola pesa más.
- **H06 — Asigna autoridad y escalamiento por etapa y escenario:** el contrato separa autoridad previa (gerencia aprueba 16) y posterior (jefatura despliega), fija plazo de 2 horas, guarda de servicio, excepción «carga observada superior a reserva más emergencia» con escalamiento al comando de incidente y gatillo de revisión «dos tormentas consecutivas con activación de emergencia o cualquier escalamiento». Extiende los contratos de P309/P313 a dos momentos de decisión; sin este hito, la reserva robusta no tendría operación ni excepción.

### Inventario técnico de implementación

- **Introduce:** decisión de dos etapas con recurso; regla de recurso en forma cerrada; criterio robusto min-max con desempate lexicográfico; valor de la flexibilidad; prima de robustez.
- **Extiende:** sensibilidad de probabilidades (P304, P309) con redistribución proporcional del resto; comparación de criterios de decisión sobre los mismos escenarios.
- **Reutiliza:** bloque `DECISION MODEL`; planeador PNG de cuatro paneles; verificación final con `assert`.
- **Aplica en nuevo caso:** enumeración de una decisión entera sobre escenarios discretos (P309, P311).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Dos etapas con recurso | H01–H02, H04 | Reserva previa + emergencia posterior; estático vs. adaptativo | Recurso en forma cerrada; cuatro escenarios. |
| Criterio robusto | H03, H05 | Min peor carga sin cubrir; desempate min x | Robusto sólo frente a escenarios modelados. |
| Política por escenario | H04, H06 | Acción, autoridad y escalamiento por escenario | Clasificación del escenario supuesta perfecta. |

### Relación técnica con actividades anteriores

Nuevo método al servicio del mismo producto: P309, P311 y P313 deciden capacidad antes de la incertidumbre; P314 añade una acción posterior a la observación y un criterio robusto. El notebook menciona «W12 preguntó… W13 agrega…» como continuidad con una actividad previa de decisión anticipada; por contenido corresponde a P313, pero la numeración heredada no está documentada. **Posible duplicación parcial:** la evaluación por escenarios discretos es la misma familia que P307/P309/P311; la novedad distinguible es el recurso de segunda etapa y el criterio robusto, no la evaluación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Regla de recurso | S02 | `implementation/prescriptiva/P314_storm_response_crews/professor/notebook.ipynb`: `recourse_actions`, bloque `DECISION MODEL`, `assert` de orden de costos | Regla válida sólo para ese orden de costos y sin plazos internos. |
| H02 — Valor de flexibilidad | S02, S03 | `implementation/prescriptiva/P314_storm_response_crews/submission/reserve_evaluation.csv`; notebook: `policy_summary`, ahorro | El ahorro y la tabla `policy_summary` no se persisten como tales. |
| H03 — Criterio robusto | S01, S03 | `implementation/prescriptiva/P314_storm_response_crews/data/storm_scenarios.csv`; notebook: meseta x=15/16 | La prima de robustez se calcula en notebook, no en `submission/`. |
| H04 — Acciones por escenario | S04 | `implementation/prescriptiva/P314_storm_response_crews/submission/scenario_actions.csv`; `implementation/prescriptiva/P314_storm_response_crews/submission/storm_response_policy_actions.csv` | Acciones para escenarios modelados, no para cargas intermedias. |
| H05 — Sensibilidad comparada | S03 | `implementation/prescriptiva/P314_storm_response_crews/submission/extreme_probability_sensitivity.csv` | Sólo varía la probabilidad extrema. |
| H06 — Autoridad por etapa | S04, S05 | `implementation/prescriptiva/P314_storm_response_crews/submission/storm_response_policy_contract.json`; `implementation/prescriptiva/P314_storm_response_crews/tests/test_activity.py` | No se justifica en el producto por qué se adopta el criterio robusto sobre el esperado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Escenarios y costos | `data/storm_scenarios.csv`, `data/policy_parameters.csv` | Sintético; cuatro escenarios; emergencia saturada en 8. |
| S02 | Modelo de dos etapas | Notebook: `static_costs`, `recourse_actions`, `adaptive_costs` | Recurso cerrado; enumeración 0–26. |
| S03 | Criterios y sensibilidad | `reserve_evaluation.csv`, `extreme_probability_sensitivity.csv`; notebook | Prima y ahorro no persistidos. |
| S04 | Política y contrato | `storm_response_policy_actions.csv`, `storm_response_policy_contract.json`, `scenario_actions.csv`, `storm_response_capacity_planner.png` | Selección del criterio robusto sin argumento persistido. |
| S05 | Pruebas | `tests/test_activity.py` | Exige al menos un archivo cualquiera en `submission/`. |
| S06 | Secuencia y referencias heredadas | Notebook: celda «W12/W13» | Numeración ajena a P3xx. |

### Contrato de evidencia actual

- **Notebook o código:** evalúa políticas estática, adaptativa esperada y adaptativa robusta; verifica restricciones de balance y capacidad; calcula ahorro, prima y sensibilidad; construye contrato y acciones.
- **`submission/`:** `reserve_evaluation.csv`, `scenario_actions.csv`, `storm_response_policy_actions.csv`, `storm_response_policy_contract.json`, `extreme_probability_sensitivity.csv`, `storm_response_capacity_planner.png`.
- **Pruebas:** sólo exigen que exista al menos un artefacto distinto de `.gitkeep`; no verifican la política, el contrato ni los nombres de archivo.
- **Trazabilidad:** P314 mapea `prescriptiva.C02`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P313:** pregunta de decisión anticipada bajo incertidumbre, explícitamente retomada en la celda «W12 preguntó…» (correspondencia por contenido, no documentada). De P309, práctica de mostrar riesgo residual del plan esperado.
- **Habilita para Pyyy:** no evidenciada dentro de P315.

## Trazabilidad y auditoría

P314 está mapeada a `prescriptiva.C02`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C02 (acción por escenario desde datos observables), C03 (comparación de criterios, sensibilidad) y C04 (autoridad pre y post evento, excepción) se sostienen; C05 por gatillo de revisión y métricas declaradas. Coincide con «política de reserva y despliegue por escenario». El producto de Analytics es una política de dos etapas con guarda de servicio y escalamiento; la formulación estocástica contribuye. Límites: robustez sólo frente a cuatro escenarios, clasificación supuesta y prueba que no verifica el producto.
