# Fuentes de búsqueda de evidencia

Versión 0.4 (aprobada)

## Propósito

Definir dónde busca el agente documentos de evidencia, qué busca en cada
fuente, cuántos trae por corrida y en qué categoría los propone. Este
archivo solo decide dónde buscar. Si un documento entra o no lo decide
`criteria.md`, aplicado contra `domain.md`.

## Reglas generales

- Solo páginas públicas, sin iniciar sesión ni pagar.
- Cada página web se imprime a PDF y se registran la URL, la fecha de
  consulta y la consulta de búsqueda que la encontró.
- Los documentos encontrados por el agente van a `ingest/agent/` y se
  juzgan con los cinco criterios completos.
- Los términos de búsqueda se usan en inglés y en español.
- Un documento ya indexado no se vuelve a traer.
- Cada página consultada se registra en `searches.csv` con su fuente,
  destino, consulta, URL, fecha, archivo, SHA-256 y resultado. Una URL ya
  traída no se vuelve a traer.

## Términos de búsqueda

Se derivan de `domain.md` (versión 0.7) y se combinan con el tipo de
documento propio de cada fuente.

- **Campo**: *analytics*, *business analytics*, analítica, analítica de
  datos.
- **Subcampos**: *descriptive*, *diagnostic*, *predictive* y *prescriptive
  analytics*; *big data analytics*; *data products*, MLOps, DataOps;
  *data engineering for analytics*, *analytics engineering*, SQL.
- **Tendencia emergente**: *generative AI for data analysis*, *AI agents
  for analytics*, *LLM for data analysis*; IA generativa para analítica.
- **Precursores**: *business intelligence*, *data mining*.

## Plataformas de aprendizaje: no se buscan

Las plataformas de aprendizaje se cubren con síntesis propias en
`syntheses/` (por ejemplo, `datacamp.md` y `pluralsight.md`), que
reconstruyen el catálogo de rutas por rol de cada proveedor. Una página
impresa por ruta describe peor la plataforma que esas síntesis, así que la
búsqueda no las incluye. Los PDF de Pluralsight que guarda david siguen
entrando como aportados por david.

## Fuente: syllabus y planes de estudio universitarios

**Qué buscar**: planes de estudio y syllabus publicados de programas de
analítica (maestría, especialización o pregrado), con resultados de
aprendizaje, competencias o contenidos por curso. Se prefieren el plan de
estudios completo del programa y los syllabus de sus cursos centrales.

**Términos adicionales**: *curriculum*, *syllabus*, *course catalog*,
*learning outcomes*; plan de estudios, malla curricular, contenido
programático.

**Límite**: hasta 2 documentos por universidad y 10 por corrida.

**Categoría de destino**: `institutional`.

### Universidades

Solo referentes internacionales. El programa de especialización de david
(primera cohorte en 2015) es el referente en Colombia y la región, así que
los programas latinoamericanos y colombianos no se buscan como evidencia de
competencias. El programa concreto de cada universidad se identifica en la
búsqueda.

**Referentes internacionales**

- Massachusetts Institute of Technology (MIT).
- Carnegie Mellon University.
- Georgia Institute of Technology.
- North Carolina State University (Institute for Advanced Analytics).
- Northwestern University.
- University of Texas at Austin.
- Imperial College London.
- University of Warwick.
- National University of Singapore.

## Fuentes futuras

Fuera de alcance por ahora:

- **Ofertas de empleo**: avisos públicos para cargos de analítica, como
  evidencia de mercado (`domain.md`, sección "Evidencia de mercado").
- **Marcos profesionales**: INFORMS *Certified Analytics Professional*
  (CAP) y SFIA (*Skills Framework for the Information Age*), con categoría
  `authoritative`.
- **Programas de Latinoamérica y Colombia**: sirven para el posicionamiento
  del programa frente a la oferta regional, no como evidencia de
  competencias.

## Versión y cambios

- 0.1 (2026-10-13): borrador inicial con dos fuentes (plataformas de
  aprendizaje y syllabus universitarios), términos alineados con
  `domain.md` 0.7, límites por corrida y lista propuesta de universidades.
- 0.2 (2026-10-13): aprobada por david con los límites, la lista de
  universidades y Udemy tal como estaban. Los PDF de Pluralsight cuentan
  como aportados por david. Se agrega el registro de búsquedas
  `searches.csv`.
- 0.3 (2026-10-13): se quitan las universidades de Latinoamérica y Colombia;
  quedan solo los referentes internacionales. La comparación regional pasa a
  fuentes futuras, como posicionamiento.
- 0.4 (2026-10-13): la búsqueda se limita a universidades. Las plataformas
  de aprendizaje quedan cubiertas por las síntesis propias de
  `syntheses/` (criteria.md 0.4).
