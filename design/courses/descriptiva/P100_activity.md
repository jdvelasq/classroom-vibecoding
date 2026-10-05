# P100 — MapReduce: conteo de palabras

## Actividad actual implementada

**Implementación:** `implementation/descriptiva/P100_mapreduce_word_count/`.

### Preguntas analíticas actuales

- No hay una pregunta analítica declarada. La única pregunta operativa que la implementación responde es: ¿cuántas veces aparece cada palabra normalizada en el conjunto de textos de entrada?

El caso son cuatro textos breves en inglés (`file1.txt`–`file4.txt`) que definen *analytics*, *business intelligence* y *data science*; su procedencia no está documentada. El script del profesor replica cada texto 1.000 veces en `temp/input/`, lo procesa con un flujo mapper → *shuffle and sort* → reducer escrito en Python puro y copia el resultado, con las convenciones de salida de Hadoop, a `submission/`. El producto es una tabla de frecuencias de términos; no hay usuario, decisión ni interpretación de esas frecuencias.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** capacidad de datos: un conteo de palabras persistido como `part-00000` (palabra y conteo separados por tabulador) más el marcador `_SUCCESS`.
- **Uso y límite:** muestra cómo un conteo se descompone en etapas map/reduce sobre muchos archivos. No permite inferir nada sobre un corpus real: el volumen es artificial (copias idénticas), las frecuencias son las de cuatro párrafos multiplicadas por 1.000 y no hay paralelismo ni sistema distribuido, sólo una simulación secuencial en memoria.
- **Disciplinas contribuyentes:** ingeniería de datos y computación distribuida (paradigma MapReduce, convenciones HDFS/Hadoop) y procesamiento básico de texto. El producto es principalmente una destreza de disciplina contribuyente; su servicio a la descripción analítica queda implícito.

### Highlights de contribución

- **H01 — Descompone un conteo en map, shuffle/sort y reduce:** el script lee registros `(archivo, línea)`, el mapper emite pares `(palabra, 1)`, `sorted()` agrupa claves iguales de forma contigua y el reducer acumula claves adyacentes. Es la primera actividad del curso; sin este hito no existiría en la secuencia la idea de transformar registros en pares clave-valor y agregarlos por clave, que luego reaparece como `groupby` y `GROUP BY` en P103–P104.
- **H02 — Fija la unidad de análisis textual mediante reglas de normalización (caso y datos):** el texto no estructurado exige decidir qué es una «palabra»: el mapper pasa a minúsculas, elimina `string.punctuation` y separa por espacios. Esa regla tiene consecuencias observables en este corpus: «(BI)» se cuenta como `bi`, y expresiones con guion como «data-driven» (en `file4.txt`) se funden en un único token sin guion. Las pruebas fijan conteos de `analytics`, `business`, `by`, `algorithms` y `analysis`, de modo que la regla de tokenización forma parte del contrato. Sin este hito, el conteo parecería independiente de decisiones de representación.
- **H03 — Simula volumen replicando el corpus:** `n = 1000` copias por archivo generan 4.000 archivos en `temp/input/` y el script mide el tiempo de ejecución. Por construcción todos los conteos son múltiplos de 1.000 y las frecuencias relativas coinciden con las de los cuatro textos originales. Sin este hito no habría motivo para separar etapas; el límite es que el volumen no aporta información nueva.
- **H04 — Reproduce las convenciones de salida de un trabajo Hadoop:** vacía o crea `temp/output/`, escribe `part-00000` y `_SUCCESS` y luego copia la salida desde el «HDFS simulado» al disco local (`submission/`). Sin este hito no se haría visible la diferencia entre almacenamiento de trabajo y entregable.
- **H05 — Verifica el resultado con conteos esperados:** las pruebas ejecutan `main.py` (el del profesor si existe `.PROFESSOR`, si no `src/main.py`), exigen ambos archivos y comparan cinco conteos exactos. Sin este hito el entregable sólo se comprobaría por existencia.

### Inventario técnico de implementación

- **Introduce:** lectura de múltiples archivos con `glob`, preparación idempotente de carpetas de trabajo, normalización de texto con `str.lower` y `str.translate`, pares clave-valor, ordenamiento como *shuffle*, reducción por claves adyacentes, escritura tabulada y marcador de éxito.
- **Introduce:** medición de tiempo con `time.time()` (se imprime; no se persiste).
- **Introduce:** contrato de ejecución dual profesor/estudiante en las pruebas mediante el marcador `.PROFESSOR` y `runpy.run_path`.
- **Interfaz de estudiante:** `src/main.py` sólo declara rutas y lanza `NotImplementedError`; el estudiante debe construir todo el flujo.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Patrón MapReduce | H01, H03 | Mapper, `sorted()` como *shuffle*, reducer secuencial sobre 4.000 archivos replicados | `professor/main.py`; simulación en un proceso, sin paralelismo ni tolerancia a fallos. |
| Tokenización de texto | H02 | Minúsculas, eliminación de puntuación, separación por espacios | `professor/main.py`, pruebas con cinco conteos; no hay *stopwords*, lematización ni n-gramas. |
| Convenciones de salida | H04 | `part-00000`, `_SUCCESS`, copia a `submission/` | `submission/`; la copia imita, no usa, HDFS. |

### Relación técnica con actividades anteriores

Es la primera actividad de `descriptiva`; no hay actividades anteriores en el curso con las cuales compararla. P101 reutiliza exactamente los mismos datos, el mismo flujo y las mismas aserciones.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Etapas map/shuffle/reduce | S03 | `implementation/descriptiva/P100_mapreduce_word_count/professor/main.py`: secciones *Mapper*, *Shuffle and sort*, *Reducer* | Simulación secuencial; no demuestra comportamiento distribuido. |
| H02 — Unidad textual y normalización | S01, S02, S05 | `implementation/descriptiva/P100_mapreduce_word_count/professor/main.py` (mapper); `implementation/descriptiva/P100_mapreduce_word_count/data/file4.txt`; `implementation/descriptiva/P100_mapreduce_word_count/tests/test_activity.py` | El contenido de `submission/part-00000` no es visible en el digest; los conteos citados son los esperados por la prueba, no un resultado leído del artefacto. |
| H03 — Volumen simulado | S01, S03 | `implementation/descriptiva/P100_mapreduce_word_count/professor/main.py`: `n = 1000`, generación de copias, `time.time()` | El tiempo no se persiste; las copias no añaden variación. |
| H04 — Convenciones de salida | S04 | `implementation/descriptiva/P100_mapreduce_word_count/professor/main.py`; `implementation/descriptiva/P100_mapreduce_word_count/submission/part-00000`; `implementation/descriptiva/P100_mapreduce_word_count/submission/_SUCCESS` | No hay HDFS real. |
| H05 — Conteos esperados | S05, S06 | `implementation/descriptiva/P100_mapreduce_word_count/tests/test_activity.py`; `implementation/descriptiva/P100_mapreduce_word_count/src/main.py` | Cinco palabras; no verifica el resto de la tabla ni su orden. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset y replicación | `data/file1.txt`–`data/file4.txt`; `professor/main.py` (`n = 1000`) | Textos sin procedencia documentada; los conteos esperados dependen de `n`. |
| S02 | Representación: regla de tokenización | `professor/main.py` (mapper) | Cambiarla altera los conteos fijados en las pruebas. |
| S03 | Método: flujo MapReduce simulado | `professor/main.py` | Script lineal sin funciones; ordenamiento completo en memoria. |
| S04 | Producto y persistencia | `submission/part-00000`; `submission/_SUCCESS` | Formato tabulado sin encabezado; sin interpretación. |
| S05 | Pruebas | `tests/test_activity.py`; `tests/conftest.py` | Existencia de archivos y cinco conteos exactos. |
| S06 | Interfaz de estudiante | `src/main.py` | Esqueleto con `NotImplementedError`; no hay notebook ni `DESCRIPTION.md`. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` debe generar las copias, ejecutar map/sort/reduce y copiar `part-00000` y `_SUCCESS` a `submission/`.
- **`submission/`:** `part-00000` (2.844 bytes) y `_SUCCESS` (vacío); contienen la tabla de frecuencias, sin metadatos de ejecución.
- **Pruebas:** ejecutan el código y verifican existencia de ambos archivos y los conteos de cinco palabras. No verifican la regla de tokenización completa, el orden, ni que se haya usado un esquema map/reduce (cualquier conteo correcto pasa).
- **Trazabilidad:** P100 mapea sólo `descriptiva.C02`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna dentro del curso.
- **Habilita para P101:** los mismos datos, el flujo map/sort/reduce y el contrato de conteos se reutilizan como punto de partida; `src/main.py` de P101 contiene este flujo en forma de script lineal.

## Trazabilidad y auditoría

P100 está mapeada a `descriptiva.C02` en `implementation/descriptiva/traceability.yaml`. La evidencia sostiene un conteo de frecuencias sobre texto, pero no una exploración de distribuciones, atípicos o calidad «antes de concluir»: no hay conclusión ni inspección del resultado. El mapeo a C02 es, a lo sumo, habilitador. Ante la pregunta descriptiva (qué ocurre, para quién, dónde, cuándo, con qué evidencia), la actividad no responde ninguna dimensión salvo «qué palabras aparecen». El producto es una capacidad de datos al servicio de descripciones posteriores; aislada, la actividad puede caracterizarse como un ejercicio introductorio de ingeniería de datos (MapReduce). La auditoría de identidad queda no resuelta en el nivel de actividad.
