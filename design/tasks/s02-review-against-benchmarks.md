# S02 — Evaluar un curso frente a evidencia de benchmarks

## Ejecución

```text
execute design/tasks/s02-review-against-benchmarks.md \
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
> secuenciar de otro modo, cambiar una actividad o agregar una nueva?

La ausencia de un elemento en un benchmark no demuestra una brecha del curso;
la aparición de una técnica tampoco justifica enseñarla. Las mejoras llegan a
una actividad sólo mediante una decisión posterior, explícita y registrada.

## Principio de cambio mínimo

La implementación actual es una base construida que funciona. Por tanto, **el
menor cambio que resuelva una necesidad evidenciada sin producir regresiones es
el mejor cambio**. S02 parte de conservar caso, secuencia, prácticas,
entregables y pruebas actuales.

Antes de proponer una modificación, compara explícitamente estas alternativas,
en este orden:

1. no cambiar: la actividad ya cubre la señal con evidencia suficiente;
2. aclarar o hacer visible: mejorar explicación, visualización, artefacto,
   prueba o trazabilidad sin alterar la experiencia central;
3. extender localmente: añadir una práctica o contraste pequeño que preserve
   el caso, producto y contratos existentes; y
4. cambiar de forma material: sustituir caso, método, producto, orden o
   actividad cuando el beneficio evidenciado lo exige; o
5. agregar una actividad: cuando falta una contribución distinguible que no
   debe sobrecargar, desdibujar o degradar las actividades existentes.

La carga de justificación crece en ese orden. Un cambio mayor o una actividad
nueva son válidos cuando su necesidad, contribución y posición en la secuencia
son claras. Pero deben declarar un **contrato de no regresión**: qué highlights,
productos, prácticas, datos, evidencia, pruebas y dependencias actuales se
preservan, y qué se reemplaza explícitamente con evidencia al menos equivalente.
No basta con que lo nuevo parezca mejor; no puede perderse silenciosamente lo
que ya aporta valor. Novedad, prestigio de la fuente, cobertura de una técnica
o preferencia de herramienta no son por sí mismos razones para ampliar o
reemplazar el diseño.

## Entradas permitidas

Lee y cumple `AGENTS.md`. Lee sustantivamente:

- el o los PDFs seleccionados bajo `design/benchmarks/`;
- `design/courses/<curso>/Pxxx_activity.md` y `Pxxx_log.md`; y
- `design/courses/<curso>/course_log.md` sólo si existe, para contexto.

Cuando un PDF tenga tabla de contenido, índice, taxonomía o lista sustantiva de
capacidades, léela además de las secciones pertinentes. Es un inventario para
auditar cobertura; no un syllabus que deba copiarse.

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
   Cuando el documento proponga aplicaciones o casos, registra también la
   pregunta organizacional, entidad/unidad, horizonte, resultado a estimar,
   decisión o usuario mencionado y contexto de error o riesgo.
3. Para cada caso o aplicación del benchmark, pregunta explícitamente: «¿aporta
   una contribución predictiva que el curso no trata?». Compárala contra los
   `Pxxx_activity.md`, no contra el nombre del taller. Distingue: (a) un ejemplo
   que ya ilustra una actividad existente; (b) un nuevo encuadre para el mismo
   producto; (c) una variación que añade datos, representación, horizonte,
   métrica, error, guardrail o producto terminal distinguible; y (d) un caso que
   no puede proponerse porque el documento no aporta datos locales, procedencia
   o una necesidad curricular. Una aplicación sectorial no basta: no atribuyas
   esa industria al dataset actual ni inventes un caso.
4. Para cada capacidad conceptual o técnica sustantiva que el referente
   enumere —por ejemplo, detección de outliers, itemsets, clustering,
   preparación, selección de variables, validación, persistencia o
   interpretación— pregunta explícitamente: «¿dónde la practica y evidencia el
   estudiante en este curso?». Un contenido de un referente reconocido tiene
   **presunción de revisión obligatoria**, no presunción automática de
   incorporación. Registra su ancla `Pxxx`/`HNN`/`SNN` o el motivo de ausencia.
   Distingue entre conocer el nombre de una técnica, usar una función de una
   librería y demostrar una capacidad mediante datos, código, producto
   persistente y prueba.
5. Para cada capacidad auditada, clasifica el resultado como:
   - **cubierta:** la actividad ya contiene práctica y evidencia suficientes;
   - **cubierta parcialmente:** existe una mención o uso aislado, pero falta
     pregunta, representación, comparación, visualización, artefacto, prueba o
     límite de interpretación;
   - **candidata a extensión:** puede incorporarse preservando pregunta,
     unidad, caso, producto y contrato de la actividad actual;
   - **candidata estructural:** exige unidad, representación, horizonte,
     métrica, contexto de error, producto o evidencia distinguible, por lo que
     requiere cambio material o actividad nueva; o
   - **fuera de alcance / no sustentada:** su incorporación desplazaría la
     identidad de Analytics, duplicaría una contribución existente o carece de
     caso/dato/procedencia que permita enseñarla con rigor.

   Una técnica adicional dentro de una actividad existente sólo es proporcional
   si fortalece un `HNN` o una `SNN` actuales y puede compararse con lo ya
   aprendido sobre el mismo problema. Propón una actividad nueva cuando la
   capacidad requiera una pregunta, unidad de análisis, representación,
   validación, tipo de error o producto terminal propio que diluiría la
   contribución de la actividad existente.
6. Audita también la práctica de implementación revelada por cada caso o
   capacidad: transformación de datos, contrato de entrada, patrón de Python o
   SQL, visualización, prueba, persistencia, reuso, interoperabilidad o límite
   operacional. Una característica de herramienta sólo justifica cambio si
   resuelve una dificultad real del dato o producto y deja una práctica
   transferible y verificable; una llamada nueva de biblioteca no es, por sí
   sola, una capacidad curricular.
7. Busca primero anclas existentes en el **índice de comparación externa** de
   S01. Vincula después `HNN` y `SNN` de la actividad. No uses un título de
   taller como sustituto de evidencia.
8. Para cada señal, elige un dictamen:
   - **ya cubierto:** se conserva; explica por qué no exige cambio;
   - **aclaración verificable:** el contenido existe, pero su evidencia,
     explicación, artefacto o prueba debe hacerse visible;
   - **candidato a cambio:** hay una mejora delimitada y una actividad con
     ancla/superficie para recibirla;
   - **candidato estructural:** un cambio mayor o una actividad nueva tiene una
     contribución propia y un contrato de no regresión verificable; o
   - **no sustentado / fuera de alcance:** no se propone cambio; explica el
     límite, tensión o riesgo de sustitución disciplinar.
9. Antes de detallar candidatos, produce los **hallazgos prioritarios de
   faltantes**: sólo las capacidades, casos, prácticas o evidencias que el
   contraste demuestra ausentes o cubiertas parcialmente. Para cada uno, indica
   por qué importa para el producto de Analytics, qué `Pxxx` no lo cubre o lo
   cubre parcialmente, el candidato asociado y la siguiente decisión o
   evidencia necesaria. Ordénalos por impacto curricular y certeza de la
   evidencia. No repitas capacidades ya cubiertas ni presentes una lista de
   técnicas del referente: ésta es la respuesta ejecutiva a «¿qué falta?».
10. Para cada candidato, formula un contrato de cambio: pregunta o producto
   analítico que mejoraría; Pxxx/HNN/SNN afectados o posición propuesta para una
   actividad nueva; caso/dataset apropiado; práctica concreta; evidencia
   persistente esperada; prueba y trazabilidad que habría que revisar;
   dependencias, riesgos y condición de aceptación.
11. Justifica la proporcionalidad: enumera las alternativas de menor impacto
   consideradas y explica por qué bastan o no bastan. Para un cambio mayor o una
   actividad nueva, demuestra además su contribución no duplicada y el contrato
   de no regresión.
12. Explicita el contrato de no regresión: lista los HNN, SNN, artefactos y
   dependencias que se conservan, y cada elemento que se sustituye junto con la
   evidencia que verificará una contribución al menos equivalente.
13. Explicita tensiones. Una técnica más reciente o frecuente no desplaza una
   línea base interpretable, un caso con valor pedagógico o un producto de
   Analytics sin una razón observable.
14. No aceptes, implementes ni copies propuestas en `Pxxx_activity.md`.

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

## Cobertura de casos y contribuciones predictivas

| Caso/aplicación del benchmark | Pregunta, unidad, horizonte y resultado | Pxxx/HNN/SNN comparados | ¿Qué aporta que no exista? | Dictamen y evidencia adicional necesaria |
| --- | --- | --- | --- | --- |

## Cobertura conceptual y técnica del referente

| Capacidad del índice o sección | Rol para Analytics y práctica técnica asociada | Pxxx/HNN/SNN comparados | Cobertura actual verificable | Dictamen y siguiente evidencia necesaria |
| --- | --- | --- | --- | --- |

## Hallazgos prioritarios de faltantes

| Prioridad | Falta demostrada | Por qué importa para Analytics | Pxxx/HNN/SNN relacionados | Candidato y siguiente decisión/evidencia |
| --- | --- | --- | --- | --- |

## Propuestas candidatas — no aceptadas

### C01 — Título preciso

- **Evidencia externa:** ruta y página/sección.
- **Actividad, posición y contrato actual:** Pxxx, ancla, HNN y SNN; o posición
  propuesta y actividades contiguas si se propone una nueva actividad.
- **Tipo y alcance:** aclaración, extensión, cambio material o actividad nueva.
- **Cambio propuesto:** qué variaría, agregaría o reemplazaría.
- **Alternativas de menor impacto descartadas:** no cambiar, aclarar o extender;
  por qué no bastan, con evidencia.
- **Contrato de no regresión:** HNN, SNN, artefactos, pruebas y dependencias que
  se conservan; equivalencia verificable de todo elemento reemplazado.
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
- cada candidato está anclado a una actividad mapeada, `HNN` y `SNN`, o, para
  una actividad nueva, declara su posición, contribución no duplicada y las
  actividades contiguas afectadas;
- cada propuesta especifica cambio, evidencia futura y condición de aceptación;
- cada candidato demuestra que no existe una alternativa de menor impacto que
  produzca el mismo beneficio verificable;
- cada cambio mayor o actividad nueva tiene un contrato de no regresión que
  preserva o sustituye explícitamente las contribuciones actuales;
- los dictámenes de cobertura no se confunden con aceptación de cambios;
- cada aplicación o caso del benchmark se contrastó explícitamente con la
  cobertura actual y, cuando se propone una actividad nueva, se demostró su
  producto, contribución no duplicada, posición y evidencia local pendiente;
- cuando el referente contiene un índice o tabla de contenido sustantiva, cada
  capacidad relevante recibió un dictamen explícito de cobertura conceptual y
  técnica; la mera presencia de una técnica en el índice no se confundió con su
  adopción automática;
- cada candidata a herramienta o técnica demuestra qué dificultad de datos o
  producto resuelve, cuál práctica transferible deja y por qué es una extensión
  o una actividad nueva en vez de una llamada adicional de biblioteca;
- el informe presenta una sección breve, priorizada y separada que responde
  explícitamente «qué falta», sin confundir cobertura existente, candidatos no
  aceptados y cambios implementados;
- se preservó la identidad de Analytics y se registraron tensiones; y
- sólo se creó o actualizó el informe S02 del executor actual.
