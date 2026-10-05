# P516 — Propuestas de mejora

**Línea base:** `P516_activity.md` (entrada S02 más reciente: `S02.P516.02`).

## T01 — Declarar una severidad por regla de calidad y derivar el estado del reporte de severidad × hallazgos

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia (corrección de defecto)
- **Fuentes:**
  - `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` p. 4 — tabla «Severidad | Acción requerida»: «Error | Detención del pipeline», «Alerta | Investigación de la falla», «Informativa | Ser consciente de la información»; cada regla de calidad lleva una severidad que determina la respuesta a sus hallazgos (Claude, 2026-10-05). Fuente *literature-derived*: aporta el mecanismo severidad → acción; el contexto de pipeline no se traslada al taller.
- **Qué gana el estudiante:** un reporte de calidad que dice la verdad sobre
  la aptitud del extracto. Hoy el estado se asigna con una regla que sólo
  puede producir `REVIEW` para la regla de alcance: cualquier otra regla con
  hallazgos > 0 (clave duplicada, `agi_stub` fuera de 1–6, `N1` negativo,
  columna faltante) quedaría en `PASS` (S02.P516.02; límite de H02 y S02).
  Con una severidad declarada en cada regla y el estado derivado de
  severidad × `finding_count`, el estudiante distingue «la fuente no puede
  responder la pregunta» (error) de «la responde tras una acción» (alerta,
  el total estatal) y de «hallazgo que conviene conocer» (informativa), y
  entiende que el estado es una decisión explícita sobre la regla, no una
  excepción codificada para un nombre.
- **Anclas actuales:** H02 (reglas nombradas con dimensión y conteo), H01
  (regla de alcance `statewide_total_requires_filter`), H03 (clave y
  dominio, que pasan a ser reglas de severidad error); superficies S02
  (reglas en `professor/notebook.ipynb`), S03 (`quality_report.csv`) y S04
  (pruebas); dependencia «Habilita para P517».
- **Alternativas menores descartadas:** aclarar en markdown que el estado
  sólo reacciona a la regla de alcance deja el reporte afirmando `PASS` en
  casos que no lo son; el defecto está en el producto, no en su
  explicación. Corregir la condición sin declarar severidades (por ejemplo,
  «toda regla con hallazgos es `REVIEW`») borra la diferencia entre un
  error que invalida el extracto y una acción de alcance, que es justamente
  el contraste de H01.
- **Contrato de no regresión:** se conservan las cinco reglas, sus nombres,
  dimensiones y conteos, la clave (`zipcode`, `agi_stub`), el diagnóstico
  sin filtrado (filtrar corresponde a P517) y las columnas actuales de
  `quality_report.csv`; sólo se añade la columna `severity` y el estado se
  deriva de ella. Con los datos actuales el reporte sigue siendo 4 `PASS` y
  1 `REVIEW`. H01–H03 siguen presentes. La prueba existente se conserva. No
  se introduce orquestación ni vocabulario de pipeline: la severidad expresa
  qué significa el hallazgo para la pregunta por código postal (riesgo de
  identidad hacia ingeniería de datos registrado por S02).
- **Interacciones:** con T02, se refuerzan: si T02 añade alguna regla sobre
  la medida de ingreso a partir del perfil, esa regla declara su severidad
  con el mecanismo de T01; si se aprueban ambas, ejecutar T01 primero.
  Hacia P517: las severidades propuestas reproducen la clasificación que
  P517 ya usa en `validate` (error ↔ `BREAKING`/`REJECT`; alerta ↔
  `SCOPE`/`FILTER_ZIPCODE_0`); P517 podría reutilizarlas en vez de
  redefinirlas, pero eso no forma parte de esta T01 ni modifica P517.
  Capacidad: cambio local de una tupla y una regla de estado; carga baja.
- **Criterio de aceptación:** S05 encuentra H02 modificado (o un highlight
  nuevo) en el que cada regla declara `severity` (`error`, `alert` o
  `info`) y el estado se deriva de severidad × hallazgos (`PASS` si no hay
  hallazgos; `FAIL` para error, `REVIEW` para alerta, `INFO` para
  informativa cuando los hay); una celda de evidencia muestra que una copia
  perturbada del extracto (una fila duplicada) produce `FAIL` en la regla de
  clave sin tocar `data/vermont.csv`; `quality_report.csv` conserva sus
  filas y columnas con `severity` añadida; una prueba verifica que el estado
  de cada fila es consistente con su severidad y su conteo y que la regla de
  alcance queda en `REVIEW`.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P516_vermont_calidad/

0. Inspecciona primero professor/notebook.ipynb (celdas 2 y 3),
   data/vermont.csv, submission/quality_report.csv y tests/test_activity.py.
   Anota los nombres exactos de las cinco reglas y de las columnas del
   reporte, y la expresión que asigna el estado. Si la implementación no
   coincide con design/courses/data/P516_activity.md (cinco reglas, estado
   que sólo puede ser REVIEW para la regla de alcance), detente e informa
   sin modificar nada. Si el estado ya se deriva de una severidad declarada,
   detente e informa: la propuesta estaría cubierta.
1. No cambies las reglas, sus nombres, dimensiones ni conteos, ni filtres el
   extracto.
2. Extiende cada tupla de regla con una severidad: error para columnas
   requeridas, dominio de agi_stub, unicidad de (zipcode, agi_stub) y N1 no
   negativo; alert para el total estatal. Si el profesor fijó otra
   asignación en la discusión de esta T01 (registrada en P516_log.md), usa
   esa.
3. Sustituye la asignación de estado por una función explícita:
   finding_count == 0 -> PASS; si no, error -> FAIL, alert -> REVIEW,
   info -> INFO. Añade 2–4 líneas de markdown que expliquen qué decisión
   sobre la pregunta por código postal implica cada estado.
4. Añade una celda de evidencia que aplique las mismas reglas a una copia del
   DataFrame con una fila duplicada y muestre el reporte resultante (la regla
   de clave debe quedar FAIL). No persistas esa copia ni toques
   data/vermont.csv.
5. Persiste submission/quality_report.csv con las columnas actuales más
   severity (orden: las existentes, con severity antes de status). Con los
   datos actuales deben quedar 4 PASS y 1 REVIEW.
6. Añade a tests/ una prueba que lea quality_report.csv y verifique: existe
   la columna severity con valores en {error, alert, info}; para cada fila,
   status es PASS si finding_count == 0 y, si no, el estado que corresponde a
   su severidad; la regla de alcance tiene severity alert y status REVIEW.
   No elimines pruebas existentes.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades (en particular P517), traceability.yaml
   ni design/.
```

## T02 — Ficha de procedencia y diccionario del extracto: fuente verificada, significado de `zipcode = 0` y de las variables usadas (incluido el perfil de la variable de ingreso), con la evidencia del diagnóstico de aptitud

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia + caso/datos
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` p. 5 — Task 3.2 «Identify and analyze data sources, including data structures» y Task 3.7 «Document and report data findings»; «Understanding the use of data inventory and documentation is incorporated in this Domain to ensure repeatable processes» (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general de documentar la fuente junto con los hallazgos.
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` pp. 14–16 — CAP-E.3.2.1 «Identify limitations and possible constraints of data, given its attributes, context, and metadata» y CAP-E.3.2.3 «Identify the source of the data» (p. 14); CAP-E.3.6.2 «Identify patterns and characteristics of a univariate dataset with data profiling outputs» (p. 15); CAP-E.3.7.1 «Identify findings in a report about data sets that may affect analysis» (p. 16) (Claude, 2026-10-05). Fuente *authoritative* de nivel inicial: sostiene procedencia, metadatos y perfil univariado de la medida.
  - `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` p. 6 — el reporte de recolección «should describe procedures followed to collect the data, hurdles faced with data collection, data format, dataset size, how the data is stored, characteristics of the data» y el de preparación describe «procedures followed to verify the quality of the data» (Claude, 2026-10-05). Fuente *institutional*: ilustra la descripción de la fuente como entregable junto a la verificación de calidad.
  - `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` p. 13 — «Documentar los datos. Registrar fuentes, significado, procedencia, limitaciones y condiciones de uso» (Claude, 2026-10-05). Fuente *literature-derived*: convergencia metodológica, no formato prescrito.
- **Qué gana el estudiante:** apoyar el diagnóstico de aptitud en la
  documentación de la fuente y no en un comentario. Hoy la decisión central
  del taller (excluir `zipcode = 0` porque es el total estatal) «sólo lo
  afirma un comentario» (límite de H01), el extracto no tiene procedencia,
  año ni diccionario (S01), y la pregunta es sobre «ingresos» sin que se
  sepa qué miden `N1` ni `A00100` ni se examine la variable de ingreso
  (ninguna de las cinco reglas toca `A00100`; S02.P516.02: «no perfila el
  extracto»). Con una ficha de procedencia verificada, un diccionario breve
  de las variables que la pregunta usa (`zipcode`, `agi_stub`, `N1`,
  `A00100`, más `STATE`/`STATEFIPS` si se citan) y un perfil univariado de
  `N1` y `A00100` por `agi_stub`, el estudiante (1) distingue una regla
  respaldada por la definición de la fuente de una supuesta, (2) contrasta
  el significado documentado de `zipcode = 0` con evidencia interna del
  propio archivo y (3) sabe qué limita la conclusión sobre ingresos. Ningún
  taller del curso construye ni usa la procedencia externa de una fuente
  para justificar una regla (P503 H01 conserva una consulta de export;
  P501/P511 reciben manifiestos provistos).
- **Anclas actuales:** H01 (regla de alcance, cuyo fundamento pasa a ser la
  definición documentada), H02 (reporte por regla, al que se suman los
  hallazgos del perfil que afecten la pregunta), H03 (clave y unidad de
  análisis, que el diccionario hace explícita); superficies S01
  (`data/vermont.csv`, «sin procedencia, año ni diccionario»), S02, S03
  (`submission/`) y S04; dependencia «Habilita para P517».
- **Condición de caso (bloqueante):** el origen real del extracto no está
  documentado en la actividad. Es plausible que provenga de las estadísticas
  por código postal del programa Statistics of Income del IRS, pero eso no
  está verificado y no debe afirmarse. El profesor debe confirmar la fuente,
  el publicador, el año fiscal, la documentación oficial que define
  `zipcode = 0`, `agi_stub`, `N1` y `A00100` (incluida la unidad monetaria)
  y las condiciones de uso y redistribución en clase, y registrarlo en
  `P516_log.md` antes de S04. Sin esa verificación, las instrucciones se
  detienen. Si la fuente no es verificable, la alternativa reducida
  (declarar en el reporte la interpretación de `zipcode = 0` como supuesto
  no verificado, con la evidencia interna del paso 4) requiere una
  aprobación explícita y distinta del profesor.
- **Alternativas menores descartadas:** aclarar en markdown que
  `zipcode = 0` «probablemente» es el total estatal no cambia lo que el
  estudiante hace antes de decidir. Un diccionario sin fuente verificada
  reproduciría el problema (significados afirmados, no documentados).
  Perfilar las 147 columnas contradice el contrato mínimo derivado de la
  pregunta (P517 H02) y es propio de Descriptiva; por eso el perfil se
  limita a las dos medidas que la pregunta necesita.
- **Contrato de no regresión:** se conservan la pregunta, las cinco reglas
  (con T01, sus severidades), la clave (`zipcode`, `agi_stub`), el
  diagnóstico sin filtrado, `data/vermont.csv` sin modificar y
  `quality_report.csv` con su esquema (más `severity` si T01 se ejecuta).
  H01–H03 siguen presentes; H01 se refuerza citando la definición
  documentada. La ficha y el diccionario son evidencia del diagnóstico, no
  un inventario de datos de la organización ni un plan de gestión de datos.
  Las pruebas existentes se conservan.
- **Interacciones:** con T01, se refuerzan; si el perfil revela un hallazgo
  que afecta la pregunta (por ejemplo, valores negativos o faltantes en
  `A00100`), se añade como regla con severidad declarada según T01, y no se
  añaden reglas por catálogo; ejecutar T01 primero. Hacia P517 (dependencia
  P516 → P517): P517 reutiliza `vermont.csv` y no tiene procedencia (P517
  S01); la ficha y el diccionario de P516 son la referencia que P517 T01
  cita para justificar la exclusión de `zipcode = 0` en su registro de
  limpieza, y el diccionario debe declarar el tipo y la forma de `zipcode`
  de modo coherente con P517 T02. Si la fuente verificada indica un año
  distinto del `source_release="2017"` inventado en P517, se registra la
  discrepancia; esta T02 no modifica P517. Capacidad: es la propuesta más
  pesada de P516; para no exceder el taller, la verificación documental la
  hace el profesor antes de clase (material en `professor/` o enlace
  citado) y el tiempo de taller se dedica a contrastar la definición con el
  archivo y a leer el perfil de ingreso. Con T01 y T02, P516 pasa de 3 a 5
  highlights; conviene decidir en la discusión si el perfil queda como
  sección final que un grupo lento completa en la sesión siguiente.
- **Criterio de aceptación:** S05 encuentra (1) un highlight nuevo de
  procedencia y significado: `submission/source_card.json` con la fuente,
  publicador, año fiscal, granularidad, definición documental de
  `zipcode = 0` y de `agi_stub`, condiciones de uso y referencia de
  verificación del profesor, todos tomados de `P516_log.md` y no inventados;
  `submission/data_dictionary.csv` con las variables usadas; y una celda que
  contrasta la definición de `zipcode = 0` con evidencia interna (suma por
  código postal frente a la fila estatal, por `agi_stub`), reportando la
  diferencia sin forzarla a cero; (2) un highlight nuevo con
  `submission/income_profile.csv` (perfil de `N1` y `A00100` por
  `agi_stub`) y 2–4 líneas que digan qué hallazgos limitan la conclusión
  sobre ingresos; (3) la regla de alcance citando la definición documentada;
  (4) pruebas que verifiquen la existencia y las columnas o claves de los
  tres artefactos. H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P516_vermont_calidad/

0. Inspecciona primero professor/notebook.ipynb, data/vermont.csv (cabecera,
   tipos, valores de zipcode y agi_stub, presencia de N1 y A00100),
   submission/ y tests/. Si la implementación no coincide con
   design/courses/data/P516_activity.md, detente e informa sin modificar
   nada. Si ya existen ficha de procedencia o diccionario, detente e
   informa.
1. PROCEDENCIA: no inventes ni infieras la fuente. Usa sólo lo que el
   profesor haya verificado y registrado en P516_log.md en la discusión de
   esta T02: fuente, publicador, año fiscal, documento oficial que define
   zipcode = 0, agi_stub, N1 y A00100 (con unidad), condiciones de uso y
   redistribución. Si ese registro no existe o está incompleto, detente y
   pídelo. No escribas "IRS", "SOI" ni ningún año a partir de suposiciones.
   Si el profesor aprobó explícitamente la alternativa reducida (supuesto no
   verificado), aplica todos los pasos, pero escribe "unverified" en los
   campos de source_card.json y en meaning/unit/source_reference del
   diccionario que no tengan respaldo documental, con verified: false, y
   declara el supuesto como tal en el notebook.
2. Persiste submission/source_card.json con las claves: source, publisher,
   tax_year, granularity, zipcode_0_meaning, agi_stub_definition,
   terms_of_use, verified (true/false), verification_reference. Si el
   material documental del profesor debe acompañar la actividad y no puede
   distribuirse, colócalo en professor/ y cita sólo su referencia.
3. Persiste submission/data_dictionary.csv con columnas: variable, meaning,
   unit, dtype_in_notebook, role_in_question, source_reference. Incluye
   zipcode (declara su tipo y forma tal como se leen: texto o número, con o
   sin cero inicial, y el centinela 0), agi_stub, N1 y A00100, y STATE o
   STATEFIPS sólo si el notebook los usa.
4. EVIDENCIA INTERNA: añade una celda que, para cada agi_stub, compare el N1
   y el A00100 de la fila zipcode = 0 con la suma sobre los códigos postales
   y muestre la diferencia absoluta y relativa en una tabla pequeña. No
   ajustes la regla para que la diferencia sea cero; explica en 2–4 líneas
   qué implica el resultado para la interpretación documentada (una
   diferencia puede deberse a cómo la fuente agrega o suprime códigos
   postales pequeños; sólo afírmalo si la documentación verificada lo dice).
5. PERFIL DE INGRESO: calcula por agi_stub, para N1 y A00100 y sólo sobre
   filas con zipcode distinto de 0: count, missing, zeros, negatives, min,
   median, max. Persiste submission/income_profile.csv con columnas:
   variable, agi_stub, count, missing, zeros, negatives, min, median, max.
   Muestra la tabla y escribe 2–4 líneas sobre qué hallazgos limitan la
   conclusión sobre ingresos.
6. Si el perfil revela un hallazgo que afecta la pregunta, añade a lo sumo
   una regla nueva al reporte (con severidad declarada si T01 está
   implementada). No añadas reglas por catálogo ni cambies las cinco
   existentes. En la regla de alcance, cita en markdown la definición
   documentada de zipcode = 0 (o el supuesto declarado si se aplicó la
   alternativa reducida).
7. Añade a tests/ pruebas que verifiquen: source_card.json existe con las
   claves del paso 2; data_dictionary.csv tiene las columnas del paso 3 e
   incluye zipcode, agi_stub, N1 y A00100; income_profile.csv tiene las
   columnas del paso 5 y filas para N1 y A00100. No elimines pruebas
   existentes.
8. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
9. No modifiques data/vermont.csv, otras actividades (en particular P517),
   traceability.yaml ni design/.
```
