# Auditoría estructural: Productos de datos

## Alcance

Esta auditoría revisa únicamente el contrato canónico de estructura de las
actividades P4xx. No evalúa ni modifica código, datos, pruebas, lógica,
resultados pedagógicos ni cobertura curricular.

## Inventario

- Actividades auditadas: `P400_*`–`P455_*`.
- Total: 56 actividades.

## Contrato comprobado

Cada actividad tiene estas carpetas:

- `data/`
- `notebooks/`
- `professor/`
- `src/`
- `submission/`
- `temp/`
- `tests/`

Además, no queda ningún directorio `scripts/` ni archivo `README.md` dentro
de las actividades P4xx.

La excepción inicial de P442 se normalizó trasladando la solución heredada de
`scripts/` a `professor/`. El README heredado de P408 fue retirado conforme al
contrato Pxxx. No se cambió código, datos, pruebas ni lógica de actividad.

## Verificación

La comprobación estructural de las 56 actividades registró cero violaciones.
La suite existente se ejecutó sobre todas las actividades P4xx y aprobó 56
pruebas.

## Resultado

**Conforme para estructura canónica.** Las futuras auditorías de Productos
pueden concentrarse en diseño de actividades, trazabilidad curricular,
artefactos de raíz y distribución, sin arrastrar el esquema heredado.

## Registro

- Fecha: 2026-10-01.
- Alcance limitado deliberadamente a estructura.
- Evidencia: inventario P400–P455, comprobación de carpetas y ausencia de
  `scripts/`/`README.md`, y ejecución de `pytest`.
