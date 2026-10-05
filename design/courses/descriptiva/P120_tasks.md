# P120 — Propuestas de mejora

**Línea base:** `P120_activity.md` (entrada S02 más reciente: `S02.P120.01`).

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
