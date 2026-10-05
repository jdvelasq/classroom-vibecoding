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
