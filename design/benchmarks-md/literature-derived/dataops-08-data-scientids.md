---
source: "design/benchmarks-pdf/literature-derived/dataops-08-data-scientids.pdf"
source_sha256: 37a435fa50be7809f94174a1bebcbbee3257df5ecb0376eb4e7a4e997fcfead0
family: literature-derived
pages: 13
min_text_coverage: 0.952
pages_without_graphics: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 13]"
---
# DataOps para el Data Engineer y el Data Scientist

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## Desarrollo de modelos tradicionales vs ML

### Programación tradicional

Tests basados



Datos ficticios o


muestras


Lógica codificada a


mano


Código crítico y

complejo

### Machine Learning


Datos

muestreados


Resultados

esperados


Aprendizaje de la

lógica



Computador


Computador



Software


Datos Nuevos


Tests basados

en ejemplos


Modelo


Datos nuevos



en ejemplos


Código testeado



Computador


Configuración y

parámetros


Computador



Resultado

### Modelado tradicional


Datos


Modelo codificado


a mano


Resultado



Tests basados en

comportamiento


Computador


Código crítico y

complejo



Resultado

<!-- fin de página 2 -->

## DataOps en Ciencia de Datos y Machine Learning

### Construcción del modelo en Machine Learning

Ejecución manual, errores

frecuentes e inflexibilidad



Se requieren muchas más
herramientas para desarrollo

que para despliegue


Monitoreo del


modelo



Definición del


problema


Limpieza,
transformación y

manipulación



Preparación de Extracción de Construcción

datos características del modelo modelo



Identificación de
transformaciones que sean

informativas y faciliten el

entrenamiento



Construcción



del modelo



Evaluación del



Despliegue del

modelo



datos



Extracción de

características



Responsabilidad
del equipo de DA


Tests automáticos

de data, código y

modelos



Cambios en los
requerimientos o

condiciones de

negocio


Monitoreo



Despliegue
automático con
técnicas de DevOps


Desconexión entre lo
requerido para desarrollar
el modelo y su despliegue



Debito técnico


Recolección de


datos



El modelo es una pequeña
fracción de lo requerido para el

despliegue y monitoreo


Manejo de recursos



de máquina


Verificación de


datos


Herramientas


de análisis


Herramientas de
manejo de procesos



Configuración



Código ML
Configuración y

parámetros


Extracción de

características



Infraestructura


de servicio

<!-- fin de página 3 -->

## Reducción de la deuda técnica usando DataOps

#### ¿Cómo introducir el proceso de construcción de un modelo de ML en los pipelines y reducir el débito técnico?



Orquestación de las

tuberías de valor e


innovación




- Introducción para pruebas lógicas de código y datos.

- Uso de un sistema de control de versiones

- Estrategia de ramificación y fusión

- Uso de multiples ambientes

- Reuso y contenerización

- Parametrización del proceso

- Doble orquestación.


Agile en solo en el
desarrollo no hace

al equipo ágil



CALIDAD

##### DATA PRODUCCION VALOR



Monitoreo del
pipeline de valor
mediante pruebas


##### DESARROLLO IDEA


### Construcción del modelo en Machine Learning



Definición del

problema



Preparación de Extracción de Construcción del

datos características modelo modelo



Construcción del



Evaluación del



Despliegue del

modelo



DevOps permite la

automatización de
pruebas del código y

despliegue


Monitoreo del


modelo



datos



Extracción de

características



modelo

<!-- fin de página 4 -->

## Arquitectura de datos canonica

En DA se debe estar
preparado para cambios

rápidos y frecuentes


**Production Environment**


Raw Lake Data Engineering Refined Data Data Science Data Visualization Data Governance



Clientes



Data

Sources
Optimizado para

requisitos de

producción



La facilidad para

no
**cambios rápidos**

es un requisito



**Un pequeño cambio en el pipeline de valor es difícil y lento**


Fallas para:

    - Actualizar y publicar cambios en las analíticas


rápidamente sin interrumpir las operaciones

    - Descubrir errores en los datos antes de que se


publiquen las analíticas

    - Crear y publicar cambios en los esquemas


rápidamente

<!-- fin de página 5 -->

## Arquitectura de datos para DataOps

**Production Environment**



Raw Lake Data Engineering Refined Data Data Science Data Visualization Data Governance



Data

Sources


**Puppet**



**Creación y**


**manejo de**

**ambientes**



**Orquestación, Monitoreo y Control**



**Airflow**

**Kubeflow**


**Grafana**



Clientes



**Test Environment**



**Orquestación, Monitoreo y Control**



**Despliegue**
**automático**



**Chef** **manejo de**

**Despliegue** **Jenkins**

**Ansible**

**ambientes**

**Travis CI**



**Dev Environment**




- Tests de lógica y de datos

- Uso de sistemas de control de versiones

- Ramificación y fusión

- Uso de ambientes múltiples

- Reuso y contenerización.

- Parametrización del proceso

- Doble orquestación


**Git**

**Docker**



Almacenamiento y

control de


versiones


**MongoDB**



**Orquestación, Monitoreo y Control**


DATAOPS PLATFORM



**Tableau**
**Okta**
**Vault**
**Power BI**
**Auth0**



DataOps



Historia y
Metadados



Autorizaciones y



DataOps Métricas
Secretos
Permisos



Equipo de
y Reportes

<!-- fin de página 6 -->

## Uso de Design Thinking en Data Analytics con DevOps


###### Metodología para abordar problemas mal definidos o complicados que desafían aproximaciones convencionales



Generación de tantas
ideas como sea posible



Creación de un prototipo

de solución, probar,

aprender y repetir



Ganar entendimiento del
problema consultado expertos,
observando y empatizando, para

ir más allá de los supuestos.


Idea


###### Empatía Ideas Experimentación

Desarrollo Pruebas Integración


Nueva Analitica
Clientes


Ciclo de tiempo



La experimentación puede tomar
mucho más tiempo que las fases

anteriores


- Manejo de proyectos usando Agile

- Creación de ambientes de producción y


desarrollo alineados

- Orquestación del aseguramiento de la

calidad y del despliegue continuo del código

- Orquestación automática del pipeline de


valor

- Pruebas de validación de la data y la lógica

de negocio




- Falta de trabajo en equipo

- Falta de colaboración entre grupos

- Espera para que IT configure

recursos del sistema

- Espera para acceder a datos

- Desarrollo lento

- Espera de aprobaciones

- Arquitecturas de datos inflexibles

- Cuellos de botella en procesos

- Debito técnico

- Baja Calidad

<!-- fin de página 7 -->

## Agile Data Warehousing

###### Aplicación de principios ágiles a proyectos de data warehouse para mejorar la velocidad de innovación —> No implica que el equipo sea ágil Productivo

On premises


Espacio de trabajo

compartido


Subconjunto de



:
**Dificultades para**

- Compartir datos entre máquinas y ambientes.

- Aprovisionamiento de máquinas físicas diferentes.

- Gestión y mantenimiento manual de ambientes en

máquinas físicas diferentes

- Realizar pruebas y capturar errores

- Eliminar riesgos en el despliegue de código.

- Gestionar los equipos humanos que realizan las


labores anteriores



Orquestación



datos para
pruebas de
desempeño y

producción


Subconjunto de

datos para

pruebas


Subconjunto de

datos para


desarrollo

<!-- fin de página 8 -->

## Aceleración de la Innovación con DataOps


###### El almacenamiento de datos en bruto y procesados (CMR, ERP, …) es fundamental para garantizar un acceso fácil y responder rápidamente.

Datos en



Datos procesados


facilmente

accesibles


Transformaciones


de datos y ETL


Espacio compartido

de datos



Fuentes de


datos



RDBMS



Manual propenso a


errores


ETL



Datos altamente
dispersos y difíciles de


accesar


Facilita tareas de
visualización y análisis


Data Mart


Data Warehouse



ERP


EIS



RDBMS


Fuentes de


datos



Es esencialmente

código



bruto



DS
Data

Warehouse


Data

Mart



Data Lake



Data Mart - En el data lake solo se colocan datos que serán consumidos



por usuarios

- Colocar todos los campos entregados por la fuente.

- Limpie, cure y transforme solo los datos requeridos

- La estructura del data lake debe ser acorde al data


warehouse.

- Tenga un gobierno de datos estricto.

- Genere data marts con datasets que requieran los

consumidores de datos y faciliten su labor.

- Mantenga backups del data lake



El grupo de DA tiene
acceso directo al data


lake



El diseño soporta el

acceso a datos

<!-- fin de página 9 -->

## Esquemas en bases de datos

**Esquemas**


  - Definición de las tablas.

  - Tipos de datos bien definidos.

  - Relaciones (uno a uno, uno a muchos, muchos a

muchos).

  - Campos clave.

  - Reglas de negocio.

  - Optimizado para inserciones y actualizaciones


En DA debe ser optimizado
para lecturas, agregaciones y
entendimiento de las personas


Qué pasa cuando se desea agregar un nuevo campo
para análisis?


      - Se agrega el nuevo campo a una tabla.

      - Se agrega una nueva tabla que una el campo nuevo

con uno existente.

<!-- fin de página 10 -->

## Reuso de código en Data Analytics

Value Pipeline




- Contenerización del ambiente de desarrollo


- Contenerización de las aplicaciones



Data en bruto


- La separación en pequeños



Reportes,
Proceso Proceso Proceso Proceso modelos o

visualización



Facilita el proceso de

llevar código a

productivo



Docker es un proyecto de código abierto para el
despliegue de aplicaciones dentro de
contenedores para la virtualización de
aplicaciones


Contenedores
Pueden ser
múltiples imágenes
de la misma App



Sistema Operativo Anfitrión


Infraestructura


- Balanceo de carga

- Gestión de memoria

- Gestión de contendores



Sistema Operativo Anfitrión


Infraestructura



App C


bins/lib


Sistema

Operativo

Invitado



componentes permite la reutilización


de código.


- Cada componente puede tener una


lógica compleja y estar escrito en un


lenguaje diferente y requerir un stack


de software distinto.


- Es difícil llevar un componente de


una máquina o ambiente a otro



Proceso


Proceso


Proceso


Innovation
Pipeline



Máquinas

virtuales


App B


bins/lib



App A


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

<!-- fin de página 11 -->

## Fallas en DA y altas expectativas


 - Los dashboards son tan valiosos como la data detrás de ellos, la


cual usualmente es de baja calidad.


 - Los datasets son peculiares y difíciles de manipular.


 - Los usuarios tienen conocimiento de negocio pero saben poco


sobre que pueden hacer los datos por ellos.


 - Es imposible realizar grandes proyectos que reconstruyan la


tubería de datos.


 - Los equipos de DA no tienen acceso a la data.


 - Se sabe que la integración de datos de bases de datos dispersas


es dura, pero es mucho mas dura de lo que la gente piensa




- Use métodos ágiles para crear nuevas analíticas.


- La infraestructura debe permitir que los equipos trabajen juntos


usando agile.


- Inicie con proyectos pequeños y simples.


- Cree rapidamente algo que de valor.


- Obtenga retroalimentación de los usuarios.


- Repita iterativamente.


- Implemente procesos automáticos de monitoreo de datos.


- Automatice los flujos de trabajo y el despliegue de nuevas


analíticas.


- Orqueste el proceso completo.


- Un ingeniero de datos debe soportar 10 analistas y científicos de


datos, que finalmente soportan 100 profesionales del negocio

<!-- fin de página 12 -->

# DataOps para el Data Engineer y el Data Scientist

> ⚠️ S01: página 13 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 13 -->
