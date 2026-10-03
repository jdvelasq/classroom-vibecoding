# S01 — Mapear las actividades implementadas de un curso

## Ejecución

Ejecuta esta tarea como:

```text
execute design/tasks/s01-map-course-activities.md course=<curso> executor=<LLM>
```

`course` identifica el directorio existente `implementation/<curso>/` y el
directorio de diseño `design/courses/<curso>/`. `executor` identifica el LLM o
entorno que realizó esta pasada y se registra únicamente para auditoría: el
contrato, las entradas y los controles son independientes del modelo usado.

## Propósito

Mapear fielmente cada actividad presencial `Pxxx_` ya implementada en
`implementation/<curso>/` a dos archivos de diseño:

- `design/courses/<curso>/Pxxx_activity.md`; y
- `design/courses/<curso>/Pxxx_log.md`.

La actividad implementada es la línea base. Esta tarea documenta lo que existe
hoy y puede mejorar la precisión, integridad o trazabilidad de su descripción
mediante una nueva lectura independiente de la implementación. No rediseña la
actividad, no añade mejoras curriculares y no modifica `implementation/`.

Una futura tarea de exploración externa podrá acumular mejoras ya aceptadas en
`Pxxx_activity.md`. S01 debe preservarlas si existen, pero no crearlas,
aceptarlas, rechazarlas ni modificarlas.

## Entradas obligatorias

Lee y cumple `AGENTS.md`. Para el curso indicado, inspecciona:

- `implementation/<curso>/traceability.yaml`;
- cada directorio `implementation/<curso>/Pxxx_*/`;
- datos, manifiestos y documentación de procedencia disponibles;
- notebooks, código, preguntas, material de profesor y archivos de
  `submission/`;
- pruebas de la actividad; y
- los archivos existentes bajo `design/courses/<curso>/` para la actividad
  correspondiente.

Lee `design/courses/<curso>/course_log.md`, si existe, únicamente para entender
decisiones transversales. No lo modifiques en S01.

No hagas investigación web. No modifiques archivos bajo `implementation/`, ni
actividades de otro curso, ni `course_log.md`.

## Dos estados de trabajo

### Estado inicial

Si `Pxxx_activity.md` no existe o está vacío, crea una primera descripción del
estado implementado y crea `Pxxx_log.md`. La descripción debe basarse en los
artefactos reales, no en nombres de directorios ni en inferencias sobre lo que
un curso “normalmente” debería enseñar.

### Estado incremental

Si `Pxxx_activity.md` ya existe, el executor debe volver a leer la
implementación de manera independiente y contrastarla con el mapa existente y
con `Pxxx_log.md`. Conserva las afirmaciones todavía sustentadas; completa,
corrige o precisa sólo aquello que pueda justificar con una ruta concreta de
implementación. No reescribas por estilo ni elimines una interpretación previa
sin dejar la razón en el log.

Las diferencias entre executors se tratan como evidencia auditable. Si la
implementación no permite resolver una diferencia, regístrala como ambigüedad
en vez de fabricar consenso.

## Protocolo por actividad

Procesa todas las actividades `Pxxx_` encontradas, en orden numérico. La
numeración existente define la secuencia; S01 no crea, elimina, renumera,
fusiona ni divide actividades.

Para cada actividad:

1. **Inventaria** los artefactos disponibles y separa material de estudiante,
   material de profesor, datos de entrada, código/notebooks, entregables y
   pruebas.
2. **Reconstruye el caso actual**: preguntas analíticas como una lista de
   viñetas, contexto, usuario o decisión sólo si están evidenciados; unidad de
   análisis, tiempo, entidades, transformaciones y limitaciones de los datos.
   No fusiona preguntas distintas en una formulación genérica.
3. **Reconstruye la experiencia observada** desde instrucciones, notebooks,
   código, entregables y pruebas. Distingue evidencia explícita, estructura
   observable e inferencia.
4. **Mapea evidencia de aprendizaje diseñada**, no logro real del estudiante:
   relaciona prácticas, técnicas y capacidades que la actividad ejercita con
   los entregables, las pruebas y la entrada de `traceability.yaml`.
5. **Inventaría la implementación técnica** que la actividad realmente
   ejercita: propiedades de datos, operaciones concretas, funciones o APIs,
   patrones de código, validaciones, pruebas, contratos, reproducibilidad,
   entrega u operación. Clasifica cada elemento como introducido, reutilizado,
   extendido o aplicado a un nuevo caso frente a actividades `Pxxx` anteriores.
   No confundas una biblioteca importada con una práctica ejercitada.
6. **Compara valor curricular.** Una pregunta de negocio repetida no convierte
   automáticamente una actividad en redundante. Identifica qué habilidad
   analítica o de implementación se perdería si se eliminara la actividad; si
   no hay una diferencia sustentada, regístrala como posible duplicación para
   revisión de curso.
7. **Audita la identidad de Analytics** usando `AGENTS.md`: identifica el
   producto analítico y la función de disciplinas contribuyentes sin convertir
   la actividad en una clase abreviada de una de ellas.
8. **Actualiza de forma atómica** primero `Pxxx_activity.md` y después agrega
   una entrada a `Pxxx_log.md`, incluso cuando la revisión confirme que no hay
   nada que corregir.

## Contrato de `Pxxx_activity.md`

El archivo describe el estado vigente de diseño de una actividad y separa con
claridad dos capas:

1. **Actividad actual implementada.** Identificador y ruta; propósito
   observado; preguntas analíticas en una lista de viñetas; caso; datos y
   procedencia disponible; experiencia de aula
   invertida evidenciada; técnicas y herramientas realmente ejercitadas;
   productos/entregables; evidencia de aprendizaje diseñada; límites y
   ambigüedades.
2. **Mejoras aceptadas pendientes de implementación.** Conserva, sin
   alterarlas, las mejoras aprobadas por tareas posteriores. Cada mejora debe
   indicar el cambio frente a la actividad actual y su estado. Si no existen,
   declara explícitamente que no hay mejoras aceptadas pendientes.

Incluye además:

- capacidades y habilidades que la actividad está diseñada para hacer
  observables, nunca una afirmación no evidenciada de logro estudiantil;
- un **inventario técnico de implementación** en viñetas: datos y sus
  propiedades relevantes; operaciones, funciones, consultas o APIs realmente
  ejercitadas; patrones de código; y prácticas de calidad, prueba, entrega u
  operación. Cada elemento identifica su rol como introducido, reutilizado,
  extendido o aplicado a un caso nuevo;
- una **relación técnica con actividades anteriores**: qué se repite, qué se
  añade, qué se extiende y qué habilidad observable se perdería al eliminar la
  actividad. Una repetición sin diferencia sustentada se marca como posible
  duplicación, no se resuelve localmente;
- la relación revisada con la entrada aplicable de `traceability.yaml`;
- una tabla de trazabilidad: afirmación → ruta(s) de implementación → tipo de
  evidencia → límite; y
- la auditoría de identidad de Analytics de `AGENTS.md`.

No uses este archivo como historial de decisiones ni como lista de mejoras
posibles no aceptadas.

## Contrato de `Pxxx_log.md`

El log es acumulativo. Cada ejecución añade una entrada `S01.Pxxx.NN` con:

- fecha, `course` y `executor`;
- estado abordado: inicial o incremental;
- rutas inspeccionadas y entrada revisada de `traceability.yaml`;
- afirmaciones confirmadas, añadidas, corregidas o cuestionadas;
- cambios concretos en la descripción de la actividad actual, o la razón de
  no cambiarlos;
- mejoras aceptadas pendientes que fueron preservadas sin modificación;
- inventario técnico y comparación con actividades previas revisados;
- ambigüedades, vacíos y posibles escalaciones de curso; y
- resultado de la auditoría de identidad de Analytics.

S01 registra en el log, pero no resuelve, cualquier problema que afecte orden
`Pxxx`, identificación, asignación de capacidades entre actividades o más de
una actividad. Esos cambios pertenecen a una tarea posterior de curso y a
`course_log.md`.

## Controles antes de guardar

Confirma que:

- se procesó cada directorio `Pxxx_` del curso, en orden numérico;
- se inspeccionó contenido sustantivo de la implementación, no sólo nombres;
- toda afirmación importante tiene una ruta de respaldo;
- se revisó la entrada correspondiente de `traceability.yaml`;
- no se inventaron caso, dataset, técnica, producto, competencia ni logro de
  aprendizaje;
- se conservaron sin modificación las mejoras aceptadas pendientes;
- sólo se modificaron `Pxxx_activity.md` y `Pxxx_log.md` del curso objetivo,
  salvo crear `design/courses/<curso>/` si faltaba; y
- los logs permiten a otro LLM repetir la inspección y aportar una lectura
  independiente.

## Condición de finalización

S01 termina cuando cada actividad `Pxxx_` de `implementation/<curso>/` tiene
su par `Pxxx_activity.md` y `Pxxx_log.md`, ambos consistentes con la
implementación existente y preparados para que futuras tareas acumulen mejoras
aceptadas antes de una fase posterior de implementación integrada.
