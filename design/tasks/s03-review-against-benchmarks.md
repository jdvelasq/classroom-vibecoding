# S03 — Proponer mejoras a un curso a partir de un benchmark

## Ejecución

```text
execute design/tasks/s03-review-against-benchmarks.md \
  course=<curso> benchmark=<ruta-md> executor=<LLM>
```

`benchmark` es **un** archivo bajo `design/benchmarks-md/` (versión Markdown
generada por S01 a partir de `design/benchmarks-pdf/`). Los documentos se
procesan uno a la vez y en secuencia: cada ejecución integra un documento en
las propuestas que dejaron los anteriores. `executor` identifica quién realizó
la lectura y queda registrado en los logs.

## Propósito y lugar en el ciclo

```text
S01 convertir PDF → S02 describir Pxxx (línea base) → S03 proponer
→ discusión con el profesor → S04 ejecutar lo aprobado → S05 verificar
```

S03 responde, para un documento y un curso:

> ¿Este documento justifica cambiar algo que mejore **de forma material** lo
> que el estudiante aprende en algún taller, sin regresión de lo que ya
> funciona?

S03 sólo **propone**. No modifica `implementation/`, `Pxxx_activity.md` ni
`traceability.yaml`. Sus propuestas quedan pendientes de discusión y nada se
ejecuta sin aprobación explícita. «Ninguna propuesta» es un resultado válido y
frecuente.

## Entradas

Lee y cumple `AGENTS.md`. Lee sustantivamente:

- el documento `design/benchmarks-md/<ruta>.md`, completo. Cita por página con
  las marcas `<!-- fin de página N -->`. Si la cabecera o una nota `⚠️ S01`
  señala una página con contenido en imagen y esa página parece relevante,
  consulta sólo esa página del PDF homónimo en `design/benchmarks-pdf/`;
- para cada Pxxx del curso: `Pxxx_activity.md`, `Pxxx_log.md` y
  `Pxxx_tasks.md` si existe;
- `design/courses/<curso>/course_tasks.md` si existe; y
- `design/courses/<curso>/course_log.md` sólo si existe, para contexto.

No lees `implementation/`: S02 es la lectura auditable de la implementación.
Tampoco lees otros documentos de benchmarks, `benchmark_reviews/` históricos,
`design/synthesis/` ni la web.

### Precondiciones

- Si el `Pxxx_log.md` de las actividades ya registra este documento con el
  mismo `source_sha256` (cabecera del `.md`), el documento ya fue revisado:
  informa y termina sin cambios.
- Si a un Pxxx le falta `Pxxx_activity.md`, o éste no sigue el contrato
  vigente de S02, no inventes su contenido: registra el límite en el resumen
  final y no propongas cambios anclados a esa actividad.

## Función de la evidencia

Toma la familia de la cabecera (`family:`) y restringe la inferencia:

- **authoritative:** principios, estándares o marcos durables; respalda
  expectativas generales, no un syllabus que copiar.
- **institutional:** cómo otra institución operacionaliza un programa; ilustra
  posibilidades, no impone identidad curricular.
- **governmental:** pertinencia laboral o de política pública; no define un
  estándar ni prescribe herramientas.
- **professional-learning:** señales de práctica y herramientas; no reemplaza
  la evidencia curricular o disciplinar.
- **literature-derived:** perspectiva histórica, metodológica u organizacional;
  distingue contexto de prescripción vigente.

Analytics conserva la identidad curricular; las demás disciplinas son
contribuyentes. Aplica las preguntas de auditoría de `AGENTS.md` a toda
propuesta material.

## Criterios de decisión

### 1. Materialidad

Una señal genera propuesta **sólo** si cumple al menos una condición:

- cambia lo que el estudiante es capaz de **hacer o entender** al terminar el
  taller (una capacidad, un contraste, una forma de evidencia o un producto
  que hoy no ejerce); o
- corrige un **defecto real**: algo incorrecto, engañoso u obsoleto en lo que
  el taller enseña.

No generan propuesta: variaciones de algo ya cubierto (otra pregunta de negocio
cuando las existentes cubren el objetivo pedagógico, otro dataset equivalente,
otra biblioteca para lo mismo); la mera presencia de una técnica en el
documento; el prestigio de la fuente; ni la novedad por sí misma.

### 2. Sin regresión

Lo que ya funciona está en los highlights `HNN`, superficies `SNN` y
dependencias de cada `Pxxx_activity.md`. Toda propuesta declara cuáles
conserva y, si sustituye alguno, por qué y con qué evidencia al menos
equivalente. Prefiere siempre el menor cambio que logre el beneficio:

1. aclarar o hacer visible algo que ya existe;
2. extender localmente sin cambiar caso, producto ni contratos;
3. cambiar materialmente la actividad;
4. crear una actividad nueva.

La carga de justificación crece en ese orden.

### 3. Identidad y capacidad del taller

Cada taller enseña algo concreto en lo técnico y lo pedagógico; esa identidad
está en su pregunta, producto y highlights. Una propuesta que **refuerza** esa
contribución va a `Pxxx_tasks.md`. Una propuesta que **agrega una segunda
contribución distinta** no se incrusta: va a `course_tasks.md` como actividad
nueva. Un taller no puede crecer indefinidamente.

### 4. Secuencia

Los grupos avanzan a ritmos distintos y algunos no llegan a los últimos
talleres. Una actividad nueva o un cambio de orden debe declarar qué
actividades desplaza y qué perdería un grupo que avanza menos.

### 5. Rechazos previos

Antes de proponer, busca en `Pxxx_log.md` rechazos de propuestas equivalentes.
Si existe uno, no la propongas de nuevo, salvo que el documento aporte un
argumento distinto; en ese caso, cita el rechazo anterior y explica qué cambia.

## Método

1. **Extrae señales** del documento: capacidades, técnicas, casos de uso,
   KPIs, preguntas de negocio, metodologías, prácticas de implementación,
   formas de evaluación y guardrails, cada una con su página. Si el documento
   tiene índice o temario, recórrelo completo.
2. **Contrasta cada señal** con los `Pxxx_activity.md`: primero con el índice
   de comparación externa, después con `HNN` y `SNN`. Nunca contra el título
   del taller.
3. **Clasifica cada señal** en una sola categoría: ya cubierta, marginal (no
   pasa materialidad), rechazada previamente, fuera de alcance (desplaza la
   identidad de Analytics o carece de caso/datos que permitan enseñarla con
   rigor), mejora de un Pxxx existente o actividad nueva.
4. **Integra** cada mejora con las propuestas existentes. Si `Pxxx_tasks.md`
   ya contiene una propuesta equivalente, no la dupliques: añade este
   documento a sus fuentes y ajusta su contenido sólo si el documento aporta
   algo nuevo. Lo mismo para `course_tasks.md`.
5. **Revisa interacciones**: las propuestas de un mismo Pxxx se discutirán y
   ejecutarán en conjunto. Declara cuáles dependen, compiten o se refuerzan.
6. **Registra** la revisión en los logs (ver «Salidas»).

## Salidas

S03 crea o actualiza sólo estos archivos de `design/courses/<curso>/`.

### `Pxxx_tasks.md` — propuestas vigentes de una actividad

Estado actual, no historial. Se crea al primer cambio propuesto y queda vacío
(«No hay propuestas pendientes.») cuando S05 verifica la ejecución.

````markdown
# Pxxx — Propuestas de mejora

**Línea base:** `Pxxx_activity.md` (entrada S02 más reciente: `S02.Pxxx.NN`).

## T01 — Título preciso del cambio

- **Estado:** pendiente de discusión | aprobada | rechazada
- **Tipo:** encuadre | producto/evidencia | método | caso/datos | proceso | pedagogía
- **Fuentes:** `design/benchmarks-md/<ruta>.md` p. N (executor, fecha); una
  línea por documento que respalda la propuesta.
- **Qué gana el estudiante:** la capacidad o comprensión nueva, o el defecto
  que se corrige. Es la justificación de materialidad.
- **Anclas actuales:** `HNN`, `SNN` y dependencias afectadas.
- **Alternativas menores descartadas:** por qué aclarar o extender no basta,
  cuando aplique.
- **Contrato de no regresión:** highlights, superficies, artefactos, pruebas y
  dependencias que se conservan; sustituciones explícitas y su evidencia.
- **Interacciones:** con otras `Txx` de este archivo.
- **Criterio de aceptación:** lo que S05 debe verificar; normalmente un
  highlight nuevo o modificado con evidencia en notebook, `submission/` o
  pruebas.

### Instrucciones de ejecución

Prompt autocontenido para S04, ejecutable por cualquier herramienta. Indica
las rutas a inspeccionar y modificar (tomadas de las `SNN`), los pasos, qué no
debe tocarse, qué pruebas o artefactos añadir o actualizar y cómo comprobar
el criterio de aceptación. Como S03 no lee `implementation/`, las
instrucciones exigen que S04 inspeccione primero las rutas y se detenga si la
implementación contradice la descripción.
````

Los IDs `T01`, `T02`… son estables dentro del archivo y no se reutilizan.

### `course_tasks.md` — actividades nuevas por decidir

````markdown
# <curso> — Actividades nuevas por decidir

## N01 — ⚠️ PENDIENTE DE DECISIÓN — Nombre tentativo

- **Fuentes:** documento y páginas; una línea por documento.
- **Contribución distinta:** qué enseñaría que ninguna Pxxx enseña, y por qué
  no cabe en una existente sin desdibujar su identidad.
- **Posición propuesta:** después de Pxxx; qué recibe de las anteriores y qué
  habilita para las siguientes.
- **Efecto en la secuencia:** qué actividades desplaza y qué perdería un grupo
  que avanza menos.
- **Caso y datos:** condición concreta que exige; o «requiere definición».
- **Producto de Analytics:** pregunta, producto terminal y límite.
- **Criterio de aceptación de una primera versión.**
````

Si en la discusión se aprueba, en ese momento se decide numeración y posición
y S04 crea su primera versión con su trío de archivos; la entrada sale de
`course_tasks.md`. Si se rechaza, sale con registro en `course_log.md`.

### `Pxxx_log.md` — registro de la revisión

Para **cada** Pxxx del curso agrega una entrada breve, aunque no haya
propuestas, para que conste qué documentos ya fueron revisados:

```markdown
## S03.Pxxx.NN

- **Fecha / executor:** AAAA-MM-DD / <executor>.
- **Documento:** `design/benchmarks-md/<ruta>.md` (`source_sha256`: <hash>).
- **Resultado:** sin cambios | refuerza T0n | propone T0n | aporta a N0n.
- **Señales descartadas relevantes:** sólo las que alguien podría esperar ver
  propuestas, con su categoría (ya cubierta, marginal, fuera de alcance,
  rechazada previamente).
```

## Discusión y decisiones (fuera de S03)

El profesor discute **todas** las propuestas de un Pxxx en conjunto, porque
interactúan. Al decidir:

- **aprobada:** queda en `Pxxx_tasks.md` con estado «aprobada» para S04;
- **rechazada:** se elimina de `Pxxx_tasks.md` y se registra en `Pxxx_log.md`
  como `DEC.Pxxx.NN` con la propuesta, sus fuentes y la razón del rechazo.
  Futuras ejecuciones de S03 la tratan como rechazo previo.

## Control antes de guardar

- Se leyó el documento completo y cada señal cita su página.
- Toda propuesta pasa el criterio de materialidad y dice qué gana el estudiante.
- Toda propuesta está anclada a `HNN`/`SNN` existentes o, si es actividad
  nueva, declara posición, contribución distinta y efecto en la secuencia.
- Se integró con propuestas existentes, sin duplicados.
- Se consultaron los rechazos previos.
- Cada propuesta tiene contrato de no regresión, criterio de aceptación e
  instrucciones de ejecución.
- Se registró la revisión en el log de cada Pxxx del curso.
- Se preservó la identidad de Analytics.
- No se modificó nada fuera de `Pxxx_tasks.md`, `course_tasks.md` y
  `Pxxx_log.md` del curso indicado.
