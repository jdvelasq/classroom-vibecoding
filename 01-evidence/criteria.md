# Criterios de selección de documentos de evidencia

Versión 0.2 (borrador)

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

Se aplica en este orden; la primera condición que se cumple decide.

1. **Rechazar** si la pertinencia es 0. El documento pasa automáticamente a
   `rejected/`. La falta de pertinencia prevalece sobre las advertencias de
   conversión: un documento ajeno al campo no se queda en `ingest/` aunque
   su conversión haya fallado.
2. **Revisar** si el documento es pertinente y tiene advertencias de
   conversión (o acceso en 0). Se queda en `ingest/` para que david decida.
3. **Documentos aportados por david**: **aceptar** si la pertinencia es 2;
   **revisar** si es 1.
4. **Documentos encontrados por el agente**:
   - **Aceptar**: ningún criterio en 0 y suma de 8 o más.
   - **Rechazar**: suma de 5 o menos, o algún criterio en 0. Pasa a
     `rejected/`.
   - **Revisar**: cualquier otro caso. Se queda en `ingest/`.

Solo los documentos pertinentes con advertencias de conversión o con
decisión "revisar" permanecen en `ingest/` a la espera de david.

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
