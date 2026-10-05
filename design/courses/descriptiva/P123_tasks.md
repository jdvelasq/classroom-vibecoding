# P123 — Propuestas de mejora

**Línea base:** `P123_activity.md` (entrada S02 más reciente: `S02.P123.01`).

## T01 — Completar la frontera del corpus: fecha de extracción, número de registros y último año posiblemente parcial

- **Estado:** pendiente de discusión
- **Tipo:** caso/datos + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 40, 45 y 51 — «Students also need to consider the provenance of the data used» (p. 40); «Data provenance» encabeza los conceptos de gestión y curaduría de datos importantes para todos los estudiantes (p. 45); entre las responsabilidades éticas, «the responsibility to ensure that results produced by the analyst are reproducible» (p. 51) (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general de procedencia y reproducibilidad.
  - `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` p. 6 — el entregable «Data Collection Report» debe «describe procedures followed to collect the data, […] data format, dataset size, how the data is stored, characteristics of the data» (Claude, 2026-10-04). Fuente *institutional*: ilustra cómo un programa exige declarar procedimiento y tamaño de la recolección.
  - `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` pp. 13 y 29 — «Documentar los datos. Registrar fuentes, significado, procedencia, limitaciones y condiciones de uso» (p. 13); en gobernanza, «Documentar los datos y procesos. Registrar el origen, el propósito, el uso» (p. 29) (Claude, 2026-10-04). Fuente *literature-derived*: perspectiva metodológica.
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` pp. 18, 19 y 21 — en la descripción de datos de CRISP-DM, «be sure to include size statistics for all data sets, and remember to consider both the number of records as well as fields» (p. 18); el informe de descripción pide «Identify the method used to capture the data» y «How large is the database (in numbers of rows and columns)?» (p. 19); lista de control: «Have you noted the size of all data sources?» (p. 21) (Claude, 2026-10-04). Fuente *professional-learning*: práctica de metodología de proyecto.
- **Qué gana el estudiante:** entender la evidencia bibliométrica como un
  corte fechado y acotado por la consulta, y no leer como caída lo que es
  un año en curso. P123 es el único taller cuyo dataset es el resultado de
  una consulta (H01), pero su límite declarado es «falta fecha de
  extracción y conteo de registros» (H01, S01). Además H06 rellena años
  vacíos sin «control del último año incompleto», y la pregunta «¿cómo
  evoluciona la producción… y qué períodos se distinguen?» se responde sólo
  con el HTML: si la exportación se hizo durante el último año de la serie,
  su barra baja puede leerse como un declive del campo. Con la fecha y el
  número de registros persistidos, una verificación de que el número de
  registros coincide con las filas cargadas y una marca del último año
  como parcial cuando corresponda, la frontera declarada pasa a ser
  frontera comprobable y la lectura temporal deja de ser engañosa.
- **Anclas actuales:** H01 (consulta persistida), H06 (serie anual completa),
  H08 (pruebas de existencia y coherencia); superficies S01 (corpus y
  procedencia), S05 (visualizaciones HTML, `s02_*`) y S07 (pruebas, que hoy
  exigen el conjunto exacto de dieciséis archivos).
- **Alternativas menores descartadas:** escribir la fecha como comentario en
  `search_string.txt` aclara, pero no permite verificar el tamaño ni corrige
  la lectura de la serie. Eliminar el último año de la serie ocultaría
  datos y cambiaría H06; la propuesta lo conserva y lo marca.
- **Contrato de no regresión:** se conservan H01–H08, `search_string.txt`,
  `scopus.csv.gz`, los pasos `s01`–`s20`, `main.py` y los dieciséis
  productos con su contenido; la serie anual conserva todos los años y sus
  conteos (sólo se añade la marca de parcialidad). La única prueba
  existente que cambia es la del conjunto exacto de archivos, que se amplía
  sin quitar ninguno. La fecha y el número de registros los aporta el
  profesor desde sus registros de la consulta a Scopus; la herramienta no
  los infiere ni los inventa.
- **Interacciones:** independiente de T02. Ambas amplían la prueba del
  conjunto exacto de archivos y tocan `main.py` o pasos del pipeline;
  ejecutar T01 primero y actualizar esa prueba una vez por propuesta. El
  número de documentos que T01 deja verificado es el mismo N que usa T02
  como denominador, lo que las refuerza. Capacidad: P123 es un pipeline de
  veinte pasos sin notebook; T01 es un cambio pequeño (un archivo de
  metadatos, una marca en `s02` y una prueba) y no compite por tiempo de
  taller con T02.
- **Criterio de aceptación:** S05 encuentra (1) la fecha de extracción, la
  base consultada, los filtros adicionales (o «ninguno») y el número de
  registros reportado por Scopus persistidos junto a la consulta, con los
  valores aprobados por el profesor y registrados en `P123_log.md`; (2)
  `submission/corpus_boundary.json` con esos datos, las filas y columnas
  cargadas, el primer y último año y si el último año es parcial; (3) la
  serie de `documents_by_year.html` con el último año marcado como parcial
  cuando la fecha de extracción cae en él; y (4) una prueba que verifica
  que el número de registros reportado coincide con las filas de
  `data/scopus.csv.gz` y que la marca de parcialidad es coherente con la
  fecha. H01 se actualiza para retirar el límite «falta fecha de
  extracción y conteo de registros».

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P123_scopus/

0. Inspecciona primero data/ (scopus.csv.gz, search_string.txt),
   professor/main.py, professor/s01_*.py, professor/s02_*.py, submission/ y
   tests/test_activity.py. Si la implementación no coincide con
   design/courses/descriptiva/P123_activity.md (o ya documenta fecha y
   tamaño de extracción), detente e informa sin modificar nada.
1. PROCEDENCIA: no inventes ni infieras la fecha de extracción, la base ni
   el número de registros. Usa los valores que el profesor haya aportado
   desde sus registros de la consulta a Scopus en la discusión de esta T01
   (registrados en P123_log.md). Si no existen, detente y pídelos. No uses
   el número de filas del CSV como sustituto del número reportado por
   Scopus.
2. Persiste esos valores en data/corpus_metadata.json con claves
   database, query_file («search_string.txt»), extraction_date
   (AAAA-MM-DD), additional_filters, records_reported. No modifiques
   search_string.txt ni scopus.csv.gz.
3. Si las filas de data/scopus.csv.gz no coinciden con records_reported,
   detente e informa la diferencia: puede haber duplicados, filtros o una
   exportación distinta, y el profesor debe decidir.
4. En el paso que corresponda (s01 o un paso nuevo invocado desde
   main.py antes de s02, sin renumerar los existentes), escribe
   submission/corpus_boundary.json con las claves de corpus_metadata.json
   más records_loaded, fields_loaded, first_year, last_year y
   last_year_partial (true si el año de extraction_date es igual a
   last_year).
5. En s02, si last_year_partial es true, marca ese año en
   documents_by_year.html (color o patrón distinto y anotación «parcial:
   extracción AAAA-MM-DD»). No elimines el año ni cambies los conteos ni el
   relleno con cero de H06.
6. En tests/test_activity.py amplía la prueba del conjunto exacto de
   archivos con corpus_boundary.json (sin quitar los dieciséis actuales) y
   añade una prueba que verifique: records_reported == records_loaded ==
   filas de data/scopus.csv.gz; last_year igual al año máximo del corpus;
   last_year_partial coherente con extraction_date; y, si es true, que el
   HTML contiene la anotación «parcial». No elimines pruebas existentes.
7. Ejecuta professor/main.py completo y las pruebas de la actividad sin
   errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```

## T02 — Normalizar la co-ocurrencia de palabras clave por la esperada por azar (fuerza de asociación / lift) antes de filtrar y detectar comunidades

- **Estado:** pendiente de discusión
- **Tipo:** método
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` pp. 80–81 y 140 — soporte y confianza pueden ser altos «and yet still produce a rule that is not useful»; «Lift indicates the strength of a rule over the random co-occurrence of the antecedent and the consequent, given their individual support» (p. 80); «Any rule with an improvement of less than 1 does not indicate a real cross-selling opportunity» (p. 81); las asociaciones entre palabras de una colección de documentos «provide context for account in the document collection» (p. 140): una co-ocurrencia frecuente no implica asociación mayor que la esperada por azar (Claude, 2026-10-04). Fuente *professional-learning*, única y de reglas de canasta: se usa sólo como argumento de la normalización por frecuencias marginales; la materialidad viene del límite que H05 ya declara (las comunidades «dependen de normalización, filtro y semilla»).
- **Qué gana el estudiante:** distinguir co-ocurrir mucho de estar asociado
  más de lo esperado. Hoy la matriz de palabras clave usa conteos brutos de
  documentos compartidos (H04) y filtra términos con diagonal ≥ 10, de modo
  que los pares entre términos muy frecuentes dominan la red y las
  comunidades Louvain (H05) por pura frecuencia marginal. Al calcular, para
  los mismos términos filtrados, lift = c_ij · N / (c_ii · c_jj)
  (proporcional a la fuerza de asociación usada en análisis de co-word),
  contrastar el top de pares por conteo con el top por lift y detectar
  comunidades sobre ambas matrices, el estudiante ve qué parte de la
  estructura temática es frecuencia y qué parte es asociación, y obtiene un
  criterio para leer el mapa del campo. Ningún taller del curso normaliza
  co-ocurrencias.
- **Anclas actuales:** H04 (matriz ítem × ítem; diagonal = documentos con el
  ítem; filtro por diagonal ≥ 10, 32 términos), H05 (Louvain `seed=0`;
  `keywords_clusters.txt` con seis grupos), H07 (funciones reutilizadas en
  pasos persistentes), H08 (pruebas); superficies S04 (co-ocurrencia,
  filtro y comunidades: `s17_*`, `s18_*`, `s19_*`), S06 (orquestación en
  `main.py`) y S07 (pruebas, conjunto exacto de archivos).
- **Alternativas menores descartadas:** declarar en el texto que los
  conteos brutos favorecen términos frecuentes ya está implícito en el
  límite de H05 y no permite verificarlo. Sustituir la matriz bruta por la
  normalizada borraría la evidencia del contraste y cambiaría productos
  que las pruebas exigen; la propuesta conserva ambas. Aplicarlo también a
  países ampliaría el cambio sin aportar un contraste distinto.
- **Contrato de no regresión:** se conservan H01–H08, el corpus, la
  normalización de palabras clave, el filtro por diagonal ≥ 10,
  `keywords_cooc_matrix.csv` y `keywords_clusters.txt` con su contenido
  actual, las redes HTML y todo el análisis de países. La variante
  normalizada se añade en un paso nuevo, sobre los mismos términos y con la
  misma semilla. La única prueba existente que cambia es la del conjunto
  exacto de archivos, que se amplía sin quitar ninguno.
- **Interacciones:** independiente de T01; el N de documentos que T01 deja
  verificado es el denominador de este lift. Ambas amplían la misma prueba
  del conjunto de archivos: ejecutar después de T01. Capacidad: P123 ya
  recorre países, fuentes, autores y palabras clave en veinte pasos sin
  notebook que haga visibles las decisiones; T02 añade un paso y una
  comparación conceptual. Si el tiempo de taller no alcanza, conviene
  decidir en la discusión que T02 sea la sección final, que un grupo lento
  puede omitir sin perder los productos actuales. Como no hay notebook, la
  lectura del contraste se persiste en un archivo de texto en
  `submission/`; crear un notebook queda fuera de esta propuesta.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que (1)
  el lift de cada par de los términos filtrados se calcula desde
  `keywords_cooc_matrix.csv` y N declarado; (2) una tabla contrasta el
  ranking de pares por conteo y por lift, con el conteo junto a cada lift;
  (3) las comunidades se detectan sobre la matriz normalizada con la misma
  semilla y se comparan término a término con las de conteo bruto; y (4)
  una lectura de 4–6 líneas dice qué cambia en la estructura temática y
  advierte que lift con pocos documentos compartidos es inestable. Debe
  estar respaldado por `keywords_pairs_association.csv`,
  `keywords_clusters_normalized.txt`, `keywords_clusters_comparison.csv`,
  la lectura en `submission/` y pruebas que recomputan el lift. H04 y H05
  siguen presentes con sus productos sin cambios.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P123_scopus/

0. Inspecciona primero professor/main.py, professor/s14_*.py a
   professor/s20_*.py, submission/keywords_cooc_matrix.csv,
   submission/keywords_clusters.txt y tests/test_activity.py. Verifica que
   la matriz es simétrica, que su diagonal es el número de documentos con
   cada término y que fuera de la diagonal hay documentos compartidos. Si
   la implementación no coincide con
   design/courses/descriptiva/P123_activity.md, si la matriz ya está
   normalizada o si no es simétrica, detente e informa sin modificar nada.
1. No cambies s01–s20 ni sus productos (en particular
   keywords_cooc_matrix.csv, keywords_clusters.txt y las redes HTML), ni el
   análisis de países.
2. Crea un paso nuevo (por ejemplo, s21_keywords_association.py) invocado
   desde main.py después del último paso de palabras clave, sin renumerar
   los existentes, que reutilice las funciones de comunidades de H05/H07:
   a. Define N = documentos del corpus con al menos una palabra clave
      después de la limpieza de s15 (decláralo en el código y en la
      lectura). Si T01 está implementada, verifica que N no supera
      records_loaded de corpus_boundary.json.
   b. Para cada par i < j de términos de la matriz filtrada, con c_ij > 0:
      lift = c_ij * N / (c_ii * c_jj).
   c. Ordena los pares por c_ij y por lift y registra ambos rankings.
   d. Construye el grafo con pesos = lift sólo para pares con lift > 1
      (asociación mayor que la esperada por azar), detecta comunidades con
      Louvain y seed=0, y compáralas término a término con
      keywords_clusters.txt. Si sklearn está en el requirements.txt raíz,
      reporta sklearn.metrics.adjusted_rand_score entre ambas particiones;
      no añadas dependencias.
3. Persiste en submission/:
   - keywords_pairs_association.csv con columnas keyword_a, keyword_b,
     cooccurrences, docs_a, docs_b, n_documents, lift, rank_by_count,
     rank_by_lift;
   - keywords_clusters_normalized.txt con el mismo formato que
     keywords_clusters.txt;
   - keywords_clusters_comparison.csv con columnas keyword, cluster_raw,
     cluster_normalized;
   - keywords_association_notes.md con 4–6 líneas: qué pares suben o
     bajan al normalizar, qué comunidades se conservan o se separan, que
     lift con pocos documentos compartidos es inestable (cita los pares de
     lift alto con cooccurrences ≤ 2) y que la co-ocurrencia describe
     asociación en el corpus, no causalidad ni madurez tecnológica.
4. En tests/test_activity.py amplía la prueba del conjunto exacto de
   archivos con los cuatro archivos nuevos (sin quitar los actuales) y
   añade pruebas que: recompongan lift desde keywords_cooc_matrix.csv y
   n_documents; verifiquen que todos los términos de
   keywords_clusters.txt aparecen en keywords_clusters_comparison.csv; y
   comprueben que keywords_cooc_matrix.csv sigue siendo simétrica. No
   elimines pruebas existentes.
5. Ejecuta professor/main.py completo y las pruebas sin errores.
6. No modifiques otras actividades, traceability.yaml ni design/.
```
