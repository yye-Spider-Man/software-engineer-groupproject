import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from db import init_db, add_log, get_all_logs, delete_log
from charts import save_subject_bar_chart, save_subject_pie_chart
from reports import export_logs_to_csv


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class StudyTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Study Time Tracker")
        self.geometry("1180x760")
        self.minsize(1050, 700)
        self.configure(fg_color="#F5F7FA")

        self.setup_ttk_styles()
        self.build_layout()
        self.refresh_table()

    def setup_ttk_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#334155",
            fieldbackground="#FFFFFF",
            rowheight=34,
            borderwidth=0,
            relief="flat",
            font=("Segoe UI", 12)
        )

        style.configure(
            "Treeview.Heading",
            background="#EEF2F6",
            foreground="#1F2937",
            borderwidth=0,
            relief="flat",
            font=("Segoe UI", 12, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", "#DCEBFF")],
            foreground=[("selected", "#1E293B")]
        )

    def build_layout(self):
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)

        self.build_header()
        self.build_form_card()
        self.build_table_card()
        self.build_chart_panel()
        self.build_action_bar()

    def build_header(self):
        header = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=0
        )
        header.grid(row=0, column=0, sticky="ew", padx=24, pady=(22, 10))
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="Study Time Tracker",
            font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold"),
            text_color="#1F2937"
        )
        title.grid(row=0, column=0, sticky="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Record, visualize, and export your study progress.",
            font=ctk.CTkFont(family="Segoe UI", size=15),
            text_color="#6B7280"
        )
        subtitle.grid(row=1, column=0, sticky="w", pady=(4, 0))

    def build_form_card(self):
        form_card = ctk.CTkFrame(
            self,
            fg_color="#FFFFFF",
            corner_radius=22,
            border_width=1,
            border_color="#E5EAF0"
        )
        form_card.grid(row=1, column=0, sticky="ew", padx=(24, 12), pady=10)
        form_card.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        form_title = ctk.CTkLabel(
            form_card,
            text="Add Study Record",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color="#1F2937"
        )
        form_title.grid(row=0, column=0, columnspan=6, sticky="w", padx=20, pady=(18, 8))

        self.subject_entry = self._create_labeled_entry(
            form_card, "Subject", 1, 0, 1, placeholder="e.g. COMP2116"
        )
        self.date_entry = self._create_labeled_entry(
            form_card, "Date", 1, 2, 1, placeholder="YYYY-MM-DD"
        )
        self.duration_entry = self._create_labeled_entry(
            form_card, "Minutes", 1, 4, 1, placeholder="e.g. 90"
        )
        self.note_entry = self._create_labeled_entry(
            form_card, "Note", 3, 0, 3, placeholder="Write a short study note..."
        )

        add_button = ctk.CTkButton(
            form_card,
            text="Add Record",
            command=self.handle_add,
            height=42,
            corner_radius=16,
            fg_color="#76A7FA",
            hover_color="#5D93F5",
            text_color="white",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold")
        )
        add_button.grid(row=4, column=4, columnspan=2, sticky="ew", padx=12, pady=(10, 20))

    def _create_labeled_entry(self, parent, label_text, row, column, columnspan, placeholder=""):
        label = ctk.CTkLabel(
            parent,
            text=label_text,
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#475569"
        )
        label.grid(row=row, column=column, columnspan=columnspan, sticky="w", padx=20, pady=(8, 4))

        entry = ctk.CTkEntry(
            parent,
            height=42,
            corner_radius=16,
            border_width=1,
            border_color="#D7DEE7",
            fg_color="#FBFCFD",
            text_color="#1F2937",
            placeholder_text=placeholder,
            font=ctk.CTkFont(family="Segoe UI", size=15)
        )
        entry.grid(row=row + 1, column=column, columnspan=columnspan, sticky="ew", padx=12, pady=(0, 10))

        return entry

    def build_table_card(self):
        table_card = ctk.CTkFrame(
            self,
            fg_color="#FFFFFF",
            corner_radius=22,
            border_width=1,
            border_color="#E5EAF0"
        )
        table_card.grid(row=2, column=0, sticky="nsew", padx=(24, 12), pady=10)
        table_card.grid_columnconfigure(0, weight=1)
        table_card.grid_rowconfigure(1, weight=1)

        table_title = ctk.CTkLabel(
            table_card,
            text="Study Records",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#1F2937"
        )
        table_title.grid(row=0, column=0, sticky="w", padx=20, pady=(18, 10))

        tree_outer = ctk.CTkFrame(
            table_card,
            fg_color="#F9FBFD",
            corner_radius=18,
            border_width=1,
            border_color="#E3E8EF"
        )
        tree_outer.grid(row=1, column=0, sticky="nsew", padx=18, pady=(0, 18))
        tree_outer.grid_columnconfigure(0, weight=1)
        tree_outer.grid_rowconfigure(0, weight=1)

        tree_host = tk.Frame(tree_outer, bg="#F9FBFD", bd=0, highlightthickness=0)
        tree_host.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        columns = ("id", "subject", "date", "minutes", "note")
        self.tree = ttk.Treeview(tree_host, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("subject", text="Subject")
        self.tree.heading("date", text="Date")
        self.tree.heading("minutes", text="Minutes")
        self.tree.heading("note", text="Note")

        self.tree.column("id", width=70, anchor="center")
        self.tree.column("subject", width=160, anchor="center")
        self.tree.column("date", width=140, anchor="center")
        self.tree.column("minutes", width=110, anchor="center")
        self.tree.column("note", width=560, anchor="w")

        scrollbar = ttk.Scrollbar(tree_host, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def build_action_bar(self):
        action_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=0
        )
        action_frame.grid(row=3, column=0, sticky="ew", padx=(24, 12), pady=(4, 22))
        action_frame.grid_columnconfigure((0, 1, 2), weight=1)

        delete_button = ctk.CTkButton(
            action_frame,
            text="Delete Selected",
            command=self.handle_delete,
            height=42,
            corner_radius=18,
            fg_color="#F1F5F9",
            hover_color="#E2E8F0",
            text_color="#334155",
            border_width=1,
            border_color="#D8E1EA",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold")
        )
        delete_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))

        chart_button = ctk.CTkButton(
            action_frame,
            text="Generate Charts",
            command=self.handle_generate_chart,
            height=42,
            corner_radius=18,
            fg_color="#EAF2FF",
            hover_color="#D8E7FF",
            text_color="#2C5EA8",
            border_width=1,
            border_color="#CFE0FA",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold")
        )
        chart_button.grid(row=0, column=1, sticky="ew", padx=8)

        export_button = ctk.CTkButton(
            action_frame,
            text="Export CSV",
            command=self.handle_export_csv,
            height=42,
            corner_radius=18,
            fg_color="#EEF8F2",
            hover_color="#DDF2E5",
            text_color="#2F6B4F",
            border_width=1,
            border_color="#CFE7D9",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold")
        )
        export_button.grid(row=0, column=2, sticky="ew", padx=(8, 0))

    def build_chart_panel(self):
        self.chart_card = ctk.CTkFrame(
            self,
            fg_color="#FFFFFF",
            corner_radius=22,
            border_width=1,
            border_color="#E5EAF0"
        )
        self.chart_card.grid(row=1, column=1, rowspan=3, sticky="nsew", padx=(12, 24), pady=(10, 22))
        self.chart_card.grid_columnconfigure(0, weight=1)
        self.chart_card.grid_rowconfigure(1, weight=1)

        chart_title = ctk.CTkLabel(
            self.chart_card,
            text="Charts Preview",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#1F2937"
        )
        chart_title.grid(row=0, column=0, sticky="w", padx=18, pady=(18, 8))

        self.image_label = ctk.CTkLabel(
            self.chart_card,
            text="No chart generated yet",
            font=ctk.CTkFont(family="Segoe UI", size=14),
            text_color="#7A8794",
            fg_color="#F8FAFC",
            corner_radius=18,
            width=560,
            height=420
        )
        self.image_label.grid(row=1, column=0, sticky="nsew", padx=18, pady=10)

        switch_frame = ctk.CTkFrame(self.chart_card, fg_color="transparent")
        switch_frame.grid(row=2, column=0, sticky="ew", padx=18, pady=(0, 18))
        switch_frame.grid_columnconfigure((0, 1), weight=1)

        self.bar_button = ctk.CTkButton(
            switch_frame,
            text="Show Bar Chart",
            command=lambda: self.show_chart("image/study_bar_chart.png"),
            height=40,
            corner_radius=16,
            fg_color="#EAF2FF",
            hover_color="#D8E7FF",
            text_color="#2C5EA8"
        )
        self.bar_button.grid(row=0, column=0, sticky="ew", padx=(0, 6))

        self.pie_button = ctk.CTkButton(
            switch_frame,
            text="Show Pie Chart",
            command=lambda: self.show_chart("image/study_pie_chart.png"),
            height=40,
            corner_radius=16,
            fg_color="#EEF8F2",
            hover_color="#DDF2E5",
            text_color="#2F6B4F"
        )
        self.pie_button.grid(row=0, column=1, sticky="ew", padx=(6, 0))

    def show_chart(self, image_path):
        try:
            box_width = 560
            box_height = 420

            img = Image.open(image_path)
            img.thumbnail((box_width, box_height))

            self.chart_image = ctk.CTkImage(
                light_image=img,
                dark_image=img,
                size=(img.width, img.height)
            )
            self.image_label.configure(text="", image=self.chart_image)

        except Exception:
            self.image_label.configure(text="Unable to load chart image.", image=None)

    def animate_chart_sequence(self):
        self.show_chart("image/study_bar_chart.png")
        self.after(500, lambda: self.show_chart("image/study_pie_chart.png"))

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
            self.animate_chart_sequence()
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
    app = StudyTrackerApp()
    app.mainloop()