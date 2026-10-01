# Estas son las funciones que definimos en la actividad anterior.

import csv
import gzip
import os
import shutil
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from time import perf_counter


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ACTIVITY_DIR / "data"
TEMP_DIR = ACTIVITY_DIR / "temp"
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def map_pairs(records, mapper):
    pairs = []
    for record in records:
        pairs.extend(mapper(record))
    return pairs


def group_by_key(pairs):
    groups = {}
    for key, value in pairs:
        groups.setdefault(key, []).append(value)
    return groups


def reduce_by_key(groups, reducer):
    return [reducer(key, values) for key, values in groups.items()]


def map_flight(record):
    if record["Cancelled"] == "0":
        return [(record["Origin"], 1)]
    return []


def sum_flights(origin, counts):
    return origin, sum(counts)


def prepare_partitions(partition_count):
    input_dir = TEMP_DIR / "input"
    shutil.rmtree(input_dir, ignore_errors=True)
    input_dir.mkdir()

    with gzip.open(DATA_DIR / "flights.csv.gz", "rt", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    partition_size = max(1, (len(rows) + partition_count - 1) // partition_count)
    paths = []
    for index, start in enumerate(range(0, len(rows), partition_size)):
        path = input_dir / f"part-{index:03}.csv"
        with path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys(), lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows[start : start + partition_size])
        paths.append(path)
    return paths


def map_partition(path):
    path = Path(path)
    with path.open(encoding="utf-8", newline="") as file:
        pairs = map_pairs(csv.DictReader(file), map_flight)
    return reduce_by_key(group_by_key(pairs), sum_flights)


def run_mapreduce(partition_paths, workers):
    started = perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        partial_pairs = [pair for partial in executor.map(map_partition, partition_paths) for pair in partial]
    final_pairs = reduce_by_key(group_by_key(partial_pairs), sum_flights)
    return sorted(final_pairs), perf_counter() - started


def main():
    available_workers = os.cpu_count() or 1
    partition_paths = prepare_partitions(max(4, available_workers * 4))
    single_result, single_seconds = run_mapreduce(partition_paths, workers=1)
    parallel_result, parallel_seconds = run_mapreduce(partition_paths, workers=available_workers)
    assert single_result == parallel_result

    with (SUBMISSION_DIR / "origin_flights.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["origin", "flight_count"])
        writer.writerows(parallel_result)

    speedup = single_seconds / parallel_seconds if parallel_seconds else float("inf")
    with (SUBMISSION_DIR / "benchmark.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["workers", "seconds", "speedup"], lineterminator="\n")
        writer.writeheader()
        writer.writerow({"workers": 1, "seconds": round(single_seconds, 6), "speedup": 1.0})
        writer.writerow({"workers": available_workers, "seconds": round(parallel_seconds, 6), "speedup": round(speedup, 3)})


if __name__ == "__main__":
    main()
