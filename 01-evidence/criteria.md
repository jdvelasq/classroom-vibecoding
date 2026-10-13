# Criterios de selección de documentos de evidencia

Versión 0.4 (borrador)

## Propósito

Seleccionar documentos que describan lo que una persona verdaderamente
competitiva en el campo definido en `domain.md` debe saber y saber hacer,
según las tendencias disciplinares, la práctica profesional y los estándares
nacionales e internacionales.

Este método solo decide qué documentos entran como evidencia. La asignación
de niveles (por ejemplo, pregrado, especialización o maestría) es una
decisión posterior y separada.

## Origen de los documentos

- **Aportados por david**: se presumen curados. La pertinencia y el acceso
  se aplican siempre; autoridad, especificidad y vigencia se califican y se
  registran, pero no deciden.
- **Encontrados por el agente**: se aplican los cinco criterios completos.
- **Síntesis propias**: reconstrucciones del proyecto sobre las fuentes
  públicas de un proveedor, con fecha, método, límites y fuentes citadas
  (por ejemplo, `syntheses/datacamp.md`). Entran sin pasar por la
  selección: se guardan en `syntheses/`, se registran en `index.csv` con
  emisor y origen `propio`, y su decisión lista las fuentes que citan. No
  se re-evalúan por cambios del dominio; si el dominio cambia, se revisa
  la síntesis.

## Criterios

Cada criterio se califica en una escala de 0 a 2:
0 = no cumple, 1 = cumple parcialmente, 2 = cumple.

### 1. Pertinencia

¿El documento trata el campo, un subcampo, un precursor o un vecino según lo
define `domain.md`?

- Entra (2): un marco de competencias para profesionales del campo.
- No entra (0): un documento sobre un campo ajeno que solo menciona el campo
  de paso.

La pertinencia se aplica a todo documento, incluidos los aportados por
david. Si el texto no puede convertirse, se juzga por el título, el nombre
del archivo y los metadatos.

### 2. Autoridad

¿Quién respalda el documento? Se aceptan cinco categorías:

- **Institucional**: universidades, programas acreditados, asociaciones
  académicas.
- **Derivada de la literatura**: revisiones sistemáticas o estudios
  publicados con revisión por pares.
- **Aprendizaje profesional**: programas de formación ejecutiva o de
  certificación de proveedores reconocidos.
- **Autorizada**: asociaciones o cuerpos profesionales del campo.
- **Gubernamental**: normas, acuerdos y marcos nacionales o internacionales.

Ejemplos:

- Entra (2): el marco de un cuerpo profesional reconocido del campo.
- No entra (0): una entrada de blog anónima o un material comercial sin
  autor identificable.

### 3. Especificidad

¿El documento enuncia competencias, resultados de aprendizaje o contenidos
que puedan citarse con número de página?

- Entra (2): una lista de competencias o dominios con descripción.
- No entra (0): un texto de opinión que habla del campo en términos
  generales.

Los anuncios de cursos y programas cuentan como señales de mercado de
especificidad débil (1): indican qué se ofrece y se demanda, pero no
describen competencias con detalle.

### 4. Vigencia

¿El documento es reciente, o es fundacional para un campo precursor?

- Entra (2): un documento publicado en los últimos años, o un texto clásico
  que define un precursor del campo.
- No entra (0): un documento antiguo, superado por versiones posteriores y
  sin valor fundacional.

### 5. Acceso

¿Se dispone del texto completo en un formato que pueda convertirse a texto?

- Entra (2): un PDF o una página web con el texto completo.
- No entra (0): solo un resumen, o un documento escaneado imposible de
  convertir.

## Rol

Cada decisión registra el rol del documento:

- `actual`: describe el campo tal como se practica hoy.
- `precursor`: describe un campo que antecede al actual y explica su origen.

## Regla de decisión

Toda decisión es **aceptar** o **rechazar**: el proceso nunca deja
documentos pendientes para david. Se aplica en este orden; la primera
condición que se cumple decide.

1. **Rechazar** si la pertinencia es 0. El documento pasa a `rejected/`.
2. **Documentos aportados por david**: **aceptar** si la pertinencia es 1
   o 2.
3. **Documentos encontrados por el agente**: **aceptar** si ningún
   criterio está en 0 y la suma es 7 o más; si no, **rechazar**.
4. Un documento con el mismo título, emisor y año que uno ya indexado se
   **rechaza** como duplicado y referencia al indexado. Si el año es
   distinto, es una edición nueva: se decide con las reglas anteriores y
   se enlaza con la edición previa.

Las advertencias de conversión y las dudas del juicio no bloquean la
decisión: se registran en la decisión del documento y se informan a david.
Como `rejected/` es un borrado suave, un rechazo se puede revertir.

## Re-evaluación por cambios del dominio

Cada decisión registra la versión de `domain.md` con que se tomó. Cuando
`domain.md` cambia de versión, antes de procesar documentos nuevos:

- Si el dominio **se amplía**, se re-evalúan los documentos rechazados por
  pertinencia en versiones anteriores.
- Si el dominio **se restringe**, se re-evalúan los documentos aceptados.
- Si hace las dos cosas, se re-evalúan ambos grupos.

`rejected/` es un borrado suave precisamente para esto: un documento
rechazado vuelve a `ingest/` y se juzga de nuevo con la regla vigente. La
decisión anterior se conserva como reemplazada, y la nueva la referencia.

## Calibración

Antes de aplicar los criterios al conjunto completo, se prueban con
documentos conocidos. Si la regla clasifica mal alguno, se ajustan los
umbrales o las definiciones y se registra el cambio.

## Conjunto de calibración

Resultados esperados según el veredicto experto de david. Toda versión
nueva de la regla debe reproducirlos.

| Documento | Origen | P | Au | E | V | Ac | Veredicto esperado | Rol |
|---|---|---|---|---|---|---|---|---|
| `informs-analytics-framework-2024.pdf` | david | 2 | 2 | 2 | 2 | 2 | Aceptar | `actual` |
| `sas-data-mining.pdf` | david | 2 | 1 | 1 | 1 | 2 | Aceptar | `precursor` |
| `mit-data-science-big-data.pdf` | david | 2 | 2 | 1 | 2 | 2 | Aceptar | `actual` |
| `mit-blockchain-disruptive-technology.pdf` | david | 0 | – | – | – | 0 | Rechazar (fuera del dominio) | – |

Notas:

- SAS es un *white paper* comercial de 2016 sobre minería de datos.
  Con la regla 0.1 sumaba 7 y quedaba en "revisar"; david lo acepta como
  precursor. Por eso los documentos aportados por david no dependen de
  autoridad, especificidad ni vigencia.
- El PDF del MIT no tiene texto extraíble (22 páginas sin capa de texto).
  Se rechaza por pertinencia, juzgada por el título; la advertencia de
  conversión no lo retiene en `ingest/`.
- Los dos documentos del MIT comparten emisor y reciben veredictos
  opuestos: la regla juzga el contenido, no el emisor. El de *Data Science
  y Big Data* (2022) es un anuncio de curso: especificidad débil (1), pero
  pertinente para la analítica de grandes datos y la predictiva.

## Versión y cambios

- 0.1 (2026-10-13): borrador inicial.
- 0.2 (2026-10-13): calibración con cuatro documentos de david. La pertinencia
  se aplica a todos; los documentos fuera del dominio pasan a `rejected/` y
  la falta de pertinencia prevalece sobre las advertencias de conversión;
  autoridad, especificidad y vigencia deciden solo para documentos
  encontrados por el agente; los anuncios de cursos son señales de mercado
  de especificidad débil; se agrega el conjunto de calibración.
- 0.3 (2026-10-13): se agrega la re-evaluación por cambios del dominio; cada
  decisión registra la versión de `domain.md`. Se elimina el resultado
  "revisar": toda decisión es aceptar o rechazar. Las advertencias de
  conversión y las dudas se registran sin bloquear. Los documentos de david
  con pertinencia 1 se aceptan; los del agente se aceptan con suma de 7 o
  más sin ceros. Los duplicados de título, emisor y año se rechazan.
- 0.4 (2026-10-13): se agregan las síntesis propias como origen que entra
  sin pasar por la selección. Las síntesis de DataCamp y Pluralsight
  (antes `design/synthesis/s01a-*` y `s01b-*`) pasan a `syntheses/`.
