# Log — P314

## S02.P314.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P314_storm_response_crews/` (`data/` dos CSV, `professor/notebook.ipynb`, `submission/` seis artefactos, `tests/test_activity.py`; notebook de estudiante sin celdas).
- **Trazabilidad revisada:** P314 → `prescriptiva.C02`, `C03`, `C04`, `C05`. Sostenidas; C05 declarativa.
- **Highlights añadidos:** H01–H06 (recurso derivado del orden de costos; valor de la flexibilidad; criterio robusto con desempate; acciones por escenario; sensibilidad esperado vs. robusto; autoridad por etapa).
- **Ambigüedades:** la elección del criterio robusto (x=16) sobre el esperado (x=12) no se justifica en un artefacto persistido; ahorro y prima sólo en notebook. La prueba acepta cualquier archivo. Referencias heredadas «W12/W13». Garantía de cero interrupción depende de cuatro escenarios y de clasificación perfecta.
- **Superficies / contrato / dependencias:** S01–S06; recibe la pregunta de P313 (por contenido) y práctica de P309; habilitación no evidenciada.
- **Auditoría de Analytics:** producto = política de reserva y despliegue con autoridad, plazo, guarda y escalamiento. La formulación de dos etapas sirve a la política; identidad preservada.

## S03.P314.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
