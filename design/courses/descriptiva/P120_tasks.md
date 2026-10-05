# P120 — Propuestas de mejora

**Línea base:** `P120_activity.md` (entrada S02 más reciente: `S02.P120.01`).

## T01 — Encuadrar las preguntas: decisión, destinatario, supuestos y alcance en `questions.json`

- **Estado:** pendiente de discusión
- **Tipo:** encuadre
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` pp. 4–5 — el encuadre existe para asegurar «that a clear, actionable problem is defined before seeking solutions» (p. 4); Task 2.1 «Reformulate the statement of the business problem (question) as an analytics problem statement» y Task 2.3 «State the set of assumptions related to the analytics problem» (p. 5): la pregunta analítica se deriva de un problema de negocio y declara sus supuestos (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general, no un formato de archivo.
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` pp. 7, 8, 10 y 11 — en el nivel de entrada: CAP-E.1.2.2 «Identify stakeholders and bystanders» (p. 7), CAP-E.1.4.1 «Identify the part of a business statement that is unclear» (p. 8), CAP-E.2.1.2 «Identify if the statement is a business problem, analytics problem, both, or neither» (p. 10) y CAP-E.2.3.1–2.3.3 (supuestos explícitos, «aspects of the business problem that have been simplified», «the constraints that should be documented in an analytics problem statement», p. 11): un analista principiante separa problema de negocio y problema analítico y declara supuestos y simplificaciones (Claude, 2026-10-04). Fuente *authoritative*.
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` pp. 7, 9 y 10 — CAP-P.1.2.1 «Identify the primary and secondary stakeholders» (p. 7), CAP-P.1.6.1 «identify the proposed elements that are in or out of scope of the business problem (question) statement» (p. 9) y CAP-P.2.1.1 «Identify the aspect of a business problem that makes it an analytics problem» (p. 10): destinatario y alcance forman parte del enunciado (Claude, 2026-10-04). Fuente *authoritative*.
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
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 39, 44 y 47 — un flujo de trabajo eficaz incluye «drawing appropriate conclusions, and communicating results» (p. 39); «it is important for students to study confounding and causal inference early to make sense of the data around them» (p. 44); los estudiantes deben «construct effective visual displays and compelling written summaries» (p. 47): el límite causal se aprende pronto, no al final (Claude, 2026-10-04). Fuente *authoritative*.
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

## T03 — Leer el ranking de segmentos contra la tasa base y su incertidumbre antes de priorizar

- **Estado:** pendiente de discusión
- **Tipo:** método
- **Fuentes:**
  - `design/benchmarks-md/institutional/cambridge-business-analytics.md` pp. 6–7 — el módulo «Análisis descriptivo» («Sé capaz de recopilar, limpiar y describir los datos que tienes», p. 6) incluye «Tamaño del efecto e intervalos de confianza» junto a las estadísticas descriptivas (p. 7): la incertidumbre de una medida forma parte de describirla (Claude, 2026-10-04). Fuente *institutional*: ilustra que otra institución sitúa el intervalo dentro de lo descriptivo; no impone el método.
- **Qué gana el estudiante:** antes de priorizar por tasa, pregunta cuánto
  se aparta cada segmento de la tasa global y si esa distancia se distingue
  del ruido con el volumen que tiene. Corrige un defecto: `return_risk.csv`
  ordena combinaciones categoría–canal por tasa (Home & Garden — Mobile App,
  0,5758, primero) con un único resguardo de volumen (H06), y la tasa global
  por órdenes es 0,516 (H04). Las tasas por categoría difieren alrededor de
  un punto (0,512–0,522 en `category_summary.csv`). Con celdas del orden de
  50–100 órdenes, el semiancho aproximado de un intervalo al 95 % para una
  proporción cercana a 0,5 es de unos 0,10–0,14, mayor que la distancia
  entre el primer segmento y la base (≈ 0,06). El ranking por tasa puede ser
  ruido, y el taller hoy lo presenta como señal de riesgo. Con la diferencia
  frente a la base y una banda por segmento, el estudiante declara cuándo
  el orden no se distingue del ruido, y entiende por qué la prioridad por
  valor devuelto (H07) es la lectura más defendible del producto. También da
  un criterio explícito a la pregunta de medios de pago (S05).
- **Anclas actuales:** H04 (tasa global en `kpi_summary.csv`), H06 (umbral
  de 50 órdenes y matriz; evidencia «no se evalúa si las diferencias son
  estables»), H07 (riesgo vs prioridad); superficies S02 («tasas sin
  incertidumbre»), S03 (segmentación, umbral y priorización), S05 (criterio
  de medios de pago) y S06 (pruebas); índice externo «Sin intervalos ni
  pruebas de diferencia».
- **Alternativas menores descartadas:** declarar en markdown que las tasas
  son parecidas no permite al estudiante comprobar cuándo dejan de serlo.
  Subir el umbral de volumen reduce el ruido pero no lo muestra, y con 1.000
  órdenes dejaría pocas celdas. Una prueba de hipótesis formal por pares o
  un ajuste por comparaciones múltiples desplazaría el taller hacia
  Estadística; aquí basta una banda de lectura por segmento frente a una
  sola referencia.
- **Contrato de no regresión:** se conservan H01–H08, el umbral de 50
  órdenes, la matriz categoría × canal, la priorización por valor devuelto
  y los nueve CSV con su esquema y valores; `return_risk.csv` no cambia, de
  modo que su prueba de recomputación sigue intacta. Se añade
  `submission/segment_baseline_comparison.csv`. La única modificación
  admitida a una prueba existente es ampliar la lista esperada de archivos
  del test de conjunto exacto (sin quitar ninguno).
- **Interacciones:** T03 alimenta la evidencia de T02 (criterio de
  «requiere investigación» y límite de incertidumbre); conviene ejecutarla
  antes que T02. Refuerza el supuesto del umbral que T01 declara. No
  compite con ninguna.
- **Capacidad del taller (las tres propuestas):** P120 tiene ocho
  highlights y es el primer caso descriptivo completo tras P100–P109. T01,
  T02 y T03 añaden tres secciones breves (encuadre al inicio, banda de
  lectura en la segmentación, conclusiones al final), sin cambiar caso,
  datos ni tablas. Aun así, conviene decidir en la discusión si T03 o la
  redacción de T02 quedan como sección final que un grupo lento completa en
  la sesión siguiente. P120 es además la plantilla que P121 y P122 repiten
  (preguntas, KPI, matriz, top N con umbral). Aprobar estas propuestas no
  modifica P121 ni P122; su propagación, si se quiere, serían propuestas
  separadas por actividad, que deberían evaluar el caso propio de cada una
  (por ejemplo, en P121 los umbrales de 25.000 vuelos hacen el ruido mucho
  menor).
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que,
  para cada combinación categoría–canal de `return_risk.csv` y cada medio de
  pago, se persiste órdenes, tasa de devolución por órdenes, tasa base
  global, diferencia frente a la base, intervalo aproximado al 95 % y una
  marca de si el intervalo excluye la base; y una lectura en markdown dice
  explícitamente si el orden del ranking por tasa se distingue del ruido y
  qué implica para H07. Debe estar respaldado por notebook,
  `submission/segment_baseline_comparison.csv` y una prueba que lo
  recompute desde `data/sales.csv`. H01–H08 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P120_retail_sales/

0. Inspecciona primero professor/notebook.ipynb, data/sales.csv,
   submission/kpi_summary.csv, return_risk.csv, payment_summary.csv,
   category_summary.csv y tests/. Si la implementación no coincide con
   design/courses/descriptiva/P120_activity.md o ya reporta intervalos o
   diferencias frente a la tasa base, detente e informa. Comprueba si la
   tasa de return_risk.csv es por órdenes (media de IsReturned) o por
   valor; esta tarea usa la tasa por órdenes. Registra el número de órdenes
   de las celdas de return_risk.csv; si todas tienen varios cientos de
   órdenes o más y las diferencias con la base superan claramente sus
   intervalos, detente e informa: el defecto no estaría presente.
1. No cambies return_risk.csv, payment_summary.csv, su cálculo, el umbral
   de 50 órdenes ni priority_segments.csv.
2. Después de la sección de return_risk, añade «Tasa base e incertidumbre»:
   a. Toma la tasa base de return_rate_by_orders (kpi_summary).
   b. Para cada combinación categoría–canal que pasa el umbral y para cada
      medio de pago, calcula desde data/sales.csv: orders, returned_orders,
      return_rate, base_rate, diff_vs_base = return_rate − base_rate, y un
      intervalo de Wilson al 95 % (ci_lower, ci_upper). Usa
      statsmodels.stats.proportion.proportion_confint(method="wilson") si
      statsmodels está en el requirements.txt raíz; si no, implementa la
      fórmula de Wilson con numpy. No añadas dependencias.
   c. differs_from_base = True si base_rate queda fuera de
      [ci_lower, ci_upper].
   d. Grafica, por segmento ordenado por tasa, el punto y su intervalo con
      una línea vertical en la tasa base (Plotly, como el resto del
      notebook).
   e. Explica en markdown, en 4–6 líneas: cuántos segmentos se distinguen
      de la base; si el primer segmento por tasa se distingue de los
      siguientes o el orden puede ser ruido; que la banda es una lectura
      aproximada, no una prueba entre todos los pares; y por qué eso hace
      más defendible priorizar por valor devuelto (H07).
3. Persiste submission/segment_baseline_comparison.csv con columnas
   dimension (category_channel | payment_method), segment, orders,
   returned_orders, return_rate, base_rate, diff_vs_base, ci_lower,
   ci_upper, differs_from_base, ordenado por dimension y return_rate
   descendente.
4. Añade a tests/ una prueba que recompute el archivo desde data/sales.csv
   con la misma preparación que ya usan las pruebas existentes, compare con
   assert_frame_equal (tolerancia numérica), y verifique que
   ci_lower ≤ return_rate ≤ ci_upper y que todas las celdas tienen al menos
   50 órdenes. Amplía la lista esperada de archivos del test de conjunto
   exacto con segment_baseline_comparison.csv sin quitar ninguno, e informa
   ese cambio. No elimines pruebas existentes.
5. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
6. No modifiques otras actividades (P121 y P122 incluidas, aunque repitan la
   plantilla), traceability.yaml ni design/.
```
