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
