# Auditoría contra diseño: Analítica descriptiva y visualización de datos

## Resultado

**Condicionalmente listo.** La implementación actual ofrece trazabilidad
bidireccional suficiente entre los talleres presenciales y las cinco
capacidades de `s05-diseno-descriptiva.md`. Aún no existe una plantilla
materializada en `distribution/descriptiva/`; por ello no se ha verificado la
fase de entrega por GitHub Classroom.

Esta auditoría no equivale a una calificación internacional 10/10. Establece
la evidencia necesaria para realizarla cuando se complete la distribución y
se integren las demás evidencias del curso.

## Insumos auditados

| Insumo | Función |
|---|---|
| `design/synthesis/s05-diseno-descriptiva.md` | Diseño de contenido y capacidades C01–C05. |
| `implementation/descriptiva/traceability.yaml` | Declaración de trazabilidad actividad-capacidad. |
| `implementation/common/P001_*`–`P009_*` | Fundamentación común reutilizada por el curso. |
| `implementation/descriptiva/P100_*`–`P105_*`, `P150_*`–`P154_*` | Talleres propios de Descriptiva. |
| `AGENTS.md` | Identidad curricular y reglas técnicas de distribución. |

No se encontró `distribution/descriptiva/` al ejecutar la auditoría.

## Trazabilidad hacia adelante

| Capacidad de diseño | Talleres que la evidencian | Evidencia implementada |
|---|---|---|
| `descriptiva.C01` — preguntas y métricas para decidir | P100–P105 | Casos con preguntas de negocio; P103 formula preguntas de inteligencia tecnológica; P105 evalúa preguntas y respuestas persistidas. |
| `descriptiva.C02` — exploración antes de concluir | P002, P004, P005, P007–P009, P100–P105, P150–P154 | Datos, código/notebooks, resultados en `submission/` cuando aplica y pruebas de actividad. |
| `descriptiva.C03` — visualización e interpretación | P007, P008, P009, P100–P105, P150–P154 | Talleres de análisis y comunicación visual, incluidos dashboard, OLAP y serving BI. |
| `descriptiva.C04` — límites entre descripción, diagnóstico, asociación y causalidad | P105 | Preguntas de salarios que exigen interpretar brechas sin convertir asociaciones en causalidad. |
| `descriptiva.C05` — documentación y comunicación responsable | P003, P004, P009, P103–P105, P150–P154 | Productos persistentes, comunicación de hallazgos y artefactos BI. |

La secuencia preserva Analytics: los componentes de bases de datos y BI
(`P150`–`P154`) aparecen después de los casos descriptivos y operan como
medios para explorar, comunicar y servir análisis, no como un currículo de BI
autónomo.

## Trazabilidad inversa

| Talleres | Diseño o justificación |
|---|---|
| P001 | Actividad habilitadora común; aporta prácticas de trabajo reproducible y se enlaza a `S04.F08`. |
| P002 | `descriptiva.C02`. |
| P003 | `descriptiva.C05`. |
| P004 | `descriptiva.C02`, `descriptiva.C05`. |
| P005 | `descriptiva.C02`. |
| P010 | `descriptiva.C05`. |
| P007 | `descriptiva.C02`, `descriptiva.C03`. |
| P008 | `descriptiva.C02`, `descriptiva.C03`. |
| P009 | `descriptiva.C02`, `descriptiva.C03`, `descriptiva.C05`. |
| P100–P102 | `descriptiva.C01`, `descriptiva.C02`, `descriptiva.C03`. |
| P103 | `descriptiva.C01`, `descriptiva.C02`, `descriptiva.C03`, `descriptiva.C05`. |
| P104 | `descriptiva.C01`, `descriptiva.C02`, `descriptiva.C03`, `descriptiva.C05`. |
| P105 | `descriptiva.C01`, `descriptiva.C02`, `descriptiva.C03`, `descriptiva.C04`, `descriptiva.C05`. |
| P150–P154 | `descriptiva.C02`, `descriptiva.C03`, `descriptiva.C05`. |

## Hallazgos

### Diseño

- La tabla de trazabilidad inversa de `s05-diseno-descriptiva.md` está vacía,
  aunque su tabla directa sí define C01–C05.
- El encabezado de perfil de ingreso contiene el carácter inicial `+`.
- La capacidad C04 cuenta con una evidencia explícita en P105. Es cobertura
  válida, pero una auditoría posterior deberá comprobar que la discusión
  docente y los criterios de evaluación hacen visible ese límite conceptual.

### Implementación

- Todas las actividades de la secuencia declarada están enlazadas en
  `traceability.yaml`; no se detectó un taller huérfano.
- La existencia de `pytest` aporta verificación técnica de los productos, pero
  no prueba por sí sola que se alcanzó una capacidad terminal.
- P100–P105 hacen explícito el contexto de decisión; la auditoría posterior
  debe verificar semánticamente el archivo de preguntas en cada caso, no solo
  su presencia.

### Distribución

- `distribution/` solo contiene su estructura inicial y `tasks/`; falta
  `distribution/descriptiva/` como repositorio plantilla materializado.
- Por tanto siguen sin verificar: exclusión de `professor/`, copia de los P
  seleccionados, `requirements.txt`, workflow de Actions y ejecución desde la
  profundidad real de la plantilla.

## Próximas verificaciones

1. Corregir los dos defectos formales de `s05-diseno-descriptiva.md` al
   regenerar S05, no manualmente.
2. Materializar `distribution/descriptiva/` desde los P aprobados, sin
   `professor/` y conservando las pruebas portables.
3. Ejecutar nuevamente esta auditoría sobre la plantilla y una copia generada
   por GitHub Classroom.
4. Añadir la evidencia de aula invertida y de los LABs al ejercicio posterior
   de comparación con referentes internacionales.
