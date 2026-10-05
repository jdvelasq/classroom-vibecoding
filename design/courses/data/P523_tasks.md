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
