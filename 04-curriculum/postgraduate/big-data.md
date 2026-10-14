---
curso: "big-data"
nivel: "posgrado"
format_version: "0.5"
fecha: "2026-10-13"
---

# Analítica de grandes datos

## Propósito

Llevar los pasos analíticos (preparación, modelos y evaluación) a datos
cuyo volumen, velocidad o variedad exigen computación distribuida. El
curso responde cómo se obtiene una respuesta analítica cuando los datos
no caben o no llegan a tiempo en un solo equipo. El producto terminal es
un análisis ejecutado a escala sobre una plataforma distribuida, al
servicio de una pregunta analítica explícita, con sus decisiones de
particionamiento, costo y tiempo de respuesta justificadas.

## Identidad

- Pregunta: cómo se obtiene una respuesta analítica cuando los datos no
  caben o no llegan a tiempo en un solo equipo.
- Producto terminal: un análisis ejecutado a escala al servicio de una
  pregunta explícita, con sus decisiones de partición, costo y tiempo de
  respuesta justificadas; procesar grandes volúmenes sin pregunta no
  basta.
- Disciplinas contribuyentes: la computación distribuida, las bases de
  datos y la ingeniería de datos aportan plataformas y técnicas de
  ejecución.
- Riesgo: confundirse con un curso de infraestructura de grandes datos;
  se evita exigiendo que cada actividad parta de una pregunta analítica.

## Conocimientos requeridos

El curso los presupone y no los enseña.

- Programación básica en Python: estructuras de datos, funciones y
  manejo de tablas de datos.
- Consultas básicas en SQL: selección, filtros, uniones y agregaciones.
- Uso básico de la línea de comandos en Linux.

## Resultados de aprendizaje

- RA03, domina: Construye el conjunto de datos analítico a un volumen,
  variedad o velocidad que exige cómputo distribuido, con sus decisiones
  de partición, costo y tiempo de respuesta justificadas.

## Resultados del curso

### RC01. Construir el conjunto de datos a escala

- Enunciado: Construir un conjunto de datos analítico documentado a
  partir de fuentes cuyo volumen o variedad superan lo que un solo
  equipo puede procesar, adaptando las decisiones de limpieza e
  integración a esa escala.
- Resultados de aprendizaje: RA03.
- Evaluación: Conjunto de datos construido sobre una fuente de gran
  volumen o variedad, con las decisiones de adaptación a la escala
  justificadas [RA03].

### RC02. Diseñar un flujo de procesamiento distribuido

- Enunciado: Diseñar un flujo de procesamiento distribuido que prepare
  los datos del caso a un volumen que un solo equipo no puede procesar,
  documentando sus decisiones de partición y paralelización.
- Resultados de aprendizaje: RA03.
- Evaluación: Flujo de procesamiento distribuido ejecutado sobre una
  muestra representativa del caso, con sus decisiones de partición y
  paralelización documentadas [RA03].

### RC03. Justificar el costo y el tiempo de respuesta de la ejecución a escala

- Enunciado: Justificar, para el análisis ejecutado a escala, el costo
  y el tiempo de respuesta frente a alternativas de particionamiento y
  de recursos de cómputo.
- Resultados de aprendizaje: RA03.
- Evaluación: Comparación de al menos dos estrategias de ejecución a
  escala, con su costo y su tiempo de respuesta medidos y la elección
  justificada [RA03].

## Alcance

- Los grandes datos por sí solos no son analítica: cada actividad del
  curso parte de una pregunta analítica que el procesamiento a escala
  responde.
- Con `descriptiva` y `predictiva`: el método descriptivo o predictivo es
  el mismo; este curso se ocupa de ejecutarlo a escala, no de enseñarlo de
  nuevo.
- Con `productos`: operar de forma continua un flujo a escala, con su
  orquestación y su monitoreo, le corresponde a productos.
- Queda fuera la administración de la infraestructura de almacenamiento y
  de las plataformas de procesamiento distribuido.
