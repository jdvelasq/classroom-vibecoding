---
source: "design/benchmarks-pdf/literature-derived/conf-origen-y-evolucion-business-analytics.pdf"
source_sha256: 1be064b6db147951e8a9e437b4cd5c3e78906ff9a7c3eaf2dbe38151d3d79131
family: literature-derived
pages: 64
min_text_coverage: 0.868
pages_without_graphics: [3, 15, 23, 29, 31, 33, 36, 41, 43, 53, 54, 61]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 62, 64]"
  - "páginas con cobertura < 0.95: [53]"
---
## Origen y Evolución de Business Analytics

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

##### ¿Por qué las organizaciones necesitan analítica?



Tareas
complejas


Tareas
repetitivas


**DATOS**

**Grandes volúmenes**


**de datos**



**ANALITICA**
**Métodos, modelos y**

**herramientas**




- Requiere **pensamiento complejo** y **experiencia**

- Muchos factores interrelacionados

- Capacidad limitada de la mente humana

- Requiere habilidades cognitivas complejas.

- Sesgos mentales y subjetividad.


- La tarea puede ser simple pero desbordante.

- Muy pocos factores.

- Propensa a errores humanos

- No requiere habilidades cognitivas complejas.



La complejidad y el volumen

superan la
capacidad humana



**CONOCIMIENTO**
**Patrones, insights y**

**entendimiento**



**DECISIONES**


Decisiones
informadas, objetivas

y oportunas



**VALOR**
Mejores resultados y
ventaja competitiva



La analítica transforma **datos** en **conocimiento** para apoyar mejores **decisiones** .

<!-- fin de página 2 -->

##### Caso de estudio: House of Cards (Netflix, 2013)

¿Cómo decidir si invertir más de USD
100 millones en una serie sin producir
primero un episodio piloto?



Analizó el comportamiento de millones de usuarios y encontró una combinación muy
atractiva:


.

- Un gran número de suscriptores veía películas protagonizadas por **Kevin Spacey**


- Existía una gran audiencia para las películas dirigidas por **David Fincher** .

- La versión británica de **House of Cards** gozaba de gran aceptación entre sus

usuarios.


- Los dramas políticos mostraban un alto nivel de consumo y de fidelidad.


La conclusión fue que la intersección de esas audiencias era lo suficientemente amplia
como para justificar la inversión.


Netflix ya sabía que:


- Por los patrones de visualización de sus usuarios, que muchas personas preferían

ver varios episodios consecutivos en lugar de esperar una semana entre capítulos.


- Desde la época del alquiler de DVD observaba que los usuarios consumían

temporadas completas cuando tenían esa posibilidad.


Por ello decidió publicar los 13 episodios el mismo día, dando origen al modelo
moderno de binge watching (maratones de series).



Primera

decisión


Segunda
decisión



**¿Cómo decidir si invertir más**
**de USD 100 millones en una**

**serie sin producir primero un**
**episodio piloto?**


**¿Cómo debía publicarse la**
**temporada?**

<!-- fin de página 3 -->

##### Caso de estudio: House of Cards (Netflix, 2013)

###### Business Analytics no elimina la incertidumbre. La convierte en una decisión informada.

Netflix no podía saber qué iba a ocurrir. Lo que podía hacer

era tomar una decisión aprovechando mejor la información

disponible.

<!-- fin de página 4 -->

### Pero para tomar decisiones con datos… primero necesitamos datos.

<!-- fin de página 5 -->

##### 1970 — Relational Database Management System

¿Cómo puede una organización
almacenar digitalmente la información
que anteriormente se administraba en
papel?


**RDBMS** : sistema de gestión de bases de

datos relacionales que facilita la
búsqueda y la organización de grandes
volúmenes de datos estructurados.


**Componentes**



**Idea clave:**
La información deja de administrarse
manualmente y pasa a almacenarse en
tablas relacionadas.


**Principales RDBMS modernos**


    - Oracle

    - PostgressSQL

    - Microsoft SQL server

    - MySQL

    - SQLite

   - …




- Esquemas

- Tablas

- Consultas

- Reportes

- Vistas

- Otros elementos


**Funciones**



**Esquemas**


- Definición de las tablas.

- Tipos de datos bien definidos.

- Relaciones (uno a uno, uno a muchos,

muchos a muchos).

- Campos clave.

- Reglas de negocio.




- Definición.

- Manipulación (inserción, borrado, actualización, …)

- Seguridad e integridad.

- Recuperación y restauración.

<!-- fin de página 6 -->

##### 1976 — Structured Query Language (SQL)

¿Cómo pueden automatizarse las
operaciones que anteriormente se
realizaban manualmente sobre una

base de datos?



**Idea clave:**
SQL convierte las operaciones
manuales sobre una base de datos en
procesos programables y reutilizables.


CREATE TABLE ‘ CUSTOMERS ';


ALTER TABLE 'ALUMNOS' ADD EDAD INT UNSIGNED;


DROP TABLE ‘ALUMNOS';


TRUNCATE TABLE ‘NOMBRE_TABLA';


SELECT * FROM vehículos ORDER BY marca, modelo;


SELECT DISTINCT marca, modelo FROM vehículos;


INSERT INTO agenda_telefonica (nombre, numero)
VALUES ('Roberto Pepe’, 4886850);


INSERT INTO phone_book2 ( [name], [phoneNumber] )
SELECT [name], [phoneNumber]
FROM phone_book
WHERE name IN ('John Doe', 'Peter Doe’)


DELETE FROM tabla WHERE columna1 = ‘valor1’;



**SQL** : lenguaje de consulta desarrollado

originalmente por **IBM** para consultar y
manipular bases de datos relacionales, y
posteriormente incorporado por **Oracle** en
el primer sistema comercial de gestión de
bases de datos relacionales (RDBMS).



**Data Definition Language (DDL)**

- Create

- Alter

- Truncate

- Rename

- Drop


**Data Manipulation Language (DML)**

- Insert

- Update

- Delete

- Select


**Data Control Language (DCL)**

- Grant

- Revoke


**Transactions Control Language (TCL)**

- Commit

- Rollback

- Savepoint

<!-- fin de página 7 -->

##### 1980s —- Sistemas de Información Empresariales

¿Cómo pueden las organizaciones
automatizar sus procesos de negocio
mediante aplicaciones especializadas?


**Sistemas funcionales** : Las bases de datos



**Idea clave:**

Los sistemas de información evolucionaron
hacia soluciones empresariales integradas,
lo que generó la necesidad de integrar
también su información.



relacionales impulsaron el desarrollo de
aplicaciones funcionales para automatizar
las distintas áreas de la organización:

  - Contabilidad

 - Nómina

  - Tesorería

  - Inventarios

 - Compras

  - Ventas

 - Producción


**Sistemas integrados** : aplicaciones

empresariales desarrolladas sobre bases
de datos relacionales que integran
procesos de negocio de diferentes áreas
funcionales (por ejemplo, contabilidad,
ventas, inventarios y recursos humanos)
mediante una base de datos común.



**ERP** (Enterprise Resource Planning): sistema integrado para administrar y

automatizar los principales procesos internos de la organización, como
contabilidad, compras, inventarios, producción, ventas y nómina.


**CRM** (Customer Relationship Management): sistema para gestionar la

información de clientes, ventas, mercadeo y servicio al cliente a lo largo
de todo el ciclo de la relación comercial.


**SCM** (Supply Chain Management): sistema para planificar y gestionar la

cadena de suministro, incluyendo compras, inventarios, logística,
distribución y la relación con los proveedores.


**HCM** (Human Capital Management): sistema para administrar el talento

humano, que incluye selección, contratación, capacitación, evaluación
del desempeño y desarrollo profesional.


Además de estos sistemas, las organizaciones utilizan aplicaciones
especializadas como WMS, TMS, MES, PLM y EAM, todas ellas
soportadas por bases de datos relacionales y potenciales fuentes de
información para un Data Warehouse.

<!-- fin de página 8 -->

##### 1984 — Classification and Regression Trees (CART)

¿Cómo pueden construirse reglas de
decisión automáticamente a partir de los
datos para clasificar casos o predecir
valores?


**Classification and Regression**

**Trees (CART):** metodología de
aprendizaje supervisado
introducida por Breiman,
Friedman, Olshen y Stone para
construir árboles de decisión

mediante particiones sucesivas
de los datos, aplicable tanto a
problemas de clasificación
como a problemas de regresión.
La monografía original de 1984
formalizó precisamente el uso
de reglas con estructura de
árbol para el análisis de datos.



**Idea clave:**

Los árboles transforman relaciones
complejas entre variables en una
secuencia interpretable de reglas de
decisión, aprendidas directamente a
partir de los datos.

```
if x2 > C then

class = azul

else

if x1 < A then

class = verde

else

if x2 < B then
class = rojo
else

class = amarillo

end if

end if

end if

```

<!-- fin de página 9 -->

### Las empresas ya tenían datos. El problema era recordar.

<!-- fin de página 10 -->

##### 1985 — Data Warehouse

¿Cómo puede conservarse la
información histórica si las bases de
datos operacionales sobrescriben
continuamente los datos?


**Data Warehouse** : Repositorio corporativo

orientado al análisis, diseñado para
integrar y conservar información histórica
proveniente de las diferentes bases de
datos de la organización (por ejemplo,
ventas, nómina, inventarios y
contabilidad), proporcionando una visión
integrada para la consulta y el análisis.


Arquitectura:

 - Orientado a temas

  - Integrado

  - Orientado al análisis y consulta


Información:

  - No volátil

  - Variable en el tiempo

  - Histórico.



**RDBMS**


- Sistemas funcionales

- Sistemas integrados


**ETL**


Fuentes

externas



**Data**

**warehouse**



**Idea clave:**
El Data Warehouse preserva la
memoria histórica de la organización
para apoyar el análisis y la toma de
decisiones.


Consulta de datos:

- SQL (usuarios técnicos)

- Generadores de reportes (FOCUS, Cognos

QUIZ/PowerHouse, Crystal Reports)

- EIS (Executive Information Systems)

<!-- fin de página 11 -->

##### 1985 — ETL

¿Cómo puede mantenerse actualizado
un Data Warehouse alimentado por
múltiples sistemas de información?


**ETL (Extract, Transform, Load)** : Proceso

de **EXTRACCIÓN**
(obtención de
información de diferentes sistemas de la
**TRANSFORMACIÓN**
organización),
(preparación de la información para
facilitar su análisis, corrigiendo errores,
eliminando duplicados y unificando
formatos) y **CARGA** (almacenamiento de la
información procesada en el Data
Warehouse para su consulta y análisis).



**RDBMS**


Fuentes

externas



**Data**

**warehouse**



**ETL**



Características



**Idea clave:**
Los procesos ETL integran, transforman
y consolidan la información corporativa.


- Automatiza la actualización periódica

del Data Warehouse.

- Corrige errores, elimina registros

duplicados y unifica los formatos de la
información.

- Integra información proveniente de

múltiples bases de datos de la
organización.

- Puede ejecutarse por lotes (batch) o

en tiempo real (stream).

- Puede iniciarse manualmente,

mediante programación o mediante
eventos de monitoreo.

<!-- fin de página 12 -->

##### ¿Quién es realmente tu mejor cliente?

¿Qué podemos descubrir de un cliente
al analizar toda su historia y no solo una
transacción?



**Idea clave:**
Una transacción representa una
operación. La historia revela el
comportamiento.


Los mejores clientes no eran
necesariamente los grandes
apostadores.



**Una transacción**


¿Cuánto gastó hoy?
¿Qué hizo en esta visita?



**Su historia**


¿Con qué frecuencia viene?
¿Qué actividades prefiere?
¿Cómo responde a las promociones?
¿Cuánto valor genera a lo largo del tiempo?

<!-- fin de página 13 -->

##### 1989 — Business Intelligence 1.0 (1989)

¿Cómo pueden responderse nuevas
preguntas de negocio cuya información
no está disponible en los EIS ni en los
sistemas operacionales?


**Business Intelligence 1.0** : Conjunto de



**Idea clave:**
Los ejecutivos solicitan al área de TI la
construcción de nuevos reportes,
indicadores y tableros a partir de la
información almacenada en el DW



herramientas, productos y tecnologías
**consultar** **visualizar** **analizar** la
para, y

en una
**información disponible**
organización, que apoya la generación de
reportes, indicadores y tableros para la
toma de decisiones.

Entre sus tareas típicas se encuentran:


 - Visualización de información.

 - Cálculo de indicadores (KPIs).

 - Dashboards ejecutivos.

 - Reportes automáticos.

 - Consultas ad hoc.



**RDBMS**


- Sistemas funcionales

- Sistemas integrados


**ETL**


Fuentes

externas


# ?



Nueva Pregunta de Negocio



**Data**

**warehouse**



|Gerencia|Col2|
|---|---|
|ocio|ocio|
|Departamento de<br>TI|Departamento de<br>TI|
|||


Consulta de datos:

- SQL (usuarios técnicos)

- Generadores de reportes (FOCUS, Cognos

QUIZ/PowerHouse, Crystal Reports)

- EIS (Executive Information Systems)

<!-- fin de página 14 -->

##### 1989 — Data Mining

¿Cómo pueden descubrirse
automáticamente patrones ocultos en
grandes bases de datos?


**Data Mining** : Proceso computacional para

descubrir patrones, tendencias y
relaciones útiles en grandes conjuntos de
datos mediante la aplicación de métodos
estadísticos a la información almacenada
en bases de datos. Entre sus tareas típicas

se encuentran:


  - Descubrimiento de reglas de



**Data**

**warehouse**



**RDBMS**


- Sistemas funcionales

- Sistemas integrados


# ?



**Idea clave:**

Los modelos estadísticos comienzan a
utilizarse para descubrir conocimiento
almacenado en bases de datos.


Gerencia


Nueva pregunta

de negocio


Analistas de


Datos



asociación.

**warehouse**

- Clasificación.

- Regresión.

- Agrupamiento (clustering).

- Detección de anomalías. **Data** SAS / SPSS /



**ETL**



Clementine


El analista reemplaza la
consulta por la construcción
de un modelo que descubre
conocimiento oculto en los

datos.




- Un modelo de clasificación

- Un modelo de regresión

- Reglas de asociación

- Segmentaciones

- Árboles de decisión

- Un informe técnico con


hallazgos



Fuentes

externas

<!-- fin de página 15 -->

##### 1989 — KDD

¿Cómo puede estructurarse un proceso
sistemático para descubrir conocimiento
a partir de los datos?


**KDD (Knowledge Discovery in**

**Databases)** : proceso iterativo
para descubrir conocimiento
útil en bases de datos, que
comprende la selección,
preparación, transformación,
minería e interpretación de los
datos.



**Proceso KDD**



**Idea clave:**
KDD formaliza las etapas necesarias
para descubrir conocimiento útil a partir
de grandes volúmenes de datos.


**Interpretación,**



**Selección** **Preproceso** **Transformación** **Data Mining**



**evaluación y**

**despliegue**



El despliegue puede ser:

- un modelo implementado;

- un sistema de soporte a decisiones;

- un reporte automatizado;

- un proceso de negocio modificado;

- una aplicación que utiliza el modelo;

- una campaña de mercadeo basada en el

modelo.

<!-- fin de página 16 -->

##### 1993 — Sistemas OLAP

¿Cómo puede organizarse y
consultarse eficientemente la

información almacenada en un Data

Warehouse?


:
**OLAP (Online Analytical Processing)**

Tecnología para agilizar la consulta y el
análisis de grandes volúmenes de
información mediante estructuras

multidimensionales que permiten explorar
los datos desde diferentes perspectivas.



**RDBMS**


- Sistemas funcionales

- Sistemas integrados


**ETL**


Fuentes

externas



**Data**

**warehouse**



**Idea clave:**
Los sistemas OLAP permiten realizar
consultas multidimensionales rápidas e
interactivas sobre grandes volúmenes
de información.


**Cubo**

**OLAP**
**Usuario**


Consultas iterativas y

toma de decisiones

(Inteligencia de negocios)

<!-- fin de página 17 -->

##### 1993 — Cubo OLAP

¿Cómo puede organizarse la misma
información para analizarla desde
múltiples perspectivas?


**Tabla bidimensional**
**Cubo OLAP**


```
Fecha Producto Ciudad  Ventas
Ene  A     Bogotá  120
Ene  A     Medellín 150
Ene  B     Bogotá  90
Ene  B     Medellín 110
Feb  A     Bogotá  130
Feb  A     Medellín 170
Feb  B     Bogotá  95
Feb  B     Medellín 125

```


Las dimensiones son:

- Fecha

- Producto

- Ciudad


La medida es:

- Ventas



**Idea clave:**
El cubo OLAP organiza las medidas de
negocio a través de múltiples
dimensiones, lo que permite analizar la
misma información desde diferentes
perspectivas.

```
Producto = A

Fecha

Ene Feb

Ciudad
Bogotá  120 130
Medellín 150 170

Producto = B

Fecha

Ene Feb

Ciudad
Bogotá  90  95
Medellín 110 125

```

<!-- fin de página 18 -->

##### 1995 — Statistical Machine Learning

¿Cómo pueden construirse modelos
predictivos que aprendan patrones a
partir de ejemplos y generalicen a datos
no observados?


**Statistical Machine Learning**



**Idea clave:**
El aprendizaje estadístico desplaza el
énfasis desde programar explícitamente
las reglas hacia aprender funciones
predictivas a partir de los datos.



**(Aprendizaje Estadístico):**
enfoque para construir modelos
que aprenden relaciones y
patrones a partir de datos,
utilizando principios estadísticos
para realizar predicciones o
clasificaciones y generalizar a
observaciones no utilizadas

durante el entrenamiento.



→
Árbol
particiones rectangulares


→
SVM hiperplano de máximo margen


→
Boosting combinación de clasificadores débiles

<!-- fin de página 19 -->

##### 1996 — Data Marts

¿Cómo puede proporcionarse a cada
área de negocio una vista especializada
de la información corporativa?


**Data Mart** : subconjunto de vistas de datos

de un Data Warehouse orientado a la

consulta. Es implementado usando cubos
OLAP


**RDBMS**


**ETL**


Fuentes

externas



Data

Marts



Cubo

OLAP



**Idea clave:**
Los Data Marts especializan la
información corporativa para las
necesidades analíticas de áreas
específicas del negocio.


Usuario


Usuario



**Data**

**warehouse**



Cubo

OLAP

<!-- fin de página 20 -->

##### 1996 — CRISP-DM (Cross-industry standard process for data mining)

¿Cómo puede incrementarse la
probabilidad de éxito de los proyectos
de minería de datos?


**CRISP-DM** : metodología estándar para

planificar, desarrollar e implementar
proyectos de minería de datos,
transformando problemas de negocio en
soluciones analíticas mediante un proceso
sistemático y repetible.



**Idea clave:**
CRISP-DM incorpora el entendimiento
del negocio y estandariza el desarrollo
de proyectos de minería de datos.



Comprensión

del negocio



Comprensión

de los datos



Preparación de

Modelado Evaluación Distribución
los datos

<!-- fin de página 21 -->

##### 1996 — Business Intelligence 2.0

¿Cómo puede evitarse que el área de TI
se convierta en un cuello de botella al
responder preguntas de negocio?


**Inteligencia de Negocios 2.0** : conjunto de

herramientas y servicios para explorar,
analizar y visualizar la información
organizacional, que permite a los usuarios
de negocio realizar consultas interactivas y
apoyar la toma de decisiones tácticas y
estratégicas.


Características / Capacidades:

- Consultas interactivas (OLAP).

- Reportes.

- Dashboards (cuadros de mando).

- Gráficos.

- Mapas.

- Integración de Data Warehouses, Data

Marts y cubos OLAP.




|Col1|Col2|Col3|Col4|Idea clave:<br>Las herramientas de Business<br>Intelligence permiten a los usuarios de<br>negocio explorar y analizar<br>directamente la información.|
|---|---|---|---|---|
||||negocio explorar y analizar<br>directamente la información.|negocio explorar y analizar<br>directamente la información.|
||||||
||||||
||||||

<!-- fin de página 22 -->

##### 1996 — Data Science

¿Cómo puede extraerse conocimiento
mediante el análisis de datos

almacenados electrónicamente?


**Ciencia de datos** : campo interdisciplinario

que desarrolla y aplica métodos, procesos
y sistemas para analizar datos
almacenados electrónicamente y extraer
conocimiento de ellos, ya sean
estructurados, semiestructurados o no
estructurados. Domina el software

propietario (S-PLUS, SPSS, Minitab,
Oracle, …)



**Idea clave:**
La Ciencia de Datos integra múltiples
disciplinas para extraer conocimiento a
partir de datos almacenados
electrónicamente.


**Aprendizaje**

**Inferencia**

**Limpieza**
**de Máquinas**

**Estadística**

**de Datos**



**Programación**



**Visualización**


**de Datos**



**Modelos**
**Productos de**
**Estadísticos**

**Datos**



**Experticia en el**

**problema**



**Adquisición de** **Computación**

**Datos** **Reproducible**



Definición del Análisis

Ingestión Limpieza Modelado
Problema Exploratorio

<!-- fin de página 23 -->

##### ¿Por qué Data Science transformó la industria?

¿Por qué Data Science se convirtió en
una de las disciplinas más demandadas
del siglo XXI?



**Idea clave:**
La disponibilidad masiva de datos y el
desarrollo de nuevas tecnologías
impulsaron una rápida adopción de la
ciencia de datos en la industria, el
gobierno y la academia.


Google Trends para “Data Science” y

“Business Analytics”

<!-- fin de página 24 -->

##### 2001 — Ensemble Learning

¿Puede la combinación de varios
modelos producir predicciones mejores
y más robustas que un único modelo?


**Ensemble Learning (Aprendizaje por**

**conjuntos):** enfoque de aprendizaje
automático que combina las predicciones
de múltiples modelos para obtener un
modelo conjunto con mayor precisión,
estabilidad o capacidad de generalización
que sus componentes individuales.


**Random Forest** : muchos árboles


entrenados sobre muestras/variables

→
diferentes votación o promedio.


**Gradient Boosting** : árboles construidos

secuencialmente, donde cada nuevo
modelo intenta corregir los errores de los

→
anteriores suma de modelos.



**Idea clave:**
En lugar de depender de un solo
modelo, los métodos de ensamblaje
combinan múltiples modelos para
mejorar la capacidad predictiva y de
generalización.


→ → →
Datos Modelo 1 + Modelo 2 + Modelo 3 + … combinación Predicción final

<!-- fin de página 25 -->

##### 2002 — Cloud computing

¿Cómo puede accederse de forma
flexible y bajo demanda a
infraestructura computacional sin
adquirir infraestructura propia?


      - Espacio físico.


     - Costos de compra y obsolescencia


     - Costos de mantenimiento y energía.


     - Atención en picos de carga y

subutililzación la mayor parte del
tiempo


     - Gestión de riesgos.



**Computación local**

(Servers on premises)
Servidores + red + clientes





**Idea clave:**
La computación en la nube transforma
la infraestructura computacional en un
servicio escalable y bajo demanda,
impulsando el desarrollo de
aplicaciones analíticas y Big Data.


- No requiere espacio físico.


- Rentados


- Escalable bajo demanda.


- Gestión de riesgos manejados por el

proveedor.



Máquina Local

|Cloud computing / Utility computing (Servers on the cloud)|Col2|
|---|---|
|Almacenamiento<br>Cómputo<br>Bases de Datos|Almacenamiento<br>Cómputo<br>Bases de Datos|
||Internet|


(Cliente)

<!-- fin de página 26 -->

##### 2002 — Modelos de servicio en la nube

**Idea clave:**

Los servicios en la nube ofrecen
distintos niveles de abstracción, desde
**¿Por qué es importante en** la infraestructura hasta las aplicaciones











**Tendencias actuales:**


- Low-code/No-code: desarrollo con

poca o ninguna programación.

- Vibe Coding: desarrollo asistido por

modelos de IA generativa.

- Serverless Computing: las aplicaciones

se ejecutan sin necesidad de
administrar servidores.

- AI as a Service (AIaaS): consumo de

modelos de IA como servicio (OpenAI,
Gemini, Claude, Azure AI).


|Modelo|¿Qué ofrece?|Ejemplos|¿Por qué es importante en<br>analítica?|
|---|---|---|---|
|**IaaS**<br>Infrastructure as a<br>Service|Servidores virtuales,<br>almacenamiento, redes y<br>capacidad de procesamiento.|AWS EC2, Azure Virtual<br>Machines, Google Compute<br>Engine|Permite ejecutar Hadoop,<br>Spark, bases de datos y<br>clústeres sin comprar<br>servidores,|
|**PaaS**<br>Platform as a Service|Plataformas administradas para<br>desarrollar y desplegar<br>aplicaciones.|Azure App Service, Google<br>App Engine, Heroku|Facilita crear aplicaciones<br>analíticas sin administrar la<br>infraestructura.|
|**SaaS**<br>Software as a Service|Aplicaciones completas<br>accesibles mediante navegador<br>o cliente.|Power BI, Tableau Cloud,<br>Microsoft 365, Salesforce|El usuario consume<br>herramientas analíticas sin<br>instalar ni mantener software.|
|**FaaS**<br>Function as a Service|Ejecución de funciones bajo<br>demanda (serverless).|AWS Lambda, Azure<br>Functions, Google Cloud<br>Functions|Automatiza procesos de<br>datos, APIs y flujos de IA<br>pagando únicamente por<br>ejecución.|

<!-- fin de página 27 -->

##### 2005 — Hadoop / MapReduce

¿Cómo pueden procesarse grandes
volúmenes de información distribuida
entre cientos de computadores?


**Aproximación Tradicional**
**(RDBMS y data warehouse)**


**Escritura**


**Lectura**


         Alto volumen de datos

         Lectura lenta

         Escritura + lenta

         Búsqueda ++ lenta


RDBMS

         Orientado a filas

         Estructura fija

         SQL

         Consistencia

         Integridad referencial

         Abstracción



**Almacenamiento**

**distribuido**



**Procesamiento**

**distribuido**


**Necesidad de poder de cómputo**



**Idea clave:**
Big Data combina almacenamiento y
procesamiento distribuidos.



Hadoop
Distributed


Filesystem

(HDFS)



**Necesidad de gestión de memoria**



**Nodos de Datos + Nodos de Computo**



**Las cinco Vs**

- Volumen (Cuántos?)

- Variedad (Tipo?)

- Velocidad (Frecuencia?)

- Veracidad (Precisión?)

- Valor (Utilidad?)

<!-- fin de página 28 -->

##### Algoritmo MapReduce

#### **DATOS**

A A C


#### **MAP**

**<Clave, Valor>**


**<A, 1>**
**<A, 1>**
**<C, 1>**


<C, 1>

<B, 1>
<D, 1>


<A, 1>
<C, 1>
<D, 1>


#### **JOB**


#### **SHUFFLE** **& SORT**

**<A, 1>**
**<A, 1>**
**<A, 1>**


**<B, 1>**


**<C, 1>**
**<C, 1>**
**<C, 1>**


**<D, 1>**
**<D, 1>**


#### **REDUCE**

**<Clave, *>**


**<A, 3>**


**<B, 1>**


**<C, 3>**


**<D, 2>**



**A A C**

**C B D**

**A C D**



C B D


A C D


#### **RESULTADO**

**<A, 3>**

**<B, 1>**
**<C, 3>**
**<D, 2>**

<!-- fin de página 29 -->

##### Ejecución de Jobs en Hadoop

¿Cómo ejecuta Hadoop procesos
complejos sobre grandes volúmenes de
datos?


**Job** : Unidad de ejecución en Hadoop que

aplica una o más operaciones Map y
Reduce sobre datos almacenados en

HDFS para producir un resultado.


**JOB**



**Idea clave:**
Los problemas complejos se resuelven
mediante la ejecución secuencial o en
paralelo de múltiples jobs de
MapReduce.


|JOB 1 JOB 2 JOB 3 JOB 4|Col2|JOB 2|Col4|JOB 3|Col6|JOB 4|Col8|
|---|---|---|---|---|---|---|---|
|**R**<br>**M**<br>**R**<br>**M**<br>**R**<br>**M**<br>**R**<br>**M**|**R**<br>**M**<br>**R**<br>**M**<br>**R**<br>**M**<br>**R**<br>**M**|**R**<br>**M**||**R**<br>**M**||**R**<br>**M**||
|**R**<br>**M**<br>**R**<br>**M**<br>**R**<br>**M**<br>**R**<br>**M**|**R**<br>**M**|**R**<br>**M**|**R**<br>**M**|**R**<br>**M**|**R**<br>**M**|**R**<br>**M**|**R**<br>**M**|
|||||||||









SS



**JOB 2**



**JOB 4**



**HDFS**









**HDFS**







**JOB 5**




|M R|Col2|
|---|---|
|**R**<br>**M**||

<!-- fin de página 30 -->

##### ¿Cuál es la principal limitación en Hadoop?

¿Qué ocurre cuando un problema
requiere ejecutar múltiples Jobs de
MapReduce?


**JOB 1** **JOB 2** **JOB 3**


**M** **R** **M** **R** **M** **R**


**HDFS**



**Idea clave:**

El almacenamiento intermedio en HDFS
y el lanzamiento repetido de Jobs
introducen una sobrecarga significativa
en aplicaciones analíticas complejas.


Sistemas Hadoop
tradicionales

Costos asociados a:

              - Movimiento de los datos.

              - Lanzamiento de los procesos.

             - Tiempos de comunicación.


Volumen de datos

<!-- fin de página 31 -->

##### ¿Por qué analítica?

¿Por qué los datos se han convertido en
uno de los principales activos de las
organizaciones?


**Antes** :


                   - Experiencia.

                    - Intuición.

                  - Reportes.

                  - Decisiones periódicas.



:
**Hoy**


- Datos.

- Modelos.

- IA.

- Decisiones en tiempo real.



**Idea clave:**
Las organizaciones que convierten
datos en decisiones obtienen ventajas
competitivas sostenibles.

<!-- fin de página 32 -->

##### Casos de éxito

¿Cómo aporta valor la analítica en las
organizaciones?


**Organización** **Problema de negocio** **Aplicación de analítica**



**Idea clave:**
La analítica no pertenece a un sector;
se ha convertido en una capacidad
transversal de prácticamente todas las
organizaciones.



Amazon ¿Qué productos ofrecer a cada cliente? Recomendación personalizada de productos.


Netflix ¿Qué contenido mantener viendo al usuario? Recomendación personalizada de películas y series.


Google ¿Qué resultados y anuncios mostrar? Búsqueda inteligente y publicidad personalizada.


Uber ¿Cómo equilibrar oferta y demanda? Tarifas dinámicas y asignación de conductores.


Spotify ¿Qué música recomendar? Descubrimiento y recomendación personalizada.


Walmart ¿Qué cantidad de productos abastecer? Pronóstico de demanda y optimización de inventarios.


JPMorgan Chase ¿Cómo reducir el fraude financiero? Detección automática de transacciones anómalas.


Tesla ¿Cómo mejorar la seguridad de la conducción? Análisis en tiempo real de datos de sensores.

<!-- fin de página 33 -->

### Tener datos ya no era suficiente. Había que convertirlos en una ventaja.

<!-- fin de página 34 -->

##### Moneyball

**¿Cómo competir contra alguien que tiene mucho más dinero que tú?**


**Oakland Athletics**
Uno de los presupuestos más bajos de las Grandes Ligas.


Imaginen que dirigen un equipo de béisbol.


Sus competidores pueden gastar muchísimo más que ustedes. Si todos evalúan a los jugadores de la

misma manera, ustedes tienen un problema: cuando aparece un gran jugador, los equipos ricos
pueden simplemente pagar más.


Billy Beane y los Oakland Athletics hicieron una pregunta diferente:


**¿Y si el mercado está equivocado sobre cuánto vale un jugador?”**


**No necesitaban tener más dinero. Necesitaban tomar mejores decisiones.**

<!-- fin de página 35 -->

##### 2006 — Business Analytics

¿Cómo pueden utilizarse los datos en
las organizaciones para mejorar la toma
de decisiones y generar ventajas
competitivas?


**Business Analytics** : Campo

interdisciplinario que integra datos,
métodos matemáticos, estadísticos y
computacionales, junto con técnicas de
simulación, optimización y apoyo a la
decisión, para mejorar la toma de
decisiones, el desempeño y la generación
de ventajas competitivas en las
organizaciones.


**Competing on Analytics (Davenport, 2006)** consolidó el
concepto de Business Analytics al integrar una tradición
proveniente de los sistemas de apoyo a la decisión (DSS), la
inteligencia de negocios (BI), la investigación de operaciones
(Operations Research), la minería de datos y los métodos
cuantitativos, demostrando que su uso sistemático podía
convertirse en una fuente sostenible de ventaja competitiva.



**Idea clave:**
Business Analytics amplía la inteligencia
de negocios al incorporar modelos
predictivos y prescriptivos para apoyar
la toma de decisiones.

<!-- fin de página 36 -->

##### Tipos de Analitica



**Analítica Descriptiva**

Análisis de la situación actual para la toma de decisiones
operativas


**Analítica Diagnóstica**

Análisis orientado a identificar las causas y factores que
explican por qué se observó un resultado o
comportamiento.


**Analítica Predictiva**

Área enfocada en el uso de técnicas de modelado
predictivo, aprendizaje de máquinas y minería de datos
para pronosticar los resultados de un proceso en un
contexto organizacional.


**Analítica Prescriptiva**

Uso de técnicas de simulación, optimización y análisis de
riesgo e incertidumbre para la toma de decisiones
organizacionales

<!-- fin de página 37 -->

##### 2008 — Pig Latin

¿Cómo pueden desarrollarse
aplicaciones para Hadoop sin
programar directamente en
MapReduce?


**Apache Pig** : lenguaje de alto nivel similar a

SQL que permite desarrollar aplicaciones
para el análisis de grandes volúmenes de
datos en Hadoop mediante flujos de datos
(data flows), los cuales son traducidos
automáticamente a programas
MapReduce.



**Idea clave:**
Pig introduce un lenguaje de alto nivel
para programar procesos distribuidos.


```
CROSS

EXLAIN

FILTER

FOREACH

GENERATE

GROUP

ILLUSTRATE

JOIN

LIMIT

LOAD

ORDER

STREAM

SPLIT

STORE

SET
QUIT

```


Ejemplo de Pig

```
 records = LOAD 'sample.txt' AS (year:chararray, temperature:int, quality:int);

 filtered_records = FILTER records BY temperature;

 grouped_records = GROUP filtered_records BY year;

 max_temp = FOREACH grouped_records GENERATE group, MAX(filtered_records.temperature);

 DUMP max_temp;

```

<!-- fin de página 38 -->

##### 2011 — Data Lake

¿Cómo pueden almacenarse grandes
volúmenes de datos estructurados,
semiestructurados y no estructurados
para su análisis posterior?


**Data Lake** : Arquitectura de



almacenamiento orientada a Big
Data que proporciona un
repositorio centralizado para
almacenar grandes volúmenes de
datos estructurados,
semiestructurados y no
estructurados en su formato

original, permitiendo su
procesamiento y análisis
posteriores mediante tecnologías
de Big Data y analítica avanzada.



RDBMS


Archivos y

registros



Logs y registros

de aplicaciones


Documentos


Correos

electrónicos



**Data Lake**



**Idea clave:**
A diferencia del Data Warehouse, el
Data Lake almacena los datos en bruto,
lo que permite definir su estructura
únicamente cuando se utilizan para el
análisis.


Aplicaciones
empresariales


**Data**

**ETL**
Business Intelligence

**warehouse**


**Hadoop**
**ecosystem**


Business Analytics

<!-- fin de página 39 -->

##### 2009 — Datos semi-estructurados y bases de datos NoSQL



¿Cómo pueden almacenarse grandes
volúmenes de datos en estructuras
flexibles que no se ajustan al modelo
relacional?


**Bases de datos NoSQL:** sistemas

de gestión de bases de datos no
relacionales diseñados para
almacenar grandes volúmenes de
datos estructurados,
semiestructurados y no
estructurados mediante modelos

de datos flexibles y escalables.


**Pares <clave, valor>**
```
  Tabla 001 .Fecha=2017-10-01

  Tabla 001 .Planta=Jaguas

  Tabla 001 .Generación=100.2

  Tabla 002 .Fecha=2017-10-01

  Tabla 002 .Planta=Playas

  Tabla 002 .Generación=23.1

  Tabla 003 .Fecha=2017-10-01

  Tabla 003 .Planta=Guatapé

  Tabla 003 .Generación=130.1

```

|KEY|Fecha|Planta|Generación|
|---|---|---|---|
|**`001`**|`2017-10-01`|`Jaguas`|`100.2`|
|**`002`**|`2017-10-01`|`Playas`|`23.1`|
|**`003`**|`2017-10-01`|`Guatape`|`130.1`|



**Document (JSON/XML)**
```
[
 {
Fecha:2017-10-01,

Planta:Jaguas,

Generación: 100.2

 },{
Fecha:2017-10-01,

Planta:Playas,
Generación:23.1,

 },{
Fecha:2017-10-01,

Planta:Guatapé,

Generación:130.1

 }
]

```


**Column family database**
```
001:{Fecha:2017-10-01, Planta:Jaguas, Generación:100.2}
002:{Fecha:2017-10-01, Planta:Playas, Generación:23.1}
003:{Fecha:2017-10-01, Planta:Guatapé, Generación:130.1}

```


**Datos tabulares**



**Sistema orientado a filas**
```
001 :2017-10-01,Jaguas,100.2
002 :2017-10-01,Playas,23.1
003 :2017-10-01,Guatape,130.1

```


**Idea clave:**
Las bases de datos NoSQL amplían el
paradigma relacional mediante modelos
de datos flexibles diseñados para
aplicaciones Big Data y sistemas
distribuidos.


**YAML**

```
   001 :

    Fecha: 2017-10-01

    Planta: Jaguas

    Generación: 100.2

   002:

    Fecha: 2017-10-01

    Planta: Playas
    generación: 23.1

   003 :

    Fecha: 2017-10-01

    Planta: Guatape

    Generación: 130.1

```

<!-- fin de página 40 -->

##### 2009-2012 — Open Data Science

¿Cómo puede desarrollarse la ciencia
de datos sin depender de plataformas
propietarias?



**Idea clave:**
El software de código abierto transformó
la ciencia de datos al hacer accesibles
herramientas avanzadas para
investigadores, estudiantes y
organizaciones sin depender de
plataformas comerciales.



1996

Data Science
(software propietario)



2009-2012
Open Data Science
(software libre)



pandas
(primeras
versiones

públicas),
manipulación
eficiente de
datos tabulares.



NumPy, una
biblioteca

fundamental para
la computación
numérica en

Python.



**Open Data Science:**

movimiento basado en
software de código
abierto que impulsó la
adopción de lenguajes
como Python y R, junto
con sus ecosistemas

de bibliotecas, para el
desarrollo de

aplicaciones de ciencia
de datos.



IPython
Notebook, el
primer entorno
interactivo

basado en

notebooks

(precursor de
Jupyter).



Primera

versión

pública de
Python



Se crea el

Comprehensive R
Archive Network,
que impulsa la
distribución de

paquetes.



Jupyter, evolución
de IPython
Notebook hacia un

proyecto
independiente.



Matplotlib,
visualización
científica en
Python.



**2005**



**2001**



**2014**


Anaconda, distribución
integrada de Python
para ciencia de datos.



**2010**



**2011**



**2003**



**2012**



**2006**



**1991**



**1993**



**2008**



**2009**



**1995**



IPython, una
consola interactiva

para computación
científica.



scikit-learn, biblioteca
estándar de Machine

Learning para Python.


pandas (inicio del
proyecto): Wes
McKinney inicia el
desarrollo de pandas.



SciPy, biblioteca
científica para
Python.


Inicio del proyecto R
por Ross Ihaka y
Robert Gentleman.

<!-- fin de página 41 -->

### La analítica dejó de depender de unas pocas herramientas y organizaciones. Empezó a convertirse en un ecosistema.

<!-- fin de página 42 -->

##### 2010-2015 — Modern Analytics

¿Qué ocurre cuando Big Data, Machine
Learning y los ecosistemas abiertos
comienzan a converger?



**Idea clave:**
La analítica moderna emerge de la
convergencia entre nuevos ecosistemas
de software, Big Data, computación
distribuida y Machine Learning.


Data Lake



**1984**


**SPSS**



**1986**



**MATLAB**



**Clementine**



**Business**

**analytics**


NumPy


Apache
Pig



Primera

versión

pública de
Python



Cloud

Computing


Matplotlib



Open
data

science



**Entreprise**
**Miner**


**Ciencia**

**de datos**



**1966**



**SAS**


**1968**



**2003**



**2014**



**2012**



Apache
Spark


**2015**


Deep
Learning



**1994**


R



**1997**



**2005**



pandas


**2010**


NoSQL



**2011**



**1991**


**S-Plus**



**1993**



**2002**



**2006**


Hadoop



**2008**



**2009**



scikit-learn


**Modern**

**analytics**

<!-- fin de página 43 -->

##### 2011-2012 — Producto de Datos



¿Cómo pueden los datos transformarse
en aplicaciones que generen valor de
forma continua?


**Producto de datos:** aplicación



Estadística y
aprendizaje de

máquinas


Los datos

están listos


Inteligencia
de Negocios



Modelado de

datos



**Idea clave:**
Los productos de datos integran datos y
algoritmos para aprender
continuamente, adaptarse
automáticamente y generar valor de
forma escalable.


Generación,
agregación, análisis
y visualización de
datos del negocio



o servicio que integra datos y
algoritmos para generar
continuamente predicciones,
recomendaciones,
decisiones o información útil
y que, además, produce
nuevos datos que pueden
ser consumidos por otros
productos de datos o
procesos analíticos.



DW / OLAP



Minería de



Descubrimiento de
DW / OLAP patrones y tendencias
claves



Datos



Analytics



DW / OLAP
Hadoop & Spark

NoSQL …

<!-- fin de página 44 -->

##### UPS-ORION

**¿Cuánto vale ahorrar unos pocos kilómetros?**


13 kilómetros menos por conductor, cada día.


≈ 130 millones de millas menos al año

≈ 10 millones de galones de combustible ahorrados


**Una pequeña decisión × millones de veces = un impacto enorme**


→ → → → →
Datos algoritmo decisión operación nuevos datos nueva decisión


La analítica dejó de ser únicamente algo que alguien consultaba en una pantalla.

Empezó a formar parte de la operación.

<!-- fin de página 45 -->

##### 2011 — Big Data Analytics

¿Cómo pueden ejecutarse algoritmos
analíticos tradicionales sobre
plataformas Big Data?


**Big Data Analytics (Analítica de**

**Big Data):** Disciplina que aplica
métodos matemáticos,
estadísticos y computacionales
para descubrir conocimiento,
identificar patrones y apoyar la
toma de decisiones mediante el
análisis de grandes volúmenes
de datos estructurados,
semiestructurados y no
estructurados.



**Idea clave:**
Los algoritmos estadísticos y de
Machine Learning comienzan a
ejecutarse en arquitecturas distribuidas.


Estadística básica


Clasificación y regresión


Filtrado colaborativo



Agrupamiento


Reducción de dimensiones


Extracción de características


Minería de patrones frecuentes


Métricas de evaluación


Exportación de modelos


Optimización



Hive


Mahout


Pig



**Apache Mahout**
Implementación en Map/Reduce
(Java y otros) de los algoritmos
de aprendizaje estadístico y
aprendizaje de máquinas



HDFS



MapReduce


HBase

<!-- fin de página 46 -->

##### 2011 — Smart Factory

¿Cómo puede automatizarse
integralmente una fábrica mediante
tecnologías digitales?


**Smart Factory (Fábrica**

**Inteligente):** Sistema de
producción altamente
digitalizado que integra
sensores, sistemas ciberfísicos,
Internet de las Cosas, analítica e
Inteligencia Artificial para
monitorear, optimizar y
automatizar de forma autónoma

los procesos de manufactura.



**Idea clave:**
La Analítica pasa a formar parte de la
operación industrial.



https://www.avsystem.com/blog/smart-factory/

<!-- fin de página 47 -->

##### 2011-2012 — Auge del Deep Learning



¿Cómo pueden resolverse problemas
para los cuales los modelos
tradicionales resultan insuficientes?


**Deep Learning (Aprendizaje**

**Profundo):** Rama del
aprendizaje automático que
utiliza redes neuronales
artificiales con múltiples capas
para aprender automáticamente
representaciones jerárquicas y
patrones complejos a partir de
grandes volúmenes de datos,
permitiendo realizar tareas de
clasificación, predicción,
reconocimiento y generación de
información.



**¿Puede reconocer un gato sin que**

**nadie le enseñe qué es un gato?**



**Idea clave:**
Las redes neuronales profundas
amplían el conjunto de modelos
disponibles para resolver problemas
analíticos.



Red neuronal ejecutada en 1.000
computadores para etiquetar imágenes
tomadas aleatoriamente de YouTube.
Experimento desarrollado por
investigadores de Google Brain, entre
ellos Quoc Le y Andrew Ng.

<!-- fin de página 48 -->

##### 2012 — Transformación Digital

¿Cómo puede transformarse una
organización tradicional en una
organización digital?


**Transformación Digital:** Proceso

de integración de tecnologías
digitales en los procesos,
productos, servicios y modelos
de negocio de una organización
para generar valor, mejorar su
desempeño y transformar la
forma en que opera y compite.



**Idea clave:**
La transformación digital redefine cómo
una organización crea valor mediante la
integración de tecnologías digitales,
datos, procesos, personas y nuevas
formas de operar.

<!-- fin de página 49 -->

##### 2013 — Apache Hive

¿Cómo pueden consultarse grandes
volúmenes de datos almacenados en
Hadoop utilizando un lenguaje similar a
SQL?


**Apache Hive:** sistema de

almacenamiento y consulta de
datos que proporciona un
lenguaje similar a SQL (HiveQL)
para consultar y analizar
grandes volúmenes de datos
almacenados en Hadoop
mediante procesamiento
distribuido.



**Idea clave:**
Hive democratiza el acceso a Hadoop al
permitir que usuarios con conocimientos
de SQL analicen grandes volúmenes de
datos sin programar directamente en
MapReduce.

<!-- fin de página 50 -->

##### 2014 — Apache Spark

¿Cómo puede acelerarse el
procesamiento Big Data y simplificarse
su ecosistema?


**Apache Spark:** motor de

procesamiento distribuido de
código abierto que permite el
procesamiento y análisis de
grandes volúmenes de datos
mediante computación en
memoria, y que soporta
aplicaciones de analítica,
aprendizaje automático y
procesamiento de flujos de
datos.



HDFS


CASSANDRA


HBase


Hive



Fuentes

Streaming

posibles
de datos **Java**
#### **Spark**

MLlib **Scala**
**Machine** **Python**

**R**



MLlib

**Machine**



**Idea clave:**
Spark reconstruye el ecosistema de Big
Data sobre una arquitectura de
procesamiento en memoria.


Spark
SQL



GraphX



Spark
Streaming


#### **Spark**



https://spark.apache.org/mllib/

<!-- fin de página 51 -->

##### 2014-2016 — Gradient Boosting a Escala

¿Cómo puede llevarse a cabo el
boosting en conjuntos de datos grandes
manteniendo una alta precisión y
tiempos de entrenamiento prácticos?


**Gradient Boosting:** técnica de aprendizaje

supervisado que construye modelos de
forma secuencial, en la que cada nuevo
modelo intenta reducir los errores
residuales de la combinación previa.



**Idea clave:**
El gradient boosting se convierte en una
de las familias más competitivas para
datos tabulares al combinar precisión,
flexibilidad y escalabilidad.



→ → → → →
Modelo 1 errores Modelo 2 corrige errores restantes Modelo 3 corrige Predicción final


→ → →
Gradient Boosting XGBoost LightGBM CatBoost

<!-- fin de página 52 -->

##### Data Ops (2015)

¿Cómo pueden desarrollarse productos
de datos que evolucionen
continuamente?


**DataOps:** disciplina que integra


personas, procesos y
tecnologías para automatizar,
gestionar y monitorear el ciclo
de vida de los datos,
garantizando la calidad, la
confiabilidad y la entrega
continua de productos de
datos.


            - Notebooks interactivos

             - Visualización interactiva

           - Modelos

            - Presentaciones

            - Aplicaciones web inteligentes

            - Servicios RESTful

           - Dashboards



Depósito de



software



**Idea clave:**
Los productos analíticos pasan de ser
proyectos con un final definido a
convertirse en activos que evolucionan
junto con el negocio.



Equipos de desarrollo de

software


&

Científicos de datos



Pruebas



Analistas de datos


&

Científicos de datos


Diseño


Pruebas



Desarrollo Integración


Pruebas

<!-- fin de página 53 -->

##### 2015 — DataOps: Pipelines de Innovación y Valor



¿Cómo puede innovarse continuamente
sin afectar el producto que actualmente
genera valor?


**Heroísmo** : Trabajo fuera de
horario y fines de semana.


**Escenarios desastrosos** :

 - Despliegue de cambios que dañan


los sistemas productivos.

 - Entrega de datos de poca calidad a


los usuarios.


**Miedo** : Ausencia de confianza en

que los resultados sean correctos

o los cambios funcionen

correctamente.



**Idea clave:**
La experimentación se separa de la
operación para reducir el riesgo.


CALIDAD


DATA PRODUCCION VALOR


Ingestión Transformación Modelado Visualización Reporte



**Value**
**Pipeline**


CALIDAD


PRODUCCION


DESARROLLO



CALIDAD


**Value**
DATA PRODUCCION VALOR
**Pipeline**


DESARROLLO



Los tests sobre los datos en cada paso

garantizan la calidad de la salida



IDEA


**Innovation**
**Pipeline**



IDEA
**Innovation**

**Pipeline**

<!-- fin de página 54 -->

##### 2016 — Machine Learning Operations (MLOps)

¿Cómo pueden llevarse los modelos de
Machine Learning desde el laboratorio
hasta ambientes de producción?


**MLOps:** disciplina que integra


personas, procesos y
tecnologías para automatizar,
desplegar, monitorear y
gestionar el ciclo de vida de los
modelos de aprendizaje
automático, garantizando su
calidad, reproducibilidad,
confiabilidad y operación
continua en entornos de
producción.



**Idea clave:**
MLOps gestiona el ciclo de vida
completo de los modelos desplegados.


**-**
**Principios (ml** **[ops.org)](http://ml-ops.org)**


 - Unificación del ciclo de machine


learning y liberación de software


 - Pruebas automáticas de artefactos en


ML (validación de datos, pruebas de

modelos, pruebas de integración).


 - Soporte de modelos y datos para


construir modelos como elementos

principales en sistemas CD/CI


 - Reducción del débito técnico


 - MLOps como una práctica agnóstica


(de lenguajes, plataformas e

infraestructura).

<!-- fin de página 55 -->

### Hasta aquí construíamos los modelos. ¿Qué ocurre cuando los modelos empiezan a ayudarnos a construir la analítica?

<!-- fin de página 56 -->

##### 2017-2023 — Foundation models

¿Cómo pueden desarrollarse modelos
reutilizables capaces de resolver
múltiples tareas analíticas?













**Idea clave:**

Los modelos fundacionales
proporcionan capacidades generales
que posteriormente pueden adaptarse a
distintos dominios.










|Col1|BERT: primer modelo de GPT-3: modelo de ChatGPT: Primera aplicación<br>lenguaje basado en lenguaje basado en de uso masivo basada en un<br>Transformer especializado Transformer capaz de modelo fundacional que<br>en comprender el resolver múltiples tareas permitió interactuar mediante<br>significado y el contexto mediante prompts, pero conversaciones en lenguaje<br>de los textos, pero no en sin interacción natural, pero limitada<br>generar lenguaje natural conversacional con el principalmente al intercambio<br>de forma fluida. usuario. de información textual.|Col3|
|---|---|---|
|**2023**<br>**2022**<br>**Foundation models**: <br>paradigma de modelos<br>preentrenados reutilizables<br>que sirven como base para<br>desarrollar aplicaciones en<br>múltiples tareas y dominios,<br>pero cuyo potencial todavía<br>no era accesible para la<br>mayoría de los usuarios.<br>**2021**<br>**2020**<br>**GPT-2**: modelo de<br>lenguaje basado en<br>Transformer<br>especializado en generar<br>texto coherente a partir<br>de un texto inicial, pero<br>no en resolver múltiples<br>tareas mediante<br>instrucciones.<br>**2019**<br>**2018**<br>**Transformer**: <br>arquitectura de redes<br>neuronales que permitió<br>desarrollar modelos de<br>lenguaje capaces de<br>comprender con mayor<br>precisión el contexto y<br>las relaciones entre las<br>palabras.<br>**2017**|**2023**<br>**2022**<br>**Foundation models**: <br>paradigma de modelos<br>preentrenados reutilizables<br>que sirven como base para<br>desarrollar aplicaciones en<br>múltiples tareas y dominios,<br>pero cuyo potencial todavía<br>no era accesible para la<br>mayoría de los usuarios.<br>**2021**<br>**2020**<br>**GPT-2**: modelo de<br>lenguaje basado en<br>Transformer<br>especializado en generar<br>texto coherente a partir<br>de un texto inicial, pero<br>no en resolver múltiples<br>tareas mediante<br>instrucciones.<br>**2019**<br>**2018**<br>**Transformer**: <br>arquitectura de redes<br>neuronales que permitió<br>desarrollar modelos de<br>lenguaje capaces de<br>comprender con mayor<br>precisión el contexto y<br>las relaciones entre las<br>palabras.<br>**2017**|**GPT-4, Claude, Gemini y**<br>**Llama**: nueva generación<br>de modelos fundacionales<br>capaces de comprender e<br>integrar múltiples tipos de<br>información, con mayores<br>capacidades de<br>razonamiento y adaptación<br>a diferentes aplicaciones.|

<!-- fin de página 57 -->

##### 2023-2024 — Multimodal Foundation Models

¿Cómo pueden integrarse diferentes
tipos de datos en un mismo modelo
para realizar tareas analíticas?


**Multimodal Foundation Model (Modelo**

**Fundacional Multimodal):** modelo capaz
de procesar, relacionar y generar
información proveniente de múltiples
modalidades, como texto, imágenes,
audio, video y datos estructurados.


Texto
Imágenes

Audio


Video

Datos



Multimodal

Foundation


Model



**Idea clave:**
Los modelos fundacionales dejan de
trabajar exclusivamente con texto y
comienzan a integrar múltiples
modalidades de información.


Clasificación

Predicción
Generación
Interpretación

<!-- fin de página 58 -->

##### 2025-2026 — AI-augmented Analytics
















|Col1|Col2|Col3|Idea clave:<br>La IA deja de limitarse a generar<br>respuestas y comienza a ejecutar tareas<br>analíticas mediante código,<br>herramientas especializadas y procesos<br>de razonamiento asistido.|Col5|
|---|---|---|---|---|
|||**Deep Research**: <br>herramienta capaz de<br>planifcar y ejecutar<br>investigaciones complejas,<br>consultando múltiples<br>fuentes de información,<br>pero que aún depende de<br>la supervisión del usuario.<br>**Claude Artifacts:**Entorno<br>interactivo que permite<br>desarrollar aplicaciones,<br>visualizaciones y<br>prototipos directamente a<br>partir de conversaciones,<br>pero sin automatizar<br>procesos analíticos<br>completos.|||
|**2023**|**2025**<br>**2026**<br>**2025**<br>**NotebookLM**: Asistente<br>basado en modelos<br>fundacionales especializado<br>en analizar, sintetizar y<br>razonar sobre colecciones de<br>documentos, pero limitado al<br>conocimiento contenido en<br>las fuentes proporcionadas.<br>**2024**<br>**Automatic Code Execution**: <br>Primera herramienta basada<br>en un modelo fundacional<br>capaz de generar, ejecutar y<br>corregir automáticamente<br>código para resolver tareas<br>analíticas, pero limitada a un<br>entorno de trabajo<br>específco.|**2025**<br>**2026**<br>**2025**<br>**NotebookLM**: Asistente<br>basado en modelos<br>fundacionales especializado<br>en analizar, sintetizar y<br>razonar sobre colecciones de<br>documentos, pero limitado al<br>conocimiento contenido en<br>las fuentes proporcionadas.<br>**2024**<br>**Automatic Code Execution**: <br>Primera herramienta basada<br>en un modelo fundacional<br>capaz de generar, ejecutar y<br>corregir automáticamente<br>código para resolver tareas<br>analíticas, pero limitada a un<br>entorno de trabajo<br>específco.|**2025**<br>**2026**<br>**2025**<br>**NotebookLM**: Asistente<br>basado en modelos<br>fundacionales especializado<br>en analizar, sintetizar y<br>razonar sobre colecciones de<br>documentos, pero limitado al<br>conocimiento contenido en<br>las fuentes proporcionadas.<br>**2024**<br>**Automatic Code Execution**: <br>Primera herramienta basada<br>en un modelo fundacional<br>capaz de generar, ejecutar y<br>corregir automáticamente<br>código para resolver tareas<br>analíticas, pero limitada a un<br>entorno de trabajo<br>específco.|**AI-Augmented Analytics**: <br>paradigma en el que la IA<br>participa activamente en la<br>preparación, análisis,<br>visualización e interpretación de<br>datos mediante herramientas<br>computacionales, pero no ejecuta<br>procesos organizacionales<br>completos de forma autónoma.|

<!-- fin de página 59 -->

##### 2026 — Agentic AI

¿Cómo pueden automatizarse procesos
completos mediante agentes
inteligentes capaces de tomar
decisiones y ejecutar acciones de forma
autónoma?


**Agentic AI:** paradigma de IA en el

que agentes inteligentes basados
en modelos fundacionales

planifican, razonan, utilizan
herramientas y ejecutan de forma
autónoma procesos completos
para alcanzar un objetivo definido
por el usuario.


:
**Capacidades de un agente inteligente**


 Comprende el objetivo planteado por el usuario.

 Planifica una estrategia para alcanzarlo.

 Utiliza herramientas como Python, SQL, APIs,

navegadores, bases de datos y aplicaciones

empresariales.

 Ejecuta tareas y toma decisiones intermedias.

 Evalúa los resultados y corrige errores.

 Continúa iterando hasta cumplir el objetivo.

 Presenta el resultado final al usuario.



**Idea clave:**
La IA deja de asistir al analista y
comienza a ejecutar procesos
completos de forma autónoma para
alcanzar objetivos definidos por el
usuario.

<!-- fin de página 60 -->

##### Especialización por áreas

¿Cómo pueden adaptarse los métodos
analíticos a las necesidades específicas
de cada dominio de aplicación?


**Domain Analytics (Analítica por**

**Dominio):** Aplicación de
métodos, modelos y tecnologías
analíticas para resolver
problemas específicos de un
área del conocimiento, una
industria o una función

organizacional.


         People / Human Resources Analytics


         Financial Analytics


         Accounting Analytics


         Marketing Analytics


         Inventory Analytics


         Demand Analytics


         Custumer Analytics



**Idea clave:**

Los mismos fundamentos analíticos
pueden aplicarse a múltiples dominios,
dando origen a disciplinas
especializadas adaptadas a sus datos,

<!-- fin de página 61 -->

##### Rutas de formación

> ⚠️ S01: página 62 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 62 -->

##### ¿Qué aprendieron las organizaciones en estos 50 años?

Registrar
↓

Recordar

↓

Analizar

↓
Aprender
↓

Decidir

↓

Actuar


Business Analytics es la historia de cómo las organizaciones aprendieron a

convertir datos en decisiones.


**Si una máquina puede analizar, recomendar, decidir y ejecutar… ¿qué queda**

**para nosotros?**

<!-- fin de página 63 -->

## Origen y Evolución de Business Analytics

> ⚠️ S01: página 64 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 64 -->
