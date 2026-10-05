# Log — P122

## S02.P122.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P122_supply_chain/` (`data/supply_chain.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` vacío, `submission/` con `questions.json` y ocho CSV, `tests/`); P106, P120 y P121 como comparación.
- **Trazabilidad revisada:** P122 → `descriptiva.C01`, `C02`, `C03`; coherente. La declaración de cobertura de flete roza C05, no mapeada.
- **Highlights añadidos:** H01–H07 (grano y calidad, KPI desde fechas, proporción vs promedio, valor expuesto, cobertura de flete, umbrales por nivel, persistencia y pruebas). Highlights obligatorios de caso y datos: H02 y H05.
- **Cambios realizados:** creación de `P122_activity.md`; sin cambios en implementación ni propuestas.
- **Ambigüedades:** procedencia y licencia del dataset no documentadas (insumos de salud por país); el comentario mensual promete controlar «cambio de mezcla» pero el código no lo hace; serie mensual sin volumen mínimo; umbrales 50/20/30 sin justificación; el contraste proporción–promedio (H03) es observable pero no comentado; pruebas más laxas que en P120/P121 y sin verificación de `questions.json`; `priority_segments.csv` se guarda sin el ordenamiento que se muestra.
- **Cambios de IDs:** ninguno.
- **Superficies, contrato y dependencias:** S01–S06 declaradas; dependencias demostrables de P120/P121 (plantilla) y P106 (conversión de tipos); salida no evidenciada.
- **Auditoría de Analytics:** diagnóstico de cumplimiento y valor expuesto con límite de cobertura explícito; disciplinas al servicio del producto. Sin declaración explícita de límite causal.

## S03.P122.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - *scores* y *rankings* con características deseables (DM-Proximity, p. 75) — ya cubierta: umbrales de volumen y separación entre riesgo y prioridad (P120 H06–H07, P121 H05, P122 H04/H06).

## S03.P122.02

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Task 3.6 «Assess data quality and identify relationships in the data» (p. 5) — ya cubierta: P120 H02, P121 H02, P122 H01, H05.
  - Task 3.8 «Validate and update the business and analytics problem statements» (p. 5) — ya cubierta: P122 H05.
