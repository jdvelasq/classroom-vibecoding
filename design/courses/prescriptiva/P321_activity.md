# P321 — Comunicación y seguimiento de políticas: registro operativo de una política de capacidad

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/`.

### Preguntas analíticas actuales

- ¿Cómo dejamos una política de capacidad lista para que una autoridad la opere, supervise y revise?

`data/recommendation.csv` tiene una sola fila con la decisión recomendada (`refuerzo_flexible`), la alternativa no elegida (`capacidad_actual`), el supuesto (`demanda_esperada`), el indicador (`service_rate`) y el gatillo (`menor_a_0.90`). `professor/main.py` transforma esa fila en un registro operativo de 17 campos; los cinco primeros conceptos vienen del CSV y el resto (contexto, cadencia, necesidad de respuesta, objetivo, restricción, salvaguarda, modo de ejecución, autoridad, meta del indicador, responsable y acción de revisión) está escrito en el código. El notebook de profesor carga la fila, invoca la función y guarda el registro.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** operar, supervisar y revisar una política de capacidad semanal; la autoridad declarada es la «Dirección de operaciones».
- **Producto terminal:** `submission/policy_register.csv`, una fila con acción, alternativa, supuesto, objetivo, restricción, salvaguarda, autoridad, indicador, meta, gatillo, responsable y acción de revisión.
- **Uso y límite:** muestra qué debe registrarse para que una recomendación sea operable y revisable. No produce ni evalúa la política: la recomendación llega dada, no hay datos de seguimiento con los que aplicar el gatillo y la mayor parte del registro es texto fijo.
- **Disciplinas contribuyentes:** documentación estructurada de decisiones y diseño de indicadores sirven a la operación de una política.

### Highlights de contribución

- **H01 — Separa recomendación de registro operativo (caso y datos):** el dato de entrada es una única recomendación ya tomada, no observaciones; la actividad no decide sino que documenta. El registro conserva la alternativa no elegida y el supuesto del que depende la recomendación, junto a la acción. Sin este hito, la recomendación quedaría sin el contexto que permite saber cuándo deja de valer.
- **H02 — Vincula indicador, meta, gatillo, responsable y acción de revisión:** el registro declara `service_rate >= 0.90` como meta, `service_rate < 0.90 durante la revisión semanal` como gatillo, la Dirección de operaciones como responsable y «revisar demanda, capacidad y continuidad de la política» como acción. Sin este hito, el monitoreo sería una lista de métricas sin consecuencia.
- **H03 — Hace visible la gobernanza en un artefacto verificado:** la prueba `test_02` exige que el registro tenga `recommended_action`, `assumption`, `decision_authority`, `indicator`, `review_trigger` y `review_owner`. Es una de las pocas pruebas del curso que verifica columnas de gobernanza y no sólo presencia de archivos. Sin este hito, la estructura del registro no estaría protegida.

### Inventario técnico de implementación

- **Introduce:** registro operativo de política como tabla de una fila con 17 campos.
- **Reutiliza:** los elementos del contrato de política (cadencia, necesidad de respuesta, salvaguarda, autoridad, gatillo) presentes desde P300, ahora en formato tabular.
- **Aplica en nuevo caso:** política de capacidad de atención semanal.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Registro de decisión | H01 | Acción, alternativa no elegida y supuesto en una fila | Recomendación dada; sin evidencia que la sustente. |
| Seguimiento | H02 | Indicador, meta, gatillo, responsable, acción de revisión | Sin datos de seguimiento; el gatillo no se aplica. |
| Gobernanza verificada | H03 | Prueba de columnas de gobernanza | No verifica valores. |

### Relación técnica con actividades anteriores

La arquitectura ubica P321 como núcleo transversal de operación y monitoreo. El contexto (capacidad, meta de servicio 0,90) es cercano al de P311, que compara políticas de capacidad con meta de servicio 0,90, pero P321 no consume artefactos de P311 ni de otra actividad: su recomendación está escrita en un CSV propio. Frente a los contratos JSON de P304–P320, P321 cambia el formato (registro tabular) y añade la alternativa no elegida, sin evaluar nada nuevo. Posible solapamiento con los contratos que ya cierran cada taller; requiere decisión posterior de curso sobre si P321 debe operar una política producida antes.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Recomendación frente a registro | S01, S02 | `implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/data/recommendation.csv`; `implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/professor/main.py`: `create_policy_register` | La mayor parte del registro es texto fijo en el código. |
| H02 — Seguimiento con consecuencia | S02, S03 | `implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/submission/policy_register.csv` | No hay datos para evaluar el gatillo. |
| H03 — Gobernanza verificada | S04 | `implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/tests/test_activity.py`: `test_02` | Verifica columnas, no valores. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Recomendación de entrada | `data/recommendation.csv` | Una fila; no proviene de otra actividad. |
| S02 | Construcción del registro | `professor/main.py`; `professor/notebook.ipynb` | Campos de gobernanza escritos en el código. |
| S03 | Registro entregado | `submission/policy_register.csv` | Una política; sin historial de revisiones. |
| S04 | Pruebas | `tests/test_activity.py` | Existencia y seis columnas. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook vacío. |

### Contrato de evidencia actual

- **Notebook o código:** carga la recomendación, construye el registro y lo guarda.
- **`submission/`:** `policy_register.csv`.
- **Pruebas:** `test_01` exige que exista el registro; `test_02` exige seis columnas de gobernanza. No verifican valores ni coherencia entre meta y gatillo.
- **Trazabilidad:** P321 mapea `prescriptiva.C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** el patrón de contrato de política; no recibe artefactos (el contexto de capacidad y meta 0,90 recuerda a P311 sin dependencia demostrable).
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P321 está mapeada a `prescriptiva.C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C04 se sostiene en autoridad, modo de ejecución y salvaguarda declarados; C05 en indicador, meta, gatillo y acción de revisión, sin datos de seguimiento. Frente a la arquitectura («registro, indicadores y gatillos de revisión», núcleo transversal) el registro existe, pero no se conecta con una política producida en el curso ni se ejercita el monitoreo. El producto de Analytics es la documentación operativa de una política; no hay análisis que la sustente dentro del taller.
