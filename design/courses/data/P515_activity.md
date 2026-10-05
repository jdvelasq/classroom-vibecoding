# P515 — ELT Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P515_superstore_elt/`.

### Preguntas analíticas actuales

- ¿Qué segmentos y regiones concentran las ventas y la utilidad?

Misma pregunta que P514 y mismas cuatro tablas derivadas con el mismo manifiesto. `professor/main.py` carga cada CSV sin cambios como tabla `raw_*` en `submission/superstore_elt.db`, crea dentro de SQLite `curated_superstore_sales` con `CREATE TABLE ... AS SELECT lines.*, Order Date, Customer Segment, Region, Product Category` y uniones internas `USING` sobre las claves contextuales, agrega con SQL y persiste la respuesta y un reporte de dos etapas (raw 5926; curated 1952; ambos `SUCCESS`). La tabla curada selecciona sólo cuatro columnas de contexto, a diferencia del detalle completo (28 columnas) de P511/P514. Las cinco primeras filas de `sales_by_segment_region.csv` coinciden con P514 en ventas y difieren sólo en la representación flotante de la utilidad (p. ej., 26395.042696 frente a 26395.042695999997); el código no compara ambas salidas. El estudiante parte de `src/main.py` con `NotImplementedError`; `notebooks/` no contiene notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** pregunta persistida en `questions.json`; usuario y decisión no evidenciados.
- **Producto terminal:** `submission/superstore_elt.db` (capas raw y curada), `sales_by_segment_region.csv`, `elt_report.csv` y `questions.json`.
- **Uso y límite:** la base permite auditar la respuesta desde las tablas raw dentro del mismo archivo. Las uniones internas en SQL no validan cardinalidad: una clave ausente eliminaría líneas y una duplicada las multiplicaría sin error; la conservación del grano sólo se observa en el número 1952 del reporte, sin aserción. El estado es constante.
- **Disciplinas contribuyentes:** SQL y ubicación de la transformación (ELT) al servicio de la misma respuesta descriptiva de P514.

### Highlights de contribución

- **H01 — Traslada la transformación al motor después de cargar los datos sin cambios:** `to_sql` de cuatro tablas `raw_*` y `CREATE TABLE ... AS SELECT` para la capa curada. Contrasta con P514, donde la transformación ocurre en pandas antes de publicar; primera tabla derivada creada con CTAS en el curso (P503 crea vistas, no tablas derivadas). Sin este hito, el curso no contrastaría dónde ocurre la transformación con la misma pregunta.
- **H02 — Reconstruye la línea integrada en SQL con las claves contextuales homónimas (caso y datos):** el diseño de las tablas derivadas, con la misma clave nombrada igual en hecho y contexto, permite `JOIN ... USING(order_context_key)` y equivalentes. Al no existir `validate=`, la garantía de P511/P514 se sustituye por el conteo curated = 1952 del reporte y por la coincidencia de resultados con P514, que sólo es observable comparando archivos. Sin este hito, no se haría visible que mover la transformación a SQL cambia el mecanismo con que se protege el grano.
- **H03 — Entrega las capas raw y curada en un mismo artefacto consultable:** `superstore_elt.db` contiene las cuatro tablas fuente y la curada; P514 deja raw en `temp/`, fuera de la entrega. Sin este hito, la respuesta no podría auditarse contra su fuente dentro de la entrega.

### Inventario técnico de implementación

- **Introduce:** carga raw a SQLite y transformación `CREATE TABLE AS SELECT`; selección explícita de columnas curadas.
- **Reutiliza:** pregunta, datos y forma de reporte de P514; uniones SQL `USING` (P512); agregación SQL (P504–P507).
- **No ejercita:** validación de cardinalidad en SQL ni comparación con la salida de P514.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Transformación en el motor (ELT) | H01 | `raw_*` + CTAS en SQLite | Sin restricciones ni índices declarados. |
| Uniones por claves homónimas | H02 | `JOIN ... USING` sobre `*_context_key` | Sin validación de cardinalidad. |
| Capas en un artefacto | H03 | `submission/superstore_elt.db` | Estado constante en el reporte. |

### Relación técnica con actividades anteriores

Misma pregunta y datos que P514 con nueva ubicación de la transformación; la respuesta es numéricamente la misma (salvo precisión flotante). Es un contraste deliberado ETL/ELT, pero la pregunta, los datos y la respuesta repetidos hacen que la contribución dependa sólo del contraste técnico. Posible duplicación de producto con P511 y P514 que requiere decisión posterior.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Transformación en el motor | S02, S03 | `implementation/data/P515_superstore_elt/professor/main.py` (`load_sources`, `transform_in_database`); `implementation/data/P515_superstore_elt/submission/superstore_elt.db` | No se discute cuándo conviene una u otra ubicación. |
| H02 — Uniones por claves homónimas | S01, S02, S03 | `implementation/data/P515_superstore_elt/data/source_manifest.json`; `implementation/data/P515_superstore_elt/professor/main.py`; `implementation/data/P515_superstore_elt/submission/elt_report.csv`; `implementation/data/P514_superstore_etl/submission/sales_by_segment_region.csv` | Equivalencia con P514 verificada sólo en las filas visibles. |
| H03 — Capas en un artefacto | S03, S04 | `implementation/data/P515_superstore_elt/submission/superstore_elt.db`; `implementation/data/P515_superstore_elt/tests/test_activity.py` | Las pruebas no abren la base. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset: tablas derivadas de Superstore | `data/*.csv`; `data/source_manifest.json` | Idénticas a P511, P512 y P514. |
| S02 | Método: ELT en SQLite | `professor/main.py` | Uniones internas sin validación. |
| S03 | Producto: base, respuesta y reporte | `submission/superstore_elt.db`; `submission/sales_by_segment_region.csv`; `submission/elt_report.csv`; `submission/questions.json` | Respuesta igual a P514. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia de cuatro archivos. |
| S05 | Interfaz del estudiante | `src/main.py` | Stub sin enunciado; sin notebook. |
| S06 | Trazabilidad | `implementation/data/traceability.yaml` | P515 sin entrada. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/main.py` carga raw, crea la tabla curada con SQL, agrega, cuenta filas y persiste.
- **`submission/`:** `superstore_elt.db` (cinco tablas), `sales_by_segment_region.csv` (16 filas), `elt_report.csv` (2 etapas), `questions.json`.
- **Pruebas:** `test_01` verifica que existen los cuatro archivos; no abre la base ni verifica conteos o sumas.
- **Trazabilidad:** sin entrada en `traceability.yaml`; requiere escalación.

### Dependencias en la secuencia

- **Recibe de P514:** pregunta, forma de reporte `stage/rows/status` y contraste implícito. **Recibe de P511:** datos y manifiesto. **Recibe de P512:** uniones `USING` sobre claves contextuales.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

`implementation/data/traceability.yaml` no contiene entrada para P515 (salta de P514 a P516); la descripción previa le atribuía `data.C01`–`data.C05` sin respaldo. Se escala la ausencia sin inferir un mapeo. Por evidencia, la actividad ejercita estructuración y transformación (cercana a C02) y SQLite como habilitador (C05), pero no se asigna. Auditoría 5: con pregunta, datos y respuesta idénticos a P514, la única contribución es el contraste ETL/ELT, un tema propio de Data Engineering; la actividad puede describirse como taller de ubicación de transformaciones sin producto analítico nuevo. Auditoría no resuelta.
