# Diseño de contenido: Analítica prescriptiva

## Propósito y alcance

Curso autónomo de posgrado para diseñar, validar y gobernar **políticas
computables para decisiones operativas recurrentes**. Una política transforma
un contexto observable y datos disponibles en una acción factible bajo
objetivos, restricciones, salvaguardas y una autoridad de decisión definida;
su resultado se registra, monitorea y revisa.

La automatización no es un requisito absoluto: una política puede ejecutar una
acción de bajo riesgo o producir una recomendación que requiera aprobación
humana. En ambos casos declara cadencia y necesidad de respuesta. El curso no
es una versión abreviada de Investigación de Operaciones. Optimización,
simulación, análisis multicriterio, árboles de decisión y estimaciones
predictivas son contribuciones funcionales al diseño o validación de una
política, no productos terminales independientes.

## Perfil de ingreso y condición de entrada

El programa admite profesionales de trayectorias cuantitativas preferentes
(ingeniería, matemáticas, estadística, economía, administración, computación y
afines) y de otros campos que acrediten preparación equivalente en análisis
cuantitativo o manejo de información. La nivelación matemática, estadística o
computacional que eventualmente determine el Comité Asesor es acompañamiento
institucional; no es prerrequisito entre estos seis cursos ni autoriza a suponer
una cohorte homogénea.

## Al finalizar el curso, el estudiante es capaz de…

1. **formular una decisión recurrente como un contrato de política: contexto observable, responsable, cadencia, acción, objetivos, restricciones, salvaguardas, excepciones y criterios de revisión** — `prescriptiva.C01`; S04.F01, S04.F02, S04.F08.
2. **diseñar una política computable que transforme datos y contexto en una acción factible, distinguiendo evidencia predictiva de la decisión que la utiliza** — `prescriptiva.C02`; S04.F03, S04.F04, S04.F06.
3. **validar una política frente a líneas base, escenarios, sensibilidad, incertidumbre, demoras y consecuencias no deseadas antes de operarla** — `prescriptiva.C03`; S04.F04, S04.F05, S04.F06.
4. **definir el modo proporcional de ejecución —automatización, recomendación con aprobación humana o escalamiento por excepción— y dejar trazable cada decisión** — `prescriptiva.C04`; S04.F02, S04.F07, S04.F08.
5. **monitorear resultados, equidad, supuestos y límites de una política, y especificar los gatillos para revisarla, suspenderla o recalibrarla** — `prescriptiva.C05`; S04.F05, S04.F07, S04.F08.

Estas son capacidades terminales macro: no fijan semanas, herramientas,
algoritmos, talleres, LAB ni instrumentos de evaluación.

## Fronteras con Analítica predictiva y Productos de datos

La frontera con Predictiva se define por la pregunta y el producto. Predictiva
construye, valida e interpreta una estimación; Prescriptiva usa esa evidencia
para definir y validar una política. Pronosticar el pico de demanda de camas
es Predictiva; definir cuándo ampliar capacidad, comprar recursos o escalar una
alerta es Prescriptiva.

Productos de datos diseña la infraestructura reusable que integra, despliega,
mantiene y observa capacidades analíticas. Prescriptiva define la semántica de
la política, sus restricciones, excepciones, autoridad y validación. Una
actividad prescriptiva debe demostrar una política operable; no necesita
convertirse en arquitectura o despliegue de software.

| Situación | Producto de Predictiva | Producto de Prescriptiva |
|---|---|---|
| Capacidad hospitalaria | Pico de demanda y su incertidumbre. | Regla de capacidad, compras o escalamiento bajo restricciones. |
| Inventario | Demanda, tiempos o riesgo de agotamiento. | Política recurrente de reposición o asignación. |
| Riesgo | Probabilidad, momento o perfil de riesgo. | Política de priorización, revisión o acción con criterios explícitos. |

## Límites de contenido

No es un currículo abreviado de Investigación de Operaciones, teoría avanzada
de algoritmos, implementación de solvers, ni arquitectura de productos de
datos; no presupone cursos previos. Un modelo aislado, una frontera Pareto, un
resultado de simulación o un árbol usado solo para deliberar no bastan como
resultado terminal: deben contribuir a una política recurrente y gobernada.

## Trazabilidad directa

| Identificador | Rol | S04 | Razón de asignación |
|---|---|---|---|
| `prescriptiva.C01` | Principal | S04.F01, S04.F02, S04.F08 | Contrato de política y decisión recurrente. |
| `prescriptiva.C02` | Principal | S04.F03, S04.F04, S04.F06 | Política computable basada en evidencia. |
| `prescriptiva.C03` | Principal | S04.F04, S04.F05, S04.F06 | Validación de políticas bajo incertidumbre. |
| `prescriptiva.C04` | Principal | S04.F02, S04.F07, S04.F08 | Autoridad, excepciones y trazabilidad de ejecución. |
| `prescriptiva.C05` | Principal | S04.F05, S04.F07, S04.F08 | Seguimiento, equidad y recalibración. |

## Trazabilidad inversa

| Hallazgo S04 | Capacidades del curso |
|---|---|
| `S04.F01` | `prescriptiva.C01` |
| `S04.F02` | `prescriptiva.C01`, `prescriptiva.C04` |
| `S04.F03` | `prescriptiva.C02` |
| `S04.F04` | `prescriptiva.C02`, `prescriptiva.C03` |
| `S04.F05` | `prescriptiva.C03`, `prescriptiva.C05` |
| `S04.F06` | `prescriptiva.C02`, `prescriptiva.C03` |
| `S04.F07` | `prescriptiva.C04`, `prescriptiva.C05` |
| `S04.F08` | `prescriptiva.C01`, `prescriptiva.C04`, `prescriptiva.C05` |
| `S04.F09` | Integración posterior mediante talleres; no es capacidad terminal separada. |
| `S04.F10` | Selección funcional de técnicas y tecnologías; no es capacidad terminal separada. |
| `S04.F11` | Gobernanza del diseño y de esta trazabilidad. |

## Auditoría de identidad del curso

- **Producto terminal:** política computable y gobernada para una decisión
  operativa recurrente, con acción, restricciones, salvaguardas, excepción y
  revisión explícitas.
- **Pregunta de línea:** «¿qué acción recurrente debe tomarse bajo cuáles
  objetivos, restricciones, salvaguardas, excepciones y mecanismo de
  revisión?»
- **Disciplinas contribuyentes:** OR/optimización, simulación, modelos
  predictivos, estadística, bases de datos y técnicas de IA aportan evidencia,
  factibilidad o validación; no organizan el curso.
- **Riesgo a vigilar:** que una actividad termine en una solución matemática o
  comparación exploratoria sin producir una política operable y monitoreable.

## Registro de construcción

- Tarea: `S05`; curso: `prescriptiva`; fecha: 2026-10-01.
- Insumos: `design/synthesis/s04-synthesis.md` (SHA-256
  `ba832f2c5a6bea26256b5efbb264408dc4034e4b183aefddd0b7efb583ba22b2`) y
  `design/program-context/maestria-en-analitica.pdf` (SHA-256
  `844fcddb2381c8ca245a8f6b34f8e73883e6475cc7518e5190d97cbbdfe17d7f`).
- Hallazgos considerados: `S04.F01`–`S04.F11`; asignados: `S04.F01`–`S04.F10`
  a capacidades y `S04.F11` a la gobernanza del diseño.
- Regla: las capacidades se expresan como resultados terminales macro; no
  crean prerrequisitos y subordinan las disciplinas contribuyentes a
  Analytics. La decisión local exige una política computable y gobernada para
  una decisión recurrente; no se atribuye esa restricción como definición
  universal a las fuentes S04.
- Pendiente: programa-calendario, RAA, talleres, LAB, evidencias de evaluación
  y seguimiento de RAP/RAA.

## Preparación para auditoría

El documento permite trazar cada capacidad terminal a S04 y al perfil vigente
de la maestría. No afirma cumplimiento completo de una auditoría internacional
ni materializa todavía evidencia de implementación.
