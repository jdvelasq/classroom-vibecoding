# P207 — Clustering de demanda

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P206_clustering_demanda/`.

### Preguntas analíticas actuales

- ¿Qué patrones diarios de demanda comercial aparecen al comparar la forma de sus perfiles horarios?
- ¿Cómo se elige y se interpreta una agrupación de esos perfiles?

Parte de una tabla ancha de demanda por hora y fecha. El producto son perfiles diarios normalizados, asignaciones de cluster, evidencia para elegir el número de grupos y una descripción de su relación observada con el día de semana. No predice demanda futura ni prescribe capacidad.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** describe arquetipos diarios; no pronostica ni decide capacidad.
- **Producto terminal:** perfiles normalizados, clusters, selección y asignación de perfil recibido.
- **Uso y límite:** cluster es patrón, no causa, fecha o pronóstico.
- **Disciplinas contribuyentes:** KMeans sirve a segmentación descriptiva; identidad Predictiva queda no resuelta.

### Highlights de contribución

- **H01 — Separa forma de nivel en una serie de demanda:** transforma columnas horarias en serie larga para visualizar el nivel temporal, y luego divide cada día por su máximo para agrupar la forma relativa. Es la particularidad central del dataset: días de volumen distinto pueden tener curvas horarias semejantes; sin normalización, KMeans segmentaría sobre todo días grandes y pequeños, no patrones operativos.
- **H02 — Trata cada fecha como un perfil de 24 entradas:** la matriz de
  clustering tiene **filas = días** y **columnas = horas**; cada fila resume la
  forma normalizada de un día completo. Por ello un cluster se interpreta como
  un arquetipo de patrón horario diario —por ejemplo, una forma dominical frente
  a una forma de jornada comercial—, no como un grupo de mediciones horarias
  aisladas ni como un pronóstico. Sin este hito, la unidad de análisis y la
  lectura de los centroides quedarían ambiguas.
- **H03 — Justifica el número de grupos antes de asignar nombres:** compara silueta para 2–5 clusters y elige dos, donde el artefacto actual registra la mayor silueta (0.520). Sin este hito, el número de clusters sería una elección decorativa en vez de una hipótesis contrastada.
- **H04 — Interpreta centroides como patrones y no como causas:** grafica los centros horarios y cuenta días de la semana por cluster; domingo aparece sólo en el cluster 1, pero el notebook advierte que un cluster no determina un día. Sin este hito, se confundiría una segmentación descriptiva con una regla causal o predictiva.
- **H05 — Asigna un perfil recibido con el modelo ajustado:** conserva una fecha y su cluster mediante `kmeans.predict`, además de perfiles, selección y conteos. Extiende la exploración hacia una clasificación no supervisada reutilizable; sin esta evidencia, el modelo quedaría reducido a una visualización estática.

### Inventario técnico de implementación

- **Introduce:** transformación ancha–larga para inspección temporal y perfiles diarios normalizados por máximo.
- **Introduce:** KMeans, silueta para selección de `n_clusters`, centroides y asignaciones de perfiles.
- **Introduce:** interpretación descriptiva de clusters por forma horaria y día de semana, con límite explícito de no determinismo.
- **Introduce:** persistencia de evidencia de selección, perfiles y asignación de un perfil recibido.

### Índice de comparación externa

| Ancla | Hitos | Mecanismo | Límite |
| --- | --- | --- | --- |
| Perfil día×hora | H01–H02 | Filas=días, columnas=horas, normalización | Pierde nivel absoluto. |
| Selección/lectura | H03–H04 | Silueta, centroides y día semana | No causal/predictiva. |
| Reuso | H05 | `kmeans.predict` y artefactos | No predice demanda. |

### Relación técnica con actividades anteriores

P207 abre una rama no supervisada: P200–P205 usan una etiqueta o probabilidad; P207 descubre estructura en perfiles diarios sin objetivo. No duplica futuros pronósticos temporales: aunque usa demanda por hora, su producto es similitud de forma observada, no estimación de demanda futura.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Normalización de forma diaria | S01 | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: tabla ancha, `melt` y `data.div(data.max(axis=1), axis=0)` | Dividir por máximo descarta magnitud absoluta y puede amplificar días de demanda muy baja. |
| H02 — Día como perfil horario | S01 | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: `data` con fechas como índice y horas como columnas, perfiles y centroides | No documenta procedencia externa ni significado operacional de cada hora. |
| H03 — Selección por silueta | S02 | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: bucle 2–5 y `silhouette_score`; `implementation/predictiva/P206_clustering_demanda/submission/cluster-selection.csv` | La silueta no garantiza utilidad operativa ni estabilidad en nuevos períodos. |
| H04 — Interpretación por centroides y día | S03 | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: centroides, `day_of_week` y conteos; `implementation/predictiva/P206_clustering_demanda/submission/demanda-comercial-dias.csv` | Asociación con día de semana no prueba causalidad ni permite pronóstico determinista. |
| H05 — Perfil recibido persistido | S02, S03 | `implementation/predictiva/P206_clustering_demanda/professor/notebook.ipynb`: `kmeans.predict`; `implementation/predictiva/P206_clustering_demanda/submission/perfil-recibido.csv`; `implementation/predictiva/P206_clustering_demanda/tests/test_activity.py` | Las pruebas verifican presencia de archivos, no que el perfil sea reproducible al cambiar datos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Serie horaria y perfil diario | `data/demanda_comercial.csv.gz`; notebook | Normalizar por máximo elimina nivel absoluto. |
| S02 | Agrupación y selección | Notebook; `cluster-selection.csv` | La silueta no prueba utilidad ni estabilidad fuera del período. |
| S03 | Interpretación y producto | CSV y gráficos de `submission/`; pruebas | El cluster no permite causalidad ni pronóstico. |

### Contrato de evidencia actual

- **Notebook o código:** transforma series, normaliza, selecciona KMeans,
  interpreta centroides y asigna un perfil.
- **`submission/`:** conserva selección, asignaciones, conteos y gráficos.
- **Pruebas:** exigen siete artefactos, sin validar valores ni estabilidad.
- **Trazabilidad:** P207 mapea `predictiva.C02` y `C03`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna técnica no supervisada previa demostrable.
- **Habilita para P208:** selección e interpretación de KMeans, ahora aplicadas
  a perfiles de interés con una representación distinta.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

P207 está mapeada a `predictiva.C02` y `predictiva.C03` en `implementation/predictiva/traceability.yaml`. El producto de Analytics es una segmentación descriptiva de perfiles de demanda; normalización y clustering la sirven, sin convertirla en predicción, optimización de turnos o política de capacidad.
