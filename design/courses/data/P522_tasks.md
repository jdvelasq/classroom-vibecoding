# P522 — Propuestas de mejora

**Línea base:** `P522_activity.md` (entrada S02 más reciente: `S02.P522.02`).

## T01 — Medir la aceleración en varios niveles de escala y con repeticiones: mediana, aceleración y eficiencia por configuración

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 56 y 59 — BDS-Problems of Scale, de nivel T1 (p. 56): «The need for measurement in the context of Big Data, including size, capacity and timing», «Approaches to addressing the problems of coordination with increasing numbers of agents / processes» y la destreza «Execute a computational task at multiple scale-levels successfully»; BDS-Parallel Programming, T2 (p. 59): «Limitations of parallelism including the overheads», «Identify the overheads and computational complexity associated with parallelism in particular algorithms» y la disposición de tener en cuenta «that the overheads of parallelism can become excessive in particular cases» (Claude, 2026-10-05). Fuente *authoritative*: expectativa general; la materialidad la sostiene el límite de H04 que registró S02.
  - `design/benchmarks-md/institutional/warwick-foundations-of-data-analytics.md` p. 2 — resultado de aprendizaje «Identify issues with scaling analytics to large data sets, and use appropriate techniques (NoSQL systems, data structures) to scale up the computation» (Claude, 2026-10-05). Fuente *institutional*: ilustra que identificar los problemas de escala es un resultado de un curso de fundamentos; sus técnicas (NoSQL, estructuras de síntesis) no se proponen.
  - `design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md` p. 31 — en MapReduce, el almacenamiento intermedio y el lanzamiento repetido de jobs «introducen una sobrecarga significativa en aplicaciones analíticas complejas», con costos de «Movimiento de los datos», «Lanzamiento de los procesos» y «Tiempos de comunicación» (Claude, 2026-10-05). Fuente *literature-derived*: contexto sobre Hadoop, no prescripción; sólo respalda que coordinar procesos tiene un costo.
- **Qué gana el estudiante:** entender cuándo repartir una reducción entre
  procesos compensa y cuándo no. Hoy P522 persiste un solo número
  (aceleración 2,722 con 14 procesos), medido en una corrida, dependiente
  del equipo e incluyendo el arranque del pool; S02 registra que «no permite
  generalizar sobre rendimiento» y nada lo interpreta. Con el cambio, el
  estudiante ejecuta la misma reducción con 1, 2, 4… procesos hasta
  `cpu_count` y sobre al menos dos tamaños de entrada (un extracto y el
  archivo completo), repite cada configuración, persiste la mediana, la
  aceleración (mediana con un proceso / mediana con *p* procesos) y la
  eficiencia (aceleración / *p*), y comprueba en cada configuración que el
  resultado es igual al de un proceso. Observa así que la aceleración es
  sublineal y que con entradas pequeñas el costo de coordinar procesos
  puede anular la ganancia: aprende la limitación de la paralelización, no
  sólo su promesa, y que una medición única de rendimiento no es evidencia.
  **Límite que no se resuelve:** esta T01 no resuelve el límite que S02
  mantiene para P522, «sin pregunta analítica» (ni uso del conteo por
  origen); sólo mejora la evidencia de un mecanismo. Lo que la pone en
  alcance es la aclaración del profesor (2026-10-05): el curso está entre la
  ingeniería de datos y la analítica, y el procesamiento paralelo
  introductorio pertenece a él como puente.
- **Anclas actuales:** H04 (medición persistida), que se extiende; H02
  (reducción en dos niveles) y H03 (equivalencia secuencial–paralela), que se
  conservan y se aplican a cada configuración; H01 (filtro de cancelados),
  sin cambios. Superficies S02 (partición de entrada), S04 (ejecución y
  medición, «corrida única»), S05 (`benchmark.csv`) y S06 (prueba de sólo
  existencia). Dependencia «Recibe de P519» (operadores copiados), sin
  cambios.
- **Alternativas menores descartadas:** advertir en un comentario que la
  aceleración depende del equipo hace visible el límite pero no enseña el
  contraste. Repetir sólo la medición actual (dos configuraciones) daría una
  mediana más estable, pero no mostraría cómo cambia la aceleración con el
  número de procesos ni con el tamaño. Ampliar `benchmark.csv` con filas y
  columnas nuevas (como sugería la candidata) cambiaría el contrato del
  archivo actual; se prefiere conservarlo y añadir una tabla aparte.
- **Contrato de no regresión:** se conservan H01–H03, el filtro de
  cancelados, la fórmula de particiones `max(4, cpu_count * 4)`,
  `origin_flights.csv` (82 orígenes) y la aserción de igualdad entre la
  corrida de un proceso y la de `cpu_count` procesos. `benchmark.csv`
  conserva sus columnas y sus dos filas (1 y `cpu_count` procesos sobre el
  archivo completo), ahora con la mediana de las repeticiones en lugar de
  una corrida. La medición sigue excluyendo `prepare_partitions`. La prueba
  existente se mantiene. H04 se reescribe en términos de la tabla de
  escalamiento.
- **Interacciones:** ninguna dentro de P522 (única propuesta).
  **Riesgo de identidad:** S02 registra que en P522 «la herramienta y su
  rendimiento son el producto», en tensión con `data.C05`. Esta T01 hace
  más rica esa medición; sólo se justifica si se presenta como evidencia de
  cuándo conviene paralelizar una reducción, no como afinamiento de
  rendimiento. Conviene discutirla junto con el encuadre analítico que el
  profesor decida para el bloque P519–P523. Capacidad: varias
  configuraciones con repeticiones alargan la ejecución; el número de
  repeticiones y el tamaño del extracto deben mantenerla dentro de la sesión.
- **Criterio de aceptación:** S05 encuentra `submission/scaling_benchmark.csv`
  con una fila por tamaño de entrada y número de procesos (al menos dos
  tamaños; 1 proceso incluido), con mediana de al menos tres repeticiones,
  aceleración, eficiencia y una columna que confirma la igualdad del
  resultado; `benchmark.csv` con su esquema actual; y pruebas que verifican
  la estructura (no los valores, que varían entre equipos). H04 queda
  reescrito en esos términos; H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P522_mapreduce_multiprocessing/

0. Inspecciona primero professor/main.py, src/main.py, data/flights.csv.gz,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/data/P522_activity.md (en particular, si benchmark.csv no
   tiene dos filas con 1 y cpu_count procesos y columnas de segundos y
   aceleración, o si la medición no rodea sólo run_mapreduce), detente e
   informa sin modificar nada. Ejecuta professor/main.py una vez: si falla
   porque temp/ no existe (S02 registró mkdir() sin parents), detente e
   informa; no lo corrijas dentro de esta T01. Registra el número de filas
   de flights.csv.gz y cpu_count del equipo.
1. No cambies map_flight, sum_flights, map_partition, la fórmula de
   particiones, origin_flights.csv ni la aserción de igualdad existente.
2. NIVELES DE ESCALA: define dos tamaños de entrada: un extracto con las
   primeras filas del archivo (por ejemplo 10 % o una cifra redonda que
   haga la corrida de un proceso claramente más corta) y el archivo
   completo. Prepara las particiones de cada tamaño con prepare_partitions
   (o una variante que reciba las filas) fuera de la medición, como hoy.
3. CONFIGURACIONES: para cada tamaño, ejecuta run_mapreduce con
   workers = 1, 2, 4, … (potencias de 2 menores que cpu_count) y cpu_count.
   Repite cada configuración al menos 3 veces (por ejemplo 5) midiendo con
   perf_counter igual que hoy. En cada configuración comprueba que el
   resultado es igual al de workers = 1 del mismo tamaño.
4. Persiste submission/scaling_benchmark.csv con columnas input_label,
   input_rows, partitions, workers, repetitions, median_seconds,
   min_seconds, max_seconds, speedup, efficiency, result_matches_single,
   donde speedup = median_seconds(workers = 1, mismo tamaño) /
   median_seconds y efficiency = speedup / workers.
5. Sigue escribiendo submission/benchmark.csv con sus columnas y sus dos
   filas actuales (1 y cpu_count procesos, archivo completo), tomando las
   medianas del paso 3.
6. Imprime al final la tabla de escalamiento. Si ninguna configuración del
   extracto tiene eficiencia claramente menor que la del archivo completo,
   no lo ocultes: informa el resultado en el reporte de S04. No crees un
   notebook (S07 queda fuera de esta T01).
7. Añade a tests/ pruebas que verifiquen: scaling_benchmark.csv existe y
   tiene esas columnas; hay al menos dos valores distintos de input_rows;
   cada tamaño tiene una fila con workers = 1 y speedup = 1; repetitions es
   al menos 3; efficiency coincide con speedup / workers (con tolerancia);
   result_matches_single es verdadero en todas las filas. No verifiques
   tiempos ni aceleraciones concretas. Las pruebas deben ser independientes
   de la profundidad del taller en la distribución. No elimines la prueba
   existente.
8. Ejecuta professor/main.py y las pruebas de la actividad sin errores.
9. No añadas pregunta analítica, no cambies el dataset y no modifiques
   otras actividades (P519, P523), traceability.yaml ni design/.
```

## T02 — Plantear la pregunta analítica que resuelve el procesamiento y mostrar cómo lo resuelve

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - Decisión del profesor en la entrevista del 2026-10-05, registrada en `design/courses/data/P500_log.md` (`Nota.P500.02`) (Claude, 2026-10-05). No proviene de un benchmark.
- **Qué gana el estudiante:** ver el procesamiento paralelo como se usa
  profesionalmente: se reparte una reducción entre procesos para responder
  algo, y la respuesta sale de lo que la ejecución repartida produce,
  comprobada contra la corrida de un proceso. Hoy P522 no declara pregunta
  (S02: «No hay pregunta analítica declarada … ninguna celda o comentario
  enuncia para qué se necesita ese conteo»; «Pregunta, usuario o decisión:
  no evidenciados») y la auditoría sigue no resuelta porque no hay
  «pregunta ni uso analítico del conteo» y porque «la herramienta y su
  rendimiento … son el producto, en tensión con `data.C05`» (S02.P522.02).
  Con esta T02, el estudiante enuncia la pregunta antes de procesar, la
  responde con el resultado de la corrida paralela (el que ya se compara con
  la de un proceso en H03), persiste la respuesta ligada a la pregunta y
  escribe su lectura y su límite. El conteo por origen deja de ser un
  subproducto de la medición y pasa a ser lo que el taller entrega; el
  filtro de cancelados de H01 se vuelve parte de la definición de la medida
  que la pregunta usa (vuelos operados, no programados).
  **Pregunta sugerida (sólo sugerencia; requiere la redacción aprobada por
  el profesor):** «En el archivo de vuelos disponible, ¿desde qué
  aeropuertos de origen salen más vuelos operados (no cancelados) y qué
  parte del total de vuelos operados concentran?». Se apoya en lo que S02
  describe: `map_flight` emite `(Origin, 1)` sólo para vuelos con
  `Cancelled == "0"`, la reducción en dos niveles produce
  `origin_flights.csv` con 82 orígenes (p. ej. `ABQ, 2027`) y el resultado
  paralelo se compara con el de un proceso. No se propone usuario ni
  decisión más allá de esta sugerencia.
  **Límite explícito:** esta T02 cierra el límite «sin pregunta analítica»
  que registró S02 sólo una vez ejecutada y verificada por S05; aprobarla no
  lo cierra. Tampoco resuelve por sí sola la tensión con `data.C05`: la
  reduce sólo si la respuesta, y no el número de procesos ni la
  aceleración, es el producto que se presenta.
- **Anclas actuales:** H02 (reducción en dos niveles, de donde sale la
  respuesta), H03 (equivalencia secuencial–paralela, con la que la
  respuesta se comprueba), H01 (filtro de cancelados, que define la medida)
  y H04 (medición, que se conserva y queda fuera de la respuesta);
  superficies S03 (mapper y reducer), S04 (ejecución), S05 (producto «sin
  `questions.json`»), S06 (prueba de sólo existencia) y S07 (interfaz del
  estudiante, que no se toca). Dependencia «Recibe de P519» (operadores
  copiados), sin cambios.
- **Alternativas menores descartadas:** escribir la pregunta sólo como
  comentario o docstring hace visible una intención, pero no muestra cómo
  la reducción repartida la resuelve ni deja evidencia verificable.
  Responderla con un conteo directo en pandas sobre `flights.csv.gz`
  evitaría el procesamiento que el taller enseña; ese conteo sirve sólo
  como comprobación en las pruebas. Añadir la aceleración a la respuesta
  reforzaría la lectura que S02 objeta (la herramienta como producto).
- **Contrato de no regresión:** se conservan H01–H04, `map_flight`,
  `sum_flights`, `map_partition`, `run_mapreduce`, la fórmula de
  particiones `max(4, cpu_count * 4)`, la aserción de igualdad,
  `origin_flights.csv` (82 orígenes) y `benchmark.csv` con su esquema (y
  `scaling_benchmark.csv` si T01 se ejecuta), y la prueba existente. Se
  añaden la pregunta al inicio de `professor/main.py`,
  `submission/questions.json`, `submission/analysis_answer.csv`, una lectura
  breve con su límite y una prueba. No cambian los datos ni las
  herramientas; los vacíos registrados por S02 (procedencia y periodo de
  los vuelos, comparación textual con `"0"` no validada, `mkdir()` sin
  `parents`) quedan fuera de esta T02, salvo la comprobación de la bandera
  en el paso 0.
- **Interacciones:** independiente de T01; no comparten archivos de
  `submission/` y ninguna necesita a la otra para ejecutarse. El orden
  puede ser cualquiera, pero es preferible T02 antes de T01: T01 advierte
  que su medición «sólo se justifica si se presenta como evidencia de
  cuándo conviene paralelizar una reducción, no como afinamiento de
  rendimiento» y pide discutirla «junto con el encuadre analítico que el
  profesor decida para el bloque P519–P523»; con T02 ya ejecutada, la tabla
  de escalamiento de T01 mide cuánto cuesta y cuánto ahorra repartir una
  reducción que responde una pregunta declarada. Si T02 va después de T01,
  la respuesta se toma del resultado de `cpu_count` procesos sobre el
  archivo completo, igual que hoy. El paso 9 de T01 («No añadas pregunta
  analítica») limita a T01 por sí misma; si se aprueban ambas, la pregunta
  la añade T02. **Nota de identidad de S02:** la herramienta y su
  velocidad no deben ser el producto; por eso la respuesta, la lectura y el
  límite de esta T02 no citan segundos, procesos ni aceleración, y
  `benchmark.csv` queda como evidencia del mecanismo, no como respuesta.
  Capacidad: es un cálculo pequeño sobre un resultado que ya existe y no
  alarga la ejecución.
- **Criterio de aceptación:** S05 encuentra (1) al inicio de
  `professor/main.py` la pregunta con la redacción aprobada por el profesor,
  idéntica a la registrada en `P522_log.md`; (2) `submission/questions.json`
  que liga esa pregunta con `analysis_answer.csv`, con la misma estructura
  de claves que el `questions.json` de P500 más `reading` y `limit`; (3)
  `analysis_answer.csv` calculado a partir del resultado de la corrida
  paralela, después de la aserción de igualdad con la de un proceso, con una
  fila por origen y columnas explícitas, sin columnas de tiempo; (4) una
  lectura de 2–4 líneas con su límite; y (5) una prueba que recalcula en
  un solo proceso el conteo de vuelos no cancelados por origen desde
  `data/flights.csv.gz` y lo compara con la respuesta, y concilia la
  respuesta con `origin_flights.csv`. Un highlight nuevo (H05) recoge la
  pregunta y su respuesta; H01–H04 siguen presentes. Sólo entonces S02
  puede revisar el límite «sin pregunta analítica» y la auditoría 5 de
  P522; la revisión de `data.C01` en `traceability.yaml` queda para S05.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P522_mapreduce_multiprocessing/

0. Inspecciona primero professor/main.py, src/main.py, data/flights.csv.gz,
   submission/ y tests/, y (sólo lectura)
   implementation/data/P500_superstore_metricas/submission/questions.json
   para tomar su estructura de claves. Si la implementación no coincide con
   design/courses/data/P522_activity.md, detente e informa sin modificar
   nada. Confirma que design/courses/data/P500_log.md contiene Nota.P500.02;
   si no, detente e informa. Registra los valores distintos de Cancelled y
   cuántas filas tiene cada uno: si no son textos "0" y "1" (o equivalentes
   sin ambigüedad), detente e informa; no cambies el filtro dentro de esta
   T02. Ejecuta professor/main.py una vez: si falla porque temp/ no existe
   (S02 registró mkdir() sin parents), detente e informa; no lo corrijas
   dentro de esta T02.
1. PREGUNTA: no inventes la pregunta, el usuario ni la decisión. Usa la
   redacción que el profesor haya aprobado en la discusión de esta T02
   (registrada en P522_log.md). La pregunta sugerida en P522_tasks.md no es
   una aprobación. Si no existe redacción aprobada, detente y pídela.
   Escríbela al inicio de professor/main.py (docstring del módulo o una
   constante QUESTION usada al escribir questions.json).
2. No cambies map_flight, sum_flights, map_partition, run_mapreduce, la
   fórmula de particiones, la aserción de igualdad, origin_flights.csv,
   benchmark.csv ni, si existe, scaling_benchmark.csv.
3. RESPUESTA DESDE LO PROCESADO: después de la aserción de igualdad entre
   la corrida de un proceso y la paralela, toma el resultado paralelo y
   calcula una fila por origen con origin, operated_flights,
   share_of_operated (operated_flights / total de vuelos operados) y rank
   (1 = más vuelos; empates con el mismo rango). No incluyas segundos,
   procesos ni aceleración. Ajusta las columnas a la redacción aprobada si
   difiere, sin añadir datos externos ni columnas del archivo distintas de
   Origin y Cancelled.
4. Persiste submission/analysis_answer.csv con esas columnas, ordenado por
   rank, y submission/questions.json con la estructura de claves de P500
   (pregunta y archivo de respuesta = analysis_answer.csv) más las claves
   reading y limit.
5. LECTURA: escribe en reading 2–4 líneas que respondan la pregunta con las
   cifras de analysis_answer.csv (por ejemplo, los primeros orígenes y la
   parte del total que concentran), y en limit el límite: el archivo no
   documenta procedencia ni periodo, de modo que los conteos describen este
   archivo y no una red de aeropuertos ni un año; la medida depende de que
   Cancelled == "0" identifique los vuelos operados (comprobado en el paso
   0). No cites tiempos ni aceleración, no nombres ciudades ni aerolíneas
   que el archivo no contenga y no añadas interpretaciones de demanda o de
   negocio que la redacción aprobada no contenga. Imprime la tabla de
   respuesta al final como evidencia visible.
6. Añade a tests/ pruebas que verifiquen: questions.json existe, contiene la
   pregunta no vacía y apunta a analysis_answer.csv; analysis_answer.csv
   tiene las columnas del paso 3 y ninguna columna de tiempo; sus conteos
   coinciden por origen con los recalculados en un solo proceso desde
   data/flights.csv.gz (filas con Cancelled == "0", contadas por Origin) y
   con origin_flights.csv; share_of_operated suma 1 (con tolerancia); rank
   es coherente con operated_flights. Las pruebas deben ser independientes
   de la profundidad del taller en la distribución y no deben depender de
   temp/. No elimines pruebas existentes.
7. Ejecuta professor/main.py y las pruebas de la actividad sin errores.
8. No modifiques datos ni herramientas, no crees notebooks (S07 fuera de
   esta T02) y no toques otras actividades (P519, P523 incluidas),
   traceability.yaml ni design/.
```
