import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os

# --------------------- COLORS & STYLES ---------------------
BG_COLOR = "#2E2E2E"
TAB_BG = "#3C3F41"
FG_COLOR = "#FFFFFF"
BTN_COLOR = "#5A9BD5"
BTN_HOVER = "#4178A0"
ENTRY_BG = "#555555"
ENTRY_FG = "#FFFFFF"
FONT_TITLE = ("Arial", 24, "bold")
FONT_NORMAL = ("Arial", 12)



# --------------------- UTILITY FUNCTIONS ---------------------
def style_entry(entry):
    entry.configure(bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR, font=FONT_NORMAL)

def style_button(button):
    button.configure(bg=BTN_COLOR, fg=FG_COLOR, font=FONT_NORMAL, relief="flat", padx=10, pady=5)
    button.bind("<Enter>", lambda e: button.configure(bg=BTN_HOVER))
    button.bind("<Leave>", lambda e: button.configure(bg=BTN_COLOR))

# --------------------- DATA STORAGE ---------------------
DATA_FILE = "student_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"grades": {}, "assignments": [], "schedules": []}

def save_data_file(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# --------------------- MAIN WINDOW ---------------------

grades = {}
assignments = []
schedules = []

def build_main_app():
    login_frame.pack_forget()
    root.title("Trackademia")
    root.geometry("750x550")
    root.configure(bg=BG_COLOR)

    title = tk.Label(root, text="Trackademia Student Manager", font=FONT_TITLE, fg=FG_COLOR, bg=BG_COLOR)
    title.pack(pady=15)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
    style.configure("TNotebook.Tab", background=TAB_BG, foreground=FG_COLOR, padding=[20, 10])
    style.map("TNotebook.Tab", background=[("selected", BTN_COLOR)])

    tabview = ttk.Notebook(root)
    tabview.pack(fill="both", expand=True, padx=15, pady=15)

    ctrl_frame = tk.Frame(root, bg=BG_COLOR)
    ctrl_frame.pack(pady=5)

    save_btn = tk.Button(ctrl_frame, text="Save Data", command=lambda: save_data_file({"grades": grades, "assignments": assignments, "schedules": schedules}) or messagebox.showinfo("Saved", "Data saved to student_data.json"), bg=BTN_COLOR, fg=FG_COLOR)
    save_btn.pack(side=tk.LEFT, padx=10)
    style_button(save_btn)

    def load_data_file():
        global grades, assignments, schedules
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                stored = json.load(f)
            grades = stored.get("grades", {})
            assignments = stored.get("assignments", [])
            schedules = stored.get("schedules", [])
            messagebox.showinfo("Loaded", "Saved data loaded from student_data.json")
            view_grades()
            view_assignments()
            view_schedule()
        else:
            messagebox.showwarning("Missing File", "No saved data file found.")

    load_btn = tk.Button(ctrl_frame, text="Load Data", command=load_data_file, bg=BTN_COLOR, fg=FG_COLOR)
    load_btn.pack(side=tk.LEFT, padx=10)
    style_button(load_btn)

    grades_tab = tk.Frame(tabview, bg=TAB_BG)
    assignments_tab = tk.Frame(tabview, bg=TAB_BG)
    schedules_tab = tk.Frame(tabview, bg=TAB_BG)

    tabview.add(grades_tab, text="Grades")
    tabview.add(assignments_tab, text="Assignments")
    tabview.add(schedules_tab, text="Schedules")

    subject_combo = ttk.Combobox(grades_tab, values=["Math", "Science", "English", "History", "Art", "Other"], state="readonly", font=FONT_NORMAL)
    subject_combo.set("Select Subject")
    subject_combo.pack(pady=5)

    grade_entry = tk.Entry(grades_tab)
    grade_entry.insert(0, "Grade")
    grade_entry.pack(pady=5)
    style_entry(grade_entry)
    grade_entry.bind("<FocusIn>", lambda e: grade_entry.delete(0, "end") if grade_entry.get() == "Grade" else None)
    grade_entry.bind("<FocusOut>", lambda e: grade_entry.insert(0, "Grade") if grade_entry.get() == "" else None)

    grades_box = tk.Text(grades_tab, height=15, bg=ENTRY_BG, fg=FG_COLOR, font=FONT_NORMAL, insertbackground=FG_COLOR)
    grades_box.pack(pady=10)

    def add_grade():
        subject = subject_combo.get()
        if subject == "Select Subject":
            messagebox.showerror("Error", "Please choose a subject")
            return
        try:
            grade = float(grade_entry.get())
            if grade < 0 or grade > 100:
                messagebox.showerror("Error", "Grade must be between 0 and 100")
                return
            grades[subject] = grade
            subject_combo.set("Select Subject")
            grade_entry.delete(0, "end")
            grade_entry.insert(0, "Grade")
            view_grades()
        except ValueError:
            messagebox.showerror("Error", "Grade must be a number")

    def view_grades():
        grades_box.delete("1.0","end")
        if grades:
            total = 0
            for subject, grade in grades.items():
                grades_box.insert("end", f"{subject}: {grade}\n")
                total += grade
            avg = total / len(grades)
            grades_box.insert("end", f"\nAverage: {avg:.2f}")
        else:
            grades_box.insert("end","No grades saved")

    def delete_grade():
        subject = subject_combo.get()
        if subject == "Select Subject":
            messagebox.showerror("Error", "Please choose a subject to delete")
            return
        if subject in grades:
            del grades[subject]
            subject_combo.set("Select Subject")
            view_grades()
        else:
            messagebox.showwarning("Not Found", f"No grade found for {subject}")

    def clear_all_grades():
        if messagebox.askyesno("Confirm", "Clear all grades? This cannot be undone."):
            grades.clear()
            view_grades()

    add_btn = tk.Button(grades_tab, text="Add Grade", command=add_grade)
    view_btn = tk.Button(grades_tab, text="View Grades", command=view_grades)
    delete_btn = tk.Button(grades_tab, text="Delete Grade", command=delete_grade)
    clear_btn = tk.Button(grades_tab, text="Clear All", command=clear_all_grades)
    add_btn.pack(pady=5)
    view_btn.pack(pady=5)
    delete_btn.pack(pady=5)
    clear_btn.pack(pady=5)
    style_button(add_btn)
    style_button(view_btn)
    style_button(delete_btn)
    style_button(clear_btn)

    assign_name = tk.Entry(assignments_tab)
    assign_name.insert(0, "Assignment Name")
    assign_name.pack(pady=5)
    style_entry(assign_name)
    assign_name.bind("<FocusIn>", lambda e: assign_name.delete(0, "end") if assign_name.get() == "Assignment Name" else None)
    assign_name.bind("<FocusOut>", lambda e: assign_name.insert(0, "Assignment Name") if assign_name.get() == "" else None)

    assign_deadline = tk.Entry(assignments_tab)
    assign_deadline.insert(0, "Deadline")
    assign_deadline.pack(pady=5)
    style_entry(assign_deadline)
    assign_deadline.bind("<FocusIn>", lambda e: assign_deadline.delete(0, "end") if assign_deadline.get() == "Deadline" else None)
    assign_deadline.bind("<FocusOut>", lambda e: assign_deadline.insert(0, "Deadline") if assign_deadline.get() == "" else None)

    assign_box = tk.Text(assignments_tab, height=15, bg=ENTRY_BG, fg=FG_COLOR, font=FONT_NORMAL, insertbackground=FG_COLOR)
    assign_box.pack(pady=10)

    def add_assignment():
        name = assign_name.get().strip()
        deadline = assign_deadline.get().strip()
        if not name or name == "Assignment Name" or not deadline or deadline == "Deadline":
            messagebox.showerror("Error", "Enter assignment name and deadline")
            return
        assignments.append({"name": name, "due": deadline, "completed": False})
        assign_name.delete(0, "end")
        assign_deadline.delete(0, "end")
        view_assignments()

    def complete_assignment():
        target = assign_name.get().strip()
        if not target or target == "Assignment Name":
            messagebox.showerror("Error", "Enter the assignment name to complete")
            return
        found = False
        for item in assignments:
            if item["name"] == target:
                item["completed"] = True
                found = True
                break
        if found:
            assign_name.delete(0, "end")
            assign_name.insert(0, "Assignment Name")
            assign_deadline.delete(0, "end")
            assign_deadline.insert(0, "Deadline")
            view_assignments()
        else:
            messagebox.showwarning("Not Found", f"No assignment named '{target}'")

    def view_assignments():
        assign_box.delete("1.0","end")
        if assignments:
            for item in assignments:
                status = "Done" if item["completed"] else "Pending"
                assign_box.insert("end", f"{item['name']} - Due: {item['due']} [{status}]\n")
        else:
            assign_box.insert("end","No assignments saved")

    def delete_assignment():
        target = assign_name.get().strip()
        if not target or target == "Assignment Name":
            messagebox.showerror("Error", "Enter the assignment name to delete")
            return
        global assignments
        assignments = [item for item in assignments if item["name"] != target]
        assign_name.delete(0, "end")
        assign_name.insert(0, "Assignment Name")
        assign_deadline.delete(0, "end")
        assign_deadline.insert(0, "Deadline")
        view_assignments()

    def clear_all_assignments():
        if messagebox.askyesno("Confirm", "Clear all assignments? This cannot be undone."):
            assignments.clear()
            assign_name.delete(0, "end")
            assign_name.insert(0, "Assignment Name")
            assign_deadline.delete(0, "end")
            assign_deadline.insert(0, "Deadline")
            view_assignments()

    add_btn2 = tk.Button(assignments_tab, text="Add Assignment", command=add_assignment)
    view_btn2 = tk.Button(assignments_tab, text="View Assignments", command=view_assignments)
    complete_btn2 = tk.Button(assignments_tab, text="Mark Complete", command=complete_assignment)
    delete_btn2 = tk.Button(assignments_tab, text="Delete Assignment", command=delete_assignment)
    clear_btn2 = tk.Button(assignments_tab, text="Clear All", command=clear_all_assignments)
    add_btn2.pack(pady=5)
    view_btn2.pack(pady=5)
    complete_btn2.pack(pady=5)
    delete_btn2.pack(pady=5)
    clear_btn2.pack(pady=5)
    style_button(add_btn2)
    style_button(view_btn2)
    style_button(complete_btn2)
    style_button(delete_btn2)
    style_button(clear_btn2)

    sched_subject = tk.Entry(schedules_tab)
    sched_subject.insert(0, "Subject")
    sched_subject.pack(pady=5)
    style_entry(sched_subject)
    sched_subject.bind("<FocusIn>", lambda e: sched_subject.delete(0, "end") if sched_subject.get() == "Subject" else None)
    sched_subject.bind("<FocusOut>", lambda e: sched_subject.insert(0, "Subject") if sched_subject.get() == "" else None)

    sched_time = tk.Entry(schedules_tab)
    sched_time.insert(0, "Day & Time")
    sched_time.pack(pady=5)
    style_entry(sched_time)
    sched_time.bind("<FocusIn>", lambda e: sched_time.delete(0, "end") if sched_time.get() == "Day & Time" else None)
    sched_time.bind("<FocusOut>", lambda e: sched_time.insert(0, "Day & Time") if sched_time.get() == "" else None)

    sched_box = tk.Text(schedules_tab, height=15, bg=ENTRY_BG, fg=FG_COLOR, font=FONT_NORMAL, insertbackground=FG_COLOR)
    sched_box.pack(pady=10)

    def add_schedule():
        subject = sched_subject.get().strip()
        time = sched_time.get().strip()
        if not subject or subject == "Subject" or not time or time == "Day & Time":
            messagebox.showerror("Error", "Enter an event and time")
            return
        schedules.append({"event": subject, "time": time})
        sched_subject.delete(0, "end")
        sched_subject.insert(0, "Subject")
        sched_time.delete(0, "end")
        sched_time.insert(0, "Day & Time")
        view_schedule()

    def view_schedule():
        sched_box.delete("1.0","end")
        if schedules:
            sorted_schedules = sorted(schedules, key=lambda x: x['time'])
            for item in sorted_schedules:
                sched_box.insert("end", f"{item['event']} at {item['time']}\n")
        else:
            sched_box.insert("end","No schedules saved")

    def delete_schedule_func():
        target = sched_subject.get().strip()
        if not target or target == "Subject":
            messagebox.showerror("Error", "Enter the event name to delete")
            return
        global schedules
        schedules = [item for item in schedules if item["event"] != target]
        sched_subject.delete(0, "end")
        sched_subject.insert(0, "Subject")
        sched_time.delete(0, "end")
        sched_time.insert(0, "Day & Time")
        view_schedule()

    def clear_all_schedules_func():
        if messagebox.askyesno("Confirm", "Clear all schedules? This cannot be undone."):
            schedules.clear()
            sched_subject.delete(0, "end")
            sched_subject.insert(0, "Subject")
            sched_time.delete(0, "end")
            sched_time.insert(0, "Day & Time")
            view_schedule()

    add_btn3 = tk.Button(schedules_tab, text="Add Schedule", command=add_schedule)
    view_btn3 = tk.Button(schedules_tab, text="View Schedules", command=view_schedule)
    delete_btn3 = tk.Button(schedules_tab, text="Delete Schedule", command=delete_schedule_func)
    clear_btn3 = tk.Button(schedules_tab, text="Clear All", command=clear_all_schedules_func)
    add_btn3.pack(pady=5)
    view_btn3.pack(pady=5)
    delete_btn3.pack(pady=5)
    clear_btn3.pack(pady=5)
    style_button(add_btn3)
    style_button(view_btn3)
    style_button(delete_btn3)
    style_button(clear_btn3)

    # Auto-load data on startup
    load_data_file()

# --------------------- LOG-IN SYSTEM -----------------------
root = tk.Tk()
root.title("Login")
root.geometry("340x440")
root.configure(bg="#2e728f")

login_frame = tk.Frame(root, bg="#153344")
login_frame.pack(fill="both", expand=True)

login_label = tk.Label(login_frame, text="Login", fg='#00113a', font=("Raleway", 24, "bold"))
username_label = tk.Label(login_frame, text="Username", fg='#00113a', font=("Raleway", 16))
username_entry = tk.Entry(login_frame, font=("Raleway", 16))
password_label = tk.Label(login_frame, text="Password", fg='#00113a', font=("Raleway", 16))
password_entry = tk.Entry(login_frame, show="*", font=("Raleway", 16))

def login():
    if username_entry.get() == "johnsmith" and password_entry.get() == "12345":
        build_main_app()
    else:
        messagebox.showerror("Error", "Invalid login")

login_button = tk.Button(login_frame, text="Login", bg='#002263', fg='#00113a', font=("Raleway", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=15)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=15)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

root.mainloop()


