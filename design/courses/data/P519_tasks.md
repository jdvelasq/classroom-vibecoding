# P519 — Propuestas de mejora

**Línea base:** `P519_activity.md` (entrada S02 más reciente: `S02.P519.01`).

## T01 — Minimizar los atributos sensibles del registro de conductores (`ssn`, `location`): elegir los atributos según la pregunta y no distribuir `ssn`, o documentar su presencia y restricción

- **Estado:** pendiente de discusión
- **Tipo:** caso/datos + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` pp. 13 y 15 — «CAP-E.3.1.2 Identify issues related to sensitive data and restricted usage in collecting and using data» y «CAP-E.3.4.2 Identify the risks or ethical implications of acquiring unnecessary or unintended data»: en el nivel inicial, reconocer los datos sensibles y no adquirir datos innecesarios forma parte de la gestión de datos (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general, no un procedimiento.
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` pp. 13 y 15 — «CAP-P.3.4.2 Identify which data is likely to have risks or ethical implications if acquired for the project/program»; el dominio de datos declara que «security, management, and privacy protocols are vital … to ensure compliance, ethical standards, and trust» (Claude, 2026-10-05). Fuente *authoritative*: refuerza CAP-E en el nivel intermedio.
- **Qué gana el estudiante:** corrige un defecto real de lo que el taller
  distribuye y lo convierte en una decisión visible. Hoy `data/drivers.csv`
  entrega 34 filas con `ssn` y `location` junto con `name`, sin uso,
  procedencia ni restricción documentados (P519 S01; H02, límite de
  inferencia), y el taller sólo necesita `driverId` y `name` para la unión de
  H03. El estudiante ve que el maestro se reduce a los atributos que la
  unión requiere, y por qué: un identificador nacional no se copia a un
  extracto de clase sólo porque viene en la fuente. Es la primera vez en el
  curso que la parte «responsable» de `data.C04` se aplica a datos de
  personas. El aporte de aprendizaje es pequeño (una celda); la parte
  principal es la corrección del dato.
- **Anclas actuales:** H02 (extracto legible con llave compartida
  `driverId`), H03 (unión por clave con `combine_driver_hours`, que usa sólo
  `name`); superficies S01 (datasets: «columnas `ssn` y `location`
  presentes»), S03 (producto) y S04 (pruebas); dependencia «Habilita para
  P520 y P521 … usan los mismos `timesheet.csv` y `drivers.csv`».
- **Alternativas menores descartadas:** documentar el defecto sólo en el
  diseño ya está hecho por S02 y no cambia lo que se distribuye. La
  alternativa «documentar la presencia de `ssn` y su restricción sin
  retirarlo» queda como opción del profesor (por ejemplo, si el catálogo
  confirma que los valores son ficticios y la fuente impone conservar el
  archivo íntegro), pero no enseña la selección por finalidad.
- **Contrato de no regresión:** se conservan H01–H04, `timesheet.csv`
  intacto, el extracto de cuatro registros, todos los operadores (que
  P520–P523 copian literalmente) y `submission/operator_walkthrough.csv` con
  sus dos filas actuales (`10, George Vetticaden, 140.0`; `11, Jamie
  Engesser, 133.0`). Las pruebas existentes se mantienen. Sólo cambian las
  columnas de `data/drivers.csv` de P519 (o, en la opción documental, se
  añade la nota de restricción) y se añade una celda markdown. No se
  introduce contenido de privacidad formal ni normativa de otras
  jurisdicciones, y no se agrava el riesgo de identidad hacia ingeniería de
  datos registrado por S02: el cambio refuerza `data.C04`.
- **Interacciones:** no hay otras `Txx` en este archivo. El mismo
  `drivers.csv` está copiado en P521 (S01: «Idénticos a P519; `ssn` y
  `location` presentes sin uso») y, según la dependencia de P519, también en
  P520 (P520_activity sólo documenta `timesheet.csv`; S04 debe comprobarlo).
  Esta T01 queda limitada a la copia de P519 salvo que el profesor decida
  extenderla: si sólo se cambia P519, los archivos dejan de ser idénticos y
  la afirmación «mismos tamaños» de la dependencia debe revisarse en S05;
  P521 no se ve afectado funcionalmente (proyecta sólo `name`), pero
  conserva el defecto y `certified`/`wage-plan`, que una propuesta futura de
  P521 podría querer usar. Extender el cambio a P520/P521 sería una
  decisión registrada en sus logs, no parte de esta ejecución. El curso
  descriptivo usa datos semejantes; queda sólo como mención. Capacidad: una
  celda markdown y una prueba; no compromete el taller.
- **Criterio de aceptación:** S05 encuentra (1) en la opción aprobada por
  defecto, `data/drivers.csv` de P519 sin `ssn` ni `location` (columnas
  `driverId` y `name`, o las que el profesor apruebe), con las mismas 34
  filas y llaves; o, en la opción documental, la nota de presencia y
  restricción aprobada por el profesor; (2) H02 modificado con una celda
  markdown que declara qué atributos del maestro se conservan, cuáles se
  retiraron y por qué, y la procedencia conocida del archivo; (3)
  `operator_walkthrough.csv` idéntico al actual; y (4) una prueba nueva que
  verifica la ausencia de `ssn` en el maestro distribuido (o la presencia de
  la nota). H01–H04 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P519_mapreduce_operators/

0. Inspecciona primero data/drivers.csv, data/timesheet.csv,
   professor/notebook.ipynb, notebooks/notebook.ipynb,
   submission/operator_walkthrough.csv y tests/test_activity.py. Si
   drivers.csv ya no contiene ssn ni location, o si la implementación no
   coincide con design/courses/data/P519_activity.md, detente e informa sin
   modificar nada. Busca también en catalog/ la procedencia del registro de
   conductores; si no aparece, regístralo como no documentada (no la
   inventes).
1. DECISIÓN: usa la opción que el profesor haya aprobado en la discusión de
   esta T01 (registrada en P519_log.md): (A) proyectar el maestro a los
   atributos que la unión necesita, o (B) conservar el archivo y documentar
   la presencia de ssn/location y su restricción de uso. Si no hay decisión
   registrada, o si (B) no trae el texto de la restricción, detente y
   pídelo. No inventes procedencia, licencia ni restricción.
2. Opción A: reescribe data/drivers.csv de P519 con las columnas driverId y
   name (o las que el profesor apruebe), en el mismo orden de filas, sin
   cambiar valores ni llaves. No guardes en la actividad otra copia con
   ssn; si el profesor quiere conservar el original, lo ubica él fuera del
   material distribuido.
   Opción B: no modifiques drivers.csv; añade la nota aprobada en la celda
   del paso 3.
3. En el notebook del profesor, junto a la lectura del maestro (H02), añade
   una celda markdown de 3–5 líneas: qué atributos del maestro usa la unión
   (driverId como llave, name para el registro de salida), qué atributos se
   retiraron o están restringidos (ssn, location) y por qué no se copian a
   un extracto de clase, y la procedencia conocida. Si ayuda, una celda que
   muestre la cabecera del maestro como evidencia visual.
4. Verifica que submission/operator_walkthrough.csv sigue con exactamente
   las dos filas actuales.
5. Añade a tests/ una prueba que verifique que la cabecera de
   data/drivers.csv no contiene ssn ni location (opción A) o que existe la
   nota documental acordada (opción B), resolviendo la raíz de la actividad
   de forma independiente de la profundidad de distribución. No elimines
   pruebas existentes.
6. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
7. No modifiques P520, P521 ni otras actividades (aunque compartan el
   archivo), traceability.yaml ni design/.
```
