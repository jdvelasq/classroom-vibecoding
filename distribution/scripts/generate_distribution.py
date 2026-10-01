from pathlib import Path
import shutil


COURSE_IDS = (
    "data",
    "fundamentos",
    "descriptiva",
    "predictiva",
    "prescriptiva",
    "productos",
)

DISTRIBUTION_DIR = Path(__file__).resolve().parent.parent


def prepare_course_directories():
    for course_id in COURSE_IDS:
        course_dir = DISTRIBUTION_DIR / course_id

        if course_dir.exists():
            shutil.rmtree(course_dir)

        course_dir.mkdir()


def main():
    prepare_course_directories()


if __name__ == "__main__":
    main()
