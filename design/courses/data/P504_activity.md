# P504 — Consultas SQL básicas sobre el corpus Scopus de proptech

## Actividad actual implementada

**Implementación:** `implementation/data/P504_scopus_sql_basico/`.

### Preguntas analíticas actuales

- ¿Qué documentos de proptech se publicaron desde 2020?
- ¿Qué tipos de documento componen el resultado de la búsqueda?

Usa `data/scopus_proptech.db` (mismo tamaño que la base persistida en P503) y conserva `data/search_string.txt`. `professor/notebook.ipynb` lista las tablas en `sqlite_master`, muestra diez documentos ordenados por año y título, filtra `publication_year >= 2020` y agrupa por `document_type`. Persiste `documents_recent.csv` (269 líneas con encabezado; los primeros registros son de 2026, uno con título bilingüe coreano-inglés), `documents_by_type.csv` (diez tipos; los cinco primeros: Article 216, Conference paper 82, Book chapter 40, Review 34, Book 20) y `questions.json`. El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** delimitar el subconjunto reciente y la composición documental del corpus; usuario y decisión no evidenciados.
- **Producto terminal:** listado de documentos desde 2020 y distribución por tipo documental.
- **Uso y límite:** permite conocer qué se recupera y de qué tipo antes de contar producción. No evalúa si 2026 es un año completo (no hay fecha de export), no filtra por tipo ni por pertinencia y la lista reciente no es una medida de tendencia.
- **Disciplinas contribuyentes:** SQL (`SELECT`, `WHERE`, `GROUP BY`) sobre SQLite como medio de consulta.

### Highlights de contribución

- **H01 — Inspecciona el esquema antes de formular la primera consulta:** la celda «El esquema delimita qué puede consultarse antes de escribir la primera pregunta» consulta `sqlite_master` y muestra las tablas creadas en P503. Primera vez que el curso consume una base relacional existente en lugar de construirla. Sin este hito, el estudiante consultaría sin verificar qué entidades están disponibles.
- **H02 — Filtra un periodo conservando el grano documento:** `SELECT title, publication_year, document_type ... WHERE publication_year >= 2020 ORDER BY publication_year DESC, title` devuelve una fila por documento sin agregar ni transformar la fuente. Primer filtro SQL del curso. Sin este hito, la secuencia pasaría de la construcción de la base a agregados sin una consulta a nivel de registro.
- **H03 — Hace visible la heterogeneidad documental del corpus (caso y datos):** un resultado de búsqueda Scopus mezcla artículos, ponencias, capítulos, revisiones y libros; `documents_by_type.csv` muestra diez tipos, con artículos como el más frecuente (216) pero no exclusivo. Esa composición condiciona la interpretación de los conteos por año, autor y fuente de P503, P505 y P506, que suman todos los tipos sin distinguirlos. Sin este hito, se contaría «producción científica» como si cada registro fuera equivalente. Límite: la actividad muestra la composición pero ninguna consulta posterior la usa para filtrar.

### Inventario técnico de implementación

- **Introduce:** `SELECT` con proyección, `ORDER BY` con desempate, `LIMIT`, `WHERE` con condición temporal, `GROUP BY` con `COUNT(*)`.
- **Introduce:** consulta del catálogo `sqlite_master`.
- **Reutiliza:** `sqlite3.connect`, `pd.read_sql_query` y `questions.json` (P503).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Inspección de esquema | H01 | `sqlite_master` | Sólo nombres de tablas. |
| Filtro temporal a nivel de registro | H02 | `WHERE publication_year >= 2020` | Incluye 2026 sin fecha de export. |
| Composición del corpus por tipo documental | H03 | `documents_by_type.csv` (diez tipos) | No se usa para filtrar después. |

### Relación técnica con actividades anteriores

Mismo corpus y base de P503 con nuevo método de acceso: consulta SQL directa desde notebook en lugar de construcción y vistas. `GROUP BY` y `ORDER BY ... LIMIT` ya aparecían en las vistas de P503; lo nuevo es el filtro `WHERE`, la consulta a nivel de registro y la dimensión `document_type`. No se observa duplicación de respuestas con P503.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Inspección del esquema | S02 | `implementation/data/P504_scopus_sql_basico/professor/notebook.ipynb` (celda de `sqlite_master`) | El resultado no se persiste. |
| H02 — Filtro de periodo | S02, S03 | `implementation/data/P504_scopus_sql_basico/professor/notebook.ipynb` (celda `documents_recent`); `implementation/data/P504_scopus_sql_basico/submission/documents_recent.csv` | Lista, no tendencia. |
| H03 — Heterogeneidad documental (caso y datos) | S01, S03 | `implementation/data/P504_scopus_sql_basico/submission/documents_by_type.csv`; `implementation/data/P504_scopus_sql_basico/professor/notebook.ipynb` (celda `documents_by_type`) | Sólo se ven cinco de los diez tipos en el volcado. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset | `data/scopus_proptech.db`; `data/search_string.txt` | Copia de la base de P503; sin fecha de export. |
| S02 | Consultas | `professor/notebook.ipynb` | Tres consultas; periodo fijo 2020. |
| S03 | Producto | `submission/documents_recent.csv`; `submission/documents_by_type.csv`; `submission/questions.json` | Dos preguntas. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia de tres archivos. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/notebook.ipynb` debe inspeccionar el esquema, filtrar el periodo y agrupar por tipo.
- **`submission/`:** `documents_recent.csv`, `documents_by_type.csv`, `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige existencia; no verifica el filtro, los conteos ni que se haya consultado la base. Pasa con los archivos del profesor presentes.
- **Trazabilidad:** `data.C02`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P503:** `scopus_proptech.db` (mismo tamaño) y `search_string.txt`.
- **Habilita para Pyyy:** el filtro `publication_year >= 2020` reaparece en P506, P507 y P508 (en P508 como parámetro). No hay dependencia de archivo.

## Trazabilidad y auditoría

Entrada revisada: P504 → `data.C02`, `data.C05`. Ambas tienen evidencia (consulta; SQL como medio de preguntas). H03 aporta evidencia para `data.C03` (composición del corpus que afecta la evidencia), no mapeada; posible vacío a revisar, sin decidirlo aquí. El producto es una delimitación descriptiva del corpus. Pregunta 5: el título y la secuencia «básico» de P504–P507 siguen la progresión interna de un curso de SQL; las preguntas del notebook mantienen un propósito analítico, pero la actividad, aislada, se lee como introducción a `SELECT`/`WHERE`/`GROUP BY`. Riesgo de identidad moderado.
