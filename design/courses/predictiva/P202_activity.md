# P202 — Tokenización y representación de abstracts

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P202_tokenizacion/`.

### Preguntas analíticas actuales

- ¿Cómo preparamos abstracts de Scopus para identificar términos distintivos?
- ¿Cómo evitamos que ausencias, fórmulas retóricas y avisos editoriales distorsionen una representación documento–término?

Procesa abstracts comprimidos de Scopus y entrega abstracts procesados,
vocabulario, matriz documento–término dispersa y metadatos. No produce todavía
un clasificador ni una decisión organizacional: su producto terminal es una
representación textual auditable para análisis posterior.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** prepara abstracts para análisis posterior; no clasifica ni apoya una decisión aún.
- **Producto terminal:** corpus procesado, vocabulario, DTM dispersa y metadatos.
- **Uso y límite:** hace visible la representación textual; no prueba semántica ni desempeño predictivo.
- **Disciplinas contribuyentes:** NLP, regex y vectorización sirven a un producto de datos de Analytics.

### Highlights de contribución

- **H01 — Convierte ausencias textuales en una regla de calidad verificable:** mide la
  longitud, identifica el marcador `[no abstract available]` y excluye textos de
  menos de 20 palabras antes de modelar. Sin este hito, la matriz mezclaría
  contenido con marcadores de ausencia.
- **H02 — Deriva una limpieza desde evidencia del corpus:** alinea y ordena las colas
  de abstracts para hacer visibles avisos editoriales repetitivos, formula una
  expresión regular y verifica el efecto tras removerla. Sin este hito, se
  aceptarían reglas opacas que pueden borrar contenido.
- **H03 — Distingue expresiones que se preservan de fórmulas que se eliminan:** une
  conectores de varias palabras con guiones bajos, pero marca y remueve fórmulas
  retóricas como `this study`. Sin ello, el vectorizador fragmentaría expresiones
  útiles o sobrerrepresentaría la retórica del abstract.
- **H04 — Hace visibles las transformaciones léxicas:** tokeniza, conserva tokens
  alfabéticos —incluidos los compuestos con guion bajo—, elimina *stopwords* y
  lematiza sin alterar los conectores unidos. Frente a P201, aquí construye las
  *features* desde texto crudo; sin este hito no se puede auditar qué término
  llegó a la matriz.
- **H05 — Construye una matriz documento–término con un umbral declarado:** usa
  `CountVectorizer(min_df=2)` y frecuencia documental, transformando abstracts
  en una matriz dispersa de 385 documentos y 2,806 términos. Sin ella P203 no
  recibiría entradas numéricas reproducibles.
- **H06 — Persiste tanto la matriz como su explicación:** guarda textos procesados,
  vocabulario, matriz `.npz` y metadatos de exclusiones, avisos retirados y
  umbrales. Sin este hito, la representación no podría inspeccionarse ni
  reproducirse independientemente del notebook.

### Inventario técnico de implementación

- **Introduce:** inspección de contenido textual, reglas de calidad y
  normalización antes de extraer características.
- **Introduce:** expresiones regulares, marcadores de frases, tokenización,
  filtrado alfabético, *stopwords* y lematización selectiva.
- **Introduce:** `CountVectorizer`, frecuencia documental y matriz dispersa
  documento–término con umbral `min_df=2`.
- **Extiende:** persistencia de P200–P201 mediante datos procesados, vocabulario,
  matriz y metadatos.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo/dato/producto observable | Límite |
| --- | --- | --- | --- |
| Calidad y limpieza | H01–H04 | Ausencias, regex, conectores, tokens/lemmas | Reglas curadas para inglés/corpus. |
| DTM trazable | H05–H06 | `CountVectorizer`, matriz, vocabulario y metadatos | No predice ni evalúa semántica. |

### Relación técnica con actividades anteriores

P202 no repite la clasificación de dígitos de P201 ni la regresión de P200.
Introduce un problema distinto: construir características desde texto crudo y
mantener trazabilidad de las decisiones que afectan el vocabulario. Es
preparatoria para P203, pero se sostiene como producto de datos: sin P202 se
perdería la explicación reproducible que conecta abstracts crudos con una matriz
apta para modelar.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Regla de calidad para ausencias y textos breves | S01 | `implementation/predictiva/P202_tokenizacion/professor/notebook.ipynb`: `minimum_abstract_words`, marcadores y filtros; `implementation/predictiva/P202_tokenizacion/submission/matrix_metadata.json` | El umbral de 20 palabras es una decisión del taller; no se justifica como universal. |
| H02 — Limpieza de avisos basada en evidencia | S01, S02 | `implementation/predictiva/P202_tokenizacion/professor/notebook.ipynb`: `print_aligned_text_tails`, `copyright_pattern` y reemplazo | El patrón puede no cubrir todas las licencias ni todos los formatos editoriales. |
| H03 — Preservación de conectores y remoción de retórica | S02 | `implementation/predictiva/P202_tokenizacion/professor/notebook.ipynb`: `selected_connectors`, `rhetorical_scaffolding` y marcadores con `_` | La distinción es curada para este corpus y requiere revisión si cambia el dominio. |
| H04 — Tokenización y lematización auditables | S02 | `implementation/predictiva/P202_tokenizacion/professor/notebook.ipynb`: `word_tokenize`, filtro alfabético, `ENGLISH_STOP_WORDS` y `WordNetLemmatizer` | El proceso está diseñado para inglés; no valida calidad lingüística en otros idiomas. |
| H05 — Matriz documento–término declarada | S02 | `implementation/predictiva/P202_tokenizacion/professor/notebook.ipynb`: `CountVectorizer(min_df=2)`; `implementation/predictiva/P202_tokenizacion/submission/document_term_matrix.npz`; `implementation/predictiva/P202_tokenizacion/submission/vocabulary.csv` | Frecuencia documental no expresa por sí sola relevancia temática ni semántica. |
| H06 — Persistencia de representación y decisiones | S03 | `implementation/predictiva/P202_tokenizacion/submission/tokenized_abstracts.csv`; `implementation/predictiva/P202_tokenizacion/submission/matrix_metadata.json`; `implementation/predictiva/P202_tokenizacion/submission/vocabulary.csv`; `implementation/predictiva/P202_tokenizacion/submission/document_term_matrix.npz`; `implementation/predictiva/P202_tokenizacion/tests/test_activity.py` | Las pruebas verifican existencia, no consistencia dimensional ni semántica de los artefactos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Corpus, calidad y normalización | `data/scopus_abstracts.csv.gz`; notebook | Está diseñado para abstracts en inglés y reglas explícitas del corpus. |
| S02 | Representación léxica | Notebook; vocabulario y matriz | `min_df=2`, *stopwords* y lematización definen el espacio de términos. |
| S03 | Producto y verificación | `submission/`; pruebas; trazabilidad | Pruebas sólo exigen artefactos; la matriz no es aún una predicción. |

### Contrato de evidencia actual

- **Notebook o código:** filtra, normaliza, tokeniza, lematiza y vectoriza.
- **`submission/`:** conserva textos procesados, vocabulario, matriz y
  metadatos de parámetros y exclusiones.
- **Pruebas:** verifican los cuatro archivos, no contenidos ni dimensiones.
- **Trazabilidad:** P202 mapea únicamente `predictiva.C02`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna representación textual previa demostrable.
- **Habilita para P203:** vocabulario y el contrato de convertir texto crudo en
  características numéricas auditables.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

La entrada P202 de `implementation/predictiva/traceability.yaml` mapea
`predictiva.C02`. El producto es una representación textual trazable para una
pregunta analítica posterior; procesamiento de lenguaje, regex y vectorización
sirven a ese producto de Analytics. No se debe inferir que esta actividad
entrene, evalúe o despliegue un modelo predictivo.
