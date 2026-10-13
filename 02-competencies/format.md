# Formato de las competencias del mapa

Versión 0.1 (borrador)

## Propósito

Definir cómo se registra cada competencia del mapa en `map/<id>.md`, cuándo
una competencia entra al mapa y de qué tamaño debe ser.

El mapa describe lo que una persona competente en el campo de `domain.md`
sabe y sabe hacer, según la evidencia aceptada en `01-evidence/index.csv`.
No asigna niveles: el nivel se fija después, al redactar el perfil y los
resultados de aprendizaje del programa.

## Definición

Se adopta la definición del Acuerdo CESU 02 de 2020, numeral 2.2 b: una
competencia es un conjunto articulado de conocimientos, capacidades y
habilidades que permite comprender y analizar problemas y actuar de manera
eficaz en un contexto, y que se evalúa mediante resultados de aprendizaje.

De ahí salen las tres partes obligatorias de cada competencia: un enunciado
de desempeño, los conocimientos y las habilidades que lo sostienen, y la
evidencia de desempeño con la que podría evaluarse.

## Archivo de una competencia

Cada competencia vive en `map/<id>.md`. El `id` es `C` seguido de tres
dígitos (`C001`, `C002`, …), se asigna en orden y no se reutiliza.

El archivo tiene un encabezado YAML y cinco secciones, en este orden.

### Encabezado

```yaml
id: "C001"
enunciado: "…"
subcampos: ["analítica predictiva", "…"]
estado: "incluida"            # incluida | candidata | retirada
consenso:
  emisores: 2                 # emisores distintos que respaldan el enunciado
  explicitos: 1               # de ellos, con respaldo explícito
  inferidos: 1                # de ellos, solo con respaldo inferido
  actual: 1                   # de ellos, con rol actual
format_version: "0.1"
domain_version: "0.7"
fecha: "2026-10-13"
```

### 1. Enunciado

Una sola oración con tres partes:

- **Verbo de desempeño** en infinitivo: lo que la persona hace en el
  trabajo analítico (formular, preparar, modelar, evaluar, desplegar,
  comunicar, monitorear, gobernar).
- **Objeto**: aquello sobre lo que actúa y el producto que resulta.
- **Contexto**: la situación, la pregunta o la decisión al servicio de la
  cual actúa, con sus condiciones.

El verbo nombra un desempeño profesional, no un nivel cognitivo. Se evitan
los verbos que solo fijan profundidad (conocer, comprender, identificar,
describir), porque esa profundidad la fija el resultado de aprendizaje.

- Bien: *Formular un problema de decisión de una organización como un
  problema analítico con medidas de éxito, para orientar el trabajo
  analítico hacia una decisión acordada con los interesados.*
- Mal: *Comprender el aprendizaje automático.* No hay desempeño, objeto ni
  contexto, y nombra una disciplina vecina.
- Mal: *Usar Power BI.* Es una herramienta, no una competencia (véase
  Granularidad).

### 2. Subcampos

Uno o varios subcampos de `domain.md`, con sus nombres exactos. Si la
competencia aplica por igual a las cuatro analíticas que se distinguen por
la pregunta (descriptiva, diagnóstica, predictiva y prescriptiva), se
escriben las cuatro. Si la competencia pertenece a la tendencia de IA
generativa y agéntica, se agrega `IA generativa y agéntica (transversal)`.

Una competencia que no cabe en ningún subcampo no entra al mapa: o es de un
vecino, o `domain.md` debe cambiar primero.

### 3. Conocimientos y habilidades

Dos listas separadas:

- **Conocimientos**: conceptos, métodos, modelos y criterios que la persona
  debe saber para el desempeño.
- **Habilidades**: acciones concretas que ejecuta durante el desempeño.

Cada elemento termina con sus fuentes entre corchetes, por ejemplo
`[E0001 p. 5]`. Un elemento con respaldo inferido lo marca:
`[inferido: véase cadena I1]`.

### 4. Fuentes

Una tabla con una fila por documento:

| Columna | Contenido |
|---|---|
| `id` | El `id` de `index.csv`. Solo documentos con decisión `accept`. |
| Emisor | El emisor de `index.csv`; para una síntesis propia, el proveedor sintetizado (DataCamp, Pluralsight), no `propio`. |
| Rol | `actual` o `precursor`, como en `index.csv`. |
| Ubicación | Página del PDF y sección o tarea. |
| Respaldo | `explícito` o `inferido` (con el número de su cadena). |

La página es la del PDF, tal como la marca `<!-- fin de página N -->` en el
`md` del documento, no la numeración impresa. Si el documento no tiene
páginas (una síntesis o una página web), se cita la sección.

**Respaldo explícito**: el documento enuncia el desempeño, el conocimiento o
la habilidad con palabras equivalentes.

**Respaldo inferido**: el documento no lo enuncia, pero se deduce en uno o
dos pasos. Cada paso cita un texto del documento, otro documento aceptado o
`domain.md`. Una deducción de tres o más pasos no es respaldo. La cadena se
escribe así:

```
I1. E0028 p. 13: «Describe the type of data mining problem, such as
    clustering, prediction, or classification».
    → Paso 1 (domain.md, Precursores): la minería de datos precede a la
      analítica predictiva; la predicción y la clasificación son
      preguntas predictivas.
    ⇒ Elegir el tipo de analítica que responde la pregunta.
```

### 5. Evidencia de desempeño

Ejemplos de productos o actuaciones con los que se demuestra la
competencia, **tomados de las fuentes**, con su cita. No se inventan: si
ninguna fuente muestra un producto, la sección lo dice. Estos ejemplos
alimentan después la evaluación de los resultados de aprendizaje.

Las herramientas que las fuentes nombran se registran aquí, como ejemplos de
cómo se produce la evidencia, nunca como competencia.

## Regla de consenso

El consenso cuenta **emisores distintos**, no documentos: varios documentos
del mismo emisor (por ejemplo, el marco, las guías y los exámenes de
INFORMS) cuentan una vez.

Toda decisión es **incluida**, **candidata** o **retirada**. Se aplica en
este orden; la primera condición que se cumple decide.

1. **Retirada** si no tiene subcampo en `domain.md` o si todo su respaldo
   viene de documentos que dejaron de estar aceptados.
2. **Incluida** si la respaldan dos o más emisores, al menos uno de forma
   explícita y con rol `actual`.
3. **Candidata** en cualquier otro caso: un solo emisor, solo respaldo
   inferido, o solo precursores.

Una candidata no pasa al perfil. Queda en `map/` para que nueva evidencia la
promueva; se re-evalúa cada vez que entra evidencia o cambia `domain.md`.

## Granularidad

Una competencia tiene el tamaño de un desempeño que produce un resultado
verificable dentro del trabajo analítico.

- **Demasiado grande**: abarca un subcampo entero (*hacer analítica
  predictiva*) o dos productos que pueden evaluarse por separado. Se divide.
- **Demasiado pequeña**: una técnica, un algoritmo o un paso que solo tiene
  sentido dentro de otro desempeño (*calcular el RMSE*, *hacer un JOIN*). Se
  registra como conocimiento o habilidad de la competencia que lo contiene.
- **Herramientas**: un lenguaje, una biblioteca, una plataforma o un
  producto comercial (SQL Server, Spark, Power BI, IBM SPSS Modeler) nunca
  es una competencia. Aparece como ejemplo en la evidencia de desempeño. Si
  la herramienta define una capacidad propia del campo, se nombra la
  capacidad (*procesar datos en una plataforma distribuida*), no la
  herramienta; así lo hace `domain.md` con Spark en la analítica de grandes
  datos.
- **Disciplinas vecinas**: un método de estadística, aprendizaje automático
  u optimización entra como conocimiento al servicio de un desempeño
  analítico, no como competencia propia.

Prueba rápida: si dos competencias tendrían siempre la misma evidencia de
desempeño, son una sola; si una competencia tiene dos evidencias que se
pueden lograr por separado, son dos.

## Ejemplo trabajado

Construido con dos documentos aceptados:

- `E0001`: *INFORMS Analytics Framework*, INFORMS, 2024, autorizada, rol
  `actual`.
- `E0028`: *IBM SPSS Modeler CRISP-DM Guide*, IBM, 2016, aprendizaje
  profesional, rol `precursor`.

Archivo `map/C001.md`:

````markdown
---
id: "C001"
enunciado: "Formular un problema de decisión de una organización como un problema analítico con medidas de éxito, para orientar el trabajo analítico hacia una decisión acordada con los interesados."
subcampos: ["analítica descriptiva", "analítica diagnóstica", "analítica predictiva", "analítica prescriptiva"]
estado: "incluida"
consenso:
  emisores: 2
  explicitos: 2
  inferidos: 0
  actual: 1
format_version: "0.1"
domain_version: "0.7"
fecha: "2026-10-13"
---

# C001. Formular el problema analítico

## Enunciado

Formular un problema de decisión de una organización como un problema
analítico con medidas de éxito, para orientar el trabajo analítico hacia
una decisión acordada con los interesados.

- Verbo: formular.
- Objeto: el problema analítico y sus medidas de éxito.
- Contexto: un problema de decisión de una organización, con interesados
  que deben acordarlo.

## Subcampos

Las cuatro analíticas que se distinguen por la pregunta. INFORMS ubica la
reformulación antes de elegir entre analítica descriptiva, predictiva o
prescriptiva [E0001 p. 4]. La diagnóstica no aparece en las fuentes; se
incluye porque `domain.md` la define también por su pregunta (véase
Pendientes).

## Conocimientos

- Diferencia entre el problema de negocio y el problema analítico
  [E0001 p. 4; E0028 p. 10, p. 13].
- Tipos de pregunta analítica y el tipo de modelo que cada una exige
  [E0001 p. 4; inferido: véase cadena I1].
- Medidas de éxito de negocio y medidas de éxito técnicas, y su relación
  [E0001 p. 5, tarea 2.4; E0028 p. 10, p. 14].
- Línea base del desempeño actual [E0001 p. 5, tarea 2.5;
  E0028 p. 10, «Describe Current Solution»].
- Supuestos y riesgos de un planteamiento analítico [E0001 p. 5,
  tareas 2.3 y 2.6].

## Habilidades

- Redactar y refinar el enunciado del problema de negocio hasta que sea
  claro y conciso [E0001 p. 4, tareas 1.1 y 1.4; E0028 p. 10].
- Identificar a los interesados y al patrocinador, y sus perspectivas
  [E0001 p. 4, tarea 1.2; E0028 p. 10, tarea 1].
- Decidir si el problema admite una solución analítica [E0001 p. 4,
  tarea 1.3].
- Reformular el problema de negocio como problema analítico [E0001 p. 5,
  tarea 2.1; E0028 p. 13].
- Proponer los factores de entrada y su relación con los resultados
  [E0001 p. 5, tarea 2.2].
- Fijar medidas de éxito con números y horizontes concretos [E0001 p. 5,
  tarea 2.4; E0028 p. 13, p. 14].
- Obtener el acuerdo del patrocinador y de los interesados sobre el
  planteamiento [E0001 p. 4, tarea 1.6; p. 5, tarea 2.7].

## Fuentes

| id | Emisor | Rol | Ubicación | Respaldo |
|---|---|---|---|---|
| E0001 | INFORMS | actual | p. 4, Dominio I, tareas 1.1–1.6; p. 4–5, Dominio II, tareas 2.1–2.7 | explícito |
| E0028 | IBM | precursor | p. 9–10, *Determining Business Objectives*; p. 13–14, *Determining Data Mining Goals* | explícito |
| E0028 | IBM | precursor | p. 13, tipo de problema de minería de datos | inferido (I1) |

Consenso: dos emisores, ambos explícitos, uno con rol `actual`. Regla 2:
**incluida**.

### Cadenas de inferencia

```
I1. E0028 p. 13: «Describe the type of data mining problem, such as
    clustering, prediction, or classification».
    → Paso 1 (domain.md, Precursores): la minería de datos precede a la
      analítica predictiva; la predicción y la clasificación son
      preguntas predictivas.
    ⇒ Conocimiento: tipos de pregunta analítica y el tipo de modelo que
      cada una exige.
```

## Evidencia de desempeño

- Enunciado del problema de negocio y caso de negocio inicial
  [E0001 p. 4, tareas 1.1 y 1.5].
- Enunciado del problema analítico con factores de entrada, supuestos,
  medidas de éxito, línea base y riesgos [E0001 p. 5, tareas 2.1–2.6].
- Objetivos de negocio con criterios de éxito numéricos; en el caso de un
  minorista en línea: aumentar las ventas cruzadas un 10 % [E0028 p. 9].
- Traducción de los objetivos de negocio a metas técnicas; en el mismo
  caso: análisis de canasta, perfilamiento y análisis de secuencias
  [E0028 p. 14].
- Plan del proyecto basado en las metas de negocio y técnicas
  [E0028 p. 14].
- Herramienta de ejemplo: los nodos *Evaluation* y *Analysis* de IBM SPSS
  Modeler para medir el éxito técnico [E0028 p. 14]. No es parte de la
  competencia.

## Pendientes

- La analítica diagnóstica se incluye solo por `domain.md`. Buscar una
  fuente que la nombre en el planteamiento del problema.
````

Qué muestra el ejemplo:

- La competencia entra con un documento `precursor` porque el otro emisor es
  `actual` y explícito (regla 2).
- E0028 respalda la competencia de forma explícita y, en un punto, de forma
  inferida; la cadena tiene un paso.
- IBM SPSS Modeler aparece solo como herramienta de ejemplo.
- Las tareas 3.8 de INFORMS (validar el problema tras ver los datos) y 6.1
  (validación de negocio) no entran: pertenecen a desempeños posteriores,
  con otra evidencia.

## Versión y cambios

- 0.1 (2026-10-13): borrador inicial.
