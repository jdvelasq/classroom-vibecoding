# P321 — Propuestas de mejora

**Línea base:** `P321_activity.md` (entrada S02 más reciente: `S02.P321.01`).

## T01 — Aplicar el gatillo de revisión sobre una serie de seguimiento observada y registrar la decisión graduada: mantener, recalibrar o rediseñar/escalar

- **Estado:** pendiente de discusión
- **Tipo:** método + caso/datos + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` p. 7 — el dominio VII exige «ongoing oversight and calibration to ensure the analytics solution continues to perform effectively … over time» y enumera «Task 7.1 Track analytics solution performance», «Task 7.2 Recalibrate and maintain the analytics solution», «Task 7.4 Validate the business case for the analytics solution over time» y «Task 7.5 Analyze the side effects of the analytics solution over time»: el seguimiento con resultados y la recalibración son tareas del ciclo de vida, no una declaración (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general de ejercer el seguimiento, no un procedimiento.
  - `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` pp. 24–25 — objetivos verificables de nivel inicial: «CAP-E.7.1.1 Identify the metrics that monitor analytics solution performance» (p. 24), «CAP-E.7.4.1 Identify what has changed over time for the business case» y «CAP-E.7.5.1 Identify the importance of reviewing analytic solutions post deployment for unintended consequences» (p. 25); identificar el cambio exige datos posteriores a la puesta en operación (Claude, 2026-10-05). Fuente *authoritative*.
- **Qué gana el estudiante:** pasar de declarar un gatillo a operarlo. Hoy
  P321 construye un registro de una fila, en su mayoría texto fijo en
  `main.py`, y no tiene datos de seguimiento: el gatillo
  `service_rate < 0.90 durante la revisión semanal` nunca se evalúa
  (S02.P321.01, ambigüedad 3). Con una serie semanal del indicador, el
  estudiante (1) aplica el gatillo declarado y ve que un umbral único
  dispara por azar o tarda en detectar un deterioro sostenido; (2) lo
  sustituye por reglas graduadas tipo carta de control, con límites
  calculados en un periodo de referencia, que separan ruido de desviación
  sostenida; (3) traduce cada severidad en una decisión de ciclo de vida
  (mantener, recalibrar, rediseñar/escalar) con responsable y fecha; y (4)
  deja un historial de revisiones que hoy no existe (S03). Ninguna actividad
  del curso aplica un gatillo sobre resultados observados: P306, P308, P311,
  P315 y P319 declaran reglas de monitoreo o persistencia sin serie que las
  ejecute. Es la contribución que `activity-architecture.md` asigna a P321
  («Operación y monitoreo»; «Registro, indicadores y gatillos de revisión»)
  y la capacidad `prescriptiva.C05`; refuerza la identidad del taller en
  lugar de añadir otra.
- **Anclas actuales:** H01 (acción, alternativa no elegida y supuesto
  `demanda_esperada`, que el seguimiento pone a prueba), H02 (indicador,
  meta, gatillo, responsable y acción de revisión, que pasan de declarados a
  ejercidos), H03 (prueba `test_02` de columnas de gobernanza); superficies
  S01 (recomendación de entrada), S02 (construcción del registro), S03
  (registro sin historial de revisiones), S04 (pruebas). Dependencia: hoy
  «Recibe de Pxxx: … sin dependencia demostrable» de P311; esta propuesta
  sólo la crea si el vínculo puede hacerse explícito (ver instrucciones).
- **Alternativas menores descartadas:** aclarar en markdown que el gatillo
  debería aplicarse sobre datos no cambia lo que el estudiante practica.
  Aplicar sólo el umbral declarado sobre la serie enseña a evaluar una
  condición, pero no a distinguir ruido de deterioro, que es lo que
  justifica una respuesta graduada (Katz, p. 153). Moverlo a P311, que
  declara «dos incumplimientos en diez jornadas», mezclaría la prueba de la
  política antes de operar con su operación, y P311 ya tiene su propia
  identidad y su posible duplicación con P307 por resolver.
- **Contrato de no regresión:** se conservan H01–H03;
  `data/recommendation.csv` sin cambios; `submission/policy_register.csv`
  con sus 17 columnas actuales, en el mismo orden y con los mismos valores
  (sólo se admiten columnas nuevas al final); la función
  `create_policy_register` y su firma; `test_01` y `test_02` sin cambios.
  El gatillo declarado (`menor_a_0.90`) no se elimina: se evalúa sobre la
  serie como comparación y las reglas graduadas se añaden junto a él. No se
  corrige aquí el texto fijo de los demás campos del registro (ambigüedad 2
  de S02), que requiere otra decisión.
- **Interacciones:** única propuesta de este archivo. Fuera de P321: si se
  usa la derivación desde P311 y una propuesta futura cambia los datos o el
  método de P311 (S01–S02 de P311), los parámetros copiados en P321 deben
  revisarse; la derivación no crea una dependencia en tiempo de ejecución.
  Capacidad: P321 tiene tres highlights y un notebook corto; un highlight
  nuevo cabe en la sesión, pero la parte de reglas graduadas (paso 4) puede
  quedar como sección final para un grupo lento si el paso 3 (umbral único)
  ya muestra el problema.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo (H04) en el
  que (1) existe una serie de seguimiento semanal de `service_rate` con su
  procedencia declarada en `data/` (derivada de P311 con el vínculo
  explícito, o sintética rotulada como artefacto didáctico); (2) el gatillo
  declarado se evalúa sobre la serie y se contrasta con reglas graduadas
  cuyos límites se calculan sólo con el periodo de referencia; (3) cada
  periodo revisado queda en `submission/policy_review_log.csv` con regla
  activada, severidad, decisión (`mantener`, `recalibrar`,
  `redisenar_escalar`), responsable y fecha; y (4) pruebas nuevas verifican
  esquema, valores permitidos, coherencia severidad–decisión y que el
  registro conserva sus 17 columnas. H01–H03 siguen presentes y `test_01`
  y `test_02` pasan.

### Instrucciones de ejecución

```text
Actividad: implementation/prescriptiva/P321_comunicacion_y_seguimiento_politicas/

0. Inspecciona primero data/recommendation.csv, professor/main.py,
   professor/notebook.ipynb, notebooks/notebook.ipynb, submission/ y
   tests/test_activity.py. Si la implementación no coincide con
   design/courses/prescriptiva/P321_activity.md, detente e informa la
   discrepancia sin modificar nada. Si ya existen datos de seguimiento o el
   gatillo ya se evalúa sobre resultados, detente e informa: la propuesta
   estaría cubierta.
1. PROCEDENCIA DE LA SERIE. No inventes procedencia ni la presentes como
   observación real.
   a. Inspecciona, sólo para lectura,
      implementation/prescriptiva/P311_evaluacion_politicas_por_simulacion/
      data/capacity_policies.csv, data/demand_scenarios.csv y
      submission/capacity_policy_decision.json. Usa la derivación desde P311
      sólo si se cumplen las tres condiciones: la política elegida en P311
      se llama refuerzo_flexible (igual que recommended_action en
      recommendation.csv), su meta de servicio es 0.90 y la tasa de servicio
      por escenario puede calcularse como min(1, capacidad / demanda). En
      ese caso copia a data/ de P321 sólo los parámetros necesarios
      (capacidad de la política elegida, escenarios de demanda y sus
      probabilidades, servicio esperado) en
      data/followup_parameters.csv; no leas P311 en tiempo de ejecución.
   b. Si alguna condición falla, no fuerces el vínculo: usa parámetros
      propios declarados en data/followup_parameters.csv y escribe en
      markdown que la serie no proviene de ninguna actividad previa.
   c. Genera con semilla fija una serie diaria de demanda y agrégala a
      semanas (service_rate semanal = atendidos / demanda de la semana).
      Usa al menos 12 semanas de referencia generadas con los parámetros de
      la política y al menos 12 semanas de seguimiento. Si incluyes un
      cambio en el segmento de seguimiento (p. ej. desplazamiento de la
      demanda que rompe el supuesto demanda_esperada), decláralo como
      perturbación didáctica con su magnitud y semana de inicio, para que
      la revisión ponga a prueba H01. Las fechas son semanas didácticas,
      no calendario operativo real.
   d. Persiste data/followup_series.csv (columnas: week_start, segment
      [referencia|seguimiento], demand, served, service_rate) y
      data/followup_provenance.md con: origen (derivada de P311 con las
      rutas y condiciones verificadas, o sintética propia), semilla,
      parámetros, perturbación si existe y la frase «artefacto didáctico
      derivado; no son observaciones reales». Si P311 tampoco declara
      procedencia, dilo.
2. No cambies recommendation.csv, la firma de create_policy_register, las
   17 columnas de policy_register.csv ni sus valores, test_01 ni test_02.
3. GATILLO DECLARADO. Añade una sección «Aplicar el gatillo declarado»:
   evalúa service_rate < 0.90 en cada semana (referencia y seguimiento),
   cuenta cuántas veces dispara en el periodo de referencia, generado con
   la política funcionando según su supuesto, y explica en 3–5 líneas qué
   significa una alarma en ese periodo (azar) y si el umbral detecta a
   tiempo el cambio del segmento de seguimiento.
4. REGLAS GRADUADAS. Añade una sección «Reglas graduadas de revisión»:
   a. Calcula la línea central y la dispersión sólo con el periodo de
      referencia (carta de individuos con rango móvil, sigma = MR medio /
      1.128) sobre la desviación service_rate − servicio esperado de la
      política (o sobre service_rate si no hay servicio esperado
      declarado). Menciona en markdown que la tasa está acotada en 1 y que
      por eso sólo interesa el límite inferior.
   b. Declara en una tabla las reglas y su severidad, por ejemplo:
      redisenar_escalar = 2 semanas seguidas bajo el límite de 3 sigma, o
      service_rate bajo la meta 0.90 durante N semanas seguidas (N
      declarado); recalibrar = 3 semanas seguidas bajo 2 sigma, o 5
      semanas seguidas decrecientes; mantener = ninguna regla activa (un
      punto aislado fuera de 3 sigma se anota pero no cambia la política).
      Si una semana activa reglas de distinta severidad, prevalece la mayor.
   c. Aplica las reglas semana a semana en el segmento de seguimiento, sin
      recalcular límites con datos de seguimiento.
   d. Grafica la serie con línea central, límites de 2 y 3 sigma, la meta
      0.90 y las semanas con regla activa; guarda
      submission/followup_control_chart.png.
   e. Explica en 4–6 líneas la diferencia con el paso 3 y qué haría la
      autoridad en cada severidad: recalibrar ajusta parámetros de la
      política (p. ej. capacidad) sin cambiar su forma; redisenar_escalar
      lleva la política a la autoridad declarada para reemplazarla o
      retirarla.
5. REGISTRO DE REVISIONES. Persiste submission/policy_review_log.csv, una
   fila por semana de seguimiento, con columnas: week_start, service_rate,
   declared_trigger_fired, rule_fired, severity [baja|media|alta],
   review_decision [mantener|recalibrar|redisenar_escalar], review_owner,
   review_date, rationale. review_owner toma el valor de review_owner del
   registro actual (no lo inventes); review_date es la fecha de revisión de
   esa semana didáctica. Puedes añadir al final de policy_register.csv las
   columnas graded_review_rules, last_review_date y last_review_decision,
   sin alterar las existentes.
6. Pon la lógica en funciones de professor/main.py (generación de la serie,
   cálculo de límites, aplicación de reglas, construcción del log) e
   impórtalas desde el notebook de profesor. Si el notebook del estudiante
   sigue vacío, no lo completes: añade sólo una celda markdown con la
   consigna de la nueva sección.
7. Añade a tests/test_activity.py, sin eliminar pruebas existentes:
   a. followup_series.csv y followup_provenance.md existen; la serie tiene
      las columnas del paso 1d, al menos 12 semanas por segmento y
      service_rate en [0, 1]; la procedencia contiene «artefacto
      didáctico».
   b. policy_review_log.csv existe, tiene las columnas del paso 5, sólo
      valores permitidos en severity y review_decision, review_owner y
      review_date sin vacíos, y la decisión es coherente con la severidad
      (baja→mantener, media→recalibrar, alta→redisenar_escalar).
   c. policy_register.csv conserva sus 17 columnas originales en el mismo
      orden.
   d. followup_control_chart.png existe.
8. Ejecuta el notebook de profesor completo y las pruebas de la actividad
   sin errores.
9. No modifiques P311 ni otras actividades, traceability.yaml ni design/.
```
