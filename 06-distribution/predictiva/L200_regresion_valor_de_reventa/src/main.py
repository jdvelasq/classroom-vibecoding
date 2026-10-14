"""Estima el valor de reventa de vehículos usados."""


def main():
    """
    Un concesionario de vehículos usados quiere estimar a qué precio podrá
    revender un carro antes de ofrecerlo, a partir de información que conoce
    al recibirlo. Los archivos `data/train_data.csv.gz` (211 vehículos) y
    `data/test_data.csv.gz` (90 vehículos) tienen una fila por vehículo, con
    el modelo (`Car_Name`), el año de fabricación (`Year`), el precio de
    reventa (`Selling_Price`), el precio del vehículo nuevo
    (`Present_Price`), el kilometraje (`Driven_kms`), el combustible
    (`Fuel_Type`), el tipo de vendedor (`Selling_type`), la transmisión
    (`Transmission`) y el número de propietarios anteriores (`Owner`). Los
    precios están en lakhs de rupias. Los datos se recolectaron en 2021.

    Construya un modelo de regresión que estime `Selling_Price`. Entrénelo
    solamente con el conjunto de entrenamiento y use el conjunto de prueba
    únicamente para evaluarlo. Usted decide qué variables usar y cómo
    transformarlas, pero no puede usar `Selling_Price` como entrada.

    Genere tres archivos en `submission/`:

    1. `test_predictions.csv`, sin el índice de Pandas, con una fila por
       vehículo del conjunto de prueba, en el mismo orden del archivo, y las
       columnas `actual_price` (el `Selling_Price` observado) y
       `predicted_price` (la estimación del modelo).

    2. `metrics.json`, con dos llaves: `test_mae`, el error absoluto medio
       sobre el conjunto de prueba, y `test_r2`, el coeficiente de
       determinación R² sobre el mismo conjunto.

    3. `model.pkl`, con el modelo entrenado guardado con `pickle`.

    Escriba su solución en la función `main()`, que debe generar los tres
    archivos al ejecutarse.

    Ejemplo del formato de `test_predictions.csv`:

        actual_price,predicted_price
        4.75,6.9533
        7.25,7.4968
        ...

    Ejemplo del formato de `metrics.json`:

        {
          "test_mae": 1.4542,
          "test_r2": 0.7898
        }
    """

    raise NotImplementedError


if __name__ == "__main__":
    main()
