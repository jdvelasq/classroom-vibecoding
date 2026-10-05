# P306 — Credit Campaign Targeting: oferta de retención por valor causal estimado

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P306_credit_campaign_targeting/`.

### Preguntas analíticas actuales

- ¿A qué clientes ofrecer una campaña de retención con cupos limitados, distinguiendo entre quienes tienen mayor riesgo y aquellos cuya decisión puede cambiar por la oferta?
- ¿Cuánto valor incremental genera cada regla de focalización y cómo cambia con la capacidad?

El notebook declara una **campaña sintética**: `data/campaign.csv` tiene 2.000 clientes (filas = cliente; columnas = comportamiento, cuota anual, valor del cliente, oferta `retention_offer` asignada al azar —el notebook exige una tasa entre 45 % y 55 %— y resultado `retained_next_period`). `data/synthetic_truth.csv` guarda las probabilidades potenciales verdaderas y el efecto causal verdadero (`true_uplift`) por cliente; se carga sólo después de congelar las políticas y nunca se usa para ajustar ni ordenar. Aunque la carpeta se llama «credit campaign», el caso es una oferta de retención; la columna `annual_fee` sugiere un producto con cuota, sin más especificación. El producto es una política semanal de recomendación con registro de decisiones, banda de revisión humana y plan de monitoreo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** recomendar clientes para la oferta antes de cada lote semanal; autoridad declarada: responsable de campañas de retención.
- **Producto terminal:** `policy_contract.json` (decisión, cadencia, plazo, modo, autoridad, acción, elegibilidad, excepciones y límite de equidad), `decision_register.csv` (800 clientes con acción, revisión humana, autoridad y estado), `monitoring_plan.csv` (métrica, cadencia, gatillo, acción y autoridad), `targeting_decisions.csv`, `policy_comparison.csv`, `capacity_sensitivity.csv` y `credit_campaign_targeting_planner.png`.
- **Uso y límite:** permite mostrar que focalizar por efecto causal estimado y valor supera a focalizar por riesgo, y gobernar la recomendación. La evaluación usa una verdad sintética que no existe en operación real; no hay estimación del valor de la política a partir de resultados observados. El contrato declara que el caso «no permite afirmar equidad».
- **Disciplinas contribuyentes:** T-learner con dos regresiones logísticas (scikit-learn) aporta el efecto causal estimado; un ordenamiento resuelve exactamente la selección con capacidad de cardinalidad.

### Highlights de contribución

- **H01 — Aprovecha un tratamiento aleatorizado y una verdad oculta para validar sin filtración:** verifica que `retention_offer` sea aleatoria y que ninguna columna de verdad esté presente; separa entrenamiento/prueba (1.200/800) estratificando por tratamiento; congela las cuatro políticas y sólo entonces fusiona `synthetic_truth.csv`. La particularidad del dataset —aleatorización más verdad causal sintética— permite estimar efectos y juzgarlos contra la verdad, algo imposible con datos reales. Sin este hito, la comparación de políticas podría contaminarse con la información que se pretende evaluar.
- **H02 — Separa riesgo de efecto causal estimado:** ajusta un modelo de control y uno tratado sobre sus respectivos clientes de entrenamiento y obtiene `p0_hat`, `p1_hat` y `uplift_hat` en prueba; muestra clientes de alto riesgo con bajo efecto y viceversa. Primera aparición en el curso de una evidencia causal como insumo de política (P303 y P305 toman una probabilidad dada); sin este hito, se contactaría a quien más riesgo tiene y no a quien la oferta puede cambiar.
- **H03 — Traduce efecto estimado en valor económico y justifica el método de selección:** `incremental_value_hat = uplift_hat × customer_value − 5`; con costo uniforme y capacidad de cardinalidad, el notebook afirma que ordenar es el optimizador exacto y prescinde de solver, exigiendo además valor positivo. Contrasta con P305, donde el ranking no garantizaba el óptimo; sin este hito, se usaría un solver por costumbre o un ranking sin justificar su exactitud.
- **H04 — Compara cuatro reglas de focalización con el mismo cupo:** con K = 160, el valor incremental verdadero es 1.446 (riesgo), 2.724 (respuesta tratada), 5.826 (uplift) y 6.288 (valor causal) (`policy_comparison.csv`); la regla de uplift tiene mayor fracción de clientes con efecto > 0,01 (0,994 frente a 0,969), pero menor valor total. Sin este hito, el criterio de éxito de la política se confundiría con la precisión del efecto.
- **H05 — Contrasta especificaciones del modelo contra la verdad sintética:** compara el T-learner con y sin término cuadrático de compromiso digital y descarta el que recupera peor el efecto (aserción del notebook). Sin este hito, la elección de variables del insumo causal no tendría verificación; el límite es que la comparación no se persiste.
- **H06 — Muestra rendimientos decrecientes al ampliar el cupo:** con 10 %, 20 % y 30 % del lote, el valor total crece (3.664, 6.288, 8.285) y el valor por oferta cae (45,8, 39,3, 34,5) (`capacity_sensitivity.csv`). Sin este hito, la capacidad parecería una restricción sin costo marginal.
- **H07 — Gobierna la recomendación con banda de revisión y plan de monitoreo:** marca `requires_human_review` cuando el valor estimado está a ±0,50 del corte de selección, asigna `decision_status` «review_required» o «pending_approval» y persiste `monitoring_plan.csv` con cuatro métricas, cada una con cadencia, gatillo, acción (bloquear, suspender, recalibrar, escalar) y autoridad. Primera aparición en el curso de un plan de monitoreo con acciones de respuesta; sin este hito, el monitoreo seguiría siendo una lista de métricas sin consecuencia.
- **H08 — Separa registro operativo de evidencia de validación:** `targeting_decisions.csv` y `decision_register.csv` no exponen columnas de verdad; los valores verdaderos sólo aparecen en `policy_comparison.csv` y `capacity_sensitivity.csv`. Sin este hito, el registro operativo mezclaría información no disponible al decidir.

### Inventario técnico de implementación

- **Introduce:** T-learner con `Pipeline(StandardScaler, LogisticRegression)`; partición estratificada por tratamiento; término cuadrático; congelamiento de políticas antes de la evaluación; evaluación contra verdad sintética (correlación y MAE del efecto).
- **Introduce:** banda de revisión alrededor del corte; plan de monitoreo con acción y autoridad por métrica.
- **Extiende:** comparación de reglas con igual capacidad (P305) y sensibilidad a capacidad (P305); registro con estado de aprobación (P303, P305).
- **Aplica en nuevo caso:** función de ranking determinista con desempate por `customer_id`; figura de planeación persistida.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Riesgo vs efecto causal | H01–H02, H05 | Aleatorización; T-learner; verdad sintética oculta | Validación posible sólo por ser sintético. |
| Valor incremental y selección exacta | H03–H04 | Efecto × valor − costo; orden con capacidad | Costo uniforme de 5; cupo 20 %. |
| Capacidad y rendimiento decreciente | H06 | 10/20/30 % evaluados con verdad | Evaluación con información no observable. |
| Gobierno operativo | H07–H08 | Banda ±0,50; registro; plan de monitoreo | Monitoreo declarado, no ejecutado. |

### Relación técnica con actividades anteriores

Nuevo método (inferencia causal con modelos predictivos) al servicio del mismo producto de política de priorización bajo capacidad que P305. Comparte con P300 el dominio de campañas de contacto, pero pasa de alternativas agregadas a clientes individuales. Extiende el gobierno de P303–P305 con un plan de monitoreo accionable. No hay duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Validación sin filtración | S01, S03 | `implementation/prescriptiva/P306_credit_campaign_targeting/data/campaign.csv`; `implementation/prescriptiva/P306_credit_campaign_targeting/data/synthetic_truth.csv`; `implementation/prescriptiva/P306_credit_campaign_targeting/professor/notebook.ipynb`: aserciones iniciales, `train_test_split`, carga tardía de la verdad | Caso sintético; la verdad no existe en operación. |
| H02 — Riesgo vs efecto | S02 | notebook: `control_pipeline`, `treated_pipeline`, `uplift_hat`, ejemplos contrastantes | Modelo logístico simple; sin intervalos. |
| H03 — Valor y selección exacta | S02, S04 | notebook: `incremental_value_hat`, bloque «DECISION MODEL», `rank_top_k` | Costo de intervención fijo y uniforme. |
| H04 — Cuatro reglas | S03, S04 | `implementation/prescriptiva/P306_credit_campaign_targeting/submission/policy_comparison.csv` | Valores verdaderos sintéticos; política aplicada al mismo lote de prueba. |
| H05 — Especificación del modelo | S02, S03 | notebook: `FEATURES_RAW`, `uplift_correlation_raw`, aserción final | No persistido. |
| H06 — Rendimientos decrecientes | S03 | `implementation/prescriptiva/P306_credit_campaign_targeting/submission/capacity_sensitivity.csv` | Tres niveles; evaluados con verdad. |
| H07 — Banda y monitoreo | S05 | notebook: `selection_cutoff`, `review_band`, `monitoring_plan`; `implementation/prescriptiva/P306_credit_campaign_targeting/submission/decision_register.csv`; `implementation/prescriptiva/P306_credit_campaign_targeting/submission/monitoring_plan.csv`; `submission/policy_contract.json` | El valor 0,50 de la banda no figura en el contrato; los gatillos «desviación material» no tienen umbral. |
| H08 — Registro vs validación | S05 | `submission/targeting_decisions.csv`; `submission/decision_register.csv`; `submission/policy_comparison.csv` | La prueba no verifica esta separación. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético y verdad oculta | `data/campaign.csv`, `data/synthetic_truth.csv` | 2.000 clientes; tratamiento aleatorio; procedencia sintética sin generador visible. |
| S02 | Insumo causal | Notebook: partición, `FEATURES`, T-learner, término cuadrático | Dos logísticas; `customer_value` excluido de las variables. |
| S03 | Validación de políticas | Notebook: `true_policy_value`, `policy_comparison`, `capacity_sensitivity`; CSV respectivos | Depende de la verdad sintética. |
| S04 | Regla de selección | Notebook: `rank_top_k`, K = 160, costo 5 | Orden exacto sólo con costo uniforme. |
| S05 | Producto/gobierno | `policy_contract.json`, `decision_register.csv`, `monitoring_plan.csv`, `targeting_decisions.csv`, planeador PNG | Banda no documentada en el contrato; sin grupo de control en la operación propuesta. |
| S06 | Pruebas | `tests/test_activity.py` | Sólo exige al menos un archivo en `submission/`. |

### Contrato de evidencia actual

- **Notebook o código:** todo en `professor/notebook.ipynb`; valida, separa datos, ajusta el T-learner, define cuatro reglas, las congela, evalúa con verdad sintética, analiza capacidad, construye gobierno y exporta.
- **`submission/`:** siete artefactos: decisiones de focalización (800 filas), registro de decisiones (800 filas), plan de monitoreo (4 filas), contrato JSON, comparación de políticas (4 filas), sensibilidad (3 filas) y planeador PNG.
- **Pruebas:** `test_submission_contains_an_artifact` sólo exige que exista algún archivo distinto de `.gitkeep`; no nombra artefactos ni verifica contenido.
- **Trazabilidad:** P306 mapea `prescriptiva.C02`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P305:** comparación de reglas con igual capacidad, sensibilidad a capacidad y contraste ranking/optimizador; de P303, registro con estado de aprobación.
- **Habilita para Pyyy:** `monitoring_plan.csv` reaparece como formato en P308; P320 retoma una política de contacto con grupos, sin artefacto compartido demostrable.

## Trazabilidad y auditoría

P306 está mapeada a `prescriptiva.C02`, `C04` y `C05`. La evidencia sostiene C02 (política computable que distingue evidencia predictiva/causal de la decisión), C04 (aprobación humana, banda de revisión, registro) y C05 (plan de monitoreo con gatillos y acciones, límite de equidad declarado). También ejerce C01 (contrato) y C03 (validación contra verdad y sensibilidad) sin mapearlos. Coincide con el producto previsto («política de contacto con restricción de exposición») salvo en que la restricción implementada es un cupo de capacidad, no de exposición. El producto de Analytics es una política gobernada; el T-learner contribuye. Límite principal: su validación descansa en una verdad sintética y la operación propuesta no conserva un grupo de control para medir el efecto observado.
