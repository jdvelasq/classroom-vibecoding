# P123 — Scopus: mapa bibliométrico de un campo tecnológico (PropTech)

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P123_scopus/`.

### Preguntas analíticas actuales

- ¿Qué países concentran la mayor producción bibliográfica en el área?
- ¿Cómo evoluciona la producción bibliográfica en el tiempo y qué períodos se distinguen?
- ¿Qué fuentes, autores y palabras clave caracterizan el campo?

El caso se declara de «inteligencia tecnológica basado en producción bibliográfica». Usa una exportación de Scopus (`data/scopus.csv.gz`) delimitada por la cadena persistida en `data/search_string.txt` (`TITLE-ABS-KEY` sobre *proptech*, *property technology*, *real estate technology* y variantes de digitalización inmobiliaria). La fecha de consulta, el número de registros y los filtros adicionales no están documentados. No hay notebook: el profesor ejecuta `professor/main.py`, que orquesta veinte pasos `s01`–`s20` sobre una copia de trabajo en `submission/scopus.csv.gz`. El producto es un conjunto de frecuencias, matrices de co-ocurrencia, comunidades y visualizaciones HTML que describen quién, dónde, cuándo y sobre qué se publica; no evalúa calidad, impacto ni madurez tecnológica.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** caracterizar un campo tecnológico por países, años, fuentes, autores y temas; usuario y decisión no evidenciados.
- **Producto terminal:** reportes de frecuencia (países, fuentes, autores, palabras clave), serie anual, mapa mundial, matrices de co-ocurrencia de países y palabras clave, comunidades Louvain y redes interactivas.
- **Uso y límite:** permite describir concentración geográfica, temporal y temática del corpus recuperado; no generaliza más allá de la cadena de búsqueda, no mide intensidad de colaboración más allá del conteo de documentos compartidos y las comunidades dependen de normalización, filtro y semilla.
- **Disciplinas contribuyentes:** bibliometría, análisis de redes (`networkx`), cartografía (`folium`) y Plotly sirven a la descripción del campo.

### Highlights de contribución

- **H01 — Delimita el corpus con una consulta persistida:** `data/search_string.txt` conserva la cadena de búsqueda que define la población de documentos. Primera actividad del curso cuyo dataset es el resultado de una consulta; sin este hito, las frecuencias no tendrían frontera declarada. Límite: falta fecha de extracción y conteo de registros.
- **H02 — Convierte campos multivaluados en unidades contables:** la particularidad del caso es que una fila es un documento con listas separadas por «;». `s03` extrae el país como último segmento tras coma de cada afiliación y deduplica por documento; `s14` une palabras clave de autor e índice. Los reportes cuentan documentos por ítem (conteo completo), por eso sus sumas superan el número de documentos. Contrasta con P100, que contaba palabras de texto libre; sin este hito, afiliaciones y palabras clave serían texto no agregable.
- **H03 — Normaliza vocabularios con diccionarios de reemplazo y una lista válida externa:** países con un diccionario hacia los nombres del GeoJSON del mapa (por ejemplo, «USA» → «United States of America», «Palestine» → «West Bank») y descarte de nombres ausentes de ese GeoJSON descargado en ejecución; palabras clave en mayúsculas con cuatro reemplazos (`BLOCK-CHAIN`, `BLOCKCHAIN TECHNOLOGY` → `BLOCKCHAIN`, etc.). Extiende los diccionarios de reemplazo de P106 a entidades bibliográficas. Límite: el vocabulario válido de países lo fija la geometría del mapa, y el ruido residual es visible (`REAL-ESTATES` frente a `REAL ESTATE`; `AUSTRALIA`, `CHINA` y `DUCTILITY` como palabras clave).
- **H04 — Construye matrices de co-ocurrencia por documento:** `make_cooc_matrix` explota filas y columnas del mismo campo; la matriz tiene filas = ítems y columnas = ítems, diagonal = documentos con el ítem y fuera de la diagonal = documentos que comparten ambos. Para países representa co-afiliación internacional (65 países); para palabras clave se filtra a términos con diagonal ≥ 10 (32 términos). Primera representación relacional del curso; sin este hito, el análisis se quedaría en conteos univariados.
- **H05 — Pasa de matriz a comunidades y red:** elimina lazos propios y pesos nulos, detecta comunidades con Louvain (`seed=0`) y dibuja redes con tamaño por frecuencia, color por comunidad y grosor por peso. `country_clusters.txt` persiste 23 grupos, 14 de ellos de un solo país; `keywords_clusters.txt`, seis grupos, dos unitarios (`DUCTILITY`, `PLS-SEM`). Sin este hito, la estructura temática y de colaboración no sería visible; el límite es que no se reporta modularidad ni estabilidad.
- **H06 — Completa la serie anual con años sin documentos:** `s02` reindexa el rango de años y rellena con cero antes de graficar. Sin este hito, años vacíos desaparecerían del eje. Límite: la pregunta «qué períodos se distinguen» se responde sólo con el HTML; no hay segmentación ni control del último año incompleto.
- **H07 — Organiza el caso como pipeline de pasos persistentes y funciones reutilizadas:** `main.py` encadena `s01`–`s20`; cada paso lee y reescribe `submission/scopus.csv.gz`, y las funciones de frecuencia, matriz, comunidades y red se reutilizan para países y palabras clave. Extiende la modularización de P101 a un flujo analítico completo; sin este hito, el mismo procedimiento se reescribiría para cada entidad. Límite: depende de red externa (`requests.get` al importar `s04`; URL de GeoJSON en `s07`).
- **H08 — Verifica existencia y coherencia mínima de los productos:** las pruebas exigen el conjunto exacto de dieciséis archivos, que la suma de `source_frequency.csv` iguale los títulos abreviados no vacíos y sea decreciente, que la suma de autores no sea menor que el número de registros, que las tablas no estén vacías y que los HTML superen 1.000 bytes.

### Inventario técnico de implementación

- **Introduce:** corpus definido por consulta; `str.split(";").explode().value_counts()` sobre campos multivaluados; diccionario de reemplazo validado contra vocabulario externo; matriz de co-ocurrencia; filtro por diagonal; `networkx` (adyacencia, Louvain, `spring_layout`); mapa coroplético con `folium`; salidas HTML.
- **Extiende:** modularización en funciones (P101); diccionarios de reemplazo (P106); conteo de términos (P100).
- **Reutiliza:** contrato `questions.json`; persistencia en `submission/`; Plotly.
- **Aplica en nuevo caso:** frecuencias y gráficos de barras horizontales a entidades bibliográficas.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Corpus por consulta | H01 | `search_string.txt` | Sin fecha ni conteo de extracción. |
| Campos multivaluados | H02–H03 | Extracción de país por afiliación; unión y normalización de palabras clave | Conteo completo; vocabulario de países atado al mapa. |
| Co-ocurrencia | H04 | Matriz ítem × ítem; filtro por diagonal ≥ 10 | Co-ocurrencia no es causalidad ni intensidad de colaboración. |
| Comunidades y redes | H05 | Louvain `seed=0`; redes HTML | Sin modularidad ni estabilidad. |
| Serie anual | H06 | Años faltantes rellenados con cero | Períodos no segmentados. |
| Pipeline | H07–H08 | `main.py` + `s01`–`s20`; dieciséis archivos | Dependencia de red; pruebas de existencia y sumas. |

### Relación técnica con actividades anteriores

P123 no repite la plantilla tabular de P120–P122: introduce nueva representación (campos multivaluados, matrices de co-ocurrencia, redes) y un nuevo tipo de producto (mapa del campo en HTML). Recupera prácticas técnicas de los fundamentos: conteo de términos (P100), funciones y orquestación en `main.py` (P101) y diccionarios de reemplazo (P106). Conserva el contrato `questions.json`, aunque la tercera pregunta (fuentes, autores y palabras clave) apunta sólo a `keywords_frequency.csv` pese a existir `source_frequency.csv` y `authors_frequency.csv`. Es la única actividad del rango sin notebook de profesor.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Consulta persistida | S01 | `implementation/descriptiva/P123_scopus/data/search_string.txt`; `implementation/descriptiva/P123_scopus/data/scopus.csv.gz` | No se documenta fecha, base de suscripción ni número de registros. |
| H02 — Campos multivaluados | S02 | `implementation/descriptiva/P123_scopus/professor/s03_countries_create.py`; `implementation/descriptiva/P123_scopus/professor/s14_keywords_create.py`; `implementation/descriptiva/P123_scopus/professor/s05_countries_frequency_report.py` | El país se toma del último segmento de la afiliación sin verificación adicional. |
| H03 — Normalización | S03 | `implementation/descriptiva/P123_scopus/professor/s04_countries_clean.py`; `implementation/descriptiva/P123_scopus/professor/s15_keywords_clean.py`; `implementation/descriptiva/P123_scopus/submission/keywords_clusters.txt` | Reemplazo por subcadena; un término que ya contenga la forma destino puede alterarse (por ejemplo, «NLP APPLICATIONS»). |
| H04 — Co-ocurrencia | S04 | `implementation/descriptiva/P123_scopus/professor/s08_countries_cooc_matrix.py`; `implementation/descriptiva/P123_scopus/professor/s18_keywords_filter.py`; `implementation/descriptiva/P123_scopus/submission/country_cooc_matrix.csv`; `implementation/descriptiva/P123_scopus/submission/keywords_cooc_matrix.csv` | Umbral de 10 documentos sin justificación persistida. |
| H05 — Comunidades y red | S04, S05 | `implementation/descriptiva/P123_scopus/professor/s10_countries_clusters.py`; `implementation/descriptiva/P123_scopus/professor/s11_countries_network.py`; `implementation/descriptiva/P123_scopus/submission/country_clusters.txt`; `implementation/descriptiva/P123_scopus/submission/keywords_clusters.txt` | El texto emergente de la red rotula como «Frequency» el tamaño escalado, no la frecuencia. |
| H06 — Serie anual completa | S05 | `implementation/descriptiva/P123_scopus/professor/s02_make_documents_by_year_plot.py`; `implementation/descriptiva/P123_scopus/submission/documents_by_year.html` | No se segmentan períodos ni se marca el año en curso. |
| H07 — Pipeline | S06 | `implementation/descriptiva/P123_scopus/professor/main.py`; módulos `s12`, `s13`, `s16`, `s17`, `s19`, `s20` que reutilizan funciones | `src/main.py` del estudiante sólo lanza `NotImplementedError`; no hay notebook guía. |
| H08 — Pruebas | S07 | `implementation/descriptiva/P123_scopus/tests/test_activity.py`: `test_01`–`test_03` | No verifican países, normalización, matrices, comunidades ni contenido de preguntas. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Corpus y procedencia | `data/scopus.csv.gz`; `data/search_string.txt` | Procedencia parcial: consulta sí, fecha y tamaño no. |
| S02 | Extracción de entidades multivaluadas | `professor/s03_countries_create.py`; `professor/s14_keywords_create.py` | Conteo completo por documento. |
| S03 | Normalización de vocabularios | `professor/s04_countries_clean.py`; `professor/s15_keywords_clean.py` | Lista válida descargada en ejecución; reemplazos por subcadena. |
| S04 | Co-ocurrencia, filtro y comunidades | `professor/s08_*`, `s10_*`, `s17_*`, `s18_*`, `s19_*` | Umbral 10; Louvain con semilla fija. |
| S05 | Visualizaciones HTML | `professor/s02_*`, `s06_*`, `s07_*`, `s09_*`, `s11_*`, `s20_*`; seis HTML en `submission/` | HTML de varios MB; mapa con URL externa. |
| S06 | Orquestación e interfaz del estudiante | `professor/main.py`; `src/main.py` | Sin notebook; estado intermedio sobreescrito en `submission/scopus.csv.gz`. |
| S07 | Pruebas | `tests/test_activity.py` | Existencia, sumas y tamaños mínimos. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` escribe preguntas y ejecuta veinte pasos de ingestión, extracción, normalización, frecuencia, co-ocurrencia, comunidades y visualización.
- **`submission/`:** `questions.json`, `scopus.csv.gz` enriquecido, cuatro reportes de frecuencia, dos matrices, dos archivos de comunidades y seis HTML (serie anual, barras de países, mapa, mapa de calor, dos redes).
- **Pruebas:** conjunto exacto de archivos; coherencia de la suma de fuentes y del conteo de autores; tablas no vacías; HTML no triviales. No verifican la lógica de países, palabras clave ni comunidades.
- **Trazabilidad:** P123 mapea `descriptiva.C01`, `C02`, `C03` y `C05`.

### Dependencias en la secuencia

- **Recibe de P100/P101/P106:** conteo de términos, modularización en funciones con `main.py` y diccionarios de reemplazo como patrón de normalización; de P120, el contrato `questions.json`.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P123 está mapeada a `descriptiva.C01`, `descriptiva.C02`, `descriptiva.C03` y `descriptiva.C05` en `implementation/descriptiva/traceability.yaml`. C01–C03 están sostenidas por preguntas, exploración multivaluada y visualizaciones; C05 se apoya en productos HTML persistentes y en la cadena de búsqueda, aunque la documentación de procedencia es incompleta. El producto de Analytics es una descripción del campo (quién, dónde, cuándo, sobre qué); bibliometría, redes y cartografía contribuyen a él. Riesgo de identidad: sin usuario ni decisión evidenciados y sin notebook que haga visibles las decisiones, el taller podría leerse como recetario de herramientas bibliométricas; la co-ocurrencia se presenta como estructura descriptiva, sin afirmaciones causales.
