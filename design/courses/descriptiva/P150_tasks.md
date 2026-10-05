# P150 — Propuestas de mejora

**Línea base:** `P150_activity.md` (entrada S02 más reciente: `S02.P150.02`).

## T01 — Corregir la lectura temporal engañosa de la serie mensual

- **Estado:** pendiente de discusión
- **Tipo:** caso/datos (corrige defecto)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 38 y 46 — «It is insufficient for them to be handed a “canned” data set and be told to analyze it» y los graduados conocen «the pitfalls of misrepresenting data and results» (p. 38); las representaciones de datos ayudan a evitar que datos mal codificados «lead to misleading conclusions» (p. 46): una serie cuya variación es artefacto del generador no debe presentarse como evolución de las ventas (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general de no representar mal los datos, no un procedimiento.
- **Qué gana el estudiante:** reconocer cuándo una serie temporal no admite
  lectura temporal y reformular la pregunta hacia lo que los datos sí
  sostienen. Hoy la única pregunta de P150 es «¿Cómo cambian las ventas
  netas mensuales por categoría después de integrar las fuentes?», pero la
  fecha de cada pedido es una función determinista de `order_id` (un pedido
  cada tres días, casi el mismo número de pedidos por mes). La variación que
  muestra el gráfico de líneas refleja sorteos del generador, no
  estacionalidad ni comportamiento comercial (P150, «Uso y límite»; S01;
  límite de H04). El único producto de respuesta del taller induce, por
  construcción, una conclusión engañosa. Con el cambio, el estudiante
  verifica en los datos por qué la serie no es legible (pedidos por mes casi
  constantes) y responde una pregunta de composición por categoría, que sí
  es legible sobre la tabla integrada.
- **Anclas actuales:** H04 (tabla y respuesta temporal persistidas);
  superficies S01 (dataset sintético, calendario uniforme), S04 (producto y
  respuesta, sin conclusión) y S05 (pruebas: `test_04` recalcula la
  agregación mensual, `test_05` exige la pregunta literal). Dependencia
  «Habilita para P151» (grano línea y derivación de importes) sin cambios.
- **Alternativas menores descartadas:**
  - Sólo declarar el límite en una celda markdown, sin reformular la
    pregunta: dejaría persistida en `questions.json` una pregunta cuya
    respuesta el propio taller declara ilegible.
  - Alternativa mayor (no es la propuesta mínima): cambiar
    `professor/generate_data.py` para que la serie tenga un patrón temporal
    documentado (por ejemplo, estacionalidad conocida por categoría). Como
    ese generador es compartido por P150–P154 (copia en cada `professor/` y
    `data/sales_mart.db` derivado), el cambio regeneraría los datos de todo
    el bloque, cambiaría los valores que describen los `Pxxx_activity.md` de
    P151–P154 (por ejemplo, Centro–Servicios 106963.0 en P151 y P154;
    Servicios 92853.0 y Oficina 180 en P152) y obligaría a revalidar sus
    pruebas. Además, por `AGENTS.md`, un patrón simulado sólo se justifica
    si el objetivo de aprendizaje exige una simulación controlada y debe
    declararse como tal. Es decisión de curso; sustituir el caso sintético
    por un dataset real trazable también lo sería y queda fuera de esta T01.
- **Contrato de no regresión:** se conservan H01–H03 (integración, grano,
  descomposición del importe) sin cambios, `sales_analytics.csv` con su
  esquema y `test_02`–`test_03`. H04 se modifica: la tabla sigue publicada
  y la respuesta sigue derivándose de ella, pero la pregunta pasa de
  evolución mensual a composición por categoría. `monthly_category_sales.csv`
  y su gráfico se conservan como evidencia del límite (no como respuesta), y
  `test_04` se mantiene. `test_05` cambia sólo el literal de la pregunta.
- **Interacciones:** ninguna dentro de P150. Fuera de P150: P152 (*roll-up*
  mensual por región) y P154 (cualquier criterio de atención basado en
  cambios mensuales) heredan el mismo calendario; sus propuestas declaran
  esta dependencia. Si en la discusión se prefiere la alternativa del
  generador, debe decidirse para todo el bloque P150–P154 antes de ejecutar
  P152 T01 y P154 T01.
- **Criterio de aceptación:** S05 encuentra (1) una celda de evidencia
  visual con el número de pedidos por mes y una celda markdown que declara
  que el calendario es sintético y uniforme y que la variación mensual no
  admite lectura estacional ni comercial; (2) la pregunta reformulada hacia
  composición por categoría en `questions.json`, respondida por un artefacto
  nuevo en `submission/` derivado de `sales_analytics.csv`; (3) una lectura
  escrita persistida con respuesta y límite; y (4) pruebas que verifican el
  artefacto nuevo y la lectura. H01–H03 siguen presentes y H04 queda
  reescrito con la nueva pregunta.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P150_ventas_tabla/

0. Inspecciona primero professor/generate_data.py, professor/notebook.ipynb,
   data/, submission/ (en especial questions.json) y tests/. Reproduce el
   conteo de pedidos distintos por mes desde data/order_lines.csv. Si el
   número de pedidos por mes NO es casi constante (o si la fecha no es una
   función determinista de order_id), detente e informa: el defecto que
   corrige esta T01 no existiría. Si la implementación no coincide con
   design/courses/descriptiva/P150_activity.md, detente e informa.
1. No modifiques professor/generate_data.py ni data/ (son compartidos con
   P151–P154). No cambies la integración, el grano, las medidas derivadas,
   sales_analytics.csv ni monthly_category_sales.csv.
2. Después del gráfico mensual existente, añade «¿Qué puede leerse de la
   serie mensual?»:
   a. Celda de evidencia visual: tabla pequeña con pedidos distintos por mes
      (desde la tabla integrada).
   b. Markdown de 3–5 líneas: el calendario es sintético y uniforme por
      construcción; la variación mensual de las ventas netas refleja sorteos
      del generador, no estacionalidad ni comportamiento comercial; por eso
      la serie no responde una pregunta de evolución.
3. Reformula la pregunta hacia composición por categoría. Usa el texto
   aprobado por el profesor en la discusión de esta T01 (registrado en
   P150_log.md). Si no existe, detente y pídelo. Redacción propuesta para
   la discusión: «¿Cómo se distribuyen las ventas netas del año entre
   categorías después de integrar las fuentes?».
4. Calcula desde sales_analytics.csv, para todo 2024, por categoría:
   net_sales, share (net_sales / total) y, como contraste, gross_sales y
   discount_amount. Grafica la composición (barras ordenadas) y verifica con
   assert que la suma de net_sales por categoría coincide con el total de
   la tabla.
5. Persiste:
   - submission/category_composition.csv con columnas category, net_sales,
     share, gross_sales, discount_amount (share suma 1).
   - submission/analysis_conclusions.csv con columnas pregunta, respuesta,
     límite (patrón de descriptiva/P125 H06). El límite debe declarar que
     los datos son sintéticos y que la composición no admite conclusiones
     comerciales ni lectura temporal.
   - questions.json con la pregunta reformulada apuntando a
     category_composition.csv (sustituye la entrada anterior; conserva la
     estructura del archivo).
6. Pruebas en tests/test_activity.py, sin eliminar ninguna:
   - test_04 se mantiene (monthly_category_sales.csv sigue entregado).
   - test_05: actualiza sólo el literal de la pregunta.
   - Añade una prueba que recalcula category_composition.csv desde
     sales_analytics.csv, exige las columnas, share en [0, 1] con suma 1 y
     reconciliación con el total de net_sales.
   - Añade una prueba que exige analysis_conclusions.csv con sus columnas,
     una fila por pregunta y un límite que mencione «sintétic» y «temporal»
     (o «estacional»).
   - Si test_01 exige un conjunto exacto de archivos, amplíalo con los dos
     archivos nuevos sin quitar ninguno.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
