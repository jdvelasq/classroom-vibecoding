# P426 — API en contenedor: el mismo contrato servido desde Docker

## Actividad actual implementada

**Implementación:** `implementation/productos/P426_api_container/`.

### Preguntas analíticas actuales

- ¿Cómo se publica localmente, desde un contenedor, el servicio de clasificación de riesgo sin cambiar su contrato?

`professor/main.py` repite la aplicación Flask de P425 (`POST /score`, validación de `daily_units_produced` entero, `risk` = `high` si es menor que 4500, `threshold` 4500), sin la generación de ejemplos ni `app.run`. `Dockerfile` parte de `python:3.11-slim`, instala `requirements.txt` (`flask==3.1.3`), copia sólo `src/` y arranca `flask --app src.main run --host 0.0.0.0 --port 8000`. `HOW_TO_RUN_ME.txt` construye la imagen, la ejecuta con `--publish 8000:8000` y guarda la respuesta de una solicitud `curl` en `submission/score_response.json` (`{"risk": "high", "threshold": 4500}`).

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** no evidenciados.
- **Producto terminal:** imagen que sirve `/score` en el puerto 8000 y una respuesta capturada desde fuera del contenedor.
- **Uso y límite:** permite consumir el servicio desde el equipo anfitrión mediante un puerto publicado. La regla sigue siendo el umbral fijo de P425; las pruebas no ejecutan el contenedor.
- **Disciplinas contribuyentes:** contenedores y servicios web al servicio de desplegar la interfaz de una capacidad.

### Highlights de contribución

- **H01 — Despliega un servicio, no un lote:** el contenedor se mantiene en ejecución y expone un puerto (`--host 0.0.0.0`, `--publish 8000:8000`), a diferencia de P418, que ejecutaba un lote y entregaba el resultado por volumen. La evidencia es una respuesta HTTP capturada con `curl --output` desde el anfitrión. Sin este hito, la interfaz de P425 sólo se ejecutaría en el ambiente del estudiante.
- **H02 — Prueba el borde de la regla y la estrictez del tipo (caso y datos):** `test_containerized_service_preserves_the_analytics_contract` envía 4500 y exige `low` (el borde que P425 no probaba); `test_containerized_service_rejects_invalid_input` rechaza `4200.0`. El caso sigue siendo un entero por solicitud contra un umbral sin procedencia; lo nuevo es fijar el comportamiento en el borde. El docstring afirma que «el contenedor entrega la misma decisión», pero la prueba usa `app.test_client()` en proceso, no el contenedor.

### Inventario técnico de implementación

- **Introduce:** contenedor de servicio, `flask --app ... run --host 0.0.0.0`, `docker run --publish`.
- **Extiende:** `Dockerfile` de P418 (misma imagen base y manifiesto local) a un servicio.
- **Reutiliza:** validación, regla y respuesta de P425 (copiadas, no importadas).
- **Aplica en nuevo caso:** ninguno.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Servicio en contenedor | H01 | Imagen con Flask y puerto publicado | Sin prueba del contenedor ni etiqueta de versión. |
| Borde de la regla | H02 | 4500 → `low`; `4200.0` → 400 | Prueba en proceso. |

### Relación técnica con actividades anteriores

Composición de P418 (contenedor) y P425 (API) con el mismo contrato. Duplica la lógica de P425 en otro archivo, lo que permite que ambas versiones diverjan. Posible solapamiento que requiere decisión posterior de curso; la contribución distinguible es el paso de lote a servicio y la prueba del borde.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Servicio en contenedor | S02, S03, S05 | `implementation/productos/P426_api_container/Dockerfile`; `implementation/productos/P426_api_container/HOW_TO_RUN_ME.txt`; `implementation/productos/P426_api_container/submission/score_response.json` | La respuesta persistida no registra si provino del contenedor. |
| H02 — Borde y tipo | S01, S04 | `implementation/productos/P426_api_container/professor/main.py`: `score`; `implementation/productos/P426_api_container/professor/test_main.py` | Las pruebas no ejecutan Docker. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Servicio y regla | `professor/main.py` | Lógica copiada de P425. |
| S02 | Imagen | `Dockerfile`; `.dockerignore`; `requirements.txt` | Copia sólo `src/`; manifiesto local justificado en `structure-audit.md`. |
| S03 | Ejecución | `HOW_TO_RUN_ME.txt` | Docker Desktop; puerto 8000. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | En proceso; existencia de la respuesta. |
| S05 | Evidencia e interfaz del estudiante | `submission/score_response.json`; `src/main.py` | La plantilla es `def main()`; el `Dockerfile` espera un objeto `app` en `src.main`. |

### Contrato de evidencia actual

- **Notebook o código:** aplicación Flask con `/score`.
- **`submission/`:** `score_response.json` con una respuesta válida.
- **Pruebas:** `professor/test_main.py` verifica el borde 4500 y el rechazo de un flotante, en proceso. `tests/test_activity.py` sólo la existencia de la respuesta. Nada verifica la imagen ni el puerto.
- **Trazabilidad:** `productos.C02`, `productos.C04`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P425:** contrato, validación y regla; de P418, el patrón de `Dockerfile`.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P426 → `productos.C02`, `productos.C04`, `productos.C05`. C02 (entrega desplegable) y C04 (interfaz) se sostienen; C05 sin evidencia. Auditoría (pregunta 5): taller de despliegue con Docker alrededor de una regla arbitraria; riesgo de lectura como capacitación en herramienta no resuelto.
