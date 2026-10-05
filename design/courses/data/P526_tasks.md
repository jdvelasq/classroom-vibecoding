# P526 — Propuestas de mejora

**Línea base:** `P526_activity.md` (entrada S02 más reciente: `S02.P526.01`).

## T01 — No copiar a la entrega los identificadores de personas que la pregunta no necesita: quitar `user_id`, seudonimizar `user_session` y documentar la sensibilidad y restricción de uso

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia + caso/datos
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` pp. 41, 84 y 108 — competencia T1 de responsabilidad social: «Demonstrate awareness about data sensitiveness when data is processed as an input» y «Apply techniques to provide data privacy during raw data processing, such as provide ranges or salting techniques» (p. 84); «Ways of maintaining the confidentiality of data» (p. 108); «The privacy and confidentiality of information is a vital matter» (p. 41) (Claude, 2026-10-05). Fuente *authoritative*: respalda tratar identificadores al procesar datos crudos, no un contenido de privacidad formal.
- **Qué gana el estudiante:** decidir qué identificadores de personas
  necesita la métrica y cuáles no deben salir en el producto. Hoy
  `event_replay.csv` copia `user_id` y `user_session` de 112 eventos de una
  muestra privada a `submission/` (S04), sin restricción documentada (S01;
  S02.P526.01). La tasa de conversión al grano sesión (H03) necesita una
  llave de sesión para agregar, pero no su valor original ni `user_id`. El
  estudiante practica la distinción entre llave de agregación y dato
  personal: conserva la unidad de análisis con un seudónimo estable, retira
  lo que la pregunta no usa y declara la sensibilidad y la restricción de
  uso. P526 es el caso del curso con identificadores reales de
  comportamiento, lo que hace visible la parte «responsable» de `data.C04`.
- **Anclas actuales:** H01 (tiempo de evento frente a orden de llegada,
  persistido en `event_replay.csv`), H03 (conversión e ingreso por
  `user_session`); superficies S01 (dataset: «identificadores de usuario y
  sesión; sin procedencia ni restricción documentadas»), S03 (métrica), S04
  (producto: «`event_replay.csv` copia `user_id` y `user_session`») y S05
  (pruebas).
- **Alternativas menores descartadas:** declarar la restricción sin cambiar
  los archivos deja los identificadores en la entrega. Retirar también
  `user_session` rompería H03, porque es la unidad de análisis; por eso se
  seudonimiza. Quitar `user_id` de `data/events.csv.gz` cambiaría el insumo
  del caso: no forma parte de esta T01 salvo decisión del profesor.
- **Contrato de no regresión:** se conservan H01–H03, la simulación
  determinista (`batch[2:] + batch[:2]`), la marca `is_late`, la definición
  `converted = revenue > 0` y las métricas actuales: 112 eventos, 28
  tardíos, 16 sesiones, 8 convertidas, tasa 0.5. Los tres archivos de
  `submission/` conservan sus filas y sus demás columnas; sólo desaparece
  `user_id` y `user_session` pasa a un seudónimo estable (el mismo en
  `event_replay.csv` y `session_conversion.csv`). `data/events.csv.gz` no
  cambia. Las pruebas existentes se mantienen. No se introduce privacidad
  diferencial, anonimización formal ni normativa extranjera: el seudónimo
  no es anonimización y así se declara.
- **Interacciones:** no hay otras `Txx` en este archivo. S02 registró además
  que la «confusión» entre orden de llegada y comportamiento que promete la
  pregunta no se muestra, porque las métricas por sesión no dependen del
  orden; ninguna fuente asignada respalda ese cambio y queda fuera de esta
  T01, sólo como contexto (si se propusiera después, este seudónimo no lo
  afecta). `src/main.py` (S06) es una plantilla vacía: la prueba nueva
  también exige al estudiante no copiar `user_id`, lo que cambia su
  contrato de entrega y debe anunciarse. Capacidad: un cambio local en
  `professor/main.py` y una prueba; no compromete el taller.
- **Criterio de aceptación:** S05 encuentra (1) que ningún archivo de
  `submission/` contiene la columna `user_id` ni un valor original de
  `user_session` de `data/events.csv.gz`; (2) que `user_session` está
  reemplazado por un seudónimo estable y consistente entre
  `event_replay.csv` y `session_conversion.csv`, sin persistir la tabla de
  correspondencia; (3) las métricas de `event_summary.csv` idénticas a las
  actuales; (4) en el comentario inicial de `professor/main.py`, junto a la
  pregunta, la procedencia conocida, la condición de muestra privada y su
  restricción de uso, y qué identificadores se retiran o seudonimizan y por
  qué; y (5) una prueba nueva que verifica (1) y (2). H01–H03 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/data/P526_eventos/

0. Inspecciona primero data/events.csv.gz, professor/main.py, src/main.py,
   los tres CSV de submission/ y tests/test_activity.py. Si la
   implementación no coincide con design/courses/data/P526_activity.md, o
   si submission/ ya no contiene user_id ni valores originales de
   user_session, detente e informa sin modificar nada.
1. RESTRICCIÓN: no inventes procedencia, licencia ni condición de uso. Usa
   el texto que el profesor haya aprobado en la discusión de esta T01
   (registrado en P526_log.md); como contexto, design/ registra en
   case-selection.md que la fuente es una «muestra privada de eventos
   reales». Si no hay texto aprobado, detente y pídelo.
2. No cambies replay_arrivals, mark_late_events, la definición de
   conversión ni data/events.csv.gz.
3. En professor/main.py, después de leer los eventos y antes de escribir
   las salidas:
   a. Retira user_id de los registros que se persisten.
   b. Sustituye user_session por un seudónimo estable (por ejemplo,
      session_01 … session_16 por orden de primera aparición en el archivo
      de origen), aplicado igual en event_replay.csv y
      session_conversion.csv. No persistas la correspondencia.
   c. Amplía el comentario inicial (donde está la pregunta) con la
      procedencia conocida, la restricción aprobada, qué identificadores se
      retiran o seudonimizan y por qué, y que el seudónimo no anonimiza: el
      evento sigue siendo enlazable con la fuente. Usa sólo comentarios que
      expliquen esa decisión y restricción, conforme a AGENTS.md.
4. Regenera los tres archivos de submission/ y comprueba que
   event_summary.csv conserva 112 eventos, 28 tardíos, 16 sesiones, 8
   convertidas y tasa 0.5, y que las filas por sesión coinciden con las
   actuales salvo la llave.
5. Añade a tests/ una prueba que verifique que ninguna cabecera de
   submission/ contiene user_id, que ningún valor de user_session de
   data/events.csv.gz aparece en submission/, y que los seudónimos de
   event_replay.csv y session_conversion.csv forman el mismo conjunto.
   Resuelve la raíz de la actividad de forma independiente de la
   profundidad de distribución. No elimines pruebas existentes.
6. Ejecuta professor/main.py y las pruebas de la actividad sin errores.
7. No modifiques otras actividades, traceability.yaml ni design/.
```
