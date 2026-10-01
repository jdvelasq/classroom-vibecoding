# Diseño de contenido: Analítica prescriptiva

## Propósito y alcance

Curso autónomo de posgrado para estructurar alternativas y recomendaciones bajo objetivos, restricciones, incertidumbre y consecuencias; se alinea con el perfil de egreso vigente de la maestría.

## Perfil de ingreso y condición de entrada

El programa admite profesionales de trayectorias cuantitativas preferentes
(ingeniería, matemáticas, estadística, economía, administración, computación y
afines) y de otros campos que acrediten preparación equivalente en análisis
cuantitativo o manejo de información. La nivelación matemática, estadística o
computacional que eventualmente determine el Comité Asesor es una condición
institucional de acompañamiento; no es un prerrequisito entre estos seis cursos
ni autoriza a suponer una cohorte homogénea.


## Al finalizar el curso, el estudiante es capaz de…

1. **formular decisiones en términos de alternativas, objetivos, restricciones, actores y criterios de valor** — `prescriptiva.C01`; S04.F01, S04.F02.
2. **construir y juzgar modelos para comparar alternativas, factibilidad y trade-offs** — `prescriptiva.C02`; S04.F06.
3. **analizar escenarios, sensibilidad, incertidumbre y dependencia de datos o supuestos** — `prescriptiva.C03`; S04.F04, S04.F05, S04.F06.
4. **usar optimización y simulación como contribuciones funcionales a recomendaciones analíticas** — `prescriptiva.C04`; S04.F03, S04.F06.
5. **comunicar recomendaciones, riesgos, impactos y límites de manera responsable** — `prescriptiva.C05`; S04.F07, S04.F08.

Estas son capacidades terminales macro: no fijan semanas, herramientas, algoritmos, talleres, LAB ni instrumentos de evaluación.

## Frontera con Analítica predictiva

La frontera se define por la pregunta y el producto analítico, no por la familia del modelo. Este curso usa estimaciones predictivas, simulaciones, modelos mecanísticos, de supervivencia, de estados, redes u otros modelos de dominio para responder «¿qué debemos hacer entre alternativas, con qué objetivos, restricciones, costos y actores?». Construye y juzga modelos para comparar alternativas, su factibilidad y sus trade-offs, y comunica una recomendación.

La Analítica predictiva construye, valida e interpreta la estimación. La Analítica prescriptiva usa esa estimación como insumo de una elección y no repite su ajuste como fin del taller. Por ejemplo, pronosticar un pico epidemiológico y la demanda de camas es Predictiva; elegir intervenciones y capacidad bajo restricciones es Prescriptiva.

## Límites de contenido

No es un currículo abreviado de Investigación de Operaciones, teoría avanzada de algoritmos o implementación de solvers; no presupone cursos previos.

## Trazabilidad directa

| Identificador | Rol | S04 | Razón de asignación |
|---|---|---|---|
| `prescriptiva.C01` | Principal | S04.F01, S04.F02 | Decisión y valor. |
| `prescriptiva.C02` | Principal | S04.F06 | Modelos de alternativas. |
| `prescriptiva.C03` | Principal | S04.F04, S04.F05, S04.F06 | Incertidumbre y escenarios. |
| `prescriptiva.C04` | Contextual | S04.F03, S04.F06 | Frontera funcional con OR. |
| `prescriptiva.C05` | Principal | S04.F07, S04.F08 | Recomendación responsable. |

## Trazabilidad inversa

| Hallazgo S04 | Capacidades del curso |
|---|---|


## Registro de construcción

- Tarea: `S05`; curso: `prescriptiva`; fecha: 2026-09-29.
- Insumos: `design/synthesis/s04-synthesis.md` (SHA-256 `ba832f2c5a6bea26256b5efbb264408dc4034e4b183aefddd0b7efb583ba22b2`) y `design/program-context/maestria-en-analitica.pdf` (SHA-256 `844fcddb2381c8ca245a8f6b34f8e73883e6475cc7518e5190d97cbbdfe17d7f`).
- Hallazgos considerados: `S04.F01`–`S04.F11`; asignados: `S04.F01`–`S04.F10` a capacidades y `S04.F11` a la gobernanza del diseño.
- Regla: las capacidades se expresan como resultados terminales macro; no crean prerrequisitos y subordinan las disciplinas contribuyentes a Analytics.
- Pendiente: detallar contenidos, programa-calendario, RAA, talleres, LAB, evidencias de evaluación y seguimiento de RAP/RAA.

## Preparación para auditoría

El documento permite trazar cada capacidad final a S04 y, en posgrado, al perfil vigente de la maestría. No afirma que el curso ya cumpla una auditoría completa ni materializa todavía la evidencia requerida por `S04.F11`.
