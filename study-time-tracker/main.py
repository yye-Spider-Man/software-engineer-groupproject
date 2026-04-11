import tkinter as tk
from tkinter import ttk, messagebox
from db import init_db, add_log, get_all_logs, delete_log
from charts import save_subject_bar_chart, save_subject_pie_chart
from reports import export_logs_to_csv

class StudyTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Time Tracker")
        self.root.geometry("1100x680")
        self.root.configure(bg="#F7F9FB")

        self.setup_styles()
        self.build_header()
        self.build_form()
        self.build_table()
        self.refresh_table()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(".", font=("Segoe UI", 10))

        style.configure("Card.TFrame", background="#FFFFFF")
        style.configure("Header.TFrame", background="#F4F6F8")
        style.configure("Title.TLabel",
                        background="#F4F6F8",
                        foreground="#233142",
                        font=("Segoe UI", 20, "bold"))
        style.configure("Subtitle.TLabel",
                        background="#F4F6F8",
                        foreground="#6B7785",
                        font=("Segoe UI", 10))

        style.configure("Section.TLabelframe",
                        background="#FFFFFF",
                        borderwidth=1,
                        relief="solid",
                        bordercolor="#D9E0E6"
                        )
        style.configure("Section.TLabelframe.Label",
                        background="#FFFFFF",
                        foreground="#233142",
                        font=("Segoe UI", 11, "bold"))

        style.configure("TLabel",
                        background="#FFFFFF",
                        foreground="#2F3A45",
                        font=("Segoe UI", 10))

        style.configure("TEntry",
                        padding=6)

        style.configure("Primary.TButton",
                        font=("Segoe UI", 10, "bold"),
                        padding=(12, 8),
                        background="#6B8DB3",
                        foreground="white",
                        borderwidth=0)
        style.map("Primary.TButton",
                  background=[("active", "#5E7FA3")])

        style.configure("Secondary.TButton",
                        font=("Segoe UI", 10),
                        padding=(12, 8),
                        background="#DCE3EA",
                        foreground="#233142",
                        borderwidth=0)
        style.map("Secondary.TButton",
                  background=[("active", "#CCD5DE")])

        style.configure("Treeview",
                        background="#FFFFFF",
                        foreground="#2F3A45",
                        rowheight=30,
                        fieldbackground="#FFFFFF",
                        bordercolor="#D8DEE6",
                        borderwidth=1,
                        font=("Segoe UI", 10))
        style.configure("Treeview.Heading",
                        background="#EAF0F5",
                        foreground="#233142",
                        font=("Segoe UI", 10, "bold"),
                        relief="flat")
        style.map("Treeview",
                  background=[("selected", "#D8E6F2")],
                  foreground=[("selected", "#1F2D3A")])

    def build_header(self):
        header = ttk.Frame(self.root, style="Header.TFrame")
        header.pack(fill="x", padx=20, pady=(20, 10))

        ttk.Label(header, text="Study Time Tracker", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            header,
            text="Record study time, analyze learning patterns, and export reports.",
            style="Subtitle.TLabel"
        ).pack(anchor="w", pady=(4, 0))

    def build_form(self):
        form_frame = ttk.LabelFrame(self.root, text="Add Study Record", style="Section.TLabelframe")
        form_frame.pack(fill="x", padx=20, pady=10, ipady=10)

        inner = ttk.Frame(form_frame, style="Card.TFrame")
        inner.pack(fill="x", padx=15, pady=10)

        ttk.Label(inner, text="Subject").grid(row=0, column=0, sticky="w", padx=8, pady=8)
        self.subject_entry = ttk.Entry(inner, width=22)
        self.subject_entry.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(inner, text="Date (YYYY-MM-DD)").grid(row=0, column=2, sticky="w", padx=8, pady=8)
        self.date_entry = ttk.Entry(inner, width=18)
        self.date_entry.grid(row=0, column=3, padx=8, pady=8)

        ttk.Label(inner, text="Minutes").grid(row=0, column=4, sticky="w", padx=8, pady=8)
        self.duration_entry = ttk.Entry(inner, width=12)
        self.duration_entry.grid(row=0, column=5, padx=8, pady=8)

        ttk.Label(inner, text="Note").grid(row=1, column=0, sticky="w", padx=8, pady=8)
        self.note_entry = ttk.Entry(inner, width=70)
        self.note_entry.grid(row=1, column=1, columnspan=4, sticky="we", padx=8, pady=8)

        ttk.Button(inner, text="Add Record", style="Primary.TButton", command=self.handle_add)\
            .grid(row=1, column=5, padx=8, pady=8)

    def build_table(self):
        table_frame = ttk.LabelFrame(self.root, text="Study Records", style="Section.TLabelframe")
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        inner = ttk.Frame(table_frame, style="Card.TFrame")
        inner.pack(fill="both", expand=True, padx=15, pady=12)

        columns = ("id", "subject", "date", "minutes", "note")
        self.tree = ttk.Treeview(inner, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("subject", text="Subject")
        self.tree.heading("date", text="Date")
        self.tree.heading("minutes", text="Minutes")
        self.tree.heading("note", text="Note")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("subject", width=140, anchor="center")
        self.tree.column("date", width=130, anchor="center")
        self.tree.column("minutes", width=100, anchor="center")
        self.tree.column("note", width=520, anchor="w")

        scrollbar = ttk.Scrollbar(inner, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        button_frame = ttk.Frame(self.root, style="Header.TFrame")
        button_frame.pack(fill="x", padx=20, pady=(0, 20))

        ttk.Button(button_frame, text="Delete Selected", style="Secondary.TButton",
                   command=self.handle_delete).pack(side="left", padx=(0, 10))

        ttk.Button(button_frame, text="Generate Charts", style="Secondary.TButton",
                   command=self.handle_generate_chart).pack(side="left", padx=10)

        ttk.Button(button_frame, text="Export CSV", style="Secondary.TButton",
                   command=self.handle_export_csv).pack(side="left", padx=10)

    def handle_add(self):
        subject = self.subject_entry.get().strip()
        study_date = self.date_entry.get().strip()
        duration = self.duration_entry.get().strip()
        note = self.note_entry.get().strip()

        if not subject or not study_date or not duration:
            messagebox.showerror("Error", "Subject, date and minutes are required.")
            return

        if not duration.isdigit():
            messagebox.showerror("Error", "Minutes must be an integer.")
            return

        add_log(subject, study_date, int(duration), note)
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Success", "Record added successfully.")

    def handle_delete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a record.")
            return

        item = self.tree.item(selected[0])
        log_id = item["values"][0]
        delete_log(log_id)
        self.refresh_table()

    def handle_generate_chart(self):
        bar_chart = save_subject_bar_chart()
        pie_chart = save_subject_pie_chart()

        if bar_chart and pie_chart:
            messagebox.showinfo(
                "Success",
                f"Charts saved successfully:\n{bar_chart}\n{pie_chart}"
            )
        else:
            messagebox.showwarning("Warning", "No data available to generate charts.")

    def handle_export_csv(self):
        filename = export_logs_to_csv()
        messagebox.showinfo("Success", f"CSV exported to {filename}")

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in get_all_logs():
            self.tree.insert("", "end", values=row)

    def clear_form(self):
        self.subject_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = StudyTrackerApp(root)
    root.mainloop()