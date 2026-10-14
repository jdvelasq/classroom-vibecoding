"""Pronostica la demanda máxima diaria de electricidad."""


def main():
    """
    El operador del sistema eléctrico necesita anticipar el pico diario de
    demanda para programar la generación. El archivo
    `data/demanda_comercial.csv.gz` tiene una fila por día, desde el
    2017-01-01 hasta el 2022-08-31, con la fecha (`Fecha`) y la demanda
    comercial de cada una de las 24 horas del día (`H01`, `H02`, ...,
    `H24`).

    Use estas definiciones:

    - Pico diario (`actual_peak`): la mayor demanda horaria del día.
    - Conjunto de entrenamiento: el primer 80 % de los días, en orden
      cronológico (redondee la cantidad de días hacia abajo). Conjunto de
      prueba: los días restantes.
    - Pronóstico base (`baseline_forecast`): el pico diario promedio del
      conjunto de entrenamiento, igual para todos los días de prueba.
    - Pronóstico por día de la semana (`weekday_forecast`): el pico diario
      promedio de los días del conjunto de entrenamiento que caen en el
      mismo día de la semana que el día pronosticado.

    Genere dos archivos en `submission/`:

    1. `forecast.csv`, sin el índice de Pandas, con una fila por día del
       conjunto de prueba, en orden cronológico, y las columnas `Fecha` (en
       formato `AAAA-MM-DD`), `actual_peak`, `baseline_forecast` y
       `weekday_forecast`.

    2. `metrics.json`, con dos llaves: `baseline_mae` y `weekday_mae`, el
       error absoluto medio de cada pronóstico sobre el conjunto de prueba.

    Escriba su solución en la función `main()`, que debe generar los dos
    archivos al ejecutarse.

    Ejemplo del formato de `forecast.csv`:

        Fecha,actual_peak,baseline_forecast,weekday_forecast
        2021-07-14,10185785.87,9361644.7507,9636851.2230
        2021-07-15,10199084.8,9361644.7507,9639853.9742
        ...

    Ejemplo del formato de `metrics.json`:

        {
          "baseline_mae": 746571.3821,
          "weekday_mae": 682405.6048
        }
    """

    raise NotImplementedError


if __name__ == "__main__":
    main()
