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
La suite existente aprobó 56 pruebas. P405 requiere primero ejecutar
`professor/main.py`, pues su prueba comprueba el log persistente y, por diseño,
no ejecuta el código del profesor.

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

P408–P411 y P415–P416 no contienen una solución Python bajo `professor/`: son
talleres guiados de Git y automatización cuya solución ocurre en un repositorio
temporal y deja evidencia en `submission/`. P433 ejecuta un proyecto dbt y
conserva sus artefactos de herramienta en la raíz de la actividad. Las siete
actividades tienen `HOW_TO_RUN_ME.txt`; por tanto, son excepciones justificadas
al patrón de solución Python, no faltantes de material del profesor.

P426 conserva un `requirements.txt` local porque su Dockerfile lo necesita en
el contexto de construcción de la actividad. Es un artefacto de ejecución, no
una segunda fuente de verdad: declara únicamente `flask==3.1.3`, compatible
con el límite `flask<3.2` del `requirements.txt` canónico de la raíz.

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
