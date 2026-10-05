# P304 — Airline Revenue Management: aceptación de tarifa baja con protección de capacidad

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P304_airline_revenue_management/`.

### Preguntas analíticas actuales

- ¿Cuántos asientos vender ahora a tarifa baja y cuántos reservar para pasajeros de tarifa alta que aún no han llegado, sin saber cuántos aparecerán?
- ¿Debe aceptarse o rechazarse cada solicitud temprana de tarifa baja?

Los datos describen un solo vuelo (`flight.csv`: capacidad 20, tarifas fijas 100 y 300), veinte solicitudes tempranas ordenadas (`early_requests.csv`) y tres escenarios discretos de demanda de tarifa alta con probabilidad (`high_fare_demand.csv`: 4, 8 y 12 con 0,30 / 0,50 / 0,20). El notebook impone supuestos explícitos: todas las solicitudes tempranas preceden a la demanda alta, cada aceptación consume un asiento y no hay cancelaciones ni sobreventa. La procedencia no está documentada y el caso no se declara sintético, aunque su escala y estructura son de laboratorio. El producto es una regla de aceptación por solicitud, derivada de un nivel de protección, con contrato de operación y evaluación por escenario.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** aceptar o rechazar cada solicitud temprana; autoridad declarada: el revenue manager aprueba cambios de parámetros y resuelve excepciones; el sistema aplica la regla vigente.
- **Producto terminal:** `policy_contract.json` (entradas observables, regla de acción, objetivo, restricciones, salvaguardas, modo de ejecución, autoridad, monitoreo y gatillos), `booking_decisions.csv` (decisión por solicitud y política), `capacity_value.csv`, `scenario_results.csv` y `revenue_management_cockpit.png`.
- **Uso y límite:** permite operar solicitud por solicitud con una regla de costo de oportunidad y comparar consecuencias por escenario. No estima la distribución de demanda (viene dada), no modela llegadas intercaladas, cancelaciones ni sobreventa, y la sensibilidad a probabilidades queda exploratoria y no persistida.
- **Disciplinas contribuyentes:** valor esperado y valor marginal de capacidad (revenue management) sirven a la regla; matplotlib construye la evidencia visual.

### Highlights de contribución

- **H01 — Representa capacidad perecedera bajo llegadas secuenciales:** el caso fija que las veinte solicitudes tempranas llegan antes de cualquier demanda alta y que no hay sobreventa; por eso aceptar todo agota la capacidad con 2.000 de ingreso en los tres escenarios y rechaza toda la demanda alta (`scenario_results.csv`). Esta particularidad convierte el problema en elegir cuánta capacidad proteger, no en maximizar ventas inmediatas. Sin este hito, el ingreso temprano parecería ingreso total.
- **H02 — Calcula el valor marginal esperado de proteger un asiento:** construye `min(protegidos, demanda) × tarifa alta` por escenario, pondera por probabilidad y diferencia para obtener `marginal_capacity_value`, que compara con la tarifa baja; `capacity_value.csv` marca un único nivel recomendado. Primera aparición en el curso de un valor marginal de recurso como criterio de decisión; sin este hito, la protección se fijaría por intuición.
- **H03 — Traduce el nivel de protección en una regla operativa por solicitud:** cada solicitud se acepta si queda capacidad y la tarifa ofrecida es al menos el costo de oportunidad del siguiente asiento; el notebook verifica que R12 se acepta con 9 asientos y R13 se rechaza con 8, y `booking_decisions.csv` registra `capacity_before`, `opportunity_cost`, `decision` y `protection_target`. Extiende la regla por entidad de P303 a una regla dependiente del estado del recurso; sin este hito, la política sería un número (proteger 8) sin mecanismo de ejecución.
- **H04 — Compara consecuencias distintas ante los mismos futuros:** evalúa aceptar todo, la recomendada (protege 8, acepta 12) y proteger 12 en los tres escenarios, separando demanda alta rechazada y asientos vacíos (`scenario_results.csv`: la recomendada obtiene 2.400 con demanda baja, con cuatro asientos vacíos, y 3.600 con demanda media). Sin este hito, la sobreprotección y la subprotección se leerían sólo como diferencia de ingreso.
- **H05 — Muestra que la protección depende de la creencia sobre la demanda:** con probabilidades 0,20 / 0,40 / 0,40 la protección óptima pasa a 12 (aserción del notebook); el contrato incluye «recalcular la protección cuando cambien capacidad, tarifas o probabilidades». Primera conexión explícita en el curso entre sensibilidad y gatillo de revisión; el límite es que la variante no se persiste.
- **H06 — Declara una ejecución automatizada acotada con escalamiento:** el contrato fija respuesta «inmediata», modo «automatización acotada para solicitudes con datos válidos; escalamiento al revenue manager ante excepciones», monitoreo (ingreso realizado vs esperado, demanda alta rechazada, asientos vacíos) y tres gatillos. Contrasta con P300–P303, todas con aprobación humana previa; sin este hito, el curso no mostraría un caso donde la latencia exige automatizar bajo autoridad humana sobre parámetros.
- **H07 — Verifica identidades de conservación antes de exportar:** aserciones sobre unicidad, capacidad no negativa, consumo de un asiento por aceptación, `aceptadas tempranas + aceptadas altas + vacíos = capacidad` y `aceptadas + rechazadas = demanda`. Sin este hito, las tablas de escenario no tendrían control contable reproducible.

### Inventario técnico de implementación

- **Introduce:** valor esperado de capacidad por escenarios discretos; valor marginal con `diff`; costo de oportunidad como umbral de aceptación; simulación determinista solicitud por solicitud.
- **Introduce:** comparación de tres políticas mediante `merge(how="cross")` con escenarios; métricas esperadas ponderadas por probabilidad.
- **Introduce:** contrato con `observable_inputs`, `action_rule` y modo automatizado acotado.
- **Extiende:** comparación con línea base ingenua (P301) y regla por entidad (P303).
- **Aplica en nuevo caso:** figura compuesta («cockpit») persistida en `submission/`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Nivel de protección | H01–H02 | Valor marginal esperado vs tarifa baja | Tres escenarios discretos; llegadas no intercaladas. |
| Regla de aceptación por solicitud | H03 | Costo de oportunidad dependiente de capacidad | Registrada para veinte solicitudes de un vuelo. |
| Consecuencias por escenario | H04 | Ingreso, demanda rechazada, asientos vacíos | Escenarios dados, no estimados. |
| Sensibilidad → revisión | H05 | Variante de probabilidades; gatillo de recálculo | Variante no persistida. |
| Automatización acotada | H06 | Modo, autoridad, monitoreo y gatillos | Declarativo; sin registro de excepciones. |

### Relación técnica con actividades anteriores

Primera actividad del curso en que la acción depende del estado de un recurso que se consume con cada decisión. Comparte con P303 la decisión por entidad y con P301 la comparación contra una línea base ingenua, pero añade incertidumbre en escenarios, valor marginal y ejecución automatizada. No duplica actividades anteriores.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Capacidad perecedera secuencial | S01, S04 | `implementation/prescriptiva/P304_airline_revenue_management/data/flight.csv`, `data/early_requests.csv`, `data/high_fare_demand.csv`; notebook: celdas de supuestos y política ingenua; `implementation/prescriptiva/P304_airline_revenue_management/submission/scenario_results.csv` | Supuesto de orden estricto; sin procedencia. |
| H02 — Valor marginal de capacidad | S02 | `implementation/prescriptiva/P304_airline_revenue_management/professor/notebook.ipynb`: `future_value`, `marginal_value`, `capacity_value`; `implementation/prescriptiva/P304_airline_revenue_management/submission/capacity_value.csv` | Depende de la distribución de tres escenarios. |
| H03 — Regla por solicitud | S03 | notebook: bucle `recommended`, tabla `boundary`; `implementation/prescriptiva/P304_airline_revenue_management/submission/booking_decisions.csv` | Las filas R12/R13 no son visibles en la cabecera del volcado; se apoyan en aserciones. |
| H04 — Consecuencias por escenario | S04 | notebook: `scenario_results`, `expected_metrics`; `submission/scenario_results.csv` | Comparación ex ante, no resultado observado. |
| H05 — Sensibilidad y gatillo | S02, S05 | notebook: `variant_probabilities`, aserción `variant_protection == 12`; `submission/policy_contract.json`: `safeguards` | Exploratoria; no se exporta. |
| H06 — Automatización acotada | S05 | `implementation/prescriptiva/P304_airline_revenue_management/submission/policy_contract.json` | No hay registro de excepciones ni de monitoreo ejecutado. |
| H07 — Identidades de conservación | S06 | notebook: celda de aserciones final | Las pruebas no reproducen estas verificaciones. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y supuestos de llegada | `data/flight.csv`, `data/early_requests.csv`, `data/high_fare_demand.csv` | Un vuelo; tres escenarios; sin cancelaciones ni sobreventa; procedencia no documentada. |
| S02 | Valor de capacidad y protección | Notebook: `high_revenue_by_scenario`, `future_value`, `marginal_value`, `capacity_value` | Protección elegida por ingreso total esperado. |
| S03 | Regla operativa por solicitud | Notebook: bucle `recommended`; `booking_decisions.csv` | Tarifa baja única; costo de oportunidad precalculado. |
| S04 | Evaluación por escenarios | Notebook: `policy_scenarios`, `excess`, `scenario_results`; `scenario_results.csv` | Tres políticas; sin incertidumbre de parámetros. |
| S05 | Producto/contrato y gobierno | `policy_contract.json`; `revenue_management_cockpit.png` | Monitoreo y gatillos declarados, no ejecutados; sensibilidad no persistida. |
| S06 | Validación y pruebas | Celda de aserciones; `tests/test_activity.py` | La prueba exige sólo dos archivos. |

### Contrato de evidencia actual

- **Notebook o código:** todo en `professor/notebook.ipynb`; valida datos, simula aceptar todo, calcula valor marginal y protección, aplica la regla, compara escenarios, explora sensibilidad, verifica y exporta.
- **`submission/`:** `capacity_value.csv` (21 niveles), `booking_decisions.csv` (40 filas: dos políticas × 20 solicitudes), `scenario_results.csv` (9 filas: tres políticas × tres escenarios), `policy_contract.json`, `revenue_management_cockpit.png`.
- **Pruebas:** exigen `booking_decisions.csv` y `policy_contract.json`; no verifican contenido ni los demás artefactos.
- **Trazabilidad:** P304 mapea `prescriptiva.C01`, `C02`, `C03` y `C04`.

### Dependencias en la secuencia

- **Recibe de P303:** decisión por entidad con regla explícita; de P300–P302, el contrato de política.
- **Habilita para Pyyy:** no evidenciada como artefacto. El patrón «figura de planeación persistida + contrato + tablas de escenario» reaparece en P305 y P306.

## Trazabilidad y auditoría

P304 está mapeada a `prescriptiva.C01`–`C04`. La evidencia sostiene C01 (contrato completo), C02 (regla computable desde capacidad observable y costo de oportunidad), C03 (comparación por escenarios y sensibilidad exploratoria) y C04 (automatización acotada con escalamiento). Declara además monitoreo y gatillos (afines a C05) sin mapearlos. Coincide con el producto previsto («regla de aceptación y protección de capacidad»). El producto de Analytics es una política operable por solicitud; el revenue management contribuye al cálculo y no organiza el taller. Límite: monitoreo y gatillos no se ejercen sobre resultados observados.
