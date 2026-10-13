# Dominio: analítica

Versión 0.7 (borrador)

Este archivo define el campo al que se aplican los criterios de
`criteria.md`.

## Campo

Analítica.

## Subcampos

- Analítica descriptiva.
- Analítica diagnóstica.
- Analítica predictiva.
- Analítica prescriptiva.
- Analítica de grandes datos (*Big Data Analytics*).
- Productos de datos.
- Ingeniería de datos para la analítica.

Los cuatro primeros subcampos se distinguen por la pregunta que responden.
La analítica de grandes datos se distingue de otra manera: sus pasos
analíticos son los mismos (limpieza, modelos, evaluación), pero exige
competencias propias (por ejemplo, Linux y computación distribuida) y
herramientas propias (por ejemplo, Spark). Como este método selecciona
evidencia sobre competencias, esa diferencia justifica tratarla como
subcampo.

Los grandes datos por sí solos no son necesariamente analítica. Un documento
sobre grandes datos que no los pone al servicio de una pregunta analítica se
trata como vecino.

En la historia del campo, la analítica de grandes datos aparece hacia 2011,
cuando los métodos analíticos tradicionales empiezan a ejecutarse sobre
plataformas distribuidas, y converge con el aprendizaje automático en la
analítica moderna de 2010 a 2015 (véase
`design/benchmarks-md/literature-derived/conf-origen-y-evolucion-business-analytics.md`).

Los productos de datos también se distinguen por competencias: convierten un
análisis en un producto usable y mantenido (tableros, aplicaciones de datos,
API, modelos desplegados). Exigen competencias como despliegue, control de
versiones, diseño para el usuario final y monitoreo. El monitoreo forma parte
del subcampo y cubre el desempeño y la deriva de los modelos, la calidad de
los datos y el uso del producto. Las prácticas operativas aplicadas a datos y
modelos (MLOps, DataOps, integración y despliegue continuos de modelos y
*pipelines*) también forman parte del subcampo.

La ingeniería de datos para la analítica también se distingue por
competencias: obtener, integrar y preparar los datos que una pregunta
analítica necesita. Comprende la adquisición y la integración de fuentes, SQL
y el modelado de datos para el análisis, los *pipelines* que alimentan
análisis, modelos y productos de datos, y la calidad de los datos. Sin esa
base no hay producto analítico confiable, por eso forma parte del campo y no
solo de un vecino.

## Tendencia emergente: IA generativa y agéntica en la analítica

El uso de modelos fundacionales, IA generativa e IA agéntica como
herramientas del trabajo analítico forma parte del campo. Es una dimensión
transversal a todos los subcampos, no un subcampo nuevo. Incluye, por
ejemplo, asistentes que ayudan a formular, explorar y explicar análisis;
agentes que obtienen y preparan datos, ejecutan modelos o generan reportes;
y modelos de lenguaje integrados en productos de datos. Exige competencias
propias, como especificar tareas para un modelo, verificar y auditar sus
resultados, y gobernar su uso.

La IA como disciplina autónoma (diseño, entrenamiento y teoría de los
modelos) sigue siendo vecino. Un documento entra por esta tendencia cuando
pone la IA al servicio de una pregunta o un producto analítico.

## Precursores

- **Inteligencia de negocios**.
- **Minería de datos**.

La minería de datos se incorporó después de advertir que precede
históricamente a la analítica predictiva. Los documentos de precursores se
registran con rol `precursor`.

## Vecinos

- Inteligencia artificial y aprendizaje automático.
- Ingeniería de datos como disciplina autónoma: plataformas e
  infraestructura de datos tratadas como fin en sí mismas.
- Grandes datos por sí solos, incluida su infraestructura (almacenamiento y
  plataformas de procesamiento distribuido).
- Estadística.
- Ingeniería de software, incluidos DevOps genérico y la infraestructura en
  la nube, salvo cuando se trata como parte de la entrega de un producto
  analítico.

Un documento de un campo vecino se incluye solo cuando trata ese campo como
parte del trabajo analítico. Un documento que lo trata como disciplina
autónoma no es pertinente.

> Valor por defecto pendiente de confirmación por david.

## Evidencia de mercado

Los informes de industria y los perfiles de cargo son evidencia válida de la
práctica profesional, siempre que cumplan los criterios de `criteria.md`.

## Versión y cambios

- 0.1 (2026-10-13): borrador inicial.
- 0.2 (2026-10-13): se agrega la analítica de grandes datos como dimensión
  transversal; los grandes datos por sí solos y su infraestructura quedan
  como vecino.
- 0.3 (2026-10-13): la analítica de grandes datos pasa a ser un subcampo,
  diferenciado por competencias y herramientas, no por la pregunta que
  responde.
- 0.4 (2026-10-13): se agregan los productos de datos como subcampo,
  diferenciado por competencias e incluido el monitoreo; la ingeniería de
  software queda como vecino.
- 0.5 (2026-10-13): se agrega la ingeniería de datos para la analítica como
  subcampo, diferenciado por competencias (adquisición e integración, SQL y
  modelado, *pipelines*, calidad); la ingeniería de datos como disciplina
  autónoma sigue como vecino.
- 0.6 (2026-10-13): se agrega la IA generativa y agéntica al servicio del
  trabajo analítico como tendencia emergente y transversal; la IA como
  disciplina autónoma sigue como vecino.
- 0.7 (2026-10-13): se explicita que MLOps, DataOps y la integración y el
  despliegue continuos de modelos y *pipelines* forman parte de los productos
  de datos (ampliación). DevOps genérico y la infraestructura en la nube se
  nombran dentro del vecino ingeniería de software, donde ya estaban; esto
  aclara y no restringe el dominio.
