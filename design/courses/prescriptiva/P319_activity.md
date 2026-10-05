# P319 — Catalog Assortment: surtido con canibalización bajo capacidad de catálogo

## Actividad actual implementada

**Implementación:** `implementation/prescriptiva/P319_catalog_assortment/`.

### Preguntas analíticas actuales

- ¿Qué productos incluir en un catálogo limitado, sabiendo que la demanda de cada producto depende de cuáles otros se ofrecen junto a él?
- ¿Por qué un producto con margen positivo y demanda propia puede reducir el margen total del surtido?
- ¿Cómo cambia el surtido óptimo con la capacidad del catálogo?

El notebook declara un «catálogo sintético de una sola categoría; no representa un catálogo real». `data/products.csv` tiene ocho productos con precio, costo unitario y atractivo; la elección del cliente se modela con un logit multinomial con atractivo de no compra `v0 = 1` y capacidad `K = 4`. El notebook enumera los 163 surtidos factibles, compara el óptimo con tres reglas ingenuas, demuestra la canibalización y mide la sensibilidad a la capacidad. Un segundo programa, `professor/main.py`, produce la tabla de decisión por producto, el contrato de política y el plan de monitoreo que exige la prueba. El producto es una recomendación de surtido gobernada, aunque notebook y script generan artefactos distintos y uno sobrescribe parte del otro.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** incorporar o retirar productos del catálogo de una categoría; el contrato asigna la aprobación al «gerente de categoría» y el escalamiento de precios, costos o capacidad anómalos a «comercial y operaciones». Roles declarados en un caso sintético.
- **Producto terminal:** `assortment_policy.csv` (incluir/excluir con razón), `policy_contract.json` y `policy_monitoring.csv`, respaldados por la enumeración y la sensibilidad del notebook.
- **Uso y límite:** permite justificar un surtido que no es la suma de los mejores productos individuales y fijar gatillos de revisión cuantificados. El atractivo es un parámetro dado, no estimado; la política declara «hasta cuatro productos» mientras el óptimo usa tres, y la enumeración sólo es viable a esta escala.
- **Disciplinas contribuyentes:** modelo de elección logit multinomial, enumeración exhaustiva y análisis de sensibilidad sirven a la política de surtido.

### Highlights de contribución

- **H01 — Muestra que el valor de un producto depende del surtido (caso y datos):** con el logit multinomial, `P(i|S) = v[i] / (v0 + Σ v[j])`, cada producto añadido reduce la probabilidad de los demás. El notebook calcula la economía individual de cada producto y luego demuestra que agregar P4 a {P1, P2, P3} le da demanda positiva pero reduce el margen esperado (−0,743), mientras que agregarlo a {P6} lo aumenta (+1,502). Esta particularidad del dataset (atractivos que compiten por el mismo cliente) es la que hace inválido ordenar productos por su valor propio. Sin este hito, el surtido se decidiría producto por producto.
- **H02 — Deriva una condición analítica de incorporación y la verifica:** agregar `k` mejora `R(S)` si y sólo si `margin[k] > R(S)`; el notebook compara la condición con la recomputación directa (20 frente a 27,5). Sin este hito, la canibalización sería un resultado numérico sin regla operable.
- **H03 — Justifica el método por la estructura del objetivo:** el notebook explica que un MILP aditivo sería incorrecto porque `P(i|S)` depende del conjunto completo y que, a esta escala, la búsqueda exhaustiva es el método transparente; enumera 163 surtidos (incluido el vacío), afirma su número y unicidad, y verifica que el óptimo es único con brecha 0,423 frente al segundo. Primera aparición en el curso de un objetivo no aditivo; P316–P318 usaban LP continuo. Sin este hito, se aplicaría un solver por costumbre a un objetivo que no le corresponde.
- **H04 — Compara el óptimo con tres reglas ingenuas bajo el mismo criterio:** mayor margen unitario, mayor atractivo y mayor margen individual quedan por debajo del surtido {P1, P2, P3} (margen esperado 27,5; probabilidad de compra 0,8, persistidos en `capacity_sensitivity.csv`). Sin este hito, el óptimo no tendría una línea base operable.
- **H05 — Muestra que la capacidad adicional deja de usarse:** `capacity_sensitivity.csv` persiste el óptimo para K = 1 a 6; desde K = 3 el surtido y su valor no cambian. El notebook aclara que no es que agregar productos no tenga efecto, sino que ninguno mejora el margen. Una sensibilidad a `v0` se muestra sólo en el notebook. Sin este hito, la capacidad del catálogo se interpretaría como meta de ocupación.
- **H06 — Declara una política de surtido con guardas, autoridad y gatillos cuantificados:** `policy_contract.json` fija cadencia mensual, entradas vigentes, ejecución con aprobación humana, tres guardas (no exceder cuatro plazas, no incorporar margen no positivo, no publicar con atributos incompletos), excepciones, monitoreo y gatillos con umbral (margen realizado 15 % menor durante dos revisiones; no compra 10 puntos por encima de lo estimado). `policy_monitoring.csv` persiste las líneas base 27,5 y 0,2. Sin este hito, el producto sería un ranking de surtidos.

### Inventario técnico de implementación

- **Introduce:** modelo de elección logit multinomial con opción de no compra; objetivo no aditivo; condición de incorporación `margin[k] > R(S)`; sensibilidad de capacidad con plazas no usadas.
- **Extiende:** enumeración exhaustiva verificada (P305, P308, P315) a un objetivo que no admite MILP aditivo; comparación con reglas ingenuas.
- **Reutiliza:** bloque `DECISION MODEL` en texto, celda final de verificación, planeador de cuatro paneles, contrato JSON con guardas, autoridad, monitoreo y gatillos.
- **Aplica en nuevo caso:** surtido sintético de una categoría.

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Canibalización por elección | H01–H02 | Logit multinomial; ejemplo P4 en surtido fuerte y débil; condición analítica | Atractivos dados, no estimados; ejemplos sólo en notebook. |
| Objetivo no aditivo | H03 | Justificación contra MILP aditivo; enumeración de 163 surtidos; unicidad | Viable sólo a esta escala. |
| Líneas base y capacidad | H04–H05 | Tres reglas ingenuas; óptimo por K = 1–6 | Comparación de reglas no persistida; sensibilidad a `v0` no persistida. |
| Política de surtido | H06 | Contrato con guardas, autoridad, excepciones, monitoreo y gatillos con umbral | Producido por `main.py`, no por el notebook. |

### Relación técnica con actividades anteriores

P319 vuelve a la enumeración después del LP continuo de P316–P318, pero por una razón nueva: el objetivo no es aditivo, no por el tamaño finito del problema. Comparte con P305, P308 y P315 la plantilla reglas ingenuas → modelo → enumeración → sensibilidad → planeador → contrato; lo distinto es la interdependencia de la demanda entre alternativas. Frente a P304 (aceptación con capacidad), aquí la capacidad es de exhibición y su valor marginal se anula. No hay duplicación evidente. La doble generación de artefactos (notebook y `main.py`) es una inconsistencia de implementación, no de contenido: `assortment_results.csv` persistido tiene tres columnas (versión de `main.py`), mientras el notebook escribe cinco columnas con probabilidades y rango.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Canibalización | S01, S02 | `implementation/prescriptiva/P319_catalog_assortment/data/products.csv`; `implementation/prescriptiva/P319_catalog_assortment/professor/notebook.ipynb`: `choice_probabilities`, `standalone`, celdas del surtido fuerte y débil | Cifras del notebook (afirmadas con `assert`), no persistidas. |
| H02 — Condición de incorporación | S02 | Notebook: celda de la condición `margin[k] > R(S)` | Ilustrada con un candidato. |
| H03 — Enumeración por objetivo no aditivo | S03 | Notebook: celda que descarta el MILP aditivo, enumeración y unicidad; `implementation/prescriptiva/P319_catalog_assortment/submission/assortment_results.csv` | El CSV persistido proviene de `main.py` (tres columnas). |
| H04 — Reglas ingenuas | S03, S05 | Notebook: `policy_comparison`; `implementation/prescriptiva/P319_catalog_assortment/submission/capacity_sensitivity.csv` | La tabla de comparación no se persiste. |
| H05 — Capacidad no usada | S04, S05 | `implementation/prescriptiva/P319_catalog_assortment/submission/capacity_sensitivity.csv`; notebook: `best_assortment_for_v0` | Sensibilidad a `v0` sólo impresa. |
| H06 — Política de surtido | S06, S07 | `implementation/prescriptiva/P319_catalog_assortment/professor/main.py`; `implementation/prescriptiva/P319_catalog_assortment/submission/policy_contract.json`; `implementation/prescriptiva/P319_catalog_assortment/submission/policy_monitoring.csv`; `implementation/prescriptiva/P319_catalog_assortment/submission/assortment_policy.csv` | El notebook no construye el contrato; la prueba sólo verifica presencia de archivos. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Dataset sintético | `data/products.csv`; celda de validación | Ocho productos; atractivo dado. |
| S02 | Modelo de elección y canibalización | Notebook: funciones de elección, ejemplos y condición | Ejemplos fijados para la instancia. |
| S03 | Método y líneas base | Notebook: bloque `DECISION MODEL`, enumeración, reglas ingenuas | Enumeración viable sólo a esta escala. |
| S04 | Sensibilidad | Notebook: `capacity_sensitivity`, `best_assortment_for_v0` | Sólo la de capacidad se persiste. |
| S05 | Entregables del notebook | `assortment_results.csv`, `product_decisions.csv`, `capacity_sensitivity.csv`, `catalog_portfolio_planner.png` | `assortment_results.csv` sobrescrito por `main.py`. |
| S06 | Política y contrato | `professor/main.py`; `assortment_policy.csv`; `policy_contract.json`; `policy_monitoring.csv` | Política «hasta cuatro» con óptimo de tres. |
| S07 | Pruebas | `tests/test_activity.py` | Presencia de tres archivos. |

### Contrato de evidencia actual

- **Notebook o código:** el notebook valida datos, define el modelo de elección, compara reglas, enumera, verifica unicidad, demuestra canibalización, mide sensibilidad y guarda cuatro artefactos; `main.py` valida, enumera con la guarda de margen no positivo y guarda política, contrato, monitoreo y su propia versión de `assortment_results.csv`.
- **`submission/`:** `assortment_results.csv`, `product_decisions.csv`, `capacity_sensitivity.csv`, `catalog_portfolio_planner.png`, `assortment_policy.csv`, `policy_contract.json`, `policy_monitoring.csv`.
- **Pruebas:** `test_submission_contains_policy_evidence` exige que existan `assortment_policy.csv`, `policy_contract.json` y `policy_monitoring.csv`. No verifica contenido, surtido, cálculos ni campos del contrato.
- **Trazabilidad:** P319 mapea `prescriptiva.C02`, `C03`, `C04` y `C05`.

### Dependencias en la secuencia

- **Recibe de P305/P308/P315:** enumeración exhaustiva verificada y reglas ingenuas como línea base. **Recibe de P316–P318:** el contraste explícito con métodos de solver.
- **Habilita para Pyyy:** no evidenciada.

## Trazabilidad y auditoría

P319 está mapeada a `prescriptiva.C02`, `C03`, `C04` y `C05` en `implementation/prescriptiva/traceability.yaml`. C02 se sostiene (regla de incorporación y surtido computable); C03 en la comparación con reglas ingenuas y la sensibilidad, con un modelo determinista; C04 en aprobación humana y escalamiento; C05 en monitoreo con líneas base y gatillos cuantificados. Frente a la arquitectura («regla de incorporación y retiro con capacidad») el producto existe. El producto de Analytics es una política de surtido gobernada; el modelo de elección y la enumeración son evidencia. Límite de implementación: el contrato vive en un script separado del notebook presencial, y la prueba no verifica su contenido.
