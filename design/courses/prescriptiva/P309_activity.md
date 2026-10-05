# P309 — Capacidad hospitalaria COVID: activación anticipada y escalamiento

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P309_covid_hospital_capacity/`.

### Preguntas analíticas actuales

- ¿Cuándo y cuántos bloques de camas adicionales activar ante una demanda incierta, si cada bloque tarda cuatro días en estar disponible?
- ¿Qué condición observable debe disparar un segundo bloque y quién lo autoriza?

Usa un hospital ficticio (`hospital.csv`: 100 camas iniciales, hasta 2 bloques de 20, plazo de 4 días, horizonte de 21 días, cargas y penalización declaradas como «puntos pedagógicos»), tres trayectorias completas de demanda diaria (`daily_demand.csv`, columnas `low`, `central`, `high`; filas = días) y probabilidades por trayectoria (`scenario_probabilities.csv`: 0.25, 0.65, 0.10). No hay manifiesto de procedencia; el caso no se presenta como datos COVID reales. El producto es una política en dos pasos (bloque base y escalamiento contingente) con contrato, autoridad clínica y monitoreo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** activar y escalar bloques de camas; dueño declarado «Comando de incidentes hospitalario», con la dirección clínica facultada para suspender o modificar.
- **Producto terminal:** `capacity_policy.csv` (pasos `capacidad_base` y `escalamiento_contingente` con contexto observable, acción, cadencia, necesidad de respuesta, autoridad, salvaguarda y gatillo) y `policy_contract.json`; respaldados por 13 planes evaluados, resultados plan × escenario y plan diario recomendado.
- **Uso y límite:** muestra que el plazo de activación obliga a decidir antes de ver la necesidad y que minimizar la puntuación esperada deja riesgo residual en la trayectoria alta. Las puntuaciones no son dinero ni daño clínico; las trayectorias son insumos, no pronósticos estimados en el taller. La política no automatiza decisiones de atención a pacientes.
- **Disciplinas contribuyentes:** evaluación por escenarios con enumeración de planes (día × número de bloques) y agregación pandas; no hay solver. Sirven a la regla de activación.

### Highlights de contribución

- **H01 — Separa la fecha de decisión de la fecha de efecto:** el dataset fija `lead_time_days=4`; la política reactiva (iniciar el día en que la demanda central alcanza la capacidad) deja un intervalo sin cobertura que el notebook mide en camas-día antes de la disponibilidad y visualiza con `axvspan`. Primera vez en el curso que una demora entre acción y efecto organiza la decisión; sin este hito, la capacidad parecería instantánea, como en P304–P308.
- **H02 — Trata las probabilidades como pesos de trayectorias completas:** el notebook advierte que son «probabilidades de trayectorias completas, no de eventos diarios independientes» y evalúa cada plan sobre el mismo calendario bajo las tres trayectorias (`melt` a formato largo, plan × día × escenario); las diferencias se suman como camas-día, «no como pacientes distintos». Esta particularidad del dataset impide tratar cada día como observación independiente; sin este hito, el riesgo diario se combinaría incorrectamente.
- **H03 — Enumera planes de fecha y tamaño con la información de hoy:** 13 alternativas (`none` y `B{1,2}_D03`–`D08`) se comparan por carga de ampliación más penalización por camas-día no cubiertas; `evaluated_plans.csv` persiste `B1_D05` como recomendado (398) frente a `B1_D04` (418), `B1_D06` (450), `B1_D03` (438) y sin ampliar (1299.5). Extiende la comparación por escenarios de P307 a una decisión con dos dimensiones (cuándo y cuánto); sin este hito, la anticipación no tendría costo visible.
- **H04 — Expone el compromiso de anticipar un día más o menos:** compara D04/D05/D06: adelantar no reduce el faltante esperado (11.8 en D04 y D05) pero añade carga; retrasar a D06 ahorra carga y eleva el faltante a 19.0 (`evaluated_plans.csv`). Sin este hito, «actuar antes» parecería siempre mejor.
- **H05 — Hace visible el riesgo residual del plan esperado:** `plan_scenario_results.csv` conserva por escenario camas-día no cubiertas y ociosas (p. ej. 118 camas-día no cubiertas en `high` para los planes de un bloque mostrados) y el planeador sombrea el faltante residual alto. Sin este hito, el mínimo esperado se leería como suficiencia.
- **H06 — Convierte una sensibilidad en gatillo de escalamiento gobernado:** una variante con probabilidad alta 0.30 cambia la cantidad recomendada a dos bloques (sólo en notebook); `capacity_policy.csv` y `policy_contract.json` codifican «probabilidad revisada del escenario alto ≥ 0.30» como contexto para escalar un segundo bloque, con revisión diaria, confirmación de personal/equipos/seguridad y autoridad clínica para suspender. Primera vez en el curso que la política tiene dos pasos con un gatillo derivado de sensibilidad; sin este hito, la recomendación sería un plan estático.
- **H07 — Externaliza la construcción de la política en código reutilizable:** `professor/main.py` define `build_capacity_policy` y `write_policy_artifacts` a partir de `evaluated_plans`; el notebook los importa. La prueba exige las columnas de gobierno y las dos acciones. Sin este hito, el contrato quedaría embebido sólo en celdas.

### Inventario técnico de implementación

- **Introduce:** plazo de activación como restricción temporal; cruce plan × día con `merge(how="cross")`; métricas de camas-día no cubiertas y ociosas; capacidad escalonada `step`; política en dos pasos con gatillo de probabilidad revisada.
- **Extiende:** valor esperado sobre escenarios discretos (P304, P307) a trayectorias temporales completas; separación de componentes de puntuación (carga vs. penalización).
- **Reutiliza:** planeador PNG multipanel; contrato JSON; verificación final con `assert`.
- **Aplica en nuevo caso:** sensibilidad de probabilidades separada de los entregables base (patrón de P304).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Demora acción–efecto | H01, H04 | `lead_time_days=4`; comparación reactivo/anticipado y D04–D06 | Plazo fijo y determinista. |
| Trayectorias como escenarios | H02, H05 | Tres trayectorias de 21 días con probabilidad; camas-día | Sintéticas; sin pronóstico estimado. |
| Plan por fecha y tamaño | H03 | 13 planes; puntuación carga + 10 × faltante | Puntos pedagógicos, no costos. |
| Escalamiento gobernado | H06–H07 | Gatillo ≥ 0.30, autoridad clínica, `main.py` | Gatillo tomado de una sola variante; no se calcula umbral de indiferencia. |

### Relación técnica con actividades anteriores

Nuevo método al servicio del mismo producto respecto de P307 (pedido por escenarios con guarda de servicio): P309 añade horizonte temporal, plazo de activación y escalamiento en dos pasos. Con P304 comparte el aislamiento de la sensibilidad respecto de los entregables. No reutiliza el patrón de solver de P305/P308. **Posible duplicación a vigilar:** P307, P309, P311 y P314 evalúan alternativas discretas por valor esperado sobre escenarios con probabilidad; P309 se distingue por la dimensión temporal y la demora, no por el método de evaluación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Demora | S01, S02 | `implementation/prescriptiva/P309_covid_hospital_capacity/data/hospital.csv`; `implementation/prescriptiva/P309_covid_hospital_capacity/professor/notebook.ipynb`: celdas reactiva y «Inicio día 4» | El faltante reactivo no se persiste en `submission/`. |
| H02 — Trayectorias completas | S01, S02 | `implementation/prescriptiva/P309_covid_hospital_capacity/data/daily_demand.csv`; `implementation/prescriptiva/P309_covid_hospital_capacity/data/scenario_probabilities.csv`; notebook: `demand_long`, `daily` | Tres trayectorias no representan una distribución continua. |
| H03 — Enumeración de planes | S02, S03 | `implementation/prescriptiva/P309_covid_hospital_capacity/submission/evaluated_plans.csv` | Mínimo único verificado en notebook; penalización 10 por cama-día es supuesto. |
| H04 — Compromiso de fecha | S03 | `implementation/prescriptiva/P309_covid_hospital_capacity/submission/evaluated_plans.csv` | Sólo un bloque; resolución diaria. |
| H05 — Riesgo residual | S03, S04 | `implementation/prescriptiva/P309_covid_hospital_capacity/submission/plan_scenario_results.csv`; `implementation/prescriptiva/P309_covid_hospital_capacity/submission/recommended_daily_plan.csv`; `hospital_capacity_planner.png` | El encabezado del digest no muestra la fila `B1_D05`/`high`; el notebook la verifica con `assert`. |
| H06 — Gatillo de escalamiento | S04 | `implementation/prescriptiva/P309_covid_hospital_capacity/submission/capacity_policy.csv`; `implementation/prescriptiva/P309_covid_hospital_capacity/submission/policy_contract.json`; notebook: `variant_probabilities` | El paso contingente conserva `activation_day` 5 / `available_day` 9 aunque se activaría tras revisión diaria; la variante no se persiste. |
| H07 — Política en código | S04, S05 | `implementation/prescriptiva/P309_covid_hospital_capacity/professor/main.py`; `implementation/prescriptiva/P309_covid_hospital_capacity/tests/test_activity.py` | El notebook importa `main` desde `../src`, donde sólo hay `.gitkeep`. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso y datos | `data/hospital.csv`, `data/daily_demand.csv`, `data/scenario_probabilities.csv` | Sintético, sin procedencia; trayectorias central y alta idénticas en los primeros días mostrados. |
| S02 | Representación temporal y puntuación | Notebook: `plans`, `capacity_daily`, `daily`, `burden`, `score` | Puntos pedagógicos; sin recursos clínicos modelados. |
| S03 | Comparación y sensibilidad | `evaluated_plans.csv`, `plan_scenario_results.csv`, `recommended_daily_plan.csv`; notebook | Sensibilidad de una variante, no persistida. |
| S04 | Producto y gobernanza | `professor/main.py`, `capacity_policy.csv`, `policy_contract.json`, `hospital_capacity_planner.png` | Gatillo fijo 0.30; sin registro de decisiones reales. |
| S05 | Pruebas e interfaz de ejecución | `tests/test_activity.py`; ruta `../src` del notebook | Pruebas estructurales; dependencia de `src/main.py` inexistente en el árbol. |

### Contrato de evidencia actual

- **Notebook o código:** valida datos, evalúa 13 planes bajo tres trayectorias, verifica mínimo único `B1_D05` y resultados base vs. sensibilidad, y escribe la política vía `write_policy_artifacts`.
- **`submission/`:** `evaluated_plans.csv`, `plan_scenario_results.csv`, `recommended_daily_plan.csv` (63 filas: 21 días × 3 trayectorias), `hospital_capacity_planner.png`, `capacity_policy.csv`, `policy_contract.json`.
- **Pruebas:** verifican existencia de `capacity_policy.csv` y `policy_contract.json`, columnas de contexto/acción/cadencia/autoridad/salvaguarda/gatillo, presencia de `activar_un_bloque` y `escalar_un_segundo_bloque`, y claves no vacías `safeguards`, `monitoring`, `review_trigger`. No verifican cálculos, planes ni gatillo.
- **Trazabilidad:** P309 mapea `prescriptiva.C02`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P307:** práctica de elegir una acción por valor esperado sobre escenarios con probabilidad y declarar autoridad y gatillo; de P304, separación entre sensibilidad exploratoria y entregables base. No hay artefacto compartido.
- **Habilita para P313/P314:** no evidenciada como dependencia de artefacto; P313 y P314 retoman capacidad bajo incertidumbre con otros métodos (simulación, recurso), sin referencia explícita a P309.

## Trazabilidad y auditoría

P309 está mapeada a `prescriptiva.C02`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. La evidencia sostiene C02 (regla desde trayectorias), C03 (comparación de planes, riesgo residual, sensibilidad), C04 (comando de incidentes, autoridad clínica) y C05 en forma declarativa (monitoreo y gatillo de revisión, sin datos observados). Coincide con «regla de expansión y activación por demanda» de `activity-architecture.md`. El producto de Analytics es una política de capacidad con cadencia diaria, demora explícita y escalamiento gobernado; la evaluación por escenarios contribuye a ella. Límites: el gatillo 0.30 proviene de una sola variante, el paso contingente reutiliza fechas del plan base, y no se especifica cómo se obtiene la «probabilidad revisada».
