# P306 — Propuestas de mejora

**Línea base:** `P306_activity.md` (entrada S02 más reciente: `S02.P306.01`).

## T01 — Conservar un grupo de control aleatorio en la operación para medir el efecto de la política y poder recalibrarla

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia + proceso
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` pp. 24–25 — CAP-P.7.2.1 «Identify potential opportunities for recalibration of the analytics solution» (p. 24); Task 7.4 «Validate the business case for the analytics solution over time» y CAP-P.7.4.1 «Identify which benefit is attributable to the analytics solution over time» (p. 25): una solución en operación debe poder atribuir su beneficio y recalibrarse (Claude, 2026-10-05). Fuente *authoritative*: fija la expectativa de atribución y recalibración; no prescribe el diseño con grupo de control.
  - `design/benchmarks-md/institutional/cambridge-business-analytics.md` pp. 2, 6–7 — «cómo configurar experimentos… cómo aprender de los datos» y «Estaremos siempre probando, experimentando y modificando cosas» (p. 2); «Diseña experimentos para recopilar datos significativos para tomar decisiones basadas en datos» (p. 6); Módulo 4 «El estándar de oro», «Hacer que la experimentación funcione» (p. 7) (Claude, 2026-10-05). Fuente *institutional* y genérica: respalda la experimentación continua como práctica, no el diseño concreto.
  - `design/benchmarks-md/literature-derived/dataops-02-data-strategy.md` p. 23 — «La contribución no siempre implica una causalidad demostrada… deben explicitarse los supuestos y, cuando sea viable, utilizar pilotos, grupos de comparación, series temporales u otros diseños de evaluación»; la ficha de indicador exige «Decisión asociada: la acción que puede desencadenar su resultado» (Claude, 2026-10-05). Fuente *literature-derived*, en contexto de estrategia de datos y no de políticas: respalda el principio metodológico.
- **Qué gana el estudiante:** entender que una política que focaliza por
  efecto causal estimado destruye, al operar, la aleatorización que permitió
  estimarlo, y diseñar la forma de evidencia que lo evita. Hoy P306 valida
  sus reglas contra `synthetic_truth.csv`, una verdad que «no existe en
  operación real» (S02, «Uso y límite»), y `monitoring_plan.csv` pide
  «retención observada por lote» sin contrafactual: la retención de los
  contactados no dice cuánto de ella causó la oferta (ambigüedad 3 de
  `S02.P306.01`; S05: «sin grupo de control en la operación propuesta»).
  Con la mejora, el estudiante reserva al azar una fracción de los clientes
  que la política seleccionaría, la declara en el contrato y en el registro,
  calcula con la verdad sintética cuánto valor incremental cuesta esa
  reserva, cuántos lotes hacen falta para que el efecto observado sea
  informativo, y convierte la diferencia tratados − reserva en una métrica
  de monitoreo con gatillo de recalibración. Ningún taller conserva
  capacidad de aprendizaje causal en la operación: P322 mide antes de una
  decisión única y P308 compara observado con estimado sin contrafactual.
- **Anclas actuales:** H01 (aleatorización de `retention_offer` como
  condición de identificación), H04 y H06 (valor incremental verdadero bajo
  cupo y rendimientos decrecientes, que permiten valorar la reserva), H07
  (banda de revisión, `monitoring_plan.csv` con la acción «recalibrar» y la
  métrica «retención observada por lote»), H08 (registro operativo sin
  columnas de verdad); superficies S03 (validación), S04 (`rank_top_k`,
  K = 160), S05 (producto/gobierno) y S06 (pruebas); dependencias «Recibe de
  P303/P305» y formato de `monitoring_plan.csv` retomado en P308.
- **Alternativas menores descartadas:** declarar en markdown que falta un
  contrafactual ya está hecho en S02 y no da al estudiante un mecanismo.
  Añadir sólo la métrica al plan de monitoreo, sin reserva en el registro,
  dejaría una métrica imposible de calcular.
- **Contrato de no regresión:** se conservan H01–H08, la partición, el
  T-learner, las cuatro reglas congeladas, `policy_comparison.csv` y
  `capacity_sensitivity.csv` con su esquema y valores actuales (la
  comparación de reglas sigue sin reserva). La reserva se añade como una
  capa operativa sobre la regla de valor causal: `decision_register.csv` y
  `targeting_decisions.csv` ganan columnas, sin perder las actuales ni
  exponer columnas de verdad (H08). El costo de la reserva se evalúa con la
  verdad sintética sólo en un artefacto de validación nuevo. Las pruebas
  existentes se mantienen.
- **Interacciones:** única propuesta de P306. Capacidad: P306 ya tiene ocho
  highlights y siete artefactos; conviene decidir en la discusión si la
  sección de reserva queda al final como bloque que un grupo lento puede
  completar en la sesión siguiente. Límite declarado: una reserva dentro de
  los seleccionados mide el efecto de la oferta en la población focalizada y
  permite recalibrar el corte y el efecto estimado allí; recalibrar el
  T-learner fuera de esa población exigiría además exploración aleatoria
  entre los no seleccionados, que esta T01 no propone.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que
  (1) una fracción aleatoria y reproducible de los clientes seleccionados se
  marca como reserva en `decision_register.csv`, con la fracción declarada en
  `policy_contract.json`; (2) el costo de la reserva (valor incremental
  verdadero que se deja de capturar) y el número de lotes necesarios para
  estimar el efecto observado se reportan para varias fracciones en un CSV de
  validación; (3) `monitoring_plan.csv` contiene una métrica de efecto
  observado (tratados − reserva, acumulado por lotes) con gatillo derivado de
  datos de la actividad y acción «recalibrar»; y (4) pruebas verifican esos
  artefactos y que el registro no expone columnas de verdad. H01–H08 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/prescriptiva/P306_credit_campaign_targeting/

0. Inspecciona primero data/campaign.csv, data/synthetic_truth.csv,
   professor/notebook.ipynb, submission/ y tests/. Si la implementación no
   coincide con design/courses/prescriptiva/P306_activity.md, o si la
   operación ya conserva un grupo de control, detente e informa sin
   modificar nada.
1. No cambies la partición, el T-learner, las cuatro reglas, su
   congelamiento, K = 160, el costo 5 ni policy_comparison.csv y
   capacity_sensitivity.csv.
2. FRACCIÓN DE RESERVA: no la inventes como valor operativo. Evalúa una
   rejilla (por ejemplo 0 %, 5 %, 10 %, 20 % de los K seleccionados) y usa
   como fracción operativa la que el profesor apruebe en la discusión de
   esta T01 (registrada en P306_log.md). Si no existe, completa los pasos 3
   y 4 con la rejilla, detente antes del paso 5 y pídela.
3. Después de la sección de gobierno (H07), añade «Grupo de control en la
   operación»:
   a. Explica en 3–5 líneas por qué la regla de valor causal deja de
      generar clientes no tratados comparables y por qué la retención de
      los contactados no es el efecto de la oferta.
   b. Para cada fracción h de la rejilla, sortea con semilla fija
      round(h * K) clientes entre los seleccionados por la regla de valor
      causal como reserva (sin oferta).
   c. Con synthetic_truth.csv, y sólo aquí, calcula el valor incremental
      verdadero capturado con y sin reserva y su diferencia (costo de la
      reserva).
   d. Con las probabilidades potenciales verdaderas de los seleccionados,
      calcula el error estándar de la diferencia de retención tratados −
      reserva por lote y el número de lotes semanales necesarios para que
      un intervalo del 90 % excluya cero dado el efecto medio verdadero de
      los seleccionados. Grafica costo y lotes necesarios contra h.
   e. Explica en 3–5 líneas el intercambio entre valor sacrificado y
      rapidez de aprendizaje, sin elegir la fracción por el profesor.
4. Persiste submission/holdout_tradeoff.csv con columnas holdout_fraction,
   holdout_size, true_value_captured, holdout_cost, se_effect_per_batch,
   batches_to_detect, y la figura en submission/holdout_tradeoff.png.
5. Con la fracción aprobada:
   a. Añade a decision_register.csv y targeting_decisions.csv una columna
      holdout (booleana) y, para la reserva, acción sin oferta con
      decision_status explícito (por ejemplo "holdout_control"). No añadas
      columnas de verdad.
   b. Añade a policy_contract.json una clave (por ejemplo "holdout") con
      fracción, semilla, población (seleccionados por la política) y el
      propósito declarado (medir el efecto y recalibrar).
   c. Añade a monitoring_plan.csv una fila: métrica «efecto observado
      acumulado (retención tratados − reserva)», cadencia semanal, gatillo
      «el intervalo del 90 % acumulado excluye el uplift_hat medio de los
      seleccionados» (valor calculado en el notebook a partir de los datos,
      no fijado a mano), acción «recalibrar», autoridad la ya declarada.
      Conserva las cuatro filas actuales.
6. Añade a tests/ pruebas que verifiquen: que holdout_tradeoff.csv existe
   con esas columnas y holdout_cost >= 0; que decision_register.csv tiene
   la columna holdout con una fracción de reservas igual a la del contrato
   (redondeo incluido) y sólo entre seleccionados; que ningún archivo de
   registro contiene columnas de synthetic_truth.csv; y que
   monitoring_plan.csv tiene la fila de efecto observado con acción
   recalibrar. No elimines pruebas existentes.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
