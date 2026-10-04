# P203 — Clasificación básica de texto

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P203_clasificacion_basica_texto/`.

### Preguntas analíticas actuales

- ¿Cómo anticipamos si una frase de noticia financiera comunica una señal positiva, negativa o neutral?
- ¿Cómo evaluamos ese clasificador cuando las tres clases no deben resumirse en una sola exactitud?

Convierte frases financieras etiquetadas en una representación documento–término
y entrega clasificador, vectorizador y métricas de prueba. El producto es una
estimación de sentimiento; no contiene una decisión financiera automatizada ni
evidencia de que el sentimiento cause un resultado de mercado.

### Highlights de contribución

- **Conecta una representación textual con una predicción supervisada:** ajusta
  `CountVectorizer` únicamente en frases de entrenamiento y transforma la
  muestra reservada con el mismo vocabulario. Extiende la matriz trazable de
  P202 hacia un flujo supervisado; sin este hito, la clasificación no conservaría
  el contrato entre texto, vocabulario aprendido y entradas de prueba.
- **Clasifica tres significados, no sólo dos alternativas:** usa regresión
  logística para distinguir señal positiva, negativa y neutral. Extiende P201
  desde imágenes de dígitos a texto financiero y P202 desde preparación a
  predicción; sin este hito, faltaría un caso donde las características se
  extraen desde lenguaje para responder una pregunta de clasificación.
- **Reserva frases de cada clase para juzgar el modelo:** usa división
  estratificada y mantiene el texto de entrenamiento separado del reservado.
  Reutiliza la protección multiclase de P201; sin ello, vocabulario y desempeño
  podrían depender de una partición que no representa las tres señales.
- **Evita que la exactitud oculte una clase difícil:** compara exactitud,
  exactitud balanceada y F1 macro, y visualiza una matriz de confusión. Las
  frases neutrales (1,391) superan ampliamente a positivas (570) y negativas
  (303); las métricas persistidas (0.840, 0.734 y 0.766, respectivamente)
  muestran que evaluar las tres clases requiere más que una proporción global de
  aciertos. Sin este hito, el desbalance propio de las señales financieras
  quedaría oculto detrás de la clase neutral predominante.
- **Vuelve inspeccionable una predicción textual guardada:** recarga el
  clasificador y el vectorizador, y relaciona frase, etiqueta, probabilidad
  máxima y probabilidades por clase. Sin este hito, el modelo persistido no
  permitiría revisar el fundamento de una predicción concreta.

### Inventario técnico de implementación

- **Reutiliza:** separación estratificada y clasificación multiclase de P201.
- **Extiende:** representación de P202 con `CountVectorizer` aprendido en
  entrenamiento y aplicado en prueba.
- **Introduce:** exactitud balanceada, F1 macro y revisión de una matriz de
  confusión para clases de sentimiento.
- **Reutiliza:** persistencia de modelo y añade persistencia separada del
  vectorizador que define sus entradas.

### Relación técnica con actividades anteriores

P203 sólo existe gracias a P202, pero no lo duplica: P202 explica cómo se
construye una representación textual; P203 prueba que esa representación puede
alimentar una clasificación de señales. P201 aporta clasificación multiclase y
probabilidades, pero P203 introduce el riesgo de que el vocabulario se ajuste
indebidamente con texto reservado.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| Vectorizador aprendido sólo en entrenamiento | `implementation/predictiva/P203_clasificacion_basica_texto/professor/notebook.ipynb`: separación, `CountVectorizer`, `fit_transform` y `transform` | La actividad no compara este vectorizador con la preparación específica de P202. |
| Clasificación de señales textuales | `implementation/predictiva/P203_clasificacion_basica_texto/professor/notebook.ipynb`: `LogisticRegression` y etiquetas de sentimiento | Una etiqueta de frase no demuestra impacto financiero ni recomendación de inversión. |
| Partición estratificada de tres clases | `implementation/predictiva/P203_clasificacion_basica_texto/professor/notebook.ipynb`: `train_test_split(..., stratify=dataframe.target)` | Las pruebas sólo verifican archivos persistidos. |
| Métricas sensibles a clase | `implementation/predictiva/P203_clasificacion_basica_texto/professor/notebook.ipynb`: `balanced_accuracy_score`, `f1_score` y matriz; `implementation/predictiva/P203_clasificacion_basica_texto/submission/metrics.json` | No persiste la matriz ni métricas desagregadas por clase. |
| Revisión de predicción textual persistida | `implementation/predictiva/P203_clasificacion_basica_texto/professor/notebook.ipynb`: recarga, `predict_proba` y tabla `results`; `implementation/predictiva/P203_clasificacion_basica_texto/submission/clf.pkl`; `vectorizer.pkl` | La probabilidad máxima no se somete a una prueba de calibración. |

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

P203 está mapeada a `predictiva.C01`, `predictiva.C02` y `predictiva.C04` en
`implementation/predictiva/traceability.yaml`. El producto de Analytics es la
estimación de señal textual y su evidencia; vectorización y regresión logística
contribuyen a él sin convertir la actividad en un curso de NLP o ML.
