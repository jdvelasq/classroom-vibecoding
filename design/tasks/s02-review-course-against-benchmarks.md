# S02 — Evaluar un curso frente a evidencia de benchmarks

## Ejecución

```text
execute design/tasks/s02-review-course-against-benchmarks.md \
  course=<curso> benchmark=<ruta-o-all> executor=<LLM>
```

`course` identifica `design/courses/<curso>/`. `benchmark` es una ruta local
relativa a `design/benchmarks/` o `all`. `executor` identifica una lectura
independiente; no autoriza a usar el resultado de otro modelo como evidencia ni
a sobrescribirlo.

## Propósito y límite

Esta tarea contrasta el diseño actualmente descrito por S01 con uno o varios
documentos locales de `design/benchmarks/`. Produce un **informe de propuestas
candidatas**, no modifica actividades, implementación ni trazabilidad. Su
pregunta es:

> ¿La nueva evidencia justifica conservar, aclarar, reforzar, contrastar,
> secuenciar de otro modo o proponer un cambio en alguna actividad existente?

La ausencia de un elemento en un benchmark no demuestra una brecha del curso;
la aparición de una técnica tampoco justifica enseñarla. Las mejoras llegan a
una actividad sólo mediante una decisión posterior, explícita y registrada.

## Principio de cambio mínimo

La implementación actual es una base construida que funciona. Por tanto, **el
menor cambio que resuelva una necesidad evidenciada es el mejor cambio**. S02
parte de conservar caso, secuencia, prácticas, entregables y pruebas actuales.

Antes de proponer una modificación, compara explícitamente estas alternativas,
en este orden:

1. no cambiar: la actividad ya cubre la señal con evidencia suficiente;
2. aclarar o hacer visible: mejorar explicación, visualización, artefacto,
   prueba o trazabilidad sin alterar la experiencia central;
3. extender localmente: añadir una práctica o contraste pequeño que preserve
   el caso, producto y contratos existentes; y
4. cambiar de forma material: sustituir caso, método, producto, orden o
   actividad sólo si las alternativas anteriores no resuelven el beneficio.

La carga de la prueba crece en ese orden. Una propuesta no es aceptable si no
explica por qué una alternativa de menor impacto es insuficiente. Novedad,
prestigio de la fuente, cobertura de una técnica o preferencia de herramienta
no son por sí mismos razones para ampliar o reemplazar el diseño.

## Entradas permitidas

Lee y cumple `AGENTS.md`. Lee sustantivamente:

- el o los PDFs seleccionados bajo `design/benchmarks/`;
- `design/courses/<curso>/Pxxx_activity.md` y `Pxxx_log.md`; y
- `design/courses/<curso>/course_log.md` sólo si existe, para contexto.

No lees ni modificas `implementation/<curso>/`, otros cursos, informes de
otros executors, síntesis S03/S04/S05, plataformas de aprendizaje ni web. S01
es la lectura auditable de la implementación para este propósito.

Si falta un mapa S01 pertinente, registra el límite: no inventes highlights,
superficies ni contenido implementado para poder emitir una propuesta.

## Función de las familias de evidencia

Clasifica cada fuente y restringe su inferencia:

- **authoritative:** principios, estándares o marcos durables; puede respaldar
  expectativas generales, no copiar un syllabus.
- **institutional:** oferta, articulación, coherencia o forma de operacionalizar
  una institución; ilustra posibilidades, no impone identidad curricular.
- **governmental:** pertinencia externa, entorno laboral o política pública; no
  define un estándar internacional ni prescribe herramientas.
- **professional-learning:** señales de actualización y práctica de plataformas;
  no reemplaza la evidencia curricular o disciplinar.
- **literature-derived:** perspectiva histórica, metodológica, organizacional o
  conceptual; exige distinguir contexto de prescripción vigente.

Analytics conserva la identidad curricular. Machine Learning, Estadística,
Data Science, Data Mining, KDD, OR/optimización, Data Engineering, BI, IA y
otras disciplinas son contribuyentes. Aplica las preguntas de auditoría de
`AGENTS.md` a cada propuesta material.

## Método

1. Declara rutas, páginas o secciones relevantes, familia de evidencia y límite
   de inferencia. Con `benchmark=all`, cuenta y lista todos los PDFs leídos.
2. Extrae sólo señales accionables: caso/dataset, representación, técnica,
   validación, métrica, entrega persistente, práctica de código, uso operativo,
   producto o guardrail. Distingue lo que el documento afirma de la inferencia.
3. Busca primero anclas existentes en el **índice de comparación externa** de
   S01. Vincula después `HNN` y `SNN` de la actividad. No uses un título de
   taller como sustituto de evidencia.
4. Para cada señal, elige un dictamen:
   - **ya cubierto:** se conserva; explica por qué no exige cambio;
   - **aclaración verificable:** el contenido existe, pero su evidencia,
     explicación, artefacto o prueba debe hacerse visible;
   - **candidato a cambio:** hay una mejora delimitada y una actividad con
     ancla/superficie para recibirla;
   - **no sustentado / fuera de alcance:** no se propone cambio; explica el
     límite, tensión o riesgo de sustitución disciplinar.
5. Para cada candidato, formula un contrato de cambio: pregunta o producto
   analítico que mejoraría; Pxxx/HNN/SNN afectados; cambio mínimo; caso/dataset
   apropiado; práctica concreta; evidencia persistente esperada; prueba y
   trazabilidad que habría que revisar; dependencias, riesgos y condición de
   aceptación.
6. Justifica por qué el cambio propuesto es el menor suficiente: enumera las
   alternativas de menor impacto consideradas y la evidencia de que no bastan.
7. Explicita tensiones. Una técnica más reciente o frecuente no desplaza una
   línea base interpretable, un caso con valor pedagógico o un producto de
   Analytics sin una razón observable.
8. No aceptes, implementes ni copies propuestas en `Pxxx_activity.md`.

## Salida

Para una ruta única, deriva `<fuente>` del nombre del archivo sin extensión. Para
`all`, usa `all`. Crea exactamente:

`design/courses/<curso>/benchmark_reviews/<fuente>-<executor>.md`

No sobrescribas el informe de otro executor. Una ejecución incremental del
mismo executor lee sólo su informe anterior correspondiente, conserva hallazgos
vigentes y registra qué PDFs o conclusiones cambiaron.

```markdown
# S02 — Revisión de <curso> contra <fuente> (<executor>)

## Inventario y función de la evidencia

| Ruta | Familia | Páginas/secciones leídas | Qué puede sustentar | Límite |
| --- | --- | --- | --- | --- |

## Señales extraídas

| ID | Afirmación del documento | Inferencia permitida | Página/sección |
| --- | --- | --- | --- |

## Contraste con el diseño actual

| Señal | Pxxx | Ancla S01 | Hitos | Superficies | Dictamen | Razón |
| --- | --- | --- | --- | --- | --- |

## Propuestas candidatas — no aceptadas

### C01 — Título preciso

- **Evidencia externa:** ruta y página/sección.
- **Actividad y contrato actual:** Pxxx, ancla, HNN y SNN.
- **Cambio mínimo propuesto:** qué variaría y qué debe conservarse.
- **Alternativas de menor impacto descartadas:** no cambiar, aclarar o extender;
  por qué no bastan, con evidencia.
- **Producto de Analytics y decisión/usuario:** beneficio verificable o
  «requiere definición».
- **Caso, datos y práctica de implementación:** condición concreta; no un tema
  genérico.
- **Evidencia de aceptación futura:** artefacto persistente, visualización,
  prueba y trazabilidad que deberían cambiar.
- **Secuencia, riesgos y tensiones:** dependencias, sustitución disciplinar,
  costo, procedencia, sesgo, validez o límites.
- **Condición para aceptar:** evidencia adicional o decisión institucional
  necesaria.

## Señales ya cubiertas o descartadas

## Auditoría de identidad de Analytics

## Registro incremental
```

Si no hay un candidato sustentado, conserva las secciones y declara «ninguno».
Ése es un resultado válido.

## Control antes de guardar

Confirma que:

- se leyeron los PDFs locales declarados y se citan por ruta y página/sección;
- cada candidato está anclado a una actividad mapeada, `HNN` y `SNN`, o se
  declara explícitamente que el mapeo falta;
- cada propuesta especifica cambio, evidencia futura y condición de aceptación;
- cada candidato demuestra que no existe una alternativa de menor impacto que
  produzca el mismo beneficio verificable;
- los dictámenes de cobertura no se confunden con aceptación de cambios;
- se preservó la identidad de Analytics y se registraron tensiones; y
- sólo se creó o actualizó el informe S02 del executor actual.
