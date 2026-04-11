import tkinter as tk
from tkinter import ttk, messagebox
from db import init_db, add_log, get_all_logs, delete_log
from charts import save_subject_chart
from reports import export_logs_to_csv
class StudyTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Time Tracker")
        self.root.geometry("900x500")

        self.build_form()
        self.build_table()
        self.refresh_table()

    def build_form(self):
        form = tk.Frame(self.root)
        form.pack(fill="x", padx=10, pady=10)

        tk.Label(form, text="Subject").grid(row=0, column=0, sticky="w")
        self.subject_entry = tk.Entry(form, width=20)
        self.subject_entry.grid(row=0, column=1, padx=5)

        tk.Label(form, text="Date (YYYY-MM-DD)").grid(row=0, column=2, sticky="w")
        self.date_entry = tk.Entry(form, width=20)
        self.date_entry.grid(row=0, column=3, padx=5)

        tk.Label(form, text="Minutes").grid(row=0, column=4, sticky="w")
        self.duration_entry = tk.Entry(form, width=10)
        self.duration_entry.grid(row=0, column=5, padx=5)

        tk.Label(form, text="Note").grid(row=1, column=0, sticky="w")
        self.note_entry = tk.Entry(form, width=60)
        self.note_entry.grid(row=1, column=1, columnspan=4, padx=5, pady=5, sticky="we")

        tk.Button(form, text="Add Record", command=self.handle_add).grid(row=1, column=5, padx=5)

    def build_table(self):
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("id", "subject", "date", "minutes", "note")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("subject", text="Subject")
        self.tree.heading("date", text="Date")
        self.tree.heading("minutes", text="Minutes")
        self.tree.heading("note", text="Note")

        self.tree.column("id", width=50)
        self.tree.column("subject", width=120)
        self.tree.column("date", width=120)
        self.tree.column("minutes", width=80)
        self.tree.column("note", width=400)

        self.tree.pack(fill="both", expand=True)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Delete Selected", command=self.handle_delete).pack(side="left", padx=5)
        tk.Button(button_frame, text="Generate Chart", command=self.handle_generate_chart).pack(side="left", padx=5)
        tk.Button(button_frame, text="Export CSV", command=self.handle_export_csv).pack(side="left", padx=5)

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
        success = save_subject_chart()
        if success:
            messagebox.showinfo("Success", "Chart saved to data/subject_summary.png")
        else:
            messagebox.showwarning("Warning", "No data available to generate chart.")

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