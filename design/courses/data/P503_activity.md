# P503 — Modelo relacional de Scopus

## Actividad actual implementada

**Implementación:** `implementation/data/P503_scopus_relacional/`.

### Preguntas analíticas actuales

- ¿Cómo se estructura la producción científica sobre proptech por año, autores
  y fuentes?
- ¿Qué autores tienen más documentos en el resultado?
- ¿Qué revistas y conferencias concentran más documentos?

Parte de `data/scopus.csv.gz` y de la cadena de
búsqueda preservada. Entrega una base `scopus_proptech.db` y tres respuestas:
documentos por año, autores por documentos y fuentes por documentos.

La actividad está diseñada para hacer observable la transformación de un
extracto bibliográfico hacia una representación relacional que permite
responder preguntas agregadas. Los notebooks de profesor y estudiante existen,
pero el mapeo actual no infiere su secuencia sin evidencia textual adicional.

### Inventario técnico de implementación

- **Introduce:** transformación de un extracto bibliográfico comprimido a una
  base SQLite para consultas sobre años, autores y fuentes.
- **Introduce:** separación de tres salidas agregadas y almacenamiento de la
  base relacional como entrega.

### Relación técnica con actividades anteriores

Introduce un dominio y representación distintos de Superstore. Sin P503 se
pierde el puente desde un CSV bibliográfico a un caso relacional reutilizable
por la secuencia SQL P504–P508.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

| Afirmación | Evidencia | Tipo | Límite |
| --- | --- | --- | --- |
| Preguntas y respuestas | `submission/questions.json`, CSV de `submission/` | explícita | No se extrajo la procedencia de Scopus más allá del archivo local. |
| Base relacional | `submission/scopus_proptech.db` | estructural | Requiere lectura detallada posterior de los notebooks para documentar la secuencia. |
| Capacidades `data.C01`–`data.C05` | `traceability.yaml` | explícita | Alineación pendiente de auditoría. |

## Auditoría de Analytics

El modelo relacional funciona como medio para explorar evidencia bibliográfica
con preguntas concretas; no se presenta como formación autónoma en bases de
datos.
