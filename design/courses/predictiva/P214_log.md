# Log — P214

## S01.P214.01

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `ChatGPT`; **estado:** inicial.
- **Decisión:** se preservó la validación retenida y el límite causal de reglas
  de asociación en la descripción de la actividad.

## S01.P214.02

- **Fecha:** 2026-10-03; **curso / executor:** `predictiva` / `Codex`; **estado:** incremental.
- **Decisión:** se añadieron producto, highlights, anclas, superficies y contrato de evidencia para permitir contraste posterior sin reabrir implementación.
- **Auditoría Analytics:** se preservó asociación como producto predictivo condicional y se excluyó causalidad comercial.

## S03.P214.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/institutional/mit-data-science-and-machine-learning.md` (`source_sha256`: 64a07fe95cbf5c9c31aef4843b358ca9a478663579119d36db7dc95540f2a1e3).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - el folleto no trata reglas de asociación; la recomendación se revisó en P215.

## S03.P214.02

- **Fecha / executor:** 2026-10-04 / OpenWork.
- **Documento:** `design/benchmarks-md/institutional/berkeley-ai-business-strategy-applications.md` (`source_sha256`: 8a008ed5eeb167fdb5a0127c583dab9d82c2c8682d4aade665bfaebb64384fbb).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - personalización de experiencia del cliente (p. 2): ya cubierta como forma general de uso por la recomendación condicional de ítems (H03–H04); reemplazar la canasta didáctica por otra aplicación no suma una capacidad distinta ni mejora su validación retenida.
- **Corrección (2026-10-04 / Claude):** hash corregido: se había registrado el hash del archivo `.md` en lugar del `source_sha256` de su cabecera.
