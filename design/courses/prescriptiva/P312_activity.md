# P312 — Sensibilidad y tradespace: promesa de entrega

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P312_sensibilidad_y_tradespace/`.

### Preguntas analíticas actuales

- ¿Cuándo debe el servicio mantener, revisar o suspender la promesa de entrega en un día?

Usa tres opciones de servicio (`service_options.csv`: estándar, dos días y un día; costo mensual 0, 18.000 y 42.000; 10.000 clientes; ganancia de retención 0, 0.018 y 0.055). `professor/main.py` fija en constantes el valor por cliente (260) y el presupuesto mensual (42.000). No hay procedencia ni declaración de caso real o sintético. El producto es una regla mensual que activa la promesa de un día cuando la ganancia de retención supera un umbral de equilibrio, con salvaguardas, autoridad y gatillos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** promesa de entrega mensual para clientes elegibles; gerencia comercial como acción rutinaria, dirección comercial para excepciones.
- **Producto terminal:** `delivery_promise_policy.json` con acción, condición, `retention_gain_threshold` 0.0162 y presupuesto, salvaguardas, autoridad, gatillos y monitoreo; respaldado por `tradespace.csv` y `sensitivity_review.csv`.
- **Uso y límite:** convierte la sensibilidad de un supuesto (ganancia de retención) en un umbral operativo de revisión. Varía un único multiplicador aplicado a todas las opciones a la vez; no hay incertidumbre estimada, aunque la salvaguarda menciona un «intervalo de incertidumbre» que el taller no calcula. El «tradespace» tiene un solo criterio (valor neto) y tres opciones.
- **Disciplinas contribuyentes:** análisis de equilibrio y sensibilidad unidimensional; pandas.

### Highlights de contribución

- **H01 — Recorre un supuesto crítico y observa cuándo cambia la decisión:** `evaluate_sensitivity` escala la ganancia de retención por 0.20–1.25 y registra la opción ganadora; `sensitivity_review.csv` muestra estándar (P0) con 0.2 y un día (P2) desde 0.3 (valor neto 900) hasta 1.0 (101.000). Extiende las sensibilidades exploratorias de P304/P305/P309 a una tabla persistida que localiza el cambio de decisión; sin este hito, la recomendación base (P2, 101.000 en `tradespace.csv`) parecería incondicional.
- **H02 — Traduce el punto de equilibrio en el umbral de una regla:** `policy_record` calcula `monthly_cost / (monthly_customers × CUSTOMER_VALUE)` para P2 y lo publica como `retention_gain_threshold` (0.0162), con gatillo «revisar si la ganancia observada en cuatro semanas es menor o igual al umbral». Primera vez en el curso que el gatillo de revisión es la magnitud observable que hace indiferente la decisión, no una regla ad hoc; sin este hito, la revisión no estaría anclada al supuesto que la sostiene.
- **H03 — Declara una opción como no seleccionada en el rango analizado:** la salvaguarda `dominated_option` indica que la entrega en dos días no se selecciona en los escenarios analizados y «no debe mantenerse por costumbre». Ésta es la particularidad del caso: tres opciones escalonadas en costo y efecto, donde el multiplicador común hace que P1 nunca sea la ganadora en la grilla. Límite: la afirmación vale para la grilla y para un multiplicador común a todas las opciones; no se exploran cambios relativos entre opciones.

### Inventario técnico de implementación

- **Introduce:** umbral de equilibrio derivado; sensibilidad unidimensional con registro de la opción seleccionada; gatillo de revisión anclado al supuesto.
- **Extiende:** sensibilidad separada de la recomendación base (P304, P309) a artefacto persistido.
- **Reutiliza:** funciones en `main.py`; registro JSON con autoridad rutinaria/excepción (P311).
- **Aplica en nuevo caso:** comparación de valor neto entre opciones discretas.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Sensibilidad de un supuesto | H01 | Multiplicador 0.20–1.25 sobre retención | Un solo parámetro; multiplicador común. |
| Umbral de equilibrio | H02 | 42.000 / (10.000 × 260) = 0.0162 | Sólo P2 frente a P0. |
| Opción no seleccionada | H03 | Salvaguarda `dominated_option` | Afirmación sobre la grilla, no demostración general. |

### Relación técnica con actividades anteriores

Nuevo método (umbral de equilibrio) al servicio del mismo producto (regla con revisión). Las sensibilidades de P304, P305, P309 eran exploratorias y no alteraban el contrato; P312 convierte la sensibilidad en el gatillo. P309 hace algo análogo al tomar 0.30 como gatillo de escalamiento desde una variante; P312 lo deriva analíticamente. Respecto del producto previsto en `activity-architecture.md` («regla de revisión al cambiar un supuesto crítico»), coincide. El término «tradespace» no corresponde a un análisis multicriterio: hay un solo objetivo.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Sensibilidad | S02 | `implementation/prescriptiva/P312_sensibilidad_y_tradespace/professor/main.py`: `evaluate_sensitivity`; `implementation/prescriptiva/P312_sensibilidad_y_tradespace/submission/sensitivity_review.csv`; `implementation/prescriptiva/P312_sensibilidad_y_tradespace/submission/tradespace.csv` | Grilla discreta; el punto exacto de cambio no se calcula en la tabla. |
| H02 — Umbral en la regla | S03 | `implementation/prescriptiva/P312_sensibilidad_y_tradespace/professor/main.py`: `policy_record`; `implementation/prescriptiva/P312_sensibilidad_y_tradespace/submission/delivery_promise_policy.json` | La constante `REVIEW_RETENTION_GAIN` se define pero no se usa. |
| H03 — Opción no seleccionada | S01, S03 | `implementation/prescriptiva/P312_sensibilidad_y_tradespace/data/service_options.csv`; `delivery_promise_policy.json` | Presupuesto igual al costo de P2: la restricción no discrimina. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso y opciones | `data/service_options.csv`; constantes `CUSTOMER_VALUE`, `MONTHLY_BUDGET` | Sin procedencia; valor por cliente en código. |
| S02 | Sensibilidad | `main.py`: `evaluate`, `evaluate_sensitivity`; `sensitivity_review.csv` | Un supuesto, multiplicador común. |
| S03 | Regla, umbral y salvaguardas | `main.py`: `policy_record`; `delivery_promise_policy.json` | Salvaguarda de incertidumbre sin intervalo calculado. |
| S04 | Pruebas e interfaz | `tests/test_activity.py`; ruta `activity_dir / 'src'` | Pruebas de existencia; `src/` sin `main.py`. |

### Contrato de evidencia actual

- **Notebook o código:** evalúa opciones, recorre el multiplicador, muestra acción/umbral/gatillo y ejecuta `main()` para persistir.
- **`submission/`:** `tradespace.csv`, `sensitivity_review.csv`, `delivery_promise_policy.json`.
- **Pruebas:** verifican existencia de los tres archivos; no comprueban umbral, selección ni columnas.
- **Trazabilidad:** P312 mapea `prescriptiva.C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P311:** estructura de registro JSON con autoridad rutinaria/excepción, gatillos y monitoreo (misma forma de claves). De P304/P309, práctica de separar sensibilidad y recomendación base.
- **Habilita para Pyyy:** no evidenciada; P313–P315 incluyen sensibilidades sin referencia a P312.

## Trazabilidad y auditoría

P312 está mapeada a `prescriptiva.C03` y `C05` en `implementation/prescriptiva/traceability.yaml`. C03 se sostiene por la sensibilidad y el umbral; C05 por gatillos de revisión, suspensión y recalibración. El contrato también declara autoridad rutinaria y de excepción (evidencia de `C04`, no mapeada). El producto de Analytics es una regla mensual de promesa de entrega con umbral de revisión; el análisis de equilibrio contribuye. Límites: un supuesto, sin incertidumbre cuantificada, y nombre «tradespace» sin múltiples criterios.
