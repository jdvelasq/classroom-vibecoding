# P312 — Propuestas de mejora

**Línea base:** `P312_activity.md` (entrada S02 más reciente: `S02.P312.01`).

## T01 — Mostrar el compromiso costo–beneficio con su frontera de Pareto y atar la salvaguarda de «opción dominada» al valor por cliente y al presupuesto

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia (corrige un rótulo engañoso del contrato)
- **Fuentes:**
  - `design/benchmarks-md/institutional/mit-quantitative-methods-in-systems-engineering.md` pp. 3–4 — «define how these designs will be evaluated in terms of value (Week 2) and other outputs, such as cost and performance» y «tradespace visualization» (p. 3); «looking for patterns in the tradespace, such as clusters and the Pareto Front. You will define what sensitivity means for a design in the tradespace» (p. 4): el tradespace se lee en varios atributos (valor y costo), se interpreta por su frontera de Pareto y la sensibilidad se define sobre él (Claude, 2026-10-05). Fuente *institutional*, única y de sólo títulos semanales: ilustra la posibilidad; la justificación de la propuesta es el defecto de P312, no el syllabus de MIT.
- **Qué gana el estudiante:** distinguir una opción **dominada** (otra es
  igual o mejor en todos los atributos) de una opción **no seleccionada bajo
  un modelo de valor y una restricción**. Con los datos que describe S02
  (P0: costo 0, ganancia 0; P1: 18.000 y 0,018; P2: 42.000 y 0,055; 10.000
  clientes; valor por cliente 260), las tres opciones son eficientes en el
  plano costo mensual–clientes retenidos: P1 es más barata que P2 y retiene
  más que P0, así que nadie la domina. Lo que ocurre es más fino: P1 queda
  por debajo del segmento P0–P2 (con 18.000 de costo, ese segmento retiene
  ≈ 236 clientes; P1 retiene 180), de modo que **ningún** valor positivo por
  cliente la hace ganar si el presupuesto no restringe. Por eso el
  multiplicador común de H01 nunca la elige (P2 supera a P1 desde un valor
  ≈ 64,9 por cliente; P1 sólo supera a P0 desde 100). Pero si el presupuesto
  mensual baja de 42.000 y no de 18.000, P2 deja de ser factible y P1 (valor
  neto 28.800 con 260 por cliente) pasa a ser la elegida. La salvaguarda
  `dominated_option` dice que P1 «no debe mantenerse por costumbre»; su texto
  es cierto en la grilla analizada, pero su rótulo es falso y su validez
  depende de dos constantes en código (`CUSTOMER_VALUE`, `MONTHLY_BUDGET`) que
  el contrato no declara como condición. El estudiante ve en una figura la
  frontera, las rectas de igual valor neto y el corte del presupuesto, y
  reescribe la salvaguarda como condición explícita del contrato, con
  gatillo de revisión. La frontera no es el producto: sirve a la regla de
  revisión de la política. Además, el nombre «tradespace» que S02 registra
  como impropio (un solo criterio) pasa a tener contenido: dos atributos y su
  agregación.
- **Anclas actuales:** H03 (opción no seleccionada; límite «afirmación sobre
  la grilla» y «presupuesto igual al costo de P2: la restricción no
  discrimina»); H01 y H02 se conservan intactos; superficies S01
  (`service_options.csv`, `CUSTOMER_VALUE`, `MONTHLY_BUDGET`), S02
  (`evaluate`, `evaluate_sensitivity`), S03 (`policy_record`,
  `delivery_promise_policy.json`) y S04 (`tests/test_activity.py`).
  Dependencia: recibe de P311 la forma del registro JSON, que se conserva.
- **Alternativas menores descartadas:** renombrar la salvaguarda o matizar su
  texto corrige el rótulo, pero no da al estudiante la evidencia que muestra
  por qué P1 no está dominada ni cuándo volvería a ser la elegida. Extender
  H01 con otro multiplicador no basta: un multiplicador común sobre el valor
  nunca elige P1 (por la geometría descrita); sólo el presupuesto la
  reactiva.
- **Contrato de no regresión:** se conservan H01 y H02 con sus cifras
  (`sensitivity_review.csv` de 0,20 a 1,25; umbral 0,0162 y su gatillo), el
  caso y `service_options.csv`, `tradespace.csv` con sus filas y columnas
  actuales y las demás claves de `delivery_promise_policy.json` (acción,
  condición, umbral, presupuesto, autoridad rutinaria y de excepción,
  gatillos, monitoreo). **Sustitución explícita:** la salvaguarda
  `dominated_option` se reemplaza por una salvaguarda condicionada (por
  ejemplo `non_selected_option`) cuyo texto declara el valor por cliente y el
  presupuesto bajo los que vale; la evidencia que la sostiene (frontera y
  barrido de presupuesto) es más fuerte que la afirmación actual. No se
  crean roles nuevos: el escalamiento usa la autoridad de excepción ya
  declarada (dirección comercial). Las pruebas existentes se mantienen.
- **Interacciones:** ninguna dentro de P312 (única propuesta). Capacidad:
  añade una figura, una tabla corta y un barrido de presupuesto sobre tres
  opciones; no cambia caso ni producto, por lo que el riesgo para el taller
  es bajo.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo (o H03
  modificado) en el que (1) una figura muestra las tres opciones en el plano
  costo mensual–clientes retenidos, la frontera de Pareto, las rectas de
  igual valor neto con 260 por cliente y el corte del presupuesto; (2) una
  tabla persistida marca P1 como eficiente y no soportada (bajo el segmento
  P0–P2); (3) un barrido de presupuesto muestra que P1 se elige con
  presupuestos en [18.000, 42.000); y (4) `delivery_promise_policy.json`
  sustituye `dominated_option` por una salvaguarda condicionada al valor por
  cliente y al presupuesto, con gatillo de revisión si el presupuesto baja de
  42.000. Respaldo en notebook, `submission/` y pruebas. H01 y H02 siguen
  presentes con sus cifras.

### Instrucciones de ejecución

```text
Actividad: implementation/prescriptiva/P312_sensibilidad_y_tradespace/

0. Inspecciona primero data/service_options.csv, professor/main.py
   (evaluate, evaluate_sensitivity, policy_record, CUSTOMER_VALUE,
   MONTHLY_BUDGET), professor/notebook.ipynb, submission/ y tests/. Si los
   costos, ganancias de retención, clientes, valor por cliente o presupuesto
   no coinciden con design/courses/prescriptiva/P312_activity.md (0/18.000/
   42.000; 0/0,018/0,055; 10.000; 260; 42.000), detente e informa. Verifica
   también si el presupuesto se aplica como restricción de factibilidad en
   evaluate; anota la respuesta (cambia el paso 3, no la propuesta). Si con
   los datos reales P1 resulta dominada por P0 o por P2 (igual o peor en
   costo y en clientes retenidos), detente e informa: la propuesta no
   tendría evidencia.
1. No cambies service_options.csv, el multiplicador de evaluate_sensitivity,
   sensitivity_review.csv, el umbral 0,0162 ni las filas y columnas de
   tradespace.csv.
2. FRONTERA: añade en main.py una función (por ejemplo pareto_review) que,
   para cada opción, calcule retained_customers = monthly_customers ×
   retention_gain, gross_value = retained_customers × CUSTOMER_VALUE,
   net_value, pareto_efficient (ninguna otra opción tiene costo menor o
   igual y retención mayor o igual, con al menos una estricta) y supported
   (la opción está sobre la envolvente convexa superior de las eficientes, es
   decir, algún valor positivo por cliente la hace óptima sin presupuesto).
   Persiste submission/pareto_review.csv con columnas option, monthly_cost,
   retention_gain, retained_customers, gross_value, net_value,
   pareto_efficient, supported.
3. PRESUPUESTO: añade una función (por ejemplo evaluate_budget) que recorra
   presupuestos mensuales de 0 a 60.000 (paso 6.000, incluyendo 18.000 y
   42.000) y elija la opción factible (monthly_cost <= budget) de mayor
   valor neto con CUSTOMER_VALUE. Persiste submission/budget_review.csv con
   columnas monthly_budget, selected_option, net_value. Si evaluate no
   aplicaba el presupuesto (paso 0), no cambies evaluate: el barrido es
   adicional.
4. FIGURA: en el notebook de profesor, después de la sección de H01,
   grafica costo mensual (x) contra clientes retenidos (y), la frontera de
   Pareto, dos o tres rectas de igual valor neto con 260 por cliente y una
   línea vertical en el presupuesto de 42.000. Guarda
   submission/tradespace_frontier.png. Explica en markdown, en 4–6 líneas:
   por qué P1 no está dominada, por qué ningún valor por cliente la elige
   sin presupuesto (queda bajo el segmento P0–P2) y en qué rango de
   presupuesto pasa a ser la elegida.
5. SALVAGUARDA: en policy_record sustituye la clave dominated_option por
   una salvaguarda condicionada (por ejemplo non_selected_option) que diga
   que P1 no se mantiene mientras el valor por cliente sea el declarado y el
   presupuesto mensual sea >= 42.000, y añade a los gatillos existentes uno
   que pida reevaluar P1 frente a P0 y escalar a la autoridad de excepción
   ya declarada si el presupuesto baja de 42.000. No crees roles ni cambies
   las demás claves. No uses la palabra «dominated» para P1.
6. Añade a tests/ pruebas que verifiquen: pareto_review.csv con esas
   columnas y P1 con pareto_efficient verdadero y supported falso;
   budget_review.csv con P1 seleccionada en al menos un presupuesto en
   [18.000, 42.000) y P2 con presupuesto >= 42.000; el PNG; y que
   delivery_promise_policy.json ya no contiene dominated_option y contiene
   la salvaguarda condicionada. No elimines pruebas existentes.
7. Ejecuta main(), el notebook completo y las pruebas sin errores; confirma
   que sensitivity_review.csv y el umbral 0,0162 no cambiaron.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
