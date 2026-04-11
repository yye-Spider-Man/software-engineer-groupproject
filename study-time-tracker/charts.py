from pathlib import Path
import matplotlib.pyplot as plt
from services import get_subject_summary

IMAGE_DIR = Path("image")
IMAGE_DIR.mkdir(exist_ok=True)

ACADEMIC_COLORS = [
    "#6B8DB3",  # soft blue
    "#88A0B6",  # blue gray
    "#9BB7A4",  # sage green
    "#C2A878",  # muted sand
    "#A88FBF",  # dusty purple
    "#7FA7A1",  # desaturated teal
    "#C98F8F",  # muted rose
    "#D8C27A"   # soft yellow
]

BAR_ALPHA = 0.78
PIE_ALPHA = 0.72

def save_subject_bar_chart():
    data = get_subject_summary()
    if not data:
        return None

    subjects = [x[0] for x in data]
    minutes = [x[1] for x in data]
    colors = ACADEMIC_COLORS[:len(subjects)]

    plt.style.use("default")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=160)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    bars = ax.bar(
        subjects,
        minutes,
        color=colors,
        alpha=BAR_ALPHA,
        edgecolor="#AEB8C2",
        linewidth=0.8
    )

    ax.set_title("Study Time by Subject", fontsize=16, fontweight="semibold", pad=14)
    ax.set_xlabel("Subject", fontsize=12)
    ax.set_ylabel("Minutes", fontsize=12)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#BFC7D0")
    ax.spines["bottom"].set_color("#BFC7D0")

    ax.grid(axis="y", linestyle="--", linewidth=0.8, alpha=0.25, color="#AAB4BE")
    ax.set_axisbelow(True)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 3,
            f"{int(height)}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="#4A5560"
        )

    plt.xticks(rotation=25, ha="right", fontsize=10, color="#4A5560")
    plt.yticks(fontsize=10, color="#4A5560")
    plt.tight_layout()

    output_path = IMAGE_DIR / "study_bar_chart.png"
    plt.savefig(output_path, bbox_inches="tight", facecolor="white")
    plt.close()

    return str(output_path)

def save_subject_pie_chart():
    data = get_subject_summary()
    if not data:
        return None

    subjects = [x[0] for x in data]
    minutes = [x[1] for x in data]
    colors = ACADEMIC_COLORS[:len(subjects)]

    plt.style.use("default")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=160)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    wedges, texts, autotexts = ax.pie(
        minutes,
        labels=subjects,
        colors=colors,
        autopct="%1.1f%%",
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.42, "edgecolor": "white", "linewidth": 1.0},
        textprops={"fontsize": 10, "color": "#4A5560"}
    )

    for wedge in wedges:
        wedge.set_alpha(PIE_ALPHA)

    for autotext in autotexts:
        autotext.set_color("#2F3A45")
        autotext.set_fontsize(10)
        autotext.set_fontweight("semibold")

    ax.set_title("Study Time Distribution by Subject", fontsize=16, fontweight="semibold", pad=16)

    output_path = IMAGE_DIR / "study_pie_chart.png"
    plt.savefig(output_path, bbox_inches="tight", facecolor="white")
    plt.close()

    return str(output_path)