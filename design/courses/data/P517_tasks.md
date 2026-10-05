# P517 — Propuestas de mejora

**Línea base:** `P517_activity.md` (entrada S02 más reciente: `S02.P517.01`).

## T01 — Aplicar la acción de filtro (`FILTER_ZIPCODE_0`), revalidar y entregar el conjunto preparado con su registro de limpieza

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` p. 5 — «Making data usable includes critical actions applied to the data before it can be used, such as cleaning, harmonizing, transforming, merging/joining and validating data, as well as data quality evaluation»; Task 3.8 «Validate and update the business and analytics problem statements» (Claude, 2026-10-05). Fuente *authoritative*: la evaluación de calidad no termina en diagnóstico sino en datos utilizables y validados.
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
