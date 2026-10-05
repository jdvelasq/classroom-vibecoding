# Log — P108

## S02.P108.01

- **Fecha:** 2026-10-04; **curso / executor:** `descriptiva` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/descriptiva/P108_anonimizacion_pandas/` (`data/raw.csv`, `data/auxiliary.csv`, `professor/notebook.ipynb`, `notebooks/notebook.ipynb`, `submission/anonymized.csv`, `tests/`). Comparado con P102 y P103.
- **Trazabilidad revisada:** entrada P108 → `descriptiva.C05`.
- **Highlights añadidos:** H01 (roles de riesgo de columnas; highlight de caso y datos), H02 (insuficiencia de la supresión ante enlace), H03 (técnicas diferenciadas), H04 (generalización con riesgo residual por paso), H05 (costo en utilidad), H06 (contrato del conjunto compartible). No inferibles: conteos de reidentificación (no persistidos ni visibles).
- **Ambigüedades:** clave HMAC escrita en el notebook; en las filas visibles los números de tarjeta son secuenciales y sus cuatro dígitos conservados identifican cada registro; `annual_spend` exacto; riesgo evaluado sólo contra 20 perfiles, sin garantía formal; procedencia no documentada.
- **Superficies / contrato / dependencias:** S01–S06; recibe de P102/P103; habilita P109 (mismos datos, reglas, seudónimo y prueba).
- **Auditoría de Analytics:** producto = capacidad de datos compartible con riesgo y utilidad explícitos; C05 sustentado en su dimensión responsable. Domina la privacidad de datos como disciplina contribuyente.

## S03.P108.01

- **Fecha / executor:** 2026-10-04 / Claude.
- **Documento:** `design/benchmarks-md/authoritative/acm-computing-competencies-undergraduate-data-science-2021.md` (`source_sha256`: eaa9929c6b74446c34ff054292d1c7423b7807fd5c059132fb33edfe45570483).
- **Resultado:** sin cambios.
- **Señales descartadas relevantes:**
  - técnicas de privacidad en datos crudos «provide ranges or salting techniques» (DP-Social Responsibility, p. 84); funciones *hash* (DP-Cryptography, p. 85); tensión transparencia–privacidad (DP-Information Systems, p. 85) — ya cubierta: P108 H03 (`pd.cut`, HMAC con clave), H04–H05 (riesgo frente a utilidad). La clave HMAC escrita en el notebook (P108 S02) es un defecto real ya registrado por S02. ACM no aporta un argumento específico de gestión de secretos, por lo que no justifica aquí una propuesta propia.
