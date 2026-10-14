# Formato del perfil de egreso y de los resultados de aprendizaje

Versión 0.1 (borrador)

## Propósito

Definir cómo se registran el perfil de egreso (`profile.md`) y los
resultados de aprendizaje del programa (`outcomes/<id>.md`), cómo se
derivan del mapa de competencias de `02-competencies/map/` y qué reglas de
cobertura debe cumplir el conjunto.

El mapa dice lo que una persona competente en analítica sabe y sabe hacer,
sin nivel. Este directorio fija el nivel: dice qué debe demostrar quien
termina el programa y cómo se comprueba.

## Alcance: un programa de posgrado con base en la especialización

Se redacta un solo programa: el posgrado en analítica, con el nivel de una
especialización. Según el Acuerdo 033 de 2007 del CSU, art. 11 a, la
especialización busca «el perfeccionamiento, la actualización o la
profundización de conocimientos» y desarrolla «habilidades y destrezas» en
la profesión; su trabajo final refleja la aplicación de esas habilidades
(art. 12 a).

La maestría y el doctorado reutilizan estos resultados de aprendizaje y
agregan solo su componente de investigación o de tesis. Ese componente
queda fuera de este formato.

## Fundamento normativo

Del Acuerdo CESU 02 de 2020 (`00-regulations/md/cesu-acuerdo-02-2020.md`):

- Numeral 2.2 a: los resultados de aprendizaje son declaraciones expresas
  de lo que el estudiante debe conocer y demostrar al completar el
  programa. Se establecen según las tendencias de las disciplinas, el
  perfil de formación, el nivel y la modalidad, y los estándares
  internacionales, y se definen para un programa específico.
- Numeral 2.2 b: las competencias se evalúan mediante resultados de
  aprendizaje.
- Característica 18: el desempeño del estudiante se hace evidente por el
  logro de resultados de aprendizaje que responden a las competencias.
- Característica 24: debe haber coherencia entre las competencias, el
  nivel de formación y los resultados de aprendizaje.
- Característica 25: el programa evalúa periódicamente el grado en que los
  estudiantes alcanzan los resultados de aprendizaje.

De ahí salen las piezas de cada resultado de aprendizaje: un enunciado
evaluable con nivel (2.2 a), las competencias que evalúa (2.2 b y
característica 24), un mecanismo de evaluación (características 18 y 25)
y la trazabilidad hasta la evidencia que respalda esas competencias.

Los lineamientos de armonización curricular de la UNAL
(`unal-lineamientos-armonizacion-curricular.md`) piden además incorporar
los resultados de aprendizaje al currículo y diseñar su seguimiento. Eso
ocurre en el eslabón siguiente (matriz de resultados por cursos).

## Perfil de egreso: `profile.md`

Un solo archivo con un encabezado YAML y tres secciones, en este orden:
`## Perfil de egreso`, `## Desempeños` y `## Alcance`.

```yaml
programa: "Posgrado en Analítica"
nivel: "especialización"
format_version: "0.1"
fecha: "2026-10-13"
```

1. **Perfil de egreso**: uno o dos párrafos que dicen quién es la persona
   egresada, qué preguntas y decisiones de una organización apoya, qué
   productos analíticos entrega y con qué autonomía. Se escribe desde la
   analítica, no desde una disciplina contribuyente.
2. **Desempeños**: una viñeta por desempeño del egresado, con los
   resultados de aprendizaje que lo demuestran al final:
   `- Plantea problemas de decisión como problemas analíticos y los
   acuerda con los interesados [RA01].` Todo resultado de aprendizaje
   aparece al menos una vez, y no se cita ninguno que no exista.
3. **Alcance**: el nivel, lo que la maestría y el doctorado agregan, y lo
   que queda fuera (competencias candidatas o retiradas, vecinos de
   `domain.md`).

## Archivo de un resultado de aprendizaje

Cada resultado de aprendizaje vive en `outcomes/<id>.md`. El `id` es `RA`
seguido de dos dígitos (`RA01`, `RA02`, …), se asigna en orden y no se
reutiliza.

El archivo tiene un encabezado YAML y cinco secciones, en este orden:
`## Enunciado`, `## Partes del enunciado`, `## Competencias`,
`## Evaluación` y `## Trazabilidad`. Al final se admiten `## Notas` y
`## Pendientes`.

### Encabezado

```yaml
id: "RA01"
enunciado: "…"
competencias: ["C001", "C006"]
nivel: "especialización"
format_version: "0.1"
fecha: "2026-10-13"
```

### 1. Enunciado

Una sola oración, evaluable, con cuatro partes:

- **Verbo observable** en infinitivo, al inicio: lo que el estudiante hace
  y alguien puede ver o revisar.
- **Objeto**: el producto analítico que resulta.
- **Condición o contexto**: la situación, los datos, la decisión y las
  restricciones bajo las que actúa.
- **Nivel**: lo que hace que el desempeño sea de posgrado. En la
  especialización, el estudiante actúa con autonomía sobre un caso real o
  realista, con datos imperfectos, justifica sus decisiones frente a
  alternativas e integra varias piezas de la competencia en un producto.

En el mapa, el verbo nombraba un desempeño sin fijar profundidad. Aquí el
verbo sí fija el nivel. Se excluyen:

- verbos no observables: conocer, comprender, entender, saber, aprender,
  familiarizarse, apreciar, valorar, interiorizar, asimilar;
- verbos de un nivel inferior al de posgrado: definir, describir,
  enumerar, identificar, listar, nombrar, recordar, reconocer, repetir,
  memorizar.

Verbos adecuados: formular, diseñar, construir, evaluar, justificar,
integrar, desplegar, monitorear, comunicar, estimar, seleccionar, validar.

El enunciado no nombra herramientas. Una herramienta puede aparecer en la
evaluación como ejemplo, igual que en el mapa.

### 2. Partes del enunciado

Cuatro viñetas, en este orden, que separan el enunciado en sus partes:
`- Verbo: formular.`, `- Objeto: …`, `- Condición: …`, `- Nivel: …`. El
verbo es la primera palabra del enunciado. La viñeta de nivel dice por qué
el desempeño es de posgrado.

### 3. Competencias

Una viñeta por competencia del encabezado, con lo que el resultado toma de
ella: `- C001: el planteamiento del problema analítico y sus medidas de
éxito.`

Un resultado de aprendizaje cubre entre una y tres competencias. Solo se
citan competencias con `estado: "incluida"`.

### 4. Evaluación

El mecanismo de evaluación sugerido: qué produce o hace el estudiante, en
qué situación y qué se revisa. Sale de la evidencia de desempeño de las
competencias cubiertas, no de la costumbre de una disciplina. Cada viñeta
termina con las competencias que evalúa entre corchetes: `[C001]` o
`[C001; C006]`.

No es una rúbrica. La rúbrica y el peso de cada producto se fijan en los
cursos.

### 5. Trazabilidad

Una tabla que une el resultado con la evidencia, a través de las
competencias:

| Columna | Contenido |
|---|---|
| Competencia | Una competencia del encabezado. Cada una tiene al menos una fila. |
| Evidencia | El `id` y la ubicación de un documento citado en la sección `Evidencia de desempeño` de esa competencia. |
| Producto evaluable | El producto de esa evidencia que el mecanismo de evaluación adapta. |

Si la competencia no tiene evidencia de desempeño con fuente (su sección
dice «Ninguna fuente»), la celda dice `Ninguna fuente` y el producto se
propone; la skill lo advierte.

## Reglas de cobertura

1. Toda competencia con `estado: "incluida"` queda cubierta por al menos un
   resultado de aprendizaje.
2. Las competencias candidatas y retiradas no entran. Si una candidata
   pasa a incluida, la skill la informa como no cubierta.
3. El programa tiene entre 6 y 10 resultados de aprendizaje.
4. Cada resultado cubre entre una y tres competencias.
5. Todo resultado aparece en los desempeños del perfil.
6. Identidad (`AGENTS.md` en la raíz): el conjunto no puede leerse como el
   programa de una disciplina contribuyente. Un resultado de analítica
   prescriptiva no termina en un modelo, una frontera de Pareto o una
   simulación: termina en una política de decisión con restricciones,
   salvaguardas, autoridad humana y seguimiento de resultados.

Las reglas 1 a 5 las comprueba la skill `writing-learning-outcomes`. La
regla 6 la juzga quien redacta y se informa a david.

## Ejemplo trabajado

Dos resultados de aprendizaje a partir de competencias reales del mapa.
Las ubicaciones citadas están en la `Evidencia de desempeño` de cada
competencia.

````markdown
---
id: "RA01"
enunciado: "Formular, a partir de una situación de decisión real o realista de una organización, un problema analítico con medidas de éxito numéricas, línea base, supuestos y riesgos, y sustentarlo ante los interesados hasta obtener su acuerdo."
competencias: ["C001", "C006"]
nivel: "especialización"
format_version: "0.1"
fecha: "2026-10-13"
---

# RA01. Plantear y acordar el problema analítico

## Enunciado

Formular, a partir de una situación de decisión real o realista de una
organización, un problema analítico con medidas de éxito numéricas, línea
base, supuestos y riesgos, y sustentarlo ante los interesados hasta
obtener su acuerdo.

## Partes del enunciado

- Verbo: formular.
- Objeto: un problema analítico con medidas de éxito numéricas, línea
  base, supuestos y riesgos.
- Condición: una situación de decisión real o realista de una
  organización, con interesados de perfiles distintos y datos aún sin
  explorar.
- Nivel: el estudiante delimita el problema con autonomía, justifica las
  medidas de éxito frente a alternativas y obtiene el acuerdo de
  interesados no técnicos.

## Competencias

- C001: el paso del problema de decisión al problema analítico, con sus
  medidas de éxito.
- C006: la presentación del planteamiento, con sus supuestos y
  limitaciones, para que los interesados lo validen.

## Evaluación

- Documento de planteamiento sobre un caso de una organización: problema
  de negocio, problema analítico, factores, supuestos, medidas de éxito
  con número y horizonte, línea base y riesgos [C001].
- Sustentación oral ante un panel que hace de patrocinador e interesados,
  con el registro de los acuerdos y de los cambios al planteamiento
  [C001; C006].

## Trazabilidad

| Competencia | Evidencia | Producto evaluable |
|---|---|---|
| C001 | E0001 p. 5, tareas 2.1–2.6 | Enunciado del problema analítico con factores, supuestos, medidas de éxito, línea base y riesgos |
| C001 | E0028 p. 9 | Objetivos de negocio con criterios de éxito numéricos |
| C006 | E0143 §8 | Presentación grabada de los hallazgos ante evaluadores |
````

````markdown
---
id: "RA02"
enunciado: "Diseñar, para una decisión recurrente de una organización, una política de decisión que asigne a cada contexto observado una acción factible según los objetivos y las restricciones, con salvaguardas, excepciones, autoridad humana, cadencia de decisión y seguimiento de resultados explícitos."
competencias: ["C009"]
nivel: "especialización"
format_version: "0.1"
fecha: "2026-10-13"
---

# RA02. Diseñar una política de decisión

## Enunciado

Diseñar, para una decisión recurrente de una organización, una política de
decisión que asigne a cada contexto observado una acción factible según
los objetivos y las restricciones, con salvaguardas, excepciones,
autoridad humana, cadencia de decisión y seguimiento de resultados
explícitos.

## Partes del enunciado

- Verbo: diseñar.
- Objeto: una política de decisión que va del contexto observado a una
  acción factible, con salvaguardas, excepciones, autoridad humana,
  cadencia y seguimiento.
- Condición: una decisión recurrente de una organización, con objetivos
  en conflicto, restricciones de capacidad o de política y los datos del
  contexto disponibles al momento de decidir.
- Nivel: el estudiante usa modelos de optimización, simulación o reglas
  como soporte, compara alternativas y justifica la factibilidad, quién
  conserva la autoridad y cómo se revisa la política.

## Competencias

- C009: la política de decisión completa, del contexto observado a la
  acción, con su autoridad y su seguimiento.

## Evaluación

- Documento de política: contexto observable, acciones posibles,
  objetivos y restricciones, modelo de soporte, salvaguardas y
  excepciones, qué decide una persona y qué se automatiza, cadencia e
  indicadores de seguimiento [C009].
- Prueba de la política sobre escenarios históricos o simulados,
  comparada con la práctica actual de la organización [C009].

## Trazabilidad

| Competencia | Evidencia | Producto evaluable |
|---|---|---|
| C009 | E0031 p. 20 | Problema de optimización ajustado a la capacidad disponible, como soporte de la política |
| C009 | E0004 p. 4 | Decisiones operativas automatizadas (calificación de crédito, mejor oferta) con evaluación de sus resultados |

## Pendientes

- Las salvaguardas y las excepciones vienen de `AGENTS.md`, no de la
  evidencia: `C009` tiene ese pendiente abierto en el mapa.
````

Qué muestra el ejemplo:

- `RA01` integra dos competencias en un solo producto evaluable: el
  planteamiento se escribe y se sustenta.
- `RA01` usa un segundo verbo (sustentar) dentro de la misma oración; el
  verbo que se valida es el primero.
- `RA02` cubre una sola competencia, porque la política de decisión ya es
  un producto completo.
- `RA02` cumple la regla de identidad para la prescriptiva: el modelo de
  optimización es soporte, el producto es la política.
- Ninguno de los dos nombra herramientas; las de la evidencia (IBM SPSS
  Modeler, SAS Decision Manager) quedan fuera del enunciado.

## Versión y cambios

- 0.1 (2026-10-13): borrador inicial. Valores por defecto que david debe
  aprobar: el nivel de especialización como base, de 6 a 10 resultados,
  de una a tres competencias por resultado, las dos listas de verbos
  excluidos y la evaluación como mecanismo sugerido, sin rúbrica.
