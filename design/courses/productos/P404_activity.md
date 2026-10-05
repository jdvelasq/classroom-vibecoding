# P404 — Model input testing: compatibilidad de entradas nuevas con las de entrenamiento

## Actividad actual implementada

**Implementación:** `implementation/productos/P404_model_input_testing_pytest/`.

### Preguntas analíticas actuales

- ¿Se parecen las nuevas entradas a las conocidas durante el entrenamiento lo suficiente como para aplicarles el modelo?

El notebook del profesor abre con: «Antes de aplicar un modelo de priorización, el equipo debe decidir si las nuevas entradas se parecen a las conocidas durante el entrenamiento». `data/training_inputs.csv` (455 filas) y `data/new_inputs.csv` (114 filas) contienen `texture_mean` y `compactness_mean`; `ESTIMATOR.pkl` sólo se usa para leer esas columnas. `assess_inputs` entrena un `IsolationForest(contamination=0.05, random_state=0)` con las entradas de entrenamiento y declara compatible un conjunto si su tasa de anomalías no supera `MAX_ANOMALY_RATE = 0.15`. Un conjunto desplazado se construye sumando 100 a `texture_mean`. `submission/input_distribution_report.json` registra tasa 0,026 (compatible) para las entradas nuevas y 1,0 (incompatible) para las desplazadas. Qué se prioriza y quién decide no está especificado.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** habilitar o no el scoring de un lote; usuario declarado de forma genérica («el equipo»); el modelo se describe como «de priorización» sin objeto.
- **Producto terminal:** `submission/input_distribution_report.json` con tasa de anomalías y decisión de compatibilidad por conjunto.
- **Uso y límite:** permite rechazar un lote claramente fuera del dominio de entrenamiento. No calibra la sensibilidad ante desplazamientos moderados, no identifica qué variable se desplazó y no define la acción ante incompatibilidad.
- **Disciplinas contribuyentes:** detección de anomalías (scikit-learn) y pruebas automatizadas al servicio de la habilitación de un modelo.

### Highlights de contribución

- **H01 — Alinea las entradas con la interfaz declarada del artefacto:** `load_inputs` toma `feature_names_in_` del estimador y selecciona esas columnas en ambos conjuntos «para evitar evaluar un conjunto con una interfaz distinta». El modelo no puntúa; sólo define el contrato de entrada. Extiende P403 de verificar el modelo a verificar sus insumos. Sin este hito, la compatibilidad se evaluaría sobre columnas arbitrarias.
- **H02 — Decide compatibilidad con un detector entrenado en el dominio conocido:** `IsolationForest` se ajusta sobre `training_inputs` y la decisión es una tasa agregada frente a 0,15; `contamination=0.05` implica que el detector marca por construcción una fracción de las propias entradas de entrenamiento. La tasa persistida para entradas nuevas es 0,026. Primera comprobación de distribución de entrada en el curso. Sin este hito, el modelo se aplicaría a cualquier lote con las columnas correctas.
- **H03 — Contrasta con un desplazamiento sintético controlado (caso y datos):** las «entradas nuevas» coinciden en sus primeras filas con el holdout de P403 sin `target`, por lo que provienen de la misma fuente que el entrenamiento y su compatibilidad es esperable; no hay entradas de producción reales. El único contraste es sintético: +100 en una variable, que lleva la tasa a 1,0 y se muestra en un diagrama de dispersión de las tres nubes. Sin este hito, el detector no mostraría que puede rechazar; con él queda visible que sólo se ensaya un desplazamiento extremo.
- **H04 — Prueba la compuerta en ambos sentidos con los datos reales:** `test_01_accepts_the_expected_input_distribution` exige compatibilidad de `new_inputs` y `test_02_rejects_a_shifted_input_distribution` exige rechazo del conjunto desplazado. Sin este hito, una compuerta que aceptara todo pasaría inadvertida.

### Inventario técnico de implementación

- **Introduce:** `IsolationForest` con semilla como detector de compatibilidad; tasa de anomalías con umbral; desplazamiento sintético como caso de contraste; diagrama de dispersión entrenamiento/nuevas/desplazadas.
- **Extiende:** uso de `feature_names_in_` de P403.
- **Reutiliza:** el artefacto y las filas de P403; pruebas en `professor/test_main.py` con carga por `importlib`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Contrato de entrada del modelo | H01 | `feature_names_in_` | Sin tipos ni rangos. |
| Compatibilidad de distribución | H02 | `IsolationForest` + tasa ≤ 0,15 | Umbral y contaminación sin justificación. |
| Contraste controlado | H03 | +100 en `texture_mean`; dispersión | Desplazamiento extremo y único. |
| Compuerta bidireccional | H04 | Prueba de aceptación y de rechazo | No evalúa al estudiante. |

### Relación técnica con actividades anteriores

Mismo artefacto que P403 con nueva exigencia: verificar insumos en lugar de desempeño. Nuevo método (detección de anomalías) al servicio de la habilitación del mismo modelo. Frente a P402, pasa de reglas declarativas sobre valores a una comparación con la distribución de entrenamiento.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Interfaz del artefacto | S01, S02 | `implementation/productos/P404_model_input_testing_pytest/professor/main.py`: `load_inputs`; `implementation/productos/P404_model_input_testing_pytest/ESTIMATOR.pkl` | El estimador no puntúa. |
| H02 — Detector | S02, S04 | `implementation/productos/P404_model_input_testing_pytest/professor/main.py`: `assess_inputs`, `MAX_ANOMALY_RATE`; `implementation/productos/P404_model_input_testing_pytest/submission/input_distribution_report.json` | Tasa agregada, sin diagnóstico por variable. |
| H03 — Desplazamiento sintético | S01, S03 | `implementation/productos/P404_model_input_testing_pytest/data/new_inputs.csv`; `implementation/productos/P404_model_input_testing_pytest/data/training_inputs.csv`; `implementation/productos/P404_model_input_testing_pytest/professor/notebook.ipynb` | Coincidencia con P403 observada en las primeras filas. |
| H04 — Pruebas bidireccionales | S05 | `implementation/productos/P404_model_input_testing_pytest/professor/test_main.py`: `test_01`, `test_02` | Evaluación del estudiante sólo por existencia. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Datos y artefacto | `data/training_inputs.csv`; `data/new_inputs.csv`; `ESTIMATOR.pkl` | Entradas nuevas de la misma fuente. |
| S02 | Detector y umbral | `professor/main.py` | `contamination=0.05`; umbral 0,15. |
| S03 | Material del profesor | `professor/notebook.ipynb` | Reporte con `rows` y `max_anomaly_rate`, distinto del persistido. |
| S04 | Producto | `submission/input_distribution_report.json` | Dos conjuntos; sin umbral registrado. |
| S05 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Evaluación sólo por existencia. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** alinea columnas, entrena el detector, evalúa ambos conjuntos y persiste el reporte; el notebook añade el gráfico de dispersión.
- **`submission/`:** `input_distribution_report.json` con tasas y compatibilidad de las entradas nuevas y desplazadas.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista el reporte. `professor/test_main.py` verifica aceptación y rechazo con datos reales; no verifica sensibilidad intermedia.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P403:** artefacto `ESTIMATOR.pkl` (mismo tamaño) y filas del holdout como `new_inputs.csv`.
- **Habilita para Pyyy:** no evidenciada dentro de P405–P413.

## Trazabilidad y auditoría

Entrada revisada: P404 → `productos.C02`, `productos.C03`, `productos.C05`. C03 sostenido (validación de insumos frente al uso del modelo); C05 parcialmente: la comparación con la distribución de entrenamiento es un antecedente de monitoreo, ejecutado una vez. El producto es la decisión de habilitar el scoring de un lote; la detección de anomalías sirve a esa decisión. El objeto priorizado y el usuario no se especifican, lo que limita la identidad de la capacidad operada.
