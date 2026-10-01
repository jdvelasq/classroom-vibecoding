# Diseño de contenido: Productos de datos

## Propósito y alcance

Curso autónomo de posgrado que constituye la línea de **DataOps/MLOps para
capacidades analíticas**. Convierte una capacidad descriptiva, predictiva o
prescriptiva ya definida en un sistema reproducible, verificable, desplegable,
observable, seguro, recuperable y gobernable para sus usuarios. Se alinea con
el perfil de egreso vigente de la maestría.

## Perfil de ingreso y condición de entrada

El programa admite profesionales de trayectorias cuantitativas preferentes
(ingeniería, matemáticas, estadística, economía, administración, computación y
afines) y de otros campos que acrediten preparación equivalente en análisis
cuantitativo o manejo de información. La nivelación matemática, estadística o
computacional que eventualmente determine el Comité Asesor es una condición
institucional de acompañamiento; no es un prerrequisito entre estos seis cursos
ni autoriza a suponer una cohorte homogénea.


## Al finalizar el curso, el estudiante es capaz de…

1. **definir el contrato operativo de una capacidad analítica: usuarios, decisión que apoya, entradas, salidas, límites, nivel de servicio y criterios de éxito** — `productos.C01`; S04.F01, S04.F02.
2. **integrar datos, artefactos analíticos, interfaces y automatización como una capacidad reproducible, verificable y desplegable** — `productos.C02`; S04.F03, S04.F04, S04.F10.
3. **validar datos, modelos, contratos e insumos frente al uso operativo previsto, sin volver a enseñar el método analítico de origen** — `productos.C03`; S04.F05, S04.F06.
4. **habilitar el uso responsable de una capacidad mediante interfaces, control de acceso, revisión humana, documentación y retroalimentación operativa** — `productos.C04`; S04.F07, S04.F09.
5. **observar, gobernar, recuperar y mejorar una capacidad en operación mediante monitoreo, linaje, privacidad, costos, incidentes y retención** — `productos.C05`; S04.F08, S04.F10, S04.F11.

Estas son capacidades terminales macro: no fijan semanas, herramientas, algoritmos, talleres, LAB ni instrumentos de evaluación.

## Fronteras de contenido

No vuelve a formular, explorar, predecir ni prescribir el problema analítico:
esas son responsabilidades de Fundamentos, Descriptiva, Predictiva y
Prescriptiva. Tampoco es arquitectura empresarial de datos, Big Data
Analytics, ingeniería de software general, cloud engineering ni capacitación
en una plataforma. Selecciona prácticas de DataOps/MLOps solo cuando hacen
operable una capacidad analítica concreta.

## Trazabilidad directa

| Identificador | Rol | S04 | Razón de asignación |
|---|---|---|---|
| `productos.C01` | Principal | S04.F01, S04.F02 | Contrato operativo de la capacidad y de su uso. |
| `productos.C02` | Principal | S04.F03, S04.F04, S04.F10 | Integración, automatización y entrega confiable. |
| `productos.C03` | Recurrente | S04.F05, S04.F06 | Validación operacional de evidencia y artefactos. |
| `productos.C04` | Recurrente | S04.F07, S04.F09 | Interfaces, autoridad y retroalimentación en uso. |
| `productos.C05` | Principal | S04.F08, S04.F10, S04.F11 | Operación, gobierno, recuperación y mejora. |

## Trazabilidad inversa

| Hallazgo S04 | Capacidades del curso |
|---|---|
| `S04.F01` | `productos.C01` |
| `S04.F02` | `productos.C01` |
| `S04.F03` | `productos.C02` |
| `S04.F04` | `productos.C02` |
| `S04.F05` | `productos.C03` |
| `S04.F06` | `productos.C03` |
| `S04.F07` | `productos.C04` |
| `S04.F08` | `productos.C05` |
| `S04.F09` | `productos.C04` |
| `S04.F10` | `productos.C02`, `productos.C05` |
| `S04.F11` | `productos.C05` |

## Auditoría de identidad del curso

- **Pregunta y producto terminal:** ¿cómo se opera responsablemente una
  capacidad analítica para que sus usuarios puedan usarla con confianza? El
  producto terminal es una capacidad analítica versionada, comprobable,
  desplegable y observable; no un modelo, una política o una arquitectura
  aislados.
- **Disciplinas contribuyentes:** DataOps, MLOps, ingeniería de software,
  Data Engineering, seguridad y gobierno aportan prácticas de operación. No
  organizan el curso por sí mismas: cada práctica debe sostener una capacidad
  analítica con propósito, evidencia y usuarios identificables.
- **Riesgo de relabeling:** se evita al excluir formación genérica en cloud,
  herramientas o arquitectura empresarial y exigir que cada actividad opere
  una capacidad analítica concreta.


## Registro de construcción

- Tarea: `S05`; curso: `productos`; fecha: 2026-09-29.
- Insumos: `design/synthesis/s04-synthesis.md` (SHA-256 `ba832f2c5a6bea26256b5efbb264408dc4034e4b183aefddd0b7efb583ba22b2`) y `design/program-context/maestria-en-analitica.pdf` (SHA-256 `844fcddb2381c8ca245a8f6b34f8e73883e6475cc7518e5190d97cbbdfe17d7f`).
- Hallazgos considerados y asignados: `S04.F01`–`S04.F11`.
- Regla: las capacidades se expresan como resultados terminales macro; no crean prerrequisitos y subordinan las disciplinas contribuyentes a Analytics.
- Pendiente: detallar programa-calendario, RAA, talleres, LAB, evidencias de evaluación y seguimiento de RAP/RAA.

## Preparación para auditoría

El documento permite trazar cada capacidad final a S04 y, en posgrado, al perfil vigente de la maestría. No afirma que el curso ya cumpla una auditoría completa ni materializa todavía la evidencia requerida por `S04.F11`.
