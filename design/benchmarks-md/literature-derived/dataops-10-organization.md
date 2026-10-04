---
source: "design/benchmarks-pdf/literature-derived/dataops-10-organization.pdf"
source_sha256: b44d1ac8df33474a143431a3bdab8cad82a2dd9ec7ea1c1de65a2e396bcf7946
family: literature-derived
pages: 10
min_text_coverage: 0.987
pages_without_graphics: [2, 3, 4, 7, 8]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 9, 10]"
---
# Organización para DataOps

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

## Estructuras típicas

Tareas repetidas por

muchas personas


Trabajo en silos y
entendimiento mínmo del

trabajo paralelo


Altos costos debido al

trabajo mundano y

reptitivo


Alto nivel de burocracia,
procesos muy regulados


Altos costos debido al

trabajo mundano y

reptitivo


Alto nivel de
acoplamiento. Si algo

falla todo falla




- El equipo tiene unicamente científicos de


datos.

- No se requiere Big Data. El volumen de datos

es pequeño

### Large Scale DataOps


- El equipo tiene científicos de datos,

ingenieros de datos, ingenieros DevOps

- Operaciones de Big Data y MLOps Multi
escala son manejadas por el equipo


El código y la data crecen

independientemente



El código y la data crecen

independientemente

### Small Teams



Falta de trazabilidad para

el entrenamiento y
monitoreo de modelos

Artifactos no
reproducibles

### Big Data Ops



Artifactos no
reproducibles




- El equipo tiene cientificos de datos e

ingenieros de software

- Se requiere Big Data

- Focalización en un solo problema

### Hybrid Ops


- El equipo tiene cientificos de datos e

ingenieros de datos e ingenieros DevOps

- Big Data y MLOps están focalizadas en un

rango estrecho de operaciones manejadas
por el equipo


El código y la data crecen

independientemente



Altos costos debido al

trabajo mundano y

reptitivo


El código y la data crecen

independientemente


Altos costos debido al

trabajo mundano y

reptitivo


Monitoreo del modelo y

rentrenamiento


ineficientes

<!-- fin de página 2 -->

## Equipos organizados por función

Los equipos centralizados suelen ser
pequeños y tienen dificultades para crear
productos de datos complejos.


BI Analysts



Falta de consciencia de

como se contribuya a
los objetivos globales


División basada en


herramientas o
habilidades o experticia



Fuentes de


datos



Data

Science



Cuellos de


botella


Data
Engineering



Stakeholders


Data
Analysis



Casos de


uso


#### Proyecto Proyecto



Data

Engineers



Dificultad para generar

cambios en la

organización


###### Equipos



Data
###### por Maximiza la utilización de

Scientists



Data Warehouse y

almacenamiento


Coordinación
compleja entre

equipos


###### por función



capital humano escaso



IT
Operations



IT Security &

Data

Governance



IT

infrastructure



DB

Administrators


Equipos Ad hoc
Falta de capacidad de

formados por

atención de otros equipos



No hay
ownership



proyectos


Equipos mucho
menos productivos
que equipos estables



Grupos
centralizados

<!-- fin de página 3 -->

## Equipos organizados por dominio

Coordinación

mediante roles

jerárquicos


Coordinación
mediante capítulos y

comunidades de


interés


Coordinación

mediante un centro


de excelencia



Equipo
transversal de


especialista


Casos de


uso



Razones para preferir equipos organizados por dominio y
orientados a producto:


- Mayor credibilidad entre miembros.

- Facilidad de interacción

- Incentivos para hacer su trabajo más fácil.

- Altamente orientados a cumplir compromisos

- Claridad sobre el trabajo de cada miembro.

- Experticia del problema muy profunda

- Feedback de largo plazo

- Relaciones fuertes con clientes.

- Soporte de largo plazo a los productos

- Cumplen con objetivos de largo plazo de la organización



Dificultades para desarrollo
profesional, compartición de

conocimiento, contratación


#### Data platform team

Cada miembro

tiene destrezas


únicas


Independencia

entre grupos



Mejores prácticas y

consistencia entre

equipos

#### Equipo de Excelencia


Casos de


uso


**Los equipos planos autosuficientes**
**orientados al desarrollo de productos**

**completos**


#### Equipo Equipo

Respuesta

rápida


Equipo
transversal de


especialista



BI Analysts
Data Engineer
Data Scientist

#### Equipo


Altamente
efectivos para

DataOps


Casos de


uso



Dificultades para reuso de

código y desarrollo de

pipelines

<!-- fin de página 4 -->

## Habilidades del grupo Core (no son títulos ni personas)




















|Rol|Nombre del cargo|Responsabilidades|Habilidades|Herramientas|
|---|---|---|---|---|
|Data platform<br>administrator|Arquitecto de datos|Lagos de datos<br>Bodegas de datos<br>Data mars<br>Diseño de esquemas|**Infraestructura de datos**<br>ETL<br>Data sources|SQL<br>Talend<br>Hadoop<br>Hive<br>Spark|
|Data engineer|Arquitecto de datos<br>Modelador de datos<br>Administrador de bases de datos<br>Ingeniero de aseguramiento de la calidad de datos<br>Ingeniero ETL|Construcción de pipelines<br>Manejo de datasets en la<br>infraestructura de datos|Bases de datos<br>Programación<br>Infraestructura en la nube<br>Almacenamiento|SQL<br>Talend<br>Hadoop<br>Hive<br>Spark|
|Data Analyst<br>(BI analyst)|Diseñador de visualizaciones de datos<br>Analista de datos de negocio<br>Analista financiero<br>Analista de producto<br>Analista de marketing<br>Desarrollador de Tableau<br>Analista de reportes<br>Profesional de inteligencia de negocios|Consulta<br>Limpieza<br>Exploración<br>Interpretación<br>Visualizaciones<br>Tablas<br>Reportes|**Entendimiento y análisis de**<br>**datos que influencian las**<br>**decisiones.**<br>Programación<br>Estadística básica<br>Limpieza de datos<br>Visualización de datos|Excel<br>Tableau<br>Looker<br>Qlick View<br>Altryx<br>Sporfire|
|Data Scientist|Cientifico de machine learning<br>Ingeniero de machine learning<br>Analista cuantitativo<br>Programador de IA<br>Actuario|Modelos<br>Algoritmos|Experticia del problema<br>Estadística avanzada<br>Machine learning<br>Minería de datos<br>Programación avanzada<br>Visualización avanzada|R <br>Python<br>SAS<br>SPSS|
|DataOps Engineer||Orquestación del pipelines<br>Automatización de la calidad<br>Aprovisionamiento de ambientes<br>Despliegue a producción|Agile<br>DevOps<br>Control de procesos|Frameworks para tests de datos<br>Python<br>Scripts|
|Team lead||Rapidez en el desarrollo del<br>producto|||
|Solution expert|Senior data engineer<br>Senior data scientist|Construcción del producto<br>correctamente|||
|Stakeholder|Usuario||||

<!-- fin de página 5 -->

## Habilidades del grupo de soporte
















|Rol|Nombre del cargo|Responsabilidades|Habilidades|Herramientas|
|---|---|---|---|---|
|Data product owner|Gerente de producto|Responsable por el éxito del<br>producto de datos y represéntale al<br>usuario. Garantiza el producto de<br>datos correcto.|Data storytelling<br>Visualización||
|Domain expert||Provee experticia que no tiene el<br>grupo|||
|Analytics specialist||Experticia especifica en herramienta<br>y metodologías faltante en el grupo.|||
|Technical specialist|Software engineer<br>ML engineer<br>Security expert||||
|Data architects||Manejo del ciclo de vida de la base<br>de datos o solución de big data<br>usada para capturar, almacenar,<br>integrar y procesar datos.|||

<!-- fin de página 6 -->

## Habilidades del grupo de soporte


##### Amplitud de conocimiento



Los equipos tienden a ser

liderados por este tipo de



No mejoran el flujo de persona



trabajo del equipo



Dash-Shaped

(Generalist)


I-Shaped
(Specialist)


Conocimiento muy
profundo y específico

Creación de silos


Falta de visión


**Estos perfiles no**

**agregan valor**



T-Shaped
(Generalized Specialist)


Empatía y ayuda al equipo
Remueve cuellos de botella



Pi-Shaped
(Multi-skill)


Conocimiento amplio y
experticia en dos áreas


##### Equipos altamente productivos

M-Shaped

(Poly-skill)


Conocimiento amplio y
experticia en tres o más

áreas



E-Shaped
(Experticia,
Experiencia,
Exploración,

Ejecución)


##### **Perfiles difíciles de obtener**

<!-- fin de página 7 -->

## Equipos optimizados

#### **Production Environment**



Raw Lake Data Engineering Refined Data Data Science Data Visualization Data Governance



Data

Sources



Data

Platform

Team


Equipo
transversal de
especialistas Equipo
centralizado


Equipo
transversal de

especialistas


BI Analysts
Data Engineer

Data Scientist


BI Analysts
Data Engineer

Data Scientist



Falta de Comprensión
de las necesidades de


datos de los demás

s¡equipos


**Data Chief**

**Officer**



Clientes


BI Analysts


Data

Engineers

##### **Estructura centralizada** Cada miembro reporta a su grupo centralizado


Data

Scientists


DB

Administrators



Finanzas


Marketing



Proyecto


Proyecto

##### **Estructura descentralizada** Cada grupo reporta a su respectiva gerencia

<!-- fin de página 8 -->

## Construcción de credibilidad

> ⚠️ S01: página 9 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 9 -->

# Organización para DataOps

> ⚠️ S01: página 10 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 10 -->
