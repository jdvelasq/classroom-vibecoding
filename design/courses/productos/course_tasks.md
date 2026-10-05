# productos — Actividades nuevas por decidir

## N01 — ⚠️ PENDIENTE DE DECISIÓN — Contrato operativo de una capacidad analítica

- **Fuentes:**
  - `design/benchmarks-md/authoritative/informs-analytics-framework-2024.md` p. 7 — «Task 6.4 Create requirements for a deployed analytics solution, including model, usability, system, and business»; p. 5 — «Task 2.4 Define primary measures of success» y «Task 2.5 Identify baseline performance of the current state»; p. 7 — «Task 7.6 Ensure documentation is complete and/or maintained»: antes de desplegar se declaran los requisitos de la solución separados en modelo, usabilidad, sistema y negocio, con una medida de éxito y una línea base del estado actual, y esa documentación se mantiene (Claude, 2026-10-05). Fuente *authoritative*: respalda la expectativa general de declarar el contrato antes de operar, no un temario ni un formato.
- **Contribución distinta:** el estudiante redacta, para una capacidad
  analítica real, el contrato operativo completo que define
  `productos.C01` en `s05-diseno-productos.md`: usuarios, decisión que
  apoya, entradas, salidas, límites, nivel de servicio y criterios de
  éxito. Siguiendo Task 6.4, separa los requisitos de modelo, usabilidad,
  sistema y negocio. Siguiendo Tasks 2.4–2.5, el criterio de éxito tiene
  una medida, un umbral y la línea base del estado actual con su origen.
  Hoy ningún taller produce ese contrato y C01 aparece fragmentada:
  - tarjeta de tres a cinco campos en P408–P411 (P408 H01: «primer esbozo
    de contrato operativo»; P411 H02: producto, consumidor, métrica,
    unidad y responsable, sin entradas, límites ni nivel de servicio);
  - contrato de interfaz en P425 (H01: entrada, salida y error, sin usuario
    ni decisión, H03);
  - versión de contrato en P434 (H01: compatibilidad declarada, sin
    consumidor ni registros);
  - meta de servicio en P445 (H02: meta 0.95 «acordada» sin capacidad,
    periodo ni autor);
  - ficha operacional en P454 (H01: dueño, frecuencia, versión y consumidor
    escritos a mano y copiados).

  Las auditorías S02 de P425, P434 y P445 registran que esos talleres son
  evidencia natural de C01 y que C01 no está mapeada en ellos (P425_log,
  P434_log, P445_log), y la de P454 registra que la ficha no se verifica
  contra el producto.

  **Por qué no se incrusta en un taller existente.** Cada uno ya tiene una
  contribución propia y el contrato completo sería una segunda
  contribución (criterio 3):
  - P425 enseña la frontera verificable de una interfaz: validación,
    errores explicables y ejemplos ejecutados (H01–H02).
  - P434 enseña la decisión de integración por compatibilidad declarada.
  - P445 enseña un indicador de servicio con borde de meta probado.
  - P454 enseña la ficha de gobierno de un dataset.
  - P408 enseña el ciclo de commit de Git. Ampliar su tarjeta fue la
    alternativa menor considerada en la señal y se descarta porque convierte
    la primera práctica de Git en un taller de encuadre operativo.

  Además, el contrato es lógicamente anterior a todos ellos. P425 debería
  exponer las entradas y salidas que el contrato declara, P434 debería
  versionarlo, P445 debería evaluar la meta que fija y P454 debería
  resumirlo. Incrustarlo en cualquiera de ellos lo dejaría después de los
  talleres que deberían consumirlo.
- **Posición propuesta:** al inicio del curso, antes de P400, como primer
  taller. No recibe artefactos de otra actividad de `productos`. Recibe del
  curso de origen la capacidad, su medida de desempeño y su línea base (ver
  «Caso y datos»). Habilita que los talleres siguientes operen una capacidad
  declarada en vez de un indicador sin usuario. Por ejemplo, la tarjeta de
  P408–P411 pasaría a ser la versión de ese contrato, P425 expondría sus
  entradas y salidas, P445 evaluaría su nivel de servicio y P454 lo
  resumiría. Esas adaptaciones no se proponen aquí (ver «Decisión de curso
  implicada»).

  Alternativas de posición:
  - **Antes de P408**, de modo que la tarjeta que versionan P408–P411 nazca
    del contrato. Conserva intactos P400–P407, pero los primeros ocho
    talleres siguen operando un indicador sin usuario ni decisión.
  - **Más adelante**, antes de P425, que abre el bloque de interfaz,
    contratos y servicio. Llega cuando el estudiante ya conoce la mecánica,
    pero los 25 talleres previos no tendrían contrato que consumir, y el
    contrato llegaría como recapitulación y no como punto de partida.
- **Efecto en la secuencia:** como el curso tiene 56 talleres (P400–P455),
  una actividad nueva en cualquier posición desplaza una sesión todo lo que
  queda después.
  - **Al inicio:** un grupo lento pierde el último taller al que hoy llega.
    En la secuencia actual, el riesgo cae sobre el bloque final P450–P455
    (revisión humana, retroalimentación, control de acceso, enmascaramiento,
    catálogo y retención), y P454 es justamente uno de los fragmentos de
    C01. A cambio, todo grupo ejerce C01.
  - **Antes de P408:** el mismo desplazamiento, con la misma pérdida al
    final del curso.
  - **Antes de P425 o más tarde:** P400–P424 no se desplazan, pero un grupo
    que no llegue a esa posición nunca produce el contrato. C01 seguiría
    sin evidencia completa para ese grupo, que es el defecto que N01
    corrige.

  La carga de justificación es la más alta del criterio 2 (actividad
  nueva). La sostiene que C01 es una capacidad terminal principal del curso
  sin un producto que la evidencie.
- **Caso y datos:** requiere definición. S02 registró que el curso opera
  hoy, como hilo principal, un indicador trivial: `factory_totals`, la suma
  de cuatro filas sin fecha ni procedencia, sin usuario ni decisión (P400
  H03). Le sigue un «riesgo por fábrica» con un umbral 4500 sin procedencia
  (P425 H03), que reaparece con datos propios en P430–P454. Un contrato
  escrito sobre ese indicador sería un ejercicio de formulario. Por eso N01
  exige una capacidad analítica real, ya construida en otro curso, con
  usuario y decisión identificables. Opciones, que debe elegir el profesor:
  - un modelo de `predictiva` cuya decisión esté encuadrada, con su medida
    de éxito y una línea base ingenua. El encuadre que propone
    `predictiva/P200` T01 sería un insumo natural si se aprueba;
  - un producto de KPI de `descriptiva` con usuario y cadencia de
    actualización;
  - una política de `prescriptiva` con su decisión y su restricción
    operativa.

  En todos los casos, el dataset debe ser trazable (preferir `datalabs/` o
  `catalog/`, según `AGENTS.md`), y el usuario, la decisión, la medida de
  éxito y el valor de línea base deben provenir del curso de origen o del
  profesor. S04 no los inventa: si no existen, se detiene y lo informa.
  N01 no reentrena ni reformula la capacidad (frontera del curso). Sólo
  declara las condiciones bajo las que se opera.
- **Decisión de curso implicada:** adoptar N01 implica una decisión de
  curso, previa a su primera versión: qué capacidad operan los talleres
  posteriores. Es el hallazgo de identidad de S02, según el cual los
  talleres se leen como capacitación en herramientas sobre un indicador
  trivial.
  - Si la capacidad del contrato es distinta de `factory_totals` y del
    riesgo por fábrica, N01 deja visible la brecha. El resto del curso
    seguiría operando otra cosa.
  - Si se decide que el bloque opere la capacidad contratada, eso es un
    rediseño del hilo del curso. No se propone aquí: corresponde a una
    discusión de curso aparte, y N01 se puede aprobar sin él, como primer
    paso.
- **Producto de Analytics:**
  - **Pregunta:** ¿para quién opera esta capacidad, qué decisión apoya y
    bajo qué condiciones se considera que cumple?
  - **Producto terminal:** un contrato operativo persistido en
    `submission/` con los siete componentes de C01 y los requisitos
    agrupados en modelo, usabilidad, sistema y negocio. Cada valor tiene su
    procedencia: la actividad del curso de origen o el texto aportado por
    el profesor. Además, declara la versión del contrato y su responsable
    de mantenimiento (Task 7.6).
  - **Límite:** declara, no verifica. El cumplimiento del nivel de servicio
    o de la medida de éxito en operación corresponde a talleres posteriores
    (P423, P445). El contrato no sustituye la interfaz de P425 ni la
    versión de P434.
- **Criterio de aceptación de una primera versión.** S05 verifica lo
  siguiente:
  - existe el trío de archivos de la nueva actividad;
  - el contrato en `submission/` nombra una capacidad de otro curso
    identificada por ruta calificada (p. ej. `predictiva/Pxxx`);
  - los siete componentes de C01 están presentes y no vacíos, cada uno con
    su procedencia;
  - el criterio de éxito tiene medida, umbral y línea base con su origen;
  - el nivel de servicio declara indicador, meta, ventana de medición y
    consecuencia del incumplimiento;
  - los límites incluyen al menos un uso no soportado;
  - los requisitos están agrupados en modelo, usabilidad, sistema y
    negocio;
  - `tests/test_activity.py` verifica esos campos en el contenido, no sólo
    la existencia del archivo;
  - un highlight «caso y datos» documenta de dónde salen el usuario y la
    decisión;
  - la entrada de `traceability.yaml` mapea `productos.C01` con evidencia
    en el contrato;
  - ningún usuario, decisión ni valor de línea base fue inventado. Si el
    profesor no los aportó, la versión no se acepta.
