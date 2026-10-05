# P507 — Ranking anual de palabras clave con funciones de ventana

## Actividad actual implementada

**Implementación:** `implementation/data/P507_scopus_sql_analitico/`.

### Preguntas analíticas actuales

- ¿Qué palabras clave están entre las diez más frecuentes por año desde 2020?

Usa `data/scopus_proptech.db` (mismo tamaño que la base de P503) y `data/search_string.txt`. `professor/notebook.ipynb` abre con «Un ranking temporal permite detectar los temas que ganan relevancia en el corpus», dibuja el camino `document_keywords → documents` / `keywords`, y ejecuta una consulta con dos CTE: `keyword_years` (documentos distintos por año y palabra clave desde 2020) y `ranked_keywords` (`ROW_NUMBER() OVER (PARTITION BY publication_year ORDER BY document_count DESC, keyword)`), filtrando `rank_in_year <= 10`. Persiste `top_keywords_by_year.csv` (71 líneas: 70 filas, compatible con diez por año entre 2020 y 2026) y `questions.json`. En 2020, «proptech» ocupa el puesto 1 con 7 documentos y los puestos 2–5 visibles («blockchain», «fintech», «real estate», «technology») tienen 2 documentos cada uno. El notebook del estudiante no tiene celdas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** qué temas son más frecuentes cada año; el comentario inicial apunta a «temas que ganan relevancia», pero no hay usuario ni decisión.
- **Producto terminal:** tabla de las diez palabras clave más frecuentes por año, reutilizable por una visualización (según el notebook).
- **Uso y límite:** permite comparar la composición temática año a año. Con conteos bajos, el puesto dentro de los empates lo decide el orden alfabético; las palabras de la cadena de búsqueda aparecen como temas; variantes y sinónimos no se unifican más allá del `casefold` de P503. No sustenta afirmaciones de crecimiento: no se comparan años ni se normaliza por volumen anual.
- **Disciplinas contribuyentes:** SQL con funciones de ventana; bibliometría (co-palabras) como dominio.

### Highlights de contribución

- **H01 — Ordena dentro de cada año con una función de ventana:** `ROW_NUMBER() OVER (PARTITION BY publication_year ORDER BY document_count DESC, keyword)` asigna un puesto por partición sobre el conteo de `keyword_years`, y la consulta externa filtra los diez primeros. Primera función de ventana del curso; reutiliza el patrón de CTE de P506. Sin este hito, un «top N por grupo» exigiría consultas por año o procesamiento fuera de SQL.
- **H02 — Expone cómo las palabras clave de autor condicionan el ranking (caso y datos):** las palabras clave son texto libre de autor, normalizado sólo con `strip` y `casefold` en P503. En el resultado, el término de búsqueda «proptech» encabeza 2020 y los siguientes puestos tienen 2 documentos cada uno, de modo que `ROW_NUMBER` con desempate por `keyword` ordena los empates alfabéticamente: el puesto no distingue frecuencia en ese tramo. Sin este hito, el ranking se leería como jerarquía temática. Límite: el notebook no examina empates, términos de búsqueda ni sinónimos; la observación se apoya en el CSV persistido.

### Inventario técnico de implementación

- **Introduce:** `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)`; filtro sobre un rango calculado en una CTE.
- **Reutiliza:** CTE encadenadas (P506), filtro `publication_year >= 2020` (P504), tabla puente `document_keywords` construida en P503 y hasta ahora no consultada.
- **Reutiliza:** exportación a CSV y `questions.json`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Top N por grupo con ventana | H01 | `ROW_NUMBER` particionado por año | Sin `RANK`/`DENSE_RANK`; empates rotos alfabéticamente. |
| Palabras clave de autor como dato temático | H02 | `document_keywords` normalizadas con `casefold` | Sin sinónimos; términos de búsqueda incluidos. |
| Ranking anual persistido | H01, H02 | `top_keywords_by_year.csv` (70 filas) | Conteos bajos; no compara años. |

### Relación técnica con actividades anteriores

Mismo corpus con nueva entidad (palabra clave) y nuevo método (función de ventana) al servicio de una descripción temporal. Es la primera actividad que usa `document_keywords` y `keywords`. El join con `keywords` es redundante para el resultado (la palabra ya está en `document_keywords`). No se observa duplicación con P503–P506.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Ventana por año | S02, S03 | `implementation/data/P507_scopus_sql_analitico/professor/notebook.ipynb` (consulta `keyword_rankings`); `implementation/data/P507_scopus_sql_analitico/submission/top_keywords_by_year.csv` | Sólo se ven las primeras filas en el volcado. |
| H02 — Palabras clave de autor y empates (caso y datos) | S01, S02, S03 | `implementation/data/P507_scopus_sql_analitico/submission/top_keywords_by_year.csv`; `implementation/data/P503_scopus_relacional/professor/notebook.ipynb` (normalización de `keyword`); `implementation/data/P507_scopus_sql_analitico/data/search_string.txt` | Empates observados en 2020; otros años no visibles. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset / representación de palabras clave | `data/scopus_proptech.db` (tablas `document_keywords`, `keywords` creadas en P503) | Sólo `casefold`; términos de búsqueda presentes. |
| S02 | Consulta | `professor/notebook.ipynb` | `ROW_NUMBER`, top 10, desde 2020. |
| S03 | Producto | `submission/top_keywords_by_year.csv`; `submission/questions.json` | 70 filas. |
| S04 | Pruebas | `tests/test_activity.py` | Sólo existencia de dos archivos. |
| S05 | Interfaz del estudiante | `notebooks/notebook.ipynb` | Notebook sin celdas. |

### Contrato de evidencia actual

- **Notebook o código:** `professor/notebook.ipynb` debe contar documentos por año y palabra clave, ordenarlos por partición y conservar los diez primeros.
- **`submission/`:** `top_keywords_by_year.csv` (año, palabra, documentos, puesto) y `questions.json`.
- **Pruebas:** `tests/test_activity.py::test_01_submission_contains_required_artifacts` sólo exige existencia; no verifica la ventana, el corte ni el contenido.
- **Trazabilidad:** `data.C01`, `data.C02`, `data.C03`, `data.C05`.

### Dependencias en la secuencia

- **Recibe de P503–P506:** tablas de palabras clave (P503), filtro desde 2020 (P504), CTE encadenadas (P506).
- **Habilita para Pyyy:** no evidenciada; el notebook menciona una visualización o dashboard que no existe en P508.

## Trazabilidad y auditoría

Entrada revisada: P507 → `data.C01`, `data.C02`, `data.C03`, `data.C05`. C01, C02 y C05 tienen evidencia. `data.C03` no se evidencia en la actividad: no se evalúan empates, términos de búsqueda ni variantes de palabras clave, aunque condicionan la lectura del ranking; vacío a escalar. El producto es una descripción temática anual del corpus, sin usuario. Pregunta 5: el nombre «sql_analitico» designa funciones de ventana (terminología de SQL), no el producto; la actividad podría describirse como lección de *window functions* si no se hace explícita la limitación del dato. Riesgo de identidad moderado.
