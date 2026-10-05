# P506 — Producción sostenida de autores con CTE sobre el corpus Scopus

## Actividad actual implementada

**Implementación:** `implementation/data/P506_scopus_sql_avanzado/`.

### Preguntas analíticas actuales

- ¿Qué autores muestran producción sostenida sobre proptech desde 2020?

Usa `data/scopus_proptech.db` (mismo tamaño que la base de P503) y `data/search_string.txt`. `professor/notebook.ipynb` abre con «La producción sostenida permite distinguir autores recurrentes de participaciones aisladas», dibuja `authors ← document_authors → documents` y ejecuta una consulta con dos CTE: `recent_documents` (documentos con `publication_year >= 2020`) y `author_production` (documentos distintos, años activos distintos, primer y último año por autor). Filtra `active_year_count >= 3`. Persiste `sustained_authors.csv` (tres autores: Tagliaro C., 8 documentos, 4 años, 2021–2026; Pomè A.P., 7, 3, 2023–2026; Kassner A.J., 3, 3, 2023–2026) y `questions.json`. El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** distinguir autores recurrentes de participaciones aisladas; usuario y decisión no evidenciados.
- **Producto terminal:** lista de autores que cumplen un criterio operativo de producción sostenida.
- **Uso y límite:** permite identificar continuidad de autoría en el periodo reciente bajo un umbral explícito. El umbral de tres años no se justifica, el periodo incluye 2026 (sin fecha de export) y la identidad de autor depende del ID Scopus; no mide intensidad ni impacto.
- **Disciplinas contribuyentes:** SQL con CTE y agregados múltiples como medio para operacionalizar un concepto.

### Highlights de contribución

- **H01 — Encadena CTE para separar filtro temporal y agregación por autor:** `WITH recent_documents AS (...) , author_production AS (...)` aísla el periodo antes de agregar `COUNT(DISTINCT rd.document_id)`, `COUNT(DISTINCT rd.publication_year)`, `MIN` y `MAX` por `a.author_id`. Primera consulta en varias etapas nombradas del curso; extiende la unión de P505. Sin este hito, filtro y agregación quedarían en una sola consulta difícil de revisar.
- **H02 — Operacionaliza «producción sostenida» como años activos distintos (caso y datos):** en un corpus bibliográfico, un autor puede acumular documentos en un solo año; el criterio usa años distintos con publicación (`active_year_count >= 3`) en lugar del número de documentos, y conserva `first_year` y `last_year` para mostrar la ventana. El resultado muestra la diferencia: Kassner A.J. entra con 3 documentos, mientras autores con 5 documentos en P503/P505 no aparecen. Sin este hito, la continuidad se confundiría con volumen. Límite: el umbral 3 y el inicio 2020 son valores fijos sin justificación persistida; 2026 cuenta como año activo aunque pueda estar incompleto.

### Inventario técnico de implementación

- **Introduce:** CTE múltiples (`WITH ... AS`), `COUNT(DISTINCT publication_year)`, `MIN`/`MAX` de año, filtro posterior sobre agregados en la consulta externa.
- **Reutiliza:** unión `authors`–`document_authors` (P505), filtro `publication_year >= 2020` (P504), exportación a CSV y `questions.json`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Consulta por etapas con CTE | H01 | `recent_documents` → `author_production` | Una sola consulta. |
| Criterio de continuidad temporal | H02 | Años activos distintos ≥ 3 desde 2020 | Umbral sin justificación; 2026 incluido. |
| Lista de autores sostenidos | H02 | `sustained_authors.csv` (3 filas) | Identidad por ID Scopus. |

### Relación técnica con actividades anteriores

Mismo corpus y misma entidad (autor) que P505, con nuevo método (CTE) y nueva exigencia de producto: pasar de un ranking de volumen a un criterio de continuidad. El resultado no duplica el de P505: incorpora una dimensión temporal y excluye autores de alto volumen concentrado. No se observa duplicación.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — CTE encadenadas | S02 | `implementation/data/P506_scopus_sql_avanzado/professor/notebook.ipynb` (consulta `sustained_authors`) | Sin consulta intermedia persistida. |
| H02 — Continuidad como años activos (caso y datos) | S01, S02, S03 | `implementation/data/P506_scopus_sql_avanzado/professor/notebook.ipynb`; `implementation/data/P506_scopus_sql_avanzado/submission/sustained_authors.csv`; contraste: `implementation/data/P505_scopus_sql_intermedio/submission/authors_by_documents.csv` | Contraste por lectura de ambos CSV, no persistido como comparación. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/scopus_proptech.db`; `data/search_string.txt` | Copia de la base de P503; incluye 2026. |
| S02 | Consulta y criterio | `professor/notebook.ipynb` | Umbral 3 años y periodo desde 2020 fijos en SQL. |
| S03 | Producto | `submission/sustained_authors.csv`; `submission/questions.json` | Tres autores. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia de dos archivos. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/notebook.ipynb` debe filtrar el periodo en una CTE, agregar por autor en otra y aplicar el umbral de años activos.
- **`submission/`:** `sustained_authors.csv` (autor, documentos, años activos, primer y último año) y `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige existencia; no verifica el criterio, el umbral ni el contenido.
- **Trazabilidad:** `data.C01`, `data.C02`, `data.C03`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P503–P505:** base y tablas puente (P503), filtro de periodo (P504), unión autor–documento (P505).
- **Habilita para P507:** P507 reutiliza CTE encadenadas y el filtro desde 2020 sobre otra entidad (palabras clave).

## Trazabilidad y auditoría

Entrada revisada: P506 → `data.C01`, `data.C02`, `data.C03`, `data.C05`. C01 tiene evidencia (convertir «sostenida» en un requisito de datos operativo), C02 y C05 también. `data.C03` no se evidencia explícitamente: no se examina la completitud de 2026, la desambiguación de autores ni la sensibilidad del umbral; vacío a escalar. El producto es una descripción de continuidad de autoría bajo un criterio explícito. Pregunta 5: la operacionalización del concepto da propósito analítico a las CTE, pero el nombre «sql_avanzado» encuadra la actividad como paso de un temario de SQL. Riesgo de identidad moderado.
