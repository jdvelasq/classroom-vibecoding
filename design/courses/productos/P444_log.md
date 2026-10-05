# Log — P444

## S02.P444.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P444_release_version/` (`VERSION`, `CHANGELOG.md`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/release_manifest.json`, `tests/test_activity.py`, `data/`); contexto de P421, P424, P425, P431, P434.
- **Trazabilidad revisada:** P444 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (capacidad nombrada sin artefacto, caso y datos como límite), H02 (fuente única de versión).
- **Ambigüedades:** no se libera ningún artefacto; el indicador de riesgo sólo se nombra; no se valida coherencia `VERSION`/`CHANGELOG.md`.
- **Superficies / contrato / dependencias:** S01–S05; sin dependencias demostrables.
- **Auditoría de Analytics:** no resuelta; riesgo de versionado genérico de software.

## S03.P444.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - cuerpo de conocimiento por competencias (conocimiento + habilidades + disposiciones, niveles T1/T2/E) para pregrados en ciencia de datos. Las competencias operativas (calidad, integridad, privacidad, pruebas, ciclo de vida, automatización auditable) aparecen como principios generales, sin desarrollar MLOps ni operación de productos de datos. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.
