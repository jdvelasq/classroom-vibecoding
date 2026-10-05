# P106 — Propuestas de mejora

**Línea base:** `P106_activity.md` (entrada S02 más reciente: `S02.P106.01`).

## T01 — Persistir un reporte de preparación: supuestos aplicados, filas afectadas, residuo no canonizado y valores extremos marcados sin recortar

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` p. 5 — Task 3.7 «Document and report data findings (e.g., data quality, impact analysis, results, and data management plan)», junto a Task 3.5 (limpiar, armonizar y validar): documentar lo hallado al preparar los datos es una tarea del dominio de datos, no un anexo (Claude, 2026-10-04). Fuente *authoritative*: respaldo general.
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` pp. 15–16 — CAP-E.3.5.2 incluye «default data» entre los problemas comunes de *wrangling* (p. 15) y CAP-E.3.7.1 pide «Identify findings in a report about data sets that may affect analysis» (p. 16): los supuestos por defecto que afectan el análisis deben quedar en un reporte (Claude, 2026-10-04). Fuente *authoritative*: objetivo de examen de nivel inicial.
  - `design/benchmarks-md/institutional/unf-cap-6768-data-analytics-syllabus.md` p. 6 — el entregable «Data Preparation Report» debe describir el proceso seguido y los «procedures followed to verify the quality of the data, and clean the data»: el reporte es un producto distinto del dataset (Claude, 2026-10-04). Fuente *institutional*: ilustra cómo otro programa lo exige; por sí sola no bastaría.
  - `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` pp. 16–17 — la preparación debe dejar «explicit documentation of procedures, data quality, limitations, and potential errors» (p. 16) y producir «detailed preparation reports documenting acquisition, cleaning activities, feature construction, and integration logic», porque los errores u omisiones de esta fase «propagate through the lifecycle» (p. 17) (Claude, 2026-10-04). Fuente *literature-derived*: síntesis metodológica; respalda la práctica, no un formato.
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` pp. 21 y 23–25 — CRISP-DM pide notar si los faltantes tienen significado (p. 21), «document the rationale behind your decisions» (p. 23), escribir un reporte de limpieza porque «Reporting your data-cleaning efforts is essential for tracking alterations to the data» (p. 24) y registrar «any cases or attributes that could not be salvaged» (p. 25) (Claude, 2026-10-04). Fuente *professional-learning*: señal de práctica; da la forma (regla, filas tocadas, residuo).
- **Qué gana el estudiante:** entiende que una tabla «limpia» tiene un
  residuo de supuestos e incertidumbre que el usuario debe conocer, y
  aprende a entregarlo como evidencia junto al dataset. Hoy P106 entrega
  sólo `submission/ventas.csv`; las decisiones que cambian el resultado
  viven en el código: fechas con día y mes ≤ 12 asumidas `yyyy-mm-dd`
  (H03), pesos sin unidad leídos como kilogramos (H04), variantes no
  listadas que pasan sin cambio (H02), descuentos y pesos con faltantes
  (S04) e importes sin validación de rango (H04, H05). Con un reporte por
  columna (regla, supuesto, filas afectadas, filas no resueltas) y una
  tabla de valores extremos tras la conversión, marcados con una decisión
  explícita pero sin modificarlos, el estudiante aprende que un formato
  correcto no garantiza un valor verosímil y que el atípico se justifica,
  no se elimina por defecto. Corrige además el límite de la auditoría:
  «no hay comunicación ni registro de decisiones para usuarios» (respaldo
  débil de C05).
- **Anclas actuales:** H02 (canonización con diagnóstico de colisiones;
  hoy herramienta del profesor sin prueba), H03 (fechas y regla día/mes),
  H04 (unidades y escalas; peso sin unidad = kg), H05 (invariantes de
  dominio); superficies S02 (reglas), S03 (diagnóstico), S04 (producto
  limpio), S05 (pruebas); dependencia «Habilita para P107» (mismo dato,
  contrato y prueba).
- **Alternativas menores descartadas:** documentar los supuestos en
  comentarios o docstrings no los vuelve evidencia revisable por el
  usuario ni verificable por prueba. Añadir sólo un rango más a las
  invariantes de H05 sería una variante de lo cubierto y ocultaría el
  juicio de dominio que exige un extremo.
- **Contrato de no regresión:** se conservan H01–H05, `data/ventas.csv`,
  las reglas de limpieza y `submission/ventas.csv` con sus 103 registros,
  sus 11 columnas en su orden y sus valores actuales: el reporte describe
  la limpieza y no la cambia; ningún extremo se recorta, imputa ni
  elimina. Las pruebas existentes no se eliminan ni se debilitan.
  `diagnostics.py` puede reutilizarse como fuente del residuo no
  canonizado sin cambiar su comportamiento de diagnóstico.
- **Interacciones:** una sola propuesta en P106, con dos partes que se
  refuerzan (reporte de supuestos y marcado de extremos). Capacidad: P106
  ya tiene cinco highlights; si el taller no alcanza, el marcado de
  extremos puede quedar como sección final que un grupo lento completa
  después. Fuera de P106: P107 comparte datos, contrato y una prueba
  idéntica; las pruebas nuevas romperían esa identidad sólo si se copian.
  Replicar el reporte en P107 es una decisión aparte.
- **Criterio de aceptación:** S05 encuentra (1) un highlight nuevo con
  `submission/cleaning_report.csv`, una fila por columna y regla con su
  supuesto, filas afectadas y filas no resueltas, que incluye al menos las
  fechas ambiguas, los pesos sin unidad, las variantes de proveedor y
  ciudad no canonizadas y los faltantes; y (2) un highlight nuevo con
  `submission/value_flags.csv`, que marca los valores extremos de las
  magnitudes convertidas con la regla usada y una decisión explícita, sin
  alterar `ventas.csv`. Las pruebas verifican columnas, coherencia de
  conteos con `ventas.csv` y que `ventas.csv` no cambió. H01–H05 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P106_limpieza_pandas/

0. Inspecciona primero data/ventas.csv, professor/main.py,
   professor/diagnostics.py, src/main.py, submission/ventas.csv y
   tests/test_activity.py. Si la implementación no coincide con
   design/courses/descriptiva/P106_activity.md (en particular, la regla
   día/mes de yyyy_dd_mm_2_yyyy_mm_dd y el supuesto de kg en clean_weight),
   detente e informa la discrepancia sin modificar nada. Guarda una copia
   de referencia del submission/ventas.csv actual para comparar al final.
1. No cambies data/, las reglas de limpieza, los diccionarios
   *_REPLACEMENTS ni el contenido de submission/ventas.csv.
2. REPORTE DE PREPARACIÓN: en professor/main.py, añade funciones pequeñas
   que, a partir de la columna original y la limpia, cuenten por regla:
   a. fechas cuyo día y mes son ambos ≤ 12 (resueltas por supuesto como
      yyyy-mm-dd);
   b. pesos sin unidad (leídos como kg);
   c. valores de proveedor y ciudad que no coinciden con una forma canónica
      de los diccionarios (residuo no canonizado), reutilizando la clave de
      colisión de diagnostics.py si conviene;
   d. faltantes por columna tras la limpieza;
   e. filas modificadas por cada función clean_*.
   Escribe submission/cleaning_report.csv con columnas column, rule,
   assumption, rows_affected, rows_unresolved (sin índice). El texto de
   assumption debe describir la regla del código, no justificarla con
   hechos de negocio inventados.
3. VALORES EXTREMOS: para cada magnitud convertida (peso, importe, precio
   unitario y descuento), marca los valores fuera de una regla declarada
   (por ejemplo, fuera de [Q1 − 3·IQR, Q3 + 3·IQR]) y, si las columnas lo
   permiten, las inconsistencias entre importe, precio y cantidad.
   Escribe submission/value_flags.csv con columnas row, column, value,
   rule, decision, donde decision ∈ {posible_error_de_unidad, válido,
   no_decidible}. No asignes «válido» ni «posible_error_de_unidad» sin una
   razón observable en los datos (p. ej., un factor 1000 frente a valores
   comparables del mismo proveedor); en otro caso usa no_decidible. No
   recortes, imputes ni elimines ningún valor.
4. Si existe una interfaz de estudiante (src/main.py), añade sólo las
   firmas de las funciones nuevas con NotImplementedError, siguiendo el
   esqueleto actual.
5. Añade a tests/test_activity.py pruebas que verifiquen: que ambos CSV
   existen con esas columnas; que rows_affected y rows_unresolved son
   enteros entre 0 y 103; que el reporte incluye filas para fechas
   ambiguas y pesos sin unidad; que cada row de value_flags existe en
   ventas.csv y decision pertenece al dominio; y que ventas.csv sigue
   teniendo 103 registros y las mismas columnas. Sigue el patrón de rutas
   de las pruebas existentes. No elimines ni debilites pruebas existentes.
6. Ejecuta professor/main.py y las pruebas de la actividad sin errores, y
   comprueba que submission/ventas.csv es idéntico a la copia del paso 0.
7. No modifiques otras actividades (en particular P107), traceability.yaml
   ni design/.
```
