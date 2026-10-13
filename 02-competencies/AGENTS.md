# Mapa de competencias

Segundo eslabón de la cadena de diseño:

```
01-evidence  →  02-competencies  →  perfil y RA del programa  →  matriz RA × cursos  →  syllabus
(documentos)    (mapa sin nivel)    (con nivel)
```

Este directorio convierte la evidencia aceptada en `01-evidence/index.csv` en
un mapa de competencias del campo definido en `01-evidence/domain.md`.
Sigue la definición del Acuerdo CESU 02 de 2020, numeral 2.2 b
(`00-regulations/md/cesu-acuerdo-02-2020.md`): una competencia es un conjunto
articulado de conocimientos y habilidades que se evalúa mediante resultados
de aprendizaje.

## Archivos

- `format.md`: formato de cada competencia, regla de consenso y
  granularidad. Es la norma de este directorio; versiónalo como
  `criteria.md`.
- `map/<id>.md`: una competencia por archivo, con el formato vigente.
- `mapped.csv`: documentos ya mapeados, con las versiones de `format.md` y
  `domain.md` usadas. Lo escribe la skill.

El mapa se construye con la skill `mapping-competencies`
(`.agents/skills/mapping-competencies/`). Sus scripts calculan el consenso y
el estado; no se escriben a mano.

## Reglas

- El mapa no asigna niveles. El nivel (pregrado, especialización, maestría)
  se decide al redactar el perfil y los resultados de aprendizaje.
- Toda afirmación del mapa cita su fuente por el `id` de `index.csv`. Una
  competencia sin fuente no entra.
- Solo se citan documentos con decisión `accept`.
- `01-evidence/` es de solo lectura desde aquí. Si un documento falta o está
  mal clasificado, se informa a david; no se corrige desde este directorio.
- Escribe en español.
