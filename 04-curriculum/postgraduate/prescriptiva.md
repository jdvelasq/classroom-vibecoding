---
curso: "prescriptiva"
nivel: "posgrado"
format_version: "0.5"
fecha: "2026-10-13"
---

# Analítica prescriptiva

## Propósito

Diseñar, validar y gobernar políticas de decisión para decisiones
operativas recurrentes. El curso responde qué acción recurrente debe
tomarse bajo cuáles objetivos, restricciones, salvaguardas, excepciones y
mecanismo de revisión. El producto terminal es una política que
transforma el contexto observable y los datos disponibles en una acción
factible, con una autoridad de decisión definida, validada frente a
líneas base y escenarios antes de operarla, y con el seguimiento que
indica cuándo revisarla, suspenderla o recalibrarla. La automatización no
es obligatoria: una política puede ejecutar una acción de bajo riesgo o
producir una recomendación que requiere aprobación humana, y en ambos
casos declara su cadencia y su necesidad de respuesta.

## Identidad

- Pregunta: qué acción recurrente debe tomarse bajo cuáles objetivos,
  restricciones, salvaguardas, excepciones y mecanismo de revisión.
- Producto terminal: una política computable y gobernada para una
  decisión operativa recurrente; un modelo, una frontera de Pareto, una
  simulación o un árbol de decisión aislados no bastan.
- Disciplinas contribuyentes: la optimización, la simulación, los modelos
  predictivos, la estadística y las bases de datos aportan evidencia,
  factibilidad o validación a la política.
- Riesgo: confundirse con un curso abreviado de investigación de
  operaciones, o que una actividad termine en una solución matemática sin
  una política operable y monitoreable; se evita exigiendo que cada
  actividad termine en una política.

## Conocimientos requeridos

El curso los presupone y no los enseña.

- Programación básica en Python: estructuras de datos, funciones y
  manejo de tablas de datos.
- Álgebra lineal y cálculo básicos.
- Probabilidad básica: distribuciones y valor esperado.

## Resultados de aprendizaje

- RA01, domina: Formula y sustenta ante un panel el problema de decisión
  completo que da origen a la política.
- RA02, domina: Diseña la política de decisión con salvaguardas, autoridad
  humana, cadencia y seguimiento.

## Resultados del curso

### RC01. Formular el contrato de la política

- Enunciado: Formular una decisión operativa recurrente como el contrato
  de una política, con su contexto observable, su responsable, su
  cadencia, sus acciones, sus objetivos y sus restricciones, y
  sustentarlo ante los interesados.
- Resultados de aprendizaje: RA01, RA02.
- Evaluación: Contrato de política sustentado ante un panel, con el
  registro de los acuerdos [RA01; RA02].

### RC02. Diseñar y validar la política

- Enunciado: Diseñar una política que lleve el contexto observado a una
  acción factible y validarla frente a la práctica actual, escenarios y
  análisis de sensibilidad antes de operarla.
- Resultados de aprendizaje: RA02.
- Evaluación: Política con su modelo de soporte y su validación sobre
  escenarios históricos o simulados [RA02].

### RC03. Gobernar la política en operación

- Enunciado: Establecer la autoridad humana, las salvaguardas, las
  excepciones y los indicadores de seguimiento de una política, con los
  umbrales que obligan a revisarla o suspenderla.
- Resultados de aprendizaje: RA02.
- Evaluación: Plan de gobierno de la política, con qué decide una
  persona, qué se automatiza y cuándo se revisa [RA02].

## Alcance

- Con `predictiva`: predictiva construye, valida e interpreta una
  estimación; prescriptiva la usa como evidencia para definir y validar
  una política. Pronosticar el pico de demanda es predictiva; definir
  cuándo ampliar capacidad, comprar recursos o escalar una alerta es
  prescriptiva.
- Con `productos`: productos integra, despliega, mantiene y observa la
  capacidad que ejecuta la política; prescriptiva define su semántica, sus
  restricciones, sus excepciones, su autoridad y su validación. Una
  actividad prescriptiva demuestra una política operable sin convertirse
  en arquitectura o despliegue de software.
- Queda fuera un currículo abreviado de investigación de operaciones, la
  teoría avanzada de algoritmos y la implementación de *solvers*. La
  optimización, la simulación, el análisis multicriterio, los árboles de
  decisión y las estimaciones predictivas entran como soporte de la
  política: un modelo aislado, una frontera de Pareto o un resultado de
  simulación no bastan como producto terminal.
