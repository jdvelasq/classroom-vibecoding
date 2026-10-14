import json
import sqlite3
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
DATABASE_PATH = ACTIVITY_DIR / "submission" / "superstore_elt.db"
QUESTION = "¿Qué segmentos y regiones concentran las ventas y la utilidad?"


def load_sources(database):
    for name in ["orders", "customers", "products", "order_lines"]:
        pd.read_csv(DATA_DIR / f"{name}.csv").to_sql(
            f"raw_{name}", database, index=False, if_exists="replace"
        )


def transform_in_database(database):
    database.execute(
        """
        CREATE TABLE curated_superstore_sales AS
        SELECT lines.*, orders.`Order Date`, customers.`Customer Segment`,
               customers.Region, products.`Product Category`
        FROM raw_order_lines AS lines
        JOIN raw_orders AS orders USING(order_context_key)
        JOIN raw_customers AS customers USING(customer_context_key)
        JOIN raw_products AS products USING(product_context_key)
        """
    )
    return pd.read_sql_query(
        """
        SELECT `Customer Segment`, Region, SUM(Sales) AS sales, SUM(Profit) AS profit
        FROM curated_superstore_sales
        GROUP BY `Customer Segment`, Region
        ORDER BY sales DESC, profit DESC
        """,
        database,
    )


def main():
    DATABASE_PATH.unlink(missing_ok=True)
    with sqlite3.connect(DATABASE_PATH) as database:
        load_sources(database)
        answer = transform_in_database(database)
        raw_rows = sum(
            database.execute(f"SELECT COUNT(*) FROM raw_{name}").fetchone()[0]
            for name in ["orders", "customers", "products", "order_lines"]
        )
        curated_rows = database.execute(
            "SELECT COUNT(*) FROM curated_superstore_sales"
        ).fetchone()[0]

    submission = ACTIVITY_DIR / "submission"
    answer.to_csv(submission / "sales_by_segment_region.csv", index=False)
    pd.DataFrame(
        [("raw", raw_rows, "SUCCESS"), ("curated", curated_rows, "SUCCESS")],
        columns=["stage", "rows", "status"],
    ).to_csv(submission / "elt_report.csv", index=False)
    (submission / "questions.json").write_text(
        json.dumps([{"pregunta": QUESTION, "archivo_respuesta": "sales_by_segment_region.csv"}], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
