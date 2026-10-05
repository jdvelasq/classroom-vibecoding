# P518 — Propuestas de mejora

**Línea base:** `P518_activity.md` (entrada S02 más reciente: `S02.P518.02`).

## T01 — Plantear la pregunta analítica que resuelve el procesamiento y mostrar cómo lo resuelve

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - Decisión del profesor en la entrevista del 2026-10-05, registrada en `design/courses/data/P500_log.md` (`Nota.P500.02`) (Claude, 2026-10-05). No proviene de un benchmark.
- **Qué gana el estudiante:** ver la ingestión desde una API como se hace
  profesionalmente: se obtiene y aplana una respuesta para responder algo, y
  la respuesta sale de la tabla que la ingestión dejó. Hoy P518 no declara
  pregunta (S02: «Pregunta, usuario o decisión: no evidenciados»; S05 «Sin
  `questions.json` ni uso analítico») y la auditoría sigue no resuelta porque
  «falta finalidad analítica (sin pregunta ni consumidor; vacío C01)»
  (S02.P518.02). Con esta T01, el estudiante enuncia la pregunta antes de
  procesar, la responde desde `github_issues.parquet`, persiste la respuesta
  ligada a la pregunta y escribe su lectura y su límite. La pregunta usa
  justamente el elemento que S02 identifica como único vínculo con una
  unidad de análisis: la marca `is_pull_request` (H02), que impide mezclar
  dos entidades al contar.
  **Pregunta sugerida (sólo sugerencia; requiere la redacción aprobada por
  el profesor):** «En la página de issues capturada de `pandas-dev/pandas`,
  ¿cuántos registros son issues y cuántos pull requests, y cuántos de cada
  uno siguen abiertos?». Se apoya en lo que S02 describe: una página
  congelada de 20 objetos proyectada a ocho campos, con `state` e
  `is_pull_request`. No se propone usuario ni decisión más allá de esta
  sugerencia.
  **Límite explícito:** esta T01 cierra el límite «sin pregunta analítica»
  que registró S02 sólo una vez ejecutada y verificada por S05; aprobarla no
  lo cierra.
- **Anclas actuales:** H02 (proyección y marca de pull requests, que define
  la unidad que se cuenta), H03 (llave única y reporte, con el que la
  respuesta se concilia) y H01 (falla y reintento, sin cambios); superficies
  S03 (proyección), S05 (producto «sin `questions.json` ni uso analítico»),
  S06 (prueba que «acepta cualquier archivo») y S07 (interfaz del
  estudiante, que no se toca). Dependencia «Recibe de P513» (forma del
  reporte), sin cambios.
- **Alternativas menores descartadas:** declarar la pregunta sólo en el
  docstring hace visible una intención, pero no muestra cómo la proyección
  la resuelve ni deja evidencia verificable. Contar sobre el JSON original
  en lugar de la tabla aplanada evitaría la representación que el taller
  enseña.
- **Contrato de no regresión:** se conservan H01–H03, `request_page`, el
  bucle de reintentos y su `RuntimeError`, la proyección a ocho campos, el
  `assert` de unicidad, `github_issues.parquet` y `api_ingestion_report.csv`
  con su esquema y valores, y la prueba existente. Se añaden la pregunta al
  inicio de `professor/main.py`, `submission/questions.json`,
  `submission/analysis_answer.csv`, una lectura breve con su límite y una
  prueba. No cambian los datos ni las herramientas; los defectos registrados
  por S02 (`pages_requested` y `status` constantes, procedencia sin
  manifiesto, fechas como texto) quedan fuera de esta T01.
- **Interacciones:** única propuesta de P518. Sigue el mismo patrón que
  P513 T02 (pregunta, respuesta desde lo procesado, lectura con límite), sin
  compartir archivos ni código.
- **Criterio de aceptación:** S05 encuentra (1) al inicio de
  `professor/main.py` la pregunta con la redacción aprobada por el profesor,
  idéntica a la registrada en `P518_log.md`; (2) `submission/questions.json`
  que liga esa pregunta con `analysis_answer.csv`, con la misma estructura
  de claves que el `questions.json` de P500 más `reading` y `limit`; (3)
  `analysis_answer.csv` calculado a partir de la tabla aplanada (el mismo
  DataFrame que se escribe en `github_issues.parquet`), con columnas
  explícitas; (4) una lectura de 2–4 líneas con su límite; y (5) una prueba
  que recalcula los conteos desde `github_issues.parquet` y los compara con
  la respuesta, y concilia el total con `records_retrieved`. Un highlight
  nuevo (H04) recoge la pregunta y su respuesta; H01–H03 siguen presentes.
  Sólo entonces S02 puede revisar el límite «sin pregunta analítica» y la
  auditoría 5 de P518; la revisión de `data.C01` en `traceability.yaml`
  queda para S05.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P518_github_api/

0. Inspecciona primero professor/main.py, src/main.py,
   data/github_issues_page_1.json, submission/ y tests/, y (sólo lectura)
   implementation/data/P500_superstore_metricas/submission/questions.json
   para tomar su estructura de claves. Si la implementación no coincide con
   design/courses/data/P518_activity.md, detente e informa sin modificar
   nada. Confirma que design/courses/data/P500_log.md contiene Nota.P500.02;
   si no, detente e informa. Lee github_issues.parquet y registra el número
   de filas y la distribución de is_pull_request × state; si is_pull_request
   o state no existen, detente e informa.
1. PREGUNTA: no inventes la pregunta, el usuario ni la decisión. Usa la
   redacción que el profesor haya aprobado en la discusión de esta T01
   (registrada en P518_log.md). La pregunta sugerida en P518_tasks.md no es
   una aprobación. Si no existe redacción aprobada, detente y pídela.
   Escríbela al inicio de professor/main.py (docstring del módulo, junto al
   objetivo operativo actual que se conserva, o una constante QUESTION usada
   al escribir questions.json).
2. No cambies request_page, el bucle de reintentos, la proyección, el
   assert de unicidad ni los dos archivos actuales de submission/.
3. RESPUESTA DESDE LO PROCESADO: con el DataFrame proyectado (el que se
   escribe en github_issues.parquet), calcula una fila por combinación de
   record_type (issue si is_pull_request es falso; pull_request si es
   verdadero) y state, con records y share_of_page (records / total de
   filas). Ajusta las columnas a la redacción aprobada si difiere, sin
   añadir datos externos ni campos que la proyección no conserve.
4. Persiste submission/analysis_answer.csv con columnas record_type, state,
   records, share_of_page y submission/questions.json con la estructura de
   claves de P500 (pregunta y archivo de respuesta = analysis_answer.csv)
   más las claves reading y limit.
5. LECTURA: escribe en reading 2–4 líneas que respondan la pregunta con las
   cifras de analysis_answer.csv, y en limit el límite: es una sola página
   congelada de 20 registros, sin paginación, criterio de muestreo ni fecha
   de captura documentados; describe esa página, no el repositorio. No
   inventes la fecha de captura ni parámetros de la consulta. Imprime la
   tabla de respuesta al final como evidencia visible.
6. Añade a tests/ pruebas que verifiquen: questions.json existe, contiene la
   pregunta no vacía y apunta a analysis_answer.csv; analysis_answer.csv
   tiene las columnas del paso 4; los conteos por record_type y state
   coinciden con los recalculados desde github_issues.parquet; la suma de
   records es igual al número de filas del Parquet y a records_retrieved de
   api_ingestion_report.csv; share_of_page suma 1 (con tolerancia). Las
   pruebas deben ser independientes de la profundidad del taller en la
   distribución. No elimines la prueba existente.
7. Ejecuta professor/main.py y las pruebas de la actividad sin errores.
8. No modifiques datos ni herramientas, no crees notebooks (S07 fuera de
   esta T01) y no toques otras actividades (P513 incluida),
   traceability.yaml ni design/.
```
