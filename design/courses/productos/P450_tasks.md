# P450 — Propuestas de mejora

**Línea base:** `P450_activity.md` (entrada S02 más reciente: `S02.P450.01`).

## T01 — Hacer auditable la revisión humana: quién revisó, cuándo (UTC), por qué y sobre qué recomendación

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` p. 111 — en «PR-On Automation», conocimiento «Transparency and accountability in algorithms» y habilidad «Identify steps needed to ensure that a decision-making system is auditable»: un sistema que decide o recomienda acciones debe permitir reconstruir después quién decidió y sobre qué (Claude, 2026-10-05). Fuente *authoritative*, pero el área está marcada «– E» (electiva) en el documento: respalda la expectativa general de auditabilidad, no un formato de registro.
- **Qué gana el estudiante:** distinguir entre *condicionar* una acción a una
  aprobación (H02, que se conserva) y dejar una decisión *auditable*: un
  tercero puede reconstruir quién revisó, en qué instante UTC, con qué
  motivo y exactamente qué recomendación. Hoy el registro une recomendación,
  decisión y autorización, pero S02 documenta «Sin revisor, fecha ni motivo»
  (índice de comparación; S03) y que la decisión está escrita en el código
  (S02: «Sin `main()`; decisión escrita en el código»): el registro no
  evidencia una revisión humana, sólo una constante.
- **Materialidad frente al riesgo de identidad de S02:** S02 registra que la
  recomendación revisada (fábrica 2, riesgo `high`, `inspect_machine`) no se
  deriva en el curso y contradice la regla de P425 (`high` si
  `daily_units_produced < 4500`; las filas de la fábrica 2, 4700 y 4600,
  darían `low`). Hacer auditable la revisión de un valor sin procedencia
  daría apariencia de rigor a un dato que el curso no puede sostener: eso
  sería pulir una práctica de registro y agravaría el riesgo de identidad.
  La propuesta sólo fortalece la operación de la capacidad (C04: autoridad
  humana sobre la acción derivada del indicador de riesgo) si la
  recomendación revisada queda (a) derivada aplicando una regla declarada
  del curso a datos del curso, o (b) declarada explícitamente como entrada
  con su procedencia. Las instrucciones no propagan el valor `high`
  codificado y se detienen si el profesor no decide (a) o (b).
- **Anclas actuales:** H01 (recomendación accionable; límite de
  procedencia), H02 (autorización sólo ante `approve`); superficies S01
  (`data/recommendation.json`), S02 (`professor/main.py`), S03
  (`submission/review.json`) y S04 (pruebas); dependencia «Recibe de P430»
  (contenido repetido, sin artefacto). Relación con P425 H03 (regla de
  umbral sin procedencia).
- **Alternativas menores descartadas:** añadir revisor, fecha y motivo como
  literales en `__main__` produciría un registro con forma de auditoría y
  sin revisión real. Declarar el límite en texto ya lo hace S02 y no da al
  estudiante una forma de verificarlo. Resolver la inconsistencia del riesgo
  en P425 o P430 es una decisión de curso que esta T01 no toma; aquí sólo se
  exige que la recomendación revisada tenga procedencia declarada.
- **Contrato de no regresión:** se conservan H02 y la regla
  `action_authorized = decision == "approve"`, la conservación intacta de la
  recomendación en el registro y las claves actuales de `review.json`
  (`recommendation`, `decision`, `action_authorized`). Las pruebas
  existentes se mantienen. H01 se modifica sólo en su límite: la
  recomendación pasa a tener procedencia declarada o derivada; si el
  profesor decide derivarla y el resultado cambia (por ejemplo, `low`), el
  cambio de contenido de `recommendation.json` es una sustitución explícita
  aprobada en la discusión, no una decisión de la herramienta.
- **Interacciones:** ninguna otra `Txx` en este archivo. Fuera de P450: el
  mismo `high` de la fábrica 2 aparece en P430, P451 y P452; la decisión del
  profesor sobre su procedencia debería aplicarse de forma coherente en esas
  actividades, pero cada cambio allí sería una propuesta propia. Capacidad:
  cambio local (nivel 2) más una entrada por línea de comandos; P450 tiene
  dos highlights y cabe en la sesión.
- **Criterio de aceptación:** S05 encuentra (1) en `P450_log.md` la
  decisión del profesor sobre la procedencia de la recomendación y, en
  `data/recommendation.json`, esa procedencia (regla, insumo y su huella, o
  fuente declarada); (2) un highlight nuevo o H02 modificado en el que
  `submission/review.json` registra revisor, instante UTC, motivo no vacío y
  la huella SHA-256 de la recomendación revisada, con la decisión tomada
  como entrada de `main()` y no como constante; y (3) pruebas que verifican
  que falta de revisor o de motivo se rechaza, que la huella corresponde a
  la recomendación registrada y que `action_authorized` sigue siendo
  verdadero sólo con `approve`.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P450_human_review/

0. Inspecciona primero data/recommendation.json, professor/main.py,
   professor/test_main.py, src/main.py, submission/ y tests/. Si la
   implementación no coincide con design/courses/productos/P450_activity.md
   (review_recommendation con autorización sólo ante "approve", decisión
   fija en __main__, review.json sin revisor, fecha ni motivo), detente e
   informa sin modificar nada.
1. PROCEDENCIA (condición de detención): no copies ni propagues el valor
   risk "high" de la fábrica 2 desde data/recommendation.json, P430, P451 ni
   P452 como si estuviera respaldado. Lee en P450_log.md la decisión del
   profesor para esta T01. Debe ser una de dos:
   a. DERIVADA: la recomendación se obtiene aplicando una regla declarada
      del curso (por ejemplo, classify_risk de P425 con su umbral) a un
      insumo del curso identificado por ruta y SHA-256. En ese caso, escribe
      en recommendation.json el resultado que produzca esa regla (aunque
      sea "low") y un objeto "provenance" con la regla, el umbral, la ruta y
      el SHA-256 del insumo. La acción asociada a cada nivel de riesgo debe
      venir del texto del profesor; no la inventes.
   b. DECLARADA: la recomendación se conserva como entrada externa con un
      objeto "provenance" cuyo contenido (quién o qué la produjo y con qué
      fecha o versión) aporta el profesor literalmente.
   Si no existe esa decisión, o si no aporta los valores necesarios,
   detente y pídela. No elijas entre a y b por tu cuenta.
2. En professor/main.py conserva review_recommendation y la regla
   action_authorized = decision == "approve". Amplía el registro que
   devuelve con: "reviewer" (cadena no vacía), "reviewed_at_utc" (ISO 8601
   con Z), "reason" (cadena no vacía, obligatoria para cualquier decisión) y
   "recommendation_sha256" (SHA-256 del JSON canónico de la recomendación:
   json.dumps(..., sort_keys=True, separators=(",", ":"))). Recibe el
   instante como parámetro opcional para poder probarlo; si no se pasa, usa
   datetime.now(timezone.utc). Un revisor o un motivo vacíos deben lanzar
   ValueError con un mensaje que nombre el campo.
3. Crea main() que reciba decision, reviewer y reason por línea de comandos
   (argparse, como la configuración por argumentos de P406), lea
   data/recommendation.json y escriba submission/review.json. Elimina la
   decisión fija de __main__; deja sólo la llamada a main(). Añade
   HOW_TO_RUN_ME.txt con un ejemplo de invocación; el revisor del ejemplo
   debe ser un nombre de rol o de práctica, no una persona real.
4. Regenera submission/review.json con una invocación de ejemplo. Las
   claves actuales (recommendation, decision, action_authorized) deben
   conservarse con su significado.
5. Añade a professor/test_main.py pruebas que verifiquen: revisor vacío y
   motivo vacío lanzan ValueError; recommendation_sha256 coincide con la
   huella recalculada de la recomendación incluida en el registro y cambia
   si cambia la recomendación; reviewed_at_utc es el instante inyectado en
   UTC; "approve" autoriza y cualquier otra decisión no. Añade a
   tests/test_activity.py una prueba que verifique que review.json
   entregado contiene reviewer, reviewed_at_utc, reason no vacíos,
   recommendation_sha256 de 64 caracteres hexadecimales coherente con su
   recommendation, y que recommendation.json tiene "provenance". No
   elimines ni modifiques pruebas existentes.
6. Ejecuta main() con el ejemplo de HOW_TO_RUN_ME.txt y todas las pruebas
   de la actividad sin errores.
7. No modifiques src/main.py (plantilla del estudiante), otras actividades
   (en particular P425, P430, P451 y P452), traceability.yaml ni design/.
```
