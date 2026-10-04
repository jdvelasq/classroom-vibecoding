# P218 — Despliegue mediante API

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P218_deployment_api/`.

### Preguntas analíticas actuales

- ¿Cómo puede otro proceso solicitar una predicción de precio de vivienda mediante HTTP?
- ¿Qué contrato y validaciones debe cumplir la solicitud antes de usar el modelo?

Expone un predictor serializado mediante FastAPI, con endpoint de salud,
contrato Pydantic y un cliente que consume `/predict`.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** permite a otro proceso obtener una estimación de precio mediante HTTP; no evidencia quién usa la respuesta ni con qué decisión.
- **Producto terminal:** API con `/health`, `/predict`, validación Pydantic y cliente JSON.
- **Uso y límite:** valida dominios básicos de entrada; no monitorea servicio, modelo, latencia, deriva ni autorización.
- **Disciplinas contribuyentes:** APIs y validación sirven a una capacidad analítica interoperable.

### Highlights de contribución

- **H01 — Formaliza la entrada como contrato interoperable:** `HouseFeatures` fija siete campos y restricciones de dominio antes de crear el `DataFrame`.
- **H02 — Separa disponibilidad y predicción:** `/health` responde estado y `/predict` transforma una solicitud válida en JSON serializable.
- **H03 — Hace verificable el consumidor:** `client.py` envía un ejemplo, exige éxito HTTP y devuelve JSON.
- **H04 — Delimita el servicio:** modelo, linaje, autenticación, observabilidad y despliegue real no se evidencian.

### Inventario técnico de implementación

- **Introduce:** FastAPI, endpoints GET/POST, serialización JSON y consumidor
  HTTP con `requests`.
- **Introduce:** `BaseModel` de Pydantic y restricciones de dominio para las
  siete características de vivienda.
- **Reutiliza:** modelo de precio y la transformación a `DataFrame` de P217,
  pero sustituye interfaz manual por un contrato interoperable.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto observable | Límite |
| --- | --- | --- | --- |
| Esquema de entrada | H01 | Pydantic/`Field` y orden de columnas | No valida distribución ni procedencia. |
| Servicio HTTP | H02 | GET health y POST predict | No hay test de ejecución. |
| Cliente | H03 | `requests.post`, timeout y JSON | URL local fija. |
| Límite operativo | H04 | Código/ausencia de artefactos | Sin seguridad/observabilidad. |

### Relación técnica con actividades anteriores

Extiende P217 para que una capacidad predictiva pueda ser invocada por software
en lugar de una persona. Sin P218 se pierde el contrato verificable entre un
modelo y un consumidor programático.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite |
| --- | --- | --- | --- |
| H01 | S01 | `professor/server.py`: `HouseFeatures` | No hay validación de modelo. |
| H02 | S02 | `health`, `predict`, `predict_price` | No se arranca servidor en pruebas. |
| H03 | S03 | `professor/client.py` | Sólo ejemplo local. |
| H04 | S04 | Código y pruebas | Ausencia no sustituye prueba de operación. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Esquema/modelo | `server.py`; `.pkl` | Siete campos y orden fijo. |
| S02 | Endpoints | `server.py` | Health no prueba modelo. |
| S03 | Cliente | `client.py` | URL localhost fija. |
| S04 | Prueba/trazabilidad | tests; YAML | Falta P218; tests sólo archivos. |

### Contrato de evidencia actual

- **Código:** valida solicitud, carga modelo y devuelve predicción JSON.
- **`submission/`:** no hay entrega separada; servidor/cliente son evidencia.
- **Pruebas:** exigen archivos no vacíos, no una llamada HTTP.
- **Trazabilidad:** falta P218.

### Dependencias en la secuencia

- **Recibe de P217:** contrato de vivienda y modelo externo.
- **Habilita para Pyyy:** no hay consumidor posterior demostrable.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Es un producto de datos con disponibilidad y validación de entrada. No existe
entrada P218 en `implementation/predictiva/traceability.yaml`; debe revisarse
antes de aprobar la actividad.
