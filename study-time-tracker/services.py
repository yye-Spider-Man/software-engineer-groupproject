from db import get_conn

def get_subject_summary():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT subject, SUM(duration_minutes)
    FROM study_logs
    GROUP BY subject
    ORDER BY SUM(duration_minutes) DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_daily_summary():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT study_date, SUM(duration_minutes)
    FROM study_logs
    GROUP BY study_date
    ORDER BY study_date ASC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows