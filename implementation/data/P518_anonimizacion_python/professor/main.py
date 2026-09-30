import json
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SOURCE = ACTIVITY_DIR / "data" / "superstore_orders.csv"
SUBMISSION = ACTIVITY_DIR / "submission"


def main():
    sales = pd.read_csv(SOURCE, sep=";", encoding="latin1", decimal=",")
    sales.columns = [column.removeprefix("ï»¿") for column in sales.columns]
    shared = (
        sales.groupby(["Customer Segment", "Region", "Product Category"], as_index=False)
        .agg(sales=("Sales", "sum"), profit=("Profit", "sum"), order_lines=("Sales", "size"))
        .sort_values(["sales", "profit"], ascending=False)
    )
    assert not {"Customer ID", "Customer Name", "Postal Code", "City"} & set(shared.columns)
    shared.to_csv(SUBMISSION / "shared_sales.csv", index=False)
    (SUBMISSION / "questions.json").write_text(json.dumps([{"pregunta":"¿Cómo compartir ventas por segmento, región y categoría sin exponer identificadores de clientes?","archivo_respuesta":"shared_sales.csv"}], ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
