# P423 — Propuestas de mejora

**Línea base:** `P423_activity.md` (entrada S02 más reciente: `S02.P423.01`).

## T01 — Monitorear con el criterio de aceptación con que P403 habilitó el modelo, derivar el umbral de la medida de éxito y la línea base, y exigir una ventana mínima (veredicto cumple/incumple/insuficiente)

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia (corrige un defecto)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` pp. 5 y 7 — «Task 2.4 Define primary measures of success» y «Task 2.5 Identify baseline performance of the current state» (p. 5); en la gestión del ciclo de vida, «Task 7.1 Track analytics solution performance» y «Task 7.4 Validate the business case for the analytics solution over time» (p. 7): el seguimiento en operación se juzga contra la medida de éxito y la línea base declaradas al encuadrar, no contra una constante nueva (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general, no un procedimiento.
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
