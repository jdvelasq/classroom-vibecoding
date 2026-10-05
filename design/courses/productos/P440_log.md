# Log — P440

## S02.P440.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P440_data_reconciliation/` (`data/source.json`, `data/target.json`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/reconciliation.json`, `tests/test_activity.py`); P402 y P417 para relación.
- **Trazabilidad revisada:** P440 → `productos.C02`, `productos.C03`, `productos.C05`.
- **Highlights:** añadidos H01 (total de control; caso y datos), H02 (veredicto agregado).
- **Ambigüedades:** métricas declaradas, no calculadas; medida `amount` ajena a los casos del curso; sin tolerancia ni localización de la diferencia; sin `HOW_TO_RUN_ME.txt`.
- **Superficies/contrato/dependencias:** S01–S05; recibe práctica de P402; habilita no evidenciada.
- **Auditoría de Analytics:** riesgo de identidad (pregunta 5): control genérico sin capacidad analítica.

## S03.P440.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P440.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - Dominio III, Task 3.5 «Clean, harmonize, transform, merge/join, and validate data» y 3.6 «Assess data quality» (p. 5) — ya cubierta: contrato y compuerta de aceptación (P402 H01–H04), conciliación (P440 H01–H02), cuarentena (P441 H01). La limpieza en sí pertenece a Fundamentos o Descriptiva.
  - Task 6.6 «Actively support deployment validation and verification, including production data flows» (p. 7) — ya cubierta: verificación del artefacto publicado de extremo a extremo (P417 H01) y conciliación origen-destino antes de publicar (P440 H02).

## S03.P440.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «deployment validation and verification, including production data flows» (p. 23, Tarea 6.6) — subtarea no evaluada; ya cubierta por la verificación del artefacto publicado (P417 H01) y la conciliación origen–destino (P440 H01–H02).
