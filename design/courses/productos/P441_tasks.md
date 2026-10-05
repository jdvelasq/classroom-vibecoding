# P441 — Propuestas de mejora

**Línea base:** `P441_activity.md` (entrada S02 más reciente: `S02.P441.01`).

## T01 — Registrar cada rechazo como un evento de error por registro y regla, separado de la salida válida

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia + caso/datos
- **Fuentes:**
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` p. 24 — la calidad de datos requiere «a comprehensive system of data quality screens or filters»; «When a data quality screen detects an error, this event is recorded in a special dimensional schema that is available only in the ETL back room», con «an error event fact table whose grain is the individual error event» y un detalle cuyo grano es cada columna que participa en el error: el rechazo tiene grano propio (violación de una regla), distinto del registro, y vive aparte de la salida que se publica (Claude, 2026-10-05). Fuente *authoritative*: respalda el principio (grano del evento de error y separación de la salida), no el esquema dimensional; no se propone construir tablas de hechos.
- **Qué gana el estudiante:** entender que el grano del rechazo es la
  violación (registro × regla), no el registro. Hoy P441 tiene una sola
  regla «codificada dos veces», añade un único `rejection_reason` por
  registro y guarda válidos y cuarentena en el mismo archivo (S02, S03).
  Con el cambio, cada regla es una comprobación nombrada; cada violación
  produce un evento (fila de origen, regla, columna, valor observado) en un
  artefacto propio; la salida válida queda en otro archivo; y un resumen
  cuenta eventos por regla. Un registro que viola dos reglas genera dos
  eventos, y sólo así se puede decir qué comprobación falla más y dónde
  corregir la fuente. No duplica P402: P402 acepta o rechaza un lote entero;
  aquí lo válido pasa y cada violación queda registrada. **Materialidad:**
  depende del caso. Con los dos registros genéricos de `amount` y una sola
  regla actuales, multiplicar reglas y eventos sólo puliría un patrón de
  data engineering (es el riesgo que S02 registra en H02) y no hay nada que
  contar por regla. Fortalece la capacidad analítica (`productos.C03`:
  validar frente al uso operativo) sólo si las reglas son el contrato del
  indicador máquina-día de P402, cuyo consumidor está declarado («equipo de
  operaciones»). Por eso la propuesta incluye ese anclaje y se detiene si el
  profesor no lo aprueba.
- **Anclas actuales:** H01 (cuarentena con motivo; el motivo se generaliza a
  eventos), H02 (caso como límite: «la misma regla sobre
  `daily_units_produced` habría conectado con el caso de fábricas»);
  superficies S01 (registros genéricos), S02 (una regla codificada dos
  veces), S03 (válidos y cuarentena juntos), S04 (pruebas); dependencia
  «Recibe de P402».
- **Alternativas menores descartadas:** añadir un campo de lista de motivos
  al archivo actual (nivel 2) conserva la mezcla de válidos y rechazos y no
  hace visible el grano del evento. Añadir reglas inventadas sobre `amount`
  sería dato y regla por conveniencia, sin uso que las justifique.
- **Contrato de no regresión:** se conservan H01 (lo válido pasa intacto y
  lo inválido no desaparece) y H02 como límite superado; la prueba de
  profesor existente y `tests/test_activity.py::test_01` se conservan.
  Sustituciones explícitas: `data/records.json` deja de ser la entrada de
  `main` y lo reemplaza un extracto derivado de P402 con defectos
  deliberados (generador y fuente limpia en `professor/`, como exige
  `AGENTS.md` para datos sucios); `submission/quarantine.json` conserva su
  nombre pero pasa a contener sólo los registros en cuarentena, mientras la
  salida válida va a un archivo propio. `records.json` se conserva si la
  prueba de profesor lo lee.
- **Interacciones:** única propuesta de P441. Fuera de P441: el resumen por
  regla podría alimentar los indicadores de calidad de P442 o de una
  eventual propuesta de linaje en P443; no es condición de esta T01. No
  modifica P402.
- **Criterio de aceptación:** S05 encuentra (1) reglas nombradas tomadas del
  contrato de P402 y aplicadas una sola vez cada una; (2) un extracto
  derivado documentado con al menos un registro que viola dos reglas; (3)
  `submission/valid_records.csv`, `submission/quarantine.json` (sólo
  rechazados, con sus campos intactos), `submission/error_events.csv` con
  una fila por registro × regla y `submission/error_summary.csv` con
  eventos por regla; y (4) pruebas que verifican que ningún registro válido
  tiene eventos, que todo registro en cuarentena tiene al menos uno, que el
  registro con dos violaciones tiene dos eventos y que los conteos del
  resumen coinciden con los eventos. H01 queda modificado o se añade un
  highlight nuevo.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P441_data_quarantine/
Insumo: implementation/productos/P402_data_testing_pytest_pandas/
        data/machine_throughput_export.csv y professor/ o main.py de P402
        (sólo lectura, para tomar las reglas del contrato)

0. Inspecciona primero data/records.json, professor/main.py,
   professor/test_main.py, src/main.py, submission/quarantine.json y
   tests/test_activity.py, y el contrato de P402 (validate_data). Si la
   implementación de P441 no coincide con
   design/courses/productos/P441_activity.md, o P402 no tiene el extracto o
   las reglas descritas, detente e informa sin modificar nada.
1. CASO: no cambies el caso por iniciativa propia. Procede sólo si el
   profesor aprobó en la discusión de esta T01 (registrado en P441_log.md)
   anclar P441 al extracto máquina-día de P402. Si no existe esa
   aprobación, detente: sobre los registros genéricos de amount la
   propuesta sólo pule un patrón y no debe ejecutarse.
2. Crea professor/build_quarantine_case.py que tome un tramo pequeño del
   extracto de P402 (por ejemplo, 30–50 filas), conserve una copia limpia en
   professor/, añada source_row como identificador e introduzca defectos
   deliberados sobre filas reales: al menos una producción negativa, una
   fecha inválida, una llave de negocio duplicada y un registro con dos
   violaciones a la vez. Escribe data/machine_day_records.csv. El docstring
   declara el origen, qué se alteró y por qué.
3. En professor/main.py:
   a. Declara las reglas de registro del contrato de P402 como
      comprobaciones nombradas, cada una con su columna (identificadores
      positivos, daily_units_produced no negativa, factory_date ISO válida,
      unicidad de factory_id-machine_id-factory_date). La regla de esquema
      es de lote y queda en P402.
   b. Evalúa cada regla una sola vez y produce un evento por violación con
      source_row, rule, column, observed_value.
   c. Persiste submission/valid_records.csv (registros sin eventos, campos
      intactos), submission/quarantine.json (sólo registros con eventos,
      campos intactos), submission/error_events.csv y
      submission/error_summary.csv (rule, events).
   d. Conserva quarantine_invalid_records si la prueba de profesor la usa;
      si su prueba no puede pasar con el nuevo diseño sin modificarla,
      detente e informa: no la borres ni la reescribas.
4. Añade en un docstring de main o en HOW_TO_RUN_ME.txt (créalo si no
   existe) 3–5 líneas: por qué el evento tiene grano registro × regla, por
   qué vive separado de la salida válida y cómo el resumen por regla indica
   dónde corregir la fuente del indicador.
5. En professor/test_main.py añade una prueba con un fixture mínimo donde un
   registro viola dos reglas y produce exactamente dos eventos. En
   tests/test_activity.py (rutas relativas al archivo de prueba) añade una
   prueba que verifique los cuatro artefactos y sus columnas, que ningún
   source_row válido aparece en error_events.csv, que todo source_row en
   cuarentena aparece al menos una vez, y que error_summary.csv coincide con
   el conteo de error_events.csv por regla. No elimines pruebas existentes.
6. Ejecuta el generador una vez, luego main.py y las pruebas de professor/
   y de tests/ sin errores.
7. No modifiques P402 ni otras actividades, traceability.yaml ni design/.
```
