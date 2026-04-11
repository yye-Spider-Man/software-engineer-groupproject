import matplotlib.pyplot as plt
from services import get_subject_summary

def save_subject_chart():
    data = get_subject_summary()
    if not data:
        return False

    subjects = [x[0] for x in data]
    minutes = [x[1] for x in data]

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, minutes)
    plt.title("Study Time by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Minutes")
    plt.tight_layout()
    plt.savefig("data/subject_summary.png")
    plt.close()

    return True