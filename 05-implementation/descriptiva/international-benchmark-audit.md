# Calificación internacional interna: Analítica descriptiva y visualización de datos

## Dictamen

| Alcance calificado | Puntaje |
|---|---:|
| Secuencia presencial implementada (P001, P100–P109, P120–P125, P150–P154) | **9.3 / 10** |
| Curso completo, con evidencia disponible al 29 de septiembre de 2026 | **8.8 / 10** |

La diferencia no obedece a una carencia de identidad, casos o profundidad
analítica. Corresponde a dos componentes que todavía no están materializados
ni auditables en este repositorio: los LABs de evaluación y la plantilla
`distribution/descriptiva/` que GitHub Classroom replicará para estudiantes.

Esta es una calificación interna contra el corpus de referentes del proyecto;
no es acreditación ni una atribución de nota por MIT, Berkeley, Stanford u
otra institución.

## Rúbrica y evidencia

| Dimensión | Máx. | Puntaje | Evidencia y juicio |
|---|---:|---:|---|
| Identidad de Analytics, decisión y alcance | 15 | 14.5 | C01 formula preguntas y métricas en P120–P125. La secuencia preserva que SQL, Pandas y BI sean medios para el análisis, coherente con S04.F01–F03. |
| Exploración, visualización, interpretación y límites | 20 | 18.5 | C02–C04 se ejercitan mediante casos de ventas, vuelos, cadena de suministro, Scopus, marketing y salarios; P125 hace explícito el límite asociación/causalidad. Falta verificar sistemáticamente ese límite en la evaluación de todos los casos. |
| Preparación, acceso y fluidez técnica durable | 10 | 9.5 | P100–P107 cubren programación, transformación, limpieza, Pandas y SQLite; las actividades no dependen de una plataforma única. |
| Práctica auténtica, casos integrados y portafolio | 15 | 14.0 | La secuencia contiene casos reales y productos persistentes, sin depender de un capstone. Resta verificar la presentación final del portafolio en los repositorios individuales. |
| Trabajo responsable, reproducible y documentado | 10 | 8.0 | P001, P101, P107–P109 y las pruebas apoyan reproducibilidad, privacidad y productos verificables. Falta evidencia de criterios recurrentes para límites, integridad y comunicación responsable en la evaluación. |
| Evidencia de evaluación y retroalimentación | 15 | 11.5 | `pytest` y los productos en `submission/` permiten evaluación técnica de P. Los LABs, que aportarán evaluación independiente y evidencia de aprendizaje, aún no pertenecen a esta implementación. |
| Entrega escalable y flujo del estudiante | 5 | 3.0 | El sitio público sostiene el aula invertida y ya publica sesiones, DataCamp y evaluación. No existe todavía la plantilla `distribution/descriptiva/` para auditar su uso con GitHub Classroom. |
| Gobernanza, trazabilidad y mejora continua | 10 | 9.0 | `traceability.yaml` permite ir de cada P a C01–C05 y existe una auditoría contra diseño. Resta regenerar S05 con su tabla inversa completa y materializar la trazabilidad hasta distribución. |
| **Total** | **100** | **88.0** | **8.8 / 10** |

## Comparación con el estándar del corpus

El curso satisface de forma fuerte los rasgos que convergen en S04:

- trabajo con datos conectado con preguntas y decisiones (`S04.F01–F02`);
- exploración, visualización e interpretación (`S04.F05–F06`);
- comunicación y práctica integrada con productos (`S04.F07`, `S04.F09`);
- herramientas como medios y no como identidad (`S04.F10`).

La oferta publicada confirma la existencia de una capa común de aula invertida:
sesiones organizadas, soporte DataCamp y una página de evaluación con talleres y
laboratorios. No se contó como evidencia de que los nuevos P ya estén
distribuidos, pues la página de evaluación representa una iteración anterior
de la secuencia.

## Condiciones concretas para 10 / 10

1. Materializar y probar `distribution/descriptiva/` como plantilla de
   GitHub Classroom: solo artefactos estudiantiles, sin `professor/`, con el
   `requirements.txt` raíz y Actions que descubran todos los P con independencia
   de su profundidad.
2. Diseñar y auditar los LABs como evaluación independiente de C01–C05; las
   pruebas técnicas deben complementar, no sustituir, la evidencia de juicio
   analítico y comunicación.
3. Reforzar y evaluar de forma visible C04 —límites entre descripción,
   diagnóstico, asociación y causalidad— en más de un caso, o justificar que
   P125 es la demostración concentrada suficiente.
4. Regenerar S05 para reparar la tabla inversa y el encabezado formal; volver
   a ejecutar la auditoría de S01 y esta rúbrica.
5. Auditar una asignación real generada por GitHub Classroom y comprobar que
   el producto del estudiante alimenta un portafolio visible y evaluable.

## Registro de construcción

- Tarea: `implementation/tasks/s02-score-course-against-international-benchmarks.md`.
- Curso: `descriptiva`.
- Fecha de ejecución: 2026-09-29.
- Fuentes locales: `design/synthesis/s04-synthesis.md`,
  `design/synthesis/s05-diseno-descriptiva.md`,
  `implementation/descriptiva/traceability.yaml`,
  `implementation/descriptiva/audit-against-design.md` y el corpus de
  `design/benchmarks/`.
- Evidencia pública contextual: el sitio de Analítica Descriptiva y
  Visualización de Datos, consultado el 2026-09-29.
