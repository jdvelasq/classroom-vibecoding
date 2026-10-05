# P315 — Posicionamiento preventivo de recursos contra incendios

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P315_wildfire_resource_positioning/`.

### Preguntas analíticas actuales

- ¿Qué política recurrente de posicionamiento y reasignación preventiva reduce el tiempo esperado de respuesta ante incendios, sin activar más bases que las autorizadas?

Usa una geografía ficticia («Distrito Sierra Alta», caso sintético): 8 zonas de riesgo con coordenadas en km y `risk_weight` que suma uno (`risk_zones.csv`), 6 bases candidatas (`candidate_bases.csv`) y parámetros (`deployment_parameters.csv`: activar 2 bases; velocidad media 45 km/h). Los tiempos se derivan de distancia euclidiana; el notebook declara que no se requieren datos GIS reales. El producto es una política de bases activas (B01, B03) con reglas de reasignación por etapa, monitoreo con umbrales y contrato.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** posicionamiento antes de temporada y reasignación preventiva; aprobación del comandante de operaciones; director de operaciones para la activación pre-temporada.
- **Producto terminal:** `deployment_policy.json`, `reassignment_rules.csv` (pre-temporada, revisión programada, alerta territorial con gatillo, acción, autoridad y plazo) y `policy_monitoring.csv` (tiempo esperado 32,65 frente a umbral 40; máximo por zona 53,75 frente a 60), respaldados por decisiones de despliegue, asignación zona–base, sensibilidad de recursos y mapa.
- **Uso y límite:** permite mostrar por qué la mejor combinación espacial difiere de heurísticas de un criterio y cómo cambia con el número de bases. Riesgo estático, sin escenarios de incendio, sin capacidad por base ni incendios simultáneos; velocidad constante. El monitoreo compara salidas del modelo recalculado con umbrales fijos, no tiempos de respuesta observados.
- **Disciplinas contribuyentes:** modelo p-mediana con PuLP/HiGHS verificado por enumeración; geometría euclidiana; sirven a la política de posicionamiento.

### Highlights de contribución

- **H01 — Convierte geografía y riesgo en un objetivo de tiempo esperado:** distancias euclidianas a tiempos (60 × km / 45) y pesos de riesgo que suman uno permiten leer el objetivo como «minutos esperados de respuesta ponderados por riesgo». Particularidad del caso: la unidad es el par zona–base en un plano y la asignación a la base activa más cercana es óptima porque no hay capacidad por base (declarado en el notebook). Sin este hito, el riesgo se leería como prioridad por zona y no como contribución a un tiempo del sistema; el límite es que no representa red vial ni simultaneidad.
- **H02 — Contrasta heurísticas de un solo criterio con la interacción espacial:** «riesgo individual» y «centralidad geográfica» se evalúan con el mismo criterio que el óptimo; la comparación de la segunda base con una base fija muestra que cubrir un foco de riesgo no cubre mejor el resto. Reutiliza el contraste heurística–óptimo de P305/P308 en un problema espacial; sin este hito, el óptimo parecería una variante del ranking por riesgo. Límite: los valores de las heurísticas no se persisten.
- **H03 — Formula y verifica un modelo de localización con activación:** bloque `MODEL` con `y[j]` (activación), `x[i,j]` (asignación), `x <= y` y `sum y = P`; enumeración de C(6,2) combinaciones y HiGHS coinciden en bases, asignación y objetivo; el notebook ilustra que C(30,6) no sería enumerable. Extiende el patrón de P308 a variables enlazadas de activación y asignación; sin este hito, no se ejercería una decisión de ubicación.
- **H04 — Muestra que más recursos cambian la composición, no sólo el valor:** `resource_sensitivity.csv` registra P=1 B03 (51,13 min), P=2 B01;B03 (32,65) y P=3 B01;B02;B04 (17,28), donde B03 sale al pasar a tres bases. Mismo hallazgo de conjuntos no anidados que P305 en otro dominio; sin este hito, una ampliación de recursos se planificaría añadiendo bases a las existentes.
- **H05 — Traduce el óptimo en reglas de reasignación por etapa y monitoreo con umbral:** `reassignment_rules.csv` define tres etapas con gatillo observable, acción, autoridad y plazo (p. ej. «alguna zona supera 60 min» → evaluar base temporal o mover reserva, sin desactivar cobertura sin aprobación); `policy_monitoring.csv` fija línea base y umbral por métrica; la prueba verifica que la línea base no supere el umbral. Primera política del curso con reglas diferenciadas por etapa de temporada; sin este hito, el óptimo de un escenario sería una ubicación fija sin reasignación.

### Inventario técnico de implementación

- **Introduce:** matriz de tiempos zona × base desde coordenadas; modelo p-mediana con variables de activación; sensibilidad al número de instalaciones; reglas de reasignación por etapa con plazo.
- **Extiende:** verificación enumeración vs. HiGHS (P305, P308) a variables enlazadas; contraste heurística vs. óptimo.
- **Reutiliza:** bloque `MODEL`; verificación de unicidad; mapa/planeador PNG; contrato JSON.
- **Aplica en nuevo caso:** conjuntos óptimos no anidados al cambiar el recurso (P305).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Tiempo esperado ponderado | H01 | Euclidiana, 45 km/h, pesos que suman uno | Sin red vial ni escenarios de riesgo. |
| Localización p-mediana | H02–H03 | Enumeración C(6,2) + HiGHS; heurísticas | Sin capacidad por base. |
| Sensibilidad de recursos | H04 | P = 1, 2, 3; conjuntos no anidados | Sólo número de bases. |
| Reasignación gobernada | H05 | Tres etapas, umbrales 40/60 min, autoridad | Umbrales fijos; monitoreo de salidas del modelo. |

### Relación técnica con actividades anteriores

Misma técnica con nuevo caso: comparte con P305 y P308 la plantilla heurísticas → enumeración → PuLP/HiGHS → comparación → sensibilidad → planeador → contrato. Lo distinguible es la decisión espacial de activación con asignación enlazada y las reglas de reasignación por etapa. **Posible duplicación que requiere decisión posterior:** P305, P308 y P315 repiten el mismo patrón de optimización determinista con verificación cruzada. Frente a P314 (posición inmediatamente anterior), P315 vuelve a un modelo determinista sin incertidumbre, aunque la arquitectura lo ubica en la etapa «Ampliar el alcance» (P312–P319, validación bajo incertidumbre).

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Objetivo de tiempo esperado | S01, S02 | `implementation/prescriptiva/P315_wildfire_resource_positioning/data/risk_zones.csv`; `implementation/prescriptiva/P315_wildfire_resource_positioning/data/candidate_bases.csv`; `implementation/prescriptiva/P315_wildfire_resource_positioning/submission/zone_assignments.csv` | Geografía ficticia; velocidad constante. |
| H02 — Heurísticas vs. óptimo | S03 | `implementation/prescriptiva/P315_wildfire_resource_positioning/professor/notebook.ipynb`: `risk_first_bases`, centralidad, `partner_comparison` | `strategy_comparison` no se persiste. |
| H03 — Modelo de localización | S02 | notebook: bloque `MODEL`, PuLP/HiGHS, `assert` de coincidencia; `implementation/prescriptiva/P315_wildfire_resource_positioning/submission/deployment_decisions.csv` | Óptimo único verificado en notebook. |
| H04 — Conjuntos no anidados | S03 | `implementation/prescriptiva/P315_wildfire_resource_positioning/submission/resource_sensitivity.csv` | Riesgo fijo en las tres corridas. |
| H05 — Reasignación y monitoreo | S04, S05 | `implementation/prescriptiva/P315_wildfire_resource_positioning/submission/reassignment_rules.csv`; `implementation/prescriptiva/P315_wildfire_resource_positioning/submission/policy_monitoring.csv`; `implementation/prescriptiva/P315_wildfire_resource_positioning/submission/deployment_policy.json`; `implementation/prescriptiva/P315_wildfire_resource_positioning/tests/test_activity.py` | Ninguna reasignación se calcula ni se simula; umbrales 40/60 no derivados. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso y geografía | `data/risk_zones.csv`, `data/candidate_bases.csv`, `data/deployment_parameters.csv` | Sintético; riesgo estático; 8 zonas, 6 bases. |
| S02 | Representación y modelo | Notebook: `response_time`, `evaluate_deployment`, bloque `MODEL`, PuLP/HiGHS | Sin capacidad por base ni simultaneidad. |
| S03 | Comparación y sensibilidad | Notebook: heurísticas, `partner_comparison`; `resource_sensitivity.csv` | Comparación de heurísticas no persistida. |
| S04 | Política, reasignación y monitoreo | `deployment_policy.json`, `reassignment_rules.csv`, `policy_monitoring.csv`, `wildfire_resource_deployment_map.png` | Monitoreo de salidas del modelo, no de resultados observados. |
| S05 | Pruebas | `tests/test_activity.py` | Verifican estructura y coherencia línea base ≤ umbral; no optimalidad. |

### Contrato de evidencia actual

- **Notebook o código:** valida datos, calcula tiempos, evalúa heurísticas, enumera y resuelve con HiGHS, analiza sensibilidad, construye mapa, reglas, monitoreo y contrato.
- **`submission/`:** `deployment_decisions.csv`, `zone_assignments.csv`, `resource_sensitivity.csv`, `reassignment_rules.csv`, `policy_monitoring.csv`, `deployment_policy.json`, `wildfire_resource_deployment_map.png`.
- **Pruebas:** tres pruebas: existencia de los siete artefactos; contrato con número de bases > 0, bases activas iguales al número autorizado y campos de cadencia, objetivo, salvaguarda y autoridad no vacíos; reglas con al menos tres filas y columnas completas, y monitoreo con `baseline_value <= review_threshold`. No verifican el óptimo ni las asignaciones.
- **Trazabilidad:** P315 mapea `prescriptiva.C02`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P308/P305:** patrón demostrable de modelo binario en bloque `MODEL`, enumeración exhaustiva verificada contra HiGHS, heurísticas bajo el mismo criterio y sensibilidad de recurso con conjuntos no anidados.
- **Habilita para Pyyy:** no evidenciada dentro del alcance inspeccionado.

## Trazabilidad y auditoría

P315 está mapeada a `prescriptiva.C02`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C02 (bases y asignación desde riesgo y geografía) y C04 (autoridad por etapa, salvaguarda de cobertura) se sostienen; C03 sólo por sensibilidad al número de bases, sin incertidumbre ni escenarios; C05 por monitoreo con umbrales sobre salidas del modelo. Coincide con «política de ubicación y reasignación de recursos». El producto de Analytics es una política de posicionamiento con reglas de reasignación gobernadas; la optimización contribuye. Límites: la reasignación se declara pero no se ejercita y el monitoreo no usa resultados observados.
