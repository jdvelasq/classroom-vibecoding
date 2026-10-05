# Diseño de contenido: Fundamentos de data para analítica

## Propósito y alcance

Curso optativo de pregrado sobre datos accesibles, confiables, comprensibles y reproducibles para finalidades analíticas. Prepara a quien hará analítica o *data science for business* para intervenir en el origen y la organización de los datos: saber de dónde vienen, qué significan y con qué calidad llegan, prepararlos e integrarlos, y organizarlos en las agregaciones y modelos que alimentan el análisis y las herramientas de BI. No forma al ingeniero de datos responsable de que las bases entreguen datos de forma oportuna y eficiente (rendimiento, operación y administración de bases de datos).

Se ubica a la mitad entre la ingeniería de datos y la analítica. Sus talleres son prácticos y muestran cómo se hace profesionalmente: ingesta, ETL/ELT, modelado y agregación para BI, formatos y particionamiento, e introducción conceptual al procesamiento distribuido. Cuando un taller calcula sobre datos, plantea la pregunta analítica que ese procesamiento resuelve.

Es optativo y no todos los estudiantes lo ven: ningún otro curso depende de él y no es prerrequisito. Para buena parte de sus estudiantes puede ser la única formación en *business intelligence*; por eso trata BI de forma completa, aunque se solape con Analítica descriptiva, que pertenece a otro programa y población.

## Al finalizar el curso, el estudiante es capaz de…

1. **derivar requisitos de datos a partir de una pregunta analítica, identificando unidades, variables, granularidad, fuentes y restricciones** — `data.C01`; S04.F01, S04.F02, S04.F04.
2. **obtener, estructurar, consultar, integrar, transformar y agregar datos de forma justificable para análisis, incluidos los modelos y agregaciones que alimentan las herramientas de BI** — `data.C02`; S04.F04, S04.F10.
3. **evaluar calidad, procedencia, faltantes, inconsistencias y sesgos que afectan la evidencia** — `data.C03`; S04.F04, S04.F05, S04.F08.
4. **documentar datos, transformaciones, decisiones y límites para que el análisis sea reproducible y responsable** — `data.C04`; S04.F07, S04.F08.
5. **reconocer bases de datos, flujos ETL/ELT, procesamiento distribuido y herramientas como habilitadores de Analytics, no como identidad curricular** — `data.C05`; S04.F03, S04.F10.

Estas son capacidades terminales macro: no fijan semanas, herramientas, algoritmos, talleres, LAB ni instrumentos de evaluación.

## Fronteras de contenido

Cubre prácticas de ingeniería de datos y de BI en la medida en que permiten intervenir en el origen y la organización de los datos para analizar. No cubre:

- rendimiento, operación ni administración de bases de datos;
- plataformas de procesamiento distribuido (Spark, Hadoop u otras): el procesamiento distribuido se introduce de forma conceptual, emulando sus operaciones en Python;
- la operación productiva de capacidades analíticas según DataOps/MLOps (pruebas de datos y código como reglas de producción, orquestación, monitoreo, despliegue), que es de Productos de datos;
- arquitectura empresarial de datos;
- la construcción completa de modelos analíticos.

Se acepta solapamiento con Analítica descriptiva (BI) y con Productos de datos (ETL/ELT) porque son programas académicos y poblaciones distintas.

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


## Auditoría de identidad del curso

- **Pregunta y producto terminal:** ¿qué datos documentados y aptos para un
  propósito analítico están disponibles, de dónde vienen y cómo están
  organizados? El producto es un conjunto de datos preparado, evaluado,
  trazable y organizado para el análisis o para BI; no una explicación,
  predicción, política ni una capacidad operada en producción.
- **Disciplinas contribuyentes:** bases de datos, programación y prácticas de
  ingeniería aportan acceso, transformación y documentación funcionales.
- **Frontera:** se ubica entre la ingeniería de datos y la analítica. Usa
  prácticas de ingeniería de datos y de BI para habilitar evidencia, sin
  convertirse en administración de bases de datos, capacitación en una
  plataforma distribuida ni DataOps/MLOps.

## Registro de construcción

- Tarea: `S05`; curso: `data`; fecha: 2026-09-29.
- Insumos: `design/synthesis/s04-synthesis.md` (SHA-256 `ba832f2c5a6bea26256b5efbb264408dc4034e4b183aefddd0b7efb583ba22b2`).
- Hallazgos considerados: `S04.F01`–`S04.F11`; asignados: `S04.F01`–`S04.F10` a capacidades y `S04.F11` a la gobernanza del diseño.
- Regla: las capacidades se expresan como resultados terminales macro; no crean prerrequisitos y subordinan las disciplinas contribuyentes a Analytics.
- Revisión 2026-10-05: propósito, capacidades `data.C02` y `data.C05`, fronteras y auditoría ajustados según la entrevista con el profesor (curso entre ingeniería de datos y analítica; BI completo; procesamiento distribuido conceptual en Python; ETL/ELT práctico; solapamientos aceptados entre programas). La trazabilidad a S04 no cambia.
- Pendiente: detallar contenidos, programa-calendario, RAA, talleres, LAB, evidencias de evaluación y seguimiento de RAP/RAA.

## Preparación para auditoría

El documento permite trazar cada capacidad final a S04 y, en posgrado, al perfil vigente de la maestría. No afirma que el curso ya cumpla una auditoría completa ni materializa todavía la evidencia requerida por `S04.F11`.
