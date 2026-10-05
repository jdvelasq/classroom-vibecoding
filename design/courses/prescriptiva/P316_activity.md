# P316 — Humanitarian Food Aid: abastecimiento y distribución humanitaria

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P316_humanitarian_food_aid/`.

### Preguntas analíticas actuales

- ¿Cuántas toneladas comprar a cada proveedor y enviar a cada destino para cubrir exactamente la demanda declarada al menor costo total entregado, sin superar la oferta de ningún proveedor?
- ¿Por qué reglas de compra al menor precio o de menor costo puesto en destino no capturan el valor de la capacidad escasa del proveedor más barato, y cuánto vale ampliarla?
- ¿Bajo qué condiciones el plan de costo mínimo no puede liberarse y debe escalarse a una autoridad humana?

El notebook de profesor declara el caso como «respuesta humanitaria sintética»: tres proveedores con oferta y costo de compra (`data/suppliers.csv`), cuatro destinos con toneladas requeridas (`data/destinations.csv`) y doce rutas con costo de transporte por tonelada (`data/transport.csv`). La oferta total (120 + 300 + 250 = 670 t) supera la demanda total (150 + 150 + 120 + 130 = 550 t). El producto es un plan de embarques de costo mínimo calculado con programación lineal y liberado por un contrato de política con aprobación humana, bloqueos y gatillos de revisión. No hay horizonte temporal, capacidad de transporte, prioridad por necesidad ni incertidumbre de demanda: la demanda declarada se trata como exacta.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** aprobar diariamente compras y despachos por proveedor y destino; el contrato nombra a «coordinación logística» como aprobadora y a «coordinación humanitaria» como instancia de escalamiento. Son roles declarados en un caso sintético, no una organización evidenciada.
- **Producto terminal:** recomendación de abastecimiento-distribución (`shipment_plan.csv`) gobernada por `policy_contract.json` (cadencia, entradas observables, restricciones, guardas con autoridad, monitoreo y gatillos).
- **Uso y límite:** permite recomendar un plan factible de costo mínimo cuando la oferta alcanza y declarar cuándo no debe liberarse. No implementa la «asignación de escasez» ni la «priorización por necesidad» a las que escalan las guardas; el monitoreo se declara sin línea base ni umbrales persistidos.
- **Disciplinas contribuyentes:** programación lineal (PuLP + HiGHS), heurísticas de referencia y análisis de sensibilidad sirven a la factibilidad y validación del plan; no organizan el taller.

### Highlights de contribución

- **H01 — Lee el caso como red bipartita con holgura global y escasez local:** las tres tablas se validan como red completa (`len(transport) == len(suppliers) * len(destinations)`), sin faltantes ni valores no positivos, y se exige `total_supply >= total_demand` antes de decidir. La matriz `transport_matrix` y la matriz derivada `landed_cost` tienen filas = proveedores y columnas = destinos; cada celda es un costo unitario de ruta, no una observación. La particularidad del caso es que la holgura total (670 frente a 550 t) coexiste con un proveedor barato y escaso (S1, 120 t), que el notebook identifica como la fuente de menor costo puesto para D1 y D2 sin capacidad para cubrir ninguno de los dos. Esa condición da sentido a la restricción de igualdad de demanda, al costo de oportunidad y a la guarda de escasez. Sin este hito, el problema se leería como una tabla de costos intercambiable.
- **H02 — Construye el costo puesto en destino antes de decidir:** muestra por separado costo de compra y matriz de transporte y los combina con `transport_matrix.add(procurement_cost, axis=0)`; `cheapest_per_destination` evidencia que el precio de compra más bajo no determina la fuente más barata en cada destino. Una única función `total_delivered_cost` evalúa luego heurísticas y óptimo con el mismo criterio. Sin este hito, el análisis confundiría costo de compra con costo de atender.
- **H03 — Muestra que una heurística depende de su regla y de su orden:** compara «compra primero» con una regla codiciosa por costo puesto procesada en dos órdenes de destinos. `plan_comparison.csv` persiste 163.350, 158.450 y 159.650, respectivamente; el notebook declara que el orden D1–D4 alcanza el óptimo «por coincidencia». Extiende las comparaciones heurística–óptimo de P305, P308 y P315 con la sensibilidad de una misma heurística al orden de procesamiento. Sin este hito, la coincidencia de una heurística con el óptimo podría leerse como prueba de su validez.
- **H04 — Valora la capacidad escasa como costo de oportunidad y lo contrasta re-resolviendo:** calcula `penalty_per_tonne` (diferencia entre la mejor y la segunda fuente por costo puesto) para D1 y D2 y vuelve a resolver el modelo con S1 en 120, 150 y 180 t; el notebook afirma que el ahorro por tonelada adicional coincide con esas penalizaciones. Extiende la sensibilidad de capacidad de P305 y P315 con una explicación del valor marginal. Sin este hito, el plan óptimo no explicaría por qué ampliar S1 vale distinto según el destino. Las tablas de penalización y sensibilidad no se persisten.
- **H05 — Pasa de enumeración a programación lineal continua:** el notebook declara que las actividades previas enumeraban alternativas discretas y que aquí `x[s,d] >= 0` es continuo, sin conjunto finito que enumerar; escribe el modelo en un bloque de texto (conjuntos, parámetros, costo puesto derivado, oferta `<=`, demanda `=`) y lo implementa en PuLP con HiGHS. Es la primera actividad del curso donde el solver no se contrasta con una búsqueda exhaustiva (P305, P308 y P315 sí lo hacían). Sin este hito, la secuencia no mostraría por qué un problema de flujo exige un modelo matemático en lugar de enumeración.
- **H06 — Valida el plan sin referencia exhaustiva:** sustituye la igualdad con la enumeración por comprobaciones independientes: flujos no negativos, oferta respetada, demanda exacta por destino, total de 550 t, objetivo recomputado con `total_delivered_cost`, descomposición compra + transporte igual al objetivo y dominancia sobre las tres heurísticas. Sin este hito, la confianza en el plan descansaría en el estado `Optimal` del solver.
- **H07 — Convierte el plan de costo mínimo en una política con aprobación y bloqueo:** `policy_contract.json` fija cadencia diaria y ante actualizaciones, aprobación previa a compras y despachos, un sistema que «calcula una recomendación factible; no emite compras ni despachos», tres guardas con condición, acción y autoridad, cuatro métricas de monitoreo y tres gatillos de revisión. Dos guardas coinciden con las condiciones en que el modelo de costo mínimo deja de ser una respuesta válida (oferta total insuficiente; destino sin 100 % de cumplimiento). Sin este hito, el producto sería un óptimo de transporte, no una política gobernada.
- **H08 — Persiste el plan, la utilización y la comparación como evidencia operable:** `shipment_plan.csv` registra cinco rutas activas que suman 550 t con costo de compra, transporte y puesto por ruta; `supplier_utilization.csv` muestra S1 y S3 al 100 % y S2 al 60 %; `plan_comparison.csv` y `humanitarian_supply_planner.png` conservan la comparación y el planeador proveedor–destino. Sin estos artefactos, la recomendación no sería auditable tras cerrar el notebook.

### Inventario técnico de implementación

- **Introduce:** costo puesto en destino como matriz derivada; programación lineal continua de transporte con restricciones de oferta e igualdad de demanda; validación de un óptimo sin búsqueda exhaustiva; sensibilidad de una heurística al orden de procesamiento; penalización de reemplazo como explicación del valor de capacidad.
- **Extiende:** comparación heurística–óptimo y sensibilidad de capacidad por re-resolución (P305, P315); planeador visual compuesto con `Figure` antes de mostrarlo.
- **Reutiliza:** PuLP + HiGHS (P305, P308, P315); bloque `MODEL` en texto; contrato JSON con guardas, autoridad, monitoreo y gatillos (patrón de P304, P306, P308); celda final de verificación con valores esperados.
- **Aplica en nuevo caso:** logística humanitaria sintética con compra y transporte decididos conjuntamente.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Red proveedor–destino con fuente escasa | H01–H02 | Tres tablas, 12 rutas, costo puesto filas = proveedores × columnas = destinos | Sintético; un período; demanda exacta. |
| Heurísticas como línea base | H03 | Compra primero y codiciosa por costo puesto en dos órdenes | Persistido en `plan_comparison.csv`; tres referencias. |
| Valor de capacidad escasa | H04 | Penalización de reemplazo y re-resolución con S1 = 120/150/180 | No persistido; un solo parámetro variado. |
| Programación lineal de transporte | H05–H06 | PuLP + HiGHS; validación por restricciones, recomputación y dominancia | Sin duales ni análisis de degeneración. |
| Política de abastecimiento gobernada | H07–H08 | Contrato con guardas, autoridad, monitoreo; plan y utilización persistidos | Monitoreo sin umbrales; escasez no implementada. |

### Relación técnica con actividades anteriores

P316 conserva la plantilla de P305, P308 y P315 —referencias heurísticas, modelo declarado en texto, PuLP + HiGHS, sensibilidad, planeador y contrato JSON—, pero cambia la representación de decisiones: de selección o asignación discreta enumerable a flujos continuos sin referencia exhaustiva. Es misma técnica de solver con nueva exigencia de validación, no duplicación. Frente a P313 y P314 no usa simulación ni incertidumbre. Los comentarios del notebook se refieren a «W04–W06» y «W07», una numeración heredada que no corresponde al orden P actual (P313 y P314 se denominan W12 y W13 en sus propios notebooks); la continuidad declarada con «W04–W06» es coherente con P305, P308 y P315, pero el texto no lo nombra.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Red con holgura global y escasez local | S01, S02 | `implementation/prescriptiva/P316_humanitarian_food_aid/data/suppliers.csv`; `implementation/prescriptiva/P316_humanitarian_food_aid/data/destinations.csv`; `implementation/prescriptiva/P316_humanitarian_food_aid/data/transport.csv`; `implementation/prescriptiva/P316_humanitarian_food_aid/professor/notebook.ipynb`: celda de `assert` y `total_supply >= total_demand` | Datos sintéticos; no representan una crisis real ni prioridades por necesidad. |
| H02 — Costo puesto en destino | S02 | `implementation/prescriptiva/P316_humanitarian_food_aid/professor/notebook.ipynb`: `transport_matrix`, `landed_cost`, `cheapest_per_destination`, `total_delivered_cost` | Costos unitarios lineales; sin economías de escala ni capacidad de ruta. |
| H03 — Heurísticas y orden | S03, S07 | `implementation/prescriptiva/P316_humanitarian_food_aid/professor/notebook.ipynb`: `procurement_first_plan`, `landed_cost_greedy_plan`, `order_comparison`; `implementation/prescriptiva/P316_humanitarian_food_aid/submission/plan_comparison.csv` | Dos órdenes de una heurística; no caracteriza su desempeño general. |
| H04 — Costo de oportunidad de S1 | S02, S05 | `implementation/prescriptiva/P316_humanitarian_food_aid/professor/notebook.ipynb`: `opportunity_cost`, `solve_for_supply`, `capacity_sensitivity`, `savings_per_tonne` | Valores afirmados en el notebook, no persistidos; sin precios sombra del solver. |
| H05 — Programación lineal continua | S04, S09 | `implementation/prescriptiva/P316_humanitarian_food_aid/professor/notebook.ipynb`: celda «W04–W06 … W07», bloque `MODEL`, `pulp.LpProblem`, `pulp.HiGHS` | La numeración W no coincide con P; la continuidad con P305/P308/P315 es inferida. |
| H06 — Validación sin enumeración | S04 | `implementation/prescriptiva/P316_humanitarian_food_aid/professor/notebook.ipynb`: celda «Validamos el plan optimizado de forma independiente» y celda final de verificación | No verifica unicidad del óptimo; las pruebas no repiten estas comprobaciones. |
| H07 — Política con aprobación y bloqueo | S06, S08 | `implementation/prescriptiva/P316_humanitarian_food_aid/submission/policy_contract.json`; `implementation/prescriptiva/P316_humanitarian_food_aid/tests/test_activity.py`: `test_policy_contract_makes_governance_visible` | La guarda de cumplimiento < 100 % no puede activarse en el plan (la demanda es igualdad); sólo aplica a la ejecución, sin datos de ejecución. |
| H08 — Plan y utilización persistidos | S07, S08 | `implementation/prescriptiva/P316_humanitarian_food_aid/submission/shipment_plan.csv`; `implementation/prescriptiva/P316_humanitarian_food_aid/submission/supplier_utilization.csv`; `implementation/prescriptiva/P316_humanitarian_food_aid/submission/humanitarian_supply_planner.png` | El cumplimiento por destino se calcula pero no se persiste; las pruebas sólo exigen plan y contrato. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético de red | `data/suppliers.csv`, `data/destinations.csv`, `data/transport.csv`; celdas de carga y validación | Tres proveedores, cuatro destinos, oferta ≥ demanda; un solo período. |
| S02 | Representación de costo puesto y escasez | Notebook: `landed_cost`, `cheapest_per_destination`, `opportunity_cost` | Costo lineal por tonelada; S1 como única fuente escasa analizada. |
| S03 | Heurísticas de referencia | Notebook: `procurement_first_plan`, `landed_cost_greedy_plan` | Tres referencias; dependencia del orden mostrada con dos órdenes. |
| S04 | Modelo, solver y validación | Notebook: bloque `MODEL`, PuLP/HiGHS, celdas de validación | LP continuo; sin duales ni análisis de óptimos alternativos. |
| S05 | Sensibilidad de capacidad | Notebook: `solve_for_supply`, `capacity_sensitivity` | Sólo S1; no persistida. |
| S06 | Contrato de política | `submission/policy_contract.json`; última celda del notebook | Monitoreo sin línea base ni umbrales; escasez delegada a un procedimiento inexistente. |
| S07 | Entregables y planeador | `submission/shipment_plan.csv`, `supplier_utilization.csv`, `plan_comparison.csv`, `humanitarian_supply_planner.png` | Sin tabla de cumplimiento por destino. |
| S08 | Pruebas | `tests/test_activity.py` | Verifican existencia y campos no vacíos; no valores. |
| S09 | Secuencia declarada | Notebook: celda con referencias «W04–W06» y «W07» | Numeración heredada distinta del orden P300–P322. |

### Contrato de evidencia actual

- **Notebook o código:** valida la red, construye costo puesto, evalúa tres heurísticas, resuelve el LP con HiGHS, valida el plan sin enumeración, calcula costo de oportunidad y sensibilidad de S1, compone el planeador y escribe el contrato.
- **`submission/`:** `shipment_plan.csv`, `supplier_utilization.csv`, `plan_comparison.csv`, `policy_contract.json`, `humanitarian_supply_planner.png`.
- **Pruebas:** `test_submission_contains_policy_and_plan` exige `shipment_plan.csv` y `policy_contract.json`; `test_policy_contract_makes_governance_visible` exige `action`, `decision_cadence`, `constraints`, `guardrails`, `authority.approver`, `monitoring` y `review_triggers` no vacíos. No verifican factibilidad, costos, utilización, comparación ni planeador.
- **Trazabilidad:** P316 mapea `prescriptiva.C02`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P305, P308 y P315:** patrón referencias → modelo en texto → PuLP + HiGHS → sensibilidad → planeador → contrato JSON; el notebook alude a esa etapa como «W04–W06». No recibe datos ni artefactos.
- **Habilita para P318:** programación lineal continua con PuLP + HiGHS validada sin enumeración; P318 repite el argumento de que no hay conjunto finito que enumerar y lo extiende a variables de estado. P317 rechaza explícitamente PuLP + HiGHS para un objetivo no lineal, contraste que presupone esta herramienta. No hay artefacto compartido.

## Trazabilidad y auditoría

P316 está mapeada a `prescriptiva.C02`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. La evidencia sostiene C02 (plan computable desde oferta, demanda y rutas) y C04 (aprobación previa, sistema sin autoridad de emisión, escalamiento por escasez). C03 está sustentada por líneas base heurísticas y sensibilidad de un parámetro, sin escenarios ni incertidumbre de demanda. C05 se apoya en métricas y gatillos declarados, sin umbrales ni línea base persistida. Frente a la arquitectura («política de abastecimiento y distribución») el producto existe; la «distribución restringida» se limita a oferta y demanda. El producto de Analytics es una recomendación de abastecimiento gobernada; la programación lineal la hace factible y validable sin convertir el taller en un ejercicio de Investigación de Operaciones, porque el contrato conecta entradas observables, acción, guardas, autoridad, cadencia y monitoreo.
