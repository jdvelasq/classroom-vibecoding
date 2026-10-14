# Formato de las descripciones y la auditoría de las actividades

Versión 0.1 (borrador)

## Propósito

Definir cómo se registran, para cada curso, la descripción de sus
actividades presenciales (`Pxxx_`), su registro, las propuestas de cambio,
la cobertura y la trazabilidad de cada actividad frente a lo que el curso
debe cubrir según la cadena de diseño:

```text
02-competencies → 03-learning-outcomes → 04-curriculum → 05-implementation
(mapa)            (perfil y RA)          (RA × cursos,    (actividades Pxxx)
                                          RC de pregrado)
```

La skill `auditing-activities` hace dos cosas, siempre por curso:

- **describe** cada `Pxxx` nueva o sin descripción desde su implementación
  observable: es la línea base (método en `describing.md`); y
- **audita** esa línea base frente a lo que el curso debe cubrir y clasifica
  cada actividad: queda igual, necesita un cambio puntual o pasa a una
  decisión de curso (método en `auditing.md`).

No modifica la implementación de ninguna actividad.

## Archivos

Las rutas se fijan en un solo lugar, `scripts/paths.py`. Hoy son:

| Archivo | Contenido |
|---|---|
| `05-implementation/<curso>/Pxxx_<nombre>/activity.md` | Descripción vigente de la actividad. |
| `05-implementation/<curso>/Pxxx_<nombre>/log.md` | Registro acumulativo, opcional: entradas `S02`, `AUD`, `DEC` y notas. |
| `05-implementation/<curso>/Pxxx_<nombre>/tasks.md` | Cambios puntuales propuestos para la actividad (`T01`, …), con lo que hay que cambiar exactamente. |
| `05-implementation/<curso>/tasks.md` | Actividades nuevas y reorganizaciones propuestas para el curso (`N01`, …), descritas en detalle. |
| `05-implementation/<curso>/audit.md` | Cobertura vigente del curso, reescrita en cada auditoría. |
| `05-implementation/<curso>/traceability.yaml` | Qué resultados del curso y competencias sirve cada actividad. |

`activity.md`, `log.md` y `tasks.md` acompañan a la implementación pero no
son material del estudiante: la distribución del curso no debe copiarlos.

Una descripción existente no se regenera. Sólo se describen las
actividades sin `activity.md`; volver a describir una actividad requiere
que david lo pida.

## Notebooks sin celdas markdown

Los notebooks de una actividad no tienen celdas markdown, por definición:
son notebooks de actividad de clase, no material para que el estudiante lea.
Ninguna propuesta agrega una celda markdown ni texto explicativo al
notebook. Lo que hay que explicar lo explica el profesor en la sesión.
Cuando debe quedar evidencia, se persiste como un artefacto en
`submission/`, o como el comentario de primera línea de una celda de
código que `AGENTS.md` admite; si no, se descarta.

## Límite pedagógico de una actividad

Una actividad es un problema típico, claro y bien definido, que se resuelve
en una sesión corta. Una actividad larga pierde su fin. Por eso:

- una actividad tiene una contribución principal, visible en su pregunta,
  su producto y sus highlights;
- un cambio puntual refuerza esa contribución sin alargarla de forma
  apreciable;
- lo que agrega una segunda contribución distinta, o alarga la actividad,
  no se incrusta: es una decisión de curso (actividad nueva o
  reorganización de la secuencia).

## Descripción: `activity.md`

Las secciones van en este orden, con estos títulos exactos. Se añaden
secciones sólo cuando la evidencia lo requiere.

```markdown
# Pxxx — Nombre observado

## Actividad actual implementada

**Implementación:** `05-implementation/<curso>/Pxxx_nombre/`.

### Preguntas analíticas actuales

- Pregunta 1.
- Pregunta 2, si está evidenciada.

Breve descripción del caso, datos, producto terminal y límites observables.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** lo evidenciado, o «no evidenciado».
- **Producto terminal:** explicación, predicción, política, capacidad de datos
  u otro artefacto observable.
- **Uso y límite:** qué permite hacer el producto y qué no permite inferir o
  decidir.
- **Disciplinas contribuyentes:** métodos, datos o software que sirven al
  producto de Analytics, sin convertirlos en la identidad del taller.

### Highlights de contribución

- **H01 — Verbo de capacidad (caso y datos):** mecanismo concreto, artefacto
  o comportamiento observable; relación con Pxxx anteriores; qué se perdería
  sin este hito.
- **H02 — …:** …

### Inventario técnico de implementación

- **Introduce / extiende / reutiliza / aplica en nuevo caso:** práctica concreta.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |

### Relación técnica con actividades anteriores

Comparación breve, incluidas posibles duplicaciones no resueltas.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset / representación / validación / producto / evaluación / interfaz / secuencia | ... | ... |

### Contrato de evidencia actual

- **Notebook o código:** comportamiento que debe conservarse o hacerse visible.
- **`submission/`:** artefactos persistentes y qué evidencia contienen.
- **Pruebas:** qué verifican realmente y qué no verifican.
- **Trazabilidad:** entrada de `traceability.yaml` o su ausencia.

### Dependencias en la secuencia

- **Recibe de Pxxx:** entrada, práctica o contrato reutilizado; o «ninguna».
- **Habilita para Pyyy:** salida, práctica o contrato que una actividad
  posterior usa de forma demostrable; o «no evidenciada».

## Trazabilidad y auditoría

Entrada de `traceability.yaml` revisada, vacíos, producto de Analytics y papel
de disciplinas contribuyentes.
```

### Reglas que comprueban los scripts

1. El título es `# Pxxx — Nombre` con el `Pxxx` del archivo.
2. La ruta de **Implementación** existe y es la carpeta `Pxxx_*` del curso.
3. Los highlights se escriben `- **HNN — Título:** texto`; sus IDs son
   únicos y crecientes. Los IDs son estables: una pasada incremental no los
   renumera.
4. Al menos un highlight lleva `(caso y datos)` en su título: vincula una
   particularidad evidenciada del caso o del dataset con la práctica que
   exige. Si la implementación no revela ninguna, la ausencia se registra
   como límite y el script lo informa como advertencia.
5. Cada highlight tiene una fila en la tabla de evidencia, con al menos una
   superficie `SNN` que exista en la tabla de superficies.
6. Cada ruta entre comillas invertidas de las columnas «Rutas de respaldo»
   y «Rutas afectadas» existe, leída desde la raíz del repositorio, desde
   la carpeta de la actividad o desde la carpeta del curso; un nombre de
   archivo sin carpeta puede estar en cualquier subcarpeta de la actividad.
   Son rutas los textos que terminan en una extensión de archivo conocida o
   en `/`, o que empiezan por una subcarpeta de la actividad (`data/`,
   `professor/`, …); los nombres de funciones y métodos no.
7. No queda la sección heredada `## Mejoras aceptadas pendientes de
   implementación` con contenido; si existe vacía, se informa como
   advertencia para retirarla.

## Registro: `log.md`

El log es opcional: una actividad sin log se audita igual, y el primer
`AUD` lo crea.

```markdown
# Log — Pxxx

## S02.Pxxx.01
...
## AUD.Pxxx.01
...
## DEC.Pxxx.01
...
```

Cada prefijo numera sus entradas en orden, desde `01`:

- **`S02`**: una descripción. Fecha, curso, executor, estado (inicial o
  incremental), rutas inspeccionadas, entrada de trazabilidad revisada,
  highlights confirmados, añadidos, corregidos o no inferibles, cambios,
  ambigüedades, cambios de IDs, superficies, contrato y dependencias
  revisados, y resultado de la auditoría de Analytics.
- **`AUD`**: una auditoría frente a la cadena 02–04. La escribe
  `apply_audit.py`: fecha, executor, curso auditado, huella de la
  auditoría, entrada, decisión con su razón, resultados y competencias,
  propuestas creadas o reforzadas, señales ancladas a la actividad con su
  nivel, e hitos fuera de lo que el curso debe enseñar.
- **`DEC`**: una decisión de david sobre una propuesta `Tnn`:
  aprobada o rechazada, con la razón. Las auditorías posteriores la tratan
  como rechazo previo.

El log documenta; no resuelve orden, capacidades compartidas ni rediseño.
Nunca se editan entradas anteriores.

## Auditoría

### Lo que el curso debe enseñar

La ficha del curso en `04-curriculum/` (`postgraduate/<curso>.md` o
`undergraduate/<curso>.md`) dice qué debe aprender el estudiante. De ella
salen:

- **Resultados del curso** `<curso>/RCnn`, con su enunciado y su
  **Evaluación**. En posgrado, cada uno deriva de resultados del programa
  `RAnn`, y el nivel que el curso le debe es el mayor nivel que
  `matrix.csv` asigna al curso para esos `RA` (`introduce`, `desarrolla` o
  `domina`). En pregrado el nivel es `introduce`.
- **Ítems**: los conocimientos y habilidades de las competencias de esos
  resultados en `02-competencies/map/` (en posgrado, las competencias de
  sus `RA`). Cada uno tiene un ID `C002.CON03` (tercer conocimiento de
  `C002`) o `C002.HAB02` (segunda habilidad), en el orden del archivo de la
  competencia. La auditoría registra la fecha de cada competencia, porque
  esos números cambian si la competencia cambia.
- **Identidad**, **Conocimientos requeridos** y **Alcance** de la ficha: la
  identidad es la auditoría de `AGENTS.md` ya aplicada al curso (pregunta,
  producto terminal, disciplinas contribuyentes y riesgo); lo requerido se
  presupone y no se enseña; el alcance fija las fronteras con los demás
  cursos.

Los resultados del curso y los ítems son las **señales** de la auditoría.

### Actividades del curso

Las carpetas `Pxxx_*` de `05-implementation/<curso>/` y las actividades de
otro curso que su `traceability.yaml` cita con ruta (`descriptiva/P103`).
Una actividad citada de otro curso se describe y se cambia en su curso
dueño: su descripción, su log y sus propuestas puntuales viven allí, con la
fuente que dice qué curso las pidió.

`P001` y los laboratorios `Lxxx` no se auditan aquí; sus entradas de
trazabilidad se conservan.

### Categorías de una señal

Cada señal recibe una sola categoría:

| Categoría | Requiere |
|---|---|
| `cubierta` | anclas a highlights existentes que alcanzan el nivel que el curso debe |
| `marginal` | razón: no pasa el criterio de materialidad |
| `rechazada previamente` | razón con la entrada `DEC` o la propuesta rechazada |
| `fuera de alcance` | razón: desplaza la identidad de Analytics, corresponde a otro curso o carece de caso y datos |
| `mejora` | actividad y propuesta puntual nueva o abierta |
| `actividad nueva` | decisión de curso nueva o abierta |

Un ancla es un highlight con el nivel al que trabaja la señal:
`{"hito": "P103:H01", "nivel": "introduce"}`. Una señal de cualquier
categoría puede llevar anclas para registrar una cobertura parcial; una
`cubierta` las exige, y si es un resultado del curso, alguna debe llegar al
nivel que el curso le debe.

### Hitos fuera de lo que el curso debe enseñar

Todo highlight de una actividad del curso queda anclado por alguna señal o
se declara **fuera**: no sirve a ningún resultado ni ítem del curso, por
ejemplo una profundidad de la disciplina contribuyente que el curso no
necesita, o un conocimiento requerido que se vuelve a enseñar. Se
**conserva** si sostiene técnicamente el producto, con su razón, o se
**recorta** con una propuesta puntual o de curso. Es aquí donde se protege
la identidad: lo que sobra es lo que acerca el curso a la versión abreviada
de una disciplina que su ficha nombra como riesgo.

### Decisión por actividad

| Decisión | Significado | Salida |
|---|---|---|
| `igual` | (a) Queda igual. | Ninguna propuesta. |
| `puntual` | (b) Un cambio puntual que refuerza su contribución sin alargarla. | Una `Tnn` nueva como máximo, o el refuerzo de propuestas abiertas. |
| `curso` | (c) Lo que falta no cabe sin una segunda contribución o sin alargarla, o la actividad no sirve a ningún resultado del curso. | Una decisión de curso `Nnn` nueva o abierta. |

Una actividad sin resultados del curso sólo admite la decisión `curso`. Se
avisa cuando una actividad acumula más de tres propuestas abiertas.

### `Pxxx_<nombre>/tasks.md` — cambios puntuales de una actividad

Dice exactamente qué cambiar en la actividad y por qué. Estado actual, no
historial. Una propuesta decidida conserva su entrada con
su estado hasta ejecutarse; una rechazada sale del archivo y queda en el
log como `DEC`, de modo que su ID no se reutiliza y las auditorías la ven.

````markdown
# Pxxx — Propuestas de mejora

**Línea base:** `activity.md` (entrada S02 más reciente: `S02.Pxxx.NN`, si hay log).

## T01 — Título preciso del cambio

- **Estado:** pendiente de discusión | aprobada | rechazada
- **Tipo:** encuadre | producto/evidencia | método | caso/datos | proceso | pedagogía
- **Fuentes:**
  - Auditoría `AUD.Pxxx.NN` (executor, fecha) del curso `descriptiva`: señales `descriptiva/RC02`, `C002.HAB03`.
- **Qué gana el estudiante:** la capacidad o comprensión nueva, o el defecto
  que se corrige.
- **Anclas actuales:** `HNN`, `SNN` afectados.
- **Alternativas menores descartadas:** por qué aclarar o extender no basta.
- **Contrato de no regresión:** lo que se conserva y las sustituciones.
- **Límite de la actividad:** por qué sigue siendo un problema corto y bien
  definido después del cambio.
- **Interacciones:** con otras `Txx` de este archivo.
- **Justificación metodológica:** qué principio del método analítico
  exige el cambio.
- **Justificación técnica:** qué práctica técnica corrige o agrega, y por
  qué es la adecuada.
- **Justificación pedagógica:** cómo mejora lo que el estudiante aprende en
  la secuencia.
- **Identidad del curso:** cómo el cambio sirve al producto terminal de la
  ficha y evita el riesgo que la ficha nombra.
- **Criterio de aceptación:** lo que debe verificarse después.

### Instrucciones de ejecución

Prompt autocontenido: rutas a inspeccionar y modificar (de las `SNN`),
pasos, qué no tocar, qué pruebas o artefactos actualizar, cómo comprobar
el criterio de aceptación, y la orden de detenerse si la implementación
contradice la descripción.
````

Los IDs `T01`, `T02`… son estables dentro del archivo y no se reutilizan.
Las entradas anteriores a esta versión citan benchmarks en **Fuentes** y no
tienen **Límite de la actividad**; se conservan.

### `tasks.md` del curso — actividades nuevas y reorganizaciones

Describe en detalle cada actividad que hay que crear y cada reorganización
de la secuencia.

````markdown
# <curso> — Actividades nuevas por decidir

## N01 — ⚠️ PENDIENTE DE DECISIÓN — Nombre tentativo

- **Estado:** pendiente de discusión | aprobada | rechazada
- **Tipo:** actividad nueva | reorganización
- **Fuentes:**
  - Auditoría del curso `descriptiva` (executor, fecha): señales `descriptiva/RC04`, `C004.HAB01`; decisión de `P121`.
- **Contribución distinta:** qué enseñaría o resolvería que ninguna Pxxx
  resuelve, y por qué no cabe en una existente sin alargarla.
- **Posición propuesta:** después de Pxxx; qué recibe y qué habilita.
- **Desplaza o fusiona:** qué actividad se desplaza, se fusiona o se
  recorta para hacerle lugar en las sesiones del curso, o «ninguna» y por
  qué cabe.
- **Efecto en la secuencia:** qué perdería un grupo que avanza menos.
- **Caso y datos:** condición concreta que exige, o «requiere definición».
- **Producto de Analytics:** pregunta, producto terminal y límite.
- **Justificación metodológica:** …
- **Justificación técnica:** …
- **Justificación pedagógica:** …
- **Identidad del curso:** …
- **Criterio de aceptación de una primera versión:** …
````

Una `reorganización` decide sobre actividades existentes: conservar,
combinar, mover o reemplazar. Una decisión de curso rechazada se conserva
con estado `rechazada` y su razón, porque no hay log de curso. Una entrada
sin **Estado** se lee como pendiente.

### `audit.md` — cobertura vigente

Lo reescribe `apply_audit.py` en cada auditoría: fecha, executor, huella,
entrada (ficha del curso y fecha de cada competencia), decisión por
actividad, la tabla de señales con su nivel debido, su categoría y sus
anclas con nivel, su propuesta o su razón, y la tabla de hitos fuera de lo
que el curso debe enseñar.

### `traceability.yaml`

```yaml
format_version: "0.1"
P103:
  resultados: [descriptiva/RC02]
  competencias: [C002, C003]
  decision: puntual
  auditoria: AUD.P103.01
descriptiva/P100:
  resultados: [fundamentos/RC01]
  competencias: [C002]
  decision: igual
  auditoria: AUD.P100.02
L101:
  - descriptiva.C02
```

- Las entradas auditadas tienen los cuatro campos, en ese orden. Los
  resultados se citan como resultados del curso, `<curso>/RCnn`, en
  posgrado y en pregrado.
  Las competencias se citan `Cnnn`, siempre con tres dígitos y sin curso.
- Las capacidades anteriores `<curso>.Cnn` (dos dígitos, con curso) nunca
  se mezclan con las competencias: sólo aparecen en entradas heredadas, en
  forma de lista, que la auditoría no reescribe (`P001`, `Lxxx` y las
  actividades aún no auditadas). El script las conserva y las informa.
- `competencias` es un subconjunto de las competencias de los
  `resultados`.

## Versión y cambios

- 0.1 (2026-10-14): borrador inicial. Une el contrato de la tarea S02
  (describir un curso) y las salidas de la tarea S03 (revisar contra
  benchmarks), con la entrada de la
  auditoría cambiada de benchmarks a las fichas de `04-curriculum/` y los
  archivos junto a la implementación. Valores por defecto que david debe aprobar: el
  marcador `(caso y datos)`; los IDs de ítem `CON`/`HAB`; las decisiones
  `igual`, `puntual` y `curso`; una sola propuesta nueva por actividad y
  auditoría; el aviso con más de tres propuestas abiertas; que las
  decisiones de curso rechazadas queden en el `tasks.md` del curso;
  `audit.md`; la prohibición de proponer celdas markdown; el nivel debido de un resultado del curso como el mayor de
  sus `RA` en la matriz; el esquema de `traceability.yaml`; que `P001` y `Lxxx` queden fuera de la auditoría.
