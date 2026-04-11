import csv
from db import get_all_logs

def export_logs_to_csv(filename="data/study_logs_export.csv"):
    rows = get_all_logs()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Subject", "Date", "Minutes", "Note"])
        writer.writerows(rows)

    return filename