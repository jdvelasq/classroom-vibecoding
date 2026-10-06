# P223 — Selección de entradas para clasificación

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P222_selection_inputs_clasificacion/`.

### Preguntas analíticas actuales

- ¿Qué subconjunto de variables permite clasificar el indicador `target` del
  conjunto de enfermedad cardíaca con evidencia separada de entrenamiento?
- ¿Cómo se busca a la vez el número de entradas y la regularización de una
  regresión logística sin separar transformaciones, selección y clasificador?

El caso usa `heart_disease.csv`, con variables clínicas numéricas y categóricas
y el campo binario `target`. Produce un `GridSearchCV` persistido. El archivo
no documenta la procedencia, población ni uso clínico del conjunto; el modelo
es un ejercicio educativo, no un diagnóstico ni una decisión de atención.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** estima `target` para el caso didáctico; no
  hay usuario clínico ni decisión de atención evidenciados.
- **Producto terminal:** estimador de clasificación con transformaciones,
  selección de entradas y parámetros buscados conjuntamente.
- **Uso y límite:** permite comparar exactitud y exactitud balanceada de un
  clasificador; no prueba utilidad clínica, calibración, causalidad ni equidad.
- **Disciplinas contribuyentes:** regresión logística, selección estadística,
  validación cruzada y codificación sirven a una predicción educativa de
  Analytics; no constituyen un curso de diagnóstico médico o de ML clínico.

### Highlights de contribución

- **H01 — Representa la categoría clínica sin imponerle orden:** codifica
  `thal` con `OneHotEncoder` dentro de `ColumnTransformer`, preservando el
  contrato de transformar igual durante ajuste y predicción. Extiende P200 y
  P222 hacia clasificación; sin este hito, el campo textual impediría el flujo
  reproducible de selección.
- **H02 — Selecciona entradas dentro del flujo evaluado:** inserta
  `SelectKBest(f_classif)` entre la transformación y el estimador. Así el
  número de variables no se decide en una tabla externa al modelo; sin este
  hito, la selección filtraría información o quedaría desconectada del
  clasificador que la usa.
- **H03 — Busca conjuntamente complejidad y regularización:** explora `k`,
  penalidad L1/L2 y `C` de `LogisticRegression(solver="saga")` mediante
  `GridSearchCV` con cinco particiones. Sin este contraste, seleccionar
  entradas parecería independiente del control de complejidad del modelo.
- **H04 — Distingue exactitud de cobertura equilibrada de clases:** reporta
  `accuracy_score` y `balanced_accuracy_score` para entrenamiento y prueba;
  reutiliza el criterio de P203 frente a una clase binaria. Sin este hito, la
  proporción global de aciertos sería la única lectura del clasificador.
- **H05 — Conserva el flujo seleccionado como un solo artefacto:** persiste y
  recupera el objeto buscado, que incluye codificación, selección y regresión.
  Sin este hito, no quedaría un contrato reutilizable entre datos de entrada y
  modelo elegido.
- **H06 — Limita el uso de un caso clínico educativo:** el CSV contiene señales
  como edad, presión, colesterol, dolor de pecho y resultado `target`, pero no
  documenta procedencia ni contexto asistencial. Por ello la actividad no puede
  traducirse en diagnóstico, triage o política clínica.

### Inventario técnico de implementación

- **Extiende:** `ColumnTransformer`, `OneHotEncoder`, partición reproducible y
  regresión logística hacia un caso binario.
- **Introduce:** `SelectKBest(f_classif)` y búsqueda conjunta de `k`, L1/L2 y
  `C` con `GridSearchCV(scoring="balanced_accuracy")`.
- **Verifica y comunica:** imprime exactitud y exactitud balanceada; persiste
  el estimador elegido, aunque las pruebas sólo comprueban su existencia.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Selección integrada | H01–H03 | Codificación de `thal`, `SelectKBest`, penalidad y `C` dentro de un pipeline buscado por CV | Notebook; no persiste selección ni resultados de CV. |
| Evaluación binaria | H04 | Exactitud y exactitud balanceada en partición 90/10 | Notebook; no hay calibración, matriz de confusión ni métricas persistidas. |
| Artefacto reutilizable | H05 | `estimator.pkl` contiene el flujo completo | Prueba verifica sólo presencia. |
| Límite del caso clínico | H06 | Variables clínicas y `target` binario | CSV; sin procedencia ni autorización para uso clínico. |

### Relación técnica con actividades anteriores

P223 traslada la selección integrada de P222 desde regresión a clasificación y
reutiliza la codificación/pipeline de P200 y P221. No duplica P204: P204
contrasta especificaciones binarias; P223 concentra la selección de entradas y
regularización en el mismo estimador. La relación con un uso clínico real no se
evidencia y no debe inferirse.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | `professor/notebook.ipynb`: `ColumnTransformer` y `OneHotEncoder` para `thal` | Sólo `thal` se trata explícitamente como categoría. |
| H02 | S02 | `professor/notebook.ipynb`: `SelectKBest(f_classif)` dentro de `Pipeline` | No persiste la lista de entradas elegidas. |
| H03 | S02 | `professor/notebook.ipynb`: grilla de `k`, `penalty`, `C` y CV=5 | No se conserva el resultado de cada combinación. |
| H04 | S03 | `professor/notebook.ipynb`: `accuracy_score`, `balanced_accuracy_score` | No hay matriz de confusión, calibración ni métricas en `submission/`. |
| H05 | S04 | Notebook: `pickle.dump/load`; `submission/estimator.pkl`; `tests/test_activity.py` | La prueba sólo exige el archivo. |
| H06 | S01, S05 | `data/heart_disease.csv`; codebook del notebook | Procedencia, población y uso permitido no están documentados. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso clínico y representación | `data/heart_disease.csv`; notebook | No autoriza diagnóstico ni decisión clínica. |
| S02 | Selección, regularización y CV | Notebook; `estimator.pkl` | Transformación, selección y estimador deben conservarse unidos. |
| S03 | Evaluación | Notebook | Sólo expone exactitud y exactitud balanceada. |
| S04 | Artefacto y prueba | `submission/estimator.pkl`; `tests/test_activity.py` | La prueba no valida comportamiento ni selección. |
| S05 | Trazabilidad | `implementation/predictiva/traceability.yaml` | No existe entrada P223. |

### Contrato de evidencia actual

- **Notebook o código:** separa, codifica, selecciona, busca parámetros, mide y
  serializa un clasificador.
- **`submission/`:** conserva únicamente `estimator.pkl`.
- **Pruebas:** comprueban la existencia del archivo, no sus métricas ni su
  comportamiento.
- **Trazabilidad:** falta entrada P223 y requiere escalación.

### Dependencias en la secuencia

- **Recibe de P200, P204, P221 y P222:** partición, codificación, clasificación,
  pipeline, búsqueda y selección integrada.
- **Habilita para P224:** contrasta selección de entradas con regularización de
  coeficientes; no hay dependencia de código demostrable.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P223 en `implementation/predictiva/traceability.yaml`.
El producto es un clasificador educativo persistido; los métodos estadísticos y
de ML contribuyen a ese producto sin autorizar un uso clínico.
