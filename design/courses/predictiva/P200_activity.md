# P200 — Regresión básica

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P200_regresion_basica/`.

### Preguntas analíticas actuales

- ¿Cómo podemos predecir el consumo de combustible (MPG) de un automóvil a partir de sus características técnicas?

Usa `auto_mpg.csv`; elimina nulos, trata `Origin` como categoría y reserva una
muestra reproducible. Compara regresión lineal con especificaciones de mayor
flexibilidad y guarda modelos, preprocesadores y comparación de desempeño.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima MPG desde características técnicas para
  decidir si el equipo continúa con proyectos predictivos posteriores sobre datos
  similares (caso de viabilidad); no hay decisión operativa de flota evidenciada.
- **Producto terminal:** predictores comparados, preprocesadores y tabla MSE reutilizables.
- **Uso y límite:** compara especificaciones en una partición; no prueba causalidad ni procedencia del dataset.
- **Disciplinas contribuyentes:** regresión, MLP y preprocesamiento sirven al primer producto predictivo.

### Highlights de contribución

- **H01 — Formula el primer producto predictivo del curso:** transforma la pregunta
  sobre MPG en una predicción cuantitativa contrastable contra consumo observado;
  es la primera actividad P200–P226 y, por tanto, establece el contrato de
  entrenamiento, predicción y evaluación que las posteriores extienden.
- **H02 — Hace explícita la semántica del dato antes de modelar:** detecta y elimina
  nulos, e identifica `Origin` como categoría sin orden; deja visible que una
  etiqueta de país no debe tratarse como una escala numérica. Sin este hito, la
  primera predicción del curso naturalizaría una representación inválida.
- **H03 — Separa datos sin filtrar información del futuro:** construye una partición
  reproducible y ajusta `StandardScaler` y los codificadores sólo con vehículos
  de entrenamiento antes de transformar la muestra de prueba.
- **H04 — Construye una línea base interpretable:** usa sólo `Horsepower`, grafica la
  curva predicha contra los datos y calcula MSE; permite observar qué explica y
  qué no explica una relación simple.
- **H05 — Codifica categorías como un método de representación:** usa
  `OneHotEncoder` para convertir cada origen nominal en indicadores sin imponer
  una distancia u orden entre países; ajusta las categorías en entrenamiento y
  contempla valores no vistos al predecir. El aporte no es conocer una librería,
  sino saber cuándo y por qué una categoría debe convertirse de ese modo. Sin
  ello, el flujo multivariable no podría incorporar origen sin una codificación
  ordinal artificial.
- **H06 — Integra variables heterogéneas en un único contrato:** usa
  `ColumnTransformer` para aplicar conjuntamente escalamiento a entradas
  numéricas y codificación a origen, preservando el mismo tratamiento al ajustar
  y al predecir.
- **H07 — Muestra que una regresión puede ganar flexibilidad sin cambiar de familia:**
  incorpora `Horsepower_squared` y `Weight_x_Horsepower`, y compara la
  especificación lineal base con una que representa curvatura e interacción.
- **H08 — Muestra que la no linealidad puede importar aun con una sola variable:** la
  MLP que usa sólo `Horsepower` reduce el MSE de prueba frente a la regresión
  lineal de esa misma entrada (15.60 frente a 22.03 en el artefacto actual).
  Así separa el efecto de cambiar la representación funcional del efecto de
  añadir más variables.
- **H09 — Contrasta capacidad de representación, no sólo una métrica:** compara
  regresiones y MLP con una entrada y con todas las entradas; la red neuronal se
  introduce como alternativa cuyo valor debe verificarse sobre la muestra de
  prueba, no como sustituto automático del modelo lineal.
- **H10 — Deja un modelo reutilizable, no sólo una salida de notebook:** persiste
  preprocesadores, modelo flexible, MLP y tabla de MSE, y recarga el MLP con el
  mismo preprocesador para predecir nuevamente. Sin este hito, las actividades
  posteriores de pipeline, despliegue y evaluación no tendrían una base concreta
  de contrato modelo–transformación–entrada.
- **H11 — Encuadra el producto como un caso de viabilidad y fija un umbral de
  fracaso:** antes de modelar, plantea la decisión que justifica el taller
  (continuar o no con proyectos predictivos posteriores sobre datos similares)
  y fija el error que haría inútil el producto: ningún modelo es evidencia de
  valor si no mejora la predicción ingenua del MPG promedio de entrenamiento
  (`naive_mean_baseline`, MSE de prueba 62.19). Persiste esa fila en
  `model_comparison.csv` y verifica que el mejor modelo la supere. Sin este
  hito, H04–H09 se leerían como una comparación de MSE sin una referencia que
  diga si alguno aporta algo.
- **H12 — Diagnostica con residuos antes de flexibilizar y transforma la
  respuesta cuando la varianza no es constante:** grafica los residuos de
  `horsepower_model` contra el valor predicho y contra `Horsepower`
  (`residual_diagnostics.png`), y ajusta una alternativa con log-transformación
  de la respuesta (`TransformedTargetRegressor` con `log1p`/`expm1`), que
  reduce el MSE de prueba de 22.03 a 19.00 frente a la misma entrada (69.4 %
  de la brecha con la línea base ingenua). Motiva con evidencia por qué H07
  añade términos no lineales, en vez de presentarlos sin justificación.

### Inventario técnico de implementación

- **Introduce:** partición train/test, escalamiento, codificación categórica y regresión lineal.
- **Introduce:** MSE, visualización de predicción y comparación de modelos.
- **Introduce:** encuadre de viabilidad con línea base ingenua y diagnóstico de
  residuos con transformación de la respuesta.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo/dato/producto observable | Límite |
| --- | --- | --- | --- |
| Representación segura | H02–H06 | Nulos, `Origin`, split, OHE y ColumnTransformer | Sin procedencia de Auto MPG. |
| Flexibilidad comparada | H04, H07–H09 | Línea base, términos y MLP | MSE específico del caso. |
| Reuso | H10 | Modelos/preprocesadores persistidos | Tests sólo archivos. |
| Viabilidad y diagnóstico | H11–H12 | Línea base ingenua, residuos y log-transformación | `model_comparison.csv`; `residual_diagnostics.png`; umbral específico del caso. |

### Relación técnica con actividades anteriores

Primera actividad predictiva; establece la separación entre preparación,
ajuste y evaluación. No hay actividad Pxxx anterior de Predictiva con la cual
pueda duplicarse; los highlights identifican las capacidades que los talleres
posteriores reutilizan o especializan.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Producto predictivo inicial | S04 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`; `implementation/predictiva/traceability.yaml` | La posición inicial proviene de la numeración P200; no demuestra por sí misma dominio estudiantil. |
| H02 — Semántica de nulos y `Origin` | S01, S02 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: carga, `dropna()` y conversión de `Origin` a `category` | No explica la procedencia externa ni el sesgo del conjunto `auto_mpg.csv`. |
| H03 — Partición y ausencia de filtración | S02 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `train_test_split`, ajuste de escaladores/preprocesadores en entrenamiento | La prueba sólo verifica artefactos persistentes, no reejecuta la partición. |
| H04 — Línea base con `Horsepower` | S03 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `horsepower_model`, gráfica y MSE | Es una línea base del caso, no evidencia de causalidad del consumo. |
| H05 — Codificación nominal con `OneHotEncoder` | S02 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `OneHotEncoder(handle_unknown="ignore")` | No prueba desempeño en una categoría realmente no vista. |
| H06 — Contrato heterogéneo con `ColumnTransformer` | S02 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `ColumnTransformer` con bloques numérico y `Origin` | El contrato sólo se evalúa para este esquema de entradas. |
| H07 — Flexibilidad lineal con términos derivados | S03 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `Horsepower_squared`, `Weight_x_Horsepower` y `linear_flexible_model` | Los términos fueron definidos para este caso; no son una receta universal. |
| H08 — MLP de una variable frente a línea base | S03 | `implementation/predictiva/P200_regresion_basica/submission/model_comparison.csv`; `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb` | La ventaja 15.60 frente a 22.03 es específica de esta partición y métrica MSE. |
| H09 — Comparación de capacidad con todas las entradas | S03 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `mlp`, `linear_model`, `linear_flexible_model` y comparación de MSE | No establece que una MLP sea preferible fuera del caso ni evalúa costos de operación. |
| H10 — Persistencia y reutilización | S04 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `pickle.dump`, recarga y predicción; `implementation/predictiva/P200_regresion_basica/submission/`; `implementation/predictiva/P200_regresion_basica/tests/test_activity.py` | Las pruebas verifican existencia de archivos, no la compatibilidad semántica completa entre artefactos. |
| H11 — Encuadre de viabilidad y línea base ingenua | S03, S04 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: celda de encuadre, `naive_mean_model`, verificación `best_regressor_mse <= naive_mse`; `submission/model_comparison.csv`; `tests/test_activity.py` | El umbral de viabilidad (MSE ingenuo) es específico de esta partición y este caso educativo. |
| H12 — Residuos y log-transformación | S03 | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: gráfica de residuos, `log_horsepower_model` (`TransformedTargetRegressor`); `submission/residual_diagnostics.png`; `tests/test_activity.py` | El diagnóstico se hizo sólo sobre `horsepower_model`; no se repitió sobre `linear_model` ni `linear_flexible_model`. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso y dataset Auto MPG | `data/auto_mpg.csv`; notebook | No hay procedencia documentada en la actividad. |
| S02 | Representación y preprocesamiento | Notebook; `features_preprocessor.pkl` | `Origin` debe conservarse como nominal y el ajuste debe ocurrir sólo en entrenamiento. |
| S03 | Familias y especificaciones de modelo | Notebook; modelos `.pkl`; `model_comparison.csv`; `residual_diagnostics.png` | Deben mantenerse comparables sobre la misma partición y MSE; el diagnóstico de residuos no se repitió para todas las especificaciones. |
| S04 | Producto y verificación | `submission/`; `tests/test_activity.py`; `traceability.yaml` | Las pruebas ahora validan la línea base ingenua y la fila de `log_horsepower_model`, además de la existencia de artefactos. |

### Contrato de evidencia actual

- **Notebook o código:** encuadra el caso de viabilidad, limpia, separa,
  preprocesa, ajusta una línea base ingenua, diagnostica residuos, ajusta
  regresiones (incluida una con log-transformación) y MLP, compara MSE y
  recarga artefactos.
- **`submission/`:** conserva preprocesadores, modelos, comparación de MSE
  (con la línea base ingenua y el modelo log-transformado) y el gráfico de
  diagnóstico de residuos.
- **Pruebas:** exigen los cinco archivos originales, que la línea base
  ingenua tenga el MSE más alto, y que `log_horsepower_model` y
  `residual_diagnostics.png` existan con un MSE finito y positivo.
- **Trazabilidad:** P200 mapea `predictiva.C01`–`C04`; H11–H12 fortalecen la
  evidencia de C01–C04 sin requerir una capacidad nueva.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna; es la primera actividad P200–P226.
- **Habilita para P201, P203, P204, P220, P222 y P224:** patrón de partición,
  preprocesamiento, comparación y persistencia de estimadores.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook de profesor, datos, modelos de `submission/`, pruebas y
`traceability.yaml` sustentan `predictiva.C01`–`C04`. El producto es una
estimación de MPG; sklearn sirve al producto de Analytics.
