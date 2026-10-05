# P500 — Propuestas de mejora

**Línea base:** `P500_activity.md` (entrada S02 más reciente: `S02.P500.02`).

## T01 — Hacer verificable el contrato de lectura: codificación correcta y declarada, y faltantes calculados en vez de transcritos

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia (corrección de un defecto)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 64, 71 y 76 — «Describe the internal representation of non-numeric data, such as characters, strings, and images» (CCF-Basic Computer Architecture, T2), la disposición «_Accurate_ in the choice of data type for encoding information» (DG-Working with Various Types of Data) y, en DM-Data Preparation, «Munging data - dealing with errors in data, gaps in data, cleansing data, validating data, profiling data»: la codificación de caracteres es una decisión de representación que debe ser exacta y los vacíos del dato se perfilan y validan, no se suponen (Claude, 2026-10-05). Fuente *authoritative*: respalda una expectativa general, no un procedimiento.
- **Qué gana el estudiante:** aprende que un contrato de lectura sólo vale si
  lo que declara es cierto y comprobable en el propio archivo. Hoy el primer
  contrato del curso enseña lo contrario en dos puntos: (1) `load_sales` lee
  con `encoding="latin1"` un archivo UTF-8 con BOM, quita a mano el prefijo
  `ï»¿` de las columnas y persiste `latin1` en `source_format`, de modo que los
  textos no ASCII quedan mal decodificados (`™` → `â¢`, visible en el
  `sales_detail.csv` de P501); y (2) «Product Base Margin tiene 16 valores
  faltantes» es texto fijo: el código no lo calcula ni lo verifica (H04). Con
  la corrección, el estudiante declara la codificación como parte del formato
  (igual que separador, decimal y fecha en H01), la comprueba sobre un texto
  no ASCII y deriva del archivo los conteos de faltantes que el contrato
  publica, indicando si afectan a las columnas que usan las métricas. Es el
  menor cambio que corrige un defecto real (nivel 2): no cambia pregunta,
  grano, fórmulas ni artefactos.
- **Anclas actuales:** H01 (convención regional y `source_format`), H04
  (compuerta de calidad previa a la salida); H02 sólo en lo que el contrato
  afirma sin comprobar (`Row ID`); superficies S02 (lectura), S03
  (validación), S04 (contrato), S06 (pruebas); dependencia «Habilita para
  P501» (mismo CSV y misma lectura).
- **Alternativas menores descartadas:** corregir sólo el texto del contrato
  (`latin1` → `utf-8-sig`) sin cambiar la lectura dejaría un contrato que no
  describe el código; actualizar el «16» a mano repetiría el defecto en cuanto
  cambie el archivo. Sólo aclarar en el texto que la codificación es incorrecta
  no da al estudiante una forma de comprobarla.
- **Contrato de no regresión:** se conservan H01–H04, la pregunta,
  `data/superstore_orders.csv` sin modificar, el separador `;`, la coma
  decimal, el formato `%d/%m/%y`, el grano línea-de-orden, las cuatro
  aserciones actuales y las cuatro métricas con sus fórmulas.
  `monthly_sales_metrics.csv` y `questions.json` deben quedar idénticos (las
  métricas numéricas no dependen de la codificación). En
  `metric_contract.json` se sustituyen sólo el valor de la codificación y la
  línea fija de faltantes, por valores calculados; las demás claves se
  conservan. La limpieza manual del prefijo `ï»¿` se sustituye por la lectura
  `utf-8-sig`, que lo resuelve en origen (evidencia equivalente: P513 H01 ya
  lee el mismo caso así). La prueba existente se mantiene.
- **Interacciones:** sin otras `Txx` en P500. Fuera de P500: (a) P501 publica
  texto mal decodificado (`Accentâ¢`, P501 H03) a partir de la misma lectura;
  según S02 su `load_sales` es una copia en su propio código, así que esta T01
  **no** corrige P501 ni debe modificarlo: corregir P501 es una actividad y
  una decisión separadas, y hasta entonces P501 seguirá mostrando el defecto.
  (b) P513 H01 se describe como la «primera lectura del CSV fuente de
  Superstore con decodificación UTF-8 correcta» y contrasta con P500; si se
  aprueba esta T01, esa descripción quedará desactualizada en la próxima
  revisión S02 de P513, sin cambio de implementación. Capacidad: cambio
  pequeño en un taller de cuatro highlights sin notebook; no compite con otra
  propuesta.
- **Criterio de aceptación:** S05 encuentra (1) `load_sales` con
  `encoding="utf-8-sig"`, sin la eliminación manual de `ï»¿`, y
  `source_format` del contrato con esa misma codificación; (2) una
  comprobación ejecutable de que ningún nombre de columna conserva el BOM y de
  que los textos no ASCII de `Product Name` no contienen secuencias de
  decodificación errónea (`â`, `Ã`); (3) los conteos de faltantes por columna
  en `metric_contract.json` calculados desde el DataFrame leído, con la
  indicación de si alguna columna con faltantes interviene en las métricas, y
  la línea fija eliminada; (4) pruebas nuevas que recalculan desde el CSV la
  codificación y los faltantes y los comparan con el contrato. H01–H04
  siguen presentes, H01 y H04 modificados para describir lo comprobado.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P500_superstore_metricas/

0. Inspecciona primero professor/main.py (load_sales, build_contract, main),
   data/superstore_orders.csv, submission/ y tests/test_activity.py. Comprueba
   que los tres primeros bytes del CSV son EF BB BF y que el archivo completo
   se decodifica como UTF-8 sin errores. Si no hay BOM, si el archivo no es
   UTF-8 válido o si la implementación no coincide con
   design/courses/data/P500_activity.md (lectura latin1 con limpieza de
   "ï»¿", línea fija de los 16 faltantes), detente e informa sin modificar
   nada. Guarda una copia de submission/monthly_sales_metrics.csv para
   comparar al final.
1. No cambies la pregunta, el grano, las fórmulas, las cuatro aserciones
   existentes, data/ ni src/main.py.
2. CODIFICACIÓN: en load_sales lee con encoding="utf-8-sig" (conserva
   sep=";", decimal="," y el formato de fecha) y elimina la limpieza manual
   del prefijo "ï»¿". En build_contract, source_format debe declarar
   "utf-8-sig" (UTF-8 con BOM). Añade a main, antes de escribir artefactos,
   dos aserciones: ningún nombre de columna empieza por "﻿" o "ï»¿", y
   ningún valor de Product Name contiene "â" ni "Ã". Imprime una fila cuyo
   Product Name tenga un carácter no ASCII (por ejemplo "™") como evidencia
   visible.
3. FALTANTES: calcula df.isna().sum() sobre el DataFrame leído y persiste en
   metric_contract.json, dentro de los controles, un objeto missing_values
   {columna: conteo} con las columnas que tienen faltantes, y una lista
   metric_input_columns con las columnas que usan las métricas (Order Date,
   Order ID, Sales, Profit, o las que el código use realmente). Añade
   missing_affects_metrics = True/False según la intersección. Elimina la
   línea fija «Product Base Margin tiene 16 valores faltantes»; si quieres
   una frase legible, genérala desde el conteo. Si el conteo calculado de
   Product Base Margin no es 16, no lo ajustes: usa el calculado e informa
   la diferencia en tu respuesta.
4. ROW ID: el contrato afirma que «Row ID no es una clave única global».
   Calcula el número de valores repetidos de Row ID y persístelo en los
   controles (row_id_duplicates). Si es 0, no cambies tú la frase del
   grano: termina el resto de pasos e informa la contradicción en tu
   respuesta para que el profesor decida el texto.
5. Ejecuta professor/main.py y verifica que monthly_sales_metrics.csv es
   idéntico a la copia del paso 0 y que questions.json no cambió.
6. Añade a tests/ pruebas que: (a) lean data/superstore_orders.csv con
   encoding="utf-8-sig" y comprueben que source_format del contrato declara
   esa codificación; (b) verifiquen que submission/metric_contract.json no
   contiene "â" ni "Ã" en ningún texto; (c) recalculen los faltantes por
   columna desde el CSV y comprueben que coinciden con missing_values del
   contrato. No elimines la prueba existente.
7. Ejecuta las pruebas de la actividad sin errores.
8. No modifiques otras actividades (en particular P501, que reutiliza la
   misma lectura en su propio código, ni P513), traceability.yaml ni
   design/.
```
