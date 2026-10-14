# Auditoría contra diseño: Analítica prescriptiva

## Dictamen

**Lista condicionalmente para la fase de talleres presenciales.** La secuencia
P300–P322 materializa el producto terminal definido en
`s05-diseno-prescriptiva.md`: políticas computables y gobernadas para
decisiones recurrentes. No es aún una auditoría completa del curso ni una
calificación internacional: faltan los LABs, la distribución por GitHub
Classroom y evidencia observada de aprendizaje.

## Insumos auditados

| Insumo | Función |
|---|---|
| `design/synthesis/s05-diseno-prescriptiva.md` | Capacidades terminales C01–C05 y frontera curricular. |
| `implementation/prescriptiva/activity-architecture.md` | Progresión y productos de política. |
| `implementation/prescriptiva/traceability.yaml` | Trazabilidad actividad-capacidad. |
| `implementation/prescriptiva/P300_*`–`P322_*` | Talleres, soluciones del profesor, plantillas y evidencia persistente. |
| `AGENTS.md` | Identidad de Analytics y contrato técnico de actividades. |

## Resultado de la auditoría de identidad

- **Pregunta de línea:** qué acción recurrente debe tomarse bajo objetivos,
  restricciones, salvaguardas, excepciones y revisión.
- **Producto terminal:** política computable con acción, autoridad, guardas,
  monitoreo y gatillos; no un óptimo, una frontera o una simulación aislada.
- **Contribuciones funcionales:** optimización, simulación y pronóstico
  aportan factibilidad, evidencia o validación; no organizan el currículo.
- **Dictamen:** la identidad de Analytics se preserva. El curso no es un
  currículo abreviado de Investigación de Operaciones.

## Trazabilidad hacia adelante

| Capacidad | Evidencia principal |
|---|---|
| `prescriptiva.C01` — contrato de política | P300–P303, P307–P308, P310 y P322. |
| `prescriptiva.C02` — política basada en evidencia | P302, P304–P309 y P314–P319. |
| `prescriptiva.C03` — validación bajo incertidumbre | P304, P307, P309–P319 y P322. |
| `prescriptiva.C04` — autoridad y excepciones | P300–P311, P313–P322. |
| `prescriptiva.C05` — monitoreo y recalibración | P306–P322, con P320–P321 como formalización transversal. |

## Verificaciones técnicas realizadas

- 23 actividades con nombres P300–P322.
- Estructura uniforme: `data/`, `notebooks/`, `professor/`, `src/`,
  `submission/`, `temp/` y `tests/`.
- Sin `scripts/` ni `README.md` dentro de actividades.
- Solución en `professor/`; notebook de estudiante sin celdas.
- Suite de talleres: 32 pruebas aprobadas en la última auditoría estructural.

## Límites y próximos pasos

1. Diseñar los LABs como evidencia independiente de las cinco capacidades;
   `pytest` confirma participación y artefactos, no dominio analítico.
2. Materializar `distribution/prescriptiva/`, excluyendo `professor/`, y
   verificar la copia que se entregue a estudiantes mediante el mecanismo de
   distribución que sustituya a GitHub Classroom.
3. Auditar la experiencia de aula invertida y los resultados de cohortes antes
   de cualquier calificación frente a referentes internacionales.
4. Mantener P320 y P321 como criterios transversales en cada taller, no solo
   como las dos actividades finales especializadas.

## Registro

- Fecha: 2026-10-01.
- Alcance: implementación presencial; no distribución ni LABs.
- Resultado: trazabilidad completa y estructura conforme; evidencia de
  efectividad pedagógica pendiente.
