# Log — P316

## S02.P316.01

- **Fecha:** 2026-10-04; **curso / executor:** `prescriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/prescriptiva/P316_humanitarian_food_aid/` (`data/suppliers.csv`, `data/destinations.csv`, `data/transport.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb` sin celdas, cinco artefactos de `submission/`, `tests/test_activity.py`); para relaciones, P305, P308, P313–P315 y P317–P318. Contexto de diseño: `activity-architecture.md`, `s05-diseno-prescriptiva.md`, `audit-against-design.md`.
- **Trazabilidad revisada:** P316 → `prescriptiva.C02`, `C03`, `C04`, `C05`. C02 y C04 sustentadas; C03 parcial (líneas base y sensibilidad de un parámetro, sin incertidumbre); C05 parcial (monitoreo sin umbrales).
- **Highlights:** añadidos H01–H08. H01 es el highlight obligatorio de caso y datos (red con holgura global 670/550 t y escasez local de S1; matrices filas = proveedores, columnas = destinos). Cifras citadas sólo de `plan_comparison.csv`, `shipment_plan.csv`, `supplier_utilization.csv` y de los datos; penalizaciones y sensibilidad de S1 se describen sin valores por no persistirse.
- **Ambigüedades:** (1) los comentarios «W04–W06» y «W07» usan una numeración heredada que no coincide con P300–P322 (P313/P314 se llaman W12/W13), lo que sugiere que P316 precedía a P313–P315 en el orden original; (2) la guarda «un destino no alcanza 100 %» no puede activarse en el plan porque la demanda es restricción de igualdad, y no hay datos de ejecución; (3) las guardas escalan a una «asignación de escasez» y «priorización por necesidad» no implementadas; (4) el cumplimiento por destino se calcula pero no se persiste; (5) no se discute unicidad del óptimo.
- **Superficies / contrato / dependencias:** S01–S09 declaradas. Pruebas verifican existencia de plan y contrato y campos no vacíos, no cálculos. Recibe el patrón de P305/P308/P315; habilita la práctica de LP continuo sin enumeración reutilizada en P318. Sin artefactos compartidos.
- **Auditoría de Analytics:** el producto terminal es una política de abastecimiento-distribución con recomendación, aprobación humana, bloqueo y gatillos; el LP aporta factibilidad y validación. Auditoría resuelta con el límite de que monitoreo y escasez quedan declarados, no operados.
- **Cambios de IDs:** ninguno (pasada inicial). No se creó la sección «Mejoras aceptadas pendientes de implementación».

## S03.P316.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Algorithms for combinatorial optimization problems», «Use common algorithms … (e.g., Branch and Bound algorithms)», max-flow, «Heuristic optimization techniques» y «Implement Dynamic Programming solutions» (PDA-Algorithms, pp. 115–116). Categoría: ya cubierta en el uso (mochila P305 H03, asignación P308 H04, localización P315 H03, flujo LP P316 H05, heurísticas como línea base P316 H03). Implementar B&B o DP es fuera de alcance: `s05-diseno-prescriptiva.md` excluye la implementación de solvers.

## S03.P316.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco de práctica de INFORMS (base del CAP) con siete dominios y sus tareas, desde el encuadre del problema de negocio hasta el despliegue y la gestión del ciclo de vida de la solución analítica. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.

## S03.P316.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - desagrega cada tarea del INFORMS Analytics Framework en objetivos evaluables del examen CAP-E, con pesos por dominio (despliegue 9 %, ciclo de vida 8 %); incluye subtareas específicas para modelos prescriptivos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P300_log.md`.
