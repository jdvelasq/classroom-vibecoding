# P420 — Propuestas de mejora

**Línea base:** `P420_activity.md` (entrada S02 más reciente: `S02.P420.01`).

## T01 — Persistir la preparación junto con el modelo (Pipeline) y verificar que el modelo recuperado reproduce la métrica registrada

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia (corrige un defecto)
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/oracle-data-mining-concepts-11g.md` pp. 10, 27 y 132 — «Data for build, test, and apply must undergo the exact same transformations» (p. 10); con preparación embebida, «The transformation instructions are embedded in the model and reused whenever the model is applied» (p. 27); sin ella, «You must take care to apply the same transformations to each data set» (p. 132): la unidad que se despliega y se recupera es preparación más modelo, no el estimador solo (Claude, 2026-10-05). Fuente *professional-learning*: respalda la práctica de artefacto; el defecto que justifica el cambio es el registrado por S02.
- **Qué gana el estudiante:** entiende que una corrida es recuperable sólo si
  el artefacto guardado contiene todo lo que se aplicó a los datos antes de
  puntuar, y lo comprueba: carga `model.pkl` desde la carpeta de la corrida y
  reproduce sobre `data/test.csv` la exactitud registrada en `metrics.json`.
  Hoy el taller tiene dos defectos que S02 registró: KNN se entrena sin
  escalar variables de escalas muy distintas (H04, S02), lo que condiciona la
  comparación 0.5825 frente a 0.5075 que el propio taller pide hacer (H03), y
  «Ninguna prueba verifica… que el modelo guardado reproduzca la métrica»
  (contrato de evidencia). Con el cambio, el escalado se ajusta sólo con
  entrenamiento dentro de un `Pipeline` que se persiste como un solo objeto,
  y la recuperación de la corrida deja de ser una afirmación para ser una
  verificación. Ningún otro taller verifica que un artefacto recuperado
  reproduzca su evaluación: P403–P404 reciben un `ESTIMATOR.pkl` opaco y
  P421/P424 promueven y revierten pickles sin validarlos.
- **Anclas actuales:** H02 (corrida como unidad recuperable), H03 (índice
  comparativo), H04 (objetivo ordinal y KNN sin escalado; caso y datos);
  superficies S02 (`build_model`, `prepare_data`: «KNN sin escalado»), S03
  (`save_run`: configuración registrada), S04 (`submission/experiments/`), S05
  (pruebas) y S06 (`src/main.py`, `HOW_TO_RUN_ME.txt`); dependencias: recibe
  de P419 y P406; «Para P421/P424: no evidenciada como artefacto».
- **Alternativas menores descartadas:** declarar el límite ya está hecho en
  S02 y no cambia lo que el estudiante practica. Escalar los datos antes de
  `save_run`, fuera del artefacto, corregiría la comparación pero reproduciría
  la asimetría entre construcción y aplicación que la fuente advierte: quien
  recupere `model.pkl` puntuaría sin escalar. Añadir sólo la prueba de
  recarga, sin el `Pipeline`, verificaría la reproducibilidad de un artefacto
  cuya comparación sigue condicionada. El cambio queda en el nivel 2 (extender
  localmente): mismo caso, mismo producto, mismo contrato de carpeta.
- **Contrato de no regresión:** se conservan H01 (partición 75/25
  estratificada con `random_state=123` y `test_02`), H02 (carpeta por corrida
  con `data/train.csv`, `data/test.csv`, `config.json`, `metrics.json`,
  `model.pkl`; `exist_ok=False`), H03 (`index.json` con `run_id`, `model`,
  `test_accuracy`, `created_at`) y la parte de H04 sobre el objetivo ordinal
  tratado como clases, que sigue siendo condición del caso y queda fuera de
  esta T01. `build_model` y `test_01` se conservan sin cambios: el `Pipeline`
  se construye en una función nueva que envuelve a `build_model`. El árbol no
  recibe escalado y su exactitud 0.5825 no cambia. Las dos corridas
  persistidas no se borran: son registros inmutables (la regla de H02) y
  quedan en el índice junto a las nuevas. Sustitución explícita: la parte
  «KNN sin escalado» de H04 deja de ser un límite vigente y se reemplaza por
  evidencia (corrida nueva de KNN con escalado dentro del artefacto y prueba de
  reproducción); S05 debe actualizar la descripción de H04 y el valor de KNN
  en H03.
- **Interacciones:** ninguna otra Txx en este archivo. Fuera de P420:
  `P421_tasks.md` T01 propone como opción tomar sus candidatos de corridas de
  P420; esa opción presupone que la exactitud copiada de `metrics.json` es
  reproducible desde `model.pkl`, que es lo que esta T01 verifica. Si P421 T01
  se aprueba con esa opción, conviene ejecutar esta T01 primero.
  `P424_tasks.md` T01 menciona las corridas de P420 sólo como alternativa si
  las versiones de P424 resultan indistinguibles. Capacidad: P420 tiene cuatro
  highlights y un solo script; el cambio añade una función, un campo de
  configuración, una corrida y una prueba.
- **Criterio de aceptación:** S05 encuentra (1) en `professor/main.py` una
  función que devuelve un `sklearn.pipeline.Pipeline` con `StandardScaler`
  antes de `KNeighborsClassifier(n_neighbors=7)` y sin escalado para el árbol,
  ajustado sólo con la partición de entrenamiento, y que es lo que `save_run`
  serializa; (2) `config.json` de las corridas nuevas declara los pasos del
  `Pipeline`; (3) en `submission/experiments/` al menos una corrida nueva de
  KNN con preparación embebida, además de las dos existentes; (4) una prueba
  en `tests/test_activity.py` que, para cada corrida de `index.json`, carga
  `model.pkl`, puntúa `data/test.csv` de esa carpeta y reproduce
  `test_accuracy` de `metrics.json`, y verifica que la carpeta está completa;
  (5) una prueba de profesor que verifica que el `Pipeline` de KNN contiene el
  escalador; y (6) H01–H03 presentes, `test_01` y `test_02` sin cambios y H04
  actualizado.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P420_experiment_tracking/

0. Inspecciona primero professor/main.py (prepare_data, build_model,
   save_run, update_index), professor/test_main.py, src/main.py,
   HOW_TO_RUN_ME.txt, submission/experiments/ (index.json y las dos
   carpetas) y tests/test_activity.py. Si la implementación no coincide con
   design/courses/productos/P420_activity.md (por ejemplo, si KNN ya se
   escala o ya existe una prueba que recarga model.pkl y reproduce la
   métrica), detente e informa sin modificar nada. Comprueba también cómo se
   llama la clave de exactitud en metrics.json y qué columnas tiene
   data/test.csv; usa esos nombres, no los supuestos aquí.
1. No cambies prepare_data, la partición, build_model ni las pruebas
   test_01 y test_02. No borres ni modifiques las dos carpetas de corrida
   existentes.
2. Añade build_pipeline(model_name) que devuelva
   Pipeline([("scaler", StandardScaler()), ("model", build_model("knn"))])
   para knn y Pipeline([("model", build_model("tree"))]) para tree. Un
   docstring breve puede declarar la razón (la preparación se ajusta sólo con
   entrenamiento y viaja dentro del artefacto para que quien recupere la
   corrida puntúe igual que se evaluó); no describas lo que el código hace.
3. Haz que el flujo de main() ajuste build_pipeline(...) sólo con
   entrenamiento y que save_run serialice ese objeto en model.pkl. Añade a
   config.json un campo con los nombres de los pasos del Pipeline (por
   ejemplo, "pipeline_steps": ["scaler", "model"]). No añadas otros campos.
4. Actualiza src/main.py de forma coherente con el profesor: si expone
   build_model como plantilla con NotImplementedError, añade build_pipeline
   también como plantilla, sin resolverla.
5. Ejecuta professor/main.py --model knn (con un run_id nuevo) para añadir
   al menos una corrida de KNN con preparación embebida; si la corrida del
   árbol cambia de artefacto (ahora un Pipeline de un paso), añade también
   una corrida nueva del árbol y verifica que su exactitud sigue siendo
   0.5825. Si no lo es, detente e informa.
6. Añade a tests/test_activity.py una prueba que, para cada entrada de
   submission/experiments/index.json: verifique que su carpeta contiene
   data/train.csv, data/test.csv, config.json, metrics.json y model.pkl;
   cargue model.pkl; prediga sobre las variables de data/test.csv (todas
   excepto quality); y compare la exactitud con la de metrics.json con
   tolerancia absoluta 1e-9. Exige además al menos dos corridas. La prueba
   debe localizar archivos relativos al propio archivo de prueba, no al
   directorio de ejecución. No elimines pruebas existentes.
7. Añade a professor/test_main.py una prueba que verifique que
   build_pipeline("knn") contiene un StandardScaler antes del clasificador y
   que build_pipeline("tree") no lo contiene.
8. Añade a HOW_TO_RUN_ME.txt un paso que pida ejecutar pytest y leer, en
   2–3 líneas, por qué la corrida nueva de KNN difiere de la anterior y por
   qué la preparación debe estar dentro de model.pkl.
9. Ejecuta las pruebas de profesor y de la actividad sin errores.
10. No modifiques otras actividades, traceability.yaml ni design/.
```
