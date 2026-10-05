# Log — P125

## S02.P125.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P125_salarios/` (`data/salarios.csv`, `professor/generate_data.py`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con cinco archivos, `tests/`); P103/P104, P108/P109 y P120–P124 como comparación.
- **Trazabilidad revisada:** P125 → `descriptiva.C01`–`C05`; coherente. Es la única evidencia persistida y probada de C04 en P120–P125.
- **Highlights añadidos:** H01–H07 (población sintética de mecanismo conocido, pares comparables, estadísticos robustos, señalamiento con doble criterio, decil superior, límite causal persistido, agregados sin divulgación). Highlight obligatorio de caso y datos: H01.
- **Cambios realizados:** creación de `P125_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** el notebook no declara que los datos son sintéticos; las áreas señaladas coinciden con los ajustes negativos del generador sin que el taller lo use para discutir C04; la mediana de pares incluye al individuo y no se reporta el tamaño de los grupos; umbrales −5 %, 50 % y P90 sin justificación; la respuesta «No» a la segunda pregunta demuestra posibilidad, no igualdad de acceso; `technical_high_salary` no se persiste; las alternativas de texto fijo rozan lo prescriptivo; la redacción de la primera pregunta difiere ligeramente entre `questions.json` y la celda del notebook; carpeta `.pytest_cache/` presente.
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S05 declaradas; dependencias demostrables de P103/P104 y P120–P122 (prácticas), conceptual con P108/P109; salida no evidenciada.
- **Auditoría de Analytics:** diagnóstico de brechas con frontera causal explícita; responde qué ocurre, dónde y con qué evidencia. Las disciplinas contribuyentes sirven al producto.

## S03.P125.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - tipos de medida nominal/ordinal/intervalo/razón (DM-Proximity, p. 76) — marginal: la elección de mediana y percentiles ya está justificada en P125 H03.

## S03.P125.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 5.6 «Document and communicate model findings, including assumptions, limitations, and constraints» (p. 6) — ya cubierta en su forma descriptiva: P125 H06; extenderlo a otros talleres no se sostiene con esta señal genérica.
