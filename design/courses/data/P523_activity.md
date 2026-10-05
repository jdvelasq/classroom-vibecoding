# P523 — Particionamiento por clave, sesgo y agregación local en telemetría de camiones

## Actividad actual implementada

**Implementación:** `implementation/data/P523_mapreduce_particionamiento/`.

### Preguntas analíticas actuales

- No hay pregunta analítica. El notebook declara un problema técnico: «Mostrar cómo claves reales de telemetría pueden concentrar trabajo y cómo un combiner reduce pares antes del shuffle».

`data/truck_events.csv.gz` (253718 bytes) tiene 17075 filas según `shuffle_comparison.csv`; el notebook declara «Cada fila representa un evento de telemetría de camiones» y sólo usa `eventKey` y `eventType`. La procedencia y el significado de `eventKey` no se documentan. Una función `partition(key)` asigna cada clave a una de cuatro particiones con MD5. Se comparan las cargas al particionar por `eventKey` y por `eventType` y se cuentan pares tras una agregación local. Persiste `submission/partition_loads.csv` (por `eventKey`: 4257, 4365, 4248, 4205; por `eventType`: 17041, 11, 7, 16) y `submission/shuffle_comparison.csv` (`17075, 5, 17041`). La primera celda copia `map_pairs`, `group_by_key` y `reduce_by_key`, pero ninguna se usa. El notebook de estudiante está vacío.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** evidencia de carga por partición para dos claves y conteo de pares antes y después de agregar.
- **Uso y límite:** muestra que agrupar estos eventos por `eventType` concentra casi todo en una partición. No dice nada sobre la operación de los camiones; no se reporta qué tipo de evento domina ni cuántos tipos hay, salvo lo deducible de los cinco pares finales.
- **Disciplinas contribuyentes:** internos de MapReduce (particionador, shuffle, combiner); no sirven a un producto analítico declarado.

### Highlights de contribución

- **H01 — Contrasta dos claves de partición sobre los mismos eventos y expone un sesgo real (caso y datos):** con la misma función, `eventKey` reparte 4205–4365 eventos por partición y `eventType` deja 17041 de 17075 en la partición 0. La particularidad es la distribución muy desigual de tipos de evento: la clave natural para agregar por tipo es justamente la que concentra el trabajo. Sin este hito, el curso no mostraría que la elección de clave cambia la carga, no sólo el resultado.
- **H02 — Usa una función de partición determinista:** `int(hashlib.md5(str(key).encode()).hexdigest(), 16) % 4` produce la misma asignación en cada ejecución, a diferencia de `hash` de Python; el notebook no explica esta elección. Primera partición por clave del curso (P522 particionaba por posición). Sin este hito, las cargas persistidas no serían reproducibles.
- **H03 — Cuantifica pares antes y después de una agregación local, con un defecto de modelado:** `partials` cuenta por `eventType` dentro de cada partición y `pairs_after_local_combiner = 5`. Como los parciales se indexan por la partición de destino y no por bloque de entrada, cada tipo cae en una sola partición y el valor coincide con el número de tipos distintos, es decir, con la salida final del reduce, no con los pares que un combiner del lado del mapper enviaría al shuffle. Además, `hot_key_load = max(skewed)` es la carga de la partición 0, que puede contener hasta dos tipos (las particiones 1–3 no están vacías), no necesariamente la de una sola clave. `assert combined_pairs < len(rows)` es trivial. Sin este hito no habría ninguna cuantificación del efecto de agregar antes del shuffle, pero la cifra actual no lo mide.

### Inventario técnico de implementación

- **Introduce:** particionador por hash MD5 módulo 4; comparación de cargas por clave; contadores `defaultdict(int)` por partición.
- **Reutiliza sin ejercitar:** `map_pairs`, `group_by_key`, `reduce_by_key` (copiados, no llamados).
- **Aplica en nuevo caso:** telemetría de camiones, tercer dataset del bloque.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Sesgo de clave | H01 | `partition_loads.csv` | Semántica de `eventKey` no documentada. |
| Particionador determinista | H02 | MD5 % 4 | Número de particiones fijo. |
| Agregación local previa al shuffle | H03 | `shuffle_comparison.csv` | Mide la reducción final, no un combiner por bloque de entrada; `hot_key_load` es carga de partición. |

### Relación técnica con actividades anteriores

Nuevo dato y nueva exigencia sobre el mismo modelo: P522 particionaba por posición y agregaba localmente sin nombrarlo; P523 particiona por clave y nombra el combiner. Los operadores de P519 se copian pero no se usan, por lo que la continuidad con el bloque es nominal. `dig/case-selection.md` no documenta P523: el diseño del bloque MapReduce termina en P521 y declara que los operadores explican el modelo de cómputo sin introducir la operación de plataformas distribuidas; shuffle, particionador y sesgo de carga pertenecen a esa operación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Sesgo de clave | S01, S02, S04 | `implementation/data/P523_mapreduce_particionamiento/data/truck_events.csv.gz`; `implementation/data/P523_mapreduce_particionamiento/submission/partition_loads.csv` | Procedencia «real» afirmada, no documentada. |
| H02 — Particionador determinista | S02 | `implementation/data/P523_mapreduce_particionamiento/professor/notebook.ipynb`: `partition` | Razón de MD5 no explicada. |
| H03 — Agregación local | S03, S04 | `implementation/data/P523_mapreduce_particionamiento/professor/notebook.ipynb`: celda del combiner y escritura; `implementation/data/P523_mapreduce_particionamiento/submission/shuffle_comparison.csv` | Defecto de modelado descrito. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/truck_events.csv.gz` | Sin procedencia; dos columnas usadas. |
| S02 | Particionador y claves | `professor/notebook.ipynb`: `partition`, bucle de cargas | Cuatro particiones fijas. |
| S03 | Agregación local | `professor/notebook.ipynb`: `partials` | Indexada por partición de destino. |
| S04 | Producto | `submission/partition_loads.csv`; `submission/shuffle_comparison.csv` | Sin `questions.json`. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia. |
| S06 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Vacío. |

### Contrato de evidencia actual

- **Notebook o código:** debe calcular cargas por partición para ambas claves y pares tras agregación local, y persistirlos.
- **`submission/`:** `partition_loads.csv` (cuatro particiones) y `shuffle_comparison.csv` (una fila).
- **Pruebas:** `test_01_submission_contains_partitioning_evidence` sólo verifica que existan ambos archivos.
- **Trazabilidad:** `data.C02`, `data.C03`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** P519: operadores copiados, no usados; P522: noción de partición (práctica, sin archivo).
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P523 → `data.C02`, `data.C03`, `data.C05`. `data.C03` («calidad, procedencia… y sesgos que afectan la evidencia») no se sostiene: el sesgo aquí es de carga computacional, no de evidencia; mapeo a escalar. Auditoría (pregunta 5): el taller se lee como lección de internos de procesamiento distribuido (shuffle, particionador, combiner), fuera de la frontera del curso y sin producto analítico; auditoría no resuelta.
