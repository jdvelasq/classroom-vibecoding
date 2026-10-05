# P410 — Repositorio remoto en GitHub: publicar el historial de la tarjeta de producto

## Actividad actual implementada

**Implementación:** `implementation/productos/P410_github_remote/`.

### Preguntas analíticas actuales

- ¿Cómo se publica el historial de la definición de un producto analítico en un repositorio remoto propio, sin exponer credenciales ni tocar el repositorio del curso?

`HOW_TO_RUN_ME.txt` pide crear en GitHub un repositorio personal vacío `p410-github-remote` (sin README, `.gitignore` ni licencia), crear en `temp/github_remote_case` un repositorio con un commit de `product_card.md`, agregar `origin`, ejecutar `git push -u origin main` y `git branch -vv`, y comprobar en GitHub el archivo y el commit. La tarjeta está completa: producto `factory_totals`, consumidor «equipo de operaciones», métrica «producción acumulada» y unidad definida. La evidencia es `git log --oneline -1` local: `60a3756 chore: create product card`. `data/github_remote_case.bundle` (479 bytes) no se menciona en las instrucciones.

### Producto analítico actual y límite de identidad

- **Pregunta, usuario o decisión:** publicar la definición del producto en un remoto personal; consumidor en la tarjeta: «equipo de operaciones».
- **Producto terminal:** repositorio remoto con la tarjeta, evidenciado por una línea de log local.
- **Uso y límite:** prepara un remoto sobre el que se trabajará en P411 y P415. La evidencia persistida no demuestra que el push ocurrió ni identifica el remoto.
- **Disciplinas contribuyentes:** Git remoto y GitHub al servicio de compartir la definición del producto.

### Highlights de contribución

- **H01 — Enlaza el historial local con un remoto y su rama de seguimiento:** `git remote add origin`, `git remote -v`, `git push -u origin main` para asociar `main` con `origin/main`, y `git branch -vv` para verificar la asociación; la creación del repositorio vacío evita historiales divergentes. Primera publicación remota del curso. Sin este hito, P411 y P415 no tendrían el remoto sobre el que trabajan.
- **H02 — Separa credenciales del repositorio:** «complete el proceso en el navegador. No escriba contraseñas en el código ni en archivos del taller»; el remoto es personal del estudiante y no compartido. Primera regla explícita sobre credenciales en el curso, sólo como instrucción. Sin este hito, la publicación no tendría ninguna salvaguarda declarada.
- **H03 — Publica una tarjeta completa con evidencia sólo local (caso y datos, límite):** la tarjeta publicada reúne producto, consumidor, métrica y unidad, el contrato más completo hasta aquí; el caso no añade otra particularidad. `submission/git_log.txt` es la salida de un `git log` local, igual a la que existiría sin push. Sin este hito se ignoraría que la evidencia no cubre la operación remota que define el taller.

### Inventario técnico de implementación

- **Introduce:** creación de repositorio en GitHub; `git remote add`, `git remote -v`, `git push -u`, `git branch -vv`.
- **Reutiliza:** repositorio aislado en `temp/`, rama inicial `main` y tarjeta de producto (P408–P409).

### Índice de comparación externa

| Ancla actual | Hitos relacionados | Mecanismo, dato o producto ya observable | Evidencia y límite |
| --- | --- | --- | --- |
| Remoto con seguimiento | H01 | `push -u` + `branch -vv` | No persistido. |
| Credenciales fuera del repositorio | H02 | Autenticación en navegador | Sólo instrucción. |
| Tarjeta publicada | H03 | Cuatro campos del producto | Evidencia local. |

### Relación técnica con actividades anteriores

Misma tarjeta que P408–P409 con nueva práctica (remoto). Restituye el consumidor «equipo de operaciones» de P408, distinto del de P409. Inicia una cadena de repositorio que P411 y P415 copian.

### Evidencia de los highlights

| Highlight | Superficie(s) vinculada(s) | Rutas de respaldo | Límite de inferencia |
| --- | --- | --- | --- |
| H01 — Remoto | S02 | `implementation/productos/P410_github_remote/HOW_TO_RUN_ME.txt` | No hay evidencia persistida del push. |
| H02 — Credenciales | S02 | `implementation/productos/P410_github_remote/HOW_TO_RUN_ME.txt` | No se verifica. |
| H03 — Tarjeta y evidencia local | S01, S03, S04 | `implementation/productos/P410_github_remote/data/repository_template/product_card.md`; `implementation/productos/P410_github_remote/submission/git_log.txt`; `implementation/productos/P410_github_remote/tests/test_activity.py` | La línea de log no distingue local de remoto. |

### Superficies de cambio para revisión posterior

| ID | Componente actual | Rutas afectadas | Restricción observable |
| --- | --- | --- | --- |
| S01 | Tarjeta de producto | `data/repository_template/product_card.md` | Cuatro campos. |
| S02 | Instrucciones | `HOW_TO_RUN_ME.txt` | Requiere cuenta de GitHub. |
| S03 | Evidencia | `submission/git_log.txt` | Log local de un commit. |
| S04 | Prueba | `tests/test_activity.py` | Sólo existencia. |
| S05 | Material auxiliar | `data/github_remote_case.bundle` | No referido por las instrucciones. |

### Contrato de evidencia actual

- **Notebook o código:** no hay código; secuencia en `HOW_TO_RUN_ME.txt`.
- **`submission/`:** `git_log.txt` con un commit.
- **Pruebas:** `tests/test_activity.py::test_01` sólo exige que exista `git_log.txt`; no verifica remoto, push ni seguimiento.
- **Trazabilidad:** `productos.C02` y `productos.C04`.

### Dependencias en la secuencia

- **Recibe de P408–P409:** tarjeta de producto y prácticas de commit y rama `main`.
- **Habilita para P411:** P411 copia `../P410_github_remote/temp/github_remote_case` y usa el mismo remoto personal (y P415 continúa esa cadena).

## Trazabilidad y auditoría

Entrada revisada: P410 → `productos.C02`, `productos.C04`. C02 se sostiene por la publicación del historial; C04 sólo por la instrucción sobre credenciales y la elección privado/público, sin control de acceso ejercitado. El producto publicado es identificable; el taller se lee como práctica de GitHub (pregunta de auditoría 5).
