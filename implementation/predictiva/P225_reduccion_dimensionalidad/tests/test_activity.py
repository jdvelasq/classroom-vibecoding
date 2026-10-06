import csv
from pathlib import Path


def test_01():
    assert Path("submission/digits_pca.png").is_file()
    assert Path("submission/digits_tsne.png").is_file()
    assert Path("submission/digits_umap.png").is_file()


def test_02():
    csv_path = Path("submission/pca_components_accuracy.csv")
    assert csv_path.is_file()
    assert Path("submission/pca_components_accuracy.png").is_file()

    with csv_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    expected_columns = {"k", "explained_variance", "test_accuracy"}
    assert expected_columns.issubset(rows[0].keys())
    assert "64" in {row["k"] for row in rows}


def test_03():
    csv_path = Path("submission/umap_components_accuracy.csv")
    assert csv_path.is_file()
    assert Path("submission/components_accuracy_comparison.png").is_file()

    with csv_path.open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    expected_columns = {"k", "test_accuracy"}
    assert expected_columns.issubset(rows[0].keys())
    assert "64" in {row["k"] for row in rows}
