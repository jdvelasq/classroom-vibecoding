---
curso: "productos"
nivel: "posgrado"
format_version: "0.5"
fecha: "2026-10-13"
---

# Productos de datos

## Propósito

Convertir una capacidad descriptiva, predictiva o prescriptiva ya definida
en un producto reproducible, verificable, desplegable, observable, seguro,
recuperable y gobernable para sus usuarios. El curso responde cómo se hace
usable, confiable, mantenible y observable una capacidad analítica. El
producto terminal es una capacidad analítica versionada, con su contrato
operativo (usuarios, decisión que apoya, entradas, salidas, límites, nivel
de servicio y criterios de éxito), desplegada y monitoreada en su
desempeño, la calidad de sus datos y su uso. Las prácticas de DataOps y
MLOps entran cuando hacen operable una capacidad analítica concreta.

## Identidad

- Pregunta: cómo se opera de forma responsable una capacidad analítica
  para que sus usuarios la usen con confianza.
- Producto terminal: una capacidad analítica versionada, comprobable,
  desplegada y observable; no un modelo, una política o una arquitectura
  aislados.
- Disciplinas contribuyentes: DataOps, MLOps, ingeniería de software,
  ingeniería de datos, seguridad y gobierno aportan prácticas de
  operación al servicio de una capacidad con propósito y usuarios.
- Riesgo: confundirse con formación genérica en nube, herramientas o
  arquitectura empresarial; se evita exigiendo que cada actividad opere
  una capacidad analítica concreta.

## Conocimientos requeridos

El curso los presupone y no los enseña.

- Programación básica en Python: funciones, módulos y paquetes.
- Uso básico de la línea de comandos.
- Lectura de un análisis o de un modelo ya construido: el curso parte de
  una capacidad analítica dada por el caso.

## Resultados de aprendizaje

- RA02, desarrolla: Lleva la política a un producto que la ejecuta y
  registra sus resultados para revisarla.
- RA03, desarrolla: Valida con contratos y pruebas de calidad los datos
  que alimentan el producto en operación.
- RA07, domina: Despliega la solución analítica validada en el proceso
  de la organización y monitorea su desempeño en producción.

## Resultados del curso

### RC01. Llevar una política de decisión a un producto

- Enunciado: Llevar una política de decisión ya diseñada a un producto
  que la ejecute en un proceso de la organización y registre sus
  resultados para que pueda revisarse.
- Resultados de aprendizaje: RA02.
- Evaluación: Producto que ejecuta la política sobre casos del proceso,
  con el registro de resultados que permite revisarla [RA02].

### RC02. Desplegar la capacidad analítica como producto versionado

- Enunciado: Desplegar una capacidad analítica validada como un producto
  versionado, con su contrato operativo, en un proceso de la
  organización.
- Resultados de aprendizaje: RA07.
- Evaluación: Producto desplegado con su contrato operativo (usuarios,
  decisión que apoya, entradas, salidas, límites, nivel de servicio y
  criterios de éxito) y evidencia de su verificación en producción
  [RA07].

### RC03. Monitorear y decidir sobre el producto en producción

- Enunciado: Monitorear el desempeño, la calidad de los datos y el uso
  de un producto analítico en producción, y decidir, con indicadores
  propios, cuándo recalibrarlo o renovarlo.
- Resultados de aprendizaje: RA07.
- Evaluación: Tablero o informe de monitoreo con indicadores de
  desempeño, calidad de datos y uso, y la decisión tomada frente a ellos
  [RA07].

### RC04. Validar los datos que alimentan el producto

- Enunciado: Validar los datos que alimentan un producto analítico en
  operación mediante contratos de datos y pruebas de calidad
  automatizadas, frente al uso operativo previsto.
- Resultados de aprendizaje: RA03.
- Evaluación: Contratos y pruebas de calidad integrados al producto, con
  la evidencia de que detienen datos que incumplen el contrato [RA03].

## Alcance

- Con `descriptiva`, `predictiva` y `prescriptiva`: el curso no vuelve a
  formular, explorar, predecir ni prescribir el problema analítico; valida
  los datos, los modelos y los contratos frente al uso operativo previsto.
- Con `big-data`: la computación distribuida sobre grandes volúmenes le
  corresponde a big-data; productos la usa solo cuando el producto la
  necesita.
- Con `generativa`: los modelos de lenguaje integrados en un producto se
  operan aquí con las mismas exigencias de monitoreo y gobierno; su diseño
  como herramienta analítica le corresponde a generativa.
- Queda fuera la arquitectura empresarial de datos, la ingeniería de
  software general, la ingeniería de nube y la capacitación en una
  plataforma.
