# P105 — Propuestas de mejora

**Línea base:** `P105_activity.md` (entrada S02 más reciente: `S02.P105.01`).

## T01 — Minimizar los datos que se comparten con el asistente y verificar su respuesta contra el resultado de P103

- **Estado:** pendiente de discusión
- **Tipo:** método/evidencia (corrige un defecto real)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 22 y 138 — entre las consideraciones éticas centrales están «validating the data’s accuracy» y «safeguarding the privacy of individuals referenced in the data» (p. 22), y el juramento propuesto incluye «I will respect the privacy of my data subjects» (p. 138): compartir datos de personas exige minimizarlos y lo producido debe validarse (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general de privacidad y validación, no un procedimiento con asistentes.
- **Qué gana el estudiante:** pasa de redactar *prompts* a usar un
  asistente con dos salvaguardas que hoy faltan. Primero, decide qué datos
  pueden salir hacia un servicio externo: P105 modela compartir
  `drivers.csv` con `ssn` y `location` (S01; límite de H03), campos que
  P102 H02 enseñó a excluir. La actividad enseña así, de forma implícita,
  una práctica insegura que contradice la secuencia. Segundo, comprueba lo
  que el asistente devuelve: hoy «nada se ejecuta», no hay respuestas
  registradas ni contraste con P103 (S02–S03) y la prueba sólo exige una
  celda (S04). Con el resultado de P103 como referencia conocida, el
  estudiante registra la respuesta, la ejecuta localmente y verifica si
  reproduce el resumen; la salvaguarda «No inventes datos» (H03) pasa de
  ser una instrucción a ser una verificación.
- **Anclas actuales:** H01 (*prompts* emparejados con código de
  referencia), H02 (estructura del dataset trasladada al *prompt*), H03
  (salvaguarda frente a datos inventados); superficies S01 (dataset
  compartido), S02 (*prompts* y código), S03 (producto y persistencia), S04
  (pruebas), S05 (interfaz de estudiante); dependencias «Recibe de P103» y,
  en la secuencia, P102 H02 (minimización de `ssn` y `location`).
- **Alternativas menores descartadas:** añadir sólo una advertencia sobre
  `ssn` y `location` corrige el texto pero deja el producto sin evidencia
  de que el análisis se obtuvo y es correcto, que es el límite central de
  la auditoría S02. Verificar sin minimizar mantendría la práctica
  insegura. Ambas partes son la misma corrección: qué entra al asistente y
  qué se acepta de él.
- **Contrato de no regresión:** se conservan los diez *prompts*, su
  emparejamiento con el código de P103 (H01), las condiciones de
  granularidad en el texto (H02) y la restricción «No inventes datos ni
  modifiques las tablas» (H03), a la que se añade la regla de
  minimización. El código de referencia de P103 puede seguir comentado. La
  prueba actual (notebook con al menos una celda) se conserva y se amplía.
  No se cambian `data/` ni la pregunta.
- **Interacciones:** ninguna dentro de P105. Fuera de P105: depende de que
  P103 conserve `summary.csv` como referencia; P103 T01 no lo cambia, así
  que son compatibles. Capacidad: la ejecución con un asistente real añade
  tiempo de taller; conviene decidir en la discusión si el profesor muestra
  una respuesta registrada y los estudiantes repiten sólo la verificación.
- **Criterio de aceptación:** S05 encuentra (1) un highlight nuevo de
  minimización: el notebook comparte con el asistente sólo las columnas
  necesarias o un esquema sin `ssn` ni `location`, lo explica y lo
  persiste en `submission/shared_columns.json`; y (2) un highlight nuevo de
  verificación: la respuesta del asistente queda registrada en el notebook
  con fecha y herramienta, su código se ejecuta y produce
  `submission/summary.csv`, que se compara con el resultado de P103
  recalculado desde `data/`, con las diferencias explicadas si las hay. Las
  pruebas verifican la ausencia de `ssn` y `location` en lo compartido y
  la igualdad del resumen con el recálculo. H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P105_drivers_chatgpt/

0. Inspecciona primero professor/notebook.ipynb, data/drivers.csv,
   data/timesheet.csv, submission/ y tests/test_activity.py, y como
   referencia implementation/descriptiva/P103_drivers_pandas/ (notebook,
   submission/summary.csv y test_02), sin modificarla. Si la implementación
   no coincide con design/courses/descriptiva/P105_activity.md, detente e
   informa la discrepancia sin modificar nada.
1. RESPUESTAS DEL ASISTENTE: no inventes respuestas ni código atribuido al
   asistente. Usa las respuestas que el profesor haya obtenido con los
   prompts minimizados y aprobado en la discusión de esta T01 (registradas
   en P105_log.md o entregadas con la aprobación), con fecha y herramienta.
   Si no existen, detente y pídelas.
2. MINIMIZACIÓN: antes del primer prompt, añade una celda que construya lo
   que se comparte con el asistente: sólo driverId y name de drivers, y las
   columnas de timesheet que el análisis usa (o sólo el esquema y una
   muestra de pocas filas sin identificadores sensibles). Explica en
   markdown (2–4 líneas) por qué ssn y location no salen hacia el
   asistente, en continuidad con P102. Añade esa regla al texto del primer
   prompt, junto a «No inventes datos ni modifiques las tablas», y ajusta
   los prompts que mencionen la tabla completa. No cambies data/.
3. Persiste submission/shared_columns.json con la forma
   {"drivers": [...], "timesheet": [...]} (columnas efectivamente
   compartidas).
4. VERIFICACIÓN: después de los prompts existentes, añade una sección
   «Verificar la respuesta»:
   a. Muestra la respuesta registrada del asistente en markdown y su código
      en una celda ejecutable, sin corregirlo a mano antes de ejecutarlo.
   b. Ejecuta ese código sobre data/ y guarda submission/summary.csv con
      las columnas de P103 (driverId, hours-logged, miles-logged, name).
   c. Recalcula el resumen de P103 desde data/ (groupby, sum, merge) y
      compáralo con pd.testing.assert_frame_equal o una tabla de
      diferencias visible.
   d. Explica en markdown (3–5 líneas) si la respuesta reproduce el
      resultado y, si no, qué paso falló y cómo se corrigió. Si hubo
      corrección, conserva visibles la versión original y la corregida.
5. Añade a tests/test_activity.py pruebas que verifiquen: que
   shared_columns.json existe y no contiene ssn ni location; y que
   submission/summary.csv existe y es igual al recálculo desde data/
   (siguiendo el patrón de test_02 de P103 y el patrón de rutas de las
   pruebas existentes). No elimines la prueba existente.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques otras actividades (en particular P102, P103 y P104),
   traceability.yaml ni design/.
```
