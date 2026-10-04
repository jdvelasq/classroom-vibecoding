---
source: "design/benchmarks-pdf/literature-derived/dataops-01-the-problem.pdf"
source_sha256: 3341453c6f3c8e2d976ffb2749c4232bd0cb2002519356bf5631787d718c3f17
family: literature-derived
pages: 10
min_text_coverage: 0.99
pages_without_graphics: [2, 3, 4, 5, 6, 7, 8, 9]
converter: "pymupdf4llm 0.0.27 + pymupdf 1.26.5 (por página, respaldo sin gráficos; limpieza v1)"
converted: 2026-10-04
warnings:
  - "páginas con poco texto: [1, 10]"
---
# Problemas y desafios con Data Analytics & Data Science

> ⚠️ S01: página 1 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 1 -->

### Los problemas reales y desafíos en Data Analytics

Los objetivos cambian constantemente


Los datos viven en silos


Los formatos de los datos no optimizados para

analytics



Pocas empresas logran ventajas reales y

muchas fracasan totalmente.


La poca calidad de los datos sigue siendo un

desafío serio.


Las organizaciones usan tecnología obsoleta o

errónea.


Inexperiencia de los científicos de datos y de

sus gerentes


Se sigue CRISP-DM y modelos de cascada


Las decisiones son influenciadas por factores
emocionales, situaciones y culturales y siguen

siendo basadas en experiencia e intuición



Existencia de errores en los datos


Malos datos arruinan buenos reportes


Fatiga por procesos manuales


Heroismo, esperanza y precaución


Falta de confianza en los datos


#### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.

<!-- fin de página 2 -->

### Brechas de conocimiento

##### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.



El científico de datos debe


focalizarse en habilidades
técnicas y usar las últimas

herramientas en DS/ML


DA y el desarrollo de
software son similares


Los lideres no tienen por que

saber DA


El modelo es sabio y

omnisciente




- Se debe facilitar la toma de mejores


decisiones.


- Desconexión entre habilidades que se piensa


necesitan y las que realmente se necesitan.


- Se confunde el éxito del modelo con su


máxima precisión.


- No hay un producto mínimo viable.


- No se tienen las habilidades para llevar un


modelo a producción (desarrollo de software).

<!-- fin de página 3 -->

### Brechas de conocimiento

##### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.



El científico de datos debe


focalizarse en habilidades
técnicas y usar las últimas

herramientas en DS/ML


DA y el desarrollo de
software son similares


Los lideres no tienen por que

saber DA


El modelo es sabio y

omnisciente



Entrada


Reglas


Entrada


Salida




- El código (lógica) es crítico.

- El testeo prueba la lógica contra ejemplos


(pruebas).

- El código es complejo y los datos son simples.

- Se usan datos ficticios o muestras de datos


reales.

- No se requiere HPC o hardware especializado.


Salida


##### Programación tradicional

Código

Hecho

manualmente



Algoritmo
Reglas
Código ya listo


           - La lógica y los datos son críticos.

           - El testeo se basa en precisión no en


##### ML/DA



ejemplos.

- El código es simple y la complejidad


está en los datos.

- Se usan datos de producción.

- Se requiere HPC y hardware


especializado.

<!-- fin de página 4 -->

### Brechas de conocimiento

##### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.



El científico de datos debe


focalizarse en habilidades
técnicas y usar las últimas

herramientas en DS/ML


DA y el desarrollo de
software son similares


Los lideres no tienen por que

saber DA


El modelo es sabio y

omnisciente




- Los lideres deben tener un conocimiento


profundo.


- Los vendedores agregan etiquetas a su


producto según la moda.

- Los consultores inflan los beneficios de


nuevas aproximaciones y minimizan los


costos y la complejidad de implementación.


- No se puede separar el mito de la realidad.


- DS termina siendo magia negra.

<!-- fin de página 5 -->

### Brechas de conocimiento

##### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.



El científico de datos debe


focalizarse en habilidades
técnicas y usar las últimas

herramientas en DS/ML


DA y el desarrollo de
software son similares


Los lideres no tienen por que

saber DA


El modelo es sabio y

omnisciente




- Data Literacy es la habilidad de leer tablas y


grafos, entenderlos para concluir


correctamente y saber cuando se está


potencialmente desinformado.


- La práctica avanzada no es corriente


- Las personas no desean desarrollar


habilidades en data literacy


- Se continuan tomando decisiones basadas en


hipótesis o criterios.


- Se desechan soluciones por complicadas.


- Mover datos de Excel a Power BI no lleva a


mejores decisiones.

<!-- fin de página 6 -->

### Falta de soporte en DA

##### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.



Educación y cultura


Objetivos poco claros


Dejar a los científicos de

datos solos




- Se piensa que DA es una versión mayor de


explorar datos en Excel.

- Los científicos de datos no deben usarse para


enseñar a otros profesionales.


- Se debe buscar la gente correcta no educarla.


- La gerencia debe tomar decisiones basadas


en datos y exigir que los demás lo hagan.

<!-- fin de página 7 -->

### Falta de soporte en DA

##### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.



Educación y cultura


Objetivos poco claros


Dejar a los científicos de

datos solos




- Datos, conocimientos, decisiones y acciones no


son sinónimos.


- No se deben buscar insights interesantes o


responder preguntas interesantes sin un objetivo


claro.


- La falta de objetivos claros puede llevar a


responder preguntas de negocio de bajo valor que


los equipos de BI o individuos podrían responder.


- Se confunde el insight obtenido con el proceso.

- Se ignoran los beneficios de la automatización.

<!-- fin de página 8 -->

### Falta de soporte en DA

##### **Mito**

crear una
Es posible **y fácil**
ventaja competitiva y resolver

problemas valiosos utilizando

datos.



Objetivos poco claros


Dejar a los científicos de

datos solos




                    - Dificultad para encontrar las fuentes de datos
Educación y cultura

adecuadas.




- Falta de permisos para acceder las fuentes


requeridas en la organización

- Dificultad para acceder a recursos como máquinas


virtuales y servidores para ejecutar modelos.


- Falta de libertad para gestión de infraestructura


computacional.


- El uso de laptop analytics es común.

- Dificultad para llevar los modelos a operativo y


fricciones con el equipo de TI.


- Formación de DS focalizada en los algoritmos y no


en la creación de un producto de datos operativo


- Malas prácticas de desarrollo de software y


desconocimiento de los requerimientos para ir a


productivo.

<!-- fin de página 9 -->

# Problemas y desafios con Data Analytics & Data Science

> ⚠️ S01: página 10 con poco texto extraíble; puede tener contenido en imagen no convertido.

<!-- fin de página 10 -->
