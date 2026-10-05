# P523 — Propuestas de mejora

**Línea base:** `P523_activity.md` (entrada S02 más reciente: `S02.P523.02`).

## T01 — Corregir la medición de la agregación local: pares enviados al shuffle por bloque de entrada, con y sin combiner, y carga de la clave frente a la de su partición

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` p. 59 — BDS-Parallel Programming, T2: «Parallel algorithms and how they best fit particular hardware architectures; load balancing issues», «Typical parallel programming paradigm such as MapReduce» y la destreza «Evaluate a parallel algorithm’s load-balance on a variety of hardware architectures»; BDS-Techniques, T2: «Illustrate the role of hashing in dealing with Big Data» (Claude, 2026-10-05). Fuente *authoritative*: expectativa general; la materialidad la sostiene el defecto de H03 que registró S02.
  - `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` p. 29 — esquema «Algoritmo MapReduce»: DATOS → MAP («<Clave, Valor>», un par «<A, 1>» por aparición) → SHUFFLE & SORT → REDUCE («<A, 3>»), sin agregación local, de modo que cada par emitido por el map pasa al shuffle (Claude, 2026-10-05). Fuente *literature-derived*: contexto; fija la línea de comparación «sin combiner».
- **Qué gana el estudiante:** medir lo que realmente ahorra agregar antes
  del shuffle, en lugar de una cifra que no lo mide. Hoy
  `pairs_after_local_combiner = 5` coincide con el número de tipos
  distintos, es decir, con la salida final del reduce: los parciales se
  indexan por partición de destino y no por bloque de entrada, así que no
  son los pares que un combiner del lado del mapper enviaría al shuffle.
  Además, `hot_key_load = max(skewed)` es la carga de una partición (que
  puede contener dos tipos), no la de una clave (S02.P523.01), y
  `assert combined_pairs < len(rows)` es trivial. Con la corrección, los
  eventos se reparten en bloques de entrada contiguos, la agregación local
  se hace por bloque y se persisten los pares enviados sin combiner (uno
  por evento), los pares enviados con combiner (suma, por bloque, de los
  tipos presentes en él), los pares que recibe la partición más cargada en
  cada caso y la carga de la clave más frecuente frente a la de su
  partición. El estudiante distingue lo que la agregación local cambia (el
  número de pares enviados, también hacia la partición caliente, porque la
  suma es asociativa) de lo que no cambia (qué partición recibe cada clave,
  fijado por la clave y el particionador de H01–H02). **Límite que no se
  resuelve:** esta T01 no resuelve el límite que S02 mantiene para P523,
  «sin pregunta analítica» (ni producto analítico; el sesgo es de carga
  computacional); corrige un defecto de lo que el taller enseña. Lo que la
  pone en alcance es la aclaración del profesor (2026-10-05): el curso está
  entre la ingeniería de datos y la analítica, y el procesamiento
  clave–valor y distribuido introductorio pertenece a él como puente.
- **Anclas actuales:** H03 (agregación local «con un defecto de modelado»),
  que se corrige; H01 (sesgo por clave) y H02 (particionador MD5
  determinista), que se conservan. Superficies S03 (`partials` indexado por
  partición de destino), S04 (`shuffle_comparison.csv`) y S05 (prueba de
  sólo existencia). Dependencias «Recibe de P522» (noción de partición,
  práctica) y «Recibe de P519» (operadores copiados), sin cambios.
- **Alternativas menores descartadas:** aclarar en markdown que la cifra 5
  es la salida del reduce hace visible el defecto pero deja al taller sin
  ninguna medición del efecto del combiner. Reutilizar la reducción local de
  P522 H02 no cubre la necesidad: P522 no cuenta pares. Usar los operadores
  copiados de P519 en lugar de `defaultdict` no cambia la medición y queda
  fuera de esta T01.
- **Contrato de no regresión:** se conservan H01, H02, el dataset, la
  función `partition` y `partition_loads.csv` con su esquema y valores. H03
  se sustituye por una versión que mide pares por bloque de entrada; la
  evidencia nueva es al menos equivalente porque conserva la comparación
  «sin / con agregación local» y la corrige. `shuffle_comparison.csv` se
  sustituye por una fila con columnas explícitas (ninguna actividad
  posterior lo usa: «Habilita para Pyyy: no evidenciada»). La aserción
  trivial se sustituye por la conciliación de la suma de los parciales con
  el total de eventos. La prueba existente se mantiene.
- **Interacciones:** ninguna dentro de P523 (única propuesta). Es
  independiente de P522 T01: puede tomar como práctica la división en
  bloques contiguos de P522, sin compartir archivos ni código.
- **Criterio de aceptación:** S05 encuentra en `professor/notebook.ipynb`
  una agregación local por bloque de entrada, con una vista pequeña de los
  parciales de un bloque; un `shuffle_comparison.csv` que separa pares sin y
  con combiner, pares recibidos por la partición más cargada en cada caso y
  carga de la clave más frecuente frente a la de su partición; una
  conciliación de los parciales con el total de eventos; y pruebas que
  verifican esas relaciones. H03 queda reescrito en esos términos; H01 y
  H02 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P523_mapreduce_particionamiento/

0. Inspecciona primero professor/notebook.ipynb, notebooks/notebook.ipynb,
   data/truck_events.csv.gz, submission/ y tests/. Si la implementación no
   coincide con design/courses/data/P523_activity.md (en particular, si
   shuffle_comparison.csv no registra 17075, 5 y 17041, o si partials no se
   indexa por la partición de destino), detente e informa sin modificar
   nada. Registra los nombres actuales de las columnas de
   shuffle_comparison.csv y el número de tipos distintos de eventType.
1. No cambies partition, el cálculo de cargas por eventKey y por eventType
   ni partition_loads.csv.
2. BLOQUES DE ENTRADA: divide las filas, en su orden, en un número fijo y
   declarado de bloques contiguos (por ejemplo 8). Muestra cuántas filas
   tiene cada bloque.
3. SIN COMBINER: cada evento emite un par (eventType, 1). Calcula
   pairs_without_combiner (= número de eventos) y los pares que recibe cada
   partición de destino según partition(eventType).
4. CON COMBINER: dentro de cada bloque, suma por eventType; cada bloque
   emite un par por tipo presente en él. Calcula pairs_with_combiner (suma
   de los tipos presentes por bloque) y los pares que recibe cada partición
   de destino. Muestra los parciales de un bloque como evidencia visual.
5. CONCILIACIÓN: sustituye assert combined_pairs < len(rows) por aserciones
   de que la suma de los valores parciales de todos los bloques es igual al
   número de eventos, y de que la reducción final de los parciales es igual
   al conteo directo por eventType.
6. CARGA DE CLAVE Y DE PARTICIÓN: identifica el eventType más frecuente, su
   carga (eventos) y la partición a la que lo asigna partition; reporta la
   carga total de esa partición y cuántos tipos contiene.
7. Explica en markdown, en 3–5 líneas: qué mide cada cifra, por qué la
   cifra anterior (5) era la salida del reduce, que el combiner reduce los
   pares enviados porque la suma es asociativa, y que no cambia qué
   partición recibe cada clave.
8. Sustituye submission/shuffle_comparison.csv por una fila con columnas
   events, input_blocks, pairs_without_combiner, pairs_with_combiner,
   reduce_output_keys, hottest_partition, hottest_partition_pairs_without_combiner,
   hottest_partition_pairs_with_combiner, hottest_key, hottest_key_load,
   hottest_key_partition_load, hottest_key_partition_keys.
9. Añade a tests/ pruebas que verifiquen: las columnas del paso 8;
   events = pairs_without_combiner; reduce_output_keys <=
   pairs_with_combiner <= pairs_without_combiner; pairs_with_combiner <=
   input_blocks * reduce_output_keys; hottest_key_load <=
   hottest_key_partition_load. Las pruebas deben ser independientes de la
   profundidad del taller en la distribución. No elimines la prueba
   existente.
10. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
11. No añadas pregunta analítica, no cambies el dataset ni el número de
    particiones, no rellenes notebooks/notebook.ipynb (S06 fuera de esta
    T01) y no modifiques otras actividades (P522), traceability.yaml ni
    design/.
```

## T02 — Plantear la pregunta analítica que resuelve el procesamiento y mostrar cómo lo resuelve

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - Decisión del profesor en la entrevista del 2026-10-05, registrada en `design/courses/data/P500_log.md` (`Nota.P500.02`) (Claude, 2026-10-05). No proviene de un benchmark.
- **Qué gana el estudiante:** ver el particionamiento por clave como se usa
  profesionalmente: los eventos se reparten por clave para responder algo,
  y la respuesta sale de la salida reducida de esas particiones, conciliada
  con las cargas que el taller ya persiste. Hoy P523 declara sólo un
  problema técnico («Mostrar cómo claves reales de telemetría pueden
  concentrar trabajo…»; S02: «No hay pregunta analítica»; «Pregunta,
  usuario o decisión: no evidenciados») y S02 registra que el taller «no
  dice nada sobre la operación de los camiones; no se reporta qué tipo de
  evento domina ni cuántos tipos hay, salvo lo deducible de los cinco pares
  finales». La auditoría sigue no resuelta por «la ausencia de pregunta y
  producto analítico» (S02.P523.02). Con esta T02, el estudiante enuncia la
  pregunta antes de procesar, la responde con la reducción por `eventType`
  de los parciales de las particiones, persiste la respuesta ligada a la
  pregunta y escribe su lectura y su límite. El sesgo de carga de H01 deja
  de ser sólo un efecto computacional: es la otra cara de la respuesta (el
  tipo que domina los eventos es el que concentra la partición).
  **Pregunta sugerida (sólo sugerencia; requiere la redacción aprobada por
  el profesor):** «En el registro de eventos de telemetría de camiones
  disponible, ¿qué tipos de evento (`eventType`) aparecen, cuántas veces
  ocurre cada uno y qué parte del total representa el más frecuente?». Se
  apoya en lo que S02 describe: 17075 filas, «cada fila representa un
  evento de telemetría de camiones», `eventType` como una de las dos claves
  de partición (con `eventKey`), cuatro particiones por MD5 y una carga por
  `eventType` de 17041, 11, 7 y 16. No usa `eventKey`, cuyo significado no
  está documentado. No se propone usuario ni decisión más allá de esta
  sugerencia.
  **Límite explícito:** esta T02 cierra el límite «sin pregunta analítica»
  que registró S02 sólo una vez ejecutada y verificada por S05; aprobarla no
  lo cierra. No cambia la escalación del mapeo a `data.C03` que S02
  conserva (el sesgo que el taller muestra sigue siendo de carga).
- **Anclas actuales:** H01 (cargas por `eventType`, con las que la
  respuesta se concilia), H02 (particionador determinista, que fija la
  partición de cada tipo) y H03 (agregación local, de cuya reducción final
  sale la respuesta, no de su cifra defectuosa); superficies S02
  (particionador y claves), S03 (agregación local), S04 (producto «sin
  `questions.json`»), S05 (prueba de sólo existencia) y S06 (interfaz del
  estudiante, que no se toca). Dependencias «Recibe de P519» y «Recibe de
  P522», sin cambios.
- **Alternativas menores descartadas:** escribir la pregunta sólo en el
  markdown del notebook hace visible una intención, pero no muestra cómo el
  particionamiento y la reducción la resuelven ni deja evidencia
  verificable. Responderla con `value_counts` sobre el CSV evitaría el
  procesamiento que el taller enseña; ese conteo sirve sólo como
  comprobación. Leer el número de tipos de `pairs_after_local_combiner = 5`
  o la frecuencia del tipo dominante de `hot_key_load` reutilizaría las
  cifras que S02 registró como defectuosas.
- **Contrato de no regresión:** se conservan H01–H03, el dataset, la
  función `partition`, el número de particiones, `partition_loads.csv` con
  su esquema y valores y `shuffle_comparison.csv` (en su forma actual o en
  la de T01), y la prueba existente (y las que añada T01). Se añaden la
  pregunta en la primera celda de `professor/notebook.ipynb`,
  `submission/questions.json`, `submission/analysis_answer.csv`, una
  lectura breve con su límite y una prueba. No cambian los datos ni las
  herramientas; la procedencia de los eventos y el significado de
  `eventKey` quedan fuera de esta T02.
- **Interacciones:** con T01. T01 corrige la medición de la agregación
  local (pares por bloque de entrada y carga de la clave frente a la de su
  partición); T02 no depende de esa medición y su respuesta no debe
  depender de la métrica defectuosa: no toma el número de tipos de
  `pairs_after_local_combiner` ni la frecuencia del tipo dominante de
  `hot_key_load`, sino de la reducción por `eventType`, conciliada con el
  conteo directo. Puede ejecutarse antes o después de T01; es preferible
  después, porque entonces la respuesta sale de la reducción de los
  parciales por bloque que T01 ya concilia (su paso 5), y `hottest_key` y
  `hottest_key_load` de T01 deben coincidir con la primera fila de la
  respuesta. Si T02 va antes, la respuesta sale de la reducción de los
  parciales actuales (que, aunque mal nombrados como combiner, suman bien
  por tipo), y T01 no debe cambiarla. El paso 11 de T01 («No añadas
  pregunta analítica») limita a T01 por sí misma; si se aprueban ambas, la
  pregunta la añade T02. Capacidad: es un cálculo pequeño sobre parciales
  que ya existen.
- **Criterio de aceptación:** S05 encuentra (1) en la primera celda de
  `professor/notebook.ipynb` la pregunta con la redacción aprobada por el
  profesor, idéntica a la registrada en `P523_log.md`; (2)
  `submission/questions.json` que liga esa pregunta con
  `analysis_answer.csv`, con la misma estructura de claves que el
  `questions.json` de P500 más `reading` y `limit`; (3)
  `analysis_answer.csv` calculado a partir de la reducción por `eventType`
  de los parciales de las particiones, con una fila por tipo y columnas
  explícitas, incluida la partición que asigna `partition`; (4) una lectura
  de 2–4 líneas con su límite; y (5) una prueba que recalcula el conteo por
  `eventType` desde `data/truck_events.csv.gz`, lo compara con la
  respuesta y concilia, por partición, la suma de los tipos asignados con
  la carga por `eventType` de `partition_loads.csv`. Un highlight nuevo
  (H04) recoge la pregunta y su respuesta; H01–H03 siguen presentes. Sólo
  entonces S02 puede revisar el límite «sin pregunta analítica» y la
  auditoría 5 de P523; la revisión de `data.C01` en `traceability.yaml`
  queda para S05.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P523_mapreduce_particionamiento/

0. Inspecciona primero professor/notebook.ipynb, notebooks/notebook.ipynb,
   data/truck_events.csv.gz, submission/ y tests/, y (sólo lectura)
   implementation/data/P500_superstore_metricas/submission/questions.json
   para tomar su estructura de claves. Si la implementación no coincide con
   design/courses/data/P523_activity.md, detente e informa sin modificar
   nada. Confirma que design/courses/data/P500_log.md contiene Nota.P500.02;
   si no, detente e informa. Registra el número de filas, los valores
   distintos de eventType y la forma actual de shuffle_comparison.csv
   (actual o la de T01) para saber de qué parciales sale la reducción.
1. PREGUNTA: no inventes la pregunta, el usuario ni la decisión. Usa la
   redacción que el profesor haya aprobado en la discusión de esta T02
   (registrada en P523_log.md). La pregunta sugerida en P523_tasks.md no es
   una aprobación. Si no existe redacción aprobada, detente y pídela.
   Escríbela en la primera celda markdown de professor/notebook.ipynb, junto
   al problema técnico actual que se conserva, y úsala al escribir
   questions.json.
2. No cambies partition, el número de particiones, el cálculo de cargas,
   partition_loads.csv, shuffle_comparison.csv ni, si T01 se ejecutó, sus
   aserciones de conciliación.
3. RESPUESTA DESDE LO PROCESADO: reduce por eventType los parciales de las
   particiones (los parciales por bloque de T01 si existen; si no, los
   parciales actuales) y calcula una fila por tipo con event_type, events,
   share_of_events (events / total de eventos), rank (1 = más frecuente) y
   partition (la que asigna partition(event_type)). No uses
   pairs_after_local_combiner ni hot_key_load para ninguna cifra de la
   respuesta. Ajusta las columnas a la redacción aprobada si difiere, sin
   añadir datos externos ni columnas distintas de eventType.
4. CONCILIACIÓN: añade aserciones de que la suma de events es igual al
   número de filas, de que cada conteo coincide con el conteo directo por
   eventType y de que, para cada partición, la suma de events de los tipos
   asignados es igual a su carga por eventType en partition_loads.csv.
5. Persiste submission/analysis_answer.csv con esas columnas, ordenado por
   rank, y submission/questions.json con la estructura de claves de P500
   (pregunta y archivo de respuesta = analysis_answer.csv) más las claves
   reading y limit.
6. LECTURA: escribe en reading 2–4 líneas que respondan la pregunta con las
   cifras de analysis_answer.csv, y en limit el límite: la procedencia, el
   periodo y el significado de cada eventType no están documentados, de modo
   que los conteos describen este archivo y no la operación de una flota;
   no permiten hablar de riesgo, de conductores ni de camiones concretos.
   No interpretes los nombres de los tipos más allá de su texto literal y
   no uses eventKey. Imprime la tabla de respuesta al final como evidencia
   visible.
7. Añade a tests/ pruebas que verifiquen: questions.json existe, contiene la
   pregunta no vacía y apunta a analysis_answer.csv; analysis_answer.csv
   tiene las columnas del paso 3; los conteos coinciden por event_type con
   los recalculados desde data/truck_events.csv.gz; la suma de events es
   igual al número de filas del archivo; share_of_events suma 1 (con
   tolerancia); rank es coherente con events; por partición, la suma de
   events coincide con la carga por eventType de partition_loads.csv. Las
   pruebas deben ser independientes de la profundidad del taller en la
   distribución. No elimines pruebas existentes.
8. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
9. No modifiques datos ni herramientas, no rellenes notebooks/notebook.ipynb
   (S06 fuera de esta T02) y no toques otras actividades (P522 incluida),
   traceability.yaml ni design/.
```
