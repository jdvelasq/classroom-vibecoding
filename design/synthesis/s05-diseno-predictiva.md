# Diseño de contenido: Analítica predictiva

## Propósito y alcance

Curso autónomo de posgrado para anticipar resultados mediante modelos interpretables, validados y útiles para decisiones; se alinea con el perfil de egreso vigente de la maestría. Se fundamenta en KDD y Data Mining, que aportan metodologías y experiencias previas al surgimiento de Analytics y continúan aportando problemas, metodologías y soluciones de valor analítico demostrable. Machine Learning y Deep Learning aportan modelos y avances metodológicos cuando resultan adecuados para la tarea.

## Perfil de ingreso y condición de entrada

El programa admite profesionales de trayectorias cuantitativas preferentes
(ingeniería, matemáticas, estadística, economía, administración, computación y
afines) y de otros campos que acrediten preparación equivalente en análisis
cuantitativo o manejo de información. La nivelación matemática, estadística o
computacional que eventualmente determine el Comité Asesor es una condición
institucional de acompañamiento; no es un prerrequisito entre estos seis cursos
ni autoriza a suponer una cohorte homogénea.


## Al finalizar el curso, el estudiante es capaz de…

1. **traducir una decisión en objetivo predictivo, horizonte, variable objetivo, línea base y criterio de éxito** — `predictiva.C01`; S04.F01, S04.F02.
2. **preparar y juzgar datos para predicción, identificando representación, fuga de información, sesgos y límites** — `predictiva.C02`; S04.F04, S04.F05, S04.F08.
3. **seleccionar, validar y comparar modelos predictivos según su adecuación al problema y no sólo su desempeño técnico** — `predictiva.C03`; S04.F06.
4. **interpretar desempeño, incertidumbre, explicabilidad y consecuencias de uso de una predicción** — `predictiva.C04`; S04.F05, S04.F07, S04.F08.
5. **reconocer la necesidad de documentación, monitoreo y revisión responsable durante el ciclo de vida** — `predictiva.C05`; S04.F08, S04.F10.

Estas son capacidades terminales macro: no fijan semanas, herramientas, algoritmos, talleres, LAB ni instrumentos de evaluación.

## Frontera con Analítica prescriptiva

La frontera se define por la pregunta y el producto analítico, no por la familia del modelo. Este curso construye, valida e interpreta estimaciones que responden «¿qué ocurrirá, con qué probabilidad, cuándo o para quién?». Puede usar modelos procedentes de KDD y Data Mining, Machine Learning, Deep Learning, simulación, modelos mecanísticos, de supervivencia, de estados, redes u otros modelos de dominio cuando sean adecuados para la tarea predictiva.

Un modelo de Machine Learning o Deep Learning entra al curso porque permite resolver una tarea predictiva con valor analítico demostrable; no para cubrir una taxonomía de algoritmos. La elección del método se fundamenta en la dinámica y los supuestos del fenómeno, no en la popularidad de la técnica.

Cuando una estimación se usa como insumo para seleccionar una alternativa bajo objetivos, restricciones, costos y actores, el producto principal corresponde a Analítica prescriptiva.

## Límites de contenido

No es un curso enciclopédico de Machine Learning, Deep Learning, MLOps o infraestructura de producción; no presupone cursos previos.

## Trazabilidad directa

| Identificador | Rol | S04 | Razón de asignación |
|---|---|---|---|
| `predictiva.C01` | Principal | S04.F01, S04.F02 | Problema y objetivo predictivo. |
| `predictiva.C02` | Recurrente | S04.F04, S04.F05, S04.F08 | Datos y riesgos. |
| `predictiva.C03` | Principal | S04.F06 | Juicio sobre modelos. |
| `predictiva.C04` | Principal | S04.F05, S04.F07, S04.F08 | Interpretación para decisión. |
| `predictiva.C05` | Recurrente | S04.F08, S04.F10 | Ciclo responsable. |

## Trazabilidad inversa

| Hallazgo S04 | Capacidades del curso |
|---|---|


## Registro de construcción

- Tarea: `S05`; curso: `predictiva`; fecha: 2026-09-29.
- Insumos: `design/synthesis/s04-synthesis.md` (SHA-256 `ba832f2c5a6bea26256b5efbb264408dc4034e4b183aefddd0b7efb583ba22b2`) y `design/program-context/maestria-en-analitica.pdf` (SHA-256 `844fcddb2381c8ca245a8f6b34f8e73883e6475cc7518e5190d97cbbdfe17d7f`).
- Hallazgos considerados: `S04.F01`–`S04.F11`; asignados: `S04.F01`–`S04.F10` a capacidades y `S04.F11` a la gobernanza del diseño.
- Regla: las capacidades se expresan como resultados terminales macro; no crean prerrequisitos y subordinan las disciplinas contribuyentes a Analytics.
- Pendiente: detallar contenidos, programa-calendario, RAA, talleres, LAB, evidencias de evaluación y seguimiento de RAP/RAA.

## Preparación para auditoría

El documento permite trazar cada capacidad final a S04 y, en posgrado, al perfil vigente de la maestría. No afirma que el curso ya cumpla una auditoría completa ni materializa todavía la evidencia requerida por `S04.F11`.
