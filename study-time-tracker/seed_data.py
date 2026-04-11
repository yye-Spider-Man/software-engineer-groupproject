from db import init_db, add_log

sample_data = [
    ("COMP2116", "2026-04-01", 90, "Read software engineering lecture notes"),
    ("COMP2116", "2026-04-02", 120, "Worked on project planning"),
    ("COMP2116", "2026-04-04", 80, "Prepared GitHub repository and README draft"),
    ("COMP2116", "2026-04-06", 100, "Reviewed agile vs waterfall"),
    ("COMP2116", "2026-04-09", 110, "Wrote Tkinter UI prototype"),

    ("MATH2001", "2026-04-01", 60, "Calculus exercises"),
    ("MATH2001", "2026-04-03", 75, "Reviewed integration methods"),
    ("MATH2001", "2026-04-05", 90, "Past paper practice"),
    ("MATH2001", "2026-04-08", 70, "Homework corrections"),

    ("CSCI3002", "2026-04-02", 95, "Database normalization review"),
    ("CSCI3002", "2026-04-05", 130, "SQLite practice"),
    ("CSCI3002", "2026-04-07", 85, "SQL query exercises"),
    ("CSCI3002", "2026-04-10", 100, "CRUD logic test"),

    ("AI1001", "2026-04-03", 50, "Read AI introduction chapter"),
    ("AI1001", "2026-04-06", 65, "Classification notes"),
    ("AI1001", "2026-04-08", 75, "Model evaluation practice"),
    ("AI1001", "2026-04-10", 90, "Assignment revision"),

    ("ENGL2005", "2026-04-04", 45, "Vocabulary revision"),
    ("ENGL2005", "2026-04-07", 60, "Presentation outline"),
    ("ENGL2005", "2026-04-09", 55, "Academic writing practice")
]

if __name__ == "__main__":
    init_db()
    for row in sample_data:
        add_log(*row)
    print("Sample data inserted successfully.")