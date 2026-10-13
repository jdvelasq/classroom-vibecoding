# Fuentes de búsqueda de evidencia

Versión 0.1 (borrador)

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

## Fuente 1: plataformas de aprendizaje

**Qué buscar**: rutas por rol, no cursos sueltos. Una ruta por rol muestra
qué conjunto de competencias espera el mercado para un cargo (por ejemplo,
*data analyst*, *analytics engineer*, *machine learning engineer* aplicado
a la analítica).

| Plataforma | Tipo de ruta | Acceso |
|---|---|---|
| Coursera | *Professional Certificates*, *Specializations* | Agente |
| DataCamp | *Career Tracks*, *Skill Tracks* | Agente |
| edX | *Professional Certificates*, *MicroMasters* | Agente |
| Udemy | *Learning paths* públicos, si existen | Agente |
| Pluralsight | *Skill Paths*, *Paths* por rol | Manual: david guarda los PDF con su cuenta |

**Qué registrar**: la página pública de la ruta con su lista de cursos o
módulos y las competencias declaradas.

**Límite**: hasta 3 rutas por plataforma y por corrida.

**Categoría de destino**: `professional-learning`.

## Fuente 2: syllabus y planes de estudio universitarios

**Qué buscar**: planes de estudio y syllabus publicados de programas de
analítica (maestría, especialización o pregrado), con resultados de
aprendizaje, competencias o contenidos por curso. Se prefieren el plan de
estudios completo del programa y los syllabus de sus cursos centrales.

**Términos adicionales**: *curriculum*, *syllabus*, *course catalog*,
*learning outcomes*; plan de estudios, malla curricular, contenido
programático.

**Límite**: hasta 2 documentos por universidad y 10 por corrida.

**Categoría de destino**: `institutional`.

### Universidades propuestas

> Lista propuesta, pendiente de ajuste por david. El programa concreto de
> cada universidad se identifica en la búsqueda.

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

**Latinoamérica**

- Tecnológico de Monterrey (México).
- Instituto Tecnológico Autónomo de México (ITAM).
- Pontificia Universidad Católica de Chile.
- Universidad de Chile.
- Fundação Getulio Vargas (Brasil).
- Universidade de São Paulo (Brasil).

**Colombia**

- Universidad Nacional de Colombia.
- Universidad de los Andes.
- Pontificia Universidad Javeriana.
- Universidad EAFIT.
- Universidad Icesi.
- Universidad del Rosario.

## Fuentes futuras

Fuera de alcance por ahora:

- **Ofertas de empleo**: avisos públicos para cargos de analítica, como
  evidencia de mercado (`domain.md`, sección "Evidencia de mercado").
- **Marcos profesionales**: INFORMS *Certified Analytics Professional*
  (CAP) y SFIA (*Skills Framework for the Information Age*), con categoría
  `authoritative`.

## Versión y cambios

- 0.1 (2026-10-13): borrador inicial con dos fuentes (plataformas de
  aprendizaje y syllabus universitarios), términos alineados con
  `domain.md` 0.7, límites por corrida y lista propuesta de universidades.
