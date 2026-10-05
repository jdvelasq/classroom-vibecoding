# P438 — Propuestas de mejora

**Línea base:** `P438_activity.md` (entrada S02 más reciente: `S02.P438.01`).

## T01 — Recalcular en el backfill el indicador del período afectado y conservar el valor publicado junto al recalculado

- **Estado:** pendiente de discusión
- **Tipo:** caso/datos + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` pp. 15 y 23 — al sobrescribir un atributo (tipo 1) «you must be careful that aggregate fact tables and OLAP cubes affected by this change are recomputed» (p. 15); ante cambios retroactivos que llegan tarde, «a new row needs to be inserted in the dimension table, and then the associated fact rows must be restated» (p. 23): una corrección histórica obliga a reexpresar lo derivado de ella (Claude, 2026-10-05). Fuente *authoritative*: respalda el principio (corrección retroactiva ⇒ reexpresión de agregados), no el mecanismo ni un esquema dimensional; no se propone construir dimensiones.
- **Qué gana el estudiante:** ejercer el backfill sobre un indicador real y
  ver su consecuencia para el consumidor. Hoy P438 sólo selecciona
  identificadores en un rango: S02 registra que «no se reprocesa nada: no
  hay cálculo que se rehaga ni resultado que se reemplace», que los eventos
  no tienen contenido y que el taller «se lee como patrón genérico de
  ingeniería de datos». Con el cambio, los registros son filas máquina-día
  del extracto de P402 (`daily_units_produced`, consumidor declarado
  «equipo de operaciones»); un indicador por fábrica y día se publica con
  los datos conocidos en su momento; llegan registros tardíos del período
  (el caso de P437); el backfill recalcula sólo el rango declarado, deja
  intactos los días vecinos y persiste, por fábrica y día, el valor
  publicado y el recalculado. El estudiante aprende que una corrección
  histórica obliga a reexpresar el indicador derivado y a dejar constancia
  de qué cambió y cuánto. **Materialidad:** fortalece la capacidad analítica
  operada (recuperación de un indicador, `productos.C05`), no la práctica de
  una herramienta: sustituye un dato sin contenido por un indicador del
  curso con consumidor declarado.
- **Anclas actuales:** H01 (rango inclusivo; se conserva y pasa a operar
  sobre un cálculo), H02 (alcance registrado; límite «no hay indicador cuyo
  valor cambie al reprocesar»); superficies S01 (tres eventos con fecha),
  S02 (rango literal en `main`), S03 («selección, no resultado
  reprocesado»), S04 (pruebas); dependencia «Recibe de P437» (acción
  `backfill`).
- **Alternativas menores descartadas:** aclarar en el texto que un backfill
  debe recalcular (nivel 1) no da nada que recalcular. Añadir una medida a
  los tres eventos actuales sería inventar datos por conveniencia, contra
  `AGENTS.md`, cuando el curso ya tiene un extracto máquina-día real
  (P402). Es un cambio de caso (nivel 3) porque el dato actual no tiene
  contenido; el mecanismo de rango y su registro no cambian.
- **Contrato de no regresión:** se conservan H01 y H02, `select_backfill`
  con su semántica inclusiva, su prueba de profesor y
  `submission/backfill_selection.json` con sus claves (`start_date`,
  `end_date`, `event_ids`, ahora identificadores de fila del extracto).
  `tests/test_activity.py::test_01` se conserva. Sustitución explícita:
  `data/events.json` deja de ser la entrada de `main` y lo reemplaza un
  extracto derivado de P402 con fechas dentro y fuera del rango, de modo que
  la inclusión de extremos y la exclusión de vecinos siguen ejercitándose
  (evidencia al menos equivalente). `events.json` se conserva si la prueba
  de profesor lo lee. La relación con la idempotencia de P430 se ejerce
  (reejecutar no altera el valor publicado), pero sin artefactos de P430.
- **Interacciones:** única propuesta de P438. Fuera de P438: compite en
  carga con la eventual fusión P436–P438 que S02 dejó a decisión del curso;
  si se fusionan, esta propuesta debe trasladarse a la actividad resultante.
  Reutiliza el extracto de P402 sin modificar P402.
- **Criterio de aceptación:** S05 encuentra (1) un generador en
  `professor/` que deriva el extracto de P402 y documenta origen,
  transformación, qué filas se tratan como tardías y su límite; (2) un
  indicador publicado antes del backfill; (3) un artefacto de reexpresión
  con, por fábrica y día del rango, el valor publicado, el recalculado y la
  diferencia; y (4) una prueba que verifica que sólo cambian días del rango,
  que los vecinos conservan su valor publicado, que la reexpresión coincide
  con la suma del extracto completo y que reejecutar el backfill no altera
  el valor publicado. H01 queda modificado o se añade un highlight nuevo.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P438_backfill/
Insumo: implementation/productos/P402_data_testing_pytest_pandas/
        data/machine_throughput_export.csv (sólo lectura)

0. Inspecciona primero data/events.json, professor/main.py,
   professor/test_main.py, src/main.py, submission/backfill_selection.json
   y tests/test_activity.py, y el extracto de P402 (columnas factory_id,
   machine_id, daily_units_produced, factory_date). Si la implementación de
   P438 no coincide con design/courses/productos/P438_activity.md, o el
   extracto de P402 no existe o no tiene esas columnas, detente e informa
   sin modificar nada.
1. CASO DERIVADO: crea professor/build_backfill_case.py que, a partir del
   extracto de P402:
   a. tome un tramo corto de fechas consecutivas (por ejemplo, 7 días) con
      todas sus fábricas y máquinas, y añada source_row (fila de origen)
      como identificador;
   b. marque como tardías algunas filas de 1–2 días interiores del tramo
      (por ejemplo, una máquina por fábrica) y escriba
      data/records_as_published.csv (sin las tardías) y
      data/late_records.csv (sólo las tardías), ambos con las mismas
      columnas.
   El docstring declara el origen (P402), que el retraso es una
   construcción didáctica sobre filas reales (los valores no se alteran) y
   ese límite. Ejecútalo una vez y conserva los archivos en data/.
2. En professor/main.py:
   a. Conserva select_backfill sin cambiar su semántica. Si su prueba de
      profesor depende de data/events.json, no borres ese archivo.
   b. Calcula el indicador publicado (suma de daily_units_produced por
      factory_id y factory_date) con records_as_published.csv y persístelo
      en submission/published_indicator.csv (factory_id, factory_date,
      units). Si el archivo ya existe, no lo sobrescribas: es lo publicado.
   c. Declara el rango del backfill como los días con filas tardías, une
      registros publicados y tardíos, selecciona con select_backfill las
      filas del rango y recalcula el indicador sólo para esos días.
   d. Persiste submission/backfill_restatement.csv con factory_id,
      factory_date, published_units, restated_units, difference, sólo
      para días del rango, y conserva submission/backfill_selection.json
      con start_date, end_date y event_ids (source_row seleccionados).
3. Añade en un docstring de main o en HOW_TO_RUN_ME.txt (créalo si no
   existe) 3–5 líneas: por qué un dato tardío obliga a reexpresar el
   indicador, por qué se conserva el valor publicado y para quién (el
   «equipo de operaciones» declarado en P402), y que los días fuera del
   rango no se tocan.
4. En tests/test_activity.py (rutas relativas al archivo de prueba) añade
   una prueba que verifique: backfill_restatement.csv tiene esas columnas;
   todas sus fechas están entre start_date y end_date; al menos una fila
   tiene difference != 0; restated_units coincide con la suma de
   records_as_published.csv + late_records.csv para cada fábrica y día;
   published_indicator.csv conserva para los días fuera del rango los
   mismos valores que se obtienen de records_as_published.csv. Añade en
   professor/test_main.py una prueba de que ejecutar el backfill dos veces
   no cambia published_indicator.csv ni backfill_restatement.csv. No
   elimines pruebas existentes.
5. Ejecuta main.py y las pruebas de professor/ y de tests/ sin errores.
6. No modifiques P402 ni otras actividades, traceability.yaml ni design/.
```
