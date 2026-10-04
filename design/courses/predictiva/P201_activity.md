# P201 — Clasificación básica de imágenes

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P201_clasificacion_basica_imagenes/`.

### Preguntas analíticas actuales

- ¿Cómo podemos clasificar imágenes de dígitos escritos a mano?
- ¿Cómo se revisa la incertidumbre de cada predicción?

Usa el conjunto educativo `sklearn.datasets.load_digits`: imágenes 8×8 de
dígitos, sin caso organizacional, usuario ni procedencia externa documentados.
El producto es un clasificador multiclase persistido, junto con su exactitud de
prueba y evidencia visual de clases, errores y probabilidades.

### Highlights de contribución

- **H01 — Convierte una imagen en una entrada de modelo sin borrar su significado:**
  visualiza las matrices 8×8 y luego las aplana a un vector de 64 intensidades,
  dejando explícita la correspondencia entre una imagen para personas y una fila
  de *features* para el clasificador. Frente a P200 introduce entradas de alta
  dimensionalidad; sin este hito, la clasificación de imágenes aparecería como
  una etiqueta mágica sin representación verificable.
- **H02 — Conserva las diez clases al evaluar:** usa `train_test_split` estratificado
  para reservar imágenes de cada dígito. Extiende la partición reproducible de
  P200 hacia un problema multiclase; sin estratificación, la exactitud de prueba
  podría omitir o desbalancear clases de forma no visible.
- **H03 — Pasa de estimar una cantidad a asignar alternativas discretas:** ajusta
  `LogisticRegression` multiclase y produce tanto etiqueta como vector de diez
  probabilidades mediante `predict_proba`. Es la primera transición explícita
  del curso a clasificación; sin ella no se distinguiría una predicción de clase
  de una estimación continua de MPG.
- **H04 — Distingue desempeño global de comportamiento por clase:** compara exactitud
  de entrenamiento y prueba, y construye una matriz de confusión. La exactitud
  persistida de prueba es 0.9577 sobre 899 imágenes, pero la matriz permite ver
  qué dígitos se confunden; sin este hito, una métrica única ocultaría el patrón
  de error.
- **H05 — Inspecciona evidencia por observación:** vincula la imagen real, la etiqueta
  predicha, la distribución de probabilidades y el color de acierto/error. Esto
  extiende la gráfica de predicción de P200 hacia revisión de incertidumbre por
  caso; sin ello, `predict_proba` se reduciría a una salida numérica sin juicio
  visual.
- **H06 — Preserva el clasificador probabilístico para uso posterior:** serializa y
  recarga el estimador, comprobando que conserva sus clases y puede volver a
  generar predicciones y probabilidades. Frente a P200 persiste ahora el
  contrato completo de clasificación; sin este hito no habría evidencia de que
  la incertidumbre calculada pertenece al modelo guardado.

### Inventario técnico de implementación

- **Introduce:** representación imagen–vector, clasificación multiclase y
  `LogisticRegression` sobre 64 intensidades de píxel.
- **Extiende:** partición reproducible de P200 mediante `stratify=digits.target`.
- **Introduce:** `predict_proba`, exactitud, `ConfusionMatrixDisplay` y revisión
  visual de las probabilidades por observación.
- **Reutiliza:** persistencia con `pickle` y verificación posterior de artefactos.

### Relación técnica con actividades anteriores

P201 reutiliza el ciclo de ajustar, reservar, predecir y persistir de P200,
pero cambia variable objetivo continua por diez clases y añade probabilidades,
matriz de confusión e inspección visual de errores. No es una duplicación de
P200: si se elimina, falta la transición explícita a clasificación y la
distinción entre métrica global e incertidumbre por imagen.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| H01 — Imagen como vector de 64 entradas | `implementation/predictiva/P201_clasificacion_basica_imagenes/professor/notebook.ipynb`: `digits.images`, `reshape((n_samples, -1))` y visualizaciones | El conjunto es educativo; no demuestra desempeño con imágenes operativas. |
| H02 — Partición multiclase estratificada | `implementation/predictiva/P201_clasificacion_basica_imagenes/professor/notebook.ipynb`: `train_test_split(..., stratify=digits.target)` | La prueba no reejecuta ni valida la composición de la partición. |
| H03 — Etiquetas y probabilidades multiclase | `implementation/predictiva/P201_clasificacion_basica_imagenes/professor/notebook.ipynb`: `LogisticRegression`, `predict` y `predict_proba` | Las probabilidades son puntajes del modelo; no se evalúa su calibración. |
| H04 — Exactitud y matriz de confusión | `implementation/predictiva/P201_clasificacion_basica_imagenes/professor/notebook.ipynb`: `accuracy_score` y `ConfusionMatrixDisplay`; `implementation/predictiva/P201_clasificacion_basica_imagenes/submission/metrics.json` | El archivo persistido conserva exactitud, pero no matriz de confusión ni métricas por clase. |
| H05 — Revisión visual por observación | `implementation/predictiva/P201_clasificacion_basica_imagenes/professor/notebook.ipynb`: `plot_image`, `plot_value_array` y cuadrícula de ejemplos | La selección de ejemplos es inicial y no constituye una auditoría sistemática de todos los errores. |
| H06 — Persistencia probabilística | `implementation/predictiva/P201_clasificacion_basica_imagenes/professor/notebook.ipynb`: `pickle.dump`, recarga y nuevo `predict_proba`; `implementation/predictiva/P201_clasificacion_basica_imagenes/submission/estimator.pkl`; `implementation/predictiva/P201_clasificacion_basica_imagenes/tests/test_activity.py` | Las pruebas verifican existencia de archivos, no que la recarga reproduzca exactamente cada probabilidad. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y representación de imágenes | Notebook; `sklearn.datasets.load_digits` | Las 64 intensidades corresponden a imágenes 8×8 educativas. |
| S02 | Modelo y salida probabilística | Notebook; `estimator.pkl` | `predict_proba` no está calibrado. |
| S03 | Evaluación y evidencia visual | Notebook; `metrics.json`; pruebas | Sólo persiste exactitud; no matriz de confusión ni revisión por imagen. |

### Contrato de evidencia actual

- **Notebook o código:** aplana imágenes, estratifica, ajusta logística,
  calcula probabilidades, muestra errores y recarga el estimador.
- **`submission/`:** conserva estimador y exactitud de prueba.
- **Pruebas:** verifican ambos archivos, sin comprobar valor de métricas ni
  comportamiento multiclase.
- **Trazabilidad:** P201 mapea `predictiva.C01`–`C04`.

### Dependencias en la secuencia

- **Recibe de P200:** partición reproducible, evaluación y persistencia.
- **Habilita para P203 y P204:** clasificación multiclase/binaria,
  `predict_proba`, matriz de confusión y lectura de errores por caso.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

La entrada P201 de `implementation/predictiva/traceability.yaml` mapea
`predictiva.C01`–`C04`. El producto es un clasificador y evidencia de sus
predicciones; regresión logística, visualización y persistencia sirven a ese
producto de Analytics. La actividad no evidencia una decisión organizacional,
un usuario externo ni calibración probabilística, por lo que no deben inferirse.
