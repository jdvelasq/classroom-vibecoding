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
