"""Completa el sentimiento faltante en reseñas reales de Amazon."""


def main():
    """
    Una tienda en línea recibió miles de reseñas de teléfonos celulares y
    accesorios, pero solo una pequeña parte fue etiquetada a mano como
    positiva o negativa. Se necesita completar la etiqueta de las demás. El
    archivo `data/amazon_cells_labelled.tsv` tiene 14.609 reseñas, una por
    línea, en dos columnas separadas por tabulador y sin encabezado: el texto
    de la reseña y su sentimiento (1 si es positiva y 0 si es negativa). Solo
    1.000 reseñas tienen el sentimiento; en las demás la segunda columna está
    vacía.

    Construya un clasificador de texto entrenado con las reseñas etiquetadas
    y úselo para completar el sentimiento de las reseñas que no lo tienen.
    Las etiquetas observadas no deben cambiar.

    Genere dos archivos en `submission/`:

    1. `completed_reviews.csv`, sin el índice de Pandas, con todas las
       reseñas del archivo original, en el mismo orden, y las columnas
       `review` (el texto) y `sentiment` (0 o 1, como número entero). Ninguna
       fila puede quedar sin sentimiento.

    2. `model.pkl`, con el clasificador entrenado guardado con `pickle`. El
       modelo debe recibir una lista de textos y retornar el sentimiento de
       cada uno.

    Escriba su solución en la función `main()`, que debe generar los dos
    archivos al ejecutarse.

    Ejemplo del formato de `completed_reviews.csv`:

        review,sentiment
        I try not to adjust the volume setting to avoid that I turn ...,0
        So there is no way for me to plug it in here in the US unless ...,0
        "Good case, Excellent value.",1
        ...
    """

    raise NotImplementedError


if __name__ == "__main__":
    main()
