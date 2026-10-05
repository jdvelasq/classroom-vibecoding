# P453 — Propuestas de mejora

**Línea base:** `P453_activity.md` (entrada S02 más reciente: `S02.P453.01`).

## T01 — Reemplazar el identificador por un seudónimo con clave secreta y distinguir enmascarar, seudonimizar y anonimizar

- **Estado:** pendiente de discusión
- **Tipo:** producto/evidencia
- **Fuentes:**
  - `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` p. 84 — en «DPSIA/DP-Social Responsibility», habilidades T1 «Demonstrate awareness about data sensitiveness when data is processed as an input» y «Apply techniques to provide data privacy during raw data processing, such as provide ranges or salting techniques»: proteger los datos sensibles durante su procesamiento con técnicas como la sal (Claude, 2026-10-05). Fuente *authoritative*: respalda aplicar una técnica de privacidad con sal o clave sobre el identificador; la distinción entre enmascarar, seudonimizar y anonimizar no aparece en el documento y es contenido conceptual de esta propuesta, no de la fuente.
- **Qué gana el estudiante:** reemplazar el identificador directo por un
  seudónimo estable derivado con una clave secreta que no está en el código
  (HMAC-SHA-256), de modo que el consumidor pueda seguir reconociendo los
  registros del mismo cliente sin recibir el identificador, y nombrar en el
  producto qué protege cada técnica y qué no: el correo enmascarado conserva
  el dominio; el seudónimo es reidentificable para quien tiene la clave; y
  ninguna de las dos cosas permite afirmar anonimización. Corrige el límite
  que S02 registra: `customer_id` queda en claro y el producto «no permite
  afirmar anonimización» (H01; S03).
- **Materialidad frente al riesgo de identidad de S02 (objeción):** es la
  propuesta más débil de este lote. S02 dejó abierta la pregunta 5 de
  auditoría para P453: el caso cambia a clientes con una sola fila, el
  `risk` de cliente no se define ni se produce en el curso y la actividad
  «puede leerse como ejercicio genérico de enmascaramiento». Añadir una
  segunda técnica de privacidad sobre ese mismo caso refuerza la lectura de
  taller de técnicas, no la operación de una capacidad analítica. El
  beneficio analítico que justificaría seudonimizar en lugar de suprimir el
  identificador (poder unir registros del mismo cliente) no se ejerce: hay
  una sola fila y ningún consumidor del curso une por cliente. La parte que
  sí corrige un defecto es el contraste explícito de lo que el producto
  protege; la parte técnica (HMAC) pule una práctica. Recomendación para la
  discusión: decidir primero la discontinuidad de caso que S02 registra
  (clientes frente a fábricas) y, si se mantiene el caso, aprobar esta T01
  sólo con el contraste documentado como producto, no como ejercicio de
  función hash.
- **Anclas actuales:** H01 (dato personal en salida; límite «`customer_id`
  en claro»), H02 (regla de correo verificada); superficies S02
  (`professor/main.py`: sólo correo), S03 (`submission/masked_report.json`:
  `customer_id` en claro), S04 (pruebas) y S05 (sin instrucciones de
  ejecución). Dependencia nueva de práctica: **Recibe de P427** la lectura
  de un secreto desde una variable de ambiente con falla explicable si
  falta (P427 H01–H02). La dependencia se sostiene: P427 precede a P453, no
  hay artefacto que consumir y el mecanismo es el mismo; además da a esa
  práctica un uso con algo que proteger, que S02 echa en falta en P427
  («La credencial no protege ni habilita nada»). La clave debe ser una
  variable propia, no `ANALYTICS_API_KEY`: cada secreto sirve a un
  propósito.
- **Alternativas menores descartadas:** declarar en texto que el
  identificador queda en claro ya lo hace S02 y no cambia el producto.
  Suprimir `customer_id` sin reemplazo protegería más pero eliminaría la
  posibilidad de reconocer al mismo cliente, que es precisamente el
  contraste que distingue seudonimizar de suprimir. Un hash sin clave del
  identificador sería reversible por fuerza bruta sobre identificadores
  pequeños (`customer_id` 1) y enseñaría una práctica errónea.
- **Contrato de no regresión:** se conservan H02, `mask_email` y su prueba,
  `risk` intacto y `data/customers.csv` sin cambios (no se añaden filas
  inventadas). H01 se modifica en su límite: `customer_id` deja de aparecer
  en la salida y se sustituye por `customer_pseudonym`. Esa sustitución de
  una clave de `masked_report.json` es explícita y se justifica por el
  defecto que S02 registra; aprobar esta T01 aprueba esa sustitución. Si
  una prueba existente exige `customer_id` en claro, sólo esa aserción se
  adapta a `customer_pseudonym` y S04 lo informa. Las demás pruebas se
  mantienen sin cambios.
- **Interacciones:** ninguna otra `Txx` en este archivo. Depende de la
  práctica de P427 (secreto por variable de ambiente); no modifica P427.
  No resuelve la discontinuidad de caso con P450–P452. Capacidad: cambio
  local (nivel 2) más un `HOW_TO_RUN_ME.txt` que hoy no existe; cabe en la
  sesión, pero suma un segundo mecanismo a un taller de dos highlights.
- **Criterio de aceptación:** S05 encuentra un highlight nuevo en el que
  `submission/masked_report.json` no contiene el identificador original y
  sí un `customer_pseudonym` derivado con HMAC-SHA-256 y una clave leída de
  una variable de ambiente propia (no presente en el código ni en
  `submission/`), junto con una declaración breve de lo que protege cada
  técnica aplicada y de que el reporte no está anonimizado; y pruebas que
  verifican que el mismo identificador con la misma clave produce el mismo
  seudónimo, que otra clave produce otro, que la ausencia de la variable
  produce un error explicable y que el identificador original no aparece en
  la salida. H02 sigue presente.

### Instrucciones de ejecución

```text
Actividad: implementation/productos/P453_data_masking/

0. Inspecciona primero data/customers.csv, professor/main.py,
   professor/test_main.py, src/main.py, submission/ y tests/, y como
   referencia de práctica implementation/productos/P427_secret_config/
   (professor/main.py y HOW_TO_RUN_ME.txt). Si P453 no coincide con
   design/courses/productos/P453_activity.md (una fila, mask_email,
   customer_id y risk sin cambios), o si P427 no lee su secreto con
   os.environ y RuntimeError explicable, detente e informa sin modificar
   nada. Si alguna prueba existente exige customer_id en claro en la
   salida, adapta sólo esa aserción a customer_pseudonym (sustitución
   aprobada con esta T01) e infórmalo; no toques otras aserciones.
1. Si P453_log.md registra que el profesor decidió primero cambiar o
   retirar el caso de clientes, detente: esta T01 queda condicionada a esa
   decisión.
2. No cambies data/customers.csv ni añadas filas. No modifiques mask_email
   ni el tratamiento de risk.
3. En professor/main.py:
   a. añade get_pseudonymization_key() que lea la variable
      PSEUDONYMIZATION_KEY con os.environ.get y lance RuntimeError que
      nombre la variable si falta o está vacía (mismo patrón que P427; no
      reutilices ANALYTICS_API_KEY);
   b. añade pseudonymize(identifier, key) =
      hmac.new(key, identifier, hashlib.sha256).hexdigest() (bytes UTF-8);
   c. en create_masked_report reemplaza customer_id por customer_pseudonym;
      añade "protection": un objeto breve con, por campo, la técnica
      aplicada y lo que no protege (email: enmascarado, conserva inicial y
      dominio; customer_pseudonym: seudónimo con clave, reidentificable con
      la clave, estable para reconocer al mismo cliente) y "anonymized":
      false.
   Ninguna clave real ni de ejemplo puede quedar escrita en main.py.
4. Crea HOW_TO_RUN_ME.txt siguiendo el de P427: export de
   PSEUDONYMIZATION_KEY con un valor declarado como de práctica, ejecución,
   unset. Regenera submission/masked_report.json con esa clave de práctica.
   El valor de la clave no debe aparecer en submission/.
5. Añade a professor/test_main.py pruebas (con monkeypatch.setenv/delenv,
   como P427) que verifiquen: el mismo identificador y la misma clave dan
   el mismo seudónimo; otra clave da otro; sin la variable se lanza
   RuntimeError que nombra PSEUDONYMIZATION_KEY; el reporte no contiene
   customer_id ni el valor original del identificador; "anonymized" es
   false. Añade a tests/test_activity.py una prueba que verifique que
   masked_report.json entregado no tiene la clave customer_id, tiene
   customer_pseudonym de 64 caracteres hexadecimales y declara
   "anonymized": false. No elimines pruebas existentes; la única
   modificación permitida es la del paso 0.
6. Ejecuta main() según HOW_TO_RUN_ME.txt y todas las pruebas de la
   actividad sin errores.
7. No modifiques src/main.py (plantilla del estudiante), P427 ni otras
   actividades, traceability.yaml ni design/.
```
