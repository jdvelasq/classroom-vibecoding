# P308 — Annie Moore: asignación de familias refugiadas a localidades

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/`.

### Preguntas analíticas actuales

- ¿A qué localidad debe recomendarse cada familia de una cohorte, respetando cupos y compatibilidad de servicios, para maximizar la suma de probabilidades estimadas de empleo a seis meses?
- ¿Por qué una combinación conjunta supera a las recomendaciones individuales o a una asignación secuencial por orden administrativo?

El notebook declara un caso sintético: 8 familias (`families.csv`, con `service_requirement`), 4 localidades con capacidad 2 cada una y servicio disponible (`locations.csv`), y una matriz larga de 32 pares familia–localidad con `employment_probability` suministrada (`predicted_outcomes.csv`), vacía en los pares incompatibles. No hay archivo de procedencia; el nombre del directorio alude a Annie Moore, pero el notebook no documenta la relación con ese sistema ni con datos reales. El producto es una recomendación de asignación por cohorte con contrato, cola de decisiones pendientes de aprobación humana y plan de monitoreo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** recomendar una localidad por familia elegible antes de la reunión de asignación de cada cohorte; autoridad declarada: «Equipo autorizado de reasentamiento y protección».
- **Producto terminal:** política de recomendación (`policy_contract.json`) con guardas, condiciones de retención (`hold_conditions`), cola `decision_queue.csv` en estado `pending_human_approval` y `monitoring_plan.csv` con gatillos y respuestas.
- **Uso y límite:** permite mostrar cómo capacidad compartida y compatibilidad transforman probabilidades individuales en una asignación factible y gobernada. El objetivo es empleo de al menos un adulto a seis meses; el contrato declara que no representa bienestar integral, reunificación familiar, seguridad ni preferencias. Las probabilidades son insumos dados: no se estima ni se valida su calibración.
- **Disciplinas contribuyentes:** asignación binaria con PuLP/HiGHS y enumeración exhaustiva aportan factibilidad y optimalidad; pandas/matplotlib aportan matrices y consola visual. La identidad es la política de recomendación con autoridad humana.

### Highlights de contribución

- **H01 — Distingue incompatibilidad de baja probabilidad:** el dataset deja `employment_probability` vacía en pares no compatibles y la compatibilidad se deriva de `service_requirement` frente a `available_service`; el notebook verifica con `assert` que los incompatibles son `NaN` y que F08 sólo admite L01 y L04, y la matriz visual muestra «No compatible» en gris. Primera vez en el curso que una restricción de elegibilidad por par entra como dato estructural y no como penalización; sin este hito, un cero o un faltante se confundiría con una alternativa mala pero permitida.
- **H02 — Muestra que el mejor destino individual no es ejecutable con capacidad compartida:** elige el máximo compatible por familia y contabiliza uso por localidad; `location_utilization.csv` registra L01 con 3 casos para capacidad 2 (`utilization_rate` 1.5) y `assignment_comparison.csv` marca `individual` como `feasible=False` con 6.69. Sin este hito, la recomendación por familia parecería suficiente.
- **H03 — Hace visible el efecto del orden administrativo:** la regla secuencial F01→F08 asigna la mejor plaza restante y registra capacidad antes/después por familia; el resultado es factible pero inferior (6.31 frente a 6.67 en `assignment_comparison.csv`). La sensibilidad con orden inverso alcanza el óptimo en este caso, y el notebook advierte que eso no prueba que el método voraz sea óptimo en general. Sin este hito, una regla secuencial razonable parecería neutral respecto del orden.
- **H04 — Formula y verifica una asignación con tres familias de restricciones:** bloque `MODEL` con una localidad por familia, capacidad por localidad y `x[f,l] <= compatible[f,l]`; enumera sólo combinaciones compatibles (reduce 4^8 crudas a candidatas compatibles) y compara con HiGHS. Reutiliza el patrón enumeración + solver de P305, ahora con restricción de asignación y elegibilidad por par; sin este hito, el salto de mochila a asignación no se ejercería.
- **H05 — Explica el óptimo como un intercambio, no como una caja negra:** `placement_decisions.csv` persiste por familia destino individual, secuencial y óptimo, pérdida de oportunidad y cambio de probabilidad; F01 pasa de L01 (0.80) a L04 (0.78), y el notebook verifica que F08 es la familia que gana al ocupar L01. Sin este hito, la recomendación no sería explicable familia por familia ante la autoridad.
- **H06 — Convierte la asignación en recomendación con aprobación obligatoria y condiciones de retención:** el contrato declara cadencia por cohorte y tras cambios de capacidad, modo «Recomendación con aprobación humana obligatoria», derecho de anulación con registro de motivo y tres `hold_conditions` (predicción ausente o sin vigencia, cupo/servicio cambiado, solicitud de revisión de familia, autoridad o protección). Extiende el contrato de P302/P303 a una decisión que afecta derechos; sin este hito, el óptimo matemático se leería como asignación ejecutable.
- **H07 — Define monitoreo que separa bloqueo, revisión contextual y recalibración:** `monitoring_plan.csv` incluye violaciones de compatibilidad y exceso de capacidad con gatillo 0 y respuesta de bloqueo, aprobación faltante, tasa de anulación «no interpretar por sí sola como falla», brecha entre empleo observado a seis meses y probabilidad estimada, y solicitudes de protección. Primera vez que el curso declara la tasa de anulación humana como señal de revisión; sin este hito, la política no tendría mecanismo de aprendizaje por cohorte.

### Inventario técnico de implementación

- **Introduce:** pares familia–localidad en formato largo con `merge(..., validate=...)`; compatibilidad derivada; matrices `pivot` con valores enmascarados; asignación binaria con restricción de elegibilidad; pérdida de oportunidad por entidad; sensibilidad al orden de procesamiento; cola de decisiones con estado y autoridad.
- **Extiende:** heurística voraz con traza de capacidad (P305) a recurso por localidad; verificación de unicidad del óptimo con aritmética entera en centésimas.
- **Reutiliza:** bloque `MODEL` en comentarios, PuLP + HiGHS contrastado con enumeración exhaustiva (P305); consola/planeador PNG; contrato JSON.
- **Aplica en nuevo caso:** comparación de políticas bajo los mismos datos y capacidad.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Elegibilidad por par | H01 | Probabilidad vacía en incompatibles; `x <= compatible` | Sintético; F06–F07 no visibles en el encabezado del digest. |
| Capacidad compartida | H02–H03 | Individual inviable; secuencial factible inferior | Un solo tamaño de cohorte; sin incertidumbre en probabilidades. |
| Asignación optimizada | H04–H05 | Enumeración compatible + HiGHS; intercambio F01–F08 | Óptimo para probabilidades dadas, no para resultados reales. |
| Recomendación gobernada | H06–H07 | Contrato, cola pendiente y monitoreo con anulación | No se registran decisiones humanas reales ni resultados observados. |

### Relación técnica con actividades anteriores

Misma técnica con nuevo caso y nueva exigencia de producto respecto de P305: P305 resuelve una mochila con un recurso; P308 resuelve una asignación con capacidad por localidad y elegibilidad por par, y añade una dimensión de derechos (aprobación obligatoria, anulación con motivo, protección). Toma de P306 la idea de que una predicción es insumo, pero no estima ninguna probabilidad. **Posible duplicación que requiere decisión posterior:** P305, P308 y P315 comparten la misma plantilla (heurísticas de un criterio → enumeración exhaustiva → modelo PuLP/HiGHS con verificación cruzada → comparación → sensibilidad → planeador PNG → contrato). En P308 la novedad distinguible es la elegibilidad estructural y la gobernanza de una decisión sensible, no el patrón de optimización.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Incompatibilidad estructural | S01, S02 | `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/data/predicted_outcomes.csv`; `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/professor/notebook.ipynb`: celdas `compatible`, `assert` sobre `NaN` y F08, matriz enmascarada | Un solo tipo de servicio (`service_A`); no hay otros criterios de elegibilidad. |
| H02 — Individual inviable | S02, S03 | `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/submission/location_utilization.csv`; `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/submission/assignment_comparison.csv` | La suma 6.69 es número esperado de familias, no probabilidad de grupo. |
| H03 — Efecto del orden | S03 | `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/professor/notebook.ipynb`: celdas `capacity_history`, orden inverso; `assignment_comparison.csv` | La tabla de orden inverso no se persiste; un caso no generaliza el método voraz. |
| H04 — Modelo de asignación | S02 | `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/professor/notebook.ipynb`: bloque `MODEL`, enumeración compatible, PuLP/HiGHS y `assert` de coincidencia | El número de asignaciones factibles y la unicidad se verifican en el notebook, no en `submission/`. |
| H05 — Intercambio explicado | S03, S04 | `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/submission/placement_decisions.csv`; consola `refugee_placement_console.png` | El encabezado del digest muestra F01–F05; F08 se sustenta en `assert` del notebook. |
| H06 — Recomendación con aprobación | S04 | `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/submission/policy_contract.json`; `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/submission/decision_queue.csv` | `exception_status` es constante (`none_detected_in_training_case`); no se ejercita una retención. |
| H07 — Monitoreo por cohorte | S04, S05 | `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/submission/monitoring_plan.csv`; `implementation/prescriptiva/P308_annie_moore_refugee_resettlement/tests/test_activity.py` | Umbrales «desviación material sostenida» no cuantificados; sin datos de resultado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso y dataset sintético | `data/families.csv`, `data/locations.csv`, `data/predicted_outcomes.csv` | Sin manifiesto de procedencia; 8 familias, 4 localidades, capacidad 2; objetivo limitado a empleo. |
| S02 | Representación y modelo de asignación | Notebook: `pairs`, matrices, bloque `MODEL`, PuLP/HiGHS | Probabilidades fijas sin incertidumbre; sin restricciones de equidad ni preferencias. |
| S03 | Comparación de políticas y sensibilidad | Notebook; `placement_decisions.csv`, `location_utilization.csv`, `assignment_comparison.csv` | Sensibilidad sólo al orden; no persistida. |
| S04 | Producto y gobernanza | `policy_contract.json`, `decision_queue.csv`, `monitoring_plan.csv`, `refugee_placement_console.png` | Cola sin excepción ejercitada; monitoreo sin umbrales numéricos de brecha. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia de tres archivos. |

### Contrato de evidencia actual

- **Notebook o código:** valida pares y compatibilidad, compara individual/secuencial/óptimo, verifica óptimo único con enumeración y HiGHS, construye contrato, cola y monitoreo. Comentario de celda («Los resultados base mantienen la política secuencial F01–F08») no corresponde a lo que se persiste como recomendación (asignación óptima).
- **`submission/`:** `placement_decisions.csv`, `location_utilization.csv`, `assignment_comparison.csv`, `refugee_placement_console.png`, `policy_contract.json`, `decision_queue.csv`, `monitoring_plan.csv`.
- **Pruebas:** comprueban que existan `policy_contract.json`, `decision_queue.csv` y `monitoring_plan.csv`; no verifican factibilidad, capacidad, compatibilidad, estado de aprobación ni columnas.
- **Trazabilidad:** P308 mapea `prescriptiva.C01`, `C02` y `C04`.

### Dependencias en la secuencia

- **Recibe de P305:** patrón demostrable de modelo binario documentado en bloque `MODEL`, enumeración exhaustiva verificada contra PuLP/HiGHS y comparación de heurísticas bajo el mismo recurso. De P302/P303, el contrato con autoridad y excepción (práctica, no artefacto).
- **Habilita para P315:** reutilización observable del mismo patrón enumeración + HiGHS con asignación zona–base. No hay artefacto de datos compartido.

## Trazabilidad y auditoría

P308 está mapeada a `prescriptiva.C01`, `prescriptiva.C02` y `prescriptiva.C04` en `implementation/prescriptiva/traceability.yaml`; la evidencia las sostiene (contrato por cohorte; acción factible desde probabilidades dadas; aprobación obligatoria, anulación y retención). El plan de monitoreo con brecha observada–estimada y tasa de anulación también aportaría evidencia a `C05`, que no está mapeada; se registra sin proponer cambio. Coincide con el producto previsto en `activity-architecture.md` («asignación con utilización y restricciones»). El producto de Analytics es una política de recomendación gobernada; la optimización contribuye a la factibilidad. Límite: no se observa ejecución de la cola ni resultados, y la calidad de las probabilidades queda fuera del alcance.
