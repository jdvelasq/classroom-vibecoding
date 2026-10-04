---
source: "design/benchmarks-pdf/literature-derived/dataops-06-definition.pdf"
source_sha256: a5f328f1469d348347e5b6b3d94d20ecc3520b821518c8c1f7d95cbccfd1a4e2
family: literature-derived
pages: 26
min_text_coverage: 0.848
pages_without_graphics: [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 23]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 26]"
  - "páginas con cobertura < 0.95: [5, 7]"
---
# ¿Qué es DataOps?

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## Definición de DataOps

Herramientas y métodos que combinan data
analytics, lean thinking, agile y DevOps asegurando

la calidad impecable del dato:


cosas

- Prácticas ágiles para asegurar que se trabaja en las


correctas que adicionan valor a las personas correctas.


- Lean thinking (pensamiento esbelto) para eliminar basura

y cuellos de botella, mejorar la calidad, monitorear flujos


de datos y hacer más baratos los datos a los


consumidores.


- DevOps establece una cultura de colaboración entre



Puntos clave:


- Adapta técnicas de DevOps, Agile, Lean thinking,


pero no las copia.


- No está limitado a DS/ML o Big Data y es aplicable a


cualquier producto de datos.

- Es una filosofía, no una herramienta.


- Es una aproximación operativa y por si solo no da


insights.




                                          - Producto o servicio que incorpora DS.
equipos históricamente aislados impulsando la eficiencia.

                                          - Resuelve un problema / da utilidad.

                                         - Combina datos con algoritmos para inferencia,









predicción u optimización.

- Es rápido, escalable y repetible.

- Es reproducible.

- Su uso es continuo

- Su monitoreo es constante

- iteración basada en la experimentación.

- Entrega retroalimentación para su mejora.

<!-- fin de página 2 -->

## Modelo de cascada para el desarrollo de software

Requisitos del

sistema y del




- Requiere planeamiento detallado y alto


grado de detalle

- Funciona mejor para requerimientos fijos y


bien entendidos desde el principio

- Los cambios generan ciclos de


replaneamiento y causa retrasos y

sobrecostos.

- Diferencia entre los ambientes de desarrollo,


prueba y productivo.

- Diferencias entre el hardware en la distintas


etapas.

- Falta de replicabilidad.

- Incapacidad para respuesta rapida a


cambios


Propuesto originalmente por WW Royce
en 1970, revisado por B. Boehm en
1980 y por I. Somerville en 1985



software



Análisis



Modelos, esquema y reglas de negocio


Arquitectura del software


Diseño


Desarrollo, pruebas e integración


Codificación


Pruebas


Descubrimiento de defectos



Instalación, migración,
soporte y mantenimiento



Operaciones



Valor diferido del proyecto



Big-Bang
Deliverable

Incertidumbre hasta este


punto

<!-- fin de página 3 -->

## Lean Manufacturing



Estación


de
trabajo



Materias

primas



Estación


de
trabajo



Productos

terminados



Tubería de procesamiento


   - Mejoramiento continuo de la calidad.


   - Eliminación de actividades que no agregan valor.


   - Cada estación de trabajo tiene una entrada bien


definida, un proceso claro y una salida establecida.


   - Uso de métricas de calidad **(control de procesos)** .


Requisitos Proceso Proceso Software




- Lógica del negocio — Valida supuestos sobre los


datos. Por ejemplo:


  - Validación de clientes.


  - Validación de datos.


- Entradas — Verifica las entradas en cada paso del


pipeline


  - Conteo


  - Conformidad


  - Historia


  - Balance


  - Consistencia temporal


  - Consistencia de la aplicación


  - Verificación de los campos


- Salidas — Verifica los resultados de una


operación.


  - Completitud


  - Verificación de rango



Data en bruto



Reportes,
Proceso Proceso modelos o

visualización


          - Tests para verificar los datos (lógica de negocio,


tipo de dato, outliers, tendencias, consistencia, …)


          - Tests para verificar los modelos (precisión,


degradación del modelo, …)

<!-- fin de página 4 -->

## Agile & Agile Manifesto

Sprint


Release


Release


Importancia de las

características
implementadas



Historias de usuario

- Requerimientos

- Criterios de aceptación




**Individuals and interactions** over processes and tools


**Working software** over comprehensive documentation


**Customer collaboration** over contract negotiation


**Responding to change** over following a plan



Sprint


Release



Metodología efectiva para productos


no secuenciales con requerimientos


que evolucionan rápidamente



Diseño



Pruebas



Sprint




 - Desarrollo basado en pruebas


 - Patrones de diseño


 - Refactorización de código


 - Integración y despliegue manual


Sprint



Pruebas



Desarrollo
Integración


Pruebas

<!-- fin de página 5 -->

## DevOps (Development + Operations)



Modelo de



Puesta en

Productivo



**Esquema clásico**

- Codificación

- Construcción (integración



Cascada Productivo - Codificación



Desarrollador



Profesional


IT/Ops






- Infraestructura diferente en cada


ambiente.


- Dificultad y lentitud para


homogeneizar hardware y software


a través de ambientes.


- Actualización constante del


software base.


- Dificultad para replicar errores


entre ambientes.




- Departamentos separados


- Métricas de éxito diferentes


- Actualización manual del codebase


- Verificación manual


- Despliegue lento del código (semanas o


meses)


- Dificultad en el manejo de versiones.


- Dificultades en el manejo de incidentes


- Dificultades en el manejo de servicios IT



de código).

- Pruebas de software

- Empaquetado

- Versionado

- Configuración de la


infraestructura

- Monitoreo








- ¿Cuánto tiempo requiere para llevar el código listo a


código ejecutando en producción?

- ¿Cada cuánto libera versiones?

- ¿Cuánto tiempo requiere para restablecer el servicio?

- ¿Qué porcentaje de cambios en el software resultan


en degradación del servicio que requiere intervención?

<!-- fin de página 6 -->

## DevOps (Development + Operations)

**Serverless Computing / Function as a Service (FaaS)**

Modelo de desarrollo que permite crear y ejecutar
aplicaciones y procesos sin entrar en contacto con el
servidor.


**Software as a Service (SaaS)**

El proveedor aloja y ejecuta las aplicaciones y las hace
accesibles a los clientes. El cliente solo es responsable
de los datos.


**Platform as a Service (PaaS)**

Alquiler de servidores y almacenamiento y conectividad
en la nube para desarrollo, e incluye sistema operativo,
lenguajes, bases de datos y demás herramientas.


**Infrastructure as a Service (IaaS)**

Alquiler de servidores y almacenamiento y conectividad
en la nube. El usuario es responsable de las VM,
sistema operativo, soporte a datos, etc.


Infraestructure

as Code



DevOps es un conjunto de prácticas destinadas a reducir el tiempo entre el
compromiso de un cambio en un sistema y el cambio que se coloca en la producción
normal, al tiempo que garantiza una alta calidad



Sprint


Release



Historias de usuario

- Requerimientos

- Criterios de aceptación


Sprint



Sprint




- Integración automática


- Desarrollo basado en


pruebas


- Patrones de diseño


- Refactorización de


código


- Versionado de código


- Despliegue automático



Release


Feedback



Sprint


Release


Feedback



Producto


liberado

<!-- fin de página 7 -->

## DataOps

Introduce colaboración y trabajo en equipo entre
los equipos de datos y los usuarios aumentando
eficiencia y efectividad


Introduce la separación en procesos y el control
de calidad entre ellos


Acelera el ciclo de desarrollo de software usando
automatización para la integración continua y el
despliegue automático



Agile


Lean
Thinking


DevOps



DataOps



Desafios:


- Requerimientos cambiantes


- Retrasos.


- Usuarios disgustados.


- Inflexibilidad


- Baja calidad


- Bajo ROI


- Características irrelevantes

<!-- fin de página 8 -->

## Pasos para implementar DataOps

Paso 1 — Adicione pruebas de lógica y de datos


Los datos están libres de problemas? La lógica del negocio es correcta? Las salidas son consistentes?


SQL


Ingestión Transformación Modelado Visualización Reporte


                                                   - Se verifica que cada cambio (datos, modelos y lógica)


no haga fallar el sistema.


                                                  - Hay al menos un test en cada paso.


                                                    - Se inician por tests simples y se aumenta complejidad.


                                                    - Los tests también puede alertar situaciones extrañas.


                                                  - Los tests automáticos continuamente monitores el


pipeline

<!-- fin de página 9 -->

## Pasos para implementar DataOps

Paso 2 — Use un sistema de control de versiones


Los datos están libres de problemas? La lógica del negocio es correcta? Las salidas son consistentes?


SQL


Ingestión Transformación Modelado Visualización Reporte


                                                     - Todos los elementos son básicamente código.


                                                         - El pipeline es determinístico con resultados reproducibles.


                                                         - El código controla todo el proceso.


                                                        - El sistema de control de versiones permite manejar los


cambios y revisiones del código.

<!-- fin de página 10 -->

## Pasos para implementar DataOps

Paso 3 — Bifurque y fusione


Producción

Característica B


Actualización


Bifurcación
Fusión


Característica A



Fusión


- Gestión de copias privadas para los equipos de trabajoFusión


- Cambios en paralelo sin afectar el código en producción.


- Cada equipo tiene control de su rama.


- Facilidad para experimentar, probar y rechazar características.

<!-- fin de página 11 -->

## Pasos para implementar DataOps

Paso 4 — Use múltiples ambientes


Copia de los datos


Producción



Característica B


Actualización



Fusión


- Cada miembro tiene sus propias herramientas de desarrollo.


- El control de versiones permite manejar una copia privada del


código en productivo.


- Cada miembro debe tener una copia de los datos que requiere.


- La separación en ambientes permite gestionar cambios en el


código y en los datos



Bifurcación
Fusión


Característica A


Copia de los datos

<!-- fin de página 12 -->

## Pasos para implementar DataOps

Paso 5 — Reuso y contenerización




- Contenerización del ambiente de desarrollo


- Contenerización de las aplicaciones



Data en bruto



Reportes,
Proceso Proceso Proceso Proceso modelos o

visualización




- La separación en pequeños componentes permite


la reutilización de código.


- Cada componente puede tener una lógica


compleja y estar escrito en un lenguaje diferente y


requerir un stack de software distinto.


- Es difícil llevar un componente de una máquina o


ambiente a otro



App A


bins/lib



Docker es un proyecto de código abierto para el
despliegue de aplicaciones dentro de
contenedores para la virtualización de
aplicaciones


Contenedores
Pueden ser
múltiples imágenes
de la misma App



App C


bins/lib


Sistema

Operativo

Invitado



Máquinas

virtuales


App B


bins/lib



App A


bins/lib



App B


bins/lib


Docker Engine



bins/lib

Sistema Sistema
Operativo Operativo



App C



Docker

Images



Sistema

Operativo



Invitado



Invitado


Hypervisor



Sistema Operativo Anfitrión


Infraestructura


- Balanceo de carga

- Gestión de memoria

- Gestión de contendores



Sistema Operativo Anfitrión


Infraestructura

<!-- fin de página 13 -->

## Pasos para implementar DataOps

Paso 6 — Parametrización del procesamiento


¿Cuál versión de datos debe usarse?


Versión 1


Versión 2



Proceso



¿A cuál ambiente deben ir


los resultados?


Producción



¿Cuales procesos deben



?



Reportes,
Proceso Proceso modelos o

?

aplicarse sobre los datos?

visualización



Proceso modelos o
? ?

aplicarse sobre los datos?

visualización

Testing



aplicarse sobre los datos?



?



Versión 3


Versión 4



Proceso Proceso


Parametrización por fuera del código

         - El pipeline incluye las decisiones en la lógica.

         - Permite el ajuste a diferentes condiciones de ejecución.

<!-- fin de página 14 -->

## Pasos para implementar DataOps

Paso 7 — Trabajar sin miedo o heroísmo


**Heroísmo** : Trabajo fuera de
horario y fines de semana.



CALIDAD



**Escenarios desastrosos** :

      - Despliegue de cambios que dañan


los sistemas productivos.

      - Entrega de datos de poca calidad a


los usuarios.


**Miedo** : Ausencia de confianza en

que los resultados sean correctos

o los cambios funcionen

correctamente.


**Innovation**

**Pipeline**



DATA PRODUCCION VALOR


Ingestión Transformación Modelado Visualización Reporte



**Value**
**Pipeline**


CALIDAD


PRODUCCION


DESARROLLO


IDEA



Los tests sobre los datos en cada paso

garantizan la calidad de la salida


CALIDAD


**Value**
DATA PRODUCCION VALOR
**Pipeline**


DESARROLLO


IDEA


**Innovation**
**Pipeline**

<!-- fin de página 15 -->

## Diferencias entre DevOps y DataOps

Proceso



DevOps


DataOps



Desarrollo y Despliegue


CI CD


Desarrollo Construcción Prueba Despliegue Ejecución


Sandbox Desarrollo Orquestación Prueba Despliegue Orquestación Monitoreo



Innovation


Pipeline



Data

Pipeline





Doble
orquestación


Factores Humanos


Ingenieros de software, confortables con código

y complejidad de multiples lenguajes

herramientas y hardware/software


Científicos de datos, ingenieros, analistas que

quieren analizar datos y construir modelos. Todo

lo demás es complejidad innecesaria



Patrimonio


intelectual







DevOps

Users &


Tools


DataOps

Users &


Tools

<!-- fin de página 16 -->

## Diferencias entre DevOps y DataOps

Testing



Datos

Variables


Value
Pipeline



complejidad, muestreo,


seguridad


Automatización en la creación de


ambientes de desarrollo con los


datos, software, hardware y


librerías requeridas



Tests de datos y

monitoreo


Tamaño de los datos,



Sandbox


CALIDAD


DATA PRODUCCION VALOR



DESARROLLO


IDEA


Desarrollo


Sandbox

Ambiente de desarrollo aislado
para desarrollo y testing de
nuevas aplicaciones.



Código

Fijo


Código
Variable



Datos

Fijos


Innovation

Pipeline


Tests de
regresión,
funcionales y

desempeño



Productivo


   - Hardware y versiones de. Software


correctas.


   - Configuración de hardware y red.


- Gestión de datasets de prueba


- Mayor cantidad de herramientas


que en DevOps

<!-- fin de página 17 -->

## Diferencias entre DevOps y DataOps

**Equipos locales DA distribuidos**


Cercanos al negocio

Herramientas self-service o desktop

Científicos de datos, analistas, …


**Desarrollo**



**Innovación**

**Competitividad**




   - Las herramientas self-service no promueven

y habilitan el re-uso.

  - Tendencia a manejar cambios manualmente.

   - Integración manual de datos.

   - Requieren soporte de ingenieros de datos.


DataOps brinda

armonización


**Operaciones**
Equipo de TI

Monitoreo

Clientes



Analistas

Ingenieros de datos
Arquitectos de datos
Ingenieros de software



DataOps


**Equipo DA centralizado**



**Estandarización**

**Calidad del dato**

**Seguridad**

**Gobernabilidad**



Soporte a la compañías

Estandarización de herramientas
Científicos de datos, ingenieros, …

<!-- fin de página 18 -->

## Cadena de suministro de datos

Centralización Libertad



Fuentes de


datos



Datasets Analytics



Data
Data Supply Data Analysis Business User
Engineering



Requerimientos de
las fuentes de datos



Requerimientos

de los datasets



Requerimientos

Analytics



Necesidades




- Soporte en la integración de

                          - Soporte de los usuarios cambiantes



nuevos datasets.

- No se puede crear un dataset por




- Soporte de los usuarios



cada idea nueva

- Producen datasets de alta calidad

en data lakes, data warehoses y
data marts



del negocios

- Base de la innovación.

- Muchas tareas que no

agregan valor

<!-- fin de página 19 -->

## Implementación de MLOps

##### Fase 1 Fase 2 Fase 3




- Configuración de ambientes de

desarrollo y prueba

- Hardware, almacenamiento y

herramientas de software


Configuración de la

infraestructura


Desarrollo de modelos


- Desarrollo de modelos en un

framework eficiente que permita
automatización y optimización

- Desarrollo y manejo de tuberías

de datos

- Verificación del desempeño de

modelos



:
**Prerequisitos**

- Artifactos auditables con logging

- Modelos documentados y

verificados


Transición a Operaciones


**Tareas claves** :

 - Serialización y contenerización de

los artifactos

 - Model serving

 - Despliegue de modelos al

ambiente de producción usando
CD/CI y pruebas de aceptación

 - Cumplimiento de lineamientos de

aseguramiento de la calidad




- Monitoreo del desempeño,

incidentes y reenetrenamiento

- Monitoreo de la telemetría


MLOps


Data Operations


- Monitoreo y solución de incidentes

en la tubería de datos y la
plataforma de ML, manejo de la
seguridad

<!-- fin de página 20 -->

## Agile for DataOps

### • Muchos de los principios agiles para desarrollo de software aplican en DA/Analytics • En DataOps se debe tener en cuenta que el software por si mismo no hace mejores decisiones • Una buena decisión requiere datos y algoritmos de alta calidad. • El desarrollo de productos de datos tiene un ciclo de vida diferente al ciclo de productos de software • Actividades como entendimiento del negocio, adquisición y limpieza de datos, entrenamiento de modelos, etc son menos predecibles y más iterativas que las actividades típicas en desarrollo de software.

<!-- fin de página 21 -->

## Principios para el manejo del código fuente

### • Modularidad • Funciones dedicadas a una sola tarea • Estructuración adecuada del código • Código limpio • Testing • Control de versiones • Logging • Manejo de errores • Legibilidad • Comentarios y discusión

<!-- fin de página 22 -->

## Data Science Lifecycle

Business Provision
understanding infraestructure



Next iteration


Model

evaluation


Model training


Data pipeline

testing



Monitoring /

benefit

mesasurement


Deployment

testing &
documentation


Model

deployment


Data pipeline

deployment



Decommission



Data acquisition


Data exploration


Data

preparation


Feature

engineering


Data pipeline
development



Identify
products


Calculate value


Assess
feasibility


Priorize

products



Identify
solutions

architecture


Determine


analytical
techniques


Review

existenting
work/literature


Set vision,
secure funding

& build team



Research &
Ideation Inception
Development



Transition /
Retirement
Production

<!-- fin de página 23 -->

## Ideation






















|Ideation|Feasibility|Analyze|Backlog|Develop|Done|
|---|---|---|---|---|---|
|No limit|WIP limited|WIP limited|No limit|Team WIP<br>limits|No limit|
|• New product &<br>feature creation<br>opportunities<br>• Customer experience<br>enhancements<br>• Business efficiency<br>improvements<br>• Improvements to<br>existing solutions|• Epic hyphotesis<br>statement<br>• Rough sizing of effort<br>• Benefit estimation<br>• Priorititation matrix|• Investigate alternative<br>solutions<br>• Refine cost and<br>benefit estimates<br>• Define MVP<br>• Measurement plan<br>developed<br>• Prioritize|• Epics selected for<br>development of lean<br>portfolio management<br>team<br>• Continuous<br>prioritization of epics|<br>• Epics broken into<br>work teams, stories<br>or tasks.<br>• Teams begin<br>development when<br>they have capacity<br>• Epic tracking|• Benefit measured<br>versus plan<br>• Stop or persist<br>decision made.|



**Epics** : Iniciativas estrategicas que cierran las brecha entre el estado
futuro deseado y el estado actual basado en los objetivos de la
organización, y que capturan las ideas técnicas y de negocio más
significativas. Deben permitir la creación de un MVP.

<!-- fin de página 24 -->

## Epic Hypothesis Statement


|Estructure|Description|Example|
|---|---|---|
|Achieve|[strategic theme objective]|Compliance goal|
|Through|[target portfolio vision<br>outcome]|Improved anti-money laundering (AML) risk assessment|
|For|[customers]|Money Laundering Reporting Officer (MLRO)|
|By|[proposed solution]|Applying machine learning to automatically monitor customer<br>transactions data to identify anomalies for investigation|
|Resulting in|[predicted benefit]|Reduced risk of fines|
|Mesaured by|[metrics]|Value of AML penalties relative to peers|
|Partnering with|[other teams and partners]|Compliance and IT temas|
|Integrating|[sources and data types]|Financial transactions and customer identity data|
|And requiring|[non-functional requirements]|Ability to scale and match transaction volumenes, and achieve<br>99.99% availability|

<!-- fin de página 25 -->

# ¿Qué es DataOps?

> ⚠️ S01: página 26 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 26 -->
