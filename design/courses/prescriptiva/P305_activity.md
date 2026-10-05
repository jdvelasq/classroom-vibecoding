# P305 — Tax Inspections: priorización semanal de inspecciones bajo capacidad

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P305_tax_inspections/`.

### Preguntas analíticas actuales

- ¿A qué contribuyentes auditar con una capacidad limitada de días de inspección para maximizar el recaudo esperado sin poder revisar a todos?
- ¿Por qué una selección por riesgo, por recuperación o por eficiencia no basta?

El notebook declara un **caso sintético**: `data/taxpayers.csv` tiene doce contribuyentes (filas = contribuyente; columnas = probabilidad de incumplimiento dada, monto recuperable condicionado al incumplimiento y jornadas que exige su inspección) y `data/audit_capacity.csv` fija 14 jornadas. Las inspecciones son indivisibles y de duración heterogénea; el notebook afirma que no hay características protegidas y que el objetivo se limita a recuperación esperada. El producto es una selección semanal recomendada, con comparación de reglas, sensibilidad a capacidad, registro pendiente de supervisor y contrato.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** programar inspecciones de la semana siguiente; autoridad declarada: supervisor de fiscalización aprueba o rechaza.
- **Producto terminal:** `inspection_policy.json` (cadencia semanal, plazo, entradas, acción, objetivo, restricción, autoridad, excepciones, gatillos y selección), `inspection_recommendations.csv` (registro con estado «pendiente de supervisor»), `inspection_decisions.csv`, `portfolio_comparison.csv`, `capacity_sensitivity.csv` y `tax_inspection_planner.png`.
- **Uso y límite:** permite justificar una cartera concreta y sus exclusiones bajo una capacidad dada. El notebook advierte que «el caso no representa una política fiscal real» y que una política real exige legalidad, equidad, debido proceso, disuasión, muestreo e incertidumbre; nada de ello se modela. Las probabilidades son insumos dados.
- **Disciplinas contribuyentes:** problema de mochila binaria resuelto por enumeración y con PuLP/HiGHS; sirven a la selección y a su explicación.

### Highlights de contribución

- **H01 — Combina riesgo, monto y esfuerzo en un valor por acción indivisible:** calcula `expected_recovery = risk_probability × recoverable_amount` y `expected_recovery_per_day`, y los muestra en un gráfico de riesgo vs recuperación con tamaño por jornadas. La particularidad del dataset —monto condicionado al incumplimiento y duración entera y heterogénea— impide priorizar por un solo atributo. Sin este hito, se confundiría el contribuyente más probable con la inspección más valiosa.
- **H02 — Contrasta tres reglas de ranking con la misma capacidad:** con la regla «seleccionar si cabe», riesgo logra 980, recuperación 2.360 y eficiencia 2.480, todas usando 14 de 14 jornadas (`portfolio_comparison.csv`). Sin este hito, agotar la capacidad parecería equivalente a aprovecharla bien.
- **H03 — Obtiene la cartera exacta y la verifica con dos métodos:** formula la mochila binaria, la resuelve por enumeración de 2¹² subconjuntos y con PuLP/HiGHS, y exige coincidencia de objetivo y selección y unicidad del óptimo: T06, T07 y T08, 14 jornadas, 2.610 (`inspection_policy.json`). Primera aparición de un solver en el curso; sin este hito, el estudiante no vería que un ranking no garantiza la mejor combinación indivisible.
- **H04 — Explica las exclusiones de la cartera recomendada:** compara T05 + T09 con T07 + T08 para las mismas nueve jornadas y muestra que la mejor cartera con T04 (2.360) queda por debajo del óptimo; `gap_to_optimum` cuantifica la distancia de cada regla (1.630, 250, 130). Sin este hito, la recomendación sería correcta pero no explicable al supervisor.
- **H05 — Muestra que más capacidad cambia la composición, no sólo el tamaño:** con 12, 14 y 16 jornadas las carteras óptimas son T05;T06, T06;T07;T08 y T05;T06;T07, con 2.150, 2.610 y 3.050 (`capacity_sensitivity.csv`). Sin este hito, se supondría que ampliar capacidad sólo agrega casos a la lista previa.
- **H06 — Convierte la solución en una recomendación semanal supervisada:** el contrato declara que la política «recomienda, no inicia una fiscalización automáticamente», con excepciones por datos inválidos, capacidad distinta o restricción legal/de equidad identificada por el supervisor, y gatillos de revisión; `inspection_recommendations.csv` registra cada caso como «pendiente de supervisor». Extiende el registro de P303 a una cartera bajo capacidad; sin este hito, el óptimo matemático se presentaría como decisión.

### Inventario técnico de implementación

- **Introduce:** valor esperado por acción; reglas codiciosas con omisión si no cabe; enumeración exhaustiva con `itertools.product`; modelo binario en PuLP resuelto con HiGHS; verificación cruzada y unicidad del óptimo.
- **Introduce:** sensibilidad discreta a capacidad con análisis de entradas/salidas de la cartera.
- **Extiende:** contrato JSON y registro de decisiones con estado de aprobación (P302–P303); figura compuesta persistida (P304).
- **Reutiliza:** validación de datos con `assert`; comparación con líneas base bajo igual capacidad (P301, P304).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Valor por acción indivisible | H01 | p × monto; valor por jornada | Probabilidades dadas; caso sintético. |
| Reglas vs óptimo | H02–H04 | Tres rankings; enumeración y HiGHS; brecha al óptimo | Doce contribuyentes; una restricción. |
| Sensibilidad a capacidad | H05 | Carteras no anidadas 12/14/16 | No se modela incertidumbre de probabilidades. |
| Recomendación supervisada | H06 | Contrato y registro pendiente | Sin equidad, disuasión ni debido proceso modelados. |

### Relación técnica con actividades anteriores

Misma estructura de producto que P304 (comparación con alternativas, sensibilidad, contrato, figura persistida), con un nuevo método: selección combinatoria bajo capacidad con solver. Frente a P300/P302, la acción ya no se elige en un menú dado: se construye la cartera. Con P303 comparte el registro con aprobación pendiente. No hay duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Valor por acción indivisible | S01, S02 | `implementation/prescriptiva/P305_tax_inspections/data/taxpayers.csv`; `implementation/prescriptiva/P305_tax_inspections/professor/notebook.ipynb`: `expected_recovery`, `expected_recovery_per_day`, gráfico; `implementation/prescriptiva/P305_tax_inspections/submission/inspection_decisions.csv` | Probabilidad tomada como dada; sin incertidumbre. |
| H02 — Reglas con igual capacidad | S02 | notebook: `risk_order`, `value_order`, `efficiency_order`; `implementation/prescriptiva/P305_tax_inspections/submission/portfolio_comparison.csv` | Regla «si cabe» específica; no agota las heurísticas posibles. |
| H03 — Cartera exacta verificada | S03 | notebook: enumeración, `pulp.LpProblem`, `pulp.HiGHS`, aserciones; `implementation/prescriptiva/P305_tax_inspections/submission/inspection_policy.json` | Óptimo para estos datos y 14 jornadas. |
| H04 — Explicación de exclusiones | S03, S05 | notebook: `exchange`, `best_with_t04`; `submission/portfolio_comparison.csv`; `implementation/prescriptiva/P305_tax_inspections/submission/tax_inspection_planner.png` | El texto explicativo de la figura está escrito a mano en el notebook. |
| H05 — Composición no anidada | S04 | notebook: `capacity_sensitivity`, tabla de entradas/salidas; `implementation/prescriptiva/P305_tax_inspections/submission/capacity_sensitivity.csv` | Tres niveles; no define cuándo cambiar la capacidad. |
| H06 — Recomendación supervisada | S05 | notebook: `policy_contract`, `decision_register`; `submission/inspection_policy.json`; `implementation/prescriptiva/P305_tax_inspections/submission/inspection_recommendations.csv` | Declarativo; no registra decisión del supervisor ni resultado observado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético | `data/taxpayers.csv`, `data/audit_capacity.csv` | Doce contribuyentes; una semana; sin atributos protegidos. |
| S02 | Representación de valor y reglas de ranking | Notebook: valor esperado, valor por jornada, tres órdenes | Regla codiciosa «si cabe». |
| S03 | Modelo de selección | Notebook: enumeración, PuLP/HiGHS, intercambio, mejor con T04 | Una restricción de capacidad; sin incertidumbre. |
| S04 | Sensibilidad | Notebook: bucle 12/14/16; `capacity_sensitivity.csv` | Sólo capacidad. |
| S05 | Producto/gobierno | `inspection_policy.json`, `inspection_recommendations.csv`, `inspection_decisions.csv`, `portfolio_comparison.csv`, `tax_inspection_planner.png` | Sin métrica de monitoreo explícita fuera de los gatillos. |
| S06 | Pruebas | `tests/test_activity.py` | Existencia de seis artefactos. |

### Contrato de evidencia actual

- **Notebook o código:** todo en `professor/notebook.ipynb` (requiere `pulp` con HiGHS); valida, compara reglas, resuelve por enumeración y solver, explica, analiza sensibilidad y exporta. Una celda de verificación aparece duplicada.
- **`submission/`:** seis artefactos: decisiones por contribuyente con rangos y selecciones por regla, comparación de carteras, sensibilidad, registro de recomendaciones, contrato JSON y planeador PNG.
- **Pruebas:** `test_01` exige los seis artefactos; no verifica contenido.
- **Trazabilidad:** P305 mapea `prescriptiva.C01`, `C02` y `C04`.

### Dependencias en la secuencia

- **Recibe de P303–P304:** registro de decisiones con estado de aprobación; contrato con gatillos; figura de planeación persistida.
- **Habilita para P306:** el contraste «ranking vs optimizador» se retoma de forma explícita en P306, donde el notebook justifica que ordenar sí es exacto con costo uniforme y capacidad de cardinalidad; relación de práctica, no de artefacto.

## Trazabilidad y auditoría

P305 está mapeada a `prescriptiva.C01`, `C02` y `C04`; la evidencia sostiene las tres (contrato semanal, selección computable desde datos observables por contribuyente, aprobación supervisora y excepciones). Ejerce además sensibilidad a capacidad (afín a C03) sin mapearla. Coincide con el producto previsto («política de inspección bajo capacidad limitada»). El producto de Analytics es una recomendación semanal gobernada; la optimización contribuye y no sustituye la política. Límites: los gatillos no definen umbrales ni métricas de seguimiento y la política se demuestra sobre una sola semana.
