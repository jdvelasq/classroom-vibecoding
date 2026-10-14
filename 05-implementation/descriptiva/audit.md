# descriptiva — Auditoría de actividades

- **Fecha / executor:** 2026-10-14 / Claude.
- **Huella de la auditoría:** `sha256:4d81cc3bd73edb8251e75c2ac5f1126626cc6659aba2986692eaf5fe54ab0608`.
- **Entrada:** `04-curriculum/postgraduate/descriptiva.md`; competencias C001 (2026-10-13), C002 (2026-10-13), C003 (2026-10-13), C005 (2026-10-13), C006 (2026-10-13).

## Decisiones por actividad

| Actividad | Decisión | Resultados | Competencias | Propuestas | Razón |
| --- | --- | --- | --- | --- | --- |
| P100 | igual | descriptiva/RC01, descriptiva/RC04 | C001, C002 | — | Introduce el patrón de cómputo distribuido (gestión de datos a escala, C002.CON09) y enmarca el volumen como un reto de datos a gran escala (C001.HAB05/CON07); sus highlights ya cubren esos ítems al nivel introduce sin necesitar ajuste. |
| P101 | curso | — | — | N02 | No ancla ningún resultado del curso ni ítem vigente: enseña refactorización de software sobre el conteo de P100, no un ítem de datos o analítica; se abre como decisión de curso en lugar de forzar un anclaje artificial. |
| P102 | igual | descriptiva/RC04 | C002 | — | Valida, minimiza y re-representa datos (C002.HAB02, CON07, CON02) al nivel introduce; no hay defecto ni capacidad ausente que lo justifique. |
| P103 | puntual | descriptiva/RC02, descriptiva/RC04 | C002, C003 | T01 | T01 corrige un defecto real: comparar totales por conductor sin antes verificar exposición y distribución semanal puede atribuir a desempeño lo que es volumen de turnos; refuerza C003.HAB01 sin alargar el taller. |
| P104 | igual | descriptiva/RC02, descriptiva/RC04 | C002, C003 | — | Reexpresa el resumen de P103 en SQL declarativo (C002.CON02, C003.HAB01) sin defecto ni capacidad ausente. |
| P105 | puntual | descriptiva/RC04 | C002 | T01 | T01 minimiza los datos compartidos con el asistente y verifica su respuesta contra P103: refuerza la gobernanza de datos (C002.CON07) y la validación (C002.HAB02) sin alargar el taller. |
| P106 | puntual | descriptiva/RC04 | C002 | T01 | T01 cierra un vacío real: hoy P106 limpia y verifica (C002.CON06) pero no informa los hallazgos de calidad (C002.HAB04); persistir un reporte de preparación lo cierra sin alargar el caso. |
| P107 | igual | descriptiva/RC04 | C002 | — | Reexpresa la limpieza de P106 como consulta SQL (C002.HAB02, CON06) manteniendo el mismo contrato de salida; no hay defecto adicional que corregir aquí. |
| P108 | puntual | descriptiva/RC04 | C002 | T01 | T01 añade una métrica formal (tamaño mínimo de clases de equivalencia, k) al riesgo residual que H04 ya mide cualitativamente: refuerza el rigor de C002.CON07 sin alargar el caso. |
| P109 | igual | descriptiva/RC04 | C002 | — | Reexpresa la anonimización de P108 en SQL, evaluando el riesgo con una consulta de enlace (C002.CON07, HAB02); no hay defecto adicional que corregir. |
| P120 | puntual | descriptiva/RC01, descriptiva/RC02, descriptiva/RC04 | C001, C002, C003, C006 | T01, T02, T03 | Es el primer caso descriptivo completo tras P100–P109 y el que más resultados del curso sirve; T01 (encuadre), T02 (conclusión con límite causal) y T03 (lectura contra la tasa base) lo acercan al nivel domina de RC02 sin alargarlo, cambiar caso ni datos. |
| P121 | puntual | descriptiva/RC02, descriptiva/RC04 | C002, C003 | T01 | T01 corrige un defecto real: leer un patrón estacional sin separar tendencia y año puede confundir un año atípico con recurrencia; refuerza C003.CON02/HAB01 sin añadir caso. |
| P122 | puntual | descriptiva/RC01, descriptiva/RC02, descriptiva/RC04 | C001, C002, C003 | T01 | T01 corrige un defecto real: resumir con promedios sin inspeccionar atípicos oculta por qué proporción a tiempo y promedio de días divergen; refuerza C002.CON06/C003.HAB01 sin añadir caso. |
| P123 | puntual | descriptiva/RC02, descriptiva/RC04 | C002, C003 | T01, T02 | T01 completa la procedencia del corpus (fecha, tamaño, último año parcial) y T02 normaliza la co-ocurrencia por lo esperado al azar antes de detectar comunidades: ambas refuerzan C002.CON01/C003.CON05 sin alargar el pipeline con un segundo caso. |
| P124 | igual | descriptiva/RC02, descriptiva/RC04 | C002, C003 | — | Construye un tablero completo (C003.CON03/HAB04) desde datos validados (C002.HAB02) sin defecto observable ni capacidad ausente. |
| P125 | puntual | descriptiva/RC01, descriptiva/RC02, descriptiva/RC03, descriptiva/RC04 | C002, C003, C005, C006 | T01 | Es el vehículo del curso para RC03 (domina): ya estima el efecto por pares comparables y declara su límite causal (H02, H06). La propuesta nueva contrasta ese efecto con una regresión controlada por las mismas covariables, ejercitando C005.HAB04, ausente hoy en el curso, sin añadir un segundo caso. |
| P150 | puntual | descriptiva/RC01, descriptiva/RC02, descriptiva/RC04 | C001, C002, C003 | T01 | T01 corrige un defecto real: la lectura temporal engañosa de la serie mensual puede llevar a una conclusión incorrecta sobre tendencia; refuerza C003.CON02 sin añadir caso. |
| P151 | puntual | descriptiva/RC01, descriptiva/RC02, descriptiva/RC04 | C002, C003, C006 | T01 | T01 añade una dimensión de fecha de calendario completo, mostrando qué oculta una dimensión derivada del hecho: refuerza C002.CON10 y la transparencia del modelo (C006.CON03) sin añadir caso. |
| P152 | puntual | descriptiva/RC02, descriptiva/RC04 | C002, C003 | T01, T02 | T01 persiste la lectura de la navegación OLAP (qué significa «explican», por qué se corta en Norte) y T02 añade comparación de períodos: ambas refuerzan C003.CON03 (tableros e inferencia) sin añadir caso. |
| P153 | puntual | descriptiva/RC01, descriptiva/RC02 | C001, C003, C006 | T01, T02 | T01 añade reglas de rango/definición con severidad y ejercita la rama BLOQUEADO, y T02 completa cada KPI con propósito, decisión, frecuencia y línea base: ambas refuerzan C001.HAB07/C006.CON03 sin añadir caso. |
| P154 | puntual | descriptiva/RC01, descriptiva/RC02 | C003, C006 | T01 | T01 corrige un defecto real: sin un criterio de atención al grano mensual ni la declaración de que `orders` no es aditivo, la capa de serving puede inducir a sumar mal; refuerza C003.HAB02 sin añadir caso. |

## Señales

| Señal | Texto | Categoría | Anclas, propuesta o razón |
| --- | --- | --- | --- |
| descriptiva/RC01 | Formular la pregunta descriptiva de un caso de una organización y las medidas de éxito que orientarán la exploración de los datos. (nivel: introduce) | mejora | P120: T01; parcial en P120:H01 (introduce) |
| descriptiva/RC02 | Construir un reporte o tablero que describa, con métricas y visualizaciones, qué ocurre en el caso, para quién, dónde y cuándo, y que refine la pregunta inicial con lo observado. (nivel: domina) | mejora | P120: T02; parcial en P120:H07 (desarrolla) |
| descriptiva/RC03 | Estimar el efecto de un factor o una intervención sobre un resultado del caso, mediante un experimento o un estudio observacional, y discutir los límites de causalidad del diseño elegido. (nivel: domina) | cubierta | P125:H02 (desarrolla), P125:H06 (domina) |
| descriptiva/RC04 | Evaluar la calidad de los datos de un caso, con sus faltantes, sus atípicos y sus inconsistencias, y decidir cómo afecta lo que la descripción puede afirmar. (nivel: introduce) | cubierta | P106:H01 (introduce), P106:H05 (introduce), P120:H02 (introduce) |
| C001.CON01 | Diferencia entre el problema de negocio y el problema analítico. | mejora | P120: T01 |
| C001.CON02 | Tipos de pregunta analítica y el tipo de modelo que cada una exige. | marginal | Ninguna actividad clasifica tipos de pregunta por el tipo de modelo que exigen; cada caso ya formula su propia pregunta descriptiva sin esa taxonomía, y añadirla no cambia lo que el estudiante hace o entiende al final del taller. |
| C001.CON03 | Definición operativa del resultado que se quiere predecir o explicar. | cubierta | P120:H03 (introduce), P122:H02 (introduce), P150:H03 (introduce) |
| C001.CON04 | Medidas de éxito de negocio y técnicas, y su relación. | cubierta | P120:H04 (introduce), P122:H04 (introduce), P125:H05 (desarrolla) |
| C001.CON05 | Línea base del desempeño actual. | mejora | P120: T03; parcial en P120:H06 (introduce) |
| C001.CON06 | Supuestos y riesgos de un planteamiento analítico. | mejora | P120: T01 |
| C001.CON07 | Las cuatro «V» de los grandes datos (volumen, variedad, velocidad, veracidad) como marco para reconocer una oportunidad u obstáculo de datos a escala. | cubierta | P100:H03 (introduce) |
| C001.CON08 | Pensamiento estructurado para definir el enunciado de un problema y encuadrar su solución, con atención al diseño centrado en las personas. | marginal | Ningún highlight evidencia una técnica de pensamiento estructurado distinta del encuadre de T01 (destinatario, decisión, supuestos, alcance); lo que T01 añade ya basta para el nivel introduce que debe el curso. |
| C001.HAB01 | Redactar y refinar el enunciado del problema de negocio. | mejora | P120: T01 |
| C001.HAB02 | Identificar a los interesados y al patrocinador. | mejora | P120: T01 |
| C001.HAB03 | Decidir si el problema admite una solución analítica. | marginal | Los casos del curso llegan ya planteados como analíticos; decidir si un problema admite solución analítica pertenece a un curso introductorio anterior, no al momento en que el estudiante ya tiene el dataset en la mano. |
| C001.HAB04 | Traducir la pregunta de negocio en una pregunta o hipótesis que la analítica pueda responder. | mejora | P120: T01 |
| C001.HAB05 | Enmarcar las oportunidades y los retos de datos a gran escala como parte del problema analítico. | cubierta | P100:H03 (introduce) |
| C001.HAB06 | Proponer los factores de entrada y su relación con los resultados. | fuera de alcance | Proponer factores de entrada y su relación con un resultado es modelar, objeto de predictiva; aquí la asociación se explora y se emparejan covariables (P125 H02) sin proponer una estructura de factores causales de entrada.; parcial en P125:H02 (desarrolla) |
| C001.HAB07 | Proponer el enfoque analítico y los KPI del problema. | cubierta | P153:H01 (desarrolla), P120:H04 (introduce) |
| C001.HAB08 | Obtener el acuerdo del patrocinador y de los interesados. | marginal | Ningún taller simula la obtención del acuerdo de un patrocinador; no es material en el límite de una sesión corta guiada por el instructor. |
| C002.CON01 | Necesidades de datos derivadas de la pregunta y evaluación de las fuentes disponibles. | cubierta | P120:H01 (introduce), P150:H01 (introduce) |
| C002.CON02 | Estructuras de datos y relaciones entre fuentes. | cubierta | P103:H01 (introduce), P104:H01 (introduce), P121:H01 (introduce), P151:H01 (desarrolla), P102:H03 (introduce), P105:H02 (introduce) |
| C002.CON03 | Integración de fuentes heterogéneas: correspondencia de esquemas, integración entre dominios y extracción de información desde texto e imágenes. | cubierta | P150:H01 (desarrolla), P150:H02 (desarrolla) |
| C002.CON04 | Reducción y compresión de datos para quitar redundancia antes del análisis. | marginal | Ninguna actividad reduce o comprime datos explícitamente por redundancia antes de analizar; los casos actuales no generan el volumen que lo exigiría. |
| C002.CON05 | Tabla base analítica: un registro por entidad para el modelado supervisado. | fuera de alcance | Una tabla con un registro por entidad para modelado supervisado es el objeto de predictiva; P150/P151 construyen una tabla y un mart reutilizables para describir, no para entrenar un modelo. |
| C002.CON06 | Dimensiones de calidad de los datos: errores, faltantes, atípicos, y su efecto en la representatividad de los datos para el modelado. | cubierta | P106:H01 (introduce), P106:H05 (introduce), P122:H05 (introduce), P107:H01 (introduce) |
| C002.CON07 | Privacidad, seguridad y gobierno de los datos. | cubierta | P108:H01 (introduce), P108:H02 (introduce), P108:H03 (desarrolla), P108:H04 (desarrolla), P108:H05 (desarrolla), P108:H06 (desarrolla), P109:H03 (introduce), P105:H03 (introduce), P125:H07 (desarrolla), P102:H02 (introduce) |
| C002.CON08 | Muestreo representativo y partición en entrenamiento y prueba. | fuera de alcance | La partición en entrenamiento y prueba es un concepto de modelado supervisado (predictiva); el muestreo representativo se toca sólo tangencialmente en P125 (población sintética) sin ser el objeto del curso. |
| C002.CON09 | Gestión de datos a escala con operacionalización confiable y escalable. | cubierta | P100:H01 (introduce), P123:H07 (introduce) |
| C002.CON10 | Ubicación de los datos dentro de la organización y papel de los almacenes de datos en la estrategia. | cubierta | P151:H02 (desarrolla), P152:H01 (desarrolla) |
| C002.CON11 | Trabajo con datos de texto no estructurado (correos, encuestas, foros internos) como fuente de análisis. | marginal | Ningún caso usa texto libre no estructurado (correos, encuestas, foros); los casos actuales (ventas, vuelos, cadena de suministro, salarios, bibliometría) ya cubren variedad suficiente de fuentes sin que este tipo sea indispensable para el producto terminal. |
| C002.HAB01 | Adquirir datos de sistemas distintos, eligiendo la fuente y la técnica de adquisición según sus características y las de la aplicación, incluido el raspado web (*web scraping*) y las interfaces de programación de aplicaciones (API). | cubierta | P123:H01 (desarrolla) |
| C002.HAB02 | Limpiar, armonizar, transformar, unir y validar datos. | cubierta | P100:H02 (introduce), P100:H05 (introduce), P102:H01 (introduce), P104:H02 (introduce), P105:H01 (introduce), P106:H02 (desarrolla), P106:H03 (desarrolla), P106:H04 (desarrolla), P107:H02 (introduce), P107:H03 (introduce), P108:H06 (desarrolla), P109:H02 (introduce), P120:H02 (introduce), P122:H01 (introduce), P123:H03 (introduce), P123:H08 (introduce), P124:H01 (introduce), P124:H02 (introduce), P150:H02 (desarrolla), P121:H02 (introduce) |
| C002.HAB03 | Agregar y transformar datos hasta una tabla analítica. | cubierta | P123:H02 (introduce), P150:H04 (desarrolla), P151:H03 (desarrolla), P152:H02 (desarrolla) |
| C002.HAB04 | Evaluar la calidad de los datos e informar los hallazgos. | mejora | P106: T01 |
| C002.HAB05 | Elaborar un plan de gestión de datos. | marginal | Ningún taller produce un plan de gestión de datos como artefacto; el gobierno de datos se ejercita puntualmente en P108/P109 sin ese formato de plan. |
| C002.HAB06 | Revisar el planteamiento del problema a la luz de los datos. | cubierta | P120:H02 (introduce) |
| C003.CON01 | Estadística descriptiva y métricas de negocio, distribuciones normales y no normales, tamaño del efecto e intervalos de confianza. | cubierta | P120:H04 (introduce), P121:H03 (introduce), P122:H02 (introduce), P125:H03 (desarrolla), P153:H02 (desarrolla) |
| C003.CON02 | Principios de visualización para encontrar patrones y anomalías, y tipos de gráfico según el tipo de dato (series de tiempo, datos espaciales, multivariados, en árbol o en grafo, texto). | cubierta | P103:H04 (introduce), P121:H04 (desarrolla), P121:H06 (desarrolla), P123:H05 (desarrolla), P123:H06 (introduce), P150:H04 (introduce) |
| C003.CON03 | Tableros e inferencia a partir de la visualización. | cubierta | P124:H05 (domina), P154:H04 (domina), P152:H01 (desarrolla), P152:H04 (desarrolla) |
| C003.CON04 | Segmentación y agrupamiento como descripción de grupos, y medidas de proximidad y similitud entre registros. | fuera de alcance | La segmentación por reglas de negocio ya se cubre (P120 H07, P125 H02); el agrupamiento formal por proximidad o similitud entre registros (clustering) pertenece a la identidad de modelado de predictiva/ML y se excluye a propósito para no acercar el curso al riesgo que su ficha nombra.; parcial en P120:H07 (introduce), P125:H02 (desarrolla) |
| C003.CON05 | Minería de patrones y reglas de asociación (por ejemplo, canasta de mercado) y analítica de texto para estructurar datos no numéricos. | cubierta | P123:H04 (desarrolla), P123:H05 (desarrolla) |
| C003.CON06 | Reducción de dimensión para describir datos de muchas variables. | marginal | P123 reduce conceptualmente muchas palabras clave a comunidades de red, pero ninguna actividad aplica una técnica formal de reducción de dimensión (p. ej. PCA); no es material añadir una sólo para nombrar la técnica. |
| C003.HAB01 | Explorar relaciones, tendencias y anomalías. | cubierta | P103:H02 (introduce), P104:H03 (introduce), P121:H06 (desarrolla), P122:H03 (introduce), P125:H04 (desarrolla) |
| C003.HAB02 | Calcular e informar métricas. | cubierta | P103:H03 (introduce), P120:H04 (desarrolla), P124:H03 (desarrolla), P125:H05 (desarrolla), P152:H03 (desarrolla), P153:H01 (domina), P154:H01 (desarrolla), P151:H04 (desarrolla) |
| C003.HAB03 | Recopilar, limpiar y describir los datos disponibles, incluidas las estadísticas generales. | cubierta | P106:H05 (desarrolla), P150:H01 (desarrolla) |
| C003.HAB04 | Construir visualizaciones para usuarios con distinta formación analítica, eligiendo el tipo de gráfico según el tipo de dato. | cubierta | P103:H04 (introduce), P120:H05 (introduce), P124:H05 (domina), P154:H02 (domina) |
| C003.HAB05 | Segmentar clientes por comportamiento o atributos. | cubierta | P120:H07 (desarrolla), P121:H05 (desarrolla), P122:H06 (desarrolla), P125:H02 (desarrolla) |
| C003.HAB06 | Refinar la pregunta a partir de lo observado. | mejora | P120: T02 |
| C005.CON01 | Diferencia entre correlación y causalidad. | cubierta | P125:H06 (domina) |
| C005.CON02 | Confusión y límites de los estudios observacionales. | cubierta | P125:H02 (desarrolla), P125:H06 (domina) |
| C005.CON03 | Ensayos controlados aleatorizados. | marginal | El resultado del curso admite experimento u observacional como rutas alternativas; P125 ya alcanza el nivel domina por la vía observacional, así que ningún taller necesita ejecutar además un ensayo controlado aleatorizado. |
| C005.CON04 | Pruebas de hipótesis y valor p, incluidas alternativas no paramétricas como las pruebas de permutación y la corrección por comparaciones múltiples (tasa de descubrimientos falsos). | marginal | P125 usa salvaguardas heurísticas (tamaño mínimo y doble criterio, H04) en lugar de pruebas formales de hipótesis o valor p a propósito, para no desplazar el curso hacia una secuencia de Estadística, que es el riesgo que la ficha del curso nombra. |
| C005.CON05 | Muestreo y experimentación estadística. | cubierta | P125:H01 (introduce) |
| C005.CON06 | Análisis de causa raíz: desglosar los síntomas de un problema en sus partes para encontrar la causa que lo explica. | marginal | El curso diagnostica por segmentación (P120 H07, P122) pero no aplica una técnica formal de análisis de causa raíz; no es material en el nivel que el curso debe en este punto. |
| C005.HAB01 | Formular un problema de prueba de hipótesis. | marginal | Mismo razonamiento que C005.CON04: el curso prefiere salvaguardas heurísticas a la formulación formal de hipótesis estadísticas, para proteger su identidad frente al riesgo de volverse una secuencia de Estadística. |
| C005.HAB02 | Diseñar experimentos y formular hipótesis científicas, superando las barreras prácticas de experimentar en una organización. | marginal | El curso no incluye diseño experimental aleatorizado; P125 resuelve el resultado del curso por la vía observacional, que éste admite como alternativa suficiente. |
| C005.HAB03 | Realizar inferencia causal en ensayos aleatorizados. | marginal | Mismo razonamiento que C005.CON03: ningún taller ejecuta un ensayo aleatorizado porque la ruta observacional de P125 ya alcanza el nivel domina que el curso debe. |
| C005.HAB04 | Usar regresión con fines de inferencia. | mejora | P125: T01 |
| C005.HAB05 | Sacar conclusiones estadísticas correctas de una muestra. | cubierta | P125:H06 (domina) |
| C006.CON01 | Supuestos, limitaciones y restricciones de un resultado analítico. | cubierta | P125:H06 (domina), P122:H05 (introduce) |
| C006.CON02 | Formas de reporte: informe, tablero, presentación oral, escrita y gráfica, adaptadas a una audiencia que no es necesariamente analítica. | cubierta | P124:H05 (domina), P154:H02 (domina) |
| C006.CON03 | Transparencia del proceso ante auditores. | cubierta | P153:H03 (domina), P153:H04 (domina), P151:H03 (desarrolla), P154:H03 (domina) |
| C006.HAB01 | Documentar y comunicar los hallazgos de un modelo. | cubierta | P120:H08 (introduce), P121:H07 (introduce), P122:H07 (introduce) |
| C006.HAB02 | Comunicar hallazgos de datos. | cubierta | P121:H04 (desarrolla), P120:H05 (desarrolla) |
| C006.HAB03 | Elaborar y entregar un informe de validación de negocio. | mejora | P120: T02 |
| C006.HAB04 | Comunicar perspectivas a interesados de negocio y hacer recomendaciones. | fuera de alcance | Comunicar hallazgos a interesados ya se cubre (P120 H08 y, una vez aplicada, T02); «hacer recomendaciones» de acción pertenece a prescriptiva, que el alcance del curso excluye explícitamente: «el curso no define acciones».; parcial en P120:H08 (introduce) |
| C006.HAB05 | Presentar un análisis de forma oral. | marginal | Ningún highlight evidencia una presentación oral del análisis; no es material para el límite de un taller presencial corto guiado por el instructor. |
| C006.HAB06 | Sacar conclusiones del análisis de datos y comunicar los resultados a altos cargos mediante comunicación oral y escrita. | mejora | P120: T02 |

## Hitos fuera de lo que el curso debe enseñar

| Actividad | Hito | Acción | Propuesta | Razón |
| --- | --- | --- | --- | --- |
| P100 | H04 | conservar | — | Reproducir las convenciones de salida de un trabajo Hadoop es el detalle técnico que hace verificable y creíble el mecanismo de map/reduce de H01 y H03; no es en sí un ítem del curso. |
| P101 | H01 | conservar | — | Práctica de ingeniería de software (funciones con responsabilidad nombrada) que sostiene la legibilidad de P100 en adelante; se conserva en espera de la decisión de curso. |
| P101 | H02 | conservar | — | Separar motor genérico de lógica del problema es la misma práctica de ingeniería; sin ítem propio. |
| P101 | H03 | conservar | — | Hacer explícita una precondición del motor es parte de la misma práctica; sin ítem propio. |
| P101 | H04 | conservar | — | Usar el corpus fijo como oráculo de regresión es una práctica de verificación de software, no un ítem de datos o analítica. |
| P101 | H05 | conservar | — | Completar el flujo de entrega es la culminación de la misma práctica de refactorización; sin ítem propio. |
| P102 | H04 | conservar | — | Componer la conversión con funciones pequeñas y un punto de entrada es práctica de ingeniería que sostiene H01–H03; no es un ítem propio del curso. |
| P104 | H04 | conservar | — | Encapsular el resumen como vista reutilizable es una práctica de ingeniería SQL que sostiene H01–H03; no es un ítem propio. |
| P107 | H04 | conservar | — | Mantener el contrato de salida de P106 con otra implementación es evidencia de robustez técnica (dos motores, mismo contrato); no es un ítem propio distinto de C002.HAB02. |
| P109 | H01 | conservar | — | Formular explícitamente la pregunta que orienta la transformación es la práctica de encuadre que sostiene H02–H03; no es un ítem propio distinto. |
| P109 | H04 | conservar | — | Preservar el orden de los registros porque el contrato lo exige es un detalle técnico que sostiene la verificabilidad de H03; no es un ítem propio. |
| P109 | H05 | conservar | — | Localizar la raíz de la actividad de forma portable es una práctica de ingeniería de software (portabilidad), no un ítem de datos o analítica. |
| P124 | H04 | conservar | — | Separar funciones analíticas de la interfaz es una práctica de arquitectura de software que sostiene H01–H03 y H05; no es un ítem propio distinto. |
