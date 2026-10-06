# P225 — Reducción de dimensionalidad

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P224_reduccion_dimensionalidad/`.

### Preguntas analíticas actuales

- ¿Cómo cambian las proyecciones bidimensionales de imágenes de dígitos cuando
  se usan PCA, t-SNE y UMAP?

Parte de `sklearn.datasets.load_digits`, proyecta las 64 intensidades de cada
dígito y guarda tres gráficos. No entrena ni evalúa un predictor, ni declara
usuario, decisión o producto predictivo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** ¿cuántas componentes de una reducción de
  dimensionalidad conservan suficiente información para clasificar el dígito?
  No hay usuario ni decisión organizacional evidenciados; es un caso educativo.
- **Producto terminal:** tres proyecciones visuales (PCA, t-SNE, UMAP) y una
  curva de exactitud de prueba frente al número de componentes para PCA y
  UMAP, con la varianza explicada acumulada de PCA.
- **Uso y límite:** la curva evalúa, sobre una partición fija de este dataset
  educativo, cuánta información retiene cada representación para clasificar;
  no mide calibración, tiempo de cómputo ni estabilidad entre ejecuciones, y no
  generaliza a otro conjunto de imágenes. t-SNE no admite transformación a
  datos nuevos, por lo que no se evalúa fuera de muestra.
- **Disciplinas contribuyentes:** reducción de dimensionalidad (lineal y no
  lineal) sirve ahora a una estimación evaluada por exactitud retenida, no
  sólo a exploración visual. La auditoría de identidad de la línea Predictiva
  queda resuelta: PCA y UMAP son técnicas contribuyentes al servicio de un
  producto predictivo.

### Highlights de contribución

- **H01 — Contrasta tres formas de comprimir una imagen:** proyecta las 64
  intensidades de `load_digits` a dos dimensiones con PCA, t-SNE y UMAP. Sin
  este hito, las diferencias entre representación lineal y no lineal no quedan
  visibles sobre la misma entrada.
- **H02 — Conserva una evidencia visual por método:** guarda `digits_pca.png`,
  `digits_tsne.png` y `digits_umap.png`, de modo que la comparación sobrevive
  al notebook. Sin ello, la actividad no tendría artefactos revisables.
- **H03 — Usa una entrada cuya forma importa:** cada observación representa una
  imagen educativa de dígito con 64 intensidades, no un vector sin contexto; la
  proyección permite observar proximidades entre clases, pero no prueba que las
  etiquetas se preserven ni que una imagen sea clasificable.
- **H04 — Evalúa cuánta información retienen PCA y UMAP para clasificar, no
  sólo para verse bien en un gráfico:** entrena un clasificador logístico
  sobre k componentes de PCA (con escalamiento previo) y, por separado, sobre
  k componentes de UMAP ajustado sólo con entrenamiento y transformado a
  prueba, para k en [2, 5, 10, 20, 30, 40, 64], sobre la misma partición y
  tipo de clasificador que P201. El PCA de dos componentes que ilustra H01
  captura sólo 22.0 % de la varianza y clasifica apenas el 54.4 % de los
  casos; UMAP con las mismas dos componentes alcanza 89.0 %, y ambos se
  acercan a su techo (96.3 % y 95.1 %-95.7 %, respectivamente) a partir de
  k≈20-30. t-SNE no tiene una transformación aplicable a datos nuevos, por lo
  que no se evalúa fuera de muestra. Sin este hito, P225 seguiría siendo
  indistinguible de una demostración de reducción de dimensionalidad sin
  producto predictivo.

### Inventario técnico de implementación

- **Introduce:** PCA, t-SNE y UMAP bidimensionales sobre `load_digits`.
- **Verifica y comunica:** genera y persiste una visualización por método.
- **Introduce:** evaluación predictiva retenida (exactitud de prueba y
  varianza explicada) de PCA y UMAP en función del número de componentes,
  sobre la misma partición y tipo de clasificador que P201.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Proyección comparativa | H01 | PCA, t-SNE y UMAP a dos dimensiones | Notebook; parámetros y comparabilidad metodológica limitados. |
| Evidencia visual persistida | H02 | Tres PNG en `submission/` | Pruebas sólo verifican su presencia. |
| Imagen como dato | H03 | Dígitos 8×8 de `load_digits` | Evaluada por H04 para clasificación; no prueba que las etiquetas se preserven en la proyección visual. |
| Representación evaluada | H04 | Exactitud de prueba y varianza explicada de PCA y UMAP frente a k | `submission/pca_components_accuracy.csv`, `umap_components_accuracy.csv`; t-SNE no se evalúa (sin transformación a datos nuevos). |

### Relación técnica con actividades anteriores

P225 reutiliza el dataset de imágenes y el tipo de clasificador de P201, y
ahora también su misma partición (test_size=0.5, random_state=0,
estratificada). Extiende la exploración visual de representaciones con una
pregunta propia: cuántas componentes de una reducción de dimensionalidad
bastan para clasificar, no sólo para visualizarse. Su dependencia de P201
pasa de conceptual a demostrable.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | `professor/notebook.ipynb`: PCA, `TSNE`, `umap.UMAP` | No compara parámetros, tiempos ni fidelidad de cada proyección. |
| H02 | S03 | Notebook: `savefig`; tres PNG en `submission/`; pruebas | Los tests no inspeccionan contenido visual. |
| H03 | S01 | Notebook: `sklearn.datasets.load_digits` | Conjunto educativo sin caso organizacional. |
| H04 | S02, S03, S04 | Notebook: `Pipeline(StandardScaler, PCA, LogisticRegression)`, `umap.UMAP(...).transform`; `submission/pca_components_accuracy.csv`, `umap_components_accuracy.csv`, `components_accuracy_comparison.png`; pruebas | Resultado específico de este dataset y partición; no mide tiempo de cómputo, estabilidad entre ejecuciones ni calibración; t-SNE queda fuera por no admitir transformación a datos nuevos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y proyección | Notebook; `load_digits` | Las observaciones son imágenes educativas de 64 intensidades. |
| S02 | Producto analítico | Notebook; `submission/` | Incluye evaluación predictiva retenida (PCA, UMAP) además de las tres visualizaciones; t-SNE sigue sin evaluación fuera de muestra. |
| S03 | Evidencia y pruebas | Tres PNG; `pca_components_accuracy.csv/.png`; `umap_components_accuracy.csv`; `components_accuracy_comparison.png`; `tests/test_activity.py` | Las pruebas comprueban existencia y columnas, no significado visual ni estabilidad entre ejecuciones. |
| S04 | Trazabilidad y secuencia | `traceability.yaml`; mapas P201/P225 | Identidad Predictiva resuelta por H04; sigue sin existir entrada P225 en `traceability.yaml` (brecha anterior, no creada por este cambio). |

### Contrato de evidencia actual

- **Notebook o código:** calcula tres proyecciones visuales y, por separado,
  evalúa PCA y UMAP como representaciones predictivas (exactitud de prueba y
  varianza explicada) en función del número de componentes, sobre la misma
  partición y tipo de clasificador que P201.
- **`submission/`:** conserva las tres proyecciones visuales, la tabla y
  gráfico de PCA, y la tabla y gráfico comparativo de UMAP.
- **Pruebas:** comprueban los tres PNG originales y la presencia/columnas de
  los dos CSV y los dos PNG nuevos.
- **Trazabilidad:** sigue sin existir entrada P225 en `traceability.yaml`;
  esa brecha es anterior a H04 y queda fuera de su alcance.

### Dependencias en la secuencia

- **Recibe de P201:** dataset de dígitos, tipo de clasificador y partición
  (test_size=0.5, random_state=0, estratificada); la dependencia pasa de
  conceptual a demostrable.
- **Habilita para Pyyy:** no hay dependencia predictiva demostrable.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe entrada P225 en `implementation/predictiva/traceability.yaml`
(brecha pendiente de escalación, anterior a este cambio). Con H04, el
producto aporta una representación evaluada por exactitud predictiva
retenida, no sólo exploración visual: la auditoría de identidad de la línea
Predictiva queda resuelta.
