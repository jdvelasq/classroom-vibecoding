# P517 — Propuestas de mejora

**Línea base:** `P517_activity.md` (entrada S02 más reciente: `S02.P517.01`).

## T01 — Aplicar la acción de filtro (`FILTER_ZIPCODE_0`), revalidar y entregar el conjunto preparado con su registro de limpieza

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` p. 5 — «Making data usable includes critical actions applied to the data before it can be used, such as cleaning, harmonizing, transforming, merging/joining and validating data, as well as data quality evaluation»; Task 3.8 «Validate and update the business and analytics problem statements» (Claude, 2026-10-05). Fuente *authoritative*: la evaluación de calidad no termina en diagnóstico sino en datos utilizables y validados.
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` pp. 15–16 — Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» (p. 15); CAP-E.3.8.1 «Identify which finding for univariate data is a quality issue that will result in an update to the analytics problem statement» (p. 16) (Claude, 2026-10-05). Fuente *authoritative* de nivel inicial: el hallazgo de alcance se traduce en una acción sobre los datos y en la población que la pregunta analiza.
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` pp. 13 y 16 — descripción del Dominio III: «Making data usable includes critical actions applied to the data before it can be used, such as cleaning, harmonizing, transforming, merging/joining and validating data, as well as data quality evaluation» (p. 13); CAP-P.3.8.1 «Identify appropriate changes to an analytic problem statement based on multiple observed data findings» (p. 16) (Claude, 2026-10-05). Fuente *authoritative* de nivel intermedio: refuerza la misma expectativa; no añade un requisito distinto.
  - `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` p. 15 — «Validar los datos preparados. Comprobar que los datos sean completos, consistentes, plausibles y adecuados para el análisis» y «Construir el conjunto de datos analítico» (Claude, 2026-10-05). Fuente *literature-derived*: convergencia metodológica sobre revalidar lo preparado.
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` pp. 23–25 — «As you decide upon subsets of data to include or exclude, be sure to document the rationale behind your decisions» (p. 23); «The Data Quality Report prepared during the data understanding phase contains details about the types of problems particular to your data. You can use it as a starting point for data manipulation» y «Reporting your data-cleaning efforts is essential for tracking alterations to the data» (p. 24); «Be sure to note data excluded due to noise» (p. 25) (Claude, 2026-10-05). Fuente *professional-learning*: en CRISP-DM el reporte de calidad (P516) es el punto de partida de la preparación y la exclusión se documenta; la señal se extrajo para P516, pero la acción existe en P517, por eso se integra aquí.
- **Qué gana el estudiante:** cerrar el ciclo diagnóstico → acción →
  revalidación → conjunto apto. Hoy `FILTER_ZIPCODE_0` se nombra pero no se
  aplica (H01; índice externo: «acción nombrada, no aplicada»), y ni P516 ni
  P517 entregan un conjunto preparado (P516 S03 y P517 S04: «sin conjunto
  filtrado»; auditorías de ambas actividades). El estudiante aplicaría la
  acción que el contrato decidió sobre el extracto real, demostraría con la
  misma `validate` que el resultado queda `PASS`, verificaría la
  conservación (filas antes, excluidas y después; clave única; ningún total
  estatal) y persistiría el conjunto junto con un registro de limpieza que
  dice qué regla motivó la exclusión, cuántas filas salieron y por qué. Es
  el producto terminal que `s05-diseno-data.md` asigna al curso («conjunto
  de datos preparado, evaluado y trazable») y que hoy ningún taller del caso
  Vermont entrega; ejerce `data.C02`, hoy ausente en P516 y P517.
- **Anclas actuales:** H01 (acción por alcance), H02 (contrato mínimo de
  seis columnas, que define las columnas del conjunto preparado), H03
  (clasificación y acción), H04 (lotes perturbados, que no cambian);
  superficies S01, S02 (`validate`), S04 (`submission/`) y S05 (pruebas);
  dependencia «Recibe de P516» (reglas y, si se ejecuta P516 T02, la
  definición documentada de `zipcode = 0`).
- **Alternativas menores descartadas:** aclarar que la acción no se aplica
  ya consta en S02 y no cambia el producto. Ubicar el conjunto preparado en
  P516 obligaría a P516 a decidir una acción que todavía no existe allí (el
  diagnóstico de P516 no tiene acciones; la acción nace en `validate` de
  P517) y mezclaría su identidad de reporte de calidad con la preparación;
  por eso la señal CRISP-DM dirigida a P516 se integra aquí. Agregar los seis
  tramos a nivel de código postal sería una segunda transformación que la
  pregunta no exige en este taller; se conserva el grano código postal ×
  tramo (P516 H03) y la agregación queda como decisión del análisis
  posterior.
- **Contrato de no regresión:** se conservan `REQUIRED`, `validate` con sus
  reglas y su orden, los seis lotes de `cases`, `contract_report.csv` con
  sus filas y columnas, y H01–H04. `data/vermont.csv` no se modifica. Se
  añaden una función que aplica la acción, el conjunto preparado y el
  registro de limpieza. La prueba existente se conserva. La acción se aplica
  una vez sobre el extracto real dentro del notebook; no se construye un
  pipeline ni un orquestador (riesgo de identidad hacia ingeniería de datos
  registrado por S02).
- **Interacciones:** con T02, dependen en el orden: el filtro compara
  `zipcode` con el centinela, de modo que debe usar la representación que
  T02 declare; si se aprueban ambas, ejecutar T02 primero y escribir el
  conjunto preparado con `zipcode` como texto. Si sólo se aprueba T01, el
  filtro usa la representación actual. Desde P516 (dependencia P516 → P517):
  la columna `reason` del registro cita la definición documentada de
  `zipcode = 0` si P516 T02 fue ejecutada; si no, la declara como
  interpretación no verificada tomada del comentario del notebook. Si P516
  T01 fue ejecutada, el registro puede citar la severidad de la regla de
  alcance. Capacidad: cambio moderado (una función, dos artefactos, una
  prueba); con T02, P517 pasa de 4 a 5–6 highlights y sigue siendo un solo
  notebook.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo (o H01
  modificado) en el que la acción `FILTER_ZIPCODE_0` decidida por `validate`
  sobre el extracto real se aplica, el resultado se revalida con la misma
  `validate` y queda `PASS`, y se persisten
  `submission/vermont_zipcode_prepared.csv` (columnas de `REQUIRED`, grano
  `zipcode` × `agi_stub`, sin filas de total estatal, clave única) y
  `submission/cleaning_log.csv` (columnas `rule_name`, `action`,
  `rows_before`, `rows_removed`, `rows_after`, `reason`,
  `revalidation_status`, `change_type`); una celda muestra la conservación
  de filas; una prueba verifica ambos artefactos y su coherencia. H01–H04 y
  `contract_report.csv` siguen presentes sin cambios.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P517_vermont_contratos/

0. Inspecciona primero professor/notebook.ipynb (REQUIRED, validate, cases),
   data/vermont.csv, submission/contract_report.csv y tests/test_activity.py.
   Anota qué devuelve validate (orden y nombres de status, change_type y
   action) y cuántas filas tienen zipcode = 0. Si la implementación no
   coincide con design/courses/data/P517_activity.md (acción nombrada y no
   aplicada; sin conjunto filtrado persistido), detente e informa sin
   modificar nada. Si validate sobre el extracto real no devuelve
   FILTER_ZIPCODE_0, detente e informa.
1. No cambies REQUIRED, validate, cases ni contract_report.csv, ni modifiques
   data/vermont.csv.
2. Si T02 de este archivo está aprobada, ejecútala antes que esta T01.
3. Añade una sección «Aplicar la acción y revalidar»:
   a. Define apply_action(frame, action): para FILTER_ZIPCODE_0 devuelve las
      filas cuyo zipcode no es el centinela (usa la representación vigente
      de zipcode); para ACCEPT devuelve el frame; para REJECT no devuelve un
      conjunto. Sin otras acciones.
   b. Aplica validate al extracto real, aplica la acción devuelta, conserva
      sólo las columnas de REQUIRED y vuelve a aplicar validate al
      resultado. Si la revalidación no es PASS, detente e informa.
   c. Muestra una tabla de conservación: filas antes, excluidas y después;
      número de filas con zipcode centinela en el resultado (debe ser 0);
      duplicados de (zipcode, agi_stub) (debe ser 0).
4. Persiste submission/vermont_zipcode_prepared.csv (columnas de REQUIRED,
   una fila por zipcode × agi_stub). Si zipcode es texto, escríbelo y léelo
   con dtype str para conservar el cero inicial.
5. Persiste submission/cleaning_log.csv con columnas: rule_name, action,
   rows_before, rows_removed, rows_after, reason, revalidation_status,
   change_type. En reason, cita la definición documentada de zipcode = 0 si
   P516 T02 está ejecutada (source_card.json de P516 o su registro en
   P516_log.md); si no, escribe que es una interpretación no verificada
   tomada del comentario del notebook. No inventes procedencia.
6. Añade 2–4 líneas de markdown sobre por qué excluir el total estatal cambia
   la población de la pregunta y por qué la exclusión se registra.
7. Añade a tests/ una prueba que verifique: el CSV preparado existe, tiene
   las columnas de REQUIRED, ninguna fila con el centinela y (zipcode,
   agi_stub) única; cleaning_log.csv tiene las columnas del paso 5,
   revalidation_status PASS y rows_before - rows_removed == rows_after ==
   filas del CSV preparado. Lee zipcode con dtype str si T02 está ejecutada.
   No elimines pruebas existentes.
8. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
9. No modifiques otras actividades (en particular P516), traceability.yaml
   ni design/.
```

## T02 — Declarar en el contrato mínimo el tipo y la forma de `zipcode` (código categórico con cero inicial, distinto del centinela 0)

- **Estado:** pendiente de discusión
- **Tipo:** método (contrato)
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` p. 128 — «zip codes identify different postal zones; they do not imply order. If the zip codes are stored in a numeric column, it will be interpreted as a numerical attribute»; la conversión a texto debe «retain the leading 0»; y al preparar los datos «Pay special attention to such items as phone numbers, zip codes, and dates» (Claude, 2026-10-05). Fuente *professional-learning*: señal de práctica sobre tipificar identificadores codificados; el contexto de minería de datos no se traslada.
- **Qué gana el estudiante:** entender que un identificador codificado es
  categórico y que su representación es parte del contrato que protege la
  pregunta. Hoy el contrato de P517 protege una pregunta «por código
  postal», pero no declara tipos (índice externo: «Sin tipos ni nulidad
  declarados»; límite de H02: «No se verifican tipos de las columnas
  requeridas») y la llave de la pregunta se compara como número
  (`zipcode = 0`). Los códigos postales de Vermont empiezan por `05`; una
  representación numérica pierde el cero inicial y deja en la misma columna
  un centinela de agregación (`0`) y códigos reales. Con la forma declarada
  (texto de cinco dígitos o el centinela documentado) y una rama de
  contrato que la verifica, el estudiante ve que un lote donde el código
  cambió de forma (`05001` → `5001`) es un cambio `BREAKING` para cualquier
  integración por código postal, aunque las seis columnas estén presentes.
- **Anclas actuales:** H02 (contrato mínimo derivado de la pregunta), H03
  (clasificación de cambios: la nueva rama es `BREAKING`/`REJECT`), H04
  (lotes perturbados: se añade un lote); superficies S01 (cómo está
  almacenado `zipcode`), S02 (`validate`), S03 (`cases`), S04
  (`contract_report.csv`) y S05; relación con P516 H03 (clave compuesta) y
  H01 (centinela de alcance).
- **Alternativas menores descartadas:** aclarar en markdown que `zipcode` es
  categórico no lo verifica el contrato ni cambia ninguna decisión por lote.
  Declarar tipos y nulidad de las seis columnas sería un esquema completo
  más propio de ingeniería de datos; la propuesta se limita a la columna que
  define la unidad de análisis. Si el paso 0 encuentra que `zipcode` ya se
  lee y valida como texto de cinco caracteres, la propuesta se reduce a
  hacerlo visible (nivel 1).
- **Contrato de no regresión:** se conservan `REQUIRED`, las reglas y el
  orden de `validate` (la nueva regla se inserta entre las de `BREAKING`,
  antes de la regla de alcance), los seis lotes actuales con su decisión,
  las columnas de `contract_report.csv` y H01–H04. Las decisiones de los
  lotes existentes no cambian; el reporte gana una fila. `data/vermont.csv`
  no se modifica. La prueba existente se conserva.
- **Interacciones:** con T01, T02 va primero: el filtro de T01 y el CSV
  preparado deben usar la representación declarada aquí. Con P516
  (dependencia P516 → P517): si se ejecuta P516 T02, su diccionario declara
  el tipo y la forma de `zipcode`; ambos deben coincidir, y si no coinciden
  S04 se detiene e informa. Capacidad: cambio local (lectura, una regla, un
  lote, una prueba).
- **Criterio de aceptación:** S05 encuentra H02 modificado (o un highlight
  nuevo) en el que el contrato declara que `zipcode` se lee como texto y
  que cada valor es el centinela de total estatal o un código de cinco
  dígitos; `validate` verifica esa forma y clasifica su violación como
  `FAIL`/`BREAKING`/`REJECT`; `cases` incluye un lote con `zipcode`
  convertido a número (sin cero inicial) que produce `REJECT`; los seis
  lotes anteriores mantienen su decisión; una prueba verifica la fila nueva
  de `contract_report.csv`.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P517_vermont_contratos/

0. Inspecciona primero cómo está almacenado zipcode en data/vermont.csv
   (lee las primeras líneas como texto crudo, sin pandas: ¿los códigos
   tienen cinco dígitos con cero inicial, p. ej. 05001, o aparecen como
   5001?; ¿cómo aparece el total estatal: 0, 00000 u otro?) y cómo lo lee
   professor/notebook.ipynb (dtype resultante y cómo compara el centinela).
   Inspecciona también validate, cases, submission/contract_report.csv y
   tests/. Luego:
   - Si la implementación no coincide con
     design/courses/data/P517_activity.md, detente e informa sin modificar
     nada.
   - Si zipcode ya se lee como texto y validate ya verifica su forma,
     detente e informa: la propuesta se reduce a hacerlo visible y requiere
     confirmación del profesor.
   - Si el archivo crudo almacena los códigos sin cero inicial, detente e
     informa: normalizarlos sería una transformación que debe decidir el
     profesor (registrada en P517_log.md) antes de continuar.
   - Si P516 T02 está ejecutada y su data_dictionary.csv declara otra forma
     para zipcode, detente e informa la discrepancia.
1. No modifiques data/vermont.csv, REQUIRED, las reglas existentes ni los
   seis lotes de cases.
2. Lee el extracto con dtype={"zipcode": str} y ajusta las comparaciones del
   centinela a la forma observada en el paso 0 (por ejemplo, "0"). Verifica
   que las decisiones de los seis lotes actuales no cambian; si cambian,
   detente e informa.
3. Declara junto a REQUIRED la forma esperada de zipcode (centinela
   documentado o exactamente cinco dígitos) y añade a validate una regla que
   la verifique, ubicada con las reglas BREAKING y antes de la regla de
   alcance; su violación devuelve FAIL / BREAKING / REJECT.
4. Añade a cases un lote zipcode_numeric: el extracto con zipcode convertido
   a entero y de vuelta a texto (pierde el cero inicial). Persiste su fila en
   submission/contract_report.csv con las columnas actuales.
5. Añade 2–4 líneas de markdown: por qué un código postal es categórico, por
   qué su forma es parte del contrato y por qué el centinela no debe
   confundirse con un código real.
6. Añade a tests/ una prueba que verifique que contract_report.csv tiene la
   fila zipcode_numeric con action REJECT y que las filas anteriores
   conservan su action. No elimines pruebas existentes.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades (en particular P516), traceability.yaml
   ni design/.
```
