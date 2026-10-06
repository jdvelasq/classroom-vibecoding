# P218 — Despliegue en aplicación web

## Actividad actual implementada

**Implementación:** `implementation/predictiva/P217_deployment_web_app/`.

### Preguntas analíticas actuales

- ¿Cómo se entrega una predicción de precio de vivienda a un usuario mediante una interfaz web?
- ¿Cómo se transforma y valida la entrada del formulario antes de invocar un modelo ya entrenado?

Publica un predictor serializado de precio de vivienda en Flask, con formulario,
transformación de variables y manejo de entradas inválidas.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** permite a una persona solicitar un precio estimado; no evidencia procedencia, desempeño o uso autorizado del modelo.
- **Producto terminal:** interfaz web que valida entrada, construye una fila y devuelve predicción.
- **Uso y límite:** hace usable un modelo externo a la actividad; no entrena, monitorea ni evalúa el predictor.
- **Disciplinas contribuyentes:** Flask y contratos de entrada sirven a una capacidad analítica usable.

### Highlights de contribución

- **H01 — Define un contrato de siete características:** convierte tipos, transforma `waterfront` y construye el `DataFrame` en orden fijo.
- **H02 — Hace accesible el predictor a una persona:** ruta GET/POST y plantilla muestran resultado o error de entrada.
- **H03 — Delimita responsabilidad del despliegue:** carga un modelo previamente producido; entrenamiento, procedencia y monitoreo no están en el taller.

### Inventario técnico de implementación

- **Introduce:** aplicación Flask, rutas GET/POST, plantilla HTML y lectura de
  campos de formulario.
- **Introduce:** contrato local de siete características, conversión de tipos y
  ensamblaje de una fila `DataFrame` antes de `predict`.
- **Verifica:** trata errores de valores y entrega el archivo fuente como
  evidencia persistente; la prueba comprueba su presencia.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto observable | Límite |
| --- | --- | --- | --- |
| Contrato de entrada | H01 | Tipos y orden de siete campos | No valida rango salvo conversión. |
| Interfaz usable | H02 | Flask/formulario/error | No hay prueba de interacción. |
| Modelo externo | H03 | `HOUSE_PREDICTOR.pkl` | Sin evaluación o procedencia. |

### Relación técnica con actividades anteriores

Reutiliza un modelo ya entrenado para convertir una predicción en capacidad
utilizable. Sin P218 se pierde la transición desde evaluación de modelos hacia
una interfaz para un usuario, aunque el entrenamiento queda fuera de esta
actividad.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 | S01 | `professor/main.py`: `FEATURES`, `predict_price` | No verifica semántica de rangos. |
| H02 | S02 | `index`, plantilla y manejo de errores | Tests sólo revisan archivo. |
| H03 | S03, S04 | `HOUSE_PREDICTOR.pkl`; código | Sin monitoreo ni linaje. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Contrato/modelo | `main.py`; `.pkl` | Orden de columnas debe coincidir. |
| S02 | Interfaz y error | Plantilla/código | Error sólo cubre parseo. |
| S03 | Producto/prueba | Fuente; tests | Sin prueba funcional. |
| S04 | Trazabilidad | YAML | Falta P218. |

### Contrato de evidencia actual

- **Código:** recibe formulario, valida tipos, carga modelo y predice.
- **`submission/`:** no hay entrega separada; el código es la evidencia.
- **Pruebas:** exigen `main.py` no vacío.
- **Trazabilidad:** falta P218.

### Dependencias en la secuencia

- **Recibe de P200/P220:** artefacto de estimador, sin linaje demostrable.
- **Habilita para P219:** contrato de vivienda para uso programático.

## Mejoras aceptadas pendientes de implementación

No hay mejoras aceptadas pendientes.

## Trazabilidad y auditoría

Es un producto de datos: la predicción queda disponible a un usuario. No existe
entrada P218 en `implementation/predictiva/traceability.yaml`; debe revisarse
antes de aprobar la actividad.
