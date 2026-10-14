"""Reconstruye métricas de conversión preservando el tiempo de los eventos."""

# ¿Cuántas sesiones convierten y qué ingreso representan sin confundir el orden de llegada con el comportamiento real?

import csv
import gzip
from collections import defaultdict
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def read_events():
    with gzip.open(DATA_DIR / "events.csv.gz", "rt", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def replay_arrivals(events):
    arrived_events = []
    for start in range(0, len(events), 8):
        batch = events[start : start + 8]

        # Una fuente distribuida puede entregar una parte antigua después del resto del lote.
        arrived_events.extend(batch[2:] + batch[:2])
    return arrived_events


def mark_late_events(events):
    latest_event_time = ""
    replay = []
    for arrival_position, event in enumerate(events, 1):
        is_late = event["event_time"] < latest_event_time
        latest_event_time = max(latest_event_time, event["event_time"])
        replay.append({"arrival_position": arrival_position, **event, "is_late": is_late})
    return replay


def summarize_sessions(replay):
    sessions = defaultdict(lambda: {"event_count": 0, "late_event_count": 0, "revenue": 0.0})
    for event in replay:
        session = sessions[event["user_session"]]
        session["event_count"] += 1
        session["late_event_count"] += int(event["is_late"])
        if event["event_type"] == "purchase":
            session["revenue"] += float(event["price"])

    return [
        {
            "user_session": session_id,
            "event_count": session["event_count"],
            "late_event_count": session["late_event_count"],
            "converted": session["revenue"] > 0,
            "revenue": round(session["revenue"], 2),
        }
        for session_id, session in sorted(sessions.items())
    ]


def write_csv(path, rows, fieldnames):
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    events = read_events()
    replay = mark_late_events(replay_arrivals(events))
    sessions = summarize_sessions(replay)

    write_csv(
        SUBMISSION_DIR / "event_replay.csv",
        replay,
        ["arrival_position", "event_time", "event_type", "product_id", "category_id", "category_code", "brand", "price", "user_id", "user_session", "is_late"],
    )
    write_csv(
        SUBMISSION_DIR / "session_conversion.csv",
        sessions,
        ["user_session", "event_count", "late_event_count", "converted", "revenue"],
    )

    converted_sessions = sum(session["converted"] for session in sessions)
    summary = [
        {"metric": "event_count", "value": len(replay)},
        {"metric": "late_event_count", "value": sum(event["is_late"] for event in replay)},
        {"metric": "session_count", "value": len(sessions)},
        {"metric": "converted_session_count", "value": converted_sessions},
        {"metric": "conversion_rate", "value": round(converted_sessions / len(sessions), 4)},
    ]
    write_csv(SUBMISSION_DIR / "event_summary.csv", summary, ["metric", "value"])


if __name__ == "__main__":
    main()
