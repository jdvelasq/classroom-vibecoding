# Log — P300

## S02.P300.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P300_encuadre_analitico_de_decisiones/` (`data/policy_options.csv`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` con sólo `.gitkeep`, `submission/decision_brief.csv`, `submission/policy_contract.csv`, `tests/test_activity.py`); contexto de diseño en `s05-diseno-prescriptiva.md`, `activity-architecture.md` y `audit-against-design.md`.
- **Trazabilidad revisada:** P300 → `prescriptiva.C01`, `C04`; ambas sustentadas.
- **Highlights:** añadidos H01–H04 (factibilidad antes que objetivo; restricciones que cambian la acción en un menú agregado; contrato de política; prueba del contrato). Ninguno corregido ni descartado.
- **Ambigüedades:** (1) el notebook importa `main` desde `src/`, que sólo contiene `.gitkeep`; `main.py` está en `professor/`, por lo que la ejecución del notebook tal como está no queda demostrada; (2) procedencia del dataset no documentada y segmentos «probabilidad alta/media» sin definición; (3) la tabla de evaluación de las cuatro alternativas no se persiste; (4) la política es una elección entre cuatro alternativas preagregadas, no una regla por cliente.
- **Superficies / contrato / dependencias:** S01–S05 declaradas; contrato de evidencia separa código, dos CSV y pruebas de columnas; habilita el patrón de P302 y P307; no recibe de actividades previas.
- **Auditoría de Analytics:** producto prescriptivo parcial: acción factible con restricciones, salvaguarda, autoridad humana, cadencia y gatillo de revisión declarados; no hay registro de decisiones ni monitoreo ejecutado. La identidad de Analytics se preserva; no se reduce a un ejercicio de optimización.

## S03.P300.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - presentar datos, modelos e inferencias a clientes, «Knowing the audience», dashboards (AP, pp. 43–45). Categoría: ya cubierta por los planeadores persistidos (P304, P305, P309, P313, P316–P318). User-centred design, Interaction e Interface design (pp. 45–47) son fuera de alcance (Productos de datos).
  - «It is important for data science education to incorporate real data used in an appropriate context» (cap. 4.2, p. 29). Categoría: marginal. Es una expectativa general que `AGENTS.md` ya fija como regla de procedencia, y muchos Pxxx declaran casos sintéticos justificados por control experimental. El documento no aporta ningún caso ni dato concreto que permita sustituirlos.
  - privacidad y GDPR, «Apply techniques to provide data privacy … such as provide ranges or salting» (PR-Privacy, pp. 106–107; DPSIA/DP-Social Responsibility, p. 83). Categoría: fuera de alcance (Fundamentos de data / Productos de datos).
  - el currículo INFORMS 2015 incluye un curso de «Prescriptive Analytics» (p. 15). Categoría: marginal. Es una mención de contexto, sin contenidos.

## S03.P300.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta.
- **Señales de alcance de curso** (registradas sólo en este log):
  - Task 4.1–4.2 selección de métodos según el problema (p. 6) — ya cubierta: P306 H03, P316 H05, P317 H04 y P319 H03 justifican el método por la estructura del problema.
  - Task 5.3 «Run, verify, and evaluate the model performance and outputs» (p. 6) — ya cubierta: verificación cruzada enumeración/solver (P305 H03, P308 H04, P315 H03), validación independiente del LP (P316 H06) y validación analítica (P317 H05).
  - Task 2.5 «Identify baseline performance of the current state» (p. 5) — ya cubierta: líneas base operativas en P304 H04 (aceptar todo), P305 H02, P313 H05, P316 H03 y P318 H02.
  - Task 2.3 y 5.6 supuestos, limitaciones y restricciones documentados (pp. 5–6) — ya cubierta: `data_limitation` de P302 H03 y los contratos de P304–P319.
  - Domain III Data (p. 5: limpieza, armonización, plan de gestión de datos) — fuera de alcance: pertenece a Fundamentos de data / Productos de datos; los talleres prescriptivos reciben datos preparados.
  - Domain VI Deployment, tareas 6.4–6.6 (requisitos de producción, pruebas, flujos de datos de producción; p. 7) — fuera de alcance: frontera con Productos de datos fijada en `s05-diseno-prescriptiva.md`.
  - Task 6.1–6.2 validación de negocio e informe (p. 7) — marginal: los contratos de política con autoridad y aprobación ya cumplen esa función; un informe adicional no cambia lo que el estudiante hace.
  - Task 1.2 y 2.7 identificación de partes interesadas y acuerdo del patrocinador (pp. 4–5) — ya cubierta: autoridades y escalamientos declarados desde P300 H03 y P303 H01.
