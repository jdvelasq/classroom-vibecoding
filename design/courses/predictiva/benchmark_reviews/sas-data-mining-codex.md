# S02 — Revisión de predictiva contra sas-data-mining (Codex)

## Inventario y función de la evidencia

| Ruta | Familia | Páginas/secciones leídas | Qué puede sustentar | Límite |
| --- | --- | --- | --- | --- |
| `design/benchmarks/professional-learning/sas-data-mining.pdf` | professional-learning | 14 páginas; «El Ciclo de Vida Analítico de SAS», pasos 1–4 del descubrimiento, Enterprise Miner, Factory Miner e implementación/monitoreo | Señales de práctica profesional: pregunta–hipótesis, tabla analítica, partición y validación, comparación de modelos, activos de calificación y transición hacia una capacidad usable. | Es un white paper de SAS (2015), con interés comercial y centrado en su plataforma. No define la identidad curricular de Analytics, no prescribe SAS ni sus algoritmos, y no justifica por sí solo AutoML, Big Data, monitoreo de producción o automatización de decisiones en este curso. |

## Señales extraídas

| ID | Afirmación del documento | Inferencia permitida | Página/sección |
| --- | --- | --- | --- |
| S01 | El ciclo iterativo articula datos, descubrimiento e implementación; empieza con una pregunta de negocio y termina evaluando el resultado. | Un producto predictivo gana valor cuando conserva la conexión entre pregunta, datos, evaluación y uso; no obliga a automatizar la decisión. | pp. 1–3, «El Ciclo de Vida Analítico de SAS». |
| S02 | Una pregunta de negocio debe traducirse a resultado, etiqueta u objetivo definido; la tabla analítica supervisada tiene un registro por entidad y se divide en entrenamiento y prueba. | Son criterios para revisar si el contrato actual hace visible la unidad, el objetivo y la separación de evaluación. | p. 5, pasos 1–2. |
| S03 | Exploración, transformación y selección de variables preceden el modelado; la validación en prueba ayuda a detectar sobreajuste. | Una actividad puede requerir evidencia persistente de qué selección o transformación produjo un estimador, sin añadir una familia de modelos. | pp. 5–6, pasos 3–4. |
| S04 | La precisión y la transparencia pueden entrar en tensión; regresión y árboles pueden ser preferibles cuando se necesita interpretar los factores. | Las comparaciones actuales deben conservar líneas base interpretables; una técnica más compleja no desplaza por sí sola una especificación explicable. | p. 6, «Paso 4: Modele los Datos». |
| S05 | La implementación reutiliza el código de calificación, transformaciones y metadatos; los activos facilitan la gestión de modelos. | En las actividades de producto puede hacerse verificable, con un artefacto ligero, qué modelo y qué contrato de entradas consume el servicio. No implica gobierno o monitoreo empresarial. | pp. 6–7, «Usando SAS Enterprise Miner». |
| S06 | SAS ofrece torneos automáticos, modelos campeones por segmento, ejecución distribuida y automatización de decisiones operativas. | Es una señal de práctica de plataforma, no una razón curricular para añadir AutoML, segmentación masiva, infraestructura Big Data o reglas de decisión automáticas. | pp. 2, 8–10. |

## Contraste con el diseño actual

| Señal | Pxxx | Ancla S01 | Hitos | Superficies | Dictamen | Razón |
| --- | --- | --- | --- | --- | --- |
| S01 — pregunta, ciclo y producto | P200, P204, P205, P216 | Producto predictivo inicial; caso binario educativo; revisión de probabilidades; serie, horizonte y partición | P200 H01–H10; P204 H01–H05; P205 H01–H05; P216 H01–H13 | P200 S01–S04; P204 S01–S03; P205 S01–S03; P216 S01–S04 | ya cubierto | Hay pregunta, datos, evaluación y artefactos persistentes. Las limitaciones de decisión y de procedencia quedan explícitas, por lo que el ciclo de SAS no autoriza ampliarlo a operación real. |
| S02 — objetivo, entidad y partición | P200, P204, P216 | Representación segura; caso binario educativo; serie, horizonte y partición temporal | P200 H01–H06; P204 H01–H04; P216 H01, H13 | P200 S01–S03; P204 S01–S03; P216 S01–S03 | ya cubierto | P200 y P204 separan entrenamiento/prueba y hacen visible el objetivo; P216 preserva la separación cronológica 228/24. Ninguna evidencia del SAS exige reemplazar sus casos. |
| S03 — selección y validación trazables | P219, P221 | Exploración manual/CV/test; selección integrada | P219 H01–H03; P221 H01–H03 | P219 S01–S04; P221 S01–S04 | candidato a cambio | P219 conserva el estimador elegido; P221 selecciona `k` dentro del pipeline y por CV. Sin embargo, P221 declara que no persiste nombres ni resultados de selección: la contribución ya existe en el notebook, pero no queda auditable en el producto entregado. |
| S04 — transparencia frente a complejidad | P200, P204, P216 | Flexibilidad comparada; especificaciones comparables; familias y combinación | P200 H04, H07–H09; P204 H03–H05; P216 H04–H13 | P200 S03; P204 S02–S03; P216 S02–S03 | ya cubierto | Las líneas base se contrastan con alternativas flexibles y se declaran sus límites. Agregar algoritmos del catálogo SAS sería sustitución disciplinar, no mejora evidenciada. |
| S05 — activos reutilizables en una capacidad usable | P217, P218 | Modelo externo; contrato de entrada; esquema de entrada/servicio HTTP | P217 H01–H03; P218 H01–H04 | P217 S01–S04; P218 S01–S04 | candidato a cambio | Ambos talleres hacen usable un predictor, pero registran ausencia de linaje y sus pruebas sólo verifican archivos. Un contrato mínimo modelo–entrada puede hacer verificable la interfaz sin enseñar despliegue empresarial ni añadir monitoreo. |
| S06 — torneos, Big Data y automatización de decisiones | P205, P206, P207, P224, P225 | Revisión de umbrales; agrupamiento; proyecciones y red | P205 H01–H05; P206 H01–H05; P207 H01–H07; P224 H01–H04; P225 H01–H06 | P205 S01–S03; P206 S01–S03; P207 S01–S04; P224 S01–S04; P225 S01–S04 | no sustentado / fuera de alcance | La fuente promociona capacidades de plataforma. No resuelve las tensiones de identidad ya declaradas para talleres no predictivos, ni permite convertir umbrales ilustrativos en política crediticia, ni justifica infraestructura o AutoML. |

## Propuestas candidatas — no aceptadas

### C01 — Persistir la evidencia de selección de entradas de P221

- **Evidencia externa:** `design/benchmarks/professional-learning/sas-data-mining.pdf`, pp. 5–7: preparación, selección de variables, validación y activos con metadatos.
- **Actividad, posición y contrato actual:** P221, ancla «Selección integrada»; H01–H03; S01–S04. El pipeline conserva la selección dentro del ajuste y el estimador serializado, pero el mapa registra que no persiste nombres ni resultado de la selección.
- **Tipo y alcance:** aclaración verificable, con extensión local mínima del artefacto persistente; no se cambia el caso Auto MPG, la secuencia, `SelectKBest`, `f_regression`, `GridSearchCV`, la partición ni la familia lineal.
- **Cambio propuesto:** añadir un artefacto pequeño y legible, por ejemplo `selection_summary.json` o `selection_summary.csv`, que asocie el estimador final con `k`, los nombres de entradas seleccionadas y la métrica de selección disponible. La prueba futura sólo comprobaría esquema, presencia y coherencia básica con el pipeline; no reimplementaría el ajuste.
- **Alternativas de menor impacto descartadas:** (1) **no cambiar** conserva el aprendizaje en el notebook, pero deja sin evidencia persistente la razón técnica de la selección; (2) **explicarlo sólo en texto** no permite verificar que el artefacto cargado conserva esa selección. No se requiere un cambio material ni actividad nueva: el mismo pipeline ya contiene la capacidad.
- **Contrato de no regresión:** conservar H01–H03, S01–S04, `Origin` nominal, selección dentro del pipeline, CV separada de prueba, métricas MSE/MAE/R², `estimator.pkl` y las dependencias actuales. No se reemplaza ningún artefacto ni se introducen paquetes. El resumen nuevo debe coincidir con el estimador persistido; si no puede demostrarse esa coherencia, se conserva el estado actual y se rechaza la propuesta.
- **Producto de Analytics y decisión/usuario:** hace auditable qué entradas sustentan la estimación de MPG y con qué selección; la decisión de flota sigue sin estar evidenciada y no se inventa.
- **Caso, datos y práctica de implementación:** usar el mismo Auto MPG y el `SelectKBest(f_regression)` ya incorporado; extraer los nombres a partir del pipeline ajustado, no duplicar la selección fuera de él.
- **Evidencia de aceptación futura:** `selection_summary.*` en `submission/`, una comprobación proporcional de su esquema/coherencia y revisión de la entrada P221 en `traceability.yaml` antes de aprobar el cambio.
- **Secuencia, riesgos y tensiones:** P221 sigue después de P200/P220 y antes de P222–P223. El resumen no debe convertir una selección asociativa en afirmación causal ni declarar procedencia que el dataset no documenta. La falta actual de trazabilidad de P221 es un requisito de revisión, no una autorización para modificarla en S02.
- **Condición para aceptar:** confirmar institucionalmente que la evidencia persistente de selección es una capacidad verificable esperada del curso y validar que el resumen se deriva del estimador real, no de una lista manual.

### C02 — Hacer verificable el contrato del modelo reutilizado por P217 y P218

- **Evidencia externa:** `design/benchmarks/professional-learning/sas-data-mining.pdf`, pp. 6–7 y 10: reutilización de código de calificación, transformaciones y metadatos entre descubrimiento e implementación.
- **Actividad, posición y contrato actual:** P217, anclas «Contrato de entrada» y «Modelo externo», H01–H03, S01–S04; P218, anclas «Esquema de entrada», «Servicio HTTP» y «Cliente», H01–H04, S01–S04. Ambos conservan siete características y un predictor externo, pero sus mapas declaran que no hay linaje/modelo verificable y que las pruebas son de presencia de archivos.
- **Tipo y alcance:** aclaración verificable compartida entre dos actividades contiguas; no es un ejercicio de MLOps, un rediseño de despliegue ni una extensión hacia monitoreo de producción.
- **Cambio propuesto:** acompañar el predictor reutilizado con un contrato persistente mínimo —por ejemplo, `model_contract.json`— que indique identificador o huella del artefacto, nombres/orden/tipos de las siete entradas, unidad o semántica de la salida y límites de uso conocidos. P217 y P218 deben consumir o comprobar el mismo contrato antes de construir el `DataFrame`; una prueba futura puede verificar el esquema y la coincidencia con la lista de características, sin arrancar un servidor ni entrenar un modelo.
- **Alternativas de menor impacto descartadas:** (1) **no cambiar** mantiene una API y formulario funcionales, pero no permite comprobar que ambos representan el mismo predictor externo; (2) **una nota narrativa** comunica el límite, pero no evita divergencia silenciosa entre la lista de campos, el modelo y el consumidor. Una extensión local del contrato basta; no se justifican gobernanza, autenticación, deriva, latencia ni decisión automática.
- **Contrato de no regresión:** conservar P217 H01–H03, P218 H01–H04, las siete características, validaciones de formulario/Pydantic, rutas GET/POST, `/health`, `/predict`, cliente JSON, modelo `.pkl`, códigos fuente, pruebas existentes y dependencias. No sustituir Flask ni FastAPI, ni cambiar el caso de vivienda. El único añadido es un contrato que debe ser coherente con el modelo y los esquemas existentes; ante incoherencia, se rechaza el cambio en vez de modificar el predictor.
- **Producto de Analytics y decisión/usuario:** fortalece una capacidad analítica usable e interoperable: una persona o proceso recibe la misma estimación bajo un contrato visible. Quién decide y con qué uso sigue siendo «requiere definición»; no se infiere una decisión automática del documento SAS.
- **Caso, datos y práctica de implementación:** conservar el predictor de vivienda externo y sus siete entradas; derivar la información del código/artefacto actual, sin declarar procedencia, desempeño o autorización no evidenciados.
- **Evidencia de aceptación futura:** contrato persistente, comprobación de su esquema y de su coincidencia con `FEATURES`/`HouseFeatures`, y revisión de las entradas faltantes P217 y P218 en `traceability.yaml` antes de aprobar cualquier modificación.
- **Secuencia, riesgos y tensiones:** P217 precede a P218; un solo contrato reduce divergencia entre interfaz humana y API. Riesgo: una huella o metadato manual puede quedar obsoleto; por eso debe derivarse o contrastarse automáticamente. La evidencia SAS recomienda activos de implementación, pero no prueba que este curso deba cubrir monitoreo o gobierno empresarial.
- **Condición para aceptar:** decidir que el contrato reutilizable forma parte de la capacidad de producto de datos de Predictiva y demostrar que no altera las predicciones actuales ni exige dependencias fuera de `requirements.txt` raíz.

## Señales ya cubiertas o descartadas

- **Ya cubiertas:** partición y validación contra sobreajuste (P200 H03, P204 H04, P216 H01/H13, P219 H02); comparación de modelos interpretables y flexibles (P200 H04/H07–H09, P204 H03–H04, P216 H04–H11); persistencia de modelos o pronósticos (P200 H10, P204 H05, P216 H12, P219 H03).
- **Descartada la adición de algoritmos SAS:** la lista de redes, bosques, SVM, boosting, minería textual y asociaciones es un catálogo de producto. No identifica una brecha concreta ni una contribución no duplicada en una actividad de Predictiva.
- **Descartados AutoML, torneos y modelo campeón por segmento:** P219 y P221 ya enseñan selección acotada y verificable; automatizar torneos desplazaría la comparación razonada y no está exigido por esta fuente.
- **Descartadas infraestructura Big Data y plataformas propietarias:** no hay evidencia en los mapas S01 de un problema de escala que requiera Hadoop, procesamiento distribuido o SAS.
- **Descartada la automatización de decisiones:** P205 H03 separa explícitamente el análisis de umbrales de una política real. Convertirlo en regla automática contradice el límite de Analytics y el control humano requerido por `AGENTS.md`.
- **No se propone documentar procedencia de los datasets en esta ejecución:** P200, P216, P219 y P221 registran ese límite, pero el white paper no aporta la procedencia local requerida para corregirlo. Haría falta evidencia del origen de cada caso.

## Auditoría de identidad de Analytics

Las dos candidatas conservan el producto terminal de Analytics: P221 entrega una estimación de MPG con selección reproducible de entradas; P217/P218 entregan una capacidad para solicitar una estimación de precio bajo un contrato verificable. Estadística y ML sirven a la predicción; el contrato de software sirve a hacerla usable. Ninguna candidata transforma el curso en un curso de SAS, Machine Learning, Data Engineering o MLOps.

La tensión principal está en la propia fuente: SAS enlaza predicción con decisiones automáticas y gestión empresarial. En este diseño eso no autoriza una política ni automatización. P205 mantiene costos y grupos como simulación didáctica, mientras P217/P218 no prueban usuario, decisión, procedencia, desempeño, autorización, monitoreo o deriva. Esas fronteras se conservan explícitamente.

## Registro incremental

- Ejecución inicial de S02 para `predictiva`, `benchmark=design/benchmarks/professional-learning/sas-data-mining.pdf`, `executor=codex`.
- Se leyó exclusivamente el PDF local declarado y los mapas S01 de Predictiva pertinentes; no se leyó implementación, otros cursos, síntesis de otros ejecutores, plataformas de aprendizaje ni web.
- Resultado: dos propuestas candidatas no aceptadas (C01 y C02); no se modificó ningún `Pxxx_activity.md`, `Pxxx_log.md`, `implementation/` ni `traceability.yaml`.
