# P307 — Decisión informada por pronósticos: pedido semanal con guardia de servicio

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P307_decision_informada_por_pronosticos/`.

### Preguntas analíticas actuales

- ¿Qué cantidad debe pedir cada semana la tienda para equilibrar valor esperado y nivel de servicio ante un pronóstico incierto?

El «pronóstico» llega como tres escenarios discretos de demanda (`forecast_scenarios.csv`: 80, 110 y 150 con 0,25 / 0,50 / 0,25); no se construye ni se valida un modelo de pronóstico. `order_options.csv` limita las cantidades candidatas a esos mismos tres valores, con costo unitario 12, precio 25 y costo de disposición 2 por sobrante. `policy_contract.csv` guarda como dato los parámetros de gobierno: cadencia semanal, dueño `inventory_planner`, probabilidad máxima de quiebre 0,25, aprobación requerida y gatillo de revisión. La procedencia no está documentada. El producto es una fila de política de pedido con su evaluación.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** cantidad semanal de pedido; dueño declarado `inventory_planner`, con aprobación requerida.
- **Producto terminal:** `order_policy.csv` (cadencia, dueño, cantidad seleccionada, valor esperado, probabilidad de quiebre, nivel de servicio, aprobación y gatillo) y `order_evaluation.csv` (tres cantidades evaluadas).
- **Uso y límite:** permite mostrar cómo una guardia de servicio filtra cantidades antes de maximizar valor esperado. No hay excepción, métrica de resultado observado ni sensibilidad; las cantidades candidatas coinciden con los escenarios, y el nivel de servicio se mide como probabilidad de no quiebre, no como fracción de demanda atendida.
- **Disciplinas contribuyentes:** evaluación por escenarios de un problema tipo vendedor de periódicos con pandas; no hay modelo predictivo ni optimizador.

### Highlights de contribución

- **H01 — Lee el pronóstico como distribución de escenarios y las reglas de gobierno como datos:** el pronóstico es una tabla de escenarios con probabilidad, y la guardia, el dueño y el gatillo se cargan de `policy_contract.csv` en lugar de fijarse en código. La particularidad del caso —escenarios discretos y cantidades candidatas iguales a ellos— hace que el quiebre sólo pueda tomar los valores 0,75, 0,25 o 0. Sin este hito, el pronóstico se trataría como un único valor puntual y los parámetros de gobierno quedarían ocultos en la lógica.
- **H02 — Evalúa cada cantidad por valor esperado y riesgo de quiebre:** `evaluate_order_options` calcula vendidas, sobrantes y valor por escenario, y agrega valor esperado y probabilidad de quiebre: 80 → 1.040 y 0,75; 110 → 1.227,5 y 0,25; 150 → 937,5 y 0 (`order_evaluation.csv`). Primera aparición en el curso de un intercambio explícito entre valor y servicio con costo de sobrante; sin este hito, pedir más parecería siempre más seguro y pedir lo esperado, siempre óptimo.
- **H03 — Filtra por la guardia de servicio antes de maximizar:** `select_order_policy` conserva cantidades con quiebre ≤ 0,25 y elige 110 (`order_policy.csv`). Reutiliza el patrón de P300 con una restricción probabilística; el límite es que 110 también es el máximo sin restricción y queda exactamente en el borde de la guardia, de modo que la guardia no cambia la decisión con estos datos.
- **H04 — Persiste una política de una fila con cadencia, aprobación y gatillo:** la prueba exige una sola fila y siete columnas de decisión. Sin este hito, la cantidad seleccionada no llevaría su contexto de gobierno.

### Inventario técnico de implementación

- **Introduce:** evaluación por escenarios con `clip` para vendidas y sobrantes; probabilidad de quiebre y nivel de servicio por cantidad.
- **Introduce:** parámetros de gobierno como archivo de datos (`policy_contract.csv`).
- **Reutiliza:** filtrar factibles → maximizar (P300, P302); separación `professor/main.py` + notebook.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Escenarios como insumo | H01 | Tres escenarios con probabilidad | No hay modelo ni error de pronóstico. |
| Valor vs servicio | H02–H03 | Valor esperado; quiebre ≤ 0,25 | Tres candidatas; guardia no activa como discriminante. |
| Política persistida | H04 | `order_policy.csv` | Sin excepción, monitoreo ni registro de resultados. |

### Relación técnica con actividades anteriores

Misma técnica que P300/P302 (evaluar alternativas fijas, filtrar por restricción, maximizar) aplicada a inventario con incertidumbre por escenarios; P304 ya había evaluado capacidad bajo escenarios discretos con mayor profundidad (valor marginal, regla por solicitud, sensibilidad). Posible duplicación técnica con P300/P302 y solapamiento con P304 que requiere decisión posterior de curso; el aporte distintivo es el intercambio valor–servicio con costo de sobrante.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Escenarios y gobierno como datos | S01 | `implementation/prescriptiva/P307_decision_informada_por_pronosticos/data/forecast_scenarios.csv`; `data/order_options.csv`; `data/policy_contract.csv` | Procedencia no documentada; escenarios dados. |
| H02 — Valor y quiebre | S02 | `implementation/prescriptiva/P307_decision_informada_por_pronosticos/professor/main.py`: `evaluate_order_options`; `implementation/prescriptiva/P307_decision_informada_por_pronosticos/submission/order_evaluation.csv` | Quiebre como probabilidad de escenario, no demanda insatisfecha. |
| H03 — Guardia antes de maximizar | S02, S03 | `professor/main.py`: `select_order_policy`; `implementation/prescriptiva/P307_decision_informada_por_pronosticos/submission/order_policy.csv` | La guardia coincide con el óptimo sin restricción. |
| H04 — Política persistida | S03, S04 | `submission/order_policy.csv`; `implementation/prescriptiva/P307_decision_informada_por_pronosticos/tests/test_activity.py` | Verifica forma, no la cantidad elegida. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Escenarios, opciones y parámetros de gobierno | `data/forecast_scenarios.csv`, `data/order_options.csv`, `data/policy_contract.csv` | Tres escenarios; candidatas = escenarios; sin procedencia. |
| S02 | Evaluación y selección | `professor/main.py`: `evaluate_order_options`, `select_order_policy` (y alias `evaluate`) | Guardia en igualdad con la opción elegida. |
| S03 | Producto | `submission/order_policy.csv`, `submission/order_evaluation.csv`; `submission/order_comparison.csv` | `order_comparison.csv` no lo produce el código actual. |
| S04 | Pruebas | `tests/test_activity.py` | Existencia, una fila y columnas. |
| S05 | Notebook e interfaz | `professor/notebook.ipynb` (dos celdas, importa `main` desde `src/`); `src/` sólo con `.gitkeep` | Sin evidencia visual; `main.py` está en `professor/`. |

### Contrato de evidencia actual

- **Notebook o código:** el notebook tiene dos celdas que llaman `main()` y muestran `order_policy.csv`; toda la lógica está en `professor/main.py`.
- **`submission/`:** `order_evaluation.csv` y `order_policy.csv` (110 unidades, 1.227,5 de valor esperado, quiebre 0,25, servicio 0,75); además `order_comparison.csv`, artefacto sin productor en el código actual.
- **Pruebas:** `test_01` exige `order_policy.csv`; `test_02` exige una fila y siete columnas; no verifican valores.
- **Trazabilidad:** P307 mapea `prescriptiva.C01`–`C05`.

### Dependencias en la secuencia

- **Recibe de P300/P302:** patrón filtrar factibles → maximizar; de P304, evaluación por escenarios discretos (práctica, no artefacto).
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P307 está mapeada a las cinco capacidades (`prescriptiva.C01`–`C05`). La evidencia sostiene C01 parcialmente (cadencia, dueño, guardia y gatillo, sin excepciones ni objetivo explícito en el contrato) y C02 (distingue escenarios de pronóstico de la decisión). C03 (validación frente a líneas base, sensibilidad, demoras) y C05 (monitoreo y recalibración) no se evidencian más allá de un gatillo textual; C04 se reduce a `approval_required = yes`. Frente a `activity-architecture.md` («política de pedido por escenarios y servicio») el núcleo existe, pero la trazabilidad excede lo implementado. El producto de Analytics es una recomendación de pedido con guardia de servicio; no alcanza una política gobernada con excepción y monitoreo.
