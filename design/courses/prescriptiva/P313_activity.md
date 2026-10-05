# P313 — Capacidad de flota de entregas: simulación y contingencia

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P313_delivery_fleet_capacity/`.

### Preguntas analíticas actuales

- ¿Cuántos vehículos reservar antes de conocer los pedidos de mañana, equilibrando costo fijo de flota y costo de tercerizar los pedidos no cubiertos?
- ¿Cuándo pasar de la reserva base a una reserva de contingencia y cuándo escalar a aprobación humana?

Usa una sola fila de parámetros «congelados» (`simulation_parameters.csv`: semilla 42, 20.000 escenarios, flotas candidatas 4–16, costo fijo 180 por vehículo, tercerización 25 por pedido, demanda media 120 con forma Gamma 8, capacidad por vehículo Normal(14, 3) recortada en 4). El planeador se titula «caso sintético de entregas el mismo día». El producto es una política diaria de reserva base (8), contingencia (10) y escalamiento, validada sobre los mismos futuros simulados.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** reservar flota para el día siguiente, cadencia diaria antes de las 18:00; «operaciones» aprueba contingencias con pronóstico ≥ 185 pedidos.
- **Producto terminal:** `fleet_policy.csv` (acción normal, acción de contingencia con gatillo ≥ 145, guarda de 10 vehículos sin autorización, autoridad, gatillo de monitoreo) y `fleet_policy_validation.csv`, respaldados por evaluación de flotas con IC95%, políticas de referencia y sensibilidad al costo de tercerizar.
- **Uso y límite:** la simulación estima costos esperados con error de muestreo explícito y compara decisiones sobre futuros comunes. Los parámetros de contingencia (10, 145, 185) y el error de pronóstico (sd 15) se fijan en el notebook sin optimización; la validación de la política es dentro de la misma muestra simulada y el pronóstico se construye como demanda realizada más ruido.
- **Disciplinas contribuyentes:** simulación Monte Carlo (Gamma-Poisson, Normal recortada), números aleatorios comunes, inferencia de medias e intervalos pareados; sirven a la regla de reserva.

### Highlights de contribución

- **H01 — Representa demanda con cola derecha y capacidad incierta por vehículo:** la demanda es mezcla Gamma-Poisson (el notebook deriva Var(D) = E[μ] + Var(μ) y la verifica contra la muestra) y la capacidad por vehículo es continua equivalente en pedidos, recortada inferiormente; el notebook declara que no hay ruteo ni pedidos indivisibles. Particularidad del caso: la incertidumbre está en ambos lados (demanda y oferta) y la decisión es un entero agregado; sin este hito, la flota se dimensionaría con una media determinista como en la política `mean_demand`.
- **H02 — Evalúa todas las decisiones sobre los mismos futuros:** un conjunto maestro de futuros con capacidades acumuladas (`cumsum`) hace que las flotas mayores aniden los sorteos de las menores («cambiamos la decisión, no el mañana»), verificado con `assert`. Primera aparición de números aleatorios comunes en el curso; extiende P310, que simula una sola alternativa. Sin este hito, las diferencias entre flotas mezclarían efecto de decisión y ruido de muestreo.
- **H03 — Reporta el objetivo como estimación con incertidumbre:** `fleet_evaluation.csv` persiste costo esperado, error estándar e IC95% por flota (n=8: 1.986,92; IC 1.975,74–1.998,11). El notebook contrasta explícitamente «enumerar decisiones» con «enumerar incertidumbre». Sin este hito, el mínimo simulado se leería como valor exacto, como en los modelos deterministas de P305/P308.
- **H04 — Separa decisiones vecinas con diferencias pareadas y convergencia:** compara 7–8 y 8–9 con IC pareados que excluyen cero, contrasta el error estándar pareado frente al ingenuo y tabula convergencia con prefijos 100–20.000. Sin este hito, la elección de 8 frente a 9 (brecha verificada en notebook) no tendría respaldo estadístico. Límite: tablas pareadas y de convergencia no se persisten.
- **H05 — Compara contra reglas operativas plausibles y contra el precio del recurso externo:** `reference_policies.csv` muestra lean (7), media (9), conservadora P90 (13) y optimizada (8) con brecha de 28,10, 16,88 y 424,80; `outsourcing_cost_sensitivity.csv` muestra flota óptima 5, 8 y 10 para costo 15, 25 y 40. Sin este hito, el óptimo no se distinguiría de reglas empíricas ni se sabría qué supuesto económico lo mueve.
- **H06 — Convierte la flota óptima en política diaria con contingencia y escalamiento, y la valida:** `fleet_policy.csv` define base 8, contingencia 10 si el pronóstico ≥ 145, guarda de 10 sin autorización y aprobación humana ≥ 185; `fleet_policy_validation.csv` compara flota fija 8 (1.986,92; tercerización esperada 21,88) con base + contingencia (1.904,43; 14,69; tasa de contingencia 0,2701; tasa de escalamiento 0,0931). Primera política del curso con dos niveles de acción disparados por un pronóstico y validada por simulación; sin este hito, la simulación terminaría en un número óptimo sin regla operativa. Límites: umbrales no optimizados, validación en la misma muestra, pronóstico construido desde la demanda realizada, y el escalamiento no altera la acción simulada.

### Inventario técnico de implementación

- **Introduce:** mezcla Gamma-Poisson; números aleatorios comunes con capacidad acumulada; IC95% de medias simuladas; diferencias pareadas y comparación de errores estándar; convergencia por prefijos; validación simulada de una política con pronóstico ruidoso.
- **Extiende:** Monte Carlo de P310 de una alternativa a 13 alternativas comparables; sensibilidad a un parámetro económico.
- **Reutiliza:** bloque `DECISION MODEL` en comentarios; planeador PNG de cuatro paneles; verificación final con `assert`.
- **Aplica en nuevo caso:** comparación con reglas de referencia bajo el mismo criterio (P305, P308).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Demanda sobredispersa | H01 | Gamma-Poisson con varianza derivada | Parámetros sintéticos congelados. |
| Optimización por simulación | H02–H04 | CRN, IC95%, pareadas, convergencia | Pareadas y convergencia no persistidas. |
| Referencias y sensibilidad | H05 | Lean/media/P90; costo de tercerizar 15–40 | Sensibilidad a un parámetro. |
| Política con contingencia | H06 | Base 8 / contingencia 10 / escalamiento 185; validación | Validación en muestra; umbrales fijados a mano. |

### Relación técnica con actividades anteriores

Nuevo método al servicio del mismo producto: P309 decide capacidad con escenarios discretos y demora; P313 decide capacidad diaria con simulación estocástica y una contingencia basada en pronóstico. Extiende la simulación de P310 con exigencias de evidencia (CRN, intervalos, pareadas) que P310 no tiene. El notebook contiene referencias heredadas a «W03/W05/W06/W11/W12» para contrastar objetivos deterministas con estimados; esa numeración no corresponde a P3xx y no permite establecer a qué actividades alude. **Posible duplicación:** P310 y P313 comparten Monte Carlo; P313 subsume técnicamente a P310 en evidencia de simulación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Demanda y capacidad inciertas | S01, S02 | `implementation/prescriptiva/P313_delivery_fleet_capacity/data/simulation_parameters.csv`; `implementation/prescriptiva/P313_delivery_fleet_capacity/professor/notebook.ipynb`: celdas Gamma-Poisson, capacidad recortada, verificación muestral | Sin procedencia ni calibración; capacidad continua sin ruteo. |
| H02 — Futuros comunes | S02 | notebook: conjunto maestro, `cumulative_capacity`, `assert` de anidamiento | Sólo verificado en notebook. |
| H03 — IC del objetivo | S02, S03 | `implementation/prescriptiva/P313_delivery_fleet_capacity/submission/fleet_evaluation.csv` | IC por flota, no simultáneos. |
| H04 — Pareadas y convergencia | S03 | notebook: `paired_difference`, `convergence_table` | No persistidas en `submission/`. |
| H05 — Referencias y sensibilidad | S03 | `implementation/prescriptiva/P313_delivery_fleet_capacity/submission/reference_policies.csv`; `implementation/prescriptiva/P313_delivery_fleet_capacity/submission/outsourcing_cost_sensitivity.csv` | Referencias calculadas sobre la misma muestra. |
| H06 — Política validada | S04, S05 | `implementation/prescriptiva/P313_delivery_fleet_capacity/submission/fleet_policy.csv`; `implementation/prescriptiva/P313_delivery_fleet_capacity/submission/fleet_policy_validation.csv`; `delivery_fleet_capacity_planner.png` | El planeador se construye antes de la política y no la muestra; pronóstico = demanda + ruido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Parámetros del caso | `data/simulation_parameters.csv` | Sintético; una fila; sin procedencia. |
| S02 | Modelo de simulación y estimación | Notebook: generación, CRN, `evaluate_fleet`; `fleet_evaluation.csv` | Capacidad agregada continua. |
| S03 | Validación comparativa | Notebook: pareadas, convergencia; `reference_policies.csv`, `outsourcing_cost_sensitivity.csv` | Parte de la evidencia no persistida. |
| S04 | Política de contingencia | Notebook: `BASE_FLEET`, `CONTINGENCY_*`, `ESCALATION_TRIGGER`, `FORECAST_ERROR_SD`; `fleet_policy.csv`, `fleet_policy_validation.csv` | Umbrales fijos; validación en muestra. |
| S05 | Producto visual y pruebas | `delivery_fleet_capacity_planner.png`; `tests/test_activity.py` | Planeador sin la política; pruebas de existencia. |
| S06 | Secuencia y referencias heredadas | Notebook: celdas con «W03/W05/W06/W11/W12» | Numeración ajena a P3xx. |

### Contrato de evidencia actual

- **Notebook o código:** valida parámetros, simula futuros comunes, estima costos con IC, compara pareadamente, analiza convergencia y sensibilidad, construye el planeador y valida la política de contingencia.
- **`submission/`:** `fleet_evaluation.csv`, `reference_policies.csv`, `outsourcing_cost_sensitivity.csv`, `fleet_policy.csv`, `fleet_policy_validation.csv`, `delivery_fleet_capacity_planner.png`.
- **Pruebas:** verifican que existan `fleet_policy.csv`, `fleet_policy_validation.csv` y el PNG; no verifican contenido.
- **Trazabilidad:** P313 mapea `prescriptiva.C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P310:** práctica de evaluar una decisión con Monte Carlo y semilla fija (no referenciada explícitamente). De P305/P308, comparación con reglas de referencia bajo un mismo criterio.
- **Habilita para P314:** P314 declara en su notebook «W12 preguntó… W13 agrega…», lo que sugiere continuidad de primera etapa → recurso; la correspondencia W12 = P313 no está documentada. No hay artefacto compartido.

## Trazabilidad y auditoría

P313 está mapeada a `prescriptiva.C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C03 está fuertemente sostenida (simulación con incertidumbre de estimación, referencias, sensibilidad, validación de política); C04 por guarda de 10 vehículos y aprobación humana ≥ 185; C05 por un gatillo de monitoreo («tercerización mensual supera su línea base») sin línea base cuantificada. Coincide con «regla de flota y contingencia validada por simulación». El producto de Analytics es una política diaria de reserva con contingencia y escalamiento; la simulación es la evidencia. Límites: validación en muestra, umbrales sin derivación y pronóstico sintético dependiente de la demanda realizada.
