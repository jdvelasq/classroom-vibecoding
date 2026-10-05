# P317 — Flood Protection Investment: inversión anual en protección contra inundación

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P317_flood_protection_investment/`.

### Preguntas analíticas actuales

- ¿Qué inversión anual de protección debe aprobarse para cada nivel de riesgo de inundación, respetando el presupuesto y escalando los casos que no alcanzan el nivel de protección exigido? (pregunta literal de la primera celda).
- ¿Qué altura adicional `h` minimiza la suma del costo anualizado de protección y la pérdida anual esperada, y cómo cambia esa altura con la consecuencia de la inundación `D` y el costo por metro `k`?

El notebook declara un «caso sintético inspirado en la lógica económica de la planeación de diques holandesa; no son datos reales». `data/protection_parameters.csv` contiene siete parámetros en formato largo (`parameter,value`): probabilidad anual base `p0` = 0,01, efectividad `alpha` = 1,0, consecuencia `D` = 500.000.000, costo anualizado por metro `k` = 500.000, altura máxima `h_max` = 6 m, y —visibles en el contrato persistido— presupuesto anual 1.000.000 y probabilidad objetivo 0,001. No hay observaciones: el riesgo es una forma funcional `p(h) = p0·exp(−alpha·h)`. El modelo económico se declara evidencia; el producto es una tabla de acciones por caso de riesgo y un contrato con autoridad ordinaria, escalamiento y monitoreo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** aprobar la altura adicional de protección en cada ciclo anual de capital; el contrato asigna la aprobación ordinaria a «dirección de infraestructura» y los excedentes o la aceptación de riesgo residual a «comité de riesgo y junta de inversión». Roles declarados en un caso sintético.
- **Producto terminal:** `flood_protection_policy_actions.csv` (acción, altura e inversión aprobadas, autoridad y escalamiento por caso de riesgo) gobernado por `flood_protection_policy_contract.json`.
- **Uso y límite:** muestra cómo un óptimo económico se recorta por presupuesto y obliga a escalar cuando la protección aprobada no alcanza el objetivo de probabilidad. Los tres casos de riesgo (0,005; 0,01; 0,02) son valores fijados en el notebook aunque la columna se llame `observed_annual_flood_probability`; no hay incertidumbre sobre parámetros más allá de sensibilidad uno a uno, ni dinámica de construcción.
- **Disciplinas contribuyentes:** optimización no lineal acotada (`scipy.optimize.minimize_scalar`), cálculo de primer y segundo orden y análisis de riesgo económico sirven a la regla de aprobación.

### Highlights de contribución

- **H01 — Trabaja un caso paramétrico, no un conjunto de observaciones:** los datos son siete parámetros en formato largo convertidos a diccionario y validados por dominio, incluida la coherencia `0 < target_annual_probability < p0`. La particularidad del caso es que la probabilidad de inundación es un supuesto funcional y la decisión es una sola variable continua; por eso la validación es de consistencia matemática (convexidad, condición de primer orden) y no de ajuste a datos, y el notebook advierte que el período de retorno «es el inverso de la probabilidad anual; no es un reloj de recurrencia exacta». Sin este hito, el resultado parecería una estimación empírica del riesgo; el límite es que todo hereda la forma funcional supuesta.
- **H02 — Hace visible el trade-off como curva en U antes de optimizar:** evalúa una malla gruesa de 0,5 m y grafica costo de protección creciente, pérdida esperada decreciente y su suma. El mejor punto de malla (2,5 m) queda 9.132,45 por encima del óptimo en `investment_comparison.csv`; el notebook declara que la malla «aproxima el óptimo, pero no lo garantiza» y que no es búsqueda exhaustiva de un espacio continuo. Sin este hito, el óptimo aparecería sin la forma del objetivo que lo justifica.
- **H03 — Compara alturas fijas con un mismo criterio económico:** sin protección adicional (costo total 5.000.000), regla de ingeniería de 1,5 m (1.865.650,80), protección conservadora de 5,0 m (2.533.689,73), mejor punto de malla y óptimo (1.651.292,55), todos persistidos en `investment_comparison.csv` con `gap_vs_optimized`. El notebook aclara que la regla de ingeniería «no es un estándar real declarado». Sin este hito, proteger «mucho» o «según regla» no se contrastaría con su costo.
- **H04 — Elige el método por la estructura matemática:** declara que `h` es continua, que el objetivo contiene `exp(−alpha·h)` y que «PuLP + HiGHS … no es el solver adecuado aquí»; resuelve con `minimize_scalar(method="bounded")` en `[0, h_max]`. Es la única actividad del curso que usa un optimizador no lineal y contrasta con el LP de P316 y P318. Sin este hito, la secuencia sugeriría que todo problema prescriptivo se resuelve con el mismo solver.
- **H05 — Valida el óptimo numérico con teoría:** compara `h*` con la forma cerrada `ln(alpha·D·p0/k)/alpha`, verifica segunda derivada positiva en una malla de 61 puntos, iguala costo marginal y reducción marginal de pérdida esperada y comprueba monotonicidad de probabilidad, costo y pérdida. El óptimo persistido es `h` ≈ 2,3026 m, probabilidad anual ≈ 0,001 y período de retorno ≈ 1.000 años. Sin este hito, la confianza descansaría en `result.success`.
- **H06 — Mide cómo responde el óptimo a consecuencia y costo:** re-resuelve con `D` en 250, 500 y 1.000 millones (alturas persistidas ≈ 1,61; 2,30; 3,00 m) y con `k` en 350.000, 500.000 y 750.000, comprobando en cada caso la forma cerrada y afirmando que `h*` crece con `D` y decrece con `k`. Sin este hito, el óptimo parecería una constante y no una respuesta a supuestos revisables.
- **H07 — Convierte el óptimo económico en regla de aprobación con presupuesto y escalamiento:** fija la altura financiable `annual_budget / k` (2,0 m), calcula para cada caso de riesgo la altura económica, la aprobada, la probabilidad alcanzada y la altura objetivo, y escala si la probabilidad alcanzada supera el objetivo. Persistido: el riesgo reducido aprueba 1,61 m (804.718,96) por dirección de infraestructura; los riesgos de referencia y elevado aprueban 2,0 m (1.000.000) y se elevan al comité de riesgo y junta de inversión. El contrato añade cadencia anual y por estudio actualizado o inundación extrema, plazo de 30 días, prohibición de aceptación silenciosa de riesgo residual y gatillo de desviación de costo superior al 10 %. Sin este hito, el planeador sería sólo evidencia económica, como el propio notebook declara.
- **H08 — Persiste la evidencia económica junto con la política:** guarda curva fina de 0,1 m (`protection_curve.csv`), comparación, sensibilidad, acciones, contrato y planeador. Sin estos artefactos, la regla no sería auditable; la prueba, sin embargo, sólo exige que exista algún archivo en `submission/`.

### Inventario técnico de implementación

- **Introduce:** optimización escalar no lineal acotada con SciPy; validación por forma cerrada, convexidad y condición marginal; período de retorno como transformación de probabilidad; regla de aprobación con tope presupuestal y escalamiento por objetivo de riesgo.
- **Extiende:** comparación con referencias fijas y sensibilidad por re-resolución (P313–P316); escalamiento a comité (P310) con dos niveles de autoridad según presupuesto.
- **Reutiliza:** planeador con `Figure` compuesto antes de mostrarse; contrato JSON; celda final de verificación con valores esperados.
- **Aplica en nuevo caso:** inversión en infraestructura de protección con pérdida esperada.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Modelo paramétrico de riesgo | H01 | `p(h) = p0·exp(−alpha·h)`; siete parámetros validados | Sintético; forma funcional supuesta. |
| Trade-off costo–pérdida | H02–H03 | Curva en U, malla y cuatro referencias fijas | Persistido en `investment_comparison.csv` y `protection_curve.csv`. |
| Optimización no lineal validada | H04–H05 | `minimize_scalar` acotado; forma cerrada; convexidad | Una variable; sin incertidumbre paramétrica. |
| Sensibilidad a supuestos | H06 | Re-resolución con `D` y `k` | Uno a uno; tres valores por parámetro. |
| Regla presupuestal con escalamiento | H07–H08 | Acciones por caso de riesgo; contrato con autoridad y gatillos | Casos de riesgo fijados en código; prueba mínima. |

### Relación técnica con actividades anteriores

P317 repite la plantilla de P313–P316 (referencias, modelo en texto, solver, validación, sensibilidad, planeador, contrato), pero introduce un método distinto al servicio del mismo tipo de producto: optimización no lineal continua en lugar de enumeración, simulación o LP. Con P310 comparte el escalamiento de una inversión a un comité, sin artefactos comunes. La transición del planeador económico a la tabla de acciones por caso de riesgo es la principal adición de producto. En los tres casos persistidos `target_protection_m` coincide con `economic_protection_m`: con estos parámetros el óptimo económico alcanza exactamente la probabilidad objetivo, de modo que el escalamiento depende sólo del presupuesto; el notebook no comenta esta coincidencia.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Caso paramétrico | S01, S02 | `implementation/prescriptiva/P317_flood_protection_investment/data/protection_parameters.csv`; `implementation/prescriptiva/P317_flood_protection_investment/professor/notebook.ipynb`: celdas de carga, `assert` y funciones de riesgo | Sintético; procedencia sólo como «inspirado en» la lógica holandesa. |
| H02 — Curva en U y malla | S03 | Notebook: `protection_grid`, gráfico de forma; `implementation/prescriptiva/P317_flood_protection_investment/submission/investment_comparison.csv` | La figura de forma no se persiste; sí el planeador. |
| H03 — Referencias fijas | S03, S07 | `implementation/prescriptiva/P317_flood_protection_investment/submission/investment_comparison.csv` | Referencias ilustrativas, no estándares reales. |
| H04 — Método por estructura | S04 | Notebook: celda «La variable de decision es continua…», bloque `MODEL`, `minimize_scalar` | No compara alternativas numéricas; una sola variable. |
| H05 — Validación teórica | S04 | Notebook: `h_analytical`, `second_derivative_grid`, `marginal_loss_reduction`, celda de validación | La forma cerrada existe por la forma funcional elegida. |
| H06 — Sensibilidad a `D` y `k` | S05 | Notebook: `solve_total_cost`, `d_sensitivity`, `k_sensitivity`; `implementation/prescriptiva/P317_flood_protection_investment/submission/risk_sensitivity.csv` | Sin variación de `p0`, `alpha` ni combinaciones. |
| H07 — Regla presupuestal y escalamiento | S06, S07 | Notebook: `budget_limited_height`, `risk_cases`, `policy_rows`, `policy_contract`; `implementation/prescriptiva/P317_flood_protection_investment/submission/flood_protection_policy_actions.csv`; `implementation/prescriptiva/P317_flood_protection_investment/submission/flood_protection_policy_contract.json` | Casos de riesgo fijados en código; objetivo y óptimo coinciden, sin conflicto entre ambos. |
| H08 — Persistencia | S07, S08 | Los seis artefactos de `submission/`; `implementation/prescriptiva/P317_flood_protection_investment/tests/test_activity.py` | La prueba acepta cualquier archivo; no exige política ni contrato. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset de parámetros | `data/protection_parameters.csv`; celdas de carga y validación | Siete parámetros sintéticos; sin observaciones. |
| S02 | Modelo de riesgo y costo | Notebook: `flood_probability`, `return_period`, `expected_annual_loss`, `total_annual_cost` | Forma exponencial supuesta; costo anualizado lineal. |
| S03 | Referencias y malla | Notebook: `protection_grid`, referencias 0; 1,5; 5,0 m | Referencias no normativas. |
| S04 | Método y validación | Notebook: `minimize_scalar`, forma cerrada, convexidad, condición marginal | Una variable continua. |
| S05 | Sensibilidad | Notebook: `d_sensitivity`, `k_sensitivity`; `risk_sensitivity.csv` | Tres valores por parámetro, uno a uno. |
| S06 | Regla de aprobación y contrato | Notebook: celda de `risk_cases` y `policy_contract`; `flood_protection_policy_actions.csv`; `flood_protection_policy_contract.json` | Escalamiento determinado por presupuesto; casos de riesgo hipotéticos. |
| S07 | Entregables y planeador | `protection_curve.csv`, `investment_comparison.csv`, `flood_protection_investment_planner.png` | Planeador declarado como evidencia, no como política. |
| S08 | Pruebas | `tests/test_activity.py` | Sólo comprueban que exista algún artefacto. |

### Contrato de evidencia actual

- **Notebook o código:** valida parámetros, define riesgo y costos, evalúa malla y referencias, resuelve con SciPy, valida analíticamente, mide sensibilidad, construye planeador, deriva acciones por caso de riesgo y contrato, verifica valores esperados y persiste.
- **`submission/`:** `protection_curve.csv`, `investment_comparison.csv`, `risk_sensitivity.csv`, `flood_protection_policy_actions.csv`, `flood_protection_policy_contract.json`, `flood_protection_investment_planner.png`.
- **Pruebas:** `test_submission_contains_an_artifact` sólo exige al menos un archivo distinto de `.gitkeep`; no verifica política, contrato, autoridad, cadencia ni valores.
- **Trazabilidad:** P317 mapea `prescriptiva.C02`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P316 (y P305, P308, P315):** el uso previo de PuLP + HiGHS, que P317 rechaza explícitamente para un objetivo no lineal; plantilla de referencias, sensibilidad, planeador y contrato JSON. De P310, el patrón de escalamiento de inversión a comité, sin artefacto compartido.
- **Habilita para Pyyy:** no evidenciada; P318 vuelve a programación lineal sin referirse a P317.

## Trazabilidad y auditoría

P317 está mapeada a `prescriptiva.C02`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C02 y C04 se sostienen (regla computable por caso de riesgo; autoridad ordinaria y de escalamiento con tope presupuestal). C03 se apoya en referencias, validación analítica y sensibilidad determinista uno a uno, sin incertidumbre de parámetros. C05 se apoya en métricas y un gatillo cuantificado (desviación de costo > 10 %), sin línea base persistida en un plan de monitoreo. Frente a la arquitectura («regla de protección según riesgo y presupuesto») el producto existe, aunque los niveles de riesgo son valores fijados y no un insumo observado. El producto de Analytics es una regla anual de aprobación de inversión; la optimización no lineal la respalda y el notebook declara explícitamente que el planeador es evidencia y no política.
