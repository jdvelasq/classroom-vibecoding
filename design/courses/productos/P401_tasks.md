# P401 — Propuestas de mejora

**Línea base:** `P401_activity.md` (entrada S02 más reciente: `S02.P401.01`).

## T01 — Verificar con pytest que los campos sensibles (`ssn`, `location`) no salen en el producto publicado y justificar la publicación de `name`

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 22, 43, 45 y 50 — entre las consideraciones éticas centrales está «safeguarding the privacy of individuals referenced in the data» (p. 22); «ensuring secure data storage, and protecting confidentiality all require extensive computing skills» (p. 43); «Data subject privacy» figura entre los conceptos de gestión y curaduría de datos (p. 45); y la Rec. 2.4 pide que la ética esté «woven into the data science curriculum from the beginning and throughout» (pp. 22 y 50): la protección de identificadores se practica desde los primeros talleres, no sólo en uno dedicado (Claude, 2026-10-05). Fuente *authoritative*: respalda el principio, no un mecanismo; el mecanismo (prueba sobre el producto) es del curso.
- **Qué gana el estudiante:** que la prueba verifique una propiedad del
  producto publicado, no sólo una suma. Hoy `drivers.csv` trae `ssn` y
  `location`; la transformación sólo propaga `driverId` y `name`, pero «el
  código no declara que la exclusión sea deliberada y el nombre se publica»
  (H03; ambigüedad de `S02.P401.01`). Con el cambio, el estudiante declara
  las columnas publicables como parte del contrato de la transformación,
  escribe una prueba `pytest` que falla si un valor de `ssn` o `location`
  aparece en la salida, y justifica `name` frente a un consumidor nombrado.
  Así ve que una prueba protege también lo que no debe salir del producto.
  P453 (enmascaramiento) llega al final de la secuencia, con otro caso; un
  grupo que no llegue a P453 no ve nunca esta protección en un producto.
  **Materialidad:** fortalece la capacidad del producto en su dimensión de
  uso responsable (`productos.C04`/`C05`) y le da a P401 una contribución
  distinguible de P400 (hoy sólo cambia de marco de pruebas). No resuelve
  la falta de usuario y decisión del total por conductor: sólo la toca a
  través de la justificación de `name`. Si el profesor no aporta un
  consumidor, la propuesta se reduce a una aserción más de `pytest` (pulido
  de herramienta) y no debe ejecutarse.
- **Anclas actuales:** H01 (precondición de columnas), H02 (prueba `pytest`
  con DataFrames mínimos), H03 (dos granularidades y atributo sensible);
  superficies S02 (transformación), S03 (prueba de la transformación), S04
  (producto que publica `name`), S05 (prueba de evaluación); dependencia
  «Recibe de P400».
- **Alternativas menores descartadas:** declarar en un comentario que la
  exclusión es deliberada (nivel 1) no da al estudiante una forma de
  comprobarla ni protege el producto ante un cambio futuro (por ejemplo, un
  `merge` que arrastre todas las columnas de `drivers`). Eliminar `ssn` y
  `location` de `data/` quitaría precisamente la condición del caso que
  motiva la práctica.
- **Contrato de no regresión:** se conservan H01–H03, `data/drivers.csv` y
  `data/timesheet.csv` sin cambios, la lógica de agregar, filtrar y unir, y
  `submission/certified_driver_totals.csv` con sus 32 filas. Se conservan
  `professor/test_main.py::test_01_aggregates_only_certified_drivers` y
  `tests/test_activity.py::test_01`. Sustitución posible: sólo si el
  profesor decide no publicar `name`, la columna sale del CSV y del registro
  esperado en `test_01_aggregates_only_certified_drivers` (se quita la clave
  `name`; el resto de la aserción no cambia).
- **Interacciones:** única propuesta de P401. Fuera de P401: no compite con
  P453; P453 puede citar a P401 como primer antecedente. La revisión de
  `traceability.yaml` (posible `productos.C04`) queda para la discusión; S04
  no la modifica.
- **Criterio de aceptación:** S05 encuentra (1) una constante de columnas
  publicables en `main.py` que la transformación usa para construir la
  salida; (2) una prueba de profesor con un fixture que incluye `ssn` y
  `location` y exige que la salida tenga exactamente las columnas
  publicables; (3) una prueba en `tests/` que falla si alguna columna o algún
  valor de `ssn` o `location` de `data/drivers.csv` aparece en
  `submission/certified_driver_totals.csv`; y (4) la justificación de `name`
  con el consumidor y el uso aprobados por el profesor, no inventados. Un
  highlight modificado (H03) o nuevo lo registra. H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P401_code_testing_pytest/

0. Inspecciona primero data/drivers.csv, data/timesheet.csv,
   professor/main.py, professor/test_main.py, src/main.py,
   submission/certified_driver_totals.csv y tests/test_activity.py. Si la
   implementación no coincide con design/courses/productos/P401_activity.md
   (por ejemplo, si la salida ya excluye name o ya existe una prueba sobre
   columnas sensibles), detente e informa sin modificar nada.
1. CONSUMIDOR Y NAME: no inventes consumidor, uso ni decisión. Usa el texto
   que el profesor haya aprobado en la discusión de esta T01 (registrado en
   P401_log.md): quién consume el total por conductor, para qué, y si
   necesita name o le basta driverId. Si no existe, detente y pídelo.
2. En professor/main.py declara PUBLISHED_COLUMNS (driverId, total_hours,
   total_miles y name sólo si el profesor lo aprobó) y haz que
   build_certified_driver_totals devuelva exactamente esas columnas en ese
   orden. No cambies DRIVER_COLUMNS, TIMESHEET_COLUMNS, la agregación, el
   filtro ni la unión. Añade un docstring breve en la constante con la
   razón: ssn y location no salen del producto; name sale (o no) por el uso
   aprobado en el paso 1.
3. Si el profesor decidió no publicar name, quita sólo la clave name del
   registro esperado en test_01_aggregates_only_certified_drivers. No
   cambies nada más de esa prueba.
4. En professor/test_main.py añade una prueba cuyo fixture de drivers
   incluya ssn y location y que exija list(result.columns) ==
   PUBLISHED_COLUMNS. No elimines pruebas existentes.
5. En tests/test_activity.py añade una prueba que lea data/drivers.csv y
   submission/certified_driver_totals.csv (localizados relativos al archivo
   de prueba, sin depender de la profundidad de la actividad) y falle si
   ssn o location aparecen como columnas, o si cualquier valor de ssn o de
   location de drivers.csv aparece en alguna celda de la salida. No
   elimines test_01.
6. Regenera submission/certified_driver_totals.csv con main.py y verifica
   que conserva las 32 filas.
7. Ejecuta las pruebas de professor/ y de tests/ sin errores.
8. No modifiques data/, otras actividades, traceability.yaml ni design/.
```
