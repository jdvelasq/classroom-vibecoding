# Formato del plan de cursos y de la matriz de resultados

Versión 0.3 (borrador)

## Propósito

Definir cómo se registran los cursos (`courses.md`), la matriz que reparte
los resultados de aprendizaje del programa de posgrado entre sus cursos
(`matrix.csv`), la ficha de cada curso de posgrado
(`postgraduate/<carpeta>.md`), los resultados propios de los cursos de
pregrado (`undergraduate/<carpeta>.md`) y qué reglas debe cumplir el
conjunto.

Es el tercer eslabón del puente entre lo que el egresado debe saber y lo
que los cursos enseñan: los resultados de aprendizaje de
`03-learning-outcomes/` dicen qué se demuestra al terminar el programa;
este directorio dice en qué curso se introduce, se desarrolla y se domina
cada uno. El syllabus de cada curso, en `05-implementation/<carpeta>/`, deriva de
aquí sus contenidos y su evaluación.

## Fundamento normativo

- Acuerdo CESU 02 de 2020, característica 24: coherencia entre las
  competencias, el nivel de formación y los resultados de aprendizaje.
- Característica 25: el programa evalúa periódicamente el logro de los
  resultados de aprendizaje; la matriz dice en qué curso se evalúa cada
  uno en su nivel final.
- Lineamientos de armonización curricular de la UNAL: incorporar los
  resultados de aprendizaje al currículo y diseñar su seguimiento.

## Cursos: `courses.md`

Un archivo con un encabezado YAML (`format_version`, `domain_version`,
`fecha`) y estas secciones: `## Lista de cursos`, `## Propósito` y
`## Continuidad`.

La lista es una tabla con las columnas `Carpeta`, `Curso`, `Nivel`,
`Estado` y `Subcampos`. El nivel es `posgrado` o `pregrado`; el estado,
`vigente` o `propuesto`. Un curso propuesto cumple las mismas reglas que
uno vigente. Los subcampos, separados por punto y coma, se escriben como en
`01-evidence/domain.md`; la tendencia emergente se escribe
`IA generativa y agéntica (transversal)`. Las filas de posgrado van en el
orden en que se cursan: la regla de autocontención se comprueba sobre ese
orden.

Los cursos salen de la definición de analítica, no de una elección de
diseño: a cada subcampo de `domain.md`, y a la tendencia de IA generativa y
agéntica, le corresponde al menos un curso. La tendencia tiene curso propio
y además puede aparecer en los demás cursos.

`## Propósito` tiene una subsección `### <carpeta>` por curso con su
propósito. `courses.md` es una decisión de david: la skill lo lee, nunca lo
escribe.

## Matriz del posgrado: `matrix.csv`

Una fila por cada par resultado de aprendizaje y curso donde ese resultado
se trabaja. Los pares ausentes significan que el curso no trabaja ese
resultado.

| Columna | Contenido |
|---|---|
| `ra` | El `id` de un resultado de `03-learning-outcomes/outcomes/`. |
| `curso` | La carpeta de un curso de posgrado de `courses.md`. |
| `nivel` | `introduce`, `desarrolla` o `domina`. |
| `aporte` | Una oración: qué parte del producto del resultado se trabaja en ese curso. |
| `fecha` | Fecha en que se fijó la fila. |

### Niveles

- **introduce**: el curso presenta el desempeño del resultado y el
  estudiante lo practica de forma guiada sobre partes del producto.
- **desarrolla**: el estudiante produce el producto con autonomía parcial,
  sobre un caso preparado por el profesor, y recibe retroalimentación.
- **domina**: el estudiante produce, con la autonomía y en las condiciones
  que fija el enunciado del resultado, el producto completo que describe
  su sección `Evaluación`, y el curso lo evalúa.

Un curso puede dominar un resultado sin que otro lo haya introducido
antes: en ese caso el propio curso lo introduce y lo lleva hasta el
dominio, y la fila dice `domina`.

## Cursos de posgrado: `postgraduate/<carpeta>.md`

Cada curso de posgrado tiene su ficha. Es la vista por curso de la matriz:
lo que el syllabus de `05-syllabus/<carpeta>/` toma como punto de partida.

El archivo tiene un encabezado YAML y cuatro secciones, en este orden:
`## Propósito`, `## Conocimientos requeridos`,
`## Resultados de aprendizaje` y `## Alcance`.

```yaml
curso: "prescriptiva"
nivel: "posgrado"
format_version: "0.3"
fecha: "2026-10-14"
```

1. **Propósito**: un párrafo coherente con el propósito de `courses.md`:
   qué pregunta analítica responde el curso y qué producto terminal
   entrega el estudiante.
2. **Conocimientos requeridos**: una viñeta por conocimiento que el
   curso presupone y no enseña, por ejemplo la programación básica en
   Python en `predictiva`. El curso es autocontenido: presupone
   conocimientos, nunca cursos, así que esta sección no nombra ningún
   curso de `courses.md`. Lo que se presupone aquí no se enseña en el
   curso.
3. **Resultados de aprendizaje**: una viñeta por fila de `matrix.csv` con
   ese curso, en orden de `id`: `- RA02, domina: aporte.` El nivel y el
   aporte son los de la matriz.
4. **Alcance**: las fronteras con los demás cursos (qué le corresponde a
   cada uno cuando un tema los toca a ambos) y lo que queda fuera.

## Cursos de pregrado: `undergraduate/<carpeta>.md`

Los cursos de pregrado no derivan de los resultados de aprendizaje del
programa de posgrado, porque no hay garantía de continuidad entre los dos
niveles. Cada uno tiene sus propios resultados de curso, que salen
directamente de las competencias incluidas del mapa
(`02-competencies/map/`), a nivel introductorio.

El archivo tiene un encabezado YAML y tres secciones, en este orden:
`## Propósito`, `## Resultados del curso` y `## Alcance`.

```yaml
curso: "data"
nivel: "pregrado"
format_version: "0.3"
fecha: "2026-10-14"
```

1. **Propósito**: un párrafo coherente con el propósito de `courses.md`.
2. **Resultados del curso**: una subsección por resultado,
   `### RC01. Título`, con tres viñetas en este orden:
   - `- Enunciado: …` Una oración evaluable que empieza con un verbo
     observable en infinitivo. A nivel introductorio se admiten verbos
     como describir o identificar; se excluyen los no observables
     (conocer, comprender, entender, saber, aprender, familiarizarse,
     apreciar, valorar, interiorizar, asimilar).
   - `- Competencias: C002, C003.` Entre una y tres competencias con
     `estado: "incluida"`.
   - `- Evaluación: …` Qué produce el estudiante y qué se revisa,
     terminado con las competencias que evalúa entre corchetes.

   Los identificadores `RC` se asignan en orden dentro de cada curso. Fuera
   del archivo se citan con la carpeta: `data/RC01`.
3. **Alcance**: lo que el curso deja fuera, en particular la profundidad
   que corresponde al posgrado o a una disciplina contribuyente.

Un enunciado de pregrado no nombra herramientas, salvo las que nombre el
propósito del curso en `courses.md` (Python, en `fundamentos`).

## Reglas

1. A cada subcampo de `domain.md`, y a la tendencia de IA generativa y
   agéntica, le corresponde al menos un curso de `courses.md`.
2. Todo resultado de aprendizaje del programa llega a `domina` en algún
   curso de posgrado.
3. Ningún curso de posgrado queda sin resultados de aprendizaje.
4. Autocontención del posgrado: un curso de posgrado presupone
   conocimientos, declarados en su ficha, y no cursos. Los estudiantes de
   posgrado no han visto los cursos de pregrado. Ningún curso de posgrado presupone un curso de
   pregrado (la matriz solo admite cursos de posgrado), y la primera vez
   que un resultado aparece en el orden de `courses.md` su nivel es
   `introduce` o `domina`, nunca `desarrolla`, porque desarrollar
   presupone una introducción que ningún curso anterior dio.
5. Un resultado no retrocede: después de `domina`, un curso posterior no lo
   marca como `introduce`. Se informa como advertencia.
6. Un curso trabaja resultados de su propio campo: si los subcampos del
   curso no comparten ninguno con los de las competencias del resultado,
   se informa como advertencia para que el modelo lo justifique en el
   `aporte`.
7. Cada curso de pregrado tiene entre 3 y 6 resultados de curso, y cada
   subcampo que `courses.md` le asigna queda cubierto por al menos un
   resultado cuyas competencias lo incluyan.
8. Los cursos de pregrado no citan resultados de aprendizaje del programa
   (`RA01`, …).
9. Todo curso de posgrado tiene su ficha, y sus resultados de aprendizaje
   coinciden con las filas de `matrix.csv` para ese curso, con el mismo
   nivel. La ficha declara al menos un conocimiento requerido, sus
   conocimientos requeridos no nombran cursos, y la ficha no cita cursos
   de pregrado.
10. Identidad (`AGENTS.md` en la raíz): ningún curso se reduce a una
   versión abreviada de una disciplina contribuyente. El curso de
   prescriptiva domina resultados que terminan en una política de
   decisión, no en un modelo.

Las reglas 1 a 9 las comprueba la skill `mapping-curriculum`. La regla 10 la
juzga quien propone la matriz y se informa a david.

## Ejemplo trabajado

Filas de la matriz para los dos resultados del ejemplo de
`03-learning-outcomes/format.md`:

```csv
ra,curso,nivel,aporte,fecha
RA01,descriptiva,introduce,"Plantea la pregunta descriptiva de un caso y sus medidas de éxito antes de explorar los datos.",2026-10-14
RA01,predictiva,desarrolla,"Formula el problema predictivo con horizonte, línea base y costo de los errores y lo sustenta ante el profesor.",2026-10-14
RA01,prescriptiva,domina,"Formula y sustenta ante un panel el problema de decisión completo que da origen a la política.",2026-10-14
RA02,prescriptiva,domina,"Diseña la política de decisión con salvaguardas, autoridad humana, cadencia y seguimiento.",2026-10-14
RA02,productos,desarrolla,"Lleva la política a un producto que la ejecuta y registra sus resultados para revisarla.",2026-10-14
```

Qué muestra:

- `RA01` se introduce, se desarrolla y se domina en tres cursos distintos,
  en el orden de `courses.md`.
- `RA02` aparece por primera vez como `domina` en `prescriptiva`: el curso
  lo introduce y lo lleva hasta el dominio.
- `RA02` sigue en `productos` como `desarrolla` después de dominarse: no es
  retroceso, porque el curso posterior lo usa en un producto.

La ficha de `prescriptiva` que corresponde a esas filas:

````markdown
---
curso: "prescriptiva"
nivel: "posgrado"
format_version: "0.3"
fecha: "2026-10-14"
---

# Analítica prescriptiva

## Propósito

Diseñar, validar y gobernar políticas de decisión para decisiones
recurrentes de una organización: el producto terminal es una política que
va del contexto observado a una acción factible, con salvaguardas,
autoridad humana y seguimiento.

## Conocimientos requeridos

- Programación básica en Python: estructuras de datos, funciones y
  manejo de tablas de datos.
- Álgebra lineal y probabilidad básicas.

## Resultados de aprendizaje

- RA01, domina: Formula y sustenta ante un panel el problema de decisión
  completo que da origen a la política.
- RA02, domina: Diseña la política de decisión con salvaguardas, autoridad
  humana, cadencia y seguimiento.

## Alcance

- Con `predictiva`: predictiva construye y valida la estimación;
  prescriptiva la usa para decidir.
- Con `productos`: productos despliega y observa la política; prescriptiva
  define su semántica, sus restricciones y su validación.
- La investigación de operaciones como disciplina queda fuera: la
  optimización y la simulación entran como soporte de la política.
````

Resultados de un curso de pregrado:

````markdown
---
curso: "data"
nivel: "pregrado"
format_version: "0.3"
fecha: "2026-10-14"
---

# Fundamentos de data para analítica

## Propósito

Presentar a estudiantes de pregrado los aspectos de ingeniería de datos
que una persona de analítica necesita para obtener, integrar y preparar
los datos de una pregunta analítica.

## Resultados del curso

### RC01. Obtener e integrar datos

- Enunciado: Obtener e integrar, mediante consultas, los datos de dos o
  más fuentes que necesita una pregunta analítica dada, en un conjunto de
  datos único y documentado.
- Competencias: C002.
- Evaluación: Consultas y conjunto de datos integrado para una pregunta
  dada, con la descripción de cada fuente y de cada unión [C002].

### RC02. Evaluar la calidad de los datos

- Enunciado: Evaluar la calidad de un conjunto de datos frente a una
  pregunta analítica, con reglas de validación que detecten faltantes,
  duplicados y valores fuera de rango.
- Competencias: C002.
- Evaluación: Reporte de calidad con las reglas aplicadas, los
  problemas encontrados y la corrección de cada uno [C002].

### RC03. Entregar datos listos para el análisis

- Enunciado: Construir un flujo reproducible que entregue un conjunto de
  datos analítico listo para explorarse con resúmenes y visualizaciones.
- Competencias: C002, C003.
- Evaluación: Flujo ejecutable de principio a fin y una exploración
  inicial que muestra que los datos responden la pregunta [C002; C003].

## Alcance

- La administración de bases de datos y de plataformas queda fuera: es
  ingeniería de datos como disciplina autónoma.
- La modelación predictiva y prescriptiva queda fuera del curso.
````

## Versión y cambios

- 0.3 (2026-10-14): la condición de entrada de la ficha de posgrado pasa a
  ser `Conocimientos requeridos`: el curso es autocontenido, presupone
  conocimientos que no enseña y nunca cursos.
- 0.2 (2026-10-14): se agrega la ficha de cada curso de posgrado,
  `postgraduate/<carpeta>.md`, porque la matriz sola no deja un producto
  por curso. Sus resultados deben coincidir con `matrix.csv`.
- 0.1 (2026-10-14): borrador inicial. Valores por defecto que david debe
  aprobar: los cursos de posgrado se cursan en el orden de `courses.md`;
  los tres niveles y su definición; la autocontención como «la primera
  aparición no es `desarrolla`»; entre 3 y 6 resultados por curso de
  pregrado; verbos de nivel introductorio admitidos en pregrado; el curso
  propuesto `generativa` se cursa al final del posgrado.
