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
