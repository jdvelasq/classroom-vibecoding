# P224 — Reducción de dimensionalidad

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P224_reduccion_dimensionalidad/`.

### Preguntas analíticas actuales

- ¿Cómo cambian las proyecciones bidimensionales de imágenes de dígitos cuando
  se usan PCA, t-SNE y UMAP?

Parte de `sklearn.datasets.load_digits`, proyecta las 64 intensidades de cada
dígito y guarda tres gráficos. No entrena ni evalúa un predictor, ni declara
usuario, decisión o producto predictivo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** explora visualmente la estructura de
  imágenes educativas; no hay usuario ni decisión evidenciados.
- **Producto terminal:** tres proyecciones visuales PCA, t-SNE y UMAP.
- **Uso y límite:** permite comparar representaciones de un dataset de dígitos;
  no estima un resultado futuro o no observado, ni mide calidad de clasificación.
- **Disciplinas contribuyentes:** reducción de dimensionalidad y visualización
  sirven a exploración de datos. En su estado actual, el producto no satisface
  por sí solo la línea Predictiva; la auditoría de identidad queda sin resolver.

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
- **H04 — Deja explícito el límite de producto:** no genera estimador,
  predicción, métrica de error ni decisión. Por tanto, no debe justificarse como
  taller predictivo sólo porque emplea técnicas habituales de ML.

### Inventario técnico de implementación

- **Introduce:** PCA, t-SNE y UMAP bidimensionales sobre `load_digits`.
- **Verifica y comunica:** genera y persiste una visualización por método.
- **No evidencia:** separación train/test, modelo supervisado, métrica,
  clasificación, uso organizacional o producto predictivo.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Proyección comparativa | H01 | PCA, t-SNE y UMAP a dos dimensiones | Notebook; parámetros y comparabilidad metodológica limitados. |
| Evidencia visual persistida | H02 | Tres PNG en `submission/` | Pruebas sólo verifican su presencia. |
| Imagen como dato | H03 | Dígitos 8×8 de `load_digits` | No hay evaluación de la representación para clasificación. |
| Límite predictivo | H04 | Ausencia de estimador y métricas en código/entregas | No autoriza inferir una contribución predictiva. |

### Relación técnica con actividades anteriores

P224 reutiliza el dataset de imágenes de P201, pero cambia clasificación y
probabilidades por exploración visual de representaciones. Puede complementar
la lectura de entradas de alta dimensión, pero en la implementación actual no
habilita un producto predictivo demostrable y su posición en Predictiva exige
decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | `professor/notebook.ipynb`: PCA, `TSNE`, `umap.UMAP` | No compara parámetros, tiempos ni fidelidad de cada proyección. |
| H02 | S03 | Notebook: `savefig`; tres PNG en `submission/`; pruebas | Los tests no inspeccionan contenido visual. |
| H03 | S01 | Notebook: `sklearn.datasets.load_digits` | Conjunto educativo sin caso organizacional. |
| H04 | S02, S04 | Notebook, `submission/` y pruebas | La ausencia de predictor no prueba que la actividad deba eliminarse; sólo deja la identidad sin resolver. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y proyección | Notebook; `load_digits` | Las observaciones son imágenes educativas de 64 intensidades. |
| S02 | Producto analítico | Notebook; `submission/` | Sólo hay visualizaciones, sin predictor o evaluación. |
| S03 | Evidencia y pruebas | Tres PNG; `tests/test_activity.py` | Las pruebas comprueban existencia, no significado visual. |
| S04 | Trazabilidad y secuencia | `traceability.yaml`; mapas P201/P224 | No existe entrada P224 y su identidad Predictiva es no resuelta. |

### Contrato de evidencia actual

- **Notebook o código:** calcula tres proyecciones y las grafica.
- **`submission/`:** conserva tres PNG.
- **Pruebas:** comprueban los tres archivos, no su contenido.
- **Trazabilidad:** falta entrada P224 y requiere escalación.

### Dependencias en la secuencia

- **Recibe de P201:** dataset de dígitos e interpretación de imágenes como
  entradas; no se evidencia reutilización de código.
- **Habilita para Pyyy:** no hay dependencia predictiva demostrable.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe entrada P224 en `implementation/predictiva/traceability.yaml`. La
actividad aporta exploración visual de representación, pero su producto actual
no responde a la pregunta propia de Predictiva; auditoría no resuelta.
