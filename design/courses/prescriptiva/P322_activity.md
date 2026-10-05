# P322 — Valor de la información y experimentación: medir antes de lanzar

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/`.

### Preguntas analíticas actuales

- ¿Cuándo conviene medir antes de comprometer el presupuesto de una campaña?

`data/decision_scenarios.csv` tiene dos estados de demanda con probabilidad y valor de lanzar (alta: 0,45 y 120.000; baja: 0,55 y −80.000). `professor/main.py` fija el costo del estudio (8.000) y su precisión (0,85), compara «lanzar ahora» con «medir antes y lanzar si la señal es positiva», y persiste la comparación, el contrato y el monitoreo. El notebook de profesor sólo llama a `main()`. No hay declaración de procedencia ni de carácter sintético; los valores son ilustrativos.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** medir antes de lanzar una campaña y lanzar sólo con señal positiva; el contrato asigna la autorización al «responsable de campaña» y las excepciones al «responsable comercial».
- **Producto terminal:** `information_value.csv` (valor esperado de cada opción y decisión), `policy_contract.json` con política de acción por resultado de la medición y `policy_monitoring.csv`.
- **Uso y límite:** muestra que obtener información tiene valor cuando cambia la acción y cuesta menos de lo que evita perder. La precisión se supone simétrica, no se calcula el valor de la información perfecta, las etiquetas de decisión y sus razones están escritas en el código, y la razón persistida para «lanzar ahora» contradice su propio valor esperado.
- **Disciplinas contribuyentes:** análisis de decisiones con valor esperado y valor de la información muestral sirven a una política de medición.

### Highlights de contribución

- **H01 — Calcula el valor de medir antes de actuar (caso y datos):** con dos estados y una señal de precisión 0,85, el valor de «medir antes» descuenta el costo del estudio y evita lanzar ante señal negativa; `information_value.csv` persiste 10.000 para lanzar ahora y 31.300 para medir antes. La particularidad del caso (un estado desfavorable con pérdida grande y probabilidad mayor que el favorable) es la que da valor a la información. Sin este hito, la medición sería un costo y no una decisión.
- **H02 — Convierte el resultado de la medición en una regla de acción:** el contrato fija qué hacer con señal positiva (autorizar dentro del presupuesto) y negativa (no lanzar, conservar presupuesto y escalar una nueva hipótesis), con cadencia trimestral y necesidad de respuesta antes de comprometer el presupuesto. Sin este hito, «medir» no tendría consecuencia operativa.
- **H03 — Gobierna la medición con guardas de costo y precisión:** las guardas exigen costo de medición ≤ 8.000 y precisión observada ≥ 0,85 antes de reutilizar la medición, y prohíben exceder el presupuesto con una señal positiva; el monitoreo incluye la proporción de campañas detenidas por señal negativa y el resultado tras cada señal positiva. Sin este hito, la política de medir dependería de supuestos que nadie verifica.

### Inventario técnico de implementación

- **Introduce:** valor esperado con información muestral imperfecta; política condicionada al resultado de una medición; guardas sobre costo y precisión de la medición.
- **Reutiliza:** contrato JSON con cadencia, guardas, autoridad, monitoreo y gatillos; plan de monitoreo en CSV.
- **Aplica en nuevo caso:** campaña con demanda incierta.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Valor de la información | H01 | Valor esperado con señal de precisión 0,85 y costo 8.000 | Precisión simétrica; sin valor de información perfecta ni sensibilidad. |
| Regla condicionada a la señal | H02 | Acción por resultado positivo o negativo | — |
| Guardas de la medición | H03 | Costo, precisión, presupuesto; monitoreo de campañas detenidas | Gatillos con umbral; sin datos de seguimiento. |

### Relación técnica con actividades anteriores

P322 cierra la etapa «gobernar y aprender» de la arquitectura. Usa escenarios con probabilidad como P310 y P311, pero la decisión ya no es qué capacidad o inversión elegir sino si conviene obtener información antes de decidir. No consume artefactos previos. Nuevo método al servicio del mismo producto (una política gobernada); no hay duplicación evidente.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Valor de medir | S01, S02 | `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/data/decision_scenarios.csv`; `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/professor/main.py`: `evaluate_actions`; `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/submission/information_value.csv` | La razón persistida de «lanzar ahora» habla de «pérdida esperada» aunque su valor esperado es +10.000; las decisiones están escritas en el código. |
| H02 — Regla condicionada | S03 | `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/submission/policy_contract.json`: `action_policy` | — |
| H03 — Guardas de la medición | S03 | `policy_contract.json`: `guardrails`, `monitoring`, `review_triggers`; `implementation/prescriptiva/P322_valor_informacion_y_experimentacion/submission/policy_monitoring.csv` | La prueba sólo verifica presencia de archivos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Escenarios | `data/decision_scenarios.csv` | Dos estados; procedencia no declarada. |
| S02 | Evaluación de opciones | `professor/main.py`: `evaluate_actions`; constantes de costo y precisión | Precisión simétrica; decisiones y razones fijas. |
| S03 | Contrato y monitoreo | `submission/policy_contract.json`; `submission/policy_monitoring.csv` | — |
| S04 | Notebook presencial | `professor/notebook.ipynb`; `notebooks/notebook.ipynb` | El notebook de profesor sólo llama a `main()`, sin evidencia visual; el de estudiante está vacío. |
| S05 | Pruebas | `tests/test_activity.py` | Presencia de tres archivos. |

### Contrato de evidencia actual

- **Notebook o código:** `main.py` evalúa las dos opciones y persiste comparación, contrato y monitoreo; el notebook sólo lo ejecuta.
- **`submission/`:** `information_value.csv`, `policy_contract.json`, `policy_monitoring.csv`.
- **Pruebas:** `test_01_submission_contains_policy_evidence` exige los tres archivos. No verifica valores esperados, decisiones ni contrato.
- **Trazabilidad:** P322 mapea `prescriptiva.C01`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P310/P311:** escenarios discretos con probabilidad como insumo de decisión (práctica, no artefacto).
- **Habilita para Pyyy:** ninguna; es la última actividad.

## Trazabilidad y auditoría

P322 está mapeada a `prescriptiva.C01`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C01 se sostiene en el encuadre de la decisión de medir; C03 en la comparación de valor esperado, sin sensibilidad; C04 en autoridad y escalamiento; C05 en monitoreo y gatillos. Frente a la arquitectura («política para medir antes de actuar») el producto existe. El producto de Analytics es una política de medición gobernada; el valor de la información es evidencia. Límites de implementación: el notebook presencial no muestra el razonamiento, y la razón persistida para descartar «lanzar ahora» es incorrecta frente a su propio valor esperado positivo.
