# P307 — Propuestas de mejora

**Línea base:** `P307_activity.md` (entrada S02 más reciente: `S02.P307.01`).

## T01 — Construir los escenarios de pedido a partir del error de pronóstico fuera de muestra en el horizonte de la decisión

- **Estado:** pendiente de discusión
- **Tipo:** caso/datos + método
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/sas-forecasting.md` pp. 9, 99–100, 129, 144 y 168 — «use rolling simulations to evaluate forecast accuracy over the number of periods you need to forecast» (p. 9) y «to evaluate ex-ante forecast performance over several forecast origins» (p. 99); «Rolling simulations (also called rolling horizon) mimic how the forecast model performs over time» (p. 100); los pronósticos se distinguen por «LEADTIME, which is the interval in the future for which they are created» (p. 129); «the information that “75% of the time series have a forecast error smaller than x” is more important than the average forecast error» (p. 144); «having perfect fit to history is no guarantee that the model will generate accurate forecasts» (p. 168): la incertidumbre relevante es el error fuera de muestra al plazo de uso, leído por cuantiles (Claude, 2026-10-05). Fuente *professional-learning* y única: la propuesta se sostiene en el defecto registrado por S02, no en el prestigio de la fuente.
- **Qué gana el estudiante:** entender que la incertidumbre que debe
  absorber una política de pedido es el error del pronóstico en el plazo en
  que se decide, medido fuera de muestra, y convertir un pronóstico puntual
  más esa distribución de error en los escenarios de demanda de la
  política. Hoy el «pronóstico» son tres escenarios dados (80/110/150 con
  0,25/0,50/0,25) sin procedencia, las cantidades candidatas coinciden con
  ellos y la guardia de servicio no cambia la decisión: 110 es también el
  máximo sin restricción y queda en el borde de 0,25 (S02; ambigüedades 1 y
  4 de `S02.P307.01`: «no hay pronóstico construido»). Con escenarios
  empíricos y una rejilla de cantidades, el estudiante ve que el pedido que
  maximiza el valor esperado queda donde lo fija la razón entre costo de
  faltante y de sobrante, y que la guardia de servicio mueve la decisión
  cuando esa razón deja un riesgo de quiebre mayor que el tolerado. Con los
  parámetros actuales (precio 25, costo 12, disposición 2) esa razón es
  13 / 27 ≈ 0,48, lo que sugiere que la guardia de 0,25 sí discriminará;
  S04 debe verificarlo con los datos reales. Materializa C02 («distinguiendo
  evidencia predictiva de la decisión que la utiliza»). Frontera: el
  pronóstico y sus errores fuera de muestra llegan como insumo (producto de
  Predictiva); P307 no construye, selecciona ni valida modelos de
  pronóstico, sólo consume la distribución de error en la política.
- **Anclas actuales:** H01 (pronóstico como distribución de escenarios y
  gobierno como datos), H02 (valor esperado y quiebre por cantidad), H03
  (guardia antes de maximizar; hoy no discrimina), H04 (política de una fila
  con cadencia, aprobación y gatillo); superficies S01
  (`forecast_scenarios.csv`, `order_options.csv`, `policy_contract.csv`:
  «candidatas = escenarios; sin procedencia»), S02 (`evaluate_order_options`,
  `select_order_policy`), S03 (producto), S04 (pruebas) y S05 (notebook sin
  evidencia visual); dependencia «Recibe de P300/P302/P304».
- **Alternativas menores descartadas:** cambiar a mano los tres escenarios
  o la guardia para que ésta discrimine corregiría el síntoma con datos tan
  arbitrarios como los actuales. Ampliar sólo la rejilla de cantidades sin
  cambiar el origen de los escenarios seguiría sin conectar la política con
  el error real del pronóstico.
- **Contrato de no regresión:** se conservan H02–H04, `evaluate_order_options`
  y `select_order_policy` (generalizadas a N escenarios y M cantidades sin
  cambiar su lógica: vendidas, sobrantes, valor, quiebre; filtrar por guardia
  y maximizar), los parámetros de `policy_contract.csv` (cadencia, dueño,
  guardia 0,25, aprobación, gatillo) y de `order_options.csv` (costo 12,
  precio 25, disposición 2), y las columnas de `order_policy.csv` y
  `order_evaluation.csv`. H01 se modifica: los escenarios dejan de ser una
  tabla dada y se construyen a partir del pronóstico y su error; el
  notebook conserva la versión de tres escenarios como contraste inicial.
  Las pruebas existentes se mantienen (una fila y siete columnas).
- **Interacciones:** única propuesta de P307. Depende de la decisión de curso
  pendiente sobre la posible duplicación con P300/P302 y el solapamiento con
  P304 que registra S02 (ambigüedad 6): si P307 se fusiona o reubica, esta
  T01 debe trasladarse con su contribución (pronóstico → política). Según
  la señal de extracción, P313 fija a mano `FORECAST_ERROR_SD`; la misma
  idea podría aplicarse allí en una propuesta propia, no en esta T01.
  Capacidad: P307 tiene cuatro highlights y un notebook de dos celdas, así
  que el cambio cabe en la sesión.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que
  (1) los escenarios de demanda se construyen como pronóstico puntual más
  los errores fuera de muestra al plazo de la decisión, tomados de una
  fuente trazable aprobada por el profesor; (2) se evalúa una rejilla de
  cantidades distinta de los escenarios; (3) el notebook muestra la cantidad
  óptima sin guardia y con guardia, y si la guardia cambia o no la decisión;
  y (4) `forecast_error_scenarios.csv` y la evaluación ampliada están en
  `submission/` con pruebas. H02–H04 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/prescriptiva/P307_decision_informada_por_pronosticos/

0. Inspecciona primero data/ (forecast_scenarios.csv, order_options.csv,
   policy_contract.csv), professor/main.py (evaluate_order_options,
   select_order_policy, evaluate), professor/notebook.ipynb, src/,
   submission/ y tests/. Si la implementación no coincide con
   design/courses/prescriptiva/P307_activity.md, detente e informa sin
   modificar nada.
1. CASO Y DATOS: no inventes una serie ni sus errores. Usa la fuente que
   el profesor haya aprobado en la discusión de esta T01 (registrada en
   P307_log.md): preferentemente un caso trazable de datalabs/, catalog/ o
   DataCamp, o un artefacto de una actividad de Predictiva, que contenga
   por período el pronóstico emitido en el origen, el valor real y el
   plazo (lead time) igual al de la decisión de pedido. Si la fuente sólo
   trae la serie de demanda sin pronósticos fuera de muestra, o si el
   plazo no coincide con el de la decisión, detente y pídelo: construir
   el pronóstico es tarea de Predictiva. Documenta en data/ (o en
   markdown) la procedencia, la transformación y sus límites. Si el caso
   implica unidades, precios o costos distintos de order_options.csv, el
   profesor debe aprobarlos; si no, conserva 12/25/2.
2. En el notebook, conserva al inicio la evaluación actual con tres
   escenarios como contraste y añade «Escenarios desde el error de
   pronóstico»:
   a. Calcula los errores fuera de muestra (real − pronóstico) al plazo de
      la decisión y muéstralos (histograma y cuantiles 10/25/50/75/90).
   b. Contrasta en 2–3 líneas ese error con el error de ajuste en muestra
      si la fuente lo trae; si no, explica por qué el ajuste histórico no
      sirve como medida de incertidumbre.
   c. Construye los escenarios como pronóstico puntual de la semana a
      decidir más cada error empírico (o sus cuantiles), con probabilidad
      uniforme o de cuantil, truncando en cero.
3. Generaliza evaluate_order_options y select_order_policy a N escenarios
   y M cantidades sin cambiar su lógica, y evalúa una rejilla de cantidades
   entre los cuantiles 5 y 95 de la demanda construida (paso de 1 unidad o
   el que el profesor apruebe).
4. Muestra en una tabla y en un gráfico valor esperado y probabilidad de
   quiebre contra la cantidad, marcando el óptimo sin guardia, el óptimo
   con guardia (quiebre <= el valor de policy_contract.csv) y la razón
   crítica (precio − costo) / (precio + disposición). Explica en 3–5 líneas
   si la guardia cambia la decisión y cuánto valor esperado cuesta. Si con
   los datos aprobados la guardia no cambia la decisión, dilo: no ajustes
   parámetros para forzarlo.
5. Persiste submission/forecast_error_scenarios.csv con columnas
   scenario_id, point_forecast, forecast_error, demand, probability;
   amplía submission/order_evaluation.csv con las cantidades de la rejilla
   (mismas columnas) y añade a submission/order_policy.csv, sin quitar las
   siete columnas actuales, unconstrained_quantity y guard_binding. Guarda
   el gráfico en submission/.
6. Añade a tests/ pruebas que verifiquen: que forecast_error_scenarios.csv
   existe con esas columnas, probabilidades que suman 1 y demanda >= 0;
   que order_evaluation.csv tiene más cantidades que escenarios originales;
   que la cantidad elegida en order_policy.csv cumple la guardia y tiene el
   mayor valor esperado entre las que la cumplen; y que guard_binding es
   coherente con unconstrained_quantity. No elimines pruebas existentes.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
