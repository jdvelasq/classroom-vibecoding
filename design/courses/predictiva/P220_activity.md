# P220 — Pipelines

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P220_pipelines/`.

### Preguntas analíticas actuales

- ¿Cómo se conserva el procesamiento de texto junto con un clasificador de frases?
- ¿Cómo se busca una configuración reproducible sin separar vectorización, transformación TF–IDF y modelo?

Empaqueta clasificación de frases en un `Pipeline` de `CountVectorizer`,
`TfidfTransformer` y regresión logística, con búsqueda de parámetros y
estimador persistido.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** clasifica frases; no hay usuario o decisión financiera evidenciados.
- **Producto terminal:** pipeline persistido que transporta vocabulario, TF–IDF y clasificador.
- **Uso y límite:** protege consistencia de transformación/predicción; no evalúa calibración ni operación.
- **Disciplinas contribuyentes:** ingeniería de pipeline y texto sirven al producto de clasificación.

### Highlights de contribución

- **H01 — Une representación y estimador:** `CountVectorizer`, TF–IDF y logística viajan en el mismo `Pipeline`.
- **H02 — Busca configuración sin filtrar texto de prueba:** `GridSearchCV` selecciona parámetros con exactitud balanceada.
- **H03 — Reutiliza un objeto completo:** persiste y recarga el pipeline para predecir desde texto crudo.

### Índice de comparación externa

| Ancla actual | Hitos | Mecanismo | Límite |
| --- | --- | --- | --- |
| Pipeline de texto | H01 | Vectorización/TF–IDF/logística | No explica vocabulario/resultados. |
| Selección | H02 | CV y exactitud balanceada | Sin calibración. |
| Reuso | H03 | `estimator.pkl` | Test sólo presencia. |

### Inventario técnico de implementación

- **Introduce:** `Pipeline` de transformación y estimador, persistencia con
  `pickle` y predicción desde el objeto recuperado.
- **Extiende:** clasificación textual de P203 mediante TF–IDF y
  `GridSearchCV` con `balanced_accuracy`.
- **Verifica y comunica:** contrasta precisión y exactitud balanceada de
  entrenamiento/prueba y evita guardar un estimador peor que el actual.

### Relación técnica con actividades anteriores

Reutiliza texto y clasificación de P202–P203, pero concentra el aprendizaje en
la reproducibilidad del flujo completo. Sin P220 se pierde la garantía de que
transformación y modelo viajan juntos al usarlo después.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite |
| --- | --- | --- | --- |
| H01 | S01 | `professor/notebook.ipynb` | Sin inspección persistida de vocabulario. |
| H02 | S02 | Notebook: `GridSearchCV` | No persiste resultados CV. |
| H03 | S03, S04 | `.pkl`; pruebas | Tests sólo existencia. |

### Superficies de cambio para revisión posterior

| ID | Componente | Rutas | Restricción |
| --- | --- | --- | --- |
| S01 | Texto/pipeline | Notebook; `.pkl` | Transformación y modelo deben viajar juntos. |
| S02 | CV/métrica | Notebook | Test fuera de búsqueda. |
| S03 | Entrega/pruebas | submission/tests | Sólo presencia. |
| S04 | Trazabilidad | YAML | Falta P220. |

### Contrato de evidencia actual

- **Código:** ajusta, busca y serializa pipeline.
- **`submission/`:** estimador.
- **Pruebas:** presencia de archivo.
- **Trazabilidad:** falta P220.

### Dependencias en la secuencia

- **Recibe de P202–P203:** texto, vectorización y clasificación.
- **Habilita para P221:** pipeline como contrato, sin código común demostrado.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe una entrada P220 en `implementation/predictiva/traceability.yaml`.
Debe revisarse antes de aprobar la actividad.
