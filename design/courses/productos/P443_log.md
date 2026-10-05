# Log — P443

## S02.P443.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P443_data_lineage/` (`data/raw_operations.csv`, `professor/main.py`, `professor/test_main.py`, `requirements.txt`, `src/main.py`, `submission/factory_totals.csv`, `submission/lineage.json`, `tests/test_activity.py`); `P431_data_versioning/submission/data_manifest.json`; agregados de P412, P417, P428, P432.
- **Trazabilidad revisada:** P443 → `productos.C02`, `productos.C05`.
- **Highlights:** añadidos H01 (cambio de grano, caso y datos), H02 (huella del insumo), H03 (lo que se prueba).
- **Ambigüedades:** el linaje no registra la transformación pese al docstring; `created_at` no determinista; `requirements.txt` local no listado como excepción en `structure-audit.md`; quinta repetición del agregado por fábrica; posible solapamiento con el linaje de dbt en P433.
- **Superficies / contrato / dependencias:** S01–S05; recibe insumo demostrable de P431 (SHA-256 idéntico); habilitación no evidenciada.
- **Auditoría de Analytics:** resuelta con límite; el linaje sirve a un agregado descriptivo del caso de fábricas.

## S03.P443.01

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - DPSIA/DI-Methods (p. 91: «Role of hash algorithms in integrity preservation»; «Data provenance assurance», p. 91) — ya cubierta al nivel que el documento pide («explain»): P431 H01 identifica la versión por contenido; P443 H02 ancla la salida a la huella del insumo; P448 H02 verifica restauración por bytes. La falta de función de verificación en P431 es un límite S02, no una señal nueva de este documento.

## S03.P443.02

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` (`source_sha256`: c68ebf677366244eb2d1e673108e6cd923b37fd2990ca29b92abf885c2670117).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - marco CAP de INFORMS que describe, por análisis de tareas profesionales, siete dominios del ciclo de vida analítico, desde el encuadre del problema de negocio hasta el despliegue y la gestión continua de la solución. Como fuente authoritative, respalda expectativas generales (validación de negocio antes de desplegar, requisitos de la solución desplegada, seguimiento del valor en el tiempo), no un temario. Para esta actividad no añade una señal distinta. Las señales de alcance de curso de este documento se registran en `P400_log.md`.

## S03.P443.03

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-essentials-blueprint.md` (`source_sha256`: af729216b134cb7dcbe8d2c0b64670b7f762408c5b2ff0d2fb0b9f959b77da70).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - «Identify characteristics of lineage, traceability, and version control of data» (p. 15, CAP-E.3.4.3) — ya cubierta: P431 H01 (identidad por contenido), P443 H02 (linaje entrada→salida).

## S03.P443.04

- **Fecha / executor:** 2026-10-05 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/informs-cap-pro-blueprint.md` (`source_sha256`: 2bcd076439f1a714f08239345cd0870b6ac04fdd565c90958c03a217b8be8eb0).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - CAP-P.3.4.3 «Identify the purpose of lineage, traceability, and version control of data» (p. 15) — ya cubierta: huella de datos (P431 H01), linaje del agregado (P443 H02), versión de la definición (P408 H01–H02).
