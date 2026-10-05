# Log — P421

## S02.P421.01

- **Fecha:** 2026-10-04; **curso / executor:** `productos` / `Claude`; **estado:** inicial.
- **Rutas inspeccionadas:** `implementation/productos/P421_model_registry/` (`CANDIDATES.json`, `CANDIDATE_V1.pkl` (sólo tamaño), `HOW_TO_RUN_ME.txt`, `professor/main.py`, `professor/test_main.py`, `src/main.py`, `submission/model_registry/production/`, `tests/test_activity.py`); digests de P406, P407, P420, P424, P448.
- **Trazabilidad revisada:** P421 → `productos.C02`, `C03`, `C05`; C03 sin evidencia.
- **Highlights:** añadidos H01 (promoción separada de la construcción), H02 (identificador estable con rechazo verificado) y H03 (artefacto sin procedencia; caso y datos como límite).
- **Ambigüedades:** origen de `CANDIDATE_V1.pkl` y de la exactitud 0.91 no declarados; mismo tamaño (203183 bytes) que `ESTIMATOR.pkl` de P406–P407 y modelos de P424. La promoción sobrescribe sin historial. No consume corridas de P420 ni alimenta P424.
- **Superficies / contrato / dependencias:** S01–S05; recibe: sólo prácticas; habilita: no evidenciada.
- **Auditoría de Analytics:** no resuelta; registro genérico sin capacidad analítica identificable.
