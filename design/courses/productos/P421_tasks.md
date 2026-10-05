# P421 — Propuestas de mejora

**Línea base:** `P421_activity.md` (entrada S02 más reciente: `S02.P421.01`).

## T01 — Promover a producción sólo con un criterio declarado: comparar el candidato contra la versión vigente y un mínimo, registrar promovido/rechazado y conservar el historial

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia + proceso (corrige un defecto)
- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` pp. 5 y 7 — «Task 2.4 Define primary measures of success» y «Task 2.5 Identify baseline performance of the current state» (p. 5); antes de desplegar, «Task 6.1 Perform business validation of the analytics solution», «Task 6.2 Deliver business validation report with findings» y «Task 6.3 Obtain sponsor agreement and stakeholder alignment on moving forward with deployment» (p. 7): el paso a producción se decide con un reporte de validación contra una medida de éxito y contra el desempeño vigente (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general; el acuerdo del patrocinador queda fuera (es contribución de P450).
  - `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` pp. 20, 21 y 26 — «¿Qué tendría que ocurrir para autorizar su paso a producción?» (p. 20); «Si la solución no cumple los criterios de éxito, regresar a las actividades de framing, datos o diseño que deban revisarse antes de autorizar su liberación» (p. 21); «Validar las actualizaciones. Comparar el modelo actualizado con versiones anteriores y comprobar que cumple los criterios antes de desplegarlo» (p. 26): la promoción es la comparación con la versión anterior más un criterio, y el rechazo es un resultado previsto (Claude, 2026-10-05). Fuente *literature-derived*: perspectiva metodológica, no herramienta.
  - `design/benchmarks-md/literature-derived/dataops-06-definition.md` p. 20 — entre los prerrequisitos de la transición a operaciones, «Artifactos auditables con logging» y «Modelos documentados y verificados», y la tarea «Despliegue de modelos al ambiente de producción usando CD/CI y pruebas de aceptación»: el despliegue de un modelo pasa por una aceptación verificable y deja registro (Claude, 2026-10-05). Fuente *literature-derived*: refuerzo secundario.
  - `design/benchmarks-md/professional-learning/power-bi-enterprise-solutions-workshop-2024.md` pp. 20 y 91 — «Workspaces are promoted through Deployment Pipelines after test acceptance» (p. 20) y «Governance policy sets criteria for validation & endorsement» (p. 91): en la práctica profesional, la promoción entre etapas exige aceptación previa contra criterios fijados por una política (Claude, 2026-10-05). Fuente *professional-learning* secundaria: corrobora la práctica; no aporta mecanismo ni justifica la propuesta por sí misma.
  - `design/benchmarks-md/professional-learning/sas-data-mining.md` pp. 4 y 10 — «un modelo campeón claramente definido» (p. 4) y segmentos en que no se generan «modelos que cumplan con los criterios de aceptación» (p. 10): el modelo en uso es un campeón que un retador sólo desplaza si cumple un criterio de aceptación (Claude, 2026-10-05). Fuente *professional-learning*: señal de práctica (campeón–retador), no impone tema ni herramienta.
- **Qué gana el estudiante:** decide una promoción con evidencia verificable,
  no copiando un archivo. Hoy P421 «documenta una aprobación que no puede
  verificar» (H03): la exactitud 0.91 está escrita a mano en
  `CANDIDATES.json`, el origen del candidato no se declara, no hay umbral ni
  comparación con el modelo vigente y una nueva promoción sobrescribe
  `model.pkl` y `registry.json` sin historial (S01, S02; límite del producto).
  Con el cambio, el estudiante aplica una regla de promoción declarada (un
  mínimo y la comparación contra el campeón vigente medidos sobre la misma
  partición), registra el resultado `promoted` o `rejected` con su motivo,
  archiva al campeón desplazado y conserva el historial de decisiones. Es lo
  que distingue un registro de modelos de una carpeta, y es la primera
  evidencia de `productos.C03` en el taller (hoy «C03 no tiene evidencia»).
  Ningún taller ejerce la comparación retador–campeón: P403 aplica umbrales
  absolutos a un artefacto aislado, sin sustitución de una versión por otra.
- **Anclas actuales:** H01 (promoción separada de la construcción), H02
  (identificador estable con rechazo verificado), H03 (artefacto sin
  procedencia; caso y datos); superficies S01 (`CANDIDATES.json`,
  `CANDIDATE_V1.pkl`: «Un candidato; métrica escrita a mano»), S02 (lógica de
  promoción: «Sin umbral; sobrescribe la etapa»), S03
  (`submission/model_registry/`: «Sólo la etapa production»), S04 (pruebas) y
  S05 (`HOW_TO_RUN_ME.txt`); dependencias: «Recibe de Pxxx: no recibe
  artefactos», «Habilita para Pyyy: no evidenciada».
- **Origen del candidato (opción y condición):** S02 registra que el origen
  de `CANDIDATE_V1.pkl` y de la exactitud 0.91 no se declara, y que P421 no
  consume las corridas de P420 aunque éstas ya tienen `model.pkl` y exactitud
  sobre una partición fija (P420 H01). La propuesta admite dos opciones, que
  el profesor decide en la discusión:
  - **Opción A (preferida):** los candidatos son corridas de P420 copiadas a
    P421 como insumo con procedencia declarada (actividad, `run_id`, semilla
    y partición de origen, fecha de copia, hash de `model.pkl`), y la métrica
    se lee de su `metrics.json`, no se escribe a mano. Al compartir partición,
    las exactitudes son comparables. Condiciones: que el profesor apruebe esta
    continuidad P420 → P421 (cambia el caso de P421, hoy «ninguno», por el de
    vino tinto); que existan en P420 al menos dos corridas de modelos
    distintos; y, preferiblemente, que `P420_tasks.md` T01 esté ejecutada, para
    que la métrica copiada sea reproducible desde el artefacto y KNN no esté
    condicionado por la falta de escalado. Se copia en vez de leer la carpeta
    de P420 porque la profundidad relativa de las actividades cambia al
    distribuirlas y las pruebas de P421 no pueden depender de que el
    estudiante haya ejecutado P420. Con esta opción, H03 deja de ser un
    límite: el candidato tiene procedencia y su métrica, origen.
  - **Opción B (mínima):** se conserva `CANDIDATE_V1.pkl` y la regla se
    implementa y se prueba con artefactos temporales en `tmp_path`; la
    evidencia de `submission/` sólo muestra la primera promoción contra el
    mínimo (no hay campeón previo) y el registro marca la métrica como
    declarada sin datos. No se crean candidatos nuevos: añadir otro pickle sin
    procedencia agravaría H03. Con esta opción el criterio se ejerce, pero la
    comparación retador–campeón sólo existe en las pruebas y H03 sigue vigente.
- **Alternativas menores descartadas:** declarar en el texto que la
  promoción carece de criterio ya está hecho en S02. Añadir sólo un umbral
  absoluto replicaría la compuerta de P403 sin la contribución propia de un
  registro (sustituir una versión por otra). Conservar el historial sin regla
  dejaría la decisión sin motivo. Con la opción B el cambio es de nivel 2
  (extender localmente); con la opción A es de nivel 3 en caso y datos, sin
  cambiar el producto (un registro de etapas).
- **Contrato de no regresión:** se conservan H01 (la promoción sigue
  separada de la construcción: P421 no entrena), H02 (`find_candidate` y el
  rechazo de un identificador ausente), el argumento `--stage` y las etapas
  como directorios, y la escritura en `tmp_path` en pruebas sin tocar la
  evidencia distribuida. `submission/model_registry/production/model.pkl` y
  `registry.json` siguen existiendo con sus campos actuales; se añaden campos
  y archivos. Se mantiene el esquema de etapas propio de P421; no se unifica
  con el `REGISTRY.json` por versiones de P424. Sustituciones explícitas: con
  la opción A, `candidate_v1` deja de ser el candidato por defecto y las
  pruebas existentes que lo nombran se actualizan sólo en el identificador,
  sin debilitar sus asserts; la regla de promoción no incluye aprobación
  humana, que es contribución de P450: el registro sólo puede dejar un campo
  de referencia a ella.
- **Interacciones:** ninguna otra Txx en este archivo. Fuera de P421:
  depende de `P420_tasks.md` T01 si se elige la opción A (ejecutar primero).
  Con `P424_tasks.md` T01: ambas tocan registros de modelos con formatos
  distintos (etapas en P421, versiones en P424); ninguna consume la salida de
  la otra y cada cambio se mantiene local. Si en el futuro se decide que P424
  revierta al campeón archivado por P421, sería una propuesta aparte de
  unificación de formatos. Capacidad: P421 tiene tres highlights y un script
  corto; la opción A añade la preparación de insumos copiados.
- **Criterio de aceptación:** S05 encuentra (1) una política de promoción
  persistida como dato (métrica, mínimo, mejora mínima sobre el campeón,
  regla en el borde y quién la aprobó), con valores aportados por el
  profesor; (2) que `promote_model` a `production` compara el candidato con el
  mínimo y con el campeón vigente, y produce `promoted` o `rejected` con
  motivo; (3) que el campeón desplazado pasa a `archived/` y que un historial
  persistido en `submission/model_registry/` conserva todas las decisiones,
  incluidas las rechazadas; (4) pruebas de profesor para primera promoción,
  rechazo por mínimo, borde exacto en el mínimo, rechazo por no superar al
  campeón y promoción que archiva al campeón; (5) una prueba de actividad que
  verifica el historial, los valores de decisión y la coherencia entre
  `registry.json` y la última decisión `promoted`; y (6) con la opción A,
  candidatos con procedencia de P420 y métrica leída de su `metrics.json`;
  con la opción B, la métrica marcada como declarada. H01 y H02 siguen
  presentes; H03 queda resuelto (opción A) o vigente y declarado (opción B).

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P421_model_registry/

0. Inspecciona primero CANDIDATES.json, professor/main.py (find_candidate,
   promote_model, main), professor/test_main.py, src/main.py,
   HOW_TO_RUN_ME.txt, submission/model_registry/ y tests/test_activity.py.
   Si la implementación no coincide con
   design/courses/productos/P421_activity.md (por ejemplo, si ya existe un
   umbral, una comparación con el modelo vigente o un historial), detente e
   informa sin modificar nada.
1. POLÍTICA Y OPCIÓN: no inventes el mínimo, la mejora mínima ni quién
   aprueba la política. Usa los valores y la opción (A o B) que el profesor
   haya aprobado en la discusión de esta T01 (registrados en P421_log.md). Si
   no existen, detente y pídelos. Persiste la política en
   PROMOTION_POLICY.json en la raíz de la actividad, con: metric, minimum,
   min_improvement, boundary_rule (por ejemplo, "candidate >= minimum"),
   approved_by. En el borde, igualdad con el mínimo cumple, como en P423.
2. CANDIDATOS:
   a. Opción A: copia desde
      implementation/productos/P420_experiment_tracking/submission/experiments/
      las corridas indicadas por el profesor (al menos dos, de modelos
      distintos) a candidates/<run_id>/ con model.pkl, metrics.json y
      config.json, y escribe candidates/<run_id>/PROVENANCE.json con
      source_activity "P420", run_id, random_state y test_size de la
      partición, copied_at y sha256 de model.pkl. Reescribe CANDIDATES.json
      con esas corridas: id, archivo, metric_source (ruta del metrics.json
      copiado) y estado. La métrica se lee de metrics.json en tiempo de
      ejecución, no se copia a mano. Si las corridas de P420 no reproducen su
      métrica (P420 T01) o el profesor no indicó cuáles usar, detente.
   b. Opción B: no cambies CANDIDATE_V1.pkl ni añadas candidatos. Añade a
      su entrada de CANDIDATES.json metric_source "declarada, sin datos".
3. Modifica promote_model para la etapa production:
   a. lee el campeón vigente de submission/model_registry/production/
      registry.json si existe;
   b. decide: rejected si la métrica del candidato < minimum; rejected si
      hay campeón y la métrica del candidato < métrica del campeón +
      min_improvement; promoted en otro caso. Registra el motivo en texto
      breve;
   c. si promoted y hay campeón, mueve su model.pkl y registry.json a
      submission/model_registry/archived/<model_id del campeón>/ antes de
      copiar el candidato;
   d. en todos los casos, añade la decisión a
      submission/model_registry/promotion_history.json con: candidate_id,
      champion_id (o null), candidate_metric, champion_metric (o null),
      minimum, min_improvement, metric_source, decision, reason, decided_at.
   Conserva los campos actuales de registry.json y añade metric_source y
   policy (ruta de PROMOTION_POLICY.json). Mantén --stage archived con su
   comportamiento actual.
4. Actualiza src/main.py de forma coherente: si es plantilla con
   NotImplementedError, añade la regla como plantilla, sin resolverla.
5. Regenera la evidencia de submission/: con la opción A, promueve primero
   un candidato y luego el otro, de modo que el historial muestre dos
   decisiones con la comparación contra el campeón; con la opción B, una
   decisión. No escribas en submission/ desde las pruebas.
6. Añade a professor/test_main.py, con tmp_path y artefactos de prueba,
   pruebas para: primera promoción sin campeón; rechazo por debajo del
   mínimo (production no cambia); candidato exactamente en el mínimo
   (promoted); rechazo por no superar al campeón (el campeón sigue en
   production); promoción que archiva al campeón y deja dos decisiones en el
   historial. No elimines test_01 ni test_02; si la opción A elimina
   candidate_v1, actualiza sólo el identificador que usan, sin debilitar sus
   asserts.
7. Añade a tests/test_activity.py una prueba que verifique que
   promotion_history.json existe, que cada decisión está en {promoted,
   rejected} y tiene los campos del paso 3d, y que el model_id de
   production/registry.json coincide con el candidate_id de la última
   decisión promoted. Con la opción A, verifica además que el sha256 de
   production/model.pkl coincide con el de PROVENANCE.json del candidato.
   La prueba debe resolver rutas relativas al archivo de prueba. No elimines
   pruebas existentes.
8. Actualiza HOW_TO_RUN_ME.txt con los comandos del paso 5 y un paso que
   pida leer en promotion_history.json por qué cada candidato fue promovido
   o rechazado.
9. Ejecuta las pruebas de profesor y de la actividad sin errores.
10. No modifiques P420 (sólo lee sus corridas en la opción A), P424 ni otras
    actividades, traceability.yaml ni design/.
```
