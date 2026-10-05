# descriptiva — Actividades nuevas por decidir

## N01 — ⚠️ PENDIENTE DE DECISIÓN — Dimensiones de cambio lento: describir con la historia correcta

- **Fuentes:**
  - `design/benchmarks-md/authoritative/kimball-dimensional-modeling-techniques-2013.md` pp. 15–16 — «Type 1: Overwrite… this technique destroys history»; «Type 2: Add New Row… A minimum of three additional columns should be added to the dimension row with type 2 changes: 1) row effective date or date/time stamp; 2) row expiration date or date/time stamp; and 3) current row indicator»; los tipos 6 y 7 entregan a la vez la vista «as-was» y la «as-is» (Claude, 2026-10-04). Fuente *authoritative*.
  - `design/benchmarks-md/institutional/utdallas-mis-6309-business-data-warehousing-syllabus.md` p. 2 — «Slowly Changing Dimensions - Type 1, Type 2, and Type 3» y «Classroom Hands-on – Design a Type 2 SCD» en la semana 4 del curso (Claude, 2026-10-04). Fuente *institutional*.
- **Contribución distinta:** enseñar que una misma tabla de hechos puede
  describir dos realidades distintas según cómo se guarde la historia de una
  dimensión. Si un cliente cambia de región, las ventas pasadas pueden
  contarse en la región donde ocurrieron (tipo 2, «as-was») o en la región
  actual (tipo 1, «as-is»), y la respuesta a «¿qué región vende más?»
  cambia. El estudiante aprende a mantener una dimensión tipo 2 con fechas
  de vigencia e indicador de fila vigente, a unir el hecho con la versión
  correcta de la dimensión y a declarar qué pregunta responde cada vista.
  Ninguna Pxxx lo trata: P151 construye dimensiones estáticas cuyas claves
  copian los identificadores operativos (H01), y P152–P154 navegan ese mismo
  mart sin cambios en el tiempo. Incrustarlo en P151 añadiría una segunda
  contribución a un taller que construye el primer modelo dimensional del
  curso y que ya tiene una propuesta (T01).
- **Posición propuesta:** al cierre del bloque de BI, después de P154. Recibe
  de P151 el modelo estrella y la integridad referencial, de P152 la
  navegación por región y de P153–P154 el contrato de métricas y de consumo.
  No desplaza ninguna actividad existente. Alternativa: después de P151, que
  es donde se diseña el mart, pero desplazaría P152–P154 para los grupos que
  avanzan menos.
- **Efecto en la secuencia:** en la posición propuesta, un grupo que no
  termina el bloque de BI no la ve y conserva intacto lo que hoy ve. En la
  alternativa, un grupo lento perdería primero P154.
- **Caso y datos:** requiere definición. Opción de menor riesgo: extender el
  caso de ventas con un registro documentado de cambios de atributos de
  clientes (por ejemplo, cambios de región con fecha), declarado como
  derivado didáctico. Como el caso actual es sintético (P150–P154, S01), la
  decisión sobre el generador que plantea P150 T01 condiciona esta opción.
  Un caso real del catálogo con historia de dimensiones sería preferible
  según `AGENTS.md`.
- **Producto de Analytics:** pregunta descriptiva respondida con dos vistas
  del mismo hecho (histórica y actual), con la diferencia cuantificada por
  región y una lectura escrita de qué decisión corresponde a cada vista. El
  límite debe quedar explícito: ninguna vista es «la correcta» en abstracto;
  depende de la pregunta.
- **Criterio de aceptación de una primera versión:** un notebook que
  construye una dimensión de cliente tipo 2 (clave sustituta, clave
  durable, fechas de vigencia e indicador de fila vigente) a partir de los
  cambios documentados; une el hecho con la versión vigente en la fecha de
  cada venta; compara ventas por región en vista tipo 1 y tipo 2; persiste
  ambas vistas, su diferencia y la lectura en `submission/`; incluye pruebas
  (sin solapamiento de vigencias, una sola fila vigente por clave durable,
  conservación del total de ventas en ambas vistas) y entrada en
  `traceability.yaml`; y su `Pxxx_activity.md` (S02) evidencia highlights
  propios, no duplicados de P151–P154.
