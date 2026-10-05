# P153 — Propuestas de mejora

**Línea base:** `P153_activity.md` (entrada S02 más reciente: `S02.P153.02`).

## T01 — Añadir reglas de rango y de definición con severidad, y ejercitar la rama BLOQUEADO con una copia del hecho con defectos controlados

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/national-academies-data-science-for-undergraduates-2018.md` pp. 38, 41 y 46 — no basta con «a “canned” data set» (p. 38); *data acumen* exige «real-world data and problems that can reinforce the limitations of tools» (p. 41, Finding 2.3); «Data consistency checking» figura entre las habilidades clave de descripción de datos (p. 46): una compuerta que sólo se evalúa sobre datos íntegros por construcción no muestra lo que detecta (Claude, 2026-10-04). Fuente *authoritative*: respalda la expectativa general, no el mecanismo.
- **Qué gana el estudiante:** ver que una compuerta de publicación discrimina
  y distinguir un problema de integridad de uno de definición. Hoy P153
  pregunta «¿Podemos publicar estos KPI para la gerencia sin ocultar
  problemas de calidad o definición?», pero sus cuatro reglas sólo verifican
  integridad del hecho (llave única, ventas netas no negativas, cantidades
  positivas, fechas en `dim_date`). Ninguna verifica la definición del
  catálogo; por ejemplo, el rango de `discount_pct` que sostiene el
  descuento ponderado de H02. Sobre un mart íntegro por construcción la
  decisión es siempre `APROBADO` (H03; S01; S03 «sin caso de fallo»): una
  regla que no puede fallar no prueba nada. Con el cambio, el estudiante
  clasifica cada regla por lo que protege, le asigna una severidad y decide
  qué problema impide publicar y cuál permite publicar con una advertencia
  visible (la respuesta literal a «sin ocultar»). Además ve la misma
  compuerta producir `BLOQUEADO` sobre una copia con defectos conocidos y
  qué KPI quedan comprometidos según el linaje.
- **Anclas actuales:** H01 (KPI como contrato: grano y período), H02 (tasa
  ponderada sobre `discount_pct`), H03 (calidad como compuerta; rama de
  bloqueo no ejercitada), H04 (linaje, para señalar el KPI afectado);
  superficies S01 (mart íntegro), S03 (reglas y decisión), S05 (pruebas
  `test_02` y `test_04`).
- **Alternativas menores descartadas:**
  - Declarar en markdown que la rama `BLOQUEADO` existe: no deja ver que la
    compuerta funcione.
  - Sólo añadir reglas de definición sin la copia con defectos: sobre datos
    íntegros también pasarían siempre.
  - Introducir defectos en `data/sales_mart.db`: rompería P152 y P154, que
    leen el mismo mart, y la decisión `APROBADO` de referencia. La copia
    derivada y documentada, permitida por `AGENTS.md`, evita ese efecto.
- **Contrato de no regresión:** se conservan el catálogo (H01–H02), el
  linaje (H04), las cuatro reglas actuales con su lógica, la evaluación
  sobre `data/sales_mart.db` y su decisión (`APROBADO` si ninguna regla de
  severidad error falla), y `test_02`–`test_03` y `test_05`. Se sustituye la
  decisión binaria por una de tres estados (`APROBADO`, `APROBADO CON
  ADVERTENCIA`, `BLOQUEADO`), que contiene la binaria; `test_04` se extiende
  a esa regla. `kpi_quality_report.csv` gana columnas; las existentes no
  cambian.
- **Interacciones:** con T02, se refuerzan. La regla de rango de
  `discount_pct` protege la línea base del descuento ponderado que calcula
  T02, y la línea base sólo se publica para el mart de referencia, nunca
  para la copia con defectos. Si se aprueban ambas, ejecutar T01 primero.
  Capacidad: P153 pasaría de cuatro a seis highlights; T01 es la más
  costosa (generador de la copia, reglas, tres estados). Conviene decidir en
  la discusión si la evaluación de la copia con defectos queda como sección
  final que un grupo lento puede completar en la sesión siguiente.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que (1)
  el reporte de calidad incluye al menos una regla de definición o rango
  ligada al catálogo, cada regla con tipo, severidad y KPI afectados; (2) la
  decisión sobre el mart de referencia sigue derivándose por código con tres
  estados posibles; (3) la misma función, aplicada a una copia del hecho con
  defectos controlados y documentados, produce `BLOQUEADO` y nombra los KPI
  comprometidos; y (4) pruebas que verifican ambos reportes y la coherencia
  reporte–decisión. H01–H04 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P153_ventas_kpis/

0. Inspecciona primero professor/notebook.ipynb, data/sales_mart.db (tablas
   y columnas de fact_sales y dim_date), submission/ y tests/. Verifica que
   fact_sales contiene discount_pct y gross_sales; si discount_pct no está,
   usa como regla de definición net_sales <= gross_sales e informa. Si la
   decisión actual no es APROBADO o alguna regla ya falla, detente e
   informa. Si la implementación no coincide con
   design/courses/descriptiva/P153_activity.md, detente e informa.
1. No modifiques data/sales_mart.db, el catálogo, el linaje ni la lógica de
   las cuatro reglas existentes.
2. Reglas nuevas (añádelas a quality_checks, sin reordenar las actuales):
   - definición: 0 <= discount_pct < 1 (coherente con el KPI ponderado de
     H02);
   - definición/salida: net_sales <= gross_sales;
   - rango temporal: todas las fechas del hecho dentro del período de
     cobertura declarado en el catálogo; si el catálogo no declara un rango,
     declara la cobertura (2024) en el notebook y úsala.
3. Para cada regla (actuales y nuevas) añade rule_type (integridad,
   definición, rango) y severity (error, alerta, informativa) y
   affected_kpis (KPI del catálogo que dependen de los campos de la regla,
   derivados de metric_lineage.csv). Severidad: usa la asignación aprobada
   en la discusión de esta T01 (registrada en P153_log.md). Propuesta por
   defecto: las cuatro de integridad y las dos de definición = error; rango
   temporal = alerta. Si el profesor no confirmó la asignación, detente y
   pídela.
4. Decisión derivada por código: BLOQUEADO si falla alguna regla error;
   APROBADO CON ADVERTENCIA si sólo fallan reglas alerta; APROBADO en otro
   caso. Explica en markdown, en 3–4 líneas, por qué una advertencia visible
   responde a «sin ocultar problemas».
5. Copia con defectos controlados:
   a. Crea professor/make_controlled_defects.py que lee data/sales_mart.db,
      copia las cuatro tablas y modifica sólo fact_sales con defectos
      fijos y documentados: una llave de hecho duplicada, una línea con
      discount_pct > 1 y una fecha fuera de la cobertura (presente en
      dim_date si hace falta para aislar la regla temporal). Semilla o
      índices fijos.
   b. Escribe data/sales_mart_controlled_defects.db (artefacto derivado
      para el estudiante) y documenta en el notebook su origen, los
      defectos inyectados y que no representa un sistema real.
   c. Evalúa la misma función de reglas y decisión sobre la copia, muestra
      el reporte (celda de evidencia) y explica en 2–4 líneas qué reglas
      fallaron, qué KPI quedan comprometidos y por qué la decisión es
      BLOQUEADO.
6. Persiste:
   - submission/kpi_quality_report.csv: columnas actuales + rule_type,
     severity, affected_kpis.
   - submission/kpi_quality_report_controlled_defects.csv con el mismo
     esquema.
   - submission/kpi_publication_decision_controlled_defects.csv con el
     mismo esquema que kpi_publication_decision.csv.
   - kpi_publication_decision.csv conserva su esquema; su valor admite los
     tres estados.
7. Pruebas en tests/test_activity.py, sin eliminar ninguna:
   - Amplía test_01 con los archivos y columnas nuevos sin quitar los
     existentes.
   - test_02: recalcula también las reglas nuevas desde data/sales_mart.db.
   - test_04: extiende la coherencia reporte–decisión a tres estados y
     aplícala a ambos pares de archivos.
   - Añade una prueba que recalcula las reglas sobre
     data/sales_mart_controlled_defects.db, exige que fallen al menos la de
     llave única y la de discount_pct, que la decisión sea BLOQUEADO y que
     affected_kpis de la regla de discount_pct incluya el descuento
     ponderado.
8. Ejecuta professor/make_controlled_defects.py, el notebook completo y las
   pruebas de la actividad sin errores.
9. No modifiques otras actividades, traceability.yaml ni design/.
```

## T02 — Completar la ficha de cada KPI con propósito, decisión asociada, frecuencia y un valor de línea base calculado

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` p. 23 — «Ficha mínima de cada indicador»: «Definición y propósito: qué representa y por qué es relevante», «Línea base y meta: situación inicial y resultado esperado», «Fuente y método», «Responsable: quien produce, valida e interpreta la medición», «Frecuencia: cuándo se actualiza y se revisa», «Decisión asociada: la acción que puede desencadenar su resultado» (Claude, 2026-10-04). Fuente *literature-derived* y única: la ficha procede de la evaluación de una estrategia de datos (nivel organizacional); se adopta como práctica de definición de indicadores, no como prescripción de gestión estratégica.
- **Qué gana el estudiante:** conectar el contrato de un KPI con su uso
  descriptivo: para qué decisión se mira, cada cuánto se revisa y qué valor
  se toma como punto de partida. Hoy el catálogo (H01) declara fórmula,
  numerador, denominador, grano, período, propietario y fuente, pero «ningún
  valor de KPI se calcula ni se persiste» y «el producto es el contrato de
  los indicadores, no su lectura» (S02). El descuento ponderado de H02 está
  definido pero «no calculado ni contrastado con el promedio simple». Con el
  cambio, el estudiante calcula por primera vez los tres KPI sobre el mart y
  ve, con números, por qué la razón de sumas difiere del promedio de tasas.
  La ficha queda ligada a una decisión aportada por el profesor, no a una
  etiqueta.
- **Anclas actuales:** H01 (KPI como contrato), H02 (tasa ponderada; límite
  «el KPI no se calcula»), H04 (linaje: la línea base se calcula con los
  mismos campos); superficies S02 (catálogo; «ninguno calculado») y S05
  (pruebas: `test_01` exige columnas y atributos no nulos).
- **Alternativas menores descartadas:**
  - Escribir propósito y decisión sin calcular nada: dejaría el catálogo sin
    lectura y H02 sin evidencia numérica.
  - Calcular los KPI en una tabla aparte sin ligarlos a la ficha: repetiría
    lo que ya hacen P120–P122 y P124 (KPI sin catálogo), sin el contraste
    que aporta P153.
  - Fijar una meta inventada: la meta es texto de negocio; sólo se incluye
    si el profesor la aporta.
- **Contrato de no regresión:** se conservan los tres KPI, sus siete
  atributos actuales, el linaje, las reglas, la decisión de publicación y
  `test_02`–`test_05`. `kpi_catalog.csv` gana columnas; las existentes y sus
  valores no cambian. La pregunta de publicación no cambia.
- **Interacciones:** con T01, se refuerzan. La línea base se calcula sólo
  sobre el mart de referencia y sólo si su decisión no es `BLOQUEADO`; la
  regla de rango de `discount_pct` de T01 protege el valor del descuento
  ponderado. Si T01 se ejecuta primero, T02 se apoya en su decisión de tres
  estados; si T01 se rechaza, T02 usa la decisión binaria actual. Fuera de
  P153: P154 T01 puede usar la misma definición de línea base para su
  criterio de atención, recalculada desde su propia capa de consumo, porque
  P154 no lee artefactos de P153. Capacidad: T02 es la más liviana del
  archivo (columnas y un cálculo).
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que (1)
  cada KPI del catálogo tiene propósito, decisión asociada y frecuencia
  aportados por el profesor (registrados en `P153_log.md`, no inventados por
  la herramienta); (2) cada KPI tiene una línea base calculada desde
  `data/sales_mart.db` con su método declarado; (3) el descuento ponderado
  se contrasta numéricamente con el promedio simple de `discount_pct`; y (4)
  una prueba recalcula las líneas base. H01–H04 siguen presentes y H02 deja
  de tener el límite «no se calcula».

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P153_ventas_kpis/

0. Inspecciona primero professor/notebook.ipynb (kpi_catalog), data/
   sales_mart.db, submission/kpi_catalog.csv y tests/. Si el catálogo ya
   tiene propósito, decisión asociada o valores calculados, detente e
   informa. Si la implementación no coincide con
   design/courses/descriptiva/P153_activity.md, detente e informa.
1. TEXTO DE NEGOCIO: no inventes propósito, decisión asociada, frecuencia ni
   meta. Usa el texto que el profesor haya aprobado en la discusión de esta
   T02 (registrado en P153_log.md), uno por KPI. Si falta para algún KPI,
   detente y pídelo. Incluye meta sólo si el profesor la aportó; si no, no
   crees la columna ni un valor de relleno.
2. LÍNEA BASE: calcula cada KPI desde data/sales_mart.db con la fórmula del
   catálogo y en su período declarado (si el período es mensual, calcula el
   valor de cada mes de la cobertura y toma la media mensual como línea
   base; declara el método). Para el descuento ponderado usa
   SUM(gross_sales * discount_pct) / SUM(gross_sales).
3. Calcula también el promedio simple de discount_pct por línea y explica en
   2–4 líneas, con ambos valores, por qué el catálogo usa la razón de sumas.
4. Si la decisión de publicación del mart de referencia es BLOQUEADO, no
   publiques líneas base y explícalo; esto no debería ocurrir con los datos
   actuales.
5. Añade a submission/kpi_catalog.csv las columnas purpose,
   associated_decision, frequency, baseline_value, baseline_method (y target
   sólo si el profesor la aportó), siguiendo la convención de idioma de las
   columnas existentes. No cambies las columnas ni los valores actuales.
6. Pruebas en tests/test_activity.py, sin eliminar ninguna:
   - Amplía test_01 con las columnas nuevas (no nulas) sin quitar las
     existentes.
   - Añade una prueba que recalcula baseline_value de cada KPI desde
     data/sales_mart.db con tolerancia numérica y verifica que la línea base
     del descuento ponderado es la razón de sumas.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
