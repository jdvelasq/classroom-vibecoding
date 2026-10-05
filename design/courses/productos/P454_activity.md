# P454 — Catálogo de datos: ficha operacional del dataset de riesgo por fábrica

## Actividad actual implementada

**Implementación:** `implementation/productos/P454_data_catalog/`.

### Preguntas analíticas actuales

- ¿Quién responde por el dataset de riesgo por fábrica, con qué frecuencia se produce, bajo qué versión de contrato y para qué consumidor?

`data/catalog.json` es una ficha única: `dataset: factory_risk`, descripción «Riesgo operativo por fábrica», `owner: data-operations`, `frequency: daily`, `contract_version: 2.0`, `consumer: operations_manager`. `professor/main.py` (`load_catalog_entry`) la lee y `main()` la copia sin transformación a `submission/catalog_entry.json`. No hay esquema, linaje, ubicación ni búsqueda. El estudiante recibe `src/main.py` vacío, sin `HOW_TO_RUN_ME.txt` ni notebook.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** aclarar responsabilidad y uso antes de operar el dato (docstring); consumidor declarado: `operations_manager`.
- **Producto terminal:** ficha de catálogo del dataset de riesgo.
- **Uso y límite:** permite saber quién responde, cada cuánto y bajo qué contrato se consume el dataset. Es una copia de un archivo escrito a mano; no se verifica contra el dataset, el contrato ni el linaje reales.
- **Disciplinas contribuyentes:** gobierno de datos al servicio de la responsabilidad sobre el indicador de riesgo.

### Highlights de contribución

- **H01 — Reúne en una ficha elementos operativos dispersos del caso (caso y datos):** la ficha nombra el dataset del indicador de riesgo por fábrica y repite valores que aparecen en actividades previas: `contract_version` 2.0 coincide con `P434_contract_versioning/data/contract.json`, el dueño `data-operations` con el responsable de incidentes de P447 y el consumidor `operations_manager` con el rol autorizado de P452. Esa coincidencia se declara a mano, no se lee de los artefactos. Sin este hito, dueño, contrato y consumidor del producto quedarían dispersos entre talleres.
- **H02 — Prueba el contenido real de la ficha:** a diferencia de la mayoría de pruebas de profesor del bloque, `test_load_catalog_entry_exposes_operational_responsibility_and_use` lee el `data/catalog.json` distribuido y exige cinco valores (dataset, dueño, consumidor, frecuencia, versión de contrato). Funciona como prueba del contenido del catálogo, no de una transformación, porque no la hay. `tests/test_activity.py` sólo exige el archivo copiado. Sin este hito, los campos de responsabilidad no estarían protegidos.

### Inventario técnico de implementación

- **Introduce:** ficha de catálogo con dueño, frecuencia, versión de contrato y consumidor.
- **Reutiliza:** valores de P434 (versión de contrato), P447 (dueño) y P452 (rol consumidor), como texto.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Ficha operacional | H01 | Dueño, frecuencia, contrato, consumidor | Valores escritos a mano; sin esquema ni linaje. |
| Prueba de contenido | H02 | Cinco aserciones sobre el archivo real | No hay transformación que probar. |

### Relación técnica con actividades anteriores

Integra por nombre elementos de P434, P447 y P452, sin consumirlos. No referencia el linaje de P443 ni el manifiesto de P431. P433 (dbt) ya produce documentación de modelos en `manifest.json`; posible solapamiento conceptual no resuelto.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Ficha del caso | S01, S03 | `implementation/productos/P454_data_catalog/data/catalog.json`; `implementation/productos/P454_data_catalog/submission/catalog_entry.json`; `implementation/productos/P434_contract_versioning/data/contract.json`; `implementation/productos/P452_access_control/data/access_policy.json`; `implementation/productos/P447_incident_response/professor/main.py` | Coincidencias de texto, no dependencias. |
| H02 — Prueba de contenido | S02, S04 | `implementation/productos/P454_data_catalog/professor/main.py`: `load_catalog_entry`; `implementation/productos/P454_data_catalog/professor/test_main.py`; `implementation/productos/P454_data_catalog/tests/test_activity.py` | La prueba del estudiante no verifica contenido. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Ficha de catálogo | `data/catalog.json` | Una entrada; seis campos. |
| S02 | Lectura | `professor/main.py` | Copia sin transformación. |
| S03 | Ficha entregada | `submission/catalog_entry.json` | Idéntica a la entrada. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Profesor: cinco valores; estudiante: existencia. |
| S05 | Interfaz del estudiante | `src/main.py`; `notebooks/` | Plantilla vacía; sin instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** lee la ficha y la copia a `submission/`.
- **`submission/`:** `catalog_entry.json`.
- **Pruebas:** la de profesor verifica cinco valores del archivo de datos real; `test_01` verifica existencia.
- **Trazabilidad:** `productos.C02` y `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P434/P447/P452:** valores repetidos como texto; ningún artefacto leído.
- **Habilita para P455:** no evidenciada.

## Trazabilidad y auditoría

P454 mapea `productos.C02` y `productos.C05`. C05 («gobernar») se sostiene en la ficha; C02 (integración) es débil porque no se integra nada. La documentación para el uso, que `dig/s05-diseno-productos.md` asigna a `productos.C04`, no está mapeada. El producto descrito es el dataset de riesgo por fábrica; la ficha sirve a su gobierno sin verificarse contra él.
