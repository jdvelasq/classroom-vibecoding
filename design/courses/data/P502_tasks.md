# P502 — Propuestas de mejora

**Línea base:** `P502_activity.md` (entrada S02 más reciente: `S02.P502.02`).

## T01 — Separar en el catálogo la procedencia externa (fuente, versión, condiciones de uso, crédito) del linaje interno

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 22, 40 y 45 — entre las consideraciones éticas, «obtaining permissions to use data, crediting the sources of data properly»; «Students also need to consider the provenance of the data used»; y «Data provenance» y «Record retention policies» entre los conceptos clave de gestión y curaduría de datos, junto con «providing others a very clear understanding of the details of the data that went into a project»: la procedencia de la fuente, sus permisos y su crédito son contenido que todo estudiante debe ejercer (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general, no un formato de catálogo.
- **Qué gana el estudiante:** distinguir dos preguntas que hoy el catálogo
  mezcla o deja sin responder: de dónde viene la fuente y en qué condiciones
  puede usarse (procedencia externa: productor, versión o fecha de obtención,
  condiciones de uso y redistribución, forma de citarla) frente a cómo se
  transformó dentro del curso (linaje interno: fuente → interfaces de P501,
  H03). Hoy P502 sólo documenta el segundo; la fuente aparece con consumidor
  «Privado» sin explicación (H01) y la auditoría S02 registra el vacío
  («no se evalúa […] procedencia externa; vacío a escalar» en `data.C03`).
  Con la extensión, el estudiante puede decir si las métricas de P500–P501
  pueden publicarse, a quién se atribuyen y a qué copia exacta del archivo se
  refiere el catálogo. Ninguna actividad del curso ejerce esta distinción:
  P503 H01 conserva la consulta Scopus, pero «sin fecha ni condiciones de
  uso». Es una extensión local (nivel 2): un artefacto nuevo junto a los
  catálogos, sin cambiar caso, pregunta ni los tres CSV actuales.
- **Anclas actuales:** H01 (inventario con grano, ubicación y consumidor;
  «Privado» sin explicación), H03 (linaje interno con cambio de grano);
  superficies S01 (dataset presente pero no leído), S02 (catálogos
  literales), S04 (producto), S05 (pruebas).
- **Alternativas menores descartadas:** explicar «Privado» en una línea no
  enseña la distinción entre procedencia y linaje ni registra condiciones de
  uso. Añadir columnas de procedencia a `data_catalog.csv` las repetiría
  vacías en las tres interfaces internas y cambiaría su esquema; un artefacto
  separado hace visible la distinción y conserva el esquema actual.
- **Fuera de esta T01 (contexto S02, sin respaldo en esta fuente):** S02
  registra que catálogo y linaje son literales escritos a mano, no derivados
  del código de P501 ni contrastados con él (riesgo de «documentación formal
  desconectada de los datos»). El documento sólo respalda documentar y
  compartir los flujos de trabajo (p. 46, «Documenting and sharing workflows
  enable others to understand how data have been used and refined»), lo que
  P502 H03 ya hace; no respalda derivar el linaje del código. Ese defecto
  queda como contexto para el integrador y no se propone aquí. Esta T01 no
  lo agrava: los hechos de procedencia son externos y no derivables del
  código, y la única parte local (huella y filas del archivo) se calcula
  desde el propio CSV.
- **Contrato de no regresión:** se conservan H01–H03, `data_catalog.csv`,
  `column_catalog.csv` y `lineage.csv` con su contenido y esquema actuales,
  `questions.json` (archivo de respuesta: `lineage.csv`),
  `data/superstore_orders.csv` sin modificar y la prueba existente. El valor
  «Privado» sólo cambia si el profesor lo decide expresamente; si no, su
  significado se explica en el artefacto nuevo.
- **Interacciones:** sin otras `Txx` en P502. Si se aprueba P500 T01, no
  cambia nada aquí: la huella se calcula sobre el mismo archivo, que P500 no
  modifica. P513 tiene un `source_manifest.json` que apunta a una ruta interna
  (`datalabs/commerce/superstore-orders.csv`); eso es linaje interno, no
  procedencia externa, y no sustituye el texto del profesor. Capacidad: un
  artefacto pequeño en un taller de tres highlights sin notebook.
- **Criterio de aceptación:** S05 encuentra (1) `submission/source_provenance.csv`
  con una fila para `superstore_orders` y las columnas explícitas del paso 2,
  cuyos hechos externos coinciden con el texto aprobado por el profesor en la
  discusión de esta T01 y ninguno está vacío o inventado; (2) huella SHA-256 y
  número de filas calculados desde `data/superstore_orders.csv` por
  `professor/main.py`; (3) una frase, en el propio artefacto o en
  `questions.json`, que distinga procedencia externa (`source_provenance.csv`)
  de linaje interno (`lineage.csv`); (4) una prueba que verifique columnas,
  campos no vacíos y que la huella coincide con el archivo. Un highlight nuevo
  (procedencia externa separada del linaje) queda respaldado; H01–H03 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P502_superstore_linaje/

0. Inspecciona primero professor/main.py (build_data_catalog,
   build_column_catalog, build_lineage), data/superstore_orders.csv,
   submission/ y tests/test_activity.py. Si la implementación no coincide con
   design/courses/data/P502_activity.md (catálogos literales, linaje de tres
   aristas, consumidor «Privado» para la fuente), detente e informa sin
   modificar nada.
1. PROCEDENCIA: no inventes ni infieras productor, versión, fecha, licencia,
   condiciones de redistribución ni forma de citar, y no los busques en la web
   ni en otras actividades. Usa sólo el texto que el profesor haya aprobado en
   la discusión de esta T01 (registrado en P502_log.md), incluido el
   significado de «Privado». Si ese texto no existe o le falta alguno de esos
   campos, detente y pídelo.
2. Añade a professor/main.py una función build_source_provenance que persista
   submission/source_provenance.csv con una fila y estas columnas:
   dataset (superstore_orders), producer, obtained_from, version_or_date,
   terms_of_use, redistribution, credit_text, access_note (significado de
   «Privado»), local_path (data/superstore_orders.csv), local_sha256,
   local_rows. Los campos externos vienen del paso 1; local_sha256
   (hashlib.sha256 sobre los bytes del archivo) y local_rows (líneas de
   datos sin encabezado) se calculan leyendo el archivo.
3. Haz visible la distinción: añade a questions.json, sin cambiar la pregunta
   ni el archivo de respuesta existentes, una clave provenance_file con valor
   source_provenance.csv y una frase breve que diga que lineage.csv describe
   transformaciones internas y source_provenance.csv el origen y las
   condiciones de uso de la fuente. Si questions.json tiene un esquema que lo
   impida, pon la frase como columna scope en source_provenance.csv e
   informa.
4. No cambies data_catalog.csv, column_catalog.csv ni lineage.csv. Cambia
   «Privado» sólo si el texto aprobado por el profesor lo pide expresamente.
5. Añade a tests/ una prueba que verifique que source_provenance.csv existe,
   tiene exactamente las columnas del paso 2, ningún campo vacío, y que
   local_sha256 y local_rows coinciden con data/superstore_orders.csv. No
   elimines la prueba existente.
6. Ejecuta professor/main.py y las pruebas de la actividad sin errores, y
   verifica que los tres catálogos existentes no cambiaron.
7. No modifiques otras actividades (P500, P501, P503, P513), traceability.yaml
   ni design/.
```
