"""Evalúa los productos bibliométricos del caso Scopus."""

from pathlib import Path

import pandas as pd


OUT = Path("submission")
EXPECTED = {"authors_frequency.csv", "country_clusters.txt", "country_collab_network.html", "country_cooc_heatmap.html", "country_cooc_matrix.csv", "country_frequency.csv", "country_frequency_plot.html", "documents_by_year.html", "keywords_clusters.txt", "keywords_cooc_matrix.csv", "keywords_cooc_network.html", "keywords_frequency.csv", "scopus.csv.gz", "source_frequency.csv", "world_map.html"}


def test_01():
    assert {path.name for path in OUT.iterdir() if path.name != ".gitkeep"} == EXPECTED


def test_02():
    source = pd.read_csv("data/scopus.csv.gz")
    delivered = pd.read_csv(OUT / "source_frequency.csv")
    assert delivered.iloc[:, 1].sum() == source["Abbreviated Source Title"].fillna("").str.strip().ne("").sum()
    assert delivered.iloc[:, 1].is_monotonic_decreasing
    assert pd.read_csv(OUT / "authors_frequency.csv").iloc[:, 1].sum() >= len(source)


def test_03():
    for name in {"country_frequency.csv", "keywords_frequency.csv", "country_cooc_matrix.csv", "keywords_cooc_matrix.csv"}:
        assert not pd.read_csv(OUT / name).empty
    for name in {"documents_by_year.html", "country_frequency_plot.html", "world_map.html", "country_collab_network.html", "country_cooc_heatmap.html", "keywords_cooc_network.html"}:
        assert (OUT / name).stat().st_size > 1_000
