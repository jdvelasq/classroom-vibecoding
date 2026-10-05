# P428 — Propuestas de mejora

**Línea base:** `P428_activity.md` (entrada S02 más reciente: `S02.P428.01`).

## T01 — Derivar la cadencia de la agenda de la necesidad de actualización del consumidor y declararla como cláusula del contrato operativo

- **Estado:** pendiente de discusión
- **Tipo:** encuadre + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/professional-learning/perceptual-edge-dashboard-design-requirements-questionnaire.md` p. 1 — el levantamiento de requisitos empieza por «How often should the data be updated in the dashboard?» y sigue con «Who will use the dashboard?» y «What actions will they take in response to these answers?»: la frecuencia de actualización es un requisito que se pregunta al usuario junto con su uso, no un parámetro técnico (Claude, 2026-10-05). Fuente *professional-learning* (consultoría de visualización): aporta la forma de la pregunta de levantamiento, no un estándar; la propuesta se sostiene sobre todo en el defecto que registra `S02.P428.01`.
- **Qué gana el estudiante:** entender que la cadencia de una ejecución
  programada es una cláusula del contrato operativo (`productos.C01`), no un
  parámetro de la biblioteca. Hoy la agenda corre `every(10).seconds` sobre
  un extracto estático sin fecha, y S02 registra que «la cadencia no se
  deriva de ninguna necesidad del uso» y que el taller «puede leerse como
  entrenamiento en una biblioteca de agendamiento». Con el cambio, el
  estudiante lee la cadencia de un contrato que nombra consumidor, decisión
  y frecuencia requerida; distingue esa cadencia operativa de la aceleración
  de demostración que se usa en clase; y el reporte declara cuándo vence el
  siguiente refresco. Así la marca `executed_at` (H03) deja de ser sólo un
  instante y permite al consumidor juzgar si el reporte está vencido.
  Ningún taller deriva hoy la cadencia del uso (P454 la registra como campo
  sin justificarla). **Materialidad:** fortalece el contrato de la capacidad
  y la lectura de frescura, no la herramienta. No resuelve el riesgo de
  identidad de fondo: el indicador sigue siendo la suma por fábrica de
  cuatro filas sin fecha, repetida en P400–P418, de modo que la cláusula se
  declara sobre una fuente que en esta actividad no cambia. Si el profesor
  no aporta la necesidad del consumidor, la propuesta sería un parámetro
  más en un archivo de configuración (pulido de herramienta) y no debe
  ejecutarse.
- **Anclas actuales:** H01 (cálculo separado de la agenda), H02 (agenda
  local y su límite; «la periodicidad no se justifica»), H03 (marca UTC);
  superficies S02 (cadencia fija de 10 s), S03 (reporte), S04 (pruebas), S05
  (`HOW_TO_RUN_ME.txt`); dependencias «Recibe de P400, P412, P413, P417,
  P418» y «Habilita para P429».
- **Alternativas menores descartadas:** escribir en `HOW_TO_RUN_ME.txt` que
  10 s es una cadencia de demostración (nivel 1) aclara el límite, pero no
  da al estudiante la práctica de derivar la cadencia de un requisito ni
  hace verificable que la agenda use la cadencia contratada. Cambiar sólo
  el literal a `every().day` ocultaría la ejecución en clase y no vincularía
  la cadencia con el consumidor.
- **Contrato de no regresión:** se conservan H01–H03, `build_report` como
  función pura y su prueba de profesor, `data/daily_operations.csv`, la
  agenda con `schedule` y el ciclo `run_pending`, el límite declarado en
  `HOW_TO_RUN_ME.txt` y las claves actuales de `scheduled_report.json`
  (totales por fábrica y `executed_at`). La ejecución en clase sigue siendo
  observable cada pocos segundos, ahora como aceleración rotulada. Se añaden
  un archivo de contrato y dos claves al reporte. No se añaden dependencias
  al `requirements.txt` local.
- **Interacciones:** única propuesta de P428. Fuera de P428: P429 reutiliza
  el mismo cálculo y no consume el reporte; no se afecta. El mismo contrato
  podría luego justificar el umbral de frescura de P439 o la frecuencia de
  la ficha de P454; eso sería propuesta de esas actividades.
- **Criterio de aceptación:** S05 encuentra (1) un contrato en `data/` con
  consumidor, decisión, cadencia requerida y su justificación, aprobados por
  el profesor y no inventados, y separado de la aceleración de demostración;
  (2) una agenda que toma su intervalo de ese contrato, sin literal de
  cadencia en `main`; (3) un reporte con la cadencia contratada y el
  vencimiento del siguiente refresco (`executed_at` + cadencia); y (4)
  pruebas que verifican esas claves, su coherencia con el contrato y la
  derivación del intervalo. Un highlight nuevo o H02/H03 modificados lo
  registran. H01–H03 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P428_schedule/

0. Inspecciona primero professor/main.py, professor/test_main.py,
   HOW_TO_RUN_ME.txt, requirements.txt, data/daily_operations.csv,
   src/main.py, submission/scheduled_report.json y tests/test_activity.py.
   Si la implementación no coincide con
   design/courses/productos/P428_activity.md (por ejemplo, si la cadencia ya
   se lee de un contrato), detente e informa sin modificar nada.
1. NECESIDAD DEL CONSUMIDOR: no inventes consumidor, decisión ni frecuencia.
   La actividad no los evidencia (la tarjeta de P408 nombra al «equipo de
   operaciones» como consumidor del indicador, pero no su necesidad de
   actualización). Usa el texto que el profesor haya aprobado en la
   discusión de esta T01 (registrado en P428_log.md): quién consume el total
   por fábrica, qué decisión apoya, con qué frecuencia necesita el dato
   actualizado y por qué. Si no existe, detente y pídelo.
2. Crea data/refresh_contract.json con consumer, decision,
   refresh_cadence_seconds (la cadencia operativa aprobada, en segundos),
   rationale y demo_interval_seconds (10, la aceleración usada en clase,
   rotulada como tal).
3. En professor/main.py:
   a. Añade una función pura que reciba el contrato y devuelva el intervalo
      de agenda: demo_interval_seconds cuando se pide modo demostración y
      refresh_cadence_seconds en otro caso. El modo demostración se activa
      explícitamente (por ejemplo, un argumento o variable de entorno
      documentada en HOW_TO_RUN_ME.txt); main no contiene literales de
      cadencia.
   b. Haz que el reporte añada refresh_cadence_seconds y next_refresh_due
      (executed_at + refresh_cadence_seconds, en UTC ISO 8601). La cadencia
      del reporte es siempre la contratada, aunque se ejecute en modo
      demostración. No cambies los totales por fábrica ni executed_at.
   Usa sólo la biblioteca estándar para fechas; no modifiques
   requirements.txt.
4. Añade a HOW_TO_RUN_ME.txt 2–4 líneas: la cadencia operativa sale del
   contrato y del consumidor; 10 s es una aceleración de clase; cómo leer
   next_refresh_due para saber si el reporte está vencido. Conserva el
   límite actual (la agenda termina con la terminal).
5. En professor/test_main.py añade pruebas de la función del paso 3a (ambos
   modos) y de que el reporte de build_report incluye
   refresh_cadence_seconds y next_refresh_due coherentes con un contrato de
   prueba. Si cambiar la firma de build_report rompe la prueba existente,
   no la modifiques: añade las claves en una función separada que envuelva
   build_report. No elimines pruebas existentes.
6. En tests/test_activity.py añade una prueba que lea
   submission/scheduled_report.json y data/refresh_contract.json (rutas
   relativas al archivo de prueba) y verifique que next_refresh_due -
   executed_at == refresh_cadence_seconds del contrato. No elimines test_01.
7. Genera el reporte con una ejecución de generate_report y ejecuta las
   pruebas de professor/ y de tests/ sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
