# S01 — Describir y auditar las actividades implementadas de un curso

## Ejecución

```text
execute design/tasks/s01-describe-course.md course=<curso> executor=<LLM>
```

`course` identifica `implementation/<curso>/` y `design/courses/<curso>/`.
`executor` identifica la lectura independiente que realizó el trabajo; no cambia
el contrato de la tarea ni autoriza a inventar consenso entre modelos.

## Resultado que debe producir

Para cada directorio `implementation/<curso>/Pxxx_*/`, en orden numérico,
mantiene estos dos archivos:

- `design/courses/<curso>/Pxxx_activity.md`: descripción vigente, basada sólo
  en implementación observable; y
- `design/courses/<curso>/Pxxx_log.md`: registro acumulativo de la inspección y
  sus decisiones de descripción.

La actividad implementada es la línea base. S01 **describe y audita**; no
rediseña, no acepta mejoras curriculares, no hace investigación web y no
modifica `implementation/`. Si existen «Mejoras aceptadas pendientes de
implementación» en una actividad, las preserva literalmente.

## Principio rector: contribución, no inventario

El resultado debe permitir decidir posteriormente si conservar, mejorar,
combinar o reemplazar un taller al contrastarlo con benchmarks o nueva
información. Para lograrlo, cada actividad debe responder con evidencia:

> ¿Qué capacidad concreta se empieza a ejercer, se extiende, se contrasta o se
> aplica de una forma nueva aquí, y qué se perdería de la secuencia si este
> taller no existiera?

No basta con decir «usa Python», «enseña regresión», «incluye un notebook» o
nombrar una biblioteca. Tampoco basta con repetir la pregunta de negocio. La
contribución se expresa mediante **highlights**, separados del inventario de
técnicas.

## Entradas que se deben inspeccionar

Lee y cumple `AGENTS.md`. Para cada Pxxx, inspecciona contenido sustantivo de:

- `implementation/<curso>/traceability.yaml`;
- datos, manifiestos y documentación de procedencia disponibles;
- instrucciones, notebooks, código y material de profesor;
- `submission/`, contratos, visualizaciones y otros entregables persistentes;
- pruebas; y
- su `Pxxx_activity.md` y `Pxxx_log.md` previos, si existen.

Lee `design/courses/<curso>/course_log.md` sólo si existe y sólo para contexto.
No lo modifiques. No inspecciones ni modifiques otros cursos.

## Cómo trabajar

1. Identifica todos los Pxxx y conserva su orden. No crees, elimines, renombres,
   fusiones ni reordenes actividades.
2. Reconstruye el caso con prudencia: pregunta(s) analítica(s) en viñetas; usuario,
   decisión, entidad, tiempo, datos y procedencia sólo cuando la implementación
   los demuestre. Identifica la particularidad que el dataset impone al problema:
   unidad de análisis, estructura, etiqueta, granularidad, desbalance, faltantes,
   temporalidad, ruido, sensibilidad, simulación, transformación necesaria o
   restricción de uso. Marca lo que no esté especificado.
3. Reconstruye el producto terminal actual: explicación, predicción, política,
   capacidad de datos u otro artefacto. Comprueba la identidad de Analytics con
   las preguntas de auditoría de `AGENTS.md`; las disciplinas contribuyentes
   sirven al producto, no organizan el currículo.
4. Inventaría prácticas de implementación que realmente se ejercitan: datos,
   transformaciones, funciones/métodos, patrones, validaciones, pruebas,
   persistencia, entrega u operación. No confunde una importación con una
   práctica ejercitada.
5. Contrasta cada actividad con las Pxxx anteriores del mismo curso. Una misma
   pregunta de negocio no prueba duplicación; busca el cambio analítico,
   técnico, de datos, de evidencia o de producto.
6. Escribe los highlights y sólo después redacta el inventario técnico. Cada
   afirmación importante debe tener una ruta de respaldo concreta.
7. En una ejecución incremental, conserva lo comprobado, corrige lo que la
   evidencia contradiga y registra ambigüedades. No reescribas por estilo ni
   borres una conclusión previa sin razón documentada.

## Contrato de `Pxxx_activity.md`

Usa esta estructura. Añade secciones sólo cuando la evidencia lo requiera.

```markdown
# Pxxx — Nombre observado

## Actividad actual implementada

**Implementación:** `ruta exacta`.

### Preguntas analíticas actuales

- Pregunta 1.
- Pregunta 2, si está evidenciada.

Breve descripción del caso, datos, producto terminal y límites observables.

### Highlights de contribución

- **Verbo de capacidad:** mecanismo concreto, artefacto o comportamiento
  observable; relación con Pxxx anteriores; qué se perdería sin este hito.

### Inventario técnico de implementación

- **Introduce / extiende / reutiliza / aplica en nuevo caso:** práctica concreta.

### Relación técnica con actividades anteriores

Comparación breve, incluidas posibles duplicaciones no resueltas.

### Evidencia de los highlights

| Highlight | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- |
| ... | ... | ... |

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Entrada de `traceability.yaml` revisada, vacíos, producto de Analytics y papel
de disciplinas contribuyentes.
```

### Reglas para los highlights

Un highlight es un hito de contribución, no una etiqueta. Debe contener:

1. un verbo que describa lo que se aprende a hacer o a verificar;
2. un mecanismo específico —por ejemplo, «codifica una nominal con
   `OneHotEncoder` sin imponer orden», no «usa sklearn»—;
3. la evidencia observable: notebook, función, prueba, salida, contrato o
   visualización;
4. su lugar en la secuencia: primera aparición, extensión, contraste o nueva
   aplicación; y
5. la capacidad que faltaría si el hito se elimina.

Prefiere el nivel de precisión de «muestra que una MLP de una entrada compite
con una regresión lineal de la misma entrada» al de «introduce MLP». Si se
afirma un resultado cuantitativo, cítalo sólo si está en un artefacto persistido
o en una salida verificable del repositorio. Si falta evidencia para un
highlight, no lo inventes: descríbelo como límite o ambigüedad.

La cantidad no es fija. Un taller complejo puede requerir muchos; uno breve,
pocos. Cada uno debe justificar una contribución distinguible, no cubrir cada
línea de código. Los highlights no son mejoras propuestas ni declaraciones de
logro real del estudiante.

### Highlight obligatorio de caso y datos

Cada actividad debe incluir al menos un highlight que vincule una particularidad
evidenciada del caso o dataset con la práctica que exige. Debe responder:

> ¿Qué hace que este problema no sea intercambiable con un CSV genérico y cómo
> cambia esa condición la representación, validación, interpretación o límite
> del producto?

Ejemplos válidos: texto que exige conservar expresiones de varias palabras;
clases desbalanceadas que justifican métricas por clase; imágenes que requieren
convertir una matriz de píxeles en vector; una simulación que prohíbe inferir una
política real; una serie temporal que impide partición aleatoria. «Usa un CSV»,
«trabaja con datos reales» o el nombre del dataset no son highlights. Si la
implementación no revela una particularidad distinguible, registra esa ausencia
como límite: no inventes una.

### Inventario técnico y relación con la secuencia

El inventario complementa, pero no duplica, los highlights. Debe clasificar las
prácticas como introducidas, extendidas, reutilizadas o aplicadas a un nuevo
caso. La relación con talleres previos debe diferenciar explícitamente:

- misma pregunta con nueva implementación o dato;
- misma técnica con nueva exigencia de evidencia o producto;
- nuevo método al servicio del mismo producto; y
- posible duplicación que requiere decisión posterior de curso.

## Contrato de `Pxxx_log.md`

Cada ejecución agrega `S01.Pxxx.NN` e incluye: fecha, curso, executor, estado
(inicial o incremental), rutas inspeccionadas, entrada de trazabilidad revisada,
highlights confirmados/añadidos/corregidos/no inferibles, cambios realizados,
mejoras pendientes preservadas, ambigüedades y resultado de la auditoría de
Analytics. El log documenta; no resuelve asuntos de orden, capacidades compartidas
o rediseño de curso.

## Control antes de guardar

Confirma que:

- cada Pxxx fue inspeccionado en orden y desde su contenido, no su nombre;
- cada highlight tiene evidencia y explica una contribución secuencial;
- preguntas, inventario, highlights y trazabilidad no se contradicen;
- se revisó la entrada de `traceability.yaml` o se registró su ausencia;
- no se inventaron caso, procedencia, técnica, competencia, producto ni logro;
- se preservaron mejoras aceptadas pendientes; y
- sólo cambiaron los pares Pxxx de `design/courses/<curso>/` y, si faltaba, el
  directorio del curso.

## Condición de finalización

S01 termina cuando todos los Pxxx del curso tienen su par de archivos coherente
con la implementación, con highlights que permitan comparar su contribución
antes de evaluar futuras mejoras externas.
