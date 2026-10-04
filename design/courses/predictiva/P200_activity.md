# P200 — Regresión básica

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P200_regresion_basica/`.

### Preguntas analíticas actuales

- ¿Cómo podemos predecir el consumo de combustible (MPG) de un automóvil a partir de sus características técnicas?

Usa `auto_mpg.csv`; elimina nulos, trata `Origin` como categoría y reserva una
muestra reproducible. Compara regresión lineal con especificaciones de mayor
flexibilidad y guarda modelos, preprocesadores y comparación de desempeño.

### Highlights de contribución

- **H01 — Formula el primer producto predictivo del curso:** transforma la pregunta
  sobre MPG en una predicción cuantitativa contrastable contra consumo observado;
  es la primera actividad P200–P225 y, por tanto, establece el contrato de
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

### Inventario técnico de implementación

- **Introduce:** partición train/test, escalamiento, codificación categórica y regresión lineal.
- **Introduce:** MSE, visualización de predicción y comparación de modelos.

### Relación técnica con actividades anteriores

Primera actividad predictiva; establece la separación entre preparación,
ajuste y evaluación. No hay actividad Pxxx anterior de Predictiva con la cual
pueda duplicarse; los highlights identifican las capacidades que los talleres
posteriores reutilizan o especializan.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| H01 — Producto predictivo inicial | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`; `implementation/predictiva/traceability.yaml` | La posición inicial proviene de la numeración P200; no demuestra por sí misma dominio estudiantil. |
| H02 — Semántica de nulos y `Origin` | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: carga, `dropna()` y conversión de `Origin` a `category` | No explica la procedencia externa ni el sesgo del conjunto `auto_mpg.csv`. |
| H03 — Partición y ausencia de filtración | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `train_test_split`, ajuste de escaladores/preprocesadores en entrenamiento | La prueba sólo verifica artefactos persistentes, no reejecuta la partición. |
| H04 — Línea base con `Horsepower` | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `horsepower_model`, gráfica y MSE | Es una línea base del caso, no evidencia de causalidad del consumo. |
| H05 — Codificación nominal con `OneHotEncoder` | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `OneHotEncoder(handle_unknown="ignore")` | No prueba desempeño en una categoría realmente no vista. |
| H06 — Contrato heterogéneo con `ColumnTransformer` | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `ColumnTransformer` con bloques numérico y `Origin` | El contrato sólo se evalúa para este esquema de entradas. |
| H07 — Flexibilidad lineal con términos derivados | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `Horsepower_squared`, `Weight_x_Horsepower` y `linear_flexible_model` | Los términos fueron definidos para este caso; no son una receta universal. |
| H08 — MLP de una variable frente a línea base | `implementation/predictiva/P200_regresion_basica/submission/model_comparison.csv`; `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb` | La ventaja 15.60 frente a 22.03 es específica de esta partición y métrica MSE. |
| H09 — Comparación de capacidad con todas las entradas | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `mlp`, `linear_model`, `linear_flexible_model` y comparación de MSE | No establece que una MLP sea preferible fuera del caso ni evalúa costos de operación. |
| H10 — Persistencia y reutilización | `implementation/predictiva/P200_regresion_basica/professor/notebook.ipynb`: `pickle.dump`, recarga y predicción; `implementation/predictiva/P200_regresion_basica/submission/`; `implementation/predictiva/P200_regresion_basica/tests/test_activity.py` | Las pruebas verifican existencia de archivos, no la compatibilidad semántica completa entre artefactos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso y dataset Auto MPG | `data/auto_mpg.csv`; notebook | No hay procedencia documentada en la actividad. |
| S02 | Representación y preprocesamiento | Notebook; `features_preprocessor.pkl` | `Origin` debe conservarse como nominal y el ajuste debe ocurrir sólo en entrenamiento. |
| S03 | Familias y especificaciones de modelo | Notebook; modelos `.pkl`; `model_comparison.csv` | Deben mantenerse comparables sobre la misma partición y MSE. |
| S04 | Producto y verificación | `submission/`; `tests/test_activity.py`; `traceability.yaml` | Las pruebas actuales sólo verifican existencia de artefactos. |

### Contrato de evidencia actual

- **Notebook o código:** limpia, separa, preprocesa, ajusta regresiones y MLP,
  compara MSE y recarga artefactos.
- **`submission/`:** conserva preprocesadores, modelos y comparación de MSE.
- **Pruebas:** exigen los cinco archivos, sin validar partición, métricas ni
  compatibilidad modelo–preprocesador.
- **Trazabilidad:** P200 mapea `predictiva.C01`–`C04`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna; es la primera actividad P200–P225.
- **Habilita para P201, P203, P204, P219, P221 y P223:** patrón de partición,
  preprocesamiento, comparación y persistencia de estimadores.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Notebook de profesor, datos, modelos de `submission/`, pruebas y
`traceability.yaml` sustentan `predictiva.C01`–`C04`. El producto es una
estimación de MPG; sklearn sirve al producto de Analytics.
