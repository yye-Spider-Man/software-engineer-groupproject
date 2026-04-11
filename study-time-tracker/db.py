import sqlite3
from pathlib import Path

DB_DIR = Path("data")
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "study_tracker.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        study_date TEXT NOT NULL,
        duration_minutes INTEGER NOT NULL,
        note TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_log(subject, study_date, duration_minutes, note):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO study_logs (subject, study_date, duration_minutes, note)
    VALUES (?, ?, ?, ?)
    """, (subject, study_date, duration_minutes, note))
    conn.commit()
    conn.close()

def get_all_logs():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, subject, study_date, duration_minutes, note
    FROM study_logs
    ORDER BY study_date DESC, id DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_log(log_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM study_logs WHERE id = ?", (log_id,))
    conn.commit()
    conn.close()