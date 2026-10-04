---
source: "design/benchmarks-pdf/literature-derived/dataops-05-agile.pdf"
source_sha256: fd106f0ecff624968d4036c4d8a924f1b69aadfca988c0e0f63ee53117400cec
family: literature-derived
pages: 15
min_text_coverage: 0.961
pages_without_graphics: [2, 3, 4, 5, 6, 8, 9, 11, 13, 14]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 15]"
---
# Colaboración Agil

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## Waterfall Project Management

###### • Requiere planeamiento detallado y alto grado de detalle. • Los requerimientos fijos y bien entendidos desde el principio, pero los requerimientos y tiempos son variables • Es una forma de manejo predictivo de proyectos. Problemas: • Los cambios tardíos generan ciclos de replanteamiento y causa retrasos y sobrecostos. • Diferencia entre los ambientes de desarrollo, prueba y productivo. • Diferencias entre el hardware en la distintas etapas. • Falta de replicabilidad. • Incapacidad para respuesta rápida a cambios.

Propuesto originalmente por WW Royce
en 1970, revisado por B. Boehm en
1980 y por I. Somerville en 1985


##### Requisitos del sistema y del software



Los usuarios no saben

exactamente que

requieren

###### Modelos, esquema y reglas de negocio

##### Análisis

###### Arquitectura del software

##### Diseño

###### Desarrollo, pruebas e integración

##### Codificación


El usuario solo


conoce el
producto al final
##### Pruebas

###### Descubrimiento de defectos



Es muy difícil hacer un

cambio una vez se

finaliza una etapa


###### Instalación, migración, soporte y mantenimiento


##### Operaciones



Valor diferido del proyecto


#### Big-Bang Deliverable

Incertidumbre hasta este


punto

<!-- fin de página 2 -->

## Valores y Manifiesto Agil

**Frameworks:**


       - Rapid Application Development (RAD)


       - Dynamic Systems Development Methods (DSDM)


       - Scrum


       - Extreme Programming



Respuestas

al método


waterfall




**Individuals and interactions** over processes and tools


**Working software** over comprehensive documentation


**Customer collaboration** over contract negotiation


**Responding to change** over following a plan



Scaled Agile

Framework

(SAFe)


Escalamiento de


los frameworks




- Our highest priority is to satisfy the customer through early and continuous


delivery of valuable software.


- Welcome changing requirements, even late in development. Agile processes


harness change for the customer’s competitive advantage.


- Deliver working software frequently, from a couple of weeks to a couple of


months, with a preference to the shorter timescale.


- Business people and developers must work together daily throughout the


project.


- Build projects around motivated individuals. Give them the environment and


support they need, and trust them to get the job done.


- The most efficient and effective method of conveying information to and


within a development team is face-to-face conversation


- Working software is the primary measure of progress.


- Agile processes promote sustainable development. The sponsors,


developers, and users should be able to maintain a constant pace


indefinitely.


- Continuous attention to technical excellence and good design enhances


agility.


- Simplicity – the art of maximizing the amount of work not done – is essential.


- The best architectures, requirements, and designs emerge from self

organizing teams.


- At regular intervals, the team reflects on how to become more effective and


then tunes and adjusts its behavior accordingly.



Scrum/XP
Scrum Kanban Scrumban

hybrid

<!-- fin de página 3 -->

## Scrum

Responsable por resultados y

priorización


Responsable del enfoque del

equipo, el entrenamiento, la
eliminación de impedimentos

y la aplicación de los
principios y prácticas de

Scrum.



experimentados


Lista de tareas
priorizadas creada

por el Product
Owner y que no se

puede editar o

modificar


Task Board



Product


Owner


Scrum

Master



Cross
functional
development

team



1, 2 o 4 semanas


Time-boxed Sprint



Acciones de
mejora para el

próximo sprint



**Enfoque en el**
**desarrollo del**

**producto**



Es prescriptivo y Todas las tareas
requiere equipos
quedan finalizadas



de tareas Spring goal


Daily
Scrum


Retroalimentación



Spring
Retrospective



Spring
Backlog


Lista detallada



Spring

Tasks



Spring
Review



Característica
completamente

probada


Shippable
Increment



Product
Backlog



Spring
Planning

<!-- fin de página 4 -->

## XP & Scrum/XP hybrid



Area de foco significativa
alineada con objetivos de

largo plazo


Historias cortas que

describen el uso
significativo del producto


### Themes

User

stories


### Weekly Cycle



El WIP es
limitado por el

ciclo



Test

Cases



Costumer

approval



Requerimientos



Estimate




- Sit tighter

- Whole team

- Informative workspace

- Energized work



Planning

meeting



Small

Releases



Acceptance
Tasks



Bugs



Plan



Test-driven
Slack
development



Planeación de

largo plazo



Quarterly

cycle


Spike



Tests



Refactoring


Ultima

versión


**Enfoque en las**
**prácticas para**
**desplegar**
**código**



Incremantal

Design



Pair
Programming



Continuous

Integration


10 Minutes


Build

<!-- fin de página 5 -->

## Kanban


    - Iniciar con lo que se sabe ahora.


   - Acuerdo para seguir incrementalmente.


   - Cambio evolutivo.


   - Fomentar actos de liderazgo en todos los niveles.


    - Visualizar


    - Limitar el trabajo en proceso.


    - Manejar el flujo.


    - Hacer explicitas las políticas


   - Implementar ciclos de reglamentación


   - Mejorar colaborativamente y evolucionar


experimentalmente


- No define roles ni equipos.


- Hay un flujo continuo en vez de sprints.


- Funciona mejor para trabajo no planeado o difícil de


estimar


- Multiples ciclos de retroalimentación:


  - Trimestral: Strategy reviews


  - Mensual: Operations & risk reviews.


  - Quincenal: service delivery review.


  - Semanal: replenishment review.



Cross
functional
development

teams


Representan el

flujo de trabajo


Work items
asignados a

individuos


El manager maneja

el tablero



Se busca el movimiento


más beneficioso
maximizando el flujo


Flujo continuo de trabajos


El WIP se limita por

la cantidad máxima
de trabajos en cada

columna



**Enfoque en el**
**mejoramiento del**
**proceso eliminando**
**desperdicios**


Simula el flujo de un
producto por una línea

de ensamblaje

<!-- fin de página 6 -->

## Escalamiento de prácticas Agile




















|Scaled Agile Framework<br>Empresa (múltiples lineas de negocio, múltiples portafolios)<br>Scrum of Scrums<br>Portafolio (múltiples equipos, múltiples productos)<br>Disciplined Agile Delivery<br>Un agile<br>framework<br>por cada<br>Escalamiento<br>producto Escalamiento<br>horizontal<br>vertical<br>Concepto Comienzo Desarrollo Transición Producción Retiro<br>Operación<br>Identificación de proyectos Involucrar a los interesados Desarrollo iterativo Pruebas finales Migrar<br>Monitoreo y soporte<br>Priorización de proyectos Obtener financiamiento Documentación Remover<br>Arreglo y mejora<br>Desarrollo de la visión Formación del equipo Entrenamiento<br>Evaluación del factibilidad Configuración del entorno Despliegue<br>Programa (múltiples equipos, un producto o más productos relacionados)|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Concepto<br>Comienzo<br>Desarrollo<br>Transición<br>Producción<br>Retiro<br>Identifcación de proyectos<br>Priorización de proyectos<br>Desarrollo de la visión<br>Evaluación del factibilidad<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Desarrollo iterativo<br>Pruebas fnales<br>Documentación<br>Entrenamiento<br>Despliegue<br>Operación<br>Monitoreo y soporte<br>Arreglo y mejora<br>Migrar<br>Remover<br>**Disciplined Agile Delivery**<br>**Scrum of Scrums**<br>Empresa (múltiples lineas de negocio, múltiples portafolios)<br>Programa (múltiples equipos, un producto o más productos relacionados)<br>Portafolio (múltiples equipos, múltiples productos)<br>**Scaled Agile Framework**<br>Un agile<br>framework<br>por cada<br>producto<br>Escalamiento<br>horizontal<br>Escalamiento<br>vertical|Concepto<br>Comienzo<br>Desarrollo<br>Transición<br>Producción<br>Retiro<br>Identifcación de proyectos<br>Priorización de proyectos<br>Desarrollo de la visión<br>Evaluación del factibilidad<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Desarrollo iterativo<br>Pruebas fnales<br>Documentación<br>Entrenamiento<br>Despliegue<br>Operación<br>Monitoreo y soporte<br>Arreglo y mejora<br>Migrar<br>Remover<br>**Disciplined Agile Delivery**<br>**Scrum of Scrums**<br>Empresa (múltiples lineas de negocio, múltiples portafolios)<br>Programa (múltiples equipos, un producto o más productos relacionados)<br>Portafolio (múltiples equipos, múltiples productos)<br>**Scaled Agile Framework**<br>Un agile<br>framework<br>por cada<br>producto<br>Escalamiento<br>horizontal<br>Escalamiento<br>vertical|Concepto<br>Comienzo<br>Desarrollo<br>Transición<br>Producción<br>Retiro<br>Identifcación de proyectos<br>Priorización de proyectos<br>Desarrollo de la visión<br>Evaluación del factibilidad<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Desarrollo iterativo<br>Pruebas fnales<br>Documentación<br>Entrenamiento<br>Despliegue<br>Operación<br>Monitoreo y soporte<br>Arreglo y mejora<br>Migrar<br>Remover<br>**Disciplined Agile Delivery**<br>**Scrum of Scrums**<br>Empresa (múltiples lineas de negocio, múltiples portafolios)<br>Programa (múltiples equipos, un producto o más productos relacionados)<br>Portafolio (múltiples equipos, múltiples productos)<br>**Scaled Agile Framework**<br>Un agile<br>framework<br>por cada<br>producto<br>Escalamiento<br>horizontal<br>Escalamiento<br>vertical|**Scrum of Scrums**<br>Portafolio (múltiples equipos, múltiples productos)|**Scrum of Scrums**<br>Portafolio (múltiples equipos, múltiples productos)|**Scrum of Scrums**<br>Portafolio (múltiples equipos, múltiples productos)|
|Concepto<br>Comienzo<br>Desarrollo<br>Transición<br>Producción<br>Retiro<br>Identifcación de proyectos<br>Priorización de proyectos<br>Desarrollo de la visión<br>Evaluación del factibilidad<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Desarrollo iterativo<br>Pruebas fnales<br>Documentación<br>Entrenamiento<br>Despliegue<br>Operación<br>Monitoreo y soporte<br>Arreglo y mejora<br>Migrar<br>Remover<br>**Disciplined Agile Delivery**<br>**Scrum of Scrums**<br>Empresa (múltiples lineas de negocio, múltiples portafolios)<br>Programa (múltiples equipos, un producto o más productos relacionados)<br>Portafolio (múltiples equipos, múltiples productos)<br>**Scaled Agile Framework**<br>Un agile<br>framework<br>por cada<br>producto<br>Escalamiento<br>horizontal<br>Escalamiento<br>vertical|Concepto<br>Identifcación de proyectos<br>Priorización de proyectos<br>Desarrollo de la visión<br>Evaluación del factibilidad<br>Escalamiento<br>vertical||Desarrollo<br>Transición<br>Desarrollo iterativo<br>Pruebas fnales<br>Documentación<br>Entrenamiento<br>Despliegue<br>a (múltiples equipos, un producto o más productos relacion<br>Un agile<br>framework<br>por cada<br>producto|Producción<br>Retiro<br>Operación<br>Monitoreo y soporte<br>Arreglo y mejora<br>Migrar<br>Remover<br>**Disciplined Agile Delivery**<br>ados)|Producción<br>Retiro<br>Operación<br>Monitoreo y soporte<br>Arreglo y mejora<br>Migrar<br>Remover<br>**Disciplined Agile Delivery**<br>ados)|
|Concepto<br>Comienzo<br>Desarrollo<br>Transición<br>Producción<br>Retiro<br>Identifcación de proyectos<br>Priorización de proyectos<br>Desarrollo de la visión<br>Evaluación del factibilidad<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Desarrollo iterativo<br>Pruebas fnales<br>Documentación<br>Entrenamiento<br>Despliegue<br>Operación<br>Monitoreo y soporte<br>Arreglo y mejora<br>Migrar<br>Remover<br>**Disciplined Agile Delivery**<br>**Scrum of Scrums**<br>Empresa (múltiples lineas de negocio, múltiples portafolios)<br>Programa (múltiples equipos, un producto o más productos relacionados)<br>Portafolio (múltiples equipos, múltiples productos)<br>**Scaled Agile Framework**<br>Un agile<br>framework<br>por cada<br>producto<br>Escalamiento<br>horizontal<br>Escalamiento<br>vertical|Concepto<br>Identifcación de proyectos<br>Priorización de proyectos<br>Desarrollo de la visión<br>Evaluación del factibilidad<br>Escalamiento<br>vertical|Comienzo<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Program<br>Escalamiento<br>horizontal|Comienzo<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Program<br>Escalamiento<br>horizontal|Comienzo<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Program<br>Escalamiento<br>horizontal|Comienzo<br>Involucrar a los interesados<br>Obtener fnanciamiento<br>Formación del equipo<br>Confguración del entorno<br>Program<br>Escalamiento<br>horizontal|
||Producto (un equipo, un producto)|Producto (un equipo, un producto)|Producto (un equipo, un producto)|Producto (un equipo, un producto)||

<!-- fin de página 7 -->

## Scrum of Scrums



Cross-functional

development

team


Cross-functional

development

team



Product


Owner


Scrum

Master


Ambassador


Ambassador


Scrum

Master


Product


Owner



Product


Owner



Scrum of


Scrums Ambassador


team



Cross-functional



Scrums
meeting



development



Progreso del equipo

Siguientes pasos

Impedimentos
Coordinación entre equipos

No reportan a externos



Scrum

Master

<!-- fin de página 8 -->

## Scaled Agile Framework (SAFe)



**Program**


###### Release on Demand



Liberación de

pequeños
incrementos en

el tiempo



Program

Kanban


Team
Backlog



Program

Backlog


Planificación del

Timebox de 8-12



Program
Increment

Planning


###### Continuous Delivery Pipeline Features Architectural Runway Enablers

Innovación
Aprendizaje y



Habilita el
despliegue

continuo



Para todos los
semanas

stakeholders



herramientas



**Cross-functional Agile Team**



Scrum/XP

or Kanban


iteration


**Iterations of two weeks**



Inspect &

Adapt

Event


**Program Increment**



Program
Increment

Planning



System

Demo



Innovation
& Planning

Iteration



Sincronización
de los equipos

<!-- fin de página 9 -->

## DataOps Manifesto and Principles


          **Individuals and interactions** over processes and tools


          **Working software** over comprehensive documentation


          **Customer collaboration** over contract negotiation


          **Responding to change** over following a plan


         **Individuals and interactions** over processes and tools


         **Working analytics** over comprehensive documentation


         **Customer collaboration** over contract negotiation


         **Experimentation, iteration, and feedback** over extensive upfront


design


         **Cross functional ownership of operations** over soiled


responsibilities


Recoge las diferencias
entre desarrollo de software

y data analytics




- Continually satisfy your consumer.


- Value working analytics


- Embrace change


- It’s a team sport.


- Daily interaction


- Self-organize


- Reduce heroism


- Reflect


- Analytics is code


- Orchestrate


- Make it reproducible.


- Disposable environments


- Simplicity


- Analytics is manufacturing


- Quality is paramount


- Monitor quality and performance


- Reuse


- Improve cycle times

<!-- fin de página 10 -->

## Analytics Lifecycle

Business
understanding


Identify products


Calculate values


Asses feasibility


Prioritize
products


SAFe alinea los



Datos y

modelo


Monitoring Decommission


Deployment

testing &
documentation


Model
deployment


Data pipeline

deployment



Provision

infrastructure


Identify solutions

architecture


Determine

analytical
techniques


Review existing

work/literature


Vision, secure

funding and

build team



Data acquisition


Data exploration


Data preparation


Feature
engineering


Data pipeline

development


No presente

en software



Next iteration


Experimentation


Model

evaluation


Model training


El

entrenamie


nto es

iterativo


Data pipeline

testing



portafolios de
productos con los

objetivos



Transition/
Ideation Inception R&D Retirement
Production


Identificación y



Foco en datos y
experimentación



priorización de

productos
potenciales



Esfuerzos iniciales


antes de R&D

<!-- fin de página 11 -->

## Agile DataOps Practices
























|Ideation|Feasibility|Analyze|Backlog|Develop|Done|
|---|---|---|---|---|---|
|No limit|WIP limited|WIP limited|No limit|Team WIP limits|No limit|
|Big ideas:<br>• New product & feature<br>creation opportunities<br>• Customer experience<br>enhancements<br>• Business efficiency<br>improvements<br>• Improvements to existing<br>solutions|• Epic hypothesis statement<br>• Rough sizing of effort<br>• Benefit estimation<br>• Prioritization matrix|• Investigate alternative<br>solutions<br>• Refine cost and benefit<br>estimates<br>• Define minimum viable<br>product (MVP)<br>• Measurement plan<br>developed<br>• Prioritize|• Epics selected for<br>development by Lean<br>portafolio management<br>team<br>• Continuous prioritization of<br>epics|• Epics broken into work<br>items, stories or tasks<br>• Teams begin development<br>when they have capacity<br>• Epic tracking|• Benefit measured versus<br>plan<br>• Stop or persist decision<br>made|

<!-- fin de página 12 -->

## Agile DataOps Practices



Ideation


Inception


R&D


Transition/

Production


Retirement



Structure Description Example


Achieve Sstrategic theme objective Compliance goal


Though Target portfolio outcome Improved anti-money laundering (AML) risk assessment


For Costumers Money Laundering Reporting Officer (MLRO)



By Proposed solution



Applying machine learning to automatically monitor
customer transactions data to identify anomalies for
investigation



Resulting in Predicted benefit Reduced risk of fines


Measured by Metrics Value of AML penalties relative to peers


Partnering with Other teams and partners Compliance and IT teams


Integrating Sources and data types Financial transactions and customer identity data


Ability to scale and match transaction volumes, and
And requiring Non-functional requirements
achieve 99.99% availabilit
y

<!-- fin de página 13 -->

## Agile DataOps Practices

Ideation


Inception




- Cada epic tiene un epic owner, que es un data analytics lider responsable


del manejo del progreso de una epic.


- Si el epic es un habilitador, su owner es un especialista técnico.


- Responsabilidades del owner:


  - Estimación del esfuerzo y del costo de retrasos


  - Explorar soluciones y arquitecturas alternativas


  - Identificar recursos de datos


  - Definer un producto mínimo viable


  - Crear el panel de monitoreo y medida para los KPIs


  - Interactuar con equipos para dividir el epic en features, y a su vez en


trabajo futuro, items, historias o tareas dependiendo del framework


usado.



R&D


Transition/

Production


Retirement




- Desarrollar un MVP para verificar las hipótesis.


- Los equipos son libres de definir el marco ágil a usar.




- Los ambientes de desarrollo deben ser similares a los de producción.


- Las pipelines de datos y analíticas deben hacerse productivas lo mas


rápidamente posible.


- Se deben eliminar los pasos manuales.

<!-- fin de página 14 -->

# Colaboración Agil

> ⚠️ S01: página 15 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 15 -->
