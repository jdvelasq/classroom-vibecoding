# P151 — Propuestas de mejora

**Línea base:** `P151_activity.md` (entrada S02 más reciente: `S02.P151.02`).

## T01 — Construir una dimensión de fecha de calendario completo y mostrar qué oculta una dimensión derivada del hecho

- **Estado:** pendiente de discusión
- **Tipo:** método + producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` p. 11 — «Calendar date dimensions are attached to virtually every fact table to allow navigation of the fact table through familiar dates, months, fiscal periods, and special days on the calendar»; la dimensión lleva atributos como semana, nombre del mes, período fiscal e indicador de festivo, y una fila especial para fechas desconocidas (Claude, 2026-10-04). Fuente *authoritative*: técnica estándar del modelado dimensional.
  - `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` p. 2 — la unidad de modelado dimensional incluye «Time Dimension» y el ejercicio «Classroom Hands-on: Design your Time and Conformed Dimensions» (Claude, 2026-10-04). Fuente *institutional*: ilustra la práctica en un curso de posgrado de data warehousing.
- **Qué gana el estudiante:** entender que la dimensión de fecha es un
  calendario, no la lista de fechas en que hubo hechos, y ver qué se pierde
  cuando se deriva del hecho. Hoy `dim_date` se construye sólo con las fechas
  presentes en `fact_sales` y guarda año y mes (H01; S02: «dimensión de fecha
  mínima»); como el generador asigna una fecha por pedido, los días sin ventas
  no existen en la dimensión y el propio S02 registra que «no sirve para tasas
  por día calendario». Con un calendario continuo que cubre el rango del
  hecho, con atributos de trimestre, semana, día de la semana e indicador de
  día hábil, el estudiante puede contar días sin ventas, calcular ventas por
  día calendario frente a ventas por día con ventas y ver que un período sin
  actividad aparece en cero en lugar de desaparecer. Es la base de toda
  comparación entre períodos (P152 T02) y de la navegación año→mes de P152
  H01.
- **Anclas actuales:** H01 (hecho y dimensiones; `dim_date` derivada del
  hecho), H03 (mart persistido e íntegro), H04 (consulta en estrella);
  superficies S02 (modelo dimensional), S03 (mart y consulta) y S04 (pruebas
  `test_01`–`test_04`). Dependencia «Habilita para P152–P154» (esquema del
  mart).
- **Alternativas menores descartadas:** declarar en markdown que `dim_date` no
  es un calendario completo aclara el límite, pero no permite ver su efecto
  sobre una medida por día ni sobre los períodos vacíos.
- **Contrato de no regresión:** se conservan H01–H04, las cuatro tablas de
  `sales_mart.db` con sus nombres, la conservación de hechos (H02), la
  integridad referencial y `region_category_sales.csv` con su consulta. `dim_date`
  conserva su clave y sus columnas actuales y gana filas (todos los días del
  rango) y columnas; toda clave de fecha del hecho sigue existiendo en la
  dimensión. No se modifica `data/sales_mart.db` ni `professor/generate_data.py`:
  si el profesor decide extender `build_mart` para que P152–P154 lean el
  calendario completo, es una decisión de bloque aparte.
- **Interacciones:** habilita P152 T02 (comparaciones entre períodos). Con
  P150 T01: el calendario uniforme del generador hace que la variación entre
  meses sea ruido; el calendario completo no lo corrige, pero hace visible la
  densidad real de días con ventas, que es precisamente la evidencia de ese
  límite. Con N01 (dimensiones de cambio lento, `course_tasks.md`): ambas
  tocan el diseño de dimensiones del mart; si N01 se aprueba, conviene
  decidir juntas la posición y el caso.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que
  `dim_date` es un calendario continuo entre la primera y la última fecha del
  hecho, con atributos de calendario adicionales, y una comparación
  persistida entre una medida por día calendario y la misma medida por día
  con ventas (más el número de días sin ventas), respaldada por notebook, un
  CSV en `submission/` y pruebas. H01–H04 siguen presentes.

### Instrucciones de ejecución

```text
Actividad: implementation/descriptiva/P151_ventas_mart/

0. Inspecciona primero professor/notebook.ipynb, professor/generate_data.py,
   data/, submission/ y tests/. Si dim_date ya es un calendario continuo, o
   si la implementación no coincide con
   design/courses/descriptiva/P151_activity.md, detente e informa.
1. No cambies el hecho, dim_customer, dim_product, la consulta en estrella ni
   region_category_sales.csv. No modifiques data/ ni
   professor/generate_data.py.
2. Reemplaza la construcción de dim_date por un calendario continuo con
   pandas.date_range entre la fecha mínima y la máxima del hecho:
   - conserva la clave y las columnas actuales de dim_date;
   - añade trimestre, semana ISO, día de la semana y un indicador de fin de
     semana (no inventes festivos: si el profesor no aporta un calendario
     de festivos, omite esa columna y dilo en markdown);
   - añade una fila para fecha desconocida sólo si el hecho la necesita.
   Verifica con assert que toda clave de fecha del hecho existe en dim_date.
3. Añade una celda de evidencia visual: tabla de días por mes con y sin
   ventas, y una comparación de ventas netas promedio por día calendario
   frente a por día con ventas, por mes.
4. Explica en markdown, en 3–5 líneas, por qué una dimensión derivada del
   hecho oculta los días sin actividad y qué medidas sesga.
5. Persiste submission/calendar_coverage.csv con columnas year, month,
   calendar_days, days_with_sales, net_sales, net_sales_per_calendar_day,
   net_sales_per_sales_day.
6. Actualiza tests/: amplía la lista de archivos esperados con
   calendar_coverage.csv (sin quitar ninguno) y añade una prueba que
   verifique que dim_date no tiene huecos entre su mínimo y su máximo, que
   contiene todas las fechas del hecho y que calendar_coverage.csv suma las
   ventas netas del hecho. No elimines pruebas existentes.
7. Ejecuta el notebook completo y las pruebas sin errores.
8. No modifiques otras actividades, traceability.yaml ni design/.
```
