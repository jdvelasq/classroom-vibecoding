---
source: "design/benchmarks-pdf/literature-derived/dataops-09-data-quality.pdf"
source_sha256: fc3daa339da95c56a1938b4e1ed26694603a8f3a8742a1d245866418112eba1b
family: literature-derived
pages: 6
min_text_coverage: 1.0
pages_without_graphics: [2, 3]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 6]"
---
# DataOps para Calidad de Datos

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## Análisis de impacto



Cambio

propuesto



Falta de procesos automáticos

para el despliegue


Análisis del impacto por diferentes equipos
para determinar si el cambio causa fallas en el

sistema Ambiente de

producción

complejo


Proceso Waterfall para reducir

miedo e incertidumbre




- Se puede abstraer lo que los expertos revisan

en una serie de tests automáticos.

- Cada vez que algo falla se agrega una nueva

prueba.

- La efectividad de las pruebas automatizadas

depende de la calidad y la amplitud de los
tests y crece continuamente.

- Los tests se ejecutan de forma repetitiva y


continua.

- La reducción del ciclo de tiempo es asintótica.


Complejidad del desarrollo

de software



Esencialmente todo es código
escrito en diferentes lenguajes

y herramientas


Python
Spark



La introducción de un cambio

puede comprometer toda la

cadena



Python

Java

Spark QL
Hadoop

ETL



Python

R



:
**Tipos de tests**


- Pruebas unitarias: se prueba cada componente de software como


una unidad independiente.


- Pruebas de integración: se verifica la interacción entre


componentes.


- Pruebas funcionales: se verifican las historias de usuario.


- Pruebas de regresión: se ejecutan cada vez que hay un cambio


para verificar que la aplicación sigue funcionando correctamente.


- Pruebas de desempeño: se chequea la capacidad de respuesta,


estabilidad y disponibilidad bajo una carga determinada de trabajo.


- Tests de humo: pruebas rápidas para verificar que las funciones


principales son operativas.


El error no puede llegar a los

clientes


Tableau

Power BI Web



Acceso a datos Transformación Modelado Visualización Reporteria


- Muchos equipos de personas


- Muchas herramientas

<!-- fin de página 2 -->

## Analytics es código

Los datos son cambian


continuamente


**Value**

**Pipeline**


El código es constante en la
cadena de valor y solo cambia

en los despliegues


Los datos son


constantes



CALIDAD

#### PRODUCCION DESARROLLO IDEA


**Innovation**

**Pipeline**



CALIDAD

#### DATA PRODUCCION VALOR


Acceso a datos Transformación Modelado Visualización Reporteria


Proceso de liberación

de código


##### Código Fijo Código Variable

Ambiente idéntico al

de producción



Esencialmente todo es
código escrito en diferentes

lenguajes y herramientas


Ambiente de

producción

##### Tests de datos y monitoreo


Tamaño de los datos,


complejidad, muestreo,


seguridad



El código cambia

continuamente


### Testing

##### Datos Fijos Innovation Pipeline Tests de regresión, funcionales y desempeño


##### Datos Variables Value Pipeline

<!-- fin de página 3 -->

## Creación de confianza

###### Hay confianza cuando se cree que los datos son precisos



¿Están los datos
de entrada libres


de errores?



¿La lógica del

negocio es

correcta?



¿Las salidas son

consistentes?



Acceso a datos Transformación Modelado Visualización Reporteria



Los tests deben
incluirse en cada etapa

del pipeline





Se debe identificar los

problemas tan pronto

como se posible




|Entradas|Verificación de la cantidad de registros<br>Formato correcto de fechas, telefonos, …<br>Porcentajes de incremento en la cantidad de registros de una tabla<br>Fechas en un rango válido<br>Validación del tipo de campo<br>Validación del rango de valores de un campo|
|---|---|
|Lógica del<br>negocio|Campos diferentes de vacio<br>Impuestos|
|Salida|Precios positivos<br>Rangos esperados de los datos|


|Severidad|Acción requerida|
|---|---|
|Error|Detención del pipeline|
|Alerta|Investigación de la falla|
|Informativa|Ser consciente de la información|

<!-- fin de página 4 -->

## Tipos de pruebas y notificación




|Tipo|Acción requerida|Notificación automática<br>cuando algo falla|
|---|---|---|
|Location Balance tests|Las propiedades de los datos se mantienen en cada etapa. La cantidad de datos o sus<br>dimensiones se mantienen.|Las propiedades de los datos se mantienen en cada etapa. La cantidad de datos o sus<br>dimensiones se mantienen.|
|Historical balance|Se comparan los datos actuales con datos previos o valores esperados. Fallas al mover<br>preproducción a producción por los datos.|Se comparan los datos actuales con datos previos o valores esperados. Fallas al mover<br>preproducción a producción por los datos.|
|Statistical process control|Time balance tests. Se monitorea cada aspecto del proceso constantemente buscando<br>patrones anómalos|Time balance tests. Se monitorea cada aspecto del proceso constantemente buscando<br>patrones anómalos|

<!-- fin de página 5 -->

# DataOps para Calidad de Datos

> ⚠️ S01: página 6 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 6 -->
