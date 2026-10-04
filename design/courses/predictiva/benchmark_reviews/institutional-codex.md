# S02 — Revisión de predictiva contra institutional (Codex)

> **Estado:** ejecución incremental en curso. Este informe no es una revisión
> completa de la familia mientras el inventario conserve PDFs pendientes.

## Inventario y función de la evidencia

| Ruta | Familia | Páginas/secciones leídas | Qué puede sustentar | Límite |
| --- | --- | --- | --- | --- |
| `design/benchmarks/institutional/unal-lineamientos-armonizacion-curricular.pdf` | institutional | 4 páginas, leídas completas; ejes, dimensiones macro/meso/micro y etapas de la ruta | Coherencia entre pertinencia, resultados de aprendizaje, organización curricular, evaluación y mejora continua participativa. | No define contenidos de Analytics ni prescribe técnicas o herramientas. |
| `design/benchmarks/institutional/mit-data-science-and-machine-learning.pdf` | institutional | 17 páginas, leídas completas; estructura semanal y currículo | Ejemplo institucional de secuencia con casos, representación, regresión, clasificación, anomalías/fraude, recomendación y grafos. | Es un programa de Data Science/ML; no puede redefinir Predictiva ni convertirla en su versión abreviada. |
| `design/benchmarks/institutional/berkeley-data-c101-data-engineering.pdf` | institutional | 1 página, leída completa | Ejemplo de ciclo de vida, preparación, exploración, visualización, análisis, ML, colaboración y operación fiable a escala. | Es un curso avanzado de Data Engineering; no prescribe infraestructura o ingeniería como eje de Predictiva. |
| `design/benchmarks/institutional/berkeley-data-c102-data-inference-and-decisions.pdf` | institutional | pendiente | — | Pendiente de lectura. |
| `design/benchmarks/institutional/*.pdf` (21 restantes) | institutional | pendientes | — | Pendientes de lectura; no se emite aún un dictamen de familia. |

## Señales extraídas

| ID | Afirmación del documento | Inferencia permitida | Página/sección |
| --- | --- | --- | --- |
| I01 | UNAL organiza la armonización como pertinencia y resultados de aprendizaje, organización curricular, implementación, monitoreo y mejora continua; distingue macro, meso y microcurrículo. | Cada cambio futuro de actividad debe poder rastrearse a una necesidad, un resultado de aprendizaje, una actividad/evidencia y un mecanismo de revisión. | `unal-lineamientos…`, pp. 1–4. |
| I02 | MIT trata clustering más allá de KMeans —incluido spectral clustering— junto con representación, grafos y embeddings. | Es una capacidad que exige dictamen explícito contra P206/P207; la presencia en el programa no justifica su inclusión automática. | `mit-data-science…`, pp. 6–7. |
| I03 | MIT incluye anomalías/fraude y clasificación con falsos positivos/negativos, precisión, recobrado y F1. | Refuerza la revisión de C04: el producto de evento raro tiene una contribución distinguible frente a clasificación genérica. | `mit-data-science…`, p. 8. |
| I04 | Berkeley C101 presenta un ciclo de vida desde preparación hasta operación fiable, escalable y colaborativa. | Refuerza que los activos y contratos reutilizables son parte de una capacidad analítica usable, sin exigir enseñar Data Engineering como identidad. | `berkeley-data-c101…`, p. 1. |

## Contraste con el diseño actual

| Señal | Pxxx | Ancla S01 | Hitos | Superficies | Dictamen | Razón |
| --- | --- | --- | --- | --- | --- |
| I01 — trazabilidad y mejora | P200–P225 | Productos, evidencia y auditoría de cada mapa | Según cada mapa | Según cada mapa | cubierta parcialmente | S01 permite anclar actividades, pero existen entradas de trazabilidad pendientes y falta aún completar la revisión institucional de la familia antes de proponer el cambio proporcional. |
| I02 — clustering espectral/grafos | P206, P207 | Selección/lectura; representación/selección | P206 H01–H05; P207 H01–H07 | P206 S01–S03; P207 S01–S04 | no sustentado / fuera de alcance por ahora | KMeans, silueta, TF–IDF y UMAP ya tienen contribución; P206/P207 conservan tensión de identidad dentro de Predictiva. MIT no demuestra que spectral clustering resuelva una dificultad de estos casos. |
| I03 — evento raro | P203–P205 | Métrica por clase; caso binario; revisión de umbrales | P203 H01–H05; P204 H01–H05; P205 H01–H05 | P203 S01–S03; P204 S01–S03; P205 S01–S03 | candidato estructural | Corrobora C04 del informe SAS: falta entrenar/evaluar un evento raro con precisión–recobrado y revisión de errores. |
| I04 — activos reutilizables | P217, P218 | Modelo externo; esquema/servicio | P217 H01–H03; P218 H01–H04 | P217 S01–S04; P218 S01–S04 | candidato a cambio | Corrobora C02: falta un contrato persistente que vincule predictor, transformación y entrada. |

## Cobertura de casos y contribuciones predictivas

| Caso/aplicación del benchmark | Pregunta, unidad, horizonte y resultado | Pxxx/HNN/SNN comparados | ¿Qué aporta que no exista? | Dictamen y evidencia adicional necesaria |
| --- | --- | --- | --- | --- |
| Anomalías/fraude MIT | Evento; evento raro; clasificación y errores asimétricos | P203–P205 | Métricas y revisión de error de evento raro, no sólo probabilidades simuladas. | C04 vigente; requiere dataset local seguro, trazable y decisión institucional. |
| Casos ML, recomendación y grafos MIT | Variables, ítems/usuarios o redes; productos variados | P200–P225 | La mayoría de familias ya tiene contraparte; no se justifica copiar los casos de MIT. | Lectura de referentes restantes pendiente. |

## Cobertura conceptual y técnica del referente

| Capacidad del índice o sección | Rol para Analytics y práctica técnica asociada | Pxxx/HNN/SNN comparados | Cobertura actual verificable | Dictamen y siguiente evidencia necesaria |
| --- | --- | --- | --- | --- |
| Spectral clustering, grafos y embeddings | Representar similitud o red cuando las características ordinarias no bastan. | P206/P207; P224/P225 | Hay clustering, UMAP y representación gráfica, pero no problema local que requiera spectral clustering. | No sustentado por ahora; revisar sólo si otro referente o caso local aporta una dificultad no cubierta. |
| Anomalías, precisión/recobrado y F1 | Evaluar evento raro y el costo informativo de los errores. | P203–P205 | Hay desbalance textual, AUC/exactitud y umbrales; falta el producto completo de evento raro. | C04 vigente. |
| Portafolio/casos y activos reutilizables | Hacer visibles productos, evidencia y contratos de uso. | P200, P216–P218, P221 | Persistencia existe; selección y contratos aún son parcialmente verificables. | C01 y C02 vigentes. |

## Hallazgos prioritarios de faltantes

| Prioridad | Falta demostrada | Por qué importa para Analytics | Pxxx/HNN/SNN relacionados | Candidato y siguiente decisión/evidencia |
| --- | --- | --- | --- | --- |
| 1 | Evaluación completa de evento raro con precisión–recobrado y revisión de errores. | Complementa la clasificación con un producto predictivo cuya utilidad depende del perfil de errores. | P203–P205 | C04; buscar caso local trazable y definir revisión humana, no automatización. |
| 2 | Contrato persistente modelo–entrada para capacidades usables. | Evita divergencia entre predictor, formulario y API. | P217–P218 | C02; validar contrato mínimo sin añadir MLOps. |
| 3 | Trazabilidad curricular completa de las actividades y sus resultados. | UNAL exige articular pertinencia, resultados, organización, implementación y evaluación continua. | P200–P225 | Pendiente de completar la lectura institucional y de decidir el mecanismo mínimo; no se acepta cambio aún. |

## Propuestas candidatas — no aceptadas

Las candidatas C01, C02 y C04 quedan corroboradas de manera incremental; sus
contratos completos permanecen en `sas-data-mining-codex.md`. No se acepta ni
duplica aquí una propuesta mientras faltan documentos de la familia.

## Señales ya cubiertas o descartadas

- MIT incluye técnicas y productos de un programa amplio de Data Science/ML;
  no se adopta su catálogo ni se concluye que Predictiva deba incluir deep
  learning, causalidad, SVM, grafos o spectral clustering.
- Berkeley C101 es evidencia de Data Engineering contribuyente, no una razón
  para transformar la identidad de Predictiva en infraestructura.

## Auditoría de identidad de Analytics

La función de esta familia es ilustrar operacionalizaciones institucionales y
coherencia curricular. Analytics sigue siendo la identidad; ML, Data Science,
Data Engineering, redes e IA son disciplinas contribuyentes. Los candidatos
vigentes fortalecen productos predictivos y sus evidencias sin convertirlos en
automatización de decisiones.

## Registro incremental

- Ejecución de directorio iniciada con `benchmark=design/benchmarks/institutional/`,
  `course=predictiva`, `executor=codex`.
- Leídos: `unal-lineamientos-armonizacion-curricular.pdf`,
  `mit-data-science-and-machine-learning.pdf` y
  `berkeley-data-c101-data-engineering.pdf`.
- Pendientes: 23 PDFs del directorio, incluido el ejercicio piloto UNAL.
- No se modificó ningún `Pxxx_activity.md`, `Pxxx_log.md`, `implementation/` ni
  `traceability.yaml`.
