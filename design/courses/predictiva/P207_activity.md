# P207 — Clustering de mercadeo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P207_clustering_mercadeo/`.

### Preguntas analíticas actuales

- ¿Qué perfiles de intereses permiten segmentar una población de mercadeo?
- ¿Cómo se interpretan esos segmentos sin usar atributos demográficos para construirlos?

Usa perfiles de estudiantes con conteos de intereses y atributos demográficos. El producto es una segmentación por intereses, sus tamaños, intereses característicos y perfiles complementarios. No predice comportamiento futuro ni autoriza una acción de mercadeo.

### Highlights de contribución

- **Separa señales de segmentación de atributos de descripción:** usa 36 conteos de intereses para agrupar y reserva año de graduación, género, edad y amistades para caracterizar después. Es una dificultad propia del dataset: los perfiles mezclan intereses con atributos personales; sin esta separación, los clusters podrían reflejar directamente rasgos demográficos en vez de intereses.
- **Corrige una variable de perfil sin convertirla en entrada de cluster:** limita edades a 13–19 e imputa las ausentes con la mediana del año de graduación. Así reconoce valores no plausibles del caso antes de describir grupos; sin este hito, la caracterización de segmentos reproduciría edades erróneas.
- **Pondera intereses escasos antes de medir similitud:** transforma la matriz de conteos con TF–IDF y aplica KMeans sobre esa representación. Extiende P206: allí cada hora tenía el mismo rol relativo dentro de un día; aquí intereses frecuentes podrían dominar perfiles de decenas de miles de personas si no se reponderan.
- **Selecciona y hace reproducible una granularidad de segmentos:** compara silueta de 2–8 grupos y ajusta cinco con semilla y múltiples inicializaciones fijas. Sin este hito, los nombres de segmentos serían el resultado accidental de una corrida no justificable.
- **Convierte centroides en hipótesis de perfil verificables:** extrae los ocho intereses más altos por centro, revisa todos los pesos en un heatmap y visualiza separación con UMAP antes de nombrar clusters como Danza, Banda y marcha, Intereses mixtos, Música y rock y Religión. Sin este hito, los nombres serían etiquetas de mercadeo sin vínculo inspeccionable con los datos.
- **Distingue segmentación de caracterización posterior:** calcula tamaños y perfiles de edad, amistades, género y graduación una vez asignados los clusters. Extiende P206 desde conteos de días hacia lectura de audiencia; sin este hito, no se podría contrastar la composición de segmentos sin contaminar su construcción.
- **Persiste la segmentación y sus interpretaciones:** guarda filas segmentadas, tamaños, intereses principales, perfiles y visualizaciones. Sin estos artefactos, la audiencia no podría ser auditada ni revisada fuera del notebook.

### Inventario técnico de implementación

- **Introduce:** depuración e imputación de edad por año de graduación para perfiles descriptivos.
- **Introduce:** separación de variables de clustering y variables de caracterización.
- **Introduce:** TF–IDF aplicado a conteos de intereses, KMeans, silueta y UMAP.
- **Extiende:** interpretación de clusters de P206 con términos principales, heatmap y perfiles complementarios.
- **Reutiliza:** persistencia de asignaciones y evidencia gráfica del modelo no supervisado.

### Relación técnica con actividades anteriores

P207 reutiliza la lógica no supervisada de P206, pero cambia el significado de la representación: perfiles de interés ponderados frente a curvas horarias normalizadas. No es sólo un nuevo caso de KMeans: exige separar atributos personales de señales de segmentación, resolver edad no plausible y justificar nombres a partir de términos ponderados. La ausencia de trazabilidad formal queda pendiente de corrección a nivel de curso.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| Intereses separados de atributos personales | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `interest_columns` y `profile_columns` | Excluir atributos de la entrada no garantiza que los intereses no funcionen como proxies de atributos personales. |
| Edad limpiada e imputada | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `age_clean`, medianas por `gradyear` y `age_imputed` | La mediana por cohorte es una regla de taller y puede ocultar variación individual. |
| TF–IDF sobre intereses | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `TfidfTransformer` e `interest_matrix` | TF–IDF no valida que los intereses reflejen afinidad real ni intención de compra. |
| Silueta, KMeans y reproducibilidad | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: bucle 2–8, `silhouette_score`, `random_state=42` y `n_init` | La tabla de selección no se persiste en `submission/`; no hay evidencia archivada de la comparación tras ejecutar. |
| Términos principales, heatmap y UMAP | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `top_interests`, heatmap, UMAP y nombres; `implementation/predictiva/P207_clustering_mercadeo/submission/top_interests.csv`; `interests-heatmap.png`; `cluster-scatter.png` | UMAP es una proyección de inspección, no una prueba formal de separación ni de validez de etiquetas. |
| Perfiles posteriores a la asignación | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `cluster_profiles`, `gender_profiles` y `gradyear_profiles` | Caracterizar después no elimina proxies ni prueba que los segmentos sean apropiados para una intervención. |
| Persistencia de segmentación e interpretación | `implementation/predictiva/P207_clustering_mercadeo/submission/segmented.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/cluster_sizes.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/cluster_profiles.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/gender_profiles.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/gradyear_profiles.csv`; `implementation/predictiva/P207_clustering_mercadeo/tests/test_activity.py` | Las pruebas verifican presencia de archivos, no validez de segmentos ni uso ético de perfiles. |

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe entrada P207 en `implementation/predictiva/traceability.yaml`; es una inconsistencia que debe resolverse antes de aprobar su mapeo de capacidades. El producto de Analytics es segmentación descriptiva e interpretación de perfiles; TF–IDF, clustering y UMAP contribuyen a él sin convertir el taller en una política de segmentación o una decisión de mercadeo automatizada.
