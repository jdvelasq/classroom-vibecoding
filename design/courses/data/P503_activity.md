# P503 — Modelo relacional de un export Scopus sobre proptech

## Actividad actual implementada

**Implementación:** `implementation/data/P503_scopus_relacional/`.

### Preguntas analíticas actuales

- ¿Cómo se estructura la producción científica sobre proptech por año, autores y fuentes?
- ¿Qué autores tienen más documentos en el resultado?
- ¿Qué revistas y conferencias concentran más documentos?

El caso es un export Scopus comprimido (`data/scopus.csv.gz`) acompañado de la cadena de búsqueda que lo produjo (`data/search_string.txt`: `TITLE-ABS-KEY` con ocho términos sobre proptech y digitalización inmobiliaria). `professor/notebook.ipynb` lee el export (una fila por documento), separa las entidades fuente, documento, autor y palabra clave, crea seis tablas SQLite con claves primarias y foráneas, carga los datos, define tres vistas y exporta sus resultados. Se persisten `scopus_proptech.db`, `documents_by_year.csv` (44 líneas: 43 años; el primero visible es 1969), `authors_by_documents.csv` y `sources_by_documents.csv` (20 filas cada uno) y `questions.json`. `notebooks/notebook.ipynb` del estudiante no tiene celdas. No se documenta fecha del export ni condiciones de uso de Scopus.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** descripción de la estructura de un corpus bibliográfico; usuario y decisión no evidenciados.
- **Producto terminal:** base relacional reutilizable del corpus y tres respuestas descriptivas (documentos por año, 20 autores y 20 fuentes con más documentos).
- **Uso y límite:** permite contar documentos por año, autor y fuente sin repetir texto multivalor. No examina la pertinencia de los documentos recuperados (el corpus empieza en 1969 para un término reciente), no distingue tipos documentales en los conteos y los rankings se cortan en 20 con desempate alfabético.
- **Disciplinas contribuyentes:** modelado relacional y SQL (SQLite) al servicio de una representación consultable del corpus; bibliometría como dominio.

### Highlights de contribución

- **H01 — Conserva la consulta junto al export para reproducir el corpus:** la primera celda declara «Conservamos el export y la consulta para poder reproducir el caso» y `search_string.txt` acompaña al export; la misma cadena se copia en P504–P508. Primera vez en el curso que la procedencia de un dataset se materializa como archivo. Sin este hito, el corpus no podría regenerarse ni delimitarse. Límite: no se registra fecha de descarga, base de datos consultada ni restricción de uso.
- **H02 — Normaliza campos multivalor en relaciones muchos a muchos (caso y datos):** en el export cada documento trae `Authors`, `Author(s) ID` y `Author Keywords` como listas separadas por `;`. El notebook las divide en `document_authors` (con `author_position`, que conserva el orden de autoría) y `document_keywords` (con `explode`), y extrae `sources` como entidad porque «una fuente puede respaldar muchos documentos». Sin este hito, contar documentos por autor o palabra clave exigiría manipular texto en cada consulta y produciría duplicados.
- **H03 — Decide identidad y faltantes antes de cargar:** autores se identifican por `Author(s) ID`, no por nombre; si las listas de IDs y nombres no se alinean, el nombre de respaldo es el propio ID; las fuentes vacías o nulas se reemplazan por «Sin fuente identificada»; se descartan registros sin `EID` o `Title`; las palabras clave se recortan, se pasan a `casefold()` y se deduplican. Sin este hito, la representación relacional heredaría homónimos, vacíos y variantes de mayúsculas.
- **H04 — Convierte relaciones implícitas en restricciones verificables:** `PRAGMA foreign_keys = ON`, `PRIMARY KEY` simples y compuestas, `NOT NULL`, `UNIQUE (source_title)` y `FOREIGN KEY` en las tablas puente; la carga sigue el orden entidades → relaciones «para respetar las claves foráneas». Primera base relacional construida en el curso (P501 sólo volcaba DataFrames a SQLite). Sin este hito, la integridad referencial quedaría sin comprobar.
- **H05 — Responde las preguntas con vistas en lugar de tablas copiadas:** `v_documents_by_year`, `v_authors_by_documents` y `v_sources_by_documents` agregan con `GROUP BY` y `JOIN ... USING`, ordenan con desempate por nombre y limitan a 20; sus resultados se exportan a CSV y se enlazan en `questions.json`. Sin este hito, las respuestas no quedarían ligadas a una definición almacenada en la base. Límite: el corte en 20 con desempate alfabético puede excluir autores o fuentes empatados (en autores hay varios con 5 documentos).

### Inventario técnico de implementación

- **Introduce:** lectura de CSV comprimido (`compression="gzip"`); `str.split`, `explode`, `casefold`, `drop_duplicates`; generación de claves sustitutas (`source_id`) desde el índice.
- **Introduce:** DDL SQLite (`CREATE TABLE` con PK, FK, `NOT NULL`, `UNIQUE`), `PRAGMA foreign_keys`, carga ordenada con `to_sql(if_exists="append")`.
- **Introduce:** vistas SQL con `GROUP BY`, `JOIN ... USING`, `ORDER BY`, `LIMIT`; exportación con `pd.read_sql_query`.
- **Aplica en nuevo caso:** `questions.json` con tres preguntas (patrón de P500–P502) y cambio de dominio de ventas a bibliografía.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Procedencia de un export bibliográfico | H01 | `search_string.txt` junto a `scopus.csv.gz` | Sin fecha ni condiciones de uso. |
| Normalización de multivalor | H02 | Tablas puente autor y palabra clave con orden de autoría | Palabras clave sin unificación de sinónimos. |
| Identidad de autor y faltantes | H03 | ID Scopus como clave; marcador de fuente ausente | Desambiguación delegada a Scopus. |
| Esquema con integridad referencial | H04 | PK, FK, `PRAGMA foreign_keys` | Sin prueba que la verifique. |
| Respuestas como vistas | H05 | Tres vistas y tres CSV | Corte en 20 con desempate alfabético. |

### Relación técnica con actividades anteriores

Nuevo caso, nuevo dato y nuevo método respecto a P500–P502: de un CSV plano de ventas a un export con campos multivalor que requiere modelado relacional. Comparte con P501 el uso de SQLite, pero P501 sólo volcaba agregados; P503 diseña esquema e integridad. No se observa duplicación con actividades anteriores.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Procedencia de la consulta | S01 | `implementation/data/P503_scopus_relacional/data/search_string.txt`; `implementation/data/P503_scopus_relacional/professor/notebook.ipynb` (celda 1) | No hay manifiesto con fecha o licencia. |
| H02 — Multivalor a muchos a muchos (caso y datos) | S01, S02 | `implementation/data/P503_scopus_relacional/professor/notebook.ipynb`: celdas de `sources`, `document_authors`, `document_keywords` | El export es binario en el volcado; su estructura se infiere de las columnas usadas. |
| H03 — Identidad y faltantes | S02 | `implementation/data/P503_scopus_relacional/professor/notebook.ipynb`: `fillna("Sin fuente identificada")`, `dropna(subset=["EID", "Title"])`, bucle de autores, `casefold` | No se cuantifican los registros afectados. |
| H04 — Integridad referencial | S03 | `implementation/data/P503_scopus_relacional/professor/notebook.ipynb`: celdas `CREATE TABLE` y carga; `implementation/data/P503_scopus_relacional/submission/scopus_proptech.db` | La base es binaria; se describe desde el DDL. |
| H05 — Vistas como respuesta | S04, S05 | `implementation/data/P503_scopus_relacional/professor/notebook.ipynb`: celdas `CREATE VIEW`; `implementation/data/P503_scopus_relacional/submission/documents_by_year.csv`, `authors_by_documents.csv`, `sources_by_documents.csv`, `questions.json` | Empates en el corte no examinados. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Caso / dataset | `data/scopus.csv.gz`; `data/search_string.txt` | Export sin fecha ni condiciones de uso; corpus desde 1969. |
| S02 | Representación (normalización) | `professor/notebook.ipynb`: celdas de entidades y relaciones | ID Scopus como identidad; `casefold` sin sinónimos. |
| S03 | Esquema relacional | `professor/notebook.ipynb`: celdas DDL; `submission/scopus_proptech.db` | Seis tablas; reutilizado por P504–P508. |
| S04 | Consultas / vistas | `professor/notebook.ipynb`: celdas `CREATE VIEW` | `LIMIT 20` con desempate alfabético. |
| S05 | Producto | `submission/*.csv`; `submission/questions.json` | Tres preguntas, tres CSV. |
| S06 | Pruebas | `tests/test_activity.py` | Sólo existencia de cinco archivos. |
| S07 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/notebook.ipynb` debe normalizar el export, crear el esquema con integridad referencial, cargar en orden y exportar las vistas.
- **`submission/`:** `scopus_proptech.db`, `documents_by_year.csv`, `authors_by_documents.csv`, `sources_by_documents.csv`, `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige existencia de los cinco archivos; no abre la base, no verifica esquema, claves foráneas, vistas ni contenido. Pasa con los archivos del profesor presentes.
- **Trazabilidad:** `data.C01`–`data.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna entrada; reutiliza el patrón `questions.json` y el uso de SQLite de P501.
- **Habilita para P504–P508:** cada una contiene `data/scopus_proptech.db` del mismo tamaño (540672 bytes) que el persistido aquí y la misma `search_string.txt`; consultan sus tablas `documents`, `authors`, `document_authors`, `sources`, `document_keywords` y `keywords`. La identidad byte a byte de las bases no es verificable desde el volcado.

## Trazabilidad y auditoría

Entrada revisada: P503 → `data.C01`–`data.C05`. C01 (las entidades se derivan de la pregunta por año, autor y fuente), C02 (estructuración y carga), C03 (identidad de autor, faltantes, normalización de palabras clave), C04 (consulta preservada) y C05 (la base sirve a preguntas) tienen evidencia; C03 no incluye evaluar la pertinencia del corpus recuperado. El producto es una representación consultable de un corpus bibliográfico con tres respuestas descriptivas. Pregunta 5: el contenido técnico (DDL, PK/FK, vistas) es el de un taller de bases de datos, pero cada entidad se justifica por la estructura del export y por las preguntas; riesgo moderado, mitigado por la pregunta explícita en el notebook.
