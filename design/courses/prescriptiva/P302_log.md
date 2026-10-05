# Log — P302

## S02.P302.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P302_politica_desde_evidencia_y_restricciones/` (`data/policy_options.csv`, `data/source.json`, `professor/main.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, `src/` vacío, tres artefactos de `submission/`, `tests/test_activity.py`); relación con P300.
- **Trazabilidad revisada:** P302 → `prescriptiva.C01`, `C02`, `C04`; C02 débil (menú de tres repartos fijos).
- **Highlights:** añadidos H01–H05 (razón de descarte; piso activo sin cambiar la elección; procedencia en el producto; contrato JSON; excepción sin factibles).
- **Ambigüedades:** (1) las tres alternativas son factibles: la razón «no cumple capacidad o mínimo» y el `ValueError` nunca se ejercitan; (2) la alternativa ganadora, «solo_mayor_beneficio», está en el piso, mientras «prioridad_con_piso» se descarta por valor, lo que puede confundir la intención del producto previsto («asignación con garantía mínima»); (3) el gatillo usa asistencia por grado, ausente del caso; (4) la capacidad exige igualdad, no límite superior; (5) mecanismo de decisión casi idéntico al de P300: posible duplicación técnica.
- **Superficies / contrato / dependencias:** S01–S04; pruebas de existencia; recibe de P300; el formato `policy_contract.json` reaparece en actividades posteriores.
- **Auditoría de Analytics:** recomendación gobernada con procedencia declarada; acción factible, autoridad, cadencia y gatillo presentes; sin conexión entre contexto observable por entidad y acción ni monitoreo ejecutado.

## S03.P302.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de competencias de computación para el pregrado en ciencia de datos, organizado en 11 áreas de conocimiento con niveles T1/T2/E. Optimización, simulación y decisión secuencial aparecen sólo como técnicas sueltas (PDA, AI). Ética, sesgo, automatización auditable y comunicación con quien decide sí son expectativas transversales (PR, cap. 6–7). Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
