# P320 — Propuestas de mejora

**Línea base:** `P320_activity.md` (entrada S02 más reciente: `S02.P320.01`).

## T01 — Ejecutar la corrección de la política suspendida y medir cuánto beneficio cuesta cumplir la guarda de equidad

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia (con reparación previa del notebook como
  precondición)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 41, 108–109 — «the ethical issues should be seen to pervade the whole curriculum» (p. 41); PR-Ethical Considerations pide conocer «mechanisms for checking and avoiding bias» y «Algorithmic transparency and accountability» (p. 108) y la disposición «Responsive to issues of bias and be proactive in seeking to remove these» (p. 109): no basta detectar el sesgo, hay que actuar para removerlo y rendir cuentas (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general, no un método de corrección.
- **Qué gana el estudiante:** completar el ciclo detectar → corregir →
  reverificar → rendir cuentas del costo. Hoy P320 audita, decide
  «suspend_and_correct» para P1 y se detiene: no hay corrección (S02,
  ambigüedad 2; índice: «No hay corrección propuesta para P1»), aunque
  `activity-architecture.md` define el producto como «auditoría de equidad y
  corrección de política». Tampoco discute que P1 entrega más beneficio total
  que P0 (21.000 frente a 18.000, H02) concentrándolo en el grupo A. Con el
  cambio, el estudiante construye una variante corregida de P1 que reasigna
  contactos entre grupos dentro de la misma capacidad de contacto, la pasa
  por la misma guarda (brecha de tasa de contacto ≤ 0,10), cuantifica cuánto
  beneficio agregado cuesta cumplirla frente a P1 y cuánto conserva frente a
  P0, y deja la decisión con la autoridad ya declarada. Sale con una
  política aprobable y una razón explícita del intercambio, no con una
  suspensión sin salida. Ningún Pxxx del curso corrige una política reprobada
  por una guarda de equidad (P305, P306 y P308 sólo la declaran como límite).
- **Anclas actuales:** H01 (la guarda decide), H02 (beneficio y acceso
  auditados por separado), H03 (autoridad de cumplimiento y escalamiento al
  comité); superficies S01 (`data/policy_impacts.csv`), S02 (funciones de
  auditoría y decisión en `professor/main.py`), S03 (`equity_audit.csv`,
  `policy_correction_decisions.csv` sin corrección), S04 (contrato y
  monitoreo), S05 (`professor/notebook.ipynb`, no ejecutable) y S06
  (`tests/test_activity.py`). Dependencia: recibe sólo el patrón de contrato
  desde P300; no hay dependencias posteriores evidenciadas.
- **Precondición dentro de esta tarea (no es propuesta aparte):** S02
  registra (S05; ambigüedad 1 de `S02.P320.01`) que las celdas de
  `professor/notebook.ipynb` contienen secuencias `\n` literales: la primera
  celda queda como un solo comentario y la segunda no es Python válido. T01
  extiende ese notebook, así que S04 debe repararlo primero con el cambio
  mínimo (mismas celdas, mismo orden, mismo código, sólo saltos de línea
  reales) y comprobar que reproduce los artefactos actuales antes de
  añadir nada. La reparación es un defecto de implementación, no se deriva
  de las fuentes.
- **Alternativas menores descartadas:** declarar en markdown que P1 «debería
  corregirse» ya está implícito en la decisión y no cambia lo que el
  estudiante hace. Añadir una segunda métrica a la guarda (brecha de
  beneficio) refinaría la detección, pero seguiría sin corrección. Auditar
  otra política del curso (P306) cambiaría el caso y la identidad del
  taller; queda fuera de esta tarea.
- **Contrato de no regresión:** se conservan H01–H03; el dataset; la guarda
  `MAX_CONTACT_RATE_GAP = 0.10` y su métrica; las filas y columnas actuales de
  `equity_audit.csv` y `policy_correction_decisions.csv` (P0 aprobada, P1
  suspender y corregir); `policy_contract.json` y `policy_monitoring.csv` con
  sus claves actuales; y la prueba existente. La política corregida se
  **añade** como fila nueva (por ejemplo `P1_corrected`); P1 no se
  reescribe. La reparación del notebook no cambia el contenido de sus
  celdas. No se crean roles: la decisión sobre la variante corregida cita la
  autoridad ya declarada en el contrato.
- **Interacciones:** ninguna con otras `Txx` (única propuesta). Capacidad:
  P320 tiene tres highlights y cinco celdas; la reparación más una sección de
  corrección cabe en la sesión. El supuesto de beneficio por contacto (ver
  instrucciones) debe quedar visible como límite, no como dato.
- **Criterio de aceptación:** S05 encuentra (1) `professor/notebook.ipynb`
  ejecutable de principio a fin con las mismas celdas originales; y (2) un
  highlight nuevo en el que una variante corregida de P1, con el mismo total
  de contactos que P1, pasa por las mismas funciones de auditoría y decisión
  y queda aprobada con brecha de contacto ≤ 0,10, con su beneficio total
  estimado comparado contra P1 y contra P0, el supuesto de beneficio por
  contacto declarado y la autoridad del contrato citada en la decisión.
  Respaldo en notebook, fila nueva en `policy_correction_decisions.csv` y en
  `equity_audit.csv`, `submission/correction_tradeoff.csv` y pruebas. H01–H03
  siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/prescriptiva/P320_equidad_y_responsabilidad_prescriptiva/

0. Inspecciona primero data/policy_impacts.csv, professor/main.py,
   professor/notebook.ipynb, submission/ y tests/. Si los datos no tienen
   grano política × grupo con elegibles, contactados y beneficio, si la
   brecha de P1 no es 0,3, si P0 no se aprueba y P1 no queda como
   suspend_and_correct, o si el beneficio total de P1 no supera al de P0,
   detente e informa: la implementación contradice
   design/courses/prescriptiva/P320_activity.md. Si main.py ya produce una
   corrección de P1, detente e informa: la propuesta estaría cubierta.
1. PRECONDICIÓN — REPARAR EL NOTEBOOK: en professor/notebook.ipynb
   reemplaza las secuencias literales "\n" por saltos de línea reales en el
   source de cada celda. Mismas celdas, mismo orden, mismo código; no
   añadas, quites ni reescribas instrucciones. Ejecuta el notebook completo
   y confirma que los cuatro artefactos de submission/ coinciden con los
   que produce main(). Si tras la reparación alguna celda falla por otra
   causa, detente e informa sin corregir esa causa. No toques
   notebooks/notebook.ipynb (fuera del alcance de esta tarea).
2. No cambies policy_impacts.csv, MAX_CONTACT_RATE_GAP, la métrica de la
   guarda, las filas actuales de los artefactos ni las claves del contrato.
3. SUPUESTO DE BENEFICIO: calcula el beneficio por contactado de cada grupo
   en P0 y en P1 a partir de los datos. Usa como supuesto el beneficio por
   contactado de P1 por grupo (constante dentro del grupo) y decláralo en
   markdown como supuesto lineal del caso, no como dato. Si para un mismo
   grupo P0 y P1 implican beneficios por contactado distintos, calcula el
   beneficio de la variante con ambos y repórtalos como rango.
4. CORRECCIÓN: añade en main.py una función (por ejemplo
   correct_policy_allocation) que, manteniendo el total de contactados de
   P1 y sin superar los elegibles de cada grupo, enumere las asignaciones
   enteras de contactos entre A y B, conserve las que cumplen brecha de tasa
   de contacto <= MAX_CONTACT_RATE_GAP y elija la de mayor beneficio total
   estimado. Construye con ella las filas de P1_corrected con las mismas
   columnas de policy_impacts.csv.
5. REVERIFICAR: pasa P1_corrected por las mismas funciones de auditoría y
   decisión existentes (sin duplicarlas) y añade sus filas a
   equity_audit.csv y policy_correction_decisions.csv. La fila de decisión
   debe citar la autoridad de aprobación ya declarada en
   policy_contract.json; no inventes roles ni cambies el contrato.
6. INTERCAMBIO: persiste submission/correction_tradeoff.csv con columnas
   policy, total_contacted, contact_rate_gap, benefit_per_eligible_gap,
   total_benefit, benefit_change_vs_P1, benefit_change_vs_P0, decision,
   para P0, P1 y P1_corrected (con el rango del paso 3 si aplica, en filas
   o columnas explícitas). Muestra la tabla en el notebook y explica en
   markdown, en 4–6 líneas: cuánto beneficio cuesta cumplir la guarda
   frente a P1, cuánto se conserva frente a P0, que la brecha de beneficio
   por elegible (H02) no la controla la guarda actual y que la cifra
   depende del supuesto del paso 3.
7. Añade a tests/ pruebas que verifiquen: que professor/notebook.ipynb es
   JSON de notebook válido y que el source de cada celda de código se
   analiza con ast.parse sin error (con pytest.skip si el notebook de
   profesor no existe en la distribución, sin fallar en el descubrimiento);
   que policy_correction_decisions.csv contiene
   P1_corrected aprobada y conserva P0 aprobada y P1 suspend_and_correct;
   que su brecha de contacto es <= 0,10; que su total de contactados es
   igual al de P1; y que correction_tradeoff.csv existe con esas columnas
   y las tres políticas. No elimines la prueba existente.
8. Ejecuta main(), el notebook completo y las pruebas sin errores.
9. No modifiques otras actividades, traceability.yaml ni design/.
```
