"""CSV storage for student grade records."""

import csv
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "student_data.csv"
HEADERS = [
    "Name", "Roll Number", "Mathematics", "Physics", "Chemistry",
    "Programming", "English", "Total", "Percentage", "SGPA", "Result"
]


def save_student(record):
    file_exists = DATA_FILE.exists()

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        if not file_exists or DATA_FILE.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(record)


def read_students():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
