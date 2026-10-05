# Log — P123

## S02.P123.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P123_scopus/` (`data/scopus.csv.gz`, `data/search_string.txt`, `professor/main.py` y `s01`–`s20`, `src/main.py`, `submission/` con dieciséis archivos, `tests/`); P100, P101 y P106 como antecedentes técnicos.
- **Trazabilidad revisada:** P123 → `descriptiva.C01`, `C02`, `C03`, `C05`; coherente, con C05 apoyada en productos persistentes y procedencia parcial.
- **Highlights añadidos:** H01–H08 (consulta persistida, campos multivaluados, normalización, co-ocurrencia, comunidades y red, serie anual completa, pipeline, pruebas). Highlight obligatorio de caso y datos: H02 (documento con listas «;»), con H04 declarando filas/columnas de la matriz.
- **Cambios realizados:** creación de `P123_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** sin notebook de profesor ni de estudiante (`notebooks/` sólo `.gitkeep`); fecha y tamaño de extracción no documentados; dependencia de red en ejecución (GeoJSON); países fuera del GeoJSON se descartan sin registro; reemplazos de palabras clave por subcadena; ruido temático residual en comunidades; la tercera pregunta apunta sólo a `keywords_frequency.csv`; la pregunta de períodos no tiene producto que los distinga; el texto emergente de la red rotula el tamaño escalado como «Frequency»; nombres de autores con ID de Scopus persistidos (datos bibliográficos públicos).
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S07 declaradas; dependencias demostrables de P100/P101/P106 (prácticas) y P120 (`questions.json`); salida no evidenciada.
- **Auditoría de Analytics:** descripción de un campo tecnológico por actor, lugar, tiempo y tema; disciplinas contribuyentes visibles. Auditoría con reserva: usuario y decisión no evidenciados y decisiones analíticas no expuestas en un notebook.

## S03.P123.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - procesamiento de texto (bag-of-words, word-count, TF-IDF, n-gramas, *stop words*, *stemming*; DG-Working with Various Types of Data, p. 71) — marginal: P100 H02 ya fija la unidad textual por reglas de normalización y P123 H02–H03 normaliza vocabularios. Añadir TF-IDF o lematización sería otra técnica para lo mismo.
  - estrategia de búsqueda, «narrowing and broadening», operadores booleanos (DM-Information Retrieval, p. 82); descubrimiento de comunidades (DM-Mining Web Data, p. 81); enmarcar la pregunta y obtener datos (DM-Data Preparation, p. 76) — ya cubierta: P123 H01 (consulta persistida) y H05 (Louvain). Documentar el refinamiento de la cadena sería marginal frente al límite ya registrado (falta de fecha y conteo).
  - calidad del *clustering* (DM-Cluster Analysis, p. 77) — marginal: la falta de modularidad o estabilidad en P123 H05 ya está registrada por S02, y ACM sólo lo enuncia como conocimiento genérico de minería.

## S03.P123.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Folleto que define los siete dominios del INFORMS Analytics Framework (framing de negocio, framing analítico, datos, metodología, desarrollo de modelos, despliegue, gestión del ciclo de vida) con la lista de tareas de cada uno; sin subtareas ni detalle evaluativo (el detalle está en el blueprint CAP-E). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P100_log.md`.
