# P511 — Integración Superstore

## Actividad actual implementada

**Implementación:** `implementation/data/P511_superstore_integracion/`.

### Preguntas analíticas actuales

- ¿Qué segmentos, regiones y categorías concentran las ventas y la utilidad de Superstore?

Integra órdenes, clientes, productos y líneas de pedido derivados del extracto
Superstore. El manifiesto declara una fila por línea de orden y claves de
contexto sustitutas; la salida conserva detalle enriquecido y un agregado por
segmento, región y categoría.

### Inventario técnico de implementación

- **Introduce:** `merge` many-to-one validado sobre cuatro fuentes.
- **Introduce:** preservación del grano y comprobaciones de cardinalidad y no
  nulidad tras la integración.
- **Extiende:** agregación de ventas y utilidad sobre datos integrados.

### Relación técnica con actividades anteriores

La pregunta se parece a P500, pero añade integración validada. Sin P511 se
pierde la habilidad de enriquecer datos sin alterar el grano.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y límites

La pregunta, el manifiesto, los notebooks de profesor y los CSV de `submission/`
sustentan el mapa. `traceability.yaml` asigna `data.C01`–`data.C05` y requiere
auditoría posterior. La actividad diseña evidencia de integración; no prueba
logro real del estudiante.

## Auditoría de Analytics

Las uniones sirven una respuesta comercial y no se presentan como fin de
ingeniería de datos independiente.
