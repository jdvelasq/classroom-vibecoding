# P123 — Propuestas de mejora

**Línea base:** `P123_activity.md` (entrada S02 más reciente: `S02.P123.01`).

## T01 — Completar la frontera del corpus: fecha de extracción, número de registros y último año posiblemente parcial

- **Estado:** pendiente de discusión
- **Tipo:** caso/datos + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 40, 45 y 51 — «Students also need to consider the provenance of the data used» (p. 40); «Data provenance» encabeza los conceptos de gestión y curaduría de datos importantes para todos los estudiantes (p. 45); entre las responsabilidades éticas, «the responsibility to ensure that results produced by the analyst are reproducible» (p. 51) (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general de procedencia y reproducibilidad.
  - `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` p. 6 — el entregable «Data Collection Report» debe «describe procedures followed to collect the data, […] data format, dataset size, how the data is stored, characteristics of the data» (Claude, 2026-10-04). Fuente *institutional*: ilustra cómo un programa exige declarar procedimiento y tamaño de la recolección.
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
