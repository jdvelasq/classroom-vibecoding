# P403 — Model testing con pytest: compuertas de un clasificador congelado

## Actividad actual implementada

**Implementación:** `implementation/productos/P403_model_testing_pytest/`.

### Preguntas analíticas actuales

- ¿Sigue cumpliendo un clasificador ya entrenado los umbrales de desempeño y las expectativas de interfaz necesarias para seguir habilitado en operación?

El notebook del profesor abre con: «El modelo llega entrenado; hay que comprobar que sigue siendo confiable al operarlo». `ESTIMATOR.pkl` (1256 bytes) se carga sin reentrenar; sus columnas se leen de `feature_names_in_` (`texture_mean`, `compactness_mean`). `data/model_test_set.csv` tiene 114 filas con esas dos variables y `target` binario. El significado de `target`, el origen del modelo y el de los datos no están documentados. El producto persistido es `submission/model_test_report.json`: accuracy 0,754, balanced accuracy 0,731 y AUC 0,842 sobre 114 filas, frente a umbrales 0,70, 0,70 y 0,80.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** decidir si el artefacto «sigue habilitado»; usuario y autoridad no evidenciados.
- **Producto terminal:** `submission/model_test_report.json` con variables, filas evaluadas y métricas; compuerta de desempeño en `professor/test_main.py`.
- **Uso y límite:** permite bloquear un artefacto que cae bajo umbrales fijados. No justifica los umbrales («umbral operativo acordado» sin parte que acuerde), no relaciona errores con su costo y no dice qué ocurre si la compuerta falla.
- **Disciplinas contribuyentes:** métricas de clasificación de scikit-learn y pruebas automatizadas sirven a la habilitación de un modelo; no se enseña el método predictivo.

### Highlights de contribución

- **H01 — Evalúa un artefacto congelado a través de su propia interfaz:** `load_model_and_test_set` carga `ESTIMATOR.pkl` con `pickle` y selecciona las columnas del conjunto con `model.feature_names_in_`, sin reentrenar. Primera aparición de un modelo como artefacto operado en el curso. Sin este hito, la secuencia no distinguiría entre construir un modelo y verificar uno recibido.
- **H02 — Traduce umbrales operativos en una compuerta automatizada:** `MIN_ACCURACY`, `MIN_BALANCED_ACCURACY` y `MIN_AUC` se verifican en `test_01_model_satisfies_its_operational_thresholds`, que falla si el artefacto o el conjunto cambian y el desempeño cae. Los valores persistidos superan los umbrales con márgenes de 0,054, 0,031 y 0,042. Extiende la compuerta de datos de P402 a un modelo. Sin este hito, la habilitación del modelo no tendría condición verificable.
- **H03 — Separa familias de pruebas de modelo:** el notebook define cuatro verificaciones con `assert`: interfaz (longitud, clases y probabilidades en [0, 1] que suman 1), comportamiento conocido (dos casos de referencia con `probabilities[1] > probabilities[0]`), desempeño en holdout y puntuación reproducible (dos llamadas con salida igual). Sólo la de desempeño pasa a `main.py`, al reporte persistido y a `pytest`; el reporte del notebook (con `thresholds` y `tests`) no es el persistido. Sin este hito, «probar un modelo» se reduciría a una métrica.
- **H04 — Expone una clase asimétrica y un objetivo sin semántica (caso y datos):** se exige balanced accuracy además de accuracy, y el reporte muestra 0,731 frente a 0,754; el caso de comportamiento conocido codifica que valores mayores de ambas variables deben dar mayor probabilidad de clase 1. Ninguna de las dos decisiones se justifica con la distribución de clases ni con el significado de `target`, que no está documentado. Sin este hito, la compuerta parecería neutral; con él queda visible que su confiabilidad depende de una semántica del caso ausente.

### Inventario técnico de implementación

- **Introduce:** carga de modelo serializado; selección de variables por `feature_names_in_`; métricas `accuracy_score`, `balanced_accuracy_score`, `roc_auc_score`; umbrales como constantes; pruebas de interfaz, comportamiento de referencia y reproducibilidad (en notebook).
- **Extiende:** compuerta con reporte persistido de P402, ahora sobre un modelo.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Artefacto congelado | H01 | `pickle` + `feature_names_in_` | Origen del modelo no documentado. |
| Compuerta de desempeño | H02 | Tres umbrales en `pytest` | Umbrales sin justificación. |
| Pruebas de interfaz y comportamiento | H03 | Asserts sobre forma, probabilidades, monotonía de referencia y reproducibilidad | Sólo en notebook; no persistidas. |
| Métrica sensible a clases | H04 | Balanced accuracy y AUC | Distribución de clases no mostrada. |

### Relación técnica con actividades anteriores

Cambia el objeto verificado: de código (P400–P401) y datos (P402) a un modelo entregado. Misma técnica de compuerta con reporte persistido que P402, con nueva exigencia (métricas con umbral). Comparte artefacto y filas con P404.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Artefacto congelado | S01, S02 | `implementation/productos/P403_model_testing_pytest/ESTIMATOR.pkl`; `implementation/productos/P403_model_testing_pytest/professor/main.py`: `load_model_and_test_set` | Binario no inspeccionable en el digest. |
| H02 — Compuerta | S02, S05, S04 | `implementation/productos/P403_model_testing_pytest/professor/test_main.py`: `test_01_model_satisfies_its_operational_thresholds`; `implementation/productos/P403_model_testing_pytest/submission/model_test_report.json` | La evaluación del estudiante no la ejecuta. |
| H03 — Familias de pruebas | S03 | `implementation/productos/P403_model_testing_pytest/professor/notebook.ipynb`: `test_prediction_interface`, `test_known_behavior`, `test_holdout_performance`, `test_reproducible_scoring` | No son pruebas `pytest`. |
| H04 — Clase y semántica | S01, S03, S04 | `implementation/productos/P403_model_testing_pytest/data/model_test_set.csv`; `implementation/productos/P403_model_testing_pytest/submission/model_test_report.json` | El desbalance no se cuantifica. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Artefacto y datos | `ESTIMATOR.pkl`; `data/model_test_set.csv` | Dos variables; `target` sin semántica. |
| S02 | Evaluación y umbrales | `professor/main.py` | Tres umbrales fijos. |
| S03 | Material del profesor | `professor/notebook.ipynb` | Cuatro familias de pruebas; reporte distinto. |
| S04 | Producto | `submission/model_test_report.json` | Sólo métricas; sin umbrales ni estado. |
| S05 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Evaluación sólo por existencia. |
| S06 | Interfaz del estudiante | `src/main.py` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** carga el artefacto, calcula métricas y persiste el reporte; el notebook además verifica interfaz, comportamiento de referencia y reproducibilidad.
- **`submission/`:** `model_test_report.json` con variables, 114 filas y tres métricas.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista el reporte. `professor/test_main.py` verifica los tres umbrales con el artefacto y datos reales; no verifica interfaz ni reproducibilidad.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** práctica de compuerta con reporte de P402; ningún artefacto.
- **Habilita para Pyyy:** P404 usa un `ESTIMATOR.pkl` del mismo tamaño (1256 bytes) y su `new_inputs.csv` (114 filas) coincide en sus primeras filas con `model_test_set.csv` sin `target`.

## Trazabilidad y auditoría

Entrada revisada: P403 → `productos.C02`, `productos.C03`, `productos.C05`. C03 está bien sostenido (validación de un modelo frente a umbrales de uso); C02 por la compuerta automatizada; C05 sólo indirectamente: es una verificación puntual, no monitoreo. El producto es la decisión de habilitar un modelo; MLOps y métricas sirven a esa decisión. Límite de identidad: sin usuario, sin semántica del objetivo y sin justificación de umbrales, la «capacidad analítica» operada no es identificable.
