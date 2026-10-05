# P424 — Propuestas de mejora

**Línea base:** `P424_activity.md` (entrada S02 más reciente: `S02.P424.01`).

## T01 — Disparar la reversión desde la alerta de desempeño de P423, registrar disparador y motivo, y dejar el registro coherente con el modelo activo

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia + proceso (corrige un defecto)
- **Fuentes:**
  - `design/benchmarks-md/governmental/mintic-fedesoft-talento-digital-2025-2030.md` p. 176 — la brecha laboral es que los candidatos usaron CI/CD «en escenarios académicos simples sin haber enfrentado complejidades de proyectos reales: gestión de credenciales (secretos), rollback automatizado, despliegues blue-green o canary, integración con herramientas de monitoreo»: la reversión conectada con el monitoreo es la parte que falta en la formación (Claude, 2026-10-05). Fuente *governmental*: respalda la pertinencia, no prescribe el mecanismo (blue-green o canary no se proponen).
  - `design/benchmarks-md/literature-derived/dataops-03-methodologies.md` pp. 25–26 — entre los disparadores, «Disminuye el desempeño del modelo» y «Se supera uno de los umbrales definidos», seguidos de «¿Recalibramos, reentrenamos, reemplazamos o retiramos la solución?» (p. 25); «Decidir sobre el ciclo de vida. Determinar si la solución debe mantenerse, actualizarse, reentrenarse, reemplazarse o retirarse» (p. 26): la reversión es una respuesta de ciclo de vida a una evidencia concreta (Claude, 2026-10-05). Fuente *literature-derived*: marco metodológico.
  - `design/benchmarks-md/professional-learning/ibm-spss-modeler-crisp-dm-guide.md` p. 40 — «How will you determine when a model has "expired"? Give specifics on accuracy thresholds or expected changes in data, etc.» y «What will occur when a model expires?»: el plan de despliegue declara qué evidencia hace caducar un modelo y qué ocurre entonces (Claude, 2026-10-05). Fuente *professional-learning*: sólo corrobora; no aporta mecanismo nuevo.
  - `design/benchmarks-md/professional-learning/sas-forecasting.md` p. 155 — «We use the term _model vintage_ to represent the date of the last model update or adjustment», con la acción de severidad alta «Discard current model»: el registro conserva desde cuándo está vigente la versión activa y la reversión se lee como respuesta a la severidad más alta (Claude, 2026-10-05). Fuente *professional-learning* secundaria: respalda el campo de vigencia; el resto de la señal pertenece a `P423_tasks.md` T02.
- **Qué gana el estudiante:** entiende la reversión como respuesta operativa
  a una falla observada de la capacidad, no como copia de un archivo. Ejecuta
  la reversión sólo cuando una alerta de desempeño de P423 la justifica,
  registra qué alerta la disparó y por qué, y deja el registro de versiones
  coherente con el modelo que quedó activo. Hoy S02 registra tres defectos:
  `REGISTRY.json` «sigue indicando `v2`» después de revertir a `v1`, «por lo
  que registro y modelo activo divergen»; no se registra el motivo «ni se
  impide "revertir" a la versión vigente»; y las dos versiones tienen el mismo
  tamaño y origen no declarado, sin evidencia que motive la reversión (H03:
  «ninguna evidencia (por ejemplo, la alerta de P423) motiva la reversión»).
  Ningún taller conecta monitoreo (P422–P423) con recuperación (P424); la
  fuente gubernamental señala justamente esa integración como brecha.
- **Anclas actuales:** H01 (reversión por copia verificada por bytes), H02
  (registro de reversión auditable), H03 (versiones indistinguibles y sin
  motivo; caso y datos); superficies S01 (`REGISTRY.json`, `MODEL_V1.pkl`,
  `MODEL_V2.pkl`), S02 (`professor/main.py`, `src/main.py`: «No actualiza
  `REGISTRY.json`; no registra motivo»), S03 (`submission/production/`), S04
  (pruebas) y S05 (`HOW_TO_RUN_ME.txt`); dependencias: «Recibe de P421:
  práctica de registro»; P423 «produce una alerta que podría motivar la
  reversión; la relación no está implementada».
- **Cómo llega la alerta (decisión):** P423 y P424 no comparten artefactos
  hoy. La alerta llega como insumo copiado con procedencia declarada:
  `data/performance_alert.json`, copia del `performance_report.json` de P423,
  con la ruta de origen, la fecha de copia y el hash del original. Se
  descarta leer la carpeta `submission/` de P423 en tiempo de ejecución
  porque la profundidad relativa de las actividades cambia al distribuirlas,
  `pytest` no puede depender de esa ruta y la evidencia de P424 quedaría
  atada a que el estudiante haya ejecutado P423. La copia hace explícita la
  dependencia sin acoplar la ejecución.
- **Qué campo de la alerta dispara:** depende de lo que P423 tenga al
  ejecutar esta T01. Si `P423_tasks.md` T02 está ejecutada, dispara
  `action == "revertir"`. Si sólo T01 lo está, dispara
  `verdict == "incumple"`. Si ninguna, dispara `alert == true`, el campo
  actual (cinco filas: el límite de evidencia de P423 se hereda y se declara
  en el registro). Un veredicto `insuficiente` o una acción distinta de
  revertir no autorizan la reversión.
- **Formatos de registro:** P421 usa un registro por etapas
  (`model_registry/<stage>/registry.json`) y P424 uno por versiones
  (`REGISTRY.json`). Esta T01 mantiene el formato propio de P424 y sólo le
  añade campos. No lo unifica con P421 ni consume el campeón archivado de
  `P421_tasks.md` T01. La diferencia queda declarada en `HOW_TO_RUN_ME.txt`.
- **Alternativas menores descartadas:** sólo actualizar `REGISTRY.json`
  corrige la incoherencia, pero mantiene una reversión sin causa (H03). Sólo
  añadir un campo de motivo de texto libre deja la decisión sin evidencia
  verificable. Leer la alerta directamente de P423 se descarta por la
  distribución (ver arriba). El cambio es de nivel 2: mismo producto y misma
  operación, con un insumo nuevo copiado.
- **Contrato de no regresión:** se conservan H01 (copia del artefacto, sin
  reentrenar; igualdad de bytes verificada), H02 (`previous_version`,
  `production_version`, `rolled_back_at`; rechazo de `v3`), el argumento
  `--to-version`, `submission/production/model.pkl` y `rollback_record.json`
  con sus campos actuales, y el uso de `monkeypatch` para no tocar la
  evidencia distribuida. El `REGISTRY.json` de la raíz se conserva como
  estado inicial distribuido y no se sobrescribe, para que la actividad y sus
  pruebas puedan repetirse. El registro vigente tras la reversión se persiste
  en `submission/production/registry.json`. Sustituciones explícitas: H03
  deja de describir una reversión sin motivo. Si `rollback` exige ahora
  disparador y motivo, las llamadas de las pruebas existentes se actualizan
  sólo en sus argumentos, con insumos de prueba, sin debilitar sus asserts.
- **Interacciones:** ninguna otra Txx en este archivo. Depende de lo
  ejecutado en `P423_tasks.md` T01 y T02 para el campo que dispara (ver
  arriba); no exige que se aprueben: con el `alert` actual la T01 es
  ejecutable. Si P423 T01/T02 se aprueban después, basta con volver a copiar
  la alerta y ajustar el campo disparador. Con `P421_tasks.md` T01: formatos
  distintos, cambio local (ver arriba). Si las versiones resultan
  idénticas en bytes, una alternativa, sujeta a aprobación del profesor y a
  `P420_tasks.md` T01, es tomar como `v1` y `v2` dos corridas de P420 con
  procedencia declarada. Capacidad: P424 tiene tres highlights y un script
  corto; el cambio añade un insumo copiado, tres validaciones y campos de
  registro.
- **Criterio de aceptación:** S05 encuentra (1) `data/performance_alert.json`
  copiado de P423 con procedencia (ruta de origen, fecha y hash del
  original); (2) que `rollback` exige un motivo no vacío y un disparador que
  autorice la reversión, y rechaza revertir a la versión vigente; (3)
  `rollback_record.json` con los campos actuales más `reason`, `trigger`
  (archivo, identificador o hash del reporte, campo y valor que dispararon)
  y `active_since`; (4) `submission/production/registry.json` con
  `production_version` igual a la del registro de reversión, sha256 por
  versión y un historial de cambios de versión activa; (5) que el sha256 de
  `submission/production/model.pkl` coincide con el de la versión activa en
  ese registro; (6) pruebas de profesor para reversión autorizada, rechazo
  por disparador que no autoriza, rechazo de la versión vigente y rechazo
  sin motivo; (7) una prueba de actividad que verifica la coherencia
  registro–modelo activo y la presencia de motivo y disparador; y (8) H01 y
  H02 presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P424_model_rollback/

0. Inspecciona primero REGISTRY.json, MODEL_V1.pkl y MODEL_V2.pkl,
   professor/main.py (rollback), professor/test_main.py, src/main.py,
   HOW_TO_RUN_ME.txt, submission/production/ y tests/test_activity.py. Si la
   implementación no coincide con design/courses/productos/P424_activity.md,
   detente e informa sin modificar nada. Calcula el sha256 de MODEL_V1.pkl y
   MODEL_V2.pkl: si son idénticos, detente e informa (revertir entre
   artefactos iguales no demuestra nada); la alternativa de usar corridas de
   P420 requiere decisión del profesor.
1. ALERTA: inspecciona, sólo para leer,
   implementation/productos/P423_model_performance_monitoring/submission/
   performance_report.json. Determina el campo disparador según lo que
   exista: action == "revertir" (P423 T02), si no verdict == "incumple"
   (P423 T01), si no alert == true. Si el reporte no autoriza la reversión
   (por ejemplo, verdict "insuficiente" o alert false), detente e informa:
   la evidencia de P424 no puede mostrar una reversión justificada. Copia el
   reporte a data/performance_alert.json y escribe data/ALERT_PROVENANCE.json
   con source_activity "P423", source_path, copied_at, sha256 del original y
   trigger_field. No leas archivos de P423 en tiempo de ejecución.
2. MOTIVO: no inventes el texto del motivo. Usa el que el profesor haya
   aprobado en la discusión de esta T01 (registrado en P424_log.md); si no
   existe, detente y pídelo.
3. Modifica rollback para que reciba la versión objetivo, la ruta del
   disparador y el motivo (argumentos --trigger y --reason además de
   --to-version), y:
   a. lea el registro vigente de submission/production/registry.json si
      existe; si no, de REGISTRY.json (estado inicial);
   b. rechace con ValueError: versión no registrada (como hoy), versión
      igual a la vigente, motivo vacío y disparador que no autoriza según
      trigger_field;
   c. copie el pickle como hoy;
   d. escriba submission/production/registry.json: el contenido del
      registro con production_version actualizado, sha256 por versión,
      active_since (marca UTC) y un historial que añade el cambio;
   e. escriba rollback_record.json con los campos actuales más reason,
      trigger (archivo, report_id o sha256, campo y valor) y active_since.
   No sobrescribas REGISTRY.json de la raíz.
4. Actualiza src/main.py de forma coherente: si es plantilla con
   NotImplementedError, añade las validaciones nuevas como plantilla, sin
   resolverlas.
5. Regenera submission/production/ ejecutando la reversión v2 → v1 con el
   disparador copiado y el motivo aprobado.
6. Añade a professor/test_main.py, con monkeypatch y archivos temporales,
   pruebas para: reversión autorizada (registro vigente y registro de
   reversión indican la versión objetivo y el sha256 de model.pkl coincide);
   rechazo con un disparador que no autoriza; rechazo de la versión vigente;
   rechazo sin motivo. Conserva
   test_rollback_restores_a_registered_version y
   test_rollback_rejects_an_unknown_version; si su llamada a rollback
   necesita los argumentos nuevos, añade sólo esos argumentos con insumos de
   prueba, sin debilitar sus asserts.
7. Añade a tests/test_activity.py una prueba que verifique que
   submission/production/registry.json existe, que su production_version es
   igual a la de rollback_record.json, que el sha256 de model.pkl coincide
   con el de esa versión, y que el registro de reversión tiene reason no
   vacío y trigger con sha256 igual al de data/ALERT_PROVENANCE.json. Rutas
   relativas al archivo de prueba. No elimines pruebas existentes.
8. Actualiza HOW_TO_RUN_ME.txt con el comando nuevo, una nota de que
   REGISTRY.json es el estado inicial y el registro vigente queda en
   submission/production/registry.json, una nota de que P421 usa otro
   formato de registro, y un paso que pida explicar en 2–3 líneas qué
   evidencia de P423 justificó la reversión.
9. Ejecuta las pruebas de profesor y de la actividad sin errores.
10. No modifiques P421, P423 ni otras actividades, traceability.yaml ni
    design/.
```
