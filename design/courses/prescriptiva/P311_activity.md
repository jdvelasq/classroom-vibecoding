# P311 — Evaluación de políticas de capacidad por escenarios

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/`.

### Preguntas analíticas actuales

- ¿Qué capacidad diaria debe operar el centro para cumplir la meta de servicio, controlar el riesgo y respetar el presupuesto?

Usa tres políticas de capacidad (`capacity_policies.csv`: 80, 105 y 130 cupos con costo diario 600, 820 y 1.100 y meta de servicio 0.90) y cuatro escenarios de demanda con probabilidad (`demand_scenarios.csv`: 70, 90, 110, 140 con 0.20, 0.35, 0.30, 0.15). No hay procedencia ni declaración de caso real o sintético. Pese al nombre del directorio, no hay simulación estocástica: `evaluate` calcula esperanzas exactas sobre los cuatro escenarios. El producto es un registro de política con acción, límites, autoridad, gatillos y monitoreo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** capacidad diaria del «centro de atención» confirmada antes de cada jornada; acción rutinaria de la coordinación de operaciones y excepción aprobada por la gerencia.
- **Producto terminal:** `capacity_policy_decision.json` (P1 `refuerzo_flexible`, 105 cupos; límites de servicio esperado ≥ 0.90, probabilidad de incumplimiento ≤ 0.20, costo ≤ 900; tres gatillos; cuatro métricas) y `capacity_policy_comparison.csv`.
- **Uso y límite:** permite seleccionar la política más barata que satisface simultáneamente servicio, riesgo y presupuesto. Los escenarios son cuatro puntos fijos; no se estiman ni se simulan. Los gatillos («dos incumplimientos en diez jornadas») no se derivan ni se validan.
- **Disciplinas contribuyentes:** valor esperado sobre escenarios discretos y filtrado por restricciones; pandas.

### Highlights de contribución

- **H01 — Separa tres guardas que una política debe cumplir a la vez:** `evaluate` calcula servicio esperado, probabilidad de incumplimiento (escenarios con tasa < meta) y costo, y marca `meets_service_target`, `meets_risk_limit`, `meets_budget` y `eligible`. `capacity_policy_comparison.csv` muestra que P0 falla servicio y riesgo (0.815; 0.80), P2 falla presupuesto (1.100 > 900) y sólo P1 es elegible (0.9489; 0.15; 820). Extiende la guarda única de servicio de P307 a tres guardas; sin este hito, una política con buen promedio podría ocultar riesgo o exceder presupuesto.
- **H02 — Distingue meta en promedio de meta por escenario:** la misma meta 0.90 se usa como umbral esperado y como criterio de incumplimiento por escenario; con 105 cupos, el escenario de 110 queda sobre la meta y sólo el de 140 incumple, lo que da probabilidad de incumplimiento 0.15. Es la particularidad del dataset: cuatro escenarios discretos donde una sola cola determina el riesgo. Sin este hito, «cumplir en promedio» se confundiría con «cumplir casi siempre»; el límite es que la probabilidad depende enteramente de cuatro puntos.
- **H03 — Selecciona por menor costo entre elegibles y declara autoridad por tipo de acción:** `choose_policy` usa `nsmallest(["daily_cost", "breach_probability"])` sobre elegibles y lanza error si ninguna cumple; `policy_record` separa acción rutinaria (coordinación) y excepción (gerencia) y añade gatillos de escalamiento, revisión y suspensión. Reutiliza el patrón de contrato de P302/P307; sin este hito, la comparación no tendría consecuencia operativa.

### Inventario técnico de implementación

- **Introduce:** tasa de servicio por escenario con `clip`; probabilidad de incumplimiento como suma de probabilidades de escenarios que no alcanzan la meta; selección lexicográfica entre elegibles.
- **Extiende:** guardas de factibilidad (P300, P302) a tres criterios simultáneos.
- **Reutiliza:** funciones en `main.py` importadas por el notebook; registro JSON de política.
- **Aplica en nuevo caso:** valor esperado sobre escenarios discretos (P304, P307, P309).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Evaluación por escenarios | H01–H02 | Esperanza exacta sobre cuatro escenarios | No es simulación pese al nombre. |
| Restricciones simultáneas | H01, H03 | Servicio, riesgo y presupuesto; elegibilidad | Límites dados en constantes de `main.py`. |
| Registro de política | H03 | JSON con autoridad, gatillos y monitoreo | Gatillos no validados. |

### Relación técnica con actividades anteriores

Misma técnica con nueva exigencia de evidencia respecto de P307: P307 elige la cantidad de pedido con mayor valor esperado sujeta a probabilidad de agotamiento; P311 elige la capacidad más barata sujeta a servicio esperado, probabilidad de incumplimiento y presupuesto. El cálculo es estructuralmente equivalente (clip contra escenarios, suma ponderada, filtro por guarda). **Posible duplicación que requiere decisión posterior:** P311 se superpone con P307 y, en menor medida, con P309 y P314; su aporte distinguible es la combinación de tres guardas y el criterio de menor costo, no un método nuevo. Frente al rol previsto en `activity-architecture.md` («Prueba de política» por simulación, etapa «Probar antes de operar»), la implementación no simula ni compara contra una línea base distinta de las tres alternativas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Tres guardas | S02, S03 | `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/professor/main.py`: `evaluate`; `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/submission/capacity_policy_comparison.csv` | Límites fijos (0.20, 900) sin justificación. |
| H02 — Promedio vs. escenario | S01, S02 | `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/data/demand_scenarios.csv`; notebook: `scenario_effects` | Cuatro escenarios; sin incertidumbre sobre probabilidades. |
| H03 — Selección y autoridad | S04 | `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/professor/main.py`: `choose_policy`, `policy_record`; `implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/submission/capacity_policy_decision.json` | No se registra ejecución ni escalamiento real. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datos de escenarios y políticas | `data/demand_scenarios.csv`, `data/capacity_policies.csv` | Sin procedencia; cuatro escenarios, tres políticas. |
| S02 | Método de evaluación | `professor/main.py`: `evaluate` | Esperanza exacta; no hay simulación. |
| S03 | Guardas y selección | `main.py`: `MAX_BREACH_PROBABILITY`, `MAX_DAILY_COST`, `choose_policy`; `capacity_policy_comparison.csv` | Constantes en código. |
| S04 | Producto | `capacity_policy_decision.json` | Gatillos declarativos. |
| S05 | Pruebas, interfaz y nombre | `tests/test_activity.py`; ruta `root / 'src'`; nombre del directorio | Pruebas de existencia; `src/` sin `main.py`; nombre «por simulación» no coincide con el método. |

### Contrato de evidencia actual

- **Notebook o código:** evalúa políticas, ordena por costo, muestra efectos por escenario de la política elegida y persiste comparación y registro.
- **`submission/`:** `capacity_policy_comparison.csv` y `capacity_policy_decision.json`.
- **Pruebas:** verifican que ambos archivos existan; no comprueban contenido ni elegibilidad.
- **Trazabilidad:** P311 mapea `prescriptiva.C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P307:** patrón demostrable de evaluación por escenarios con guarda probabilística y selección entre factibles. No hay artefacto compartido.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P311 está mapeada a `prescriptiva.C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C04 se sostiene (autoridad rutinaria vs. excepción, escalamiento); C05 por métricas y gatillos declarados; C03 sólo parcialmente: hay evaluación bajo escenarios con riesgo de incumplimiento, pero no simulación, sensibilidad ni prueba frente a demoras o consecuencias no deseadas. El producto de Analytics es una regla diaria de capacidad con tres guardas y autoridad explícita; el cálculo de esperanzas contribuye. Límite: el taller no aporta un método de validación distinto de P307, y su nombre anuncia una simulación inexistente.
