# P422 — Monitoreo de entradas: desplazamiento de medias entre referencia y producción

## Actividad actual implementada

**Implementación:** `implementation/productos/P422_model_monitoring/`.

### Preguntas analíticas actuales

- ¿Qué variables de entrada en producción se alejan de las observadas en la referencia lo suficiente como para emitir una alerta?

`data/reference.csv` y `data/production.csv` tienen 250 filas cada uno con las once variables fisicoquímicas del vino tinto y `quality`; las primeras filas de la referencia coinciden con las de `winequality-red.csv` de P420. `professor/main.py` compara cada variable excepto `quality`: calcula la diferencia absoluta de medias dividida por la desviación estándar de la referencia y alerta si supera `ALERT_THRESHOLD = 1.0`. `submission/monitoring_report.json` registra el umbral, la lista de alertas y, por variable, medias, diferencia estandarizada y alerta. Alertan `fixed_acidity` (1.373), `density` (1.205) y `alcohol` (3.665).

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** el docstring de `main()` separa «una señal de monitoreo de una decisión de reentrenamiento»; quién recibe la señal y qué decide no se declara.
- **Producto terminal:** `submission/monitoring_report.json`, una señal de desplazamiento por variable.
- **Uso y límite:** permite identificar qué entradas cambiaron respecto de la referencia. No dice si el cambio afecta al modelo: no se carga ningún modelo, la diferencia de medias no detecta cambios de forma o varianza, y el umbral 1.0 no se justifica.
- **Disciplinas contribuyentes:** estadística descriptiva (media y desviación estándar) al servicio de la vigilancia de entradas de una capacidad en operación.

### Highlights de contribución

- **H01 — Convierte una comparación de distribuciones en señal por variable:** `compare_feature` devuelve medias, diferencia estandarizada y `alert`; `main()` reúne las alertas en una lista legible. `test_01` y `test_02` verifican que una distribución idéntica no alerta y que una desplazada sí. Sin este hito, el curso no tendría monitoreo de entradas en operación separado de la prueba previa al scoring de P404.
- **H02 — Expone qué cambió en un caso con desplazamiento concentrado (caso y datos):** con el mismo dominio de P420, las alertas se concentran en tres variables y `alcohol` domina (media 9.854 en referencia frente a 12.887 en producción). El archivo de producción contiene filas repetidas y valores de `alcohol` escritos como enteros (`13`, `12`), lo que sugiere un conjunto construido para mostrar el desplazamiento; su procedencia no se documenta. La señal por variable permite ver que el cambio no es uniforme, pero el caso no permite inferir un desplazamiento real.
- **H03 — Excluye la etiqueta del monitoreo de entradas:** `features = [column for column in reference.columns if column != "quality"]` deja fuera el objetivo, aunque esté en ambos archivos. Separa vigilancia de entradas (sin necesitar resultados) de vigilancia de desempeño, que P423 trata aparte. Sin este hito, la distinción entre ambos tipos de monitoreo no sería visible en el código.

### Inventario técnico de implementación

- **Introduce:** diferencia de medias estandarizada por la desviación de referencia, umbral fijo de alerta, reporte JSON por variable.
- **Reutiliza:** dominio de vino tinto de P420; patrón de reporte con decisión booleana de P404 (`compatible`).
- **Aplica en nuevo caso:** monitoreo de entradas sobre vino tinto (P404 lo hacía sobre dos variables de cáncer de mama).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Deriva univariada de medias | H01 | `abs(mean_p - mean_r) / std_r > 1.0` | Sin prueba estadística, sin forma de la distribución. |
| Señal por variable | H01, H02 | Lista `alerts` y detalle por variable | Producción de procedencia no documentada. |
| Entradas frente a desempeño | H03 | Exclusión de `quality` | No hay modelo en el taller. |

### Relación técnica con actividades anteriores

Misma pregunta general que P404 (¿las entradas nuevas se parecen a las conocidas?) con nuevo método y nuevo uso: P404 usa `IsolationForest` multivariado como compuerta antes del scoring, con columnas leídas del estimador; P422 usa una diferencia univariada como señal en operación, sin estimador. Posible solapamiento conceptual P404/P422 que requiere decisión posterior de curso. Comparte dominio con P420 sin consumir sus modelos.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Señal por variable | S02, S04 | `implementation/productos/P422_model_monitoring/professor/main.py`: `compare_feature`; `implementation/productos/P422_model_monitoring/professor/test_main.py` | Las pruebas usan un `DataFrame` de juguete con la columna `quality`, que `main()` excluye. |
| H02 — Desplazamiento concentrado | S01, S03 | `implementation/productos/P422_model_monitoring/data/reference.csv`; `implementation/productos/P422_model_monitoring/data/production.csv`; `implementation/productos/P422_model_monitoring/submission/monitoring_report.json` | No hay documentación de cómo se obtuvo `production.csv`. |
| H03 — Etiqueta excluida | S02 | `implementation/productos/P422_model_monitoring/professor/main.py`: `main` | No se usa `quality` en ninguna parte. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Referencia y producción | `data/reference.csv`; `data/production.csv` | 250 filas cada uno; procedencia no documentada. |
| S02 | Medida y umbral | `professor/main.py` | Diferencia de medias; umbral 1.0 fijo. |
| S03 | Reporte | `submission/monitoring_report.json` | Una ventana; sin fecha ni destinatario. |
| S04 | Pruebas | `professor/test_main.py`; `tests/test_activity.py` | Alerta/no alerta en datos de juguete; existencia del reporte. |
| S05 | Interfaz del estudiante | `src/main.py` | Plantilla sin `HOW_TO_RUN_ME.txt`. |

### Contrato de evidencia actual

- **Notebook o código:** compara once variables y escribe el reporte.
- **`submission/`:** `monitoring_report.json` con umbral, tres alertas y detalle por variable.
- **Pruebas:** `professor/test_main.py` verifica la lógica de alerta en dos casos extremos; `tests/test_activity.py` sólo la existencia del reporte. No se verifica el contenido del reporte ni el umbral.
- **Trazabilidad:** `productos.C02`, `productos.C03`, `productos.C05`.

### Dependencias en la secuencia

- **Recibe de P420:** dominio y, según las primeras filas, un subconjunto de `winequality-red.csv` como referencia; no recibe modelo. De P404, el patrón de comparar entradas nuevas con conocidas.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

Entrada revisada: P422 → `productos.C02`, `productos.C03`, `productos.C05`. C03 (validación de insumos frente al uso) y C05 (monitoreo) se sostienen; C02 es secundario. Auditoría: el producto es una señal de monitoreo de entradas para una capacidad de calidad de vino que no aparece en el taller; el nombre «model monitoring» no se corresponde con la ausencia de modelo. La identidad de productos se sostiene parcialmente: vigila insumos, pero sin usuario ni decisión conectados.
