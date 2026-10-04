# P206 — Clustering de demanda

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P206_clustering_demanda/`.

### Preguntas analíticas actuales

- ¿Qué patrones diarios de demanda comercial aparecen al comparar la forma de sus perfiles horarios?
- ¿Cómo se elige y se interpreta una agrupación de esos perfiles?

Parte de una tabla ancha de demanda por hora y fecha. El producto son perfiles diarios normalizados, asignaciones de cluster, evidencia para elegir el número de grupos y una descripción de su relación observada con el día de semana. No predice demanda futura ni prescribe capacidad.

### Highlights de contribución

- **Separa forma de nivel en una serie de demanda:** transforma columnas horarias en serie larga para visualizar el nivel temporal, y luego divide cada día por su máximo para agrupar la forma relativa. Es la particularidad central del dataset: días de volumen distinto pueden tener curvas horarias semejantes; sin normalización, KMeans segmentaría sobre todo días grandes y pequeños, no patrones operativos.
- **Trata cada fecha como un perfil de 24 entradas:** usa las horas como características del día y visualiza perfiles normalizados antes de agrupar. Introduce una representación distinta de P200–P205: no hay etiqueta ni una fila independiente por observación puntual; sin este hito, el clustering no tendría una unidad de análisis explícita.
- **Justifica el número de grupos antes de asignar nombres:** compara silueta para 2–5 clusters y elige dos, donde el artefacto actual registra la mayor silueta (0.520). Sin este hito, el número de clusters sería una elección decorativa en vez de una hipótesis contrastada.
- **Interpreta centroides como patrones y no como causas:** grafica los centros horarios y cuenta días de la semana por cluster; domingo aparece sólo en el cluster 1, pero el notebook advierte que un cluster no determina un día. Sin este hito, se confundiría una segmentación descriptiva con una regla causal o predictiva.
- **Asigna un perfil recibido con el modelo ajustado:** conserva una fecha y su cluster mediante `kmeans.predict`, además de perfiles, selección y conteos. Extiende la exploración hacia una clasificación no supervisada reutilizable; sin esta evidencia, el modelo quedaría reducido a una visualización estática.

### Inventario técnico de implementación

- **Introduce:** transformación ancha–larga para inspección temporal y perfiles diarios normalizados por máximo.
- **Introduce:** KMeans, silueta para selección de `n_clusters`, centroides y asignaciones de perfiles.
- **Introduce:** interpretación descriptiva de clusters por forma horaria y día de semana, con límite explícito de no determinismo.
- **Introduce:** persistencia de evidencia de selección, perfiles y asignación de un perfil recibido.

### Relación técnica con actividades anteriores

P206 abre una rama no supervisada: P200–P205 usan una etiqueta o probabilidad; P206 descubre estructura en perfiles diarios sin objetivo. No duplica futuros pronósticos temporales: aunque usa demanda por hora, su producto es similitud de forma observada, no estimación de demanda futura.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| Normalización de forma diaria | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: tabla ancha, `melt` y `data.div(data.max(axis=1), axis=0)` | Dividir por máximo descarta magnitud absoluta y puede amplificar días de demanda muy baja. |
| Día como perfil horario | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: visualización de serie y perfiles de 24 horas | No documenta procedencia externa ni significado operacional de cada hora. |
| Selección por silueta | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: bucle 2–5 y `silhouette_score`; `implementation/predictiva/P206_clustering_demanda/submission/cluster-selection.csv` | La silueta no garantiza utilidad operativa ni estabilidad en nuevos períodos. |
| Interpretación por centroides y día | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: centroides, `day_of_week` y conteos; `implementation/predictiva/P206_clustering_demanda/submission/demanda-comercial-dias.csv` | Asociación con día de semana no prueba causalidad ni permite pronóstico determinista. |
| Perfil recibido persistido | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: `kmeans.predict`; `implementation/predictiva/P206_clustering_demanda/submission/perfil-recibido.csv`; `implementation/predictiva/P206_clustering_demanda/tests/test_activity.py` | Las pruebas verifican presencia de archivos, no que el perfil sea reproducible al cambiar datos. |

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

P206 está mapeada a `predictiva.C02` y `predictiva.C03` en `implementation/predictiva/traceability.yaml`. El producto de Analytics es una segmentación descriptiva de perfiles de demanda; normalización y clustering la sirven, sin convertirla en predicción, optimización de turnos o política de capacidad.
