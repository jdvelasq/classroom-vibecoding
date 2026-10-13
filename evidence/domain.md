# Dominio: analítica

Versión 0.4 (borrador)

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
versiones, monitoreo y diseño para el usuario final.

## Precursores

- **Inteligencia de negocios**.
- **Minería de datos**.

La minería de datos se incorporó después de advertir que precede
históricamente a la analítica predictiva. Los documentos de precursores se
registran con rol `precursor`.

## Vecinos

- Inteligencia artificial y aprendizaje automático.
- Ingeniería de datos.
- Grandes datos por sí solos, incluida su infraestructura (almacenamiento y
  plataformas de procesamiento distribuido).
- Estadística.
- Ingeniería de software, salvo cuando se trata como parte de la entrega de
  un producto analítico.

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
  diferenciado por competencias; la ingeniería de software queda como
  vecino.
