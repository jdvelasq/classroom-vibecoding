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

## Separación entre solución y plantilla

La auditoría de contenido de archivos confirmó que cada `src/main.py` restante
es una plantilla: contiene una señal explícita de implementación pendiente.
Las ocho soluciones completas que permanecían en `src/` —P412–P414, P418 y
P426–P429— se trasladaron intactas a `professor/main.py`; sus nuevas plantillas
no contienen lógica resuelta.

P402–P404 tenían simultáneamente plantilla Python y notebooks vacíos. Por su
naturaleza de pruebas automatizadas y su contrato de evaluación, se preservó
la modalidad Python y se retiraron únicamente los notebooks vacíos. No queda
ninguna actividad P4xx con dos modalidades de resolución para estudiantes.

## Resultado

**Conforme para estructura canónica y separación profesor/estudiante.** Las
futuras auditorías de Productos pueden concentrarse en diseño de actividades,
trazabilidad curricular, artefactos de raíz y distribución, sin arrastrar el
esquema heredado.

## Registro

- Fecha: 2026-10-01.
- Alcance limitado deliberadamente a estructura.
- Evidencia: inventario P400–P455, comprobación de carpetas y ausencia de
  `scripts/`/`README.md`, y ejecución de `pytest`.
