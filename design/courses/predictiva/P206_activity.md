# P206 — Árboles y ensambles

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P206_arboles_y_ensambles/`.

### Preguntas analíticas actuales

- ¿Un árbol de decisión o un ensamble de árboles predice mejor el consumo de
  combustible (MPG) que las especificaciones lineales de P200, sobre
  exactamente la misma partición?
- ¿Qué variables sostiene esa predicción, leídas con dos métodos de
  importancia que pueden discrepar entre sí?

Reutiliza el caso Auto MPG, la partición y el contrato de preprocesamiento de
P200. Compara un árbol de decisión, un Random Forest y un modelo de
*gradient boosting* contra la línea base ingenua y la regresión lineal ya
conocidas, diagnostica el sobreajuste por profundidad, y contrasta dos
lecturas de importancia de variables con dependencia parcial.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** compara la capacidad predictiva de
  árboles y ensambles contra la regresión de P200 sobre el mismo caso; no hay
  decisión operativa nueva evidenciada (hereda el encuadre de viabilidad de
  P200 H11: si el enfoque aporta sobre adivinar, para decidir si el equipo
  sigue invirtiendo en proyectos predictivos).
- **Producto terminal:** tres modelos basados en árboles comparados por MSE
  de prueba contra la línea base ingenua y la regresión lineal de P200, con
  una doble lectura de importancia de variables (impureza y permutación) y
  una gráfica de dependencia parcial.
- **Uso y límite:** la comparación es específica de este caso y esta
  partición; la importancia y la dependencia parcial no prueban causalidad;
  más exactitud no implica mejor producto si se pierde interpretabilidad o
  estabilidad.
- **Disciplinas contribuyentes:** árboles de decisión y ensambles (bagging,
  boosting) sirven a la comparación predictiva del caso; sin ellos el curso
  no tendría una familia de modelo no lineal basada en particionar el
  espacio de entradas con reglas.

### Highlights de contribución

- **H01 — Compara contra la línea base de P200 sobre la misma partición:**
  recalcula `naive_mean_baseline` y `linear_model` con la partición y el
  `ColumnTransformer` de P200, y agrega tres modelos de árboles. El
  *gradient boosting* (MSE de prueba 5.25) y el Random Forest (5.71) superan
  con claridad la regresión lineal (10.02); un árbol único con la profundidad
  elegida por validación cruzada (15.39) no la supera.
- **H02 — Muestra el sobreajuste de un árbol sin restricción y lo corrige con
  una curva de validación:** un árbol sin límite de profundidad memoriza el
  entrenamiento (MSE de entrenamiento 0.0) sin mejorar en prueba (15.88)
  frente a limitarlo a profundidad 7 (15.39), la que minimiza el error de
  validación cruzada. Sin este hito, un árbol se leería como superior a la
  regresión sólo por ajustar mejor el entrenamiento.
- **H03 — Introduce bagging y boosting como dos formas distintas de combinar
  árboles:** un Random Forest (muchos árboles independientes, promediados) y
  un `HistGradientBoostingRegressor` (cada árbol corrige el error del
  anterior) capturan interacciones entre variables sin que el estudiante las
  escriba a mano, a diferencia de P200 H07.
- **H04 — Contrasta dos lecturas de importancia y muestra que pueden
  discrepar:** por impureza, `Cylinders` se lee como la segunda variable más
  relevante (0.21 sobre el ajuste de entrenamiento); por permutación sobre la
  muestra de prueba cae a un nivel similar a `Displacement` y `Acceleration`
  (0.03), y `Model Year` sube al primer lugar (0.25). `Origin` se fragmenta
  en tres indicadores por impureza (≈0.002 cada uno) pero se lee como una
  sola variable por permutación (0.005); ambas coinciden en que aporta poco.
- **H05 — Interroga el modelo con dependencia parcial sin leerla como
  causal:** grafica cómo cambia la predicción de MPG al mover `Horsepower` y
  `Weight` manteniendo las demás entradas en sus valores observados, con el
  límite explícito de que no es un experimento.
- **H06 — Persiste modelos, métricas e importancias reutilizables:** tres
  estimadores (`.pkl`), la comparación de MSE, la tabla de importancias con
  sus dos métodos y las dos gráficas, verificados por pruebas.

### Inventario técnico de implementación

- **Introduce:** `DecisionTreeRegressor`, `RandomForestRegressor` y
  `HistGradientBoostingRegressor` sobre el mismo contrato de partición y
  preprocesamiento de P200.
- **Introduce:** `validation_curve` para diagnosticar sobreajuste por
  profundidad del árbol.
- **Introduce:** contraste entre importancia por impureza y por permutación,
  y dependencia parcial con `PartialDependenceDisplay`.
- **Reutiliza:** partición, limpieza de nulos y `ColumnTransformer` de P200
  (H02, H03, H06), reconstruidos igual (no importados) para mantener
  comparabilidad.
- **Reutiliza:** el contrato de verificación de P200 (datos presentes y no
  vacíos; directorio de `submission/` existente y escribible) antes de
  entrenar o persistir artefactos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo/dato/producto observable | Límite |
| --- | --- | --- | --- |
| Comparación con P200 | H01 | Línea base y regresión recalculadas, más tres modelos de árboles | MSE específico de esta partición. |
| Sobreajuste y profundidad | H02 | Curva de validación sobre `max_depth` | No explora `n_estimators` ni `learning_rate`. |
| Mecanismo de ensamble | H03 | Random Forest frente a *gradient boosting* | No compara tiempo de cómputo. |
| Importancia contrastada | H04–H05 | `feature_importances.csv`; PNG de dependencia parcial | No prueba causalidad. |
| Reuso | H06 | `.pkl`, CSV, pruebas | Pruebas no inspeccionan contenido visual. |

### Relación técnica con actividades anteriores

Recibe de P200 el caso, la partición (`train_test_split(dataset, train_size=0.8,
random_state=0)`) y el contrato de preprocesamiento; los reconstruye en su
propio notebook, sin importar el código de P200, para mantener comparabilidad
sin acoplamiento entre actividades. A diferencia de P200 H07 (términos
cuadrático e interacción construidos a mano) y de P220 (búsqueda sistemática
de hiperparámetros con `GridSearchCV` sobre ElasticNet), aquí el mecanismo es
distinto: partir el espacio de entradas con reglas, en vez de especificar
interacciones o una penalización. Habilita para P220 (profundidad y número de
árboles como hiperparámetros a buscar sistemáticamente) y para P222–P224
(contrastar esta importancia con selección explícita y con contracción de
coeficientes).

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01, S02 | `implementation/predictiva/P206_arboles_y_ensambles/professor/notebook.ipynb`: `naive_mean_model`, `linear_model`, `decision_tree`, `random_forest`, `gradient_boosting`; `submission/model_comparison.csv` | MSE específico de esta partición y este caso. |
| H02 | S02 | Notebook: `full_tree`, `validation_curve`; `submission/validation_curve.png` | No explora otros hiperparámetros del árbol. |
| H03 | S02 | Notebook: `RandomForestRegressor`, `HistGradientBoostingRegressor` | No compara costo computacional ni tiempo de ajuste. |
| H04 | S03 | Notebook: `feature_importances_`, `permutation_importance`; `submission/feature_importances.csv` | No prueba causalidad; la impureza puede sobreestimar variables con muchos puntos de corte. |
| H05 | S03 | Notebook: `PartialDependenceDisplay`; `submission/partial_dependence.png` | No es un experimento. |
| H06 | S04 | `submission/decision_tree.pkl`, `random_forest.pkl`, `gradient_boosting.pkl`, `model_comparison.csv`, `feature_importances.csv`; `tests/test_activity.py` | Pruebas no inspeccionan contenido visual ni estabilidad entre ejecuciones. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso y partición | `data/auto_mpg.csv`; notebook | Debe coincidir con la de P200 para que el MSE sea comparable. |
| S02 | Modelos de árbol | Notebook; `decision_tree.pkl`, `random_forest.pkl`, `gradient_boosting.pkl` | `max_depth` y `n_estimators` fijados por una exploración mínima (la curva de validación sólo cubre profundidad). |
| S03 | Interpretación | `feature_importances.csv`; `partial_dependence.png` | No evalúa estabilidad entre semillas ni calibración. |
| S04 | Entrega y trazabilidad | `submission/`; `tests/test_activity.py`; `traceability.yaml` | Entrada P206 nueva; pruebas verifican artefactos y relaciones de MSE, no contenido visual. |

### Contrato de evidencia actual

- **Notebook o código:** repite la limpieza, partición y preprocesamiento de
  P200; ajusta un árbol, un Random Forest y un modelo de *gradient boosting*;
  diagnostica sobreajuste con una curva de validación; contrasta importancia
  por impureza y por permutación; interpreta con dependencia parcial.
- **`submission/`:** tres estimadores (`.pkl`), la comparación de MSE
  (`model_comparison.csv`), la tabla de importancias
  (`feature_importances.csv`) y dos gráficas (`validation_curve.png`,
  `partial_dependence.png`).
- **Pruebas:** verifican los siete artefactos, que la línea base ingenua
  siga siendo la peor, que Random Forest o *gradient boosting* superen a la
  regresión lineal, y que la tabla de importancias tenga ambos métodos con
  las variables esperadas.
- **Trazabilidad:** P206 mapea `predictiva.C01`–`C04` (entrada nueva).

### Dependencias en la secuencia

- **Recibe de P200:** caso Auto MPG, partición, contrato de preprocesamiento
  y línea base.
- **Habilita para P220:** profundidad y número de árboles como
  hiperparámetros a buscar sistemáticamente, en vez de ElasticNet como único
  ejemplo.
- **Habilita para P222–P224:** contrastar esta importancia por
  impureza/permutación con la selección explícita (P222–P223) y la
  contracción de coeficientes (P224).

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

P206 mapea `predictiva.C01`–`C04` en
`implementation/predictiva/traceability.yaml`. El producto de Analytics es
una comparación predictiva evaluada entre árboles/ensambles y las
especificaciones ya establecidas de P200, no un recorrido por algoritmos de
machine learning: árboles, bagging y boosting son disciplinas contribuyentes
al servicio de esa comparación, y la pregunta sigue siendo si aportan sobre
la línea base del caso, con el límite explícito de que la importancia y la
dependencia parcial no prueban causalidad.
