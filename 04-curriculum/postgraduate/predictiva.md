---
curso: "predictiva"
nivel: "posgrado"
format_version: "0.5"
fecha: "2026-10-13"
---

# Analítica predictiva

## Propósito

Anticipar resultados mediante modelos validados, interpretables y útiles
para una decisión. El curso responde qué resultado futuro o no observado
se estima, para quién, en qué horizonte y con qué incertidumbre. El
producto terminal es una estimación validada fuera de la muestra de
entrenamiento, con su línea base, su incertidumbre, sus supuestos y las
consecuencias de usarla. El curso se apoya en KDD y minería de datos, que
aportan metodologías y problemas anteriores a la analítica y aún vigentes;
el aprendizaje automático y el aprendizaje profundo aportan modelos cuando
son adecuados para la tarea.

## Identidad

- Pregunta: qué resultado futuro o no observado se estima, para quién, en
  qué horizonte y con qué incertidumbre.
- Producto terminal: una estimación validada e interpretable, útil para
  una decisión; no una política de acción ni una plataforma de operación,
  y tampoco un modelo con buen desempeño técnico sin línea base ni
  consecuencias de uso.
- Disciplinas contribuyentes: KDD, minería de datos, aprendizaje
  automático, aprendizaje profundo, estadística, simulación y modelos
  mecanísticos aportan métodos según el fenómeno, no como una taxonomía
  que organice el curso.
- Riesgo: confundirse con un curso abreviado de aprendizaje automático;
  se evita eligiendo cada método por la tarea predictiva y la dinámica del
  fenómeno.

## Conocimientos requeridos

El curso los presupone y no los enseña.

- Programación básica en Python: estructuras de datos, funciones y
  manejo de tablas de datos.
- Probabilidad y estadística básicas: distribuciones, valor esperado y
  varianza.
- Álgebra lineal básica: vectores, matrices y sus operaciones.

## Resultados de aprendizaje

- RA01, desarrolla: Formula el problema predictivo con horizonte, línea
  base y costo de los errores y lo sustenta ante el profesor.
- RA03, desarrolla: Prepara los datos del caso para predecir, evitando la
  fuga de información y documentando sus sesgos y límites.
- RA06, domina: Construye y valida el modelo predictivo del caso,
  justificado frente a alternativas.
- RA07, introduce: Documenta el modelo y especifica los indicadores con
  los que se monitorearía su desempeño y se decidiría revisarlo.

## Resultados del curso

### RC01. Formular el problema predictivo del caso

- Enunciado: Formular un problema predictivo con su horizonte, su línea
  base y el costo de sus errores, y sustentarlo frente al profesor sobre
  un caso preparado.
- Resultados de aprendizaje: RA01.
- Evaluación: Planteamiento del problema predictivo sustentado, con
  horizonte, línea base y costo de los errores [RA01].

### RC02. Construir y validar el modelo predictivo

- Enunciado: Construir y validar un modelo que estime el resultado del
  caso predictivo, con su desempeño medido fuera de la muestra de
  entrenamiento.
- Resultados de aprendizaje: RA06.
- Evaluación: Modelo entrenado y validado sobre un conjunto de prueba,
  con su desempeño medido [RA06].

### RC03. Seleccionar y justificar el modelo frente a alternativas

- Enunciado: Seleccionar, entre varias familias de modelo construidas
  para el caso, la más adecuada, y justificarla frente a su exactitud y
  su interpretabilidad.
- Resultados de aprendizaje: RA06.
- Evaluación: Informe de selección del modelo que compara al menos dos
  alternativas y justifica la elegida [RA06].

### RC04. Preparar los datos para predecir

- Enunciado: Preparar los datos de un caso predictivo sin fuga de
  información, con la representación de las variables justificada y sus
  sesgos y límites documentados.
- Resultados de aprendizaje: RA03.
- Evaluación: Conjunto de datos de entrenamiento y prueba con la
  verificación de que no hay fuga de información y el registro de sus
  sesgos y límites [RA03].

### RC05. Interpretar la predicción y prever su seguimiento

- Enunciado: Interpretar el desempeño, la incertidumbre y las
  consecuencias de uso de una predicción, y especificar los indicadores
  con los que se monitorearía para decidir cuándo revisarla.
- Resultados de aprendizaje: RA06, RA07.
- Evaluación: Ficha del modelo con su desempeño, su incertidumbre, sus
  límites de uso y los indicadores de monitoreo propuestos [RA06; RA07].

## Alcance

- La frontera se define por la pregunta y el producto, no por la familia
  del modelo. Un método entra porque resuelve una tarea predictiva según
  la dinámica y los supuestos del fenómeno, no para cubrir una taxonomía
  de algoritmos.
- Con `prescriptiva`: cuando una estimación se usa para elegir una acción
  bajo objetivos, restricciones y salvaguardas, el producto le corresponde
  a prescriptiva. Estimar el pico de demanda de camas y su incertidumbre
  es predictiva; decidir capacidad, compras o intervenciones es
  prescriptiva.
- Con `productos`: operar la estimación de forma confiable, desplegarla y
  monitorearla en producción le corresponde a productos.
- Con `big-data`: cuando el volumen o la velocidad de los datos exigen
  computación distribuida, la ejecución a escala le corresponde a
  big-data.
- Queda fuera un curso enciclopédico de aprendizaje automático o de
  aprendizaje profundo.
