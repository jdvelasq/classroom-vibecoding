# Perfil de egreso y resultados de aprendizaje

Tercer eslabón de la cadena de diseño:

```
01-evidence  →  02-competencies  →  03-learning-outcomes  →  matriz RA × cursos  →  syllabus
(documentos)    (mapa sin nivel)    (perfil y RA, con nivel)
```

Este directorio convierte las competencias incluidas del mapa
(`02-competencies/map/`) en el perfil de egreso y los resultados de
aprendizaje de un programa: el posgrado en analítica, con nivel de
especialización. La maestría y el doctorado reutilizan estos resultados y
agregan solo su componente de investigación o de tesis, que queda fuera de
este directorio.

Sigue el Acuerdo CESU 02 de 2020, numeral 2.2 a y b, y las
características 18, 24 y 25 (`00-regulations/md/cesu-acuerdo-02-2020.md`).

## Archivos

- `format.md`: formato del perfil y de cada resultado de aprendizaje,
  reglas de cobertura y un ejemplo trabajado. Es la norma de este
  directorio; versiónalo como `02-competencies/format.md`.
- `profile.md`: el perfil de egreso.
- `outcomes/<id>.md`: un resultado de aprendizaje por archivo.

Se escriben con la skill `writing-learning-outcomes`
(`.agents/skills/writing-learning-outcomes/`). Sus scripts leen el mapa y
comprueban el formato, la trazabilidad y la cobertura; el modelo solo
redacta el perfil y los resultados.

## Reglas

- Solo entran competencias con `estado: "incluida"`. Las candidatas no
  entran.
- Toda competencia incluida queda cubierta por al menos un resultado de
  aprendizaje, y el número de resultados es acotado (véase `format.md`).
- Todo resultado se traza hasta la evidencia de desempeño de las
  competencias que cubre, y por ella hasta `01-evidence/index.csv`.
- `01-evidence/` y `02-competencies/` son de solo lectura desde aquí. Si
  una competencia falta, está mal planteada o no tiene evidencia de
  desempeño, se informa a david; no se corrige desde este directorio.
- Al terminar un conjunto de resultados, verifica la identidad de
  `AGENTS.md` en la raíz: el perfil y los resultados describen a un
  profesional de la analítica, no un programa abreviado de una disciplina
  contribuyente.
- Escribe en español.
