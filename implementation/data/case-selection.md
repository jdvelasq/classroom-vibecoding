# Decisiones de selección de casos — Fundamentos de data para analítica

Este registro conserva decisiones que orientan la selección y revisión de
casos para los talleres presenciales del curso. Complementa la trazabilidad
por capacidades de `traceability.yaml`; no la reemplaza ni aprueba un taller.

## Criterio curricular

Los casos se seleccionan porque fortalecen una capacidad de Analytics:
formular requisitos de datos desde una pregunta, obtener y preparar datos,
examinar calidad y procedencia, o documentar decisiones reproducibles.
Las bases de datos y las técnicas de procesamiento son habilitadores, no la
identidad del curso. No se incorporan casos únicamente para enseñar una
tecnología, una arquitectura empresarial o más etapas de un pipeline.

El criterio operativo es incorporar un caso cuando añade una capacidad o una
diversidad de dominio analítico que no esté cubierta de manera suficiente por
los casos existentes. Se prefieren fuentes trazables del `catalog/`,
`datalabs/` o DataCamp y se preservan sus condiciones de acceso, procedencia y
uso en clase.

## Bloque de MapReduce y modelo clave–valor

- `P519_mapreduce_operators` introduce las operaciones genéricas y hace
  visibles sus entradas y salidas con un extracto pequeño del mismo dominio.
- `P520_mapreduce_drivers` usa el registro de turnos de conductores para una
  agregación clave–valor por `driverId`: horas, millas y número de semanas.
- `P521_mapreduce_drivers_join` continúa con el mismo dominio y añade la unión
  de esas métricas con los datos maestros de conductores.
- Los casos presentan primero la pregunta y su SQL como especificación
  declarativa; después aplican las operaciones ya introducidas en P519.
- Las operaciones locales con nombres como `mapPairs` o `reduceByKey` sirven
  para explicar el modelo de cómputo. No introducen PySpark, RDD, Pig, Hive ni
  la operación de plataformas distribuidas como contenido del curso.
- En este bloque, el SQL debe permanecer deliberadamente acotado: agregación
  por clave en P520; unión, agregación y ordenamiento sencillo en P521. SQL
  avanzado pertenece a la secuencia SQL, no a la explicación de MapReduce.

## Casos externos evaluados

| Fuente o caso | Decisión vigente | Motivo curricular |
|---|---|---|
| Lahman Baseball (`catalog/s14-hortonworks-hdp/hcatalog-basic-pig-and-hive-commands/`) | Mantener como variante reutilizable o extensión futura; no crear otro taller obligatorio ahora. | Aporta una alternativa real para agregación por jugador y unión con datos maestros, pero duplica la progresión técnica de conductores. |
| Clickstream de retail (`catalog/s14-hortonworks-hdp/visualizing-website-clickstream-data/`) | Candidato prioritario para enriquecer o reemplazar en el futuro `P529_eventos`, sujeto a verificar acceso y condiciones de uso. | Puede añadir recorridos, conversión y secuencias de eventos: diversidad analítica que no cubren los casos actuales de Superstore y Scopus. |
| HVAC y sensores (`catalog/s14-hortonworks-hdp/how-to-analyze-machine-and-sensor-data/`) | Mantener únicamente como candidato condicionado. | Es potencialmente útil para datos temporales y operaciones, pero faltan condiciones verificadas de origen y uso. |
| Operación de fábrica y enriquecimiento de vehículos (`catalog/s13-cloudera-tutorial-assets/`) | Mantener en el catálogo; no añadir al núcleo actual. | Son sintéticos o con condiciones de uso y se solapan con integración, warehouse, ETL y ELT de Superstore. |
| Inventario de repuestos de vehículos (`catalog/s13-cloudera-tutorial-assets/`) | Reservar para Predictiva. | Su finalidad principal es pronóstico, no Fundamentos de data para analítica. |

## Regla de revisión futura

Antes de promover un caso del catálogo a un taller, verificar: aporte
incremental a las capacidades del curso, pregunta analítica auténtica cuando
corresponda, disponibilidad y procedencia de los datos, restricciones de uso,
y encaje en una secuencia autocontenida. Un caso que solo repite la técnica de
un taller existente permanece como variante o referencia del catálogo.
