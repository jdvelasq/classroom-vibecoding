# Plan de cursos y matriz de resultados

Cuarto eslabón de la cadena de diseño:

```
01-evidence → 02-competencies → 03-learning-outcomes → 04-curriculum → 05-implementation
(documentos)  (mapa sin nivel)  (perfil y RA)          (RA × cursos)   (un syllabus por curso)
```

Este directorio reparte los resultados de aprendizaje del posgrado en
analítica entre sus cursos, y fija los resultados propios de los dos
cursos introductorios de pregrado.

## Archivos

- `format.md`: formato de los tres archivos siguientes, reglas y un
  ejemplo trabajado. Es la norma de este directorio; versiónalo como
  `03-learning-outcomes/format.md`.
- `courses.md`: los ocho cursos (uno de ellos propuesto), su nivel, su
  carpeta, sus subcampos de `01-evidence/domain.md` y su propósito. Los cursos salen de la definición
  de analítica y los fija david; no se reescribe sin su decisión.
- `matrix.csv`: resultados de aprendizaje × cursos de posgrado, con nivel
  `introduce`, `desarrolla` o `domina`.
- `undergraduate/<carpeta>.md`: los resultados de curso de `data` y
  `fundamentos`.

`matrix.csv` y `undergraduate/` se escriben con la skill
`mapping-curriculum` (`.agents/skills/mapping-curriculum/`). Sus scripts
leen los resultados y el mapa y comprueban las reglas; el modelo solo
propone la matriz y redacta los resultados de pregrado.

## Reglas

- Los cursos de posgrado son autocontenidos: sus estudiantes no han visto
  los cursos de pregrado.
- Los cursos de pregrado no derivan de los resultados del posgrado: salen
  de las competencias incluidas del mapa, a nivel introductorio.
- `01-evidence/`, `02-competencies/` y `03-learning-outcomes/` son de solo
  lectura desde aquí. Si un resultado falta o no cabe en ningún curso, se
  informa a david; no se corrige desde este directorio.
- Al terminar, verifica la identidad de `AGENTS.md` en la raíz: ningún
  curso es una versión abreviada de una disciplina contribuyente.
- Escribe en español.
