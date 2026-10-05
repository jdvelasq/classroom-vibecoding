# P303 — Propuestas de mejora

**Línea base:** `P303_activity.md` (entrada S02 más reciente: `S02.P303.01`).

## T01 — Derivar los umbrales de aprobar/escalar/rechazar del costo de cada tipo de error y declararlos en el contrato

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` pp. 56–58 — «A cost matrix is a convenient mechanism for changing the probability thresholds for model scoring» (p. 56); «if a model classifies a customer with poor credit as low risk, this error is costly» y la matriz de costo sirve «to influence the deployment of the model» (p. 57); el ejemplo asigna costos distintos a falso negativo, falso positivo y beneficio del verdadero negativo (1.500 / 300 / −10) (p. 58): el corte de probabilidad que gobierna una acción se fija con el costo de cada error, no con la exactitud (Claude, 2026-10-05). Fuente *professional-learning* y única: aporta el mecanismo costo → umbral; la franja de escalamiento por costo de revisión es una extensión del curso que la fuente no trata.
- **Qué gana el estudiante:** justificar con una pérdida esperada los cortes
  que separan aprobar, escalar y rechazar, en lugar de recibirlos como
  números fijos. Hoy `apply_review_policy` usa 0,08 y 0,30 sin derivación y
  el contrato no los declara (S02; ambigüedad 2 de `S02.P303.01`; «Uso y
  límite»: «No justifica los umbrales… ni los declara en el contrato»). Con
  la mejora, el estudiante ve que el corte de decisión automática resulta de
  comparar el costo esperado de aprobar a quien incumple con el de rechazar a
  quien paga (p* = C_rechazo / (C_rechazo + C_aprobación)), que la franja de
  escalamiento tiene sentido sólo donde la pérdida esperada de la mejor acción
  automática supera el costo de la revisión humana, y que los umbrales son
  parámetros revisables del contrato, ligados a supuestos de costo que pueden
  cambiar. Ningún taller del curso deriva un corte de acción a partir del
  costo de los errores de un puntaje. La probabilidad sigue llegando dada: no
  se estima, valida ni calibra modelo alguno (frontera con Predictiva).
- **Anclas actuales:** H01 (precedencia documentación → monto → riesgo),
  H02 (separa puntaje de acción), H04 (salvaguardas en el contrato);
  superficies S01 (dataset sin costos), S02 (`apply_review_policy`: «Umbrales
  0,08 / 0,30 / 10.000 sin derivación») y S03 (contrato «sin umbrales
  numéricos ni límite delegable explícito»); dependencia «Habilita para
  P306» (práctica de regla por entidad con registro).
- **Alternativas menores descartadas:** declarar 0,08 y 0,30 en el contrato
  sin derivarlos haría visible el número, pero no enseñaría de dónde sale ni
  cuándo revisarlo. Una sensibilidad sobre umbrales arbitrarios muestra que
  la acción cambia, pero no qué umbral elegir.
- **Contrato de no regresión:** se conservan H01 (la precedencia y las
  autoridades por motivo: documentación incompleta al gestor, monto > límite
  delegable al supervisor, riesgo al final), H03 (`policy_version`,
  `reason`, `human_authority`, `review_trigger`, `outcome_to_monitor`) y H04
  (salvaguardas actuales). El límite delegable de 10.000 no se deriva en esta
  T01 y se mantiene. Se sustituyen sólo los literales 0,08 y 0,30 por
  umbrales calculados; si cambian acciones de A01–A06, H02 se actualiza con
  los valores nuevos y el notebook muestra la tabla antes/después. La
  política sube a una versión nueva (por ejemplo, «P303-v2»). Las columnas
  actuales de `review_policy.csv` y las pruebas existentes se mantienen.
- **Interacciones:** única propuesta de P303. Capacidad: P303 tiene cuatro
  highlights y un notebook de tres celdas, así que el cambio cabe en la
  sesión. Si en el futuro se propone registrar la decisión humana final
  (límite de H03), esta T01 le daría los costos con que evaluarla.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que
  (1) los costos de aprobar a quien incumple, de rechazar a quien paga y de
  la revisión humana provienen de un texto aprobado por el profesor o de
  datos presentes en la actividad, con su procedencia, nunca inventados;
  (2) los umbrales de aprobación y rechazo se calculan con esos costos;
  (3) `policy_contract.json` declara costos, fórmula, umbrales resultantes y
  el límite delegable; y (4) una prueba verifica que el contrato contiene los
  umbrales y que la acción de cada solicitud en `review_policy.csv` es
  coherente con ellos. H01, H03 y H04 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/prescriptiva/P303_politicas_y_supervision_humana/

0. Inspecciona primero data/applications.csv, professor/main.py
   (apply_review_policy, policy_contract), professor/notebook.ipynb,
   src/, submission/ y tests/. Si la implementación no coincide con
   design/courses/prescriptiva/P303_activity.md (por ejemplo, los umbrales
   ya se derivan de costos o ya figuran en el contrato), detente e informa
   sin modificar nada.
1. COSTOS: no inventes costos. Usa los valores que el profesor haya
   aprobado en la discusión de esta T01 (registrados en P303_log.md) o que
   se deriven de columnas presentes en data/ con procedencia documentada.
   Se necesitan tres: C_aprob (costo de aprobar a quien incumple),
   C_rech (costo de rechazar a quien paga) y C_rev (costo de una revisión
   humana), y la decisión del profesor sobre si escalan con el monto
   solicitado. Si falta cualquiera, detente y pídelo. Escribe en markdown
   su procedencia y el supuesto de que la revisión humana resuelve el caso.
2. DERIVACIÓN, en una función nueva (por ejemplo derive_risk_thresholds)
   en el mismo módulo que apply_review_policy:
   a. Pérdida esperada de aprobar: p * C_aprob; de rechazar:
      (1 - p) * C_rech.
   b. Umbral de indiferencia p* = C_rech / (C_rech + C_aprob).
   c. Escalar cuando la pérdida esperada de la mejor acción automática
      supera C_rev: aprobar si p * C_aprob <= C_rev y p <= p*; rechazar si
      (1 - p) * C_rech <= C_rev y p > p*; escalar en otro caso. Esto da
      umbral_aprobar = min(C_rev / C_aprob, p*) y
      umbral_rechazar = max(1 - C_rev / C_rech, p*). Si los costos escalan
      con el monto, calcula los umbrales por solicitud.
   d. Si C_rev es tan alto que no queda franja de escalamiento, muéstralo y
      explícalo; no fuerces una franja.
3. Sustituye en apply_review_policy los literales 0,08 y 0,30 por los
   umbrales derivados. No cambies la precedencia (documentación → monto →
   riesgo), las autoridades ni el límite delegable de 10.000.
4. En el notebook añade, después de la aplicación actual de la regla:
   a. una tabla con los costos, p* y los dos umbrales;
   b. un gráfico de la pérdida esperada de aprobar, rechazar y escalar
      (C_rev) contra p en [0, 1], con las probabilidades de las seis
      solicitudes marcadas;
   c. una tabla antes/después con la acción de cada solicitud con los
      umbrales 0,08/0,30 y con los derivados;
   d. 3–5 líneas sobre por qué el corte depende de la asimetría de los
      errores y no de la exactitud, y qué cambio de costo obligaría a
      revisarlo.
5. Persiste en submission/policy_contract.json, sin borrar claves
   existentes, una clave nueva (por ejemplo "risk_thresholds") con
   C_aprob, C_rech, C_rev, procedencia, fórmula, umbral_aprobar,
   umbral_rechazar y delegable_amount_limit = 10000. Cambia policy_version a
   "P303-v2" en review_policy.csv y en el contrato. Guarda el gráfico en
   submission/expected_loss_thresholds.png.
6. Añade a tests/ pruebas que verifiquen: que el contrato contiene
   risk_thresholds con umbral_aprobar <= umbral_rechazar en [0, 1]; que toda
   solicitud con documentación completa y monto <= límite cuya acción sea
   aprobar tiene probabilidad <= umbral_aprobar y toda rechazada tiene
   probabilidad >= umbral_rechazar; y que el PNG existe. No elimines pruebas
   existentes.
7. Ejecuta el notebook completo y las pruebas de la actividad sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
