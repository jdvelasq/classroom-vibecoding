# P208 — Clustering de mercadeo

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P207_clustering_mercadeo/`.

### Preguntas analíticas actuales

- ¿Qué perfiles de intereses permiten segmentar una población de mercadeo?
- ¿Cómo se interpretan esos segmentos sin usar atributos demográficos para construirlos?

Usa perfiles de estudiantes con conteos de intereses y atributos demográficos. El producto es una segmentación por intereses, sus tamaños, intereses característicos y perfiles complementarios. No predice comportamiento futuro ni autoriza una acción de mercadeo.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** segmenta intereses; no predice conducta ni autoriza mercadeo.
- **Producto terminal:** clusters, perfiles e interpretaciones persistidas.
- **Uso y límite:** atributos personales describen después; no prueban causalidad o acción.
- **Disciplinas contribuyentes:** TF–IDF, KMeans y UMAP sirven a segmentación; identidad Predictiva no resuelta.

### Highlights de contribución

- **H01 — Separa señales de segmentación de atributos de descripción:** usa 36 conteos de intereses para agrupar y reserva año de graduación, género, edad y amistades para caracterizar después. Es una dificultad propia del dataset: los perfiles mezclan intereses con atributos personales; sin esta separación, los clusters podrían reflejar directamente rasgos demográficos en vez de intereses.
- **H02 — Corrige una variable de perfil sin convertirla en entrada de cluster:** limita edades a 13–19 e imputa las ausentes con la mediana del año de graduación. Así reconoce valores no plausibles del caso antes de describir grupos; sin este hito, la caracterización de segmentos reproduciría edades erróneas.
- **H03 — Pondera intereses escasos antes de medir similitud:** transforma la matriz de conteos con TF–IDF y aplica KMeans sobre esa representación. Extiende P207: allí cada hora tenía el mismo rol relativo dentro de un día; aquí intereses frecuentes podrían dominar perfiles de decenas de miles de personas si no se reponderan.
- **H04 — Selecciona y hace reproducible una granularidad de segmentos:** compara silueta de 2–8 grupos y ajusta cinco con semilla y múltiples inicializaciones fijas. Sin este hito, los nombres de segmentos serían el resultado accidental de una corrida no justificable.
- **H05 — Convierte centroides en hipótesis de perfil verificables:** extrae los ocho intereses más altos por centro, revisa todos los pesos en un heatmap y visualiza separación con UMAP antes de nombrar clusters como Danza, Banda y marcha, Intereses mixtos, Música y rock y Religión. Sin este hito, los nombres serían etiquetas de mercadeo sin vínculo inspeccionable con los datos.
- **H06 — Distingue segmentación de caracterización posterior:** calcula tamaños y perfiles de edad, amistades, género y graduación una vez asignados los clusters. Extiende P207 desde conteos de días hacia lectura de audiencia; sin este hito, no se podría contrastar la composición de segmentos sin contaminar su construcción.
- **H07 — Persiste la segmentación y sus interpretaciones:** guarda filas segmentadas, tamaños, intereses principales, perfiles y visualizaciones. Sin estos artefactos, la audiencia no podría ser auditada ni revisada fuera del notebook.

### Inventario técnico de implementación

- **Introduce:** depuración e imputación de edad por año de graduación para perfiles descriptivos.
- **Introduce:** separación de variables de clustering y variables de caracterización.
- **Introduce:** TF–IDF aplicado a conteos de intereses, KMeans, silueta y UMAP.
- **Extiende:** interpretación de clusters de P207 con términos principales, heatmap y perfiles complementarios.
- **Reutiliza:** persistencia de asignaciones y evidencia gráfica del modelo no supervisado.

### Índice de comparación externa

| Ancla | Hitos | Mecanismo | Límite |
| --- | --- | --- | --- |
| Separación atributos/intereses | H01–H02 | Intereses para cluster, atributos después | No evita todos los proxies. |
| Representación/selección | H03–H04 | TF–IDF, silueta y semilla | No predice conducta. |
| Interpretación/auditoría | H05–H07 | Términos, UMAP y perfiles | Nombres son hipótesis. |

### Relación técnica con actividades anteriores

P208 reutiliza la lógica no supervisada de P207, pero cambia el significado de la representación: perfiles de interés ponderados frente a curvas horarias normalizadas. No es sólo un nuevo caso de KMeans: exige separar atributos personales de señales de segmentación, resolver edad no plausible y justificar nombres a partir de términos ponderados. La ausencia de trazabilidad formal queda pendiente de corrección a nivel de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Intereses separados de atributos personales | S01 | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `interest_columns` y `profile_columns` | Excluir atributos de la entrada no garantiza que los intereses no funcionen como proxies de atributos personales. |
| H02 — Edad limpiada e imputada | S01 | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `age_clean`, medianas por `gradyear` y `age_imputed` | La mediana por cohorte es una regla de taller y puede ocultar variación individual. |
| H03 — TF–IDF sobre intereses | S02 | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `TfidfTransformer` e `interest_matrix` | TF–IDF no valida que los intereses reflejen afinidad real ni intención de compra. |
| H04 — Silueta, KMeans y reproducibilidad | S02 | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: bucle 2–8, `silhouette_score`, `random_state=42` y `n_init` | La tabla de selección no se persiste en `submission/`; no hay evidencia archivada de la comparación tras ejecutar. |
| H05 — Términos principales, heatmap y UMAP | S03 | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `top_interests`, heatmap, UMAP y nombres; `implementation/predictiva/P207_clustering_mercadeo/submission/top_interests.csv`; `interests-heatmap.png`; `cluster-scatter.png` | UMAP es una proyección de inspección, no una prueba formal de separación ni de validez de etiquetas. |
| H06 — Perfiles posteriores a la asignación | S03 | `implementation/predictiva/P207_clustering_mercadeo/professor/notebook.ipynb`: `cluster_profiles`, `gender_profiles` y `gradyear_profiles` | Caracterizar después no elimina proxies ni prueba que los segmentos sean apropiados para una intervención. |
| H07 — Persistencia de segmentación e interpretación | S03 | `implementation/predictiva/P207_clustering_mercadeo/submission/segmented.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/cluster_sizes.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/cluster_profiles.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/gender_profiles.csv`; `implementation/predictiva/P207_clustering_mercadeo/submission/gradyear_profiles.csv`; `implementation/predictiva/P207_clustering_mercadeo/tests/test_activity.py` | Las pruebas verifican presencia de archivos, no validez de segmentos ni uso ético de perfiles. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y atributos de perfil | `data/snsdata.csv`; notebook | Intereses pueden ser proxies de atributos personales. |
| S02 | Edad, representación y clusters | Notebook; `segmented.csv`; `top_interests.csv` | La imputación y TF–IDF condicionan los perfiles observados. |
| S03 | Interpretación y producto | Perfiles, gráficos y pruebas | Selección de cinco grupos no se persiste como tabla. |
| S04 | Trazabilidad | `traceability.yaml` | Falta entrada P208; no se deben inferir capacidades aprobadas. |

### Contrato de evidencia actual

- **Notebook o código:** limpia edad, transforma intereses, selecciona y ajusta
  clusters, nombra perfiles y calcula caracterizaciones posteriores.
- **`submission/`:** conserva segmentos, tamaños, intereses, perfiles y
  visualizaciones; no conserva la tabla de silueta.
- **Pruebas:** exigen seis CSV, sin validar selección, separación ni uso ético.
- **Trazabilidad:** no existe entrada P208; requiere escalación.

### Dependencias en la secuencia

- **Recibe de P207:** KMeans, silueta e interpretación descriptiva de clusters.
- **Habilita para P226:** no hay dependencia demostrable; ambos usan métodos no
  supervisados, pero sus representaciones y productos son diferentes.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

No existe entrada P208 en `implementation/predictiva/traceability.yaml`; es una inconsistencia que debe resolverse antes de aprobar su mapeo de capacidades. El producto de Analytics es segmentación descriptiva e interpretación de perfiles; TF–IDF, clustering y UMAP contribuyen a él sin convertir el taller en una política de segmentación o una decisión de mercadeo automatizada.
