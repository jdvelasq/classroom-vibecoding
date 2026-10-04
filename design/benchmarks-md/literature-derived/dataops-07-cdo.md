---
source: "design/benchmarks-pdf/literature-derived/dataops-07-cdo.pdf"
source_sha256: e77e412071365bc5f5d503cf5a6e39981d255e2010411e5659a765bcd98bdb0e
family: literature-derived
pages: 12
min_text_coverage: 1.0
pages_without_graphics: [3, 4, 5, 6, 7, 9, 10, 11]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 8, 12]"
---
# DataOps para el Chief Data/Analytics/ Information Officer

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## Grupos de trabajo y aislamiento



Kubeflow
Python
Spark

R
Tensorflow



Self service tools

Tableau

Alteryx
Cognos



Alation

Collibra

Wikis



Servidores

Almacenamiento

Software



Python

Java

Spark QL
Hadoop
Airflow

ETL



Data Center/IT Data Engineering Data Science Data Visualization Data Governance




- Desarrollo y uso de


modelos

- Adición de resultados a


los datasets




- Gestión del catalogo de

datos y resultados de

los modelos




- Infraestructura


computacional

- Operación de la red




- Creación de datasets


de alta calidad




- Visualización de los


datos y los resultados

de los modelos



Clientes



**Generación de silos**
por:

- Diferencia de herramientas, plataformas, ciclos de tiempo

y responsabilidades.

- Diferentes formas de abordar los problemas que son

dependientes de las herramientas usadas.

- Uso de multiples nubes / centros de datos.

- Multiples equipos en diferentes ubicaciones geográficas.

- Cada grupo se concentra en la complejidad de su propio

workflow

- Retos de coordinación de multiples equipos.

- Retos de comunicación entre equipos



Beneficios de **DataOps** :

- Robustez: por el uso de tests.

- Transparencia: Alertas automáticas, dashboards.

- Eficiencia: orquestación automática, balance entre

centralización y descentralización.

- Repetitividad.

- Separación y reuso.

<!-- fin de página 2 -->

## Coordinación Relacional (CR)

Coordinación relacional es la comunicación y el
relacionamiento con el propósito de integración de

tareas interdependientes, inciertas y con tiempos

limitados


Relaciones de roles y

flujos de trabajo



No son relaciones

interpersonales


La tecnología es un

habilitador



Dimensiones de la CR Baja CR Alta CR



Objetivos compartidos
Conocimiento compartido
Respeto mutuo


Frecuente
Oportuna
Precisa
Solución de problemas




- Robustes

- Transparencia

- Eficiencia

- Repetibilidad

- Compartible y fragmentaban


Arquitectura orientada a

servicios



Relaciones


Comunicación



Objetivos funcionales inidividuales
Conocimiento exclusivo
Fata de respeto


Infrecuente

Retrasada
Imprecisa
Señalamientos

<!-- fin de página 3 -->

## Mejoramiento del trabajo en equipo con DataOps

**Factores críticos** :

- Objetivos explícitos y consecuentes del grupo de trabajo

- Tareas y procesos diseñados optimamente y normar que

promueven dinámicas positivas.

- Sistemas de información que entregan los datos requeridos para el



trabajo y los recursos requeridos para las tareas

- Identidad colectiva y realidad compartida



**Diagnósticos erróneos:**

- Falla del director

- Problemas de trabajo en grupo.

- Problemas de trabajo individual (rapidez

y falta de atención).




- Hay un nuevo requerimiento que debe ser aprobado.

- Solicitud de acceso a datos.

- Cambios en la especificación funcional.

- Implementación del requerimiento, que puede ser similar a otro


presentado por otro equipo.

- Testing de la implementación en un ambiente que no es igual al


ambiente de producción.

- La ejecución en el ambiente de producción generan fallos severos.

- Pruebas en el ambiente de producción revelan fallos en la


analítica.

- El grupo de desarrollo difícilmente puede reproducir los fallos en el


ambiente de desarrollo.

- La nueva analítica está lista y se hace el despliegue en producción.

- El solicitante del requerimiento pregunta por qué se demoró tanto.




- Corrección de errores en las fuentes de datos

- Preparación de datasets

- Corrección de errores en la cadena de producción



Producción



Data Center/IT Data Engineering Data Science Data Visualization Data Governance


Desarrollo de nuevas


analíticas



Clientes

<!-- fin de página 4 -->

## Proceso

Productivo


Master Branch


Dev Main Branch

#### 1


Solicitud de una
#### nueva característica 2


Feature Dev Branch


DataOps Engineers


#### 3



Data Scientists



Production

Engineers


Pruebas


Creación de la rama

de desarrollo


Desarrollo



Nueva característica
#### 7

visible a los clientes


Merge


#### 6



Release


#### 4


#### 5

Tests de

integración


Pre-Release



DataOps Engineers


Merge


Desarrollo

  - Tests de datos

  - Tests de código

  - Implementación del requerimiento

  - Orquestación



**Beneficios**

- Facilita el movimiento entre equipos

- Trabajo colaborativo y coordinado

- Automatización y reducción de errores

- Mantenimiento de la seguridad

- Mejores prácticas y reuso

- Auto-servicio

- Democratización de datos

- Transparencia

<!-- fin de página 5 -->

## Eliminación de cuellos de botella

Deployment Pipeline del Proceso — Cada equipo tiene su tablero Kanban


Data Center/IT Data Engineering Data Science Data Visualization Data Governance


Clientes
#### Kanban

**Detección de un cuello de botella**

                                     - Trabajo en progreso: El trabajo se


acumula antes de una restricción.

                                  - Aceleración: En que áreas se deben



redireccionar recursos para satisfacer

usuarios.

- Tiempo del ciclo: Analizar los procesos


para el proceso con el ciclo más largo.

- Demanda: procesos que no están a la



**Process On-Going Improvement**

- Identifique la restricción

- Haga mejoras en el rendimiento de la


restricción con los recursos existentes

- Revise todas las actividades y verifique

un impacto positivo en la restricción.

- Si la restricción permanece en el mismo



**Ejemplos:**

- Dependencia de TI.

- Comités.

- Aprovisionamiento de sistemas de



sitio, defina que recursos adicionales

                          - Dependencia de TI.

pueden aliviar la restricción

                           - Comités.

Deployment Pipeline por Equipo - Vuelva al primer paso.



Cada equipo tiene su propio tablero Kanban



desarrollo y ambientes.

- Ciclos de prueba largos.

- Errores en datos

- Orquestación manual.

- Falta de trabajo en equipo.

<!-- fin de página 6 -->

## Priorización de objetivos basados en los objetivos deseados

Deployment Pipeline del Proceso — Cada equipo tiene su tablero Kanban


Data Center/IT Data Engineering Data Science Data Visualization Data Governance

###### Multiples cuellos



Clientes


###### de botella



1. Planee entrevistas orientadas a determinar los resultados requeridos.

2. Realice las entrevistas

3. Recolecte la lista de resultados deseados, remueva duplicados y

categorícelos en grupos de acuerdo a cada paso del proceso.
4. Dele una puntuación a los resultados para determinar su oportunidad.

Use una escala de 1-10 para la importancia y la satisfacción sobre

cada resultado.

5.  Organice los resultados deseados por oportunidad y planee las

mejoras.


### **Oportunidad = Importancia + max(0, Importancia - Satisfacción)**

<!-- fin de página 7 -->

## El Dashboard de DataOps

> ⚠️ S01: página 8 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 8 -->

## Trampas para el Chief Data/Analytics Officer

### **Incapacidad para entregar valor en un margen de tiempo aceptable**




- Solución de problemas

**Actividades**

- Mejora de eficiencia

**habilitadores**

- Mitigación de riesgos.

- Calidad, seguridad, privacidad de datos


Resultados que impactan directamente la

toma de decisiones



Trampa de la defensa de los

datos


Trampa del valor diferido


Trampa de la valoración de los

datos


Trampa de los proyectos de

poco valor directo y larga

duración



Defensiva


Ofensiva



Valor Indirecto


Valor Directo



Proyectos de largo plazo que son planeados
como cascada que solo son valiosos una vez

terminados


Proyectos par determinar el valor estratégico

de los datos

<!-- fin de página 9 -->

## Generación de confianza

Entrega de valor de forma
constante, rápida y efectiva


Desarrollo de analíticas para
las características más valiosas

del negocio


Despliegue rápido de nuevas

analíticas con confianza


Despliegue de datos precisos


##### **Agile**

Minimización del ciclo de

desarrollo y tests automáticos


Monitoreo de la lógica de
negocio y validez de los datos

<!-- fin de página 10 -->

## Etapas en el desarrollo de Analytics en la organización

Data Desert: la data es

desaprovechada


Boutique Analytics: Laptop
analytics desarticulada y manual


Waterfall Analytics: Proyectos

grandes y aislados


DataOps Analytics

<!-- fin de página 11 -->

# DataOps para el Chief Data/Analytics/ Information Officer

> ⚠️ S01: página 12 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 12 -->
