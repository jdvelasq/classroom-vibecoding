# Diseño de contenido: Fundamentos de data para analítica

## Propósito y alcance

Curso optativo de pregrado sobre datos accesibles, confiables, comprensibles y reproducibles para finalidades analíticas. No es prerrequisito ni un curso de Data Engineering o Big Data.

## Al finalizar el curso, el estudiante es capaz de…

1. **derivar requisitos de datos a partir de una pregunta analítica, identificando unidades, variables, granularidad, fuentes y restricciones** — `data.C01`; S04.F01, S04.F02, S04.F04.
2. **obtener, estructurar, consultar, integrar y transformar datos de forma justificable para análisis** — `data.C02`; S04.F04, S04.F10.
3. **evaluar calidad, procedencia, faltantes, inconsistencias y sesgos que afectan la evidencia** — `data.C03`; S04.F04, S04.F05, S04.F08.
4. **documentar datos, transformaciones, decisiones y límites para que el análisis sea reproducible y responsable** — `data.C04`; S04.F07, S04.F08.
5. **reconocer bases de datos y herramientas como habilitadores de Analytics, no como identidad curricular** — `data.C05`; S04.F03, S04.F10.

Estas son capacidades terminales macro: no fijan semanas, herramientas, algoritmos, talleres, LAB ni instrumentos de evaluación.

## Fronteras de contenido

No cubre arquitectura empresarial, operaciones distribuidas, pipelines productivos, MLOps ni la construcción completa de modelos.

## Trazabilidad directa

| Identificador | Rol | S04 | Razón de asignación |
|---|---|---|---|
| `data.C01` | Principal | S04.F01, S04.F02, S04.F04 | Datos guiados por finalidad analítica. |
| `data.C02` | Principal | S04.F04, S04.F10 | Acceso y preparación funcional. |
| `data.C03` | Principal | S04.F04, S04.F05, S04.F08 | Calidad y límites. |
| `data.C04` | Principal | S04.F07, S04.F08 | Documentación y responsabilidad. |
| `data.C05` | Contextual | S04.F03, S04.F10 | Frontera con ingeniería. |

## Trazabilidad inversa

| Hallazgo S04 | Capacidades del curso |
|---|---|
| `S04.F01` | `data.C01`, `data.C02`, `data.C03`, `data.C04` |
| `S04.F02` | `data.C01`, `data.C03`, `data.C04` |
| `S04.F03` | `data.C05` |
| `S04.F04` | `data.C01`, `data.C02`, `data.C03`, `data.C04` |
| `S04.F05` | `data.C01`, `data.C02`, `data.C03` (habilitación de la evidencia; no enseñanza de análisis descriptivo) |
| `S04.F06` | `data.C01`, `data.C03` (requisitos y límites de datos para seleccionar métodos; no enseñanza de métodos) |
| `S04.F07` | `data.C04` (documentación de datos y límites; no comunicación integral de hallazgos) |
| `S04.F08` | `data.C03`, `data.C04` |
| `S04.F09` | `data.C01`, `data.C02`, `data.C03`, `data.C04` |
| `S04.F10` | `data.C02`, `data.C05` |
| `S04.F11` | Gobernanza del diseño y de esta trazabilidad; no corresponde a una capacidad terminal del estudiante. |


## Registro de construcción

- Tarea: `S05`; curso: `data`; fecha: 2026-09-29.
- Insumos: `design/synthesis/s04-synthesis.md` (SHA-256 `ba832f2c5a6bea26256b5efbb264408dc4034e4b183aefddd0b7efb583ba22b2`).
- Hallazgos considerados: `S04.F01`–`S04.F11`; asignados: `S04.F01`–`S04.F10` a capacidades y `S04.F11` a la gobernanza del diseño.
- Regla: las capacidades se expresan como resultados terminales macro; no crean prerrequisitos y subordinan las disciplinas contribuyentes a Analytics.
- Pendiente: detallar contenidos, programa-calendario, RAA, talleres, LAB, evidencias de evaluación y seguimiento de RAP/RAA.

## Preparación para auditoría

El documento permite trazar cada capacidad final a S04 y, en posgrado, al perfil vigente de la maestría. No afirma que el curso ya cumpla una auditoría completa ni materializa todavía la evidencia requerida por `S04.F11`.
