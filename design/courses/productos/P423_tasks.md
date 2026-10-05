# P423 — Propuestas de mejora

**Línea base:** `P423_activity.md` (entrada S02 más reciente: `S02.P423.01`).

## T01 — Monitorear con el criterio de aceptación con que P403 habilitó el modelo, derivar el umbral de la medida de éxito y la línea base, y exigir una ventana mínima (veredicto cumple/incumple/insuficiente)

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia (corrige un defecto)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` pp. 5 y 7 — «Task 2.4 Define primary measures of success» y «Task 2.5 Identify baseline performance of the current state» (p. 5); en la gestión del ciclo de vida, «Task 7.1 Track analytics solution performance» y «Task 7.4 Validate the business case for the analytics solution over time» (p. 7): el seguimiento en operación se juzga contra la medida de éxito y la línea base declaradas al encuadrar, no contra una constante nueva (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general, no un procedimiento.
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` pp. 11 y 24 — CAP-P.2.4.2 «Identify the process to verify if the primary measures of success have been met» (p. 11) y, en Task 7.1 «Track analytics solution performance», CAP-P.7.1.1 «Identify metrics that reflect an acceptable analytics solution performance» (p. 24): las métricas de seguimiento son las que definen un desempeño aceptable, y verificar si se cumplen es un proceso declarado (Claude, 2026-10-05). Fuente *authoritative*.
- **Qué gana el estudiante:** entiende que una alerta de desempeño aplica un
  contrato, no un número: monitorea con las métricas y mínimos con que la
  capacidad fue habilitada, sabe de dónde sale el umbral y no emite veredicto
  cuando la evidencia no alcanza. Hoy P423 compara la exactitud de cinco
  filas con `MINIMUM_ACCURACY = 0.75`, un umbral «no justificado» (S02,
  índice de comparación externa), y el producto admite que «la exactitud 0.6
  no tiene precisión suficiente para sostener una decisión». Al mismo tiempo,
  P403 habilitó un clasificador exigiendo exactitud, exactitud balanceada y
  AUC (0,70/0,70/0,80), precisamente porque la clase es asimétrica (P403
  H04). El seguimiento usa así un criterio distinto y más débil que el que
  justificó la habilitación. Con el cambio, el estudiante (1) toma métricas y
  mínimos del criterio de P403 con procedencia declarada; (2) deriva el umbral
  efectivo de esa medida de éxito y de la línea base del estado actual (la
  regla trivial de clase mayoritaria sobre la misma ventana: un modelo que no
  la supera no aporta); y (3) declara un número mínimo de observaciones por
  ventana, por debajo del cual el veredicto es `insuficiente` en lugar de
  `alert: true/false`. Con un resultado por fila, una sola observación mueve
  la exactitud de cinco filas en 0,2.
- **Anclas actuales:** H01 (desempeño exige pares predicción-resultado), H02
  (borde de la alerta: igualdad con el mínimo no alerta); superficies S01
  (`data/production_outcomes.csv`: «Cinco filas sin fecha ni procedencia»), S02
  (`professor/main.py`: «Exactitud; mínimo 0.75 fijo»), S03
  (`submission/performance_report.json`), S04 (pruebas) y S05 (`src/main.py`,
  sin `HOW_TO_RUN_ME.txt`); dependencias: «Recibe de P422: patrón de reporte
  con alerta»; «P424 no usa la alerta». Fuera de P423: P403 H02 y H04, S02
  (constantes `MIN_ACCURACY`, `MIN_BALANCED_ACCURACY`, `MIN_AUC`) y S04
  (`model_test_report.json` con 0,754/0,731/0,842 sobre 114 filas).
- **Condición de caso y datos:** el criterio de P403 sólo puede aplicarse si
  P423 monitorea el clasificador de P403. Hoy no es así: las cinco filas
  `high`/`low` no tienen procedencia ni modelo identificado y no coinciden
  con el `target` 0/1 de P403. La T01 exige que el profesor decida la fuente
  de resultados observados de ese clasificador (predicción, puntaje si se
  quiere evaluar AUC, resultado real y fecha o periodo), con procedencia
  documentada. No sirven las 114 filas con que P403 lo habilitó (no son
  operación posterior) ni filas usadas para entrenarlo. Si no hay fuente
  real, el profesor puede aprobar una secuencia derivada o simulada,
  declarada como tal (excepción de datos sintéticos de `AGENTS.md`). Sin esa
  decisión, la T01 no se ejecuta.
- **Alternativas menores descartadas:** documentar el origen del 0.75 sin
  cambiar el caso no es posible: nadie lo acordó. Pedir más filas sin un
  mínimo declarado deja el problema de la precisión implícito. Una prueba
  estadística formal o un cálculo de tamaño muestral serían método de
  Predictiva; basta un mínimo declarado en el contrato operativo. Copiar sólo
  los mínimos de P403 sin la línea base dejaría pasar un modelo que no supera
  la regla trivial cuando la clase está muy desbalanceada.
- **Contrato de no regresión:** se conservan H01 y H02:
  `evaluate_performance`, `test_01` (0,75 exacto no alerta) y `test_02` siguen
  sin cambios, y la regla de borde (`<` alerta; igualdad cumple) se aplica a
  cada métrica nueva. `performance_report.json` conserva `observations`,
  `accuracy`, `minimum_accuracy` y `alert`, y añade campos: `alert` pasa a
  ser `verdict == "incumple"`. Sustitución explícita: `MINIMUM_ACCURACY =
  0.75` y las cinco filas actuales dejan de ser el caso de la evidencia
  principal y se reemplazan por el criterio copiado de P403 y los resultados
  aprobados por el profesor. Las pruebas que usan etiquetas 0/1 se conservan.
  No se toca P403: el criterio se copia como insumo con procedencia.
- **Interacciones:** T02 depende de esta T01. Usa la misma fuente de
  resultados con periodo, el mismo mínimo de observaciones (un periodo
  insuficiente no se evalúa) y el desempeño de habilitación de P403 como
  error de referencia. Si T01 se rechaza, T02 necesita igualmente resolver el
  caso y los datos. Las dos producen señales distintas que no deben
  confundirse. T01 da el veredicto de contrato (cumple, incumple o
  insuficiente) y T02 da la acción de mantenimiento. Pueden discrepar: un
  periodo aislado puede incumplir el mínimo sin que la política ordene actuar.
  El reporte muestra ambas y declara que la acción la gobierna T02. Con
  `P424_tasks.md` T01: P424 consumirá una copia del reporte de P423, así que
  los campos `verdict`, `action` (si T02 se aprueba) y un identificador del
  reporte son contrato entre ambas actividades y no deben renombrarse sin
  actualizar P424. Si se aprueban propuestas sobre P403 que justifiquen sus
  umbrales, P423 hereda los nuevos valores por la copia del criterio.
  Capacidad: P423 tiene hoy dos highlights y un script corto; T01 y T02
  juntas lo duplican y exigen preparar datos con periodos. Conviene decidir
  en la discusión si T02 queda como sección final que un grupo lento puede
  completar en la sesión siguiente.
- **Criterio de aceptación:** S05 encuentra (1) un archivo de criterio en
  `data/` con métricas, mínimos y desempeño de habilitación copiados de P403,
  con procedencia (rutas de origen, fecha, valores) y el mínimo de
  observaciones aprobado por el profesor; (2) resultados observados del
  clasificador de P403 con procedencia documentada; (3) en
  `submission/performance_report.json`, por métrica: valor, mínimo de P403 y
  su origen, línea base de clase mayoritaria sobre la misma ventana, umbral
  efectivo (el mayor de ambos) y estado; además `observations`,
  `minimum_observations` y `verdict` en {cumple, incumple, insuficiente}; una
  métrica no calculable (por ejemplo, AUC sin puntaje) figura como «no
  evaluable», no se omite; (4) pruebas de profesor para `insuficiente`
  (n < mínimo), borde exacto (cumple), incumplimiento por mínimo e
  incumplimiento por no superar la línea base; (5) una prueba de actividad
  que verifica los campos y valores del veredicto; y (6) H01 y H02 presentes,
  con `test_01` y `test_02` sin cambios.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P423_model_performance_monitoring/

0. Inspecciona primero data/production_outcomes.csv, professor/main.py
   (evaluate_performance y escritura del reporte), professor/test_main.py,
   src/main.py, submission/performance_report.json y tests/test_activity.py.
   Inspecciona también, sólo para leer,
   implementation/productos/P403_model_testing_pytest/professor/main.py
   (constantes MIN_*) y submission/model_test_report.json. Si alguna
   implementación no coincide con design/courses/productos/P423_activity.md
   o P403_activity.md, detente e informa sin modificar nada.
1. CASO Y DATOS: no inventes la fuente de resultados ni el mínimo de
   observaciones. Usa la fuente y el mínimo que el profesor haya aprobado en
   la discusión de esta T01 (registrados en P423_log.md): resultados
   observados del clasificador de P403 con columnas de predicción, resultado
   real, periodo o fecha y, si existe, puntaje de la clase 1. Si no existen,
   detente y pídelos. No uses data/model_test_set.csv de P403 ni filas de
   entrenamiento como resultados de operación. Si el profesor aprueba datos
   derivados o simulados, escribe data/PROVENANCE.md con su origen,
   transformación y la limitación declarada.
2. Crea data/acceptance_criterion.json copiado de P403 con: metrics (para
   accuracy, balanced_accuracy y auc: minimum y enablement_value), n de
   habilitación (114), source (rutas de P403 de donde salen mínimos y
   valores), copied_at y minimum_observations. No leas archivos de P403 en
   tiempo de ejecución.
3. Conserva evaluate_performance, MINIMUM_ACCURACY y sus pruebas. Añade
   evaluate_window(outcomes, criterion) que:
   a. devuelva verdict "insuficiente" si n < minimum_observations, sin
      evaluar métricas contra umbrales;
   b. calcule cada métrica del criterio (balanced_accuracy_score y
      roc_auc_score de sklearn; AUC sólo si hay puntaje, si no "no
      evaluable");
   c. calcule la línea base de clase mayoritaria sobre la misma ventana para
      cada métrica calculable;
   d. fije umbral efectivo = max(mínimo de P403, línea base) y estado por
      métrica con la regla de borde actual (valor < umbral incumple;
      igualdad cumple);
   e. devuelva verdict "incumple" si alguna métrica evaluable incumple y
      "cumple" en otro caso.
4. Escribe submission/performance_report.json conservando observations,
   accuracy, minimum_accuracy y alert (alert = verdict == "incumple") y
   añadiendo report_id (por ejemplo, hash del contenido o marca temporal),
   window (periodo inicial y final), minimum_observations, metrics (por
   métrica: value, minimum, minimum_source, baseline, effective_threshold,
   status) y verdict.
5. Añade a professor/test_main.py pruebas con DataFrames pequeños para:
   insuficiente (n < mínimo), borde exacto (cumple), incumple por mínimo,
   incumple por no superar la línea base y AUC no evaluable sin puntaje. No
   elimines ni cambies test_01 ni test_02.
6. Añade a tests/test_activity.py una prueba que verifique que el reporte
   tiene verdict en {cumple, incumple, insuficiente}, minimum_observations,
   y para cada métrica minimum_source y effective_threshold >= minimum. Las
   rutas se resuelven relativas al archivo de prueba. No elimines pruebas
   existentes.
7. Actualiza src/main.py de forma coherente (plantilla de evaluate_window
   sin resolver) y crea HOW_TO_RUN_ME.txt con el comando y un paso que pida
   explicar, en 2–3 líneas, de dónde sale cada umbral y por qué una ventana
   corta da "insuficiente".
8. Ejecuta las pruebas de profesor y de la actividad sin errores.
9. No modifiques P403, P424 ni otras actividades, traceability.yaml ni
   design/.
```

## T02 — Convertir la alerta en una política de mantenimiento graduada: límites desde el error de referencia del modelo, reglas de patrón sobre observaciones posteriores y acción declarada (mantener, recalibrar/reentrenar con revisión, revertir vía P424)

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia + proceso
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` p. 24 — el dominio de ciclo de vida implica «ongoing oversight and calibration to ensure the analytics solution continues to perform effectively», con «Task 7.2: Recalibrate and maintain the analytics solution» y CAP-P.7.2.1 «Identify potential opportunities for recalibration of the analytics solution»: operar incluye decidir cuándo recalibrar o mantener, no sólo detectar (Claude, 2026-10-05). Fuente *authoritative*: expectativa general; el reentrenamiento en sí queda fuera del curso.
  - `design/benchmarks-md/literature-derived/prodig8-strategies-executing-analytics-projects.md` pp. 20–21 — la convergencia metodológica recomienda «retraining policies, and human-in-the-loop mechanisms to maintain trust and relevance over time» (p. 20) y la gobernanza exige «policies for time-based or condition-based maintenance of data pipelines and deployed models» y «explicit maintenance policies for drift detection and retraining» (p. 21): la respuesta a la degradación es una política explícita, no una decisión ad hoc (Claude, 2026-10-05). Fuente *literature-derived*: perspectiva metodológica, no herramienta.
  - `design/benchmarks-md/professional-learning/sas-forecasting.md` pp. 153–157 — el criterio común «MAPE > 50%» es problemático porque «a single forecast may exceed the error criterion just by chance» y un modelo puede quedar siempre bajo el criterio aunque su error sea «much higher than should be achievable» (p. 153); el método usa sólo residuos y «it is model agnostic» (p. 154); reglas de patrón como «2 out of 2 points beyond 3-sigma limits» (desechar) y «3 out of 3 points beyond 2-sigma limit» (ajustar), con severidades «Low Severity—No model changes required», «Medium Severity—Adjust/refit existing model parameters» y «High Severity—Discard current model and develop new model» (p. 155); se evalúa desde el «model vintage» porque «We react only to new observations» (pp. 155–156) y «We do not want to overreact to a single point being outside the 3-sigma limits» (p. 157) (Claude, 2026-10-05). Fuente *professional-learning* (artículo de Katz): el método es para residuos de pronóstico y está patentado; aplicarlo a la proporción de errores de un clasificador es una extensión estándar de control estadístico de procesos que la fuente no muestra.
- **Qué gana el estudiante:** pasa de «detectar degradación» a «decidir la
  respuesta operativa a la degradación», que es la pregunta de Productos
  (C05: observar, gobernar, recuperar). Hoy P423 termina en `alert: true` sin
  consecuencia: la auditoría registra que el caso no identifica «la acción
  tras la alerta» y que «P424 no usa la alerta». Con el cambio, el estudiante
  (1) fija los límites a partir del error que el modelo tenía cuando quedó
  vigente (la proporción de errores de habilitación en P403) y del tamaño de
  cada periodo, no con una constante común; (2) evalúa sólo los periodos
  posteriores a la fecha de vigencia y distingue un punto aislado de un
  patrón sostenido; y (3) traduce la severidad en una acción declarada:
  mantener, solicitar recalibración o reentrenamiento con revisión humana
  (registrada, no ejecutada en el taller) o revertir a la versión registrada
  anterior, que es la operación de P424. Ningún taller del curso distingue
  excepción de patrón: P422, P423 y los demás monitores usan umbrales fijos
  de una sola ventana.
- **Anclas actuales:** H01 (se conserva: la medida sigue siendo sobre pares
  predicción-resultado), H02 (se extiende: el borde pasa a las reglas de
  patrón, con pruebas en ambos lados); superficies S01 (resultados con
  periodo), S02 (límites y reglas), S03 (reporte por periodo y acción) y S04
  (pruebas por regla); índice de comparación externa («Umbral no
  justificado», «Una ventana»); dependencia «P424 no usa la alerta».
- **Adaptación declarada:** la severidad alta de la fuente es «desechar el
  modelo y desarrollar uno nuevo». En este curso, desarrollar un modelo nuevo
  es método de Predictiva. La respuesta operable es volver a la versión
  registrada anterior (P424) y pedir la reconstrucción como revisión
  pendiente. La severidad media («ajustar») se registra como solicitud de
  recalibración o reentrenamiento con revisión humana, sin ejecutarla. Para un
  error de clasificación sólo importa el límite superior: una mejora no es una
  falla. Los límites son los de una carta p con la proporción de errores de
  referencia. La política es dato versionado y aprobado por el profesor, no
  lógica de ML.
- **Alternativas menores descartadas:** añadir sólo un campo `action` al
  reporte actual conservaría el umbral sin justificar y reaccionaría a un
  único periodo, que es justo el defecto que la fuente critica. Una revisión
  por calendario fijo («replace models… at fixed intervals», p. 153) es la
  otra práctica común que la fuente descarta; puede declararse como revisión
  periódica en la política, pero no sustituye el disparo por condición.
  Cambiar a un caso de pronóstico con actuales semanales se ajustaría mejor a
  la fuente, pero rompería la continuidad con P403 que fija T01.
- **Contrato de no regresión:** se conservan H01, `evaluate_performance`,
  `test_01`, `test_02` y los campos actuales del reporte; los de T01 también,
  si se aprueba. La política se añade en un archivo de datos nuevo y la
  evaluación por periodo en archivos nuevos de `submission/`. No se
  reentrena ni se recalibra ningún modelo en P423. No se modifica P424: la
  acción `revertir` queda en el reporte para que P424 la consuma según su
  propia T01.
- **Interacciones:** depende de T01 (fuente de resultados con periodo,
  mínimo de observaciones y desempeño de habilitación de P403). Ver
  interacciones de T01 para la diferencia entre veredicto y acción. Con
  `P424_tasks.md` T01: la acción `revertir`, la regla disparada, los periodos
  y el identificador del reporte son la entrada que P424 copia. Si T02 se
  rechaza, P424 consume el veredicto `incumple` de T01 o, si tampoco existe,
  el `alert` actual. Con `P442_tasks.md` T01 (severidad → acción en la capa
  de calidad de datos): mismo patrón señal → severidad → acción en otra capa;
  si ambas se aprueban, conviene que la discusión fije un vocabulario común
  de severidades. Capacidad: ver T01; T02 es la candidata natural a sección
  final.
- **Criterio de aceptación:** S05 encuentra (1) `data/maintenance_policy.json`
  aprobado por el profesor con: reglas (patrón, sigma, severidad, acción),
  fecha de vigencia del modelo y, si se declara, revisión periódica; (2)
  `submission/performance_by_period.csv` con periodo, n, proporción de
  errores, límites superiores 2σ y 3σ calculados con el error de referencia
  de P403 y el n del periodo, evaluable (n ≥ mínimo de T01) y regla
  disparada; (3) `submission/maintenance_decision.json` con acción en {mantener,
  recalibrar_reentrenar_con_revision, revertir}, regla, periodos que la
  sustentan, fecha de vigencia, error de referencia, versión de la política e
  identificador del reporte; (4) un gráfico de control en `submission/` como
  evidencia visual; (5) pruebas de profesor para: un solo periodo sobre 3σ →
  mantener; dos periodos evaluables consecutivos sobre 3σ → revertir; tres
  sobre 2σ sin superar 3σ → recalibrar_reentrenar_con_revision; periodos
  anteriores a la vigencia ignorados; periodos insuficientes no evaluados;
  severidad mayor gana si se disparan varias; y (6) H01 y H02 presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P423_model_performance_monitoring/

0. Inspecciona primero el estado de la actividad. Si T01 no está ejecutada
   (no existen data/acceptance_criterion.json ni resultados con periodo del
   clasificador de P403), detente e informa: T02 depende de ese caso. Si la
   implementación no coincide con design/courses/productos/P423_activity.md
   más los cambios de T01, detente e informa.
1. POLÍTICA: no inventes reglas, acciones, fecha de vigencia ni revisión
   periódica. Usa la política que el profesor haya aprobado en la discusión
   de esta T02 (registrada en P423_log.md). Si no existe, detente y pídela.
   Una política de partida para discutir, tomada de la fuente y adaptada:
   - alta: 2 de 2 periodos evaluables consecutivos sobre 3σ → revertir;
   - media: 3 de 3 periodos evaluables consecutivos sobre 2σ → recalibrar_
     reentrenar_con_revision;
   - baja: un periodo sobre 3σ sin patrón → mantener (no sobrerreaccionar);
   - en otro caso → mantener.
   Persístela en data/maintenance_policy.json con approved_by y version.
2. Error de referencia: p0 = 1 - enablement_value de accuracy en
   data/acceptance_criterion.json (de P403). Para cada periodo t con n_t
   observaciones, límite superior kσ = p0 + k * sqrt(p0 * (1 - p0) / n_t),
   para k = 2 y 3. Sólo límite superior.
3. Añade evaluate_policy(outcomes, criterion, policy) que:
   a. agrupe por periodo y calcule n_t y la proporción de errores;
   b. marque no evaluables los periodos con n_t < minimum_observations y los
      anteriores a la fecha de vigencia; «consecutivos» se refiere a
      periodos evaluables;
   c. aplique las reglas y, si se disparan varias, elija la de mayor
      severidad;
   d. devuelva acción, regla y periodos que la sustentan.
4. Persiste submission/performance_by_period.csv (period, n, error_rate,
   ucl_2sigma, ucl_3sigma, evaluable, rule_fired),
   submission/maintenance_decision.json (action, rule, periods,
   model_vintage, reference_error, policy_version, report_id) y
   submission/control_chart.png (proporción de errores por periodo con los
   límites y la fecha de vigencia). Añade action y report_id a
   performance_report.json sin cambiar sus campos existentes.
5. Añade a professor/test_main.py una prueba por regla y borde, según el
   criterio de aceptación, con DataFrames pequeños. No elimines pruebas
   existentes.
6. Añade a tests/test_activity.py una prueba que verifique los dos archivos
   nuevos, sus columnas o campos, que action está en el vocabulario de la
   política y que el PNG existe. Rutas relativas al archivo de prueba.
7. Añade a HOW_TO_RUN_ME.txt un paso que pida explicar en 3–5 líneas por qué
   un solo periodo fuera del límite no basta para actuar, por qué los
   límites salen del error de habilitación y qué hace P424 con la acción
   revertir.
8. Ejecuta las pruebas de profesor y de la actividad sin errores.
9. No reentrenes ni recalibres ningún modelo. No modifiques P403, P424 ni
   otras actividades, traceability.yaml ni design/.
```
