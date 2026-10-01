from pathlib import Path


def test_01():
    activity_dir = Path(__file__).resolve().parents[1]
    submission_dir = activity_dir / "submission"

    for filename in [
        "cluster-selection.csv",
        "demanda-comercial-clusters.csv",
        "demanda-comercial-dias.csv",
        "demanda-comercial-patrones-ejemplo.png",
        "demanda-comercial-perfiles.png",
        "demanda-comercial.png",
        "metrics.json",
        "pattern_classifier.pkl",
        "perfil-recibido.csv",
    ]:
        assert (submission_dir / filename).is_file()
