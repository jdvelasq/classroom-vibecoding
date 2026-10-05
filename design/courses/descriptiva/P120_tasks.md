# P120 — Propuestas de mejora

**Línea base:** `P120_activity.md` (entrada S02 más reciente: `S02.P120.01`).

## T01 — Encuadrar las preguntas: decisión, destinatario, supuestos y alcance en `questions.json`

- **Estado:** pendiente de discusión
- **Tipo:** encuadre
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` pp. 4–5 — el encuadre existe para asegurar «that a clear, actionable problem is defined before seeking solutions» (p. 4); Task 2.1 «Reformulate the statement of the business problem (question) as an analytics problem statement» y Task 2.3 «State the set of assumptions related to the analytics problem» (p. 5): la pregunta analítica se deriva de un problema de negocio y declara sus supuestos (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general, no un formato de archivo.
- **Qué gana el estudiante:** en el primer caso descriptivo completo, antes
  de cargar datos, aprende a decir para quién es cada pregunta, qué decisión
  apoya su respuesta, qué supuestos del caso condicionan la lectura y qué
  queda fuera de alcance. Hoy `questions.json` sólo empareja `pregunta` y
  `archivo_respuesta` (H01) y la actividad registra «usuario y decisión
  concretos no evidenciados». Los supuestos que fijan el producto existen
  pero no se declaran junto a la pregunta: devolución total por orden (H03),
  umbral de 50 órdenes (H06), período de ocho meses, procedencia no
  documentada (S01). La pregunta «¿qué segmentos priorizar para investigar y
  reducir devoluciones?» se lee sin su frontera: el producto señala dónde
  investigar (H07), no qué causa la devolución ni qué acción tomar. Es la
  dimensión «para quién» de la pregunta descriptiva del curso, que la
  auditoría de identidad echa en falta.
- **Anclas actuales:** H01 (contrato `questions.json`), H03 (supuesto de
  devolución total), H06 (umbral de volumen), H07 (riesgo vs prioridad);
  superficies S01 (dataset y procedencia), S05 (producto/entregable; la
  pregunta de medios de pago no fija criterio) y S06 (pruebas que hoy no
  leen `questions.json`); dependencia «Habilita para P121–P125»
  (`questions.json` reaparece en P123–P125 y P150–P154).
- **Alternativas menores descartadas:** escribir el encuadre sólo en una
  celda markdown no lo hace parte del contrato que enlaza pregunta y
  evidencia, ni lo verifica. Dejarlo a P125 (que ya persiste un límite)
  llega tarde: los grupos que avanzan menos no alcanzan el último caso.
  Crear un archivo de encuadre aparte duplicaría `questions.json`; extender
  el contrato existente es el menor cambio.
- **Contrato de no regresión:** se conservan H01–H08, los nueve CSV con su
  esquema y valores, y `test_01`–`test_06`. `questions.json` conserva sus
  dos preguntas, sus claves `pregunta` y `archivo_respuesta` y sus valores
  actuales; sólo se añaden claves por entrada. Las preguntas intermedias del
  notebook no cambian. No se modifica P121–P125, que tienen su propio
  `questions.json`.
- **Interacciones:** T01 encuadra lo que T02 concluye: el `límite` de cada
  conclusión de T02 debe ser coherente con el `alcance` declarado aquí, y el
  destinatario de T01 es el lector de la respuesta de T02. Si T01 se
  rechaza, T02 sigue siendo ejecutable sobre las preguntas actuales. T01 no
  depende de T03, aunque el supuesto del umbral de 50 órdenes queda mejor
  argumentado si T03 se aprueba.
- **Criterio de aceptación:** S05 encuentra (1) cada entrada de
  `submission/questions.json` con `destinatario` y `decision` tomados del
  texto que aprobó el profesor (registrado en `P120_log.md`), no inventados
  por la herramienta; (2) `supuestos` y `alcance` no vacíos, que mencionen
  al menos la devolución total por orden, el umbral de volumen, el período
  observado y que el producto no identifica causas; (3) una celda markdown
  inicial que presente ese encuadre; y (4) una prueba nueva que verifique la
  estructura de `questions.json` y que cada `archivo_respuesta` exista en
  `submission/`. H01 queda modificado o se añade un highlight de encuadre;
  H02–H08 y las pruebas existentes siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P120_retail_sales/

0. Inspecciona primero professor/notebook.ipynb, data/sales.csv,
   submission/questions.json, submission/*.csv y tests/. Si la
   implementación no coincide con design/courses/descriptiva/P120_activity.md
   (por ejemplo, questions.json no es una lista de entradas con pregunta y
   archivo_respuesta, o no se escribe antes de cargar datos), detente e
   informa la discrepancia sin modificar nada.
1. ENCUADRE DE NEGOCIO: no inventes destinatario ni decisión. Usa el texto
   que el profesor haya aprobado en la discusión de esta T01 (registrado en
   design/courses/descriptiva/P120_log.md). Si no existe, detente y pídelo.
2. Extiende, en la celda que hoy escribe questions.json, cada entrada con
   cuatro claves nuevas, sin cambiar pregunta ni archivo_respuesta:
   - destinatario: texto aprobado por el profesor.
   - decision: texto aprobado por el profesor (qué decide con la respuesta).
   - supuestos: lista de textos con los supuestos del caso que condicionan
     la lectura, tomados de lo que el notebook ya hace: devolución total por
     orden (IsReturned → ReturnedAmount = TotalAmount), una orden = un
     producto, umbral mínimo de 50 órdenes por segmento, período observado
     (calcúlalo del dato, no lo escribas de memoria) y procedencia del
     archivo no documentada.
   - alcance: lista de textos con lo que la respuesta cubre y lo que no:
     señala dónde investigar; no identifica causas de devolución; no prueba
     que un canal o medio de pago provoque devoluciones; no fija acciones.
3. Añade al inicio del notebook una celda markdown que presente, para cada
   pregunta, destinatario, decisión, supuestos y alcance en 4–8 líneas.
4. Añade a tests/ una prueba que lea submission/questions.json y verifique:
   que es una lista con las dos preguntas actuales; que cada entrada tiene
   las claves pregunta, archivo_respuesta, destinatario, decision, supuestos
   y alcance; que los textos y listas no están vacíos; y que cada
   archivo_respuesta existe en submission/. Usa la misma resolución de rutas
   independiente de la profundidad que ya usan tests/conftest.py y
   test_activity.py. No elimines ni modifiques pruebas existentes.
5. Ejecuta el notebook completo y las pruebas de la actividad sin errores;
   confirma que los nueve CSV no cambiaron.
6. No modifiques otras actividades (en particular P121–P125, aunque usen
   questions.json), traceability.yaml ni design/.
```

## T02 — Escribir una conclusión por pregunta con su evidencia y su límite (asociación no es causa)

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 39, 44 y 105 — el graduado debe «explain and interpret the numerical conclusions in the client’s terminology, and deliver text and graphics ready to be digested by non-technical personnel» (p. 39); «Importance of effectively presenting data, models, and inferences to clients in oral, written, and graphical formats» (p. 44); la comunicación incluye «the ability to have a discussion about limitations» (p. 105) (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa de comunicar resultados interpretados con su límite, no el formato.
- **Qué gana el estudiante:** cerrar cada pregunta con una respuesta escrita
  para su destinatario, la evidencia persistida que la sostiene y lo que esa
  evidencia no permite afirmar. Hoy P120 entrega nueve CSV que las pruebas
  recomputan (H08), pero ninguna respuesta. Separa riesgo y prioridad (H07)
  sin escribir qué significa esa diferencia. La pregunta de medios de pago
  no fija qué «requiere investigación» (S05). Además, aunque pregunta qué
  priorizar «para reducir» devoluciones, no declara que un canal o medio de
  pago con más devoluciones no las causa (la trazabilidad registra que «el
  notebook no declara un límite asociación/causalidad»). El patrón
  `pregunta`/`respuesta`/`límite` verificado por prueba existe hoy sólo en
  P125 H06, el último caso del bloque; un grupo que no llega a P125 termina
  sin haber escrito una conclusión ni su frontera causal.
- **Anclas actuales:** H01 (preguntas enlazadas a archivo), H04 (dos tasas
  de devolución), H07 (riesgo vs prioridad), H08 (nueve CSV recomputados);
  superficies S05 (producto/entregable) y S06 (pruebas); dependencia
  «Habilita para P121–P125». En P125, H06 pasaría de primera aparición a
  refuerzo; no se modifica P125.
- **Alternativas menores descartadas:** una celda markdown de lectura no
  queda en el producto ni se verifica, y desaparece al cerrar el notebook.
  Esperar a P125 deja el límite causal fuera del alcance de los grupos
  lentos y lo separa de las preguntas de priorización, que es donde la
  confusión asociación/causa es más probable.
- **Contrato de no regresión:** se conservan H01–H08, los nueve CSV con su
  esquema y valores, y las pruebas de recomputación `test_01`–`test_06`. Se
  añade un archivo `submission/analysis_conclusions.csv`. Como las pruebas
  actuales exigen exactamente nueve CSV, la única modificación admitida a
  una prueba existente es ampliar la lista esperada de archivos con el
  nuevo nombre (sin quitar ninguno); S04 debe informarlo. Ninguna tabla ni
  gráfico se sustituye.
- **Interacciones:** T01 encuadra lo que T02 concluye: cada respuesta se
  dirige al `destinatario` de T01 y su `límite` es coherente con el
  `alcance` declarado. T03 alimenta la evidencia de T02: si T03 se aprueba,
  la respuesta sobre medios de pago y segmentos usa su comparación con la
  tasa base y su intervalo como criterio de «requiere investigación» y dice
  cuándo el orden no se distingue del ruido. Orden de ejecución recomendado:
  T01, T03, T02. Si T03 se rechaza, T02 cita los CSV actuales y su límite
  declara que las tasas se presentan sin incertidumbre. Si T01 se rechaza,
  T02 responde las dos preguntas actuales sin destinatario explícito.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que
  `submission/analysis_conclusions.csv` tiene columnas `pregunta`,
  `respuesta`, `evidencia` y `límite`, una fila por cada pregunta de
  `questions.json`; la `evidencia` cita archivos existentes en
  `submission/` y al menos un valor de ellos; el `límite` declara que la
  asociación observada no identifica la causa de la devolución. Debe estar
  respaldado por una celda del notebook que construye la tabla y por una
  prueba de estructura y de presencia del límite causal, análoga a
  `test_06` de P125. H01–H08 siguen presentes. Si se aprueba, el profesor
  decide aparte si `traceability.yaml` debe mapear P120 a `descriptiva.C04`.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P120_retail_sales/

0. Inspecciona primero professor/notebook.ipynb, submission/questions.json,
   submission/*.csv y tests/. Si la implementación no coincide con
   design/courses/descriptiva/P120_activity.md o ya persiste conclusiones
   escritas, detente e informa. Localiza en tests/test_activity.py la
   aserción del conjunto exacto de CSV; si no existe, no la crees.
1. No cambies los nueve CSV, su cálculo, sus columnas ni las pruebas que
   los recomputan.
2. Si T01 está implementada, usa sus campos destinatario y alcance; si T03
   está implementada, usa submission/segment_baseline_comparison.csv como
   evidencia de segmentos y medios de pago. Si alguna no lo está, no la
   simules.
3. Al final del notebook, añade «Conclusiones»: construye un DataFrame con
   columnas pregunta, respuesta, evidencia y límite, una fila por cada
   pregunta de questions.json (mismo texto de pregunta):
   - respuesta: 2–4 frases para el destinatario; en la pregunta de
     segmentos distingue los que encabezan por valor devuelto de los que
     encabezan por tasa (H07); en la de medios de pago, declara el criterio
     usado para «requiere investigación».
   - evidencia: nombres de archivo de submission/ y los valores que
     sostienen la respuesta, leídos de los CSV (no escritos a mano).
   - límite: debe incluir «no identifica su causa» o «no prueba que … cause»
     referido al canal, la categoría o el medio de pago, más el límite que
     corresponda (devolución total por orden; sin incertidumbre si T03 no
     existe).
   Muestra la tabla y persístela en submission/analysis_conclusions.csv.
4. Añade una celda markdown de 2–4 líneas que explique por qué concentrar
   devoluciones no es provocarlas.
5. Pruebas: añade a tests/ una prueba que verifique que el archivo existe,
   tiene exactamente esas columnas, una fila por pregunta de questions.json
   con el mismo texto, que cada evidencia nombra al menos un archivo
   existente en submission/, y que cada límite contiene «no identifica su
   causa» o «no prueba que». Amplía la lista esperada de archivos del test
   de conjunto exacto con analysis_conclusions.csv sin quitar ninguno, e
   informa ese cambio. No elimines pruebas existentes.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades (P121–P125 incluidas), traceability.yaml
   ni design/.
```
