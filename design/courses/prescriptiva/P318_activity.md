# P318 — Hydrothermal Planning: despacho hidrotérmico con reserva intertemporal

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P318_hydrothermal_planning/`.

### Preguntas analíticas actuales

- ¿Cuánta energía generar con agua embalsada y con cada planta térmica en cada período para atender la demanda al menor costo operativo, sabiendo que usar agua hoy reduce la disponible para la demanda futura?
- ¿Cuánta agua debe preservarse antes del período pico para que el despacho sea factible?
- ¿Cuál es el valor económico de una unidad adicional de agua embalsada?

El notebook declara un «caso sintético de planeación eléctrica centralizada; no representa un sistema real». `data/periods.csv` tiene seis períodos ordenados con demanda (MWh) y caudal entrante (hm³); `data/hydro.csv`, un único embalse (almacenamiento inicial 10, mínimo 2, máximo 20, final mínimo 4 hm³; 10 MWh/hm³; 80 MWh por período); `data/thermal.csv`, dos plantas (T1: 40 por MWh, 60 MWh; T2: 90 por MWh, 100 MWh). El producto es un despacho por período y una trayectoria del embalse obtenidos con un LP intertemporal, más un contrato de política con cadencia, guardas, autoridad y gatillos. El horizonte es determinista: demanda y caudal se tratan como conocidos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** publicar el despacho de cada período; el contrato asigna la aprobación rutinaria al «centro de control» y las contingencias ante infactibilidad a la «jefatura de operación». Roles declarados en un caso sintético.
- **Producto terminal:** `generation_schedule.csv` y `reservoir_schedule.csv` gobernados por `hydrothermal_policy.json`.
- **Uso y límite:** permite mostrar qué despacho es factible y de menor costo y por qué debe reservarse agua antes del pico. No modela incertidumbre de caudal o demanda, aunque el contrato declara «demanda pronosticada» como entrada; la guarda principal está escrita para el período 4 de esta instancia y los gatillos no tienen umbrales numéricos.
- **Disciplinas contribuyentes:** programación lineal intertemporal (PuLP + HiGHS), precios sombra y reglas heurísticas sirven al despacho gobernado.

### Highlights de contribución

- **H01 — Deriva una reserva obligatoria de la estructura temporal del caso:** las filas de `periods.csv` son períodos ordenados, no observaciones intercambiables, y el embalse enlaza cada decisión con las siguientes. Antes de decidir, el notebook calcula que la demanda del período 4 (180 MWh) supera la capacidad térmica máxima (160 MWh), por lo que exige 20 MWh hidráulicos (2 hm³), y deduce el almacenamiento requerido al final del período 3; un gráfico de doble eje muestra que el pico de demanda coincide con el caudal más bajo. Esta particularidad convierte la reserva en condición de factibilidad, no en preferencia de costo. Sin este hito, «usar el agua primero porque no tiene costo variable» parecería razonable.
- **H02 — Demuestra que una regla miope destruye la factibilidad futura:** `naive_hydro_first` libera toda el agua posible en cada período; el notebook muestra y afirma infactibilidad en el período 4. Primera aparición en el curso de una línea base que no es subóptima sino infactible. Sin este hito, la comparación de políticas se reduciría a costos. La tabla de la regla ingenua no se persiste.
- **H03 — Construye una regla factible con pisos de almacenamiento:** `feasible_reserve_rule` mantiene la prioridad hidráulica pero impone `end_of_period_floor` con el piso derivado para el período 3 y el final mínimo en el período 6; verifica que no haya demanda insatisfecha. Su costo (40.250) queda persistido en `plan_comparison.csv`. El notebook declara la progresión «política basada en reglas → modelo matemático → solver profesional». Sin este hito, el óptimo no tendría una regla operable con la cual compararse.
- **H04 — Formula un LP intertemporal con variables de estado:** el bloque `MODEL` y su implementación en PuLP definen generación térmica, hidráulica, liberación, almacenamiento acotado y vertimiento, con balance de demanda, conversión hídrica, balance encadenado del embalse y almacenamiento terminal; HiGHS lo resuelve y el notebook valida período a período balances, límites y no negatividad, y recomputa el costo. El óptimo persistido (38.250) mejora en 2.000 a la regla factible. Extiende el LP de flujos de P316 a decisiones enlazadas en el tiempo. Sin este hito, la secuencia no mostraría cómo una restricción de estado acopla decisiones de distintos períodos.
- **H05 — Extrae el valor del agua como precio sombra y lo valida:** lee el dual de `reservoir_balance_1` (`.pi`), corrige su signo, lo verifica por diferencias finitas con +0,1 hm³ y lo interpreta como el costo térmico desplazado: con los datos, 10 MWh/hm³ × 90 por MWh de T2. Primera lectura de duales de un LP en el curso; P316 obtenía el valor de capacidad re-resolviendo. Sin este hito, el agua parecería gratuita porque no tiene costo en el objetivo. El valor no se persiste en CSV ni JSON; según el código sólo se rotula en el tablero PNG.
- **H06 — Comprueba en la sensibilidad que el valor del agua es constante en este caso:** re-resuelve con almacenamiento inicial de 2 a 20 hm³, afirma costo decreciente y valor del agua constante porque T2 sigue siendo el recurso marginal, y declara que «no se ajustaron los datos para forzar un valor de agua variable». Sin este hito, se generalizaría un valor del agua variable que el caso no exhibe. La tabla de sensibilidad no se persiste.
- **H07 — Declara una política de despacho con cadencia, autoridad y escalamiento:** `hydrothermal_policy.json` fija cadencia diaria y ante actualizaciones materiales, publicación antes de cada período, entradas observables (demanda pronosticada, caudal, almacenamiento observado, capacidad térmica), guardas («no liberar agua que impida cubrir el pico del periodo 4», «no publicar un despacho con demanda insatisfecha»), autoridad rutinaria y de excepción, monitoreo y gatillos de revisión. El notebook declara que el despacho «se convierte en una política operable solo al declarar autoridad, guardas y revisión». Sin este hito, el producto sería un cronograma óptimo.
- **H08 — Persiste despacho, embalse y comparación:** `generation_schedule.csv` (demanda y MWh hidráulicos, T1 y T2 por período), `reservoir_schedule.csv` (caudal, liberación, vertimiento y almacenamiento), `plan_comparison.csv` y `hydrothermal_planning_dashboard.png` con cuatro paneles. Sin estos artefactos, la trayectoria que justifica la reserva no sería auditable.

### Inventario técnico de implementación

- **Introduce:** variables de estado y balance intertemporal; línea base infactible frente a regla factible; precio sombra (`constraint.pi`) con validación por diferencias finitas; tablero de cuatro paneles con mezcla, embalse, uso de T2 y resumen.
- **Extiende:** LP continuo con PuLP + HiGHS de P316 a un horizonte de seis períodos; valor de capacidad de P316 (re-resolución) a valor dual.
- **Reutiliza:** bloque `MODEL` en texto, validación independiente del solver, celda final de verificación, contrato JSON con guardas, autoridad, monitoreo y gatillos.
- **Aplica en nuevo caso:** despacho hidrotérmico sintético.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Acoplamiento temporal por embalse | H01–H03 | Reserva obligatoria derivada; regla ingenua infactible; regla con pisos | Determinista; seis períodos; reglas ingenua y de pisos sólo en notebook, salvo costo de esta última. |
| LP intertemporal | H04 | Balance encadenado, almacenamiento acotado, vertimiento, terminal | Persistido en dos cronogramas y `plan_comparison.csv`. |
| Valor del agua | H05–H06 | Dual, diferencias finitas, interpretación por costo de T2, sensibilidad | No persistido en datos tabulares; constante en el caso. |
| Política de despacho | H07–H08 | Contrato con cadencia, guardas, autoridad, monitoreo y gatillos | Guarda ligada al período 4; gatillos sin umbrales. |

### Relación técnica con actividades anteriores

P318 reutiliza la técnica de P316 (LP continuo, PuLP + HiGHS, validación sin enumeración) con nueva exigencia de representación: estados encadenados en el tiempo y un valor económico implícito del recurso almacenado. Frente a P309 y P313, que tratan demoras y capacidad bajo incertidumbre, aquí el horizonte es determinista. La regla factible con pisos es un producto de política intermedio que no aparece en P316 ni en P317. No hay duplicación evidente. El cronograma persistido muestra T2 activo en los períodos 1–5 visibles; con un valor del agua constante, desplazar generación hidráulica entre esos períodos dentro de los límites del embalse no cambiaría el costo, de modo que el cronograma es probablemente uno de varios óptimos; el notebook no trata la unicidad.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Reserva obligatoria | S01, S02 | `implementation/prescriptiva/P318_hydrothermal_planning/data/periods.csv`; `implementation/prescriptiva/P318_hydrothermal_planning/data/hydro.csv`; `implementation/prescriptiva/P318_hydrothermal_planning/data/thermal.csv`; `implementation/prescriptiva/P318_hydrothermal_planning/professor/notebook.ipynb`: `mandatory_hydro_mwh`, `required_storage_end_p3`, gráfico de doble eje | Períodos sin unidad temporal en los datos; el contrato los llama despacho diario. |
| H02 — Regla miope infactible | S03 | Notebook: `naive_hydro_first`, celda de verificación final | Resultado no persistido. |
| H03 — Regla factible con pisos | S03, S07 | Notebook: `end_of_period_floor`, `feasible_reserve_rule`; `implementation/prescriptiva/P318_hydrothermal_planning/submission/plan_comparison.csv` | Pisos derivados a mano para esta instancia. |
| H04 — LP intertemporal | S04, S07 | Notebook: bloque `MODEL`, `pulp.LpProblem`, celda de validación por período; `implementation/prescriptiva/P318_hydrothermal_planning/submission/generation_schedule.csv`; `implementation/prescriptiva/P318_hydrothermal_planning/submission/reservoir_schedule.csv` | Posibles óptimos alternativos no discutidos; `-0.0` en liberaciones persistidas. |
| H05 — Valor del agua | S05 | Notebook: `model.constraints[...].pi`, `solve_hydrothermal`, `water_value_fd`, `implied_water_value` | No persistido en CSV/JSON. |
| H06 — Sensibilidad del almacenamiento inicial | S05 | Notebook: `storage_sensitivity` y sus `assert` | No persistida; un único parámetro. |
| H07 — Política de despacho | S06, S08 | `implementation/prescriptiva/P318_hydrothermal_planning/submission/hydrothermal_policy.json`; `implementation/prescriptiva/P318_hydrothermal_planning/tests/test_activity.py` | La prueba no exige `cadence` ni `response_need`; guardas no verificadas. |
| H08 — Persistencia de cronogramas | S07 | Los cinco artefactos de `submission/` | La prueba sólo lee el contrato. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético | `data/periods.csv`, `data/hydro.csv`, `data/thermal.csv`; celda de validación | Seis períodos sin unidad; un embalse; dos plantas. |
| S02 | Diagnóstico de reserva | Notebook: cálculo del período 4 y gráfico demanda–caudal | Derivación específica del período 4. |
| S03 | Reglas de referencia | Notebook: `naive_hydro_first`, `feasible_reserve_rule` | Sólo el costo de la regla factible se persiste. |
| S04 | Modelo LP y validación | Notebook: bloque `MODEL`, PuLP/HiGHS, validación por período | Determinista; unicidad no tratada. |
| S05 | Valor del agua y sensibilidad | Notebook: dual, diferencias finitas, `storage_sensitivity` | No persistidos; valor constante. |
| S06 | Contrato de política | Notebook: celda `policy_contract`; `submission/hydrothermal_policy.json` | Guarda ligada a la instancia; gatillos cualitativos. |
| S07 | Entregables y tablero | `generation_schedule.csv`, `reservoir_schedule.csv`, `plan_comparison.csv`, `hydrothermal_planning_dashboard.png` | El contrato se escribe en una celda posterior al guardado de los demás artefactos. |
| S08 | Pruebas | `tests/test_activity.py` | Seis campos no vacíos del contrato. |

### Contrato de evidencia actual

- **Notebook o código:** valida datos, deriva la reserva del pico, evalúa regla ingenua y regla con pisos, resuelve el LP, valida balances, obtiene y verifica el valor del agua, mide sensibilidad, construye el tablero, verifica valores esperados y persiste cronogramas, comparación, tablero y contrato.
- **`submission/`:** `generation_schedule.csv`, `reservoir_schedule.csv`, `plan_comparison.csv`, `hydrothermal_planning_dashboard.png`, `hydrothermal_policy.json`.
- **Pruebas:** `test_01_policy_contract_is_submitted` exige el contrato y que `action`, `constraints`, `guardrails`, `authority`, `monitoring` y `review_triggers` no estén vacíos. No verifica cadencia, cronogramas, factibilidad, costos ni tablero.
- **Trazabilidad:** P318 mapea `prescriptiva.C02`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P316:** LP continuo con PuLP + HiGHS, bloque `MODEL` y validación sin enumeración; el notebook repite que no existe un conjunto finito de decisiones para enumerar.
- **Habilita para Pyyy:** no evidenciada; P319 vuelve a la enumeración por una razón distinta (objetivo no aditivo).

## Trazabilidad y auditoría

P318 está mapeada a `prescriptiva.C02`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C02 se sostiene (despacho computable con reserva); C03 se apoya en una línea base infactible, una regla factible, el óptimo y sensibilidad del almacenamiento inicial, sin incertidumbre de caudal ni demanda; C04 en autoridad rutinaria y de excepción; C05 en métricas y gatillos declarados sin umbrales ni línea base persistida. Frente a la arquitectura («política de generación bajo reservas y horizonte») el producto existe, aunque las guardas están escritas para esta instancia. El producto de Analytics es un despacho gobernado; el LP y sus duales aportan factibilidad y una señal económica, y el notebook declara que el cronograma sólo se vuelve política con autoridad, guardas y revisión.
