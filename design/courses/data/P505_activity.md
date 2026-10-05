# P505 — JOIN entre autores, documentos y fuentes del corpus Scopus

## Actividad actual implementada

**Implementación:** `implementation/data/P505_scopus_sql_intermedio/`.

### Preguntas analíticas actuales

- ¿Qué autores concentran más documentos sobre proptech?
- ¿Qué fuentes concentran más documentos sobre proptech?

Usa `data/scopus_proptech.db` (mismo tamaño que la base de P503) y `data/search_string.txt`. `professor/notebook.ipynb` dibuja el camino `authors <- document_authors -> documents -> sources` como comentario y ejecuta dos consultas con `JOIN`, `COUNT(DISTINCT ...)`, `GROUP BY` por identificador y nombre, orden con desempate alfabético y `LIMIT 20`. Persiste `authors_by_documents.csv`, `sources_by_documents.csv` (21 líneas cada uno) y `questions.json`. Ambos CSV tienen el mismo tamaño (292 y 869 bytes) y las mismas primeras filas que los homónimos de P503 (p. ej. «Tagliaro C.», 8; «Journal of Property Investment and Finance», 9). El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** concentración de documentos por autor y por fuente; usuario y decisión no evidenciados.
- **Producto terminal:** dos rankings de 20 autores y 20 fuentes por número de documentos, en todo el periodo del corpus.
- **Uso y límite:** identifica autores y fuentes con más documentos recuperados. No distingue tipos documentales (P504), no corrige el conteo completo por coautoría y el corte en 20 con desempate alfabético puede excluir empatados. Reproduce respuestas ya persistidas en P503.
- **Disciplinas contribuyentes:** SQL relacional (`JOIN` sobre tabla puente) como medio de consulta.

### Highlights de contribución

- **H01 — Recorre explícitamente una tabla puente para contar documentos por autor:** el diagrama de texto `authors <- document_authors -> documents -> sources` precede a `JOIN document_authors AS da ON a.author_id = da.author_id` con `COUNT(DISTINCT da.document_id)`, y a `JOIN documents AS d ON s.source_id = d.source_id` con `COUNT(DISTINCT d.document_id)`. Extiende P504 (consultas a una tabla) hacia consultas de varias tablas escritas por el estudiante; P503 ya usaba `JOIN ... USING` dentro de vistas. Sin este hito, la relación muchos a muchos construida en P503 no se recorrería fuera de las vistas predefinidas.
- **H02 — Cuenta autoría completa sobre una relación muchos a muchos (caso y datos):** cada documento aparece en `document_authors` una vez por coautor, de modo que el ranking asigna el documento completo a cada autor (conteo completo); la suma de `document_count` entre autores excede el número de documentos. La agrupación por `a.author_id` delega la identidad del autor en el ID Scopus, no en el nombre. Sin este hito, el ranking podría leerse como reparto de la producción. Límite: el notebook no declara esta interpretación ni contrasta con un conteo fraccionado.

### Inventario técnico de implementación

- **Introduce:** `JOIN ... ON` con alias explícitos; `COUNT(DISTINCT ...)`; diagrama de texto del camino de unión.
- **Reutiliza:** `GROUP BY`, `ORDER BY` con desempate, `LIMIT 20` y exportación a CSV (P503, P504).
- **Reutiliza:** `questions.json`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Unión a través de tabla puente | H01 | `authors`–`document_authors`, `sources`–`documents` | Mismo resultado que vistas de P503. |
| Conteo completo por coautoría | H02 | `COUNT(DISTINCT document_id)` por `author_id` | Interpretación no declarada en el notebook. |

### Relación técnica con actividades anteriores

Misma pregunta y misma respuesta que P503: las vistas `v_authors_by_documents` y `v_sources_by_documents` ya calculaban ambos rankings con `COUNT(*)`, `LIMIT 20` y el mismo orden; los CSV persistidos coinciden en tamaño y primeras filas. La novedad es técnica: el estudiante escribe los `JOIN` y usa `COUNT(DISTINCT ...)`. Posible duplicación de producto que requiere decisión posterior de curso.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Unión por tabla puente | S02 | `implementation/data/P505_scopus_sql_intermedio/professor/notebook.ipynb` (diagrama y dos consultas) | El diagrama es un comentario, no se verifica. |
| H02 — Conteo completo (caso y datos) | S01, S02, S03 | `implementation/data/P505_scopus_sql_intermedio/professor/notebook.ipynb`; `implementation/data/P505_scopus_sql_intermedio/submission/authors_by_documents.csv` | La suma total no se calcula ni se persiste. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/scopus_proptech.db`; `data/search_string.txt` | Copia de la base de P503. |
| S02 | Consultas | `professor/notebook.ipynb` | Dos `JOIN`; todo el periodo; `LIMIT 20`. |
| S03 | Producto | `submission/authors_by_documents.csv`; `submission/sources_by_documents.csv`; `submission/questions.json` | Coincide con salidas de P503. |
| S04 | Secuencia | relación con `implementation/data/P503_scopus_relacional/submission/` | Duplicación de respuestas. |
| S05 | Pruebas | `tests/test_activity.py` | Sólo existencia de tres archivos. |
| S06 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/notebook.ipynb` debe unir autores y fuentes con documentos a través de sus relaciones y persistir los rankings.
- **`submission/`:** `authors_by_documents.csv`, `sources_by_documents.csv`, `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige existencia; como los nombres coinciden con salidas de P503, copiar esos archivos satisfaría la prueba. No verifica las consultas ni el contenido.
- **Trazabilidad:** `data.C01`, `data.C02`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P503:** `scopus_proptech.db` y las tablas puente; de P504, la práctica de consulta desde notebook.
- **Habilita para P506 y P508:** P506 reutiliza la unión `authors`–`document_authors`; P508 reutiliza la consulta de fuentes con `COUNT(DISTINCT d.document_id)` añadiendo un parámetro de periodo.

## Trazabilidad y auditoría

Entrada revisada: P505 → `data.C01`, `data.C02`, `data.C05`. C02 y C05 tienen evidencia. `data.C01` es débil: las preguntas están dadas y no se derivan requisitos de datos nuevos (unidad, granularidad o restricciones). El producto es una descripción de concentración del corpus, idéntica a la ya producida en P503. Pregunta 5: sin producto nuevo, la contribución observable es la sintaxis `JOIN`; la actividad puede describirse como lección de SQL intermedio. Riesgo de identidad alto, a resolver junto con la duplicación con P503.
