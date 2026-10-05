# P442 — Propuestas de mejora

**Línea base:** `P442_activity.md` (entrada S02 más reciente: `S02.P442.01`).

## T01 — Asignar a cada comprobación una severidad con su acción en lugar de un `all()` único

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/literature-derived/dataops-09-data-quality.md` p. 4 — tabla «Severidad | Acción requerida»: «Error | Detención del pipeline», «Alerta | Investigación de la falla», «Informativa | Ser consciente de la información»; cada falla de una prueba de datos tiene una consecuencia operativa distinta según su severidad, no un veredicto binario único (Claude, 2026-10-05). Fuente *literature-derived* (material de clase de seis páginas): aporta la perspectiva metodológica de la clasificación severidad→acción, no un estándar ni una herramienta; su peso es bajo.
- **Qué gana el estudiante:** convertir un veredicto de observabilidad en una
  decisión operativa sobre el producto que protege. Hoy
  `healthy = all(checks.values())` (H02) trata igual una caída de volumen y
  un esquema roto y no dice qué hacer: S02 registra «Sin ponderación,
  historia ni severidad» y que el reporte «no indica qué acción tomar ni a
  qué producto afecta». Con la mejora, cada señal declara su severidad junto
  a su umbral (extiende H01: cada señal ya viaja con su límite) y el reporte
  emite, además de `healthy`, la acción resultante: bloquear la publicación,
  abrir una investigación o sólo registrar. El estudiante distingue fallas
  que invalidan el producto de fallas que lo degradan.
- **Materialidad frente al riesgo de identidad de S02:** la propuesta sólo
  fortalece la operación de una capacidad analítica si la acción
  «bloquear la publicación» recae sobre un producto nombrado del curso (por
  ejemplo, la tabla curada por fábrica de P412/P432/P443) y si la severidad
  de cada señal se justifica por su efecto sobre ese producto. Sin ese
  anclaje, añadir una columna de severidad a señales que no observan nada
  identificable es pulir una práctica de herramienta y no resuelve la
  pregunta 5 de auditoría que S02 dejó abierta. Por eso las instrucciones se
  detienen si el profesor no aporta el producto protegido y la asignación de
  severidades.
- **Anclas actuales:** H01 (señal con umbral), H02 (veredicto integrado),
  H03 (bordes inclusivos en pruebas); superficies S01 (`data/signals.json`),
  S02 (`professor/main.py`: tres comprobaciones fijas y `all()`), S03
  (`submission/observability_report.json`) y S04 (pruebas); dependencia
  «Recibe de P439» (práctica de frescura). Relación con P446 H01 (la alerta
  de frescura prescribe «No publique un reporte nuevo»).
- **Alternativas menores descartadas:** aclarar en texto que unas fallas
  pesan más que otras no cambia el producto: el reporte seguiría sin acción.
  Ponderar las señales en un puntaje agregado ocultaría cuál falla y por qué;
  la severidad categórica conserva la lectura por señal de H02.
- **Contrato de no regresión:** se conservan H01–H03, los cinco campos
  actuales de `signals.json` y sus valores, las tres comprobaciones con sus
  umbrales inclusivos, la clave `healthy` con su semántica actual
  (`all()` sobre las comprobaciones) y las claves actuales de
  `observability_report.json`. Las pruebas de profesor existentes se
  mantienen sin cambios. Se añaden la severidad por señal, la acción por
  comprobación fallida y una acción agregada; no se sustituye nada.
- **Interacciones:** ninguna otra `Txx` en este archivo. Fuera de P442: la
  severidad de la frescura debe ser coherente con P446 H01, que ya ordena no
  publicar ante una alerta de frescura; si el profesor asigna a la frescura
  una severidad distinta de «error», la discrepancia con P446 debe quedar
  decidida y registrada, no resuelta por la herramienta. Se refuerza con
  cualquier decisión de curso que ancle las señales de P442 a un dataset del
  caso de fábricas (límite de S02); esta T01 no toma esa decisión.
  Capacidad: P442 tiene tres highlights y un `main.py` breve; el cambio es
  local (nivel 2) y no compromete la sesión.
- **Criterio de aceptación:** S05 encuentra (1) el producto protegido y la
  severidad de cada señal tal como los aprobó el profesor, registrados en
  `P442_log.md` y reflejados en `data/signals.json`; (2) un highlight nuevo
  o H02 modificado en el que `submission/observability_report.json` contiene,
  junto a `checks` y `healthy`, la severidad de cada comprobación y una
  acción agregada derivada de la falla más severa; y (3) pruebas que
  verifiquen que una falla de severidad «error» produce el bloqueo de la
  publicación, una «alerta» la investigación y una «informativa» sólo el
  registro, y que sin fallas no hay acción restrictiva. H01–H03 siguen
  presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P442_data_observability/

0. Inspecciona primero data/signals.json, professor/main.py,
   professor/test_main.py, src/main.py, submission/ y tests/. Si la
   implementación no coincide con design/courses/productos/P442_activity.md
   (cinco campos, tres comprobaciones, healthy = all(...)), o si ya asigna
   severidad o acción a las comprobaciones, detente e informa sin modificar
   nada.
1. NO INVENTES el producto ni las severidades. Usa el texto que el profesor
   haya aprobado en la discusión de esta T01 (registrado en P442_log.md):
   (a) qué producto analítico del curso protege este insumo y cuya
   publicación se bloquearía, y (b) la severidad de cada señal (error,
   warning o info) con una línea de justificación por su efecto sobre ese
   producto. Si no existe, detente y pídelo. Si la severidad de freshness
   no es error, verifica que el registro del profesor reconozca la
   discrepancia con P446 (que ordena no publicar ante una alerta de
   frescura); si no la reconoce, detente e informa.
2. En data/signals.json añade, sin cambiar los cinco campos actuales ni sus
   valores, un objeto "severity" con las claves freshness, volume y schema y
   los valores aprobados, y un campo "protected_product" con el nombre
   aprobado.
3. En professor/main.py conserva build_observability_report, las tres
   comprobaciones, sus umbrales inclusivos y healthy = all(...). Añade:
   a. una correspondencia fija severidad -> acción:
      error -> block_publication, warning -> investigate, info -> log;
   b. en el reporte, "severity" por comprobación y "failed_actions" con la
      acción de cada comprobación fallida;
   c. "action": la acción de la comprobación fallida más severa
      (error > warning > info), o "none" si ninguna falla;
   d. "protected_product" copiado de la entrada.
   Una severidad fuera de {error, warning, info} o ausente para una
   comprobación debe lanzar ValueError con un mensaje que nombre la señal.
4. Regenera submission/observability_report.json con main(). Las claves
   actuales (checks y healthy, con sus valores) deben quedar idénticas.
5. Junto a la correspondencia severidad -> acción deja un comentario de
   decisión de 2–3 líneas (AGENTS.md: comentarios reservados a decisiones)
   que diga por qué healthy no basta para decidir la publicación del
   producto protegido. No modifiques src/main.py (plantilla del
   estudiante).
6. Añade a professor/test_main.py pruebas con entradas inyectadas que
   verifiquen: una falla error produce action == "block_publication"; una
   sola falla warning produce "investigate"; una sola falla info produce
   "log"; sin fallas, action == "none"; con fallas de distinta severidad
   gana la más severa; una severidad inválida lanza ValueError. Añade a
   tests/test_activity.py una prueba que verifique que el reporte entregado
   contiene severity para las tres comprobaciones y una clave action con un
   valor del conjunto permitido. No elimines ni modifiques pruebas
   existentes.
7. Ejecuta main() y todas las pruebas de la actividad sin errores.
8. No modifiques otras actividades (en particular P439 y P446),
   traceability.yaml ni design/.
```
