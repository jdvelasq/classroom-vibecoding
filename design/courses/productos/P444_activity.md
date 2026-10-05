# P444 — Liberación versionada: manifiesto del indicador de riesgo por fábrica

## Actividad actual implementada

**Implementación:** `implementation/productos/P444_release_version/`.

### Preguntas analíticas actuales

- ¿Qué versión de la capacidad recibió el consumidor y dónde están documentados sus cambios?

La raíz de la actividad contiene `VERSION` (`1.0.0`) y `CHANGELOG.md` con una sola entrada: «Primera liberación del indicador de riesgo por fábrica». `professor/main.py` lee `VERSION` y escribe `submission/release_manifest.json` con `product: factory-risk-indicator`, la versión y `release_notes: CHANGELOG.md`. `data/` sólo tiene `.gitkeep`: no se libera ningún artefacto (tabla, regla, modelo o servicio) ni se registra su huella. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** identificar qué capacidad recibió el consumidor (docstring de `build_release_manifest`); consumidor no identificado.
- **Producto terminal:** manifiesto de liberación con nombre de producto, versión y puntero a notas.
- **Uso y límite:** permite relacionar una entrega con su número de versión y su registro de cambios. No vincula la versión con ningún artefacto ni contenido; no verifica que `CHANGELOG.md` contenga la versión declarada ni que la versión siga un esquema.
- **Disciplinas contribuyentes:** gestión de liberaciones de ingeniería de software al servicio de identificar la versión del indicador de riesgo.

### Highlights de contribución

- **H01 — Nombra la capacidad liberada sin empaquetarla (caso y datos):** el único vínculo con un producto analítico es el nombre `factory-risk-indicator` y la línea del changelog. El indicador de riesgo por fábrica aparece antes como regla de umbral (`high` si `daily_units_produced < 4500`) en P425/P426, pero P444 no la referencia ni incluye artefacto alguno. La particularidad del caso queda reducida a una etiqueta; se registra esa ausencia como límite. Sin este hito, la versión del curso seguiría refiriéndose a modelos (P421, P424) o contratos (P434), no al producto entregado.
- **H02 — Separa la versión declarada del manifiesto entregado:** la versión vive en un archivo de texto (`VERSION`) y el manifiesto se genera a partir de él; la prueba de profesor inyecta `2.1.0` y exige el manifiesto completo. `tests/test_activity.py` sólo exige su existencia. Sin este hito no habría una fuente única de versión del producto.

### Inventario técnico de implementación

- **Introduce:** archivo `VERSION`, `CHANGELOG.md` y manifiesto de liberación.
- **Contrasta:** versionado de producto frente a versión de modelo (P421, P424), de datos (P431) y de contrato (P434).
- **Reutiliza:** patrón función pura + persistencia JSON en `submission/`.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Identidad del producto liberado | H01 | `product: factory-risk-indicator` | Sin artefacto ni huella asociados. |
| Fuente única de versión | H02 | `VERSION` → manifiesto | Sin validación de esquema ni de coherencia con el changelog. |

### Relación técnica con actividades anteriores

Nueva unidad de versionado (producto) frente a modelo (P421, P424), datos (P431) y contrato (P434), sin consumir artefactos de ellas. El nombre del producto anticipa el reporte de riesgo de P450–P452 y el registro `factory-risk` de P448, pero ninguna de esas actividades lee este manifiesto.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Capacidad nombrada | S01, S03 | `implementation/productos/P444_release_version/CHANGELOG.md`; `implementation/productos/P444_release_version/submission/release_manifest.json`; `implementation/productos/P425_api_contract/professor/main.py`: `classify_risk` | El vínculo con la regla de P425 es de nombre, no de artefacto. |
| H02 — Fuente única de versión | S01, S02, S04 | `implementation/productos/P444_release_version/VERSION`; `implementation/productos/P444_release_version/professor/main.py`; `implementation/productos/P444_release_version/professor/test_main.py` | No se valida el formato ni el changelog. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Metadatos de liberación | `VERSION`; `CHANGELOG.md` | Una versión; una entrada. |
| S02 | Construcción del manifiesto | `professor/main.py` | Nombre de producto fijo en el código. |
| S03 | Manifiesto entregado | `submission/release_manifest.json` | Sin artefacto ni huella. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: forma del manifiesto; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** lee `VERSION` y construye el manifiesto.
- **`submission/`:** `release_manifest.json`.
- **Pruebas:** la de profesor verifica el diccionario completo para una versión inyectada; `test_01` verifica existencia. Ninguna compara manifiesto y changelog.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de Pxxx:** ninguna demostrable; el nombre del indicador remite al caso de P425/P426.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P444 mapea `productos.C02` (entrega confiable) y `productos.C05`. C02 se sostiene parcialmente: hay versión de producto pero no integración con el artefacto entregado. Auditoría pregunta 5: sin artefacto liberado, la actividad puede leerse como práctica genérica de versionado de software; el producto analítico es sólo nombrado.
