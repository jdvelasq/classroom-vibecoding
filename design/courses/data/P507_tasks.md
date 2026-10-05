# P507 — Propuestas de mejora

**Línea base:** `P507_activity.md` (entrada S02 más reciente: `S02.P507.02`).

## T01 — Hacer explícito el criterio de empate (ROW_NUMBER vs RANK/DENSE_RANK) y mostrar la sensibilidad del ranking a excluir los términos de búsqueda y unificar variantes

- **Estado:** pendiente de discusión
- **Tipo:** método/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 71, 75 y 76 — en DM-Proximity Measurement, «Use of scores and rankings; desirable characteristics of scores and ranking regimes» y la disposición «An accurate, yet inventive, approach to the use of scores and metrics recognizing that typically many approaches exist»; en DG-Working with Various Types of Data, el procesamiento de texto incluye «word-count, TF-IDF, n-grams, […] stop word filtering, stemming»: un ranking es un régimen con propiedades que se eligen y declaran, y un conteo sobre texto depende de decisiones de representación (Claude, 2026-10-05). Fuente *authoritative*: respalda una expectativa general; la mención de rankings está en un área de medidas de proximidad, de modo que su peso aquí es de principio, no de procedimiento.
- **Qué gana el estudiante:** aprende que un «top 10» sobre palabras clave de
  autor no es una jerarquía temática por sí mismo: depende del régimen de
  empates y de cómo se representa el texto, y eso debe declararse y medirse.
  Hoy H02 sólo se observa en el CSV: en 2020 «proptech», término de la propia
  cadena de búsqueda, encabeza con 7 documentos y los puestos 2–5 empatan con
  2, de modo que `ROW_NUMBER` con desempate por `keyword` decide puestos y,
  si hay empate en el corte, también qué términos entran, por orden
  alfabético. El notebook no examina empates, términos de búsqueda ni
  variantes, y S02 registra `data.C03` sin evidencia. Con el cambio, el
  estudiante (a) declara el régimen y ve cuántos términos entrarían con
  `RANK`/`DENSE_RANK` en cada año; y (b) mide cuántas posiciones del top 10
  cambian al excluir los términos de `search_string.txt` y al unificar
  variantes mínimas (singular/plural). Convierte una limitación descrita en
  evidencia producida, sin cambiar caso ni producto (nivel 2). No duplica
  P503 H03, que normaliza con `casefold` pero no evalúa el efecto sobre una
  respuesta.
- **Anclas actuales:** H01 (ventana por año), H02 (palabras clave de autor y
  empates; caso y datos); superficies S01 (representación de palabras clave,
  tablas creadas en P503), S02 (consulta), S03 (producto), S04 (pruebas);
  dependencias «Recibe de P503–P506» (normalización `casefold`,
  `search_string.txt`, filtro desde 2020, CTE).
- **Alternativas menores descartadas:** describir la limitación en markdown ya
  lo hace S02 y no permite al estudiante comprobarla. Cambiar directamente a
  `RANK` sin contraste ocultaría la decisión en vez de enseñarla. Unificar
  sinónimos con un tesauro amplio o *stemming* completo excede el taller y
  desplazaría su identidad hacia procesamiento de texto.
- **Contrato de no regresión:** se conservan H01–H02, la consulta actual con
  `ROW_NUMBER` y `top_keywords_by_year.csv` con su contenido y esquema
  (régimen principal salvo decisión explícita del profesor), `questions.json`,
  `data/scopus_proptech.db` sin modificaciones persistentes,
  `data/search_string.txt` y la prueba existente. El contraste y la
  sensibilidad se añaden como secciones y artefactos nuevos; ninguna sección
  existente se sustituye.
- **Identidad del taller:** S02 marca riesgo moderado de que P507 se lea como
  lección de funciones de ventana. El contraste `ROW_NUMBER`/`RANK`/
  `DENSE_RANK` debe quedar subordinado a la lectura del producto (qué dice
  el puesto y qué términos quedan fuera por un empate), no presentarse como
  catálogo de funciones; no se añaden otras ventanas (`LAG`, `NTILE`, etc.).
  La parte (b) es la que conecta el ranking con la pregunta temática.
- **Interacciones:** sin otras `Txx` en P507. No toca P503: la unificación de
  variantes se hace en una vista o tabla temporal de P507, no en las tablas
  construidas en P503. Capacidad: P507 tiene dos highlights y un notebook de
  una consulta; la propuesta añade dos secciones cortas. Si el tiempo de
  taller es limitado, la parte (b) puede quedar como sección final que un
  grupo lento complete después; (a) es la mínima.
- **Criterio de aceptación:** S05 encuentra (1) una celda markdown que declara
  el régimen de empates del producto y su consecuencia, y una tabla que, por
  año, compara `ROW_NUMBER`, `RANK` y `DENSE_RANK` y cuenta los términos
  empatados en el corte del puesto 10; (2) un ranking recalculado sin los
  términos de búsqueda y otro, además, con variantes singular/plural
  unificadas por documento distinto, con el número de términos del top 10
  que cambian por año frente al producto; (3) los CSV del paso 4 y del paso 5
  en `submission/` y pruebas que los verifiquen. H01–H02 siguen presentes;
  H02 pasa a apoyarse en evidencia del notebook, no sólo en el CSV.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P507_scopus_sql_analitico/

0. Inspecciona primero professor/notebook.ipynb, data/scopus_proptech.db
   (tablas document_keywords, keywords, documents), data/search_string.txt,
   submission/ y tests/test_activity.py. Si la consulta no usa ROW_NUMBER
   particionado por año con desempate por keyword, o la implementación no
   coincide con design/courses/data/P507_activity.md, detente e informa sin
   modificar nada.
1. No cambies la consulta existente, top_keywords_by_year.csv,
   questions.json, search_string.txt ni las tablas persistentes de
   scopus_proptech.db. Trabaja con CTE, vistas o tablas TEMP.
2. RÉGIMEN DE EMPATES: añade una sección «Empates y régimen del ranking».
   Sobre la misma CTE keyword_years, calcula en una sola consulta
   ROW_NUMBER(), RANK() y DENSE_RANK() con PARTITION BY publication_year
   ORDER BY document_count DESC (ROW_NUMBER conserva el desempate por
   keyword). Para cada año, reporta: document_count del puesto 10, número de
   términos con ese conteo y cuántos términos tendrían RANK <= 10 frente a
   los 10 de ROW_NUMBER. Escribe en markdown, en 3–5 líneas, qué régimen usa
   el producto, qué significa el puesto dentro de un empate y qué términos
   quedan fuera por orden alfabético. No cambies el régimen del producto
   salvo que el profesor lo haya decidido en la discusión de esta T01
   (registrado en P507_log.md).
3. SENSIBILIDAD: añade una sección «Sensibilidad del ranking a la
   representación».
   a. Extrae de search_string.txt los términos de búsqueda, aplícales
      strip() y casefold() como en P503, e imprime la lista. Si la cadena no
      permite extraerlos sin ambigüedad, detente y pide la lista al
      profesor.
   b. Variante sin_terminos_busqueda: recalcula el top 10 por año
      excluyendo esos términos (mismo régimen que el producto).
   c. Variante unificada: además, crea un mapeo mínimo singular/plural entre
      palabras clave presentes en la base (p. ej. una forma terminada en «s»
      cuya forma sin «s» también existe) e imprime el mapeo completo para
      revisión. Cuenta documentos DISTINTOS por término unificado (un
      documento con ambas formas cuenta una vez). No uses stemming general
      ni sinónimos.
   d. Para cada año, cuenta cuántos términos del top 10 del producto salen
      del top 10 en cada variante.
   e. Escribe en markdown, en 3–5 líneas, qué parte del ranking es robusta y
      qué parte depende de la representación, y por qué los términos de
      búsqueda dominan el conteo.
4. Persiste submission/rank_regime_comparison.csv con columnas
   publication_year, keyword, document_count, row_number, rank, dense_rank
   (al menos todos los términos con rank <= 10).
5. Persiste submission/ranking_sensitivity.csv con columnas
   publication_year, variant (baseline, sin_terminos_busqueda, unificada),
   keyword, document_count, rank_in_year, y
   submission/keyword_variant_map.csv con columnas variant_keyword,
   unified_keyword.
6. Añade a tests/ pruebas que verifiquen: columnas de los tres CSV; que en
   rank_regime_comparison.csv rank <= row_number y dense_rank <= rank; que
   las tres variantes existen para cada año del producto; y que ningún
   término de búsqueda aparece en las variantes sin_terminos_busqueda y
   unificada. No elimines la prueba existente.
7. Ejecuta el notebook completo y las pruebas sin errores.
8. No modifiques otras actividades (en particular P503), traceability.yaml
   ni design/.
```
