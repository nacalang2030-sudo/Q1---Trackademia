import tkinter as tk
from tkinter import ttk, messagebox
#--------------------- LOG-IN SYSTEM -----------------------
#color 1 red (#890304)
#color 2 dark blue (00113a)
#color 3 lighter dark blue (#002263)
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

# --------------------- MAIN WINDOW ---------------------
app = tk.Tk()
app.title("Trackademia")
app.geometry("750x550")
app.configure(bg=BG_COLOR)

title = tk.Label(app, text="Trackademia Student Manager", font=FONT_TITLE, fg=FG_COLOR, bg=BG_COLOR)
title.pack(pady=15)

# --------------------- TAB CONTROL ---------------------
style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
style.configure("TNotebook.Tab", background=TAB_BG, foreground=FG_COLOR, padding=[20, 10])
style.map("TNotebook.Tab", background=[("selected", BTN_COLOR)])

tabview = ttk.Notebook(app)
tabview.pack(fill="both", expand=True, padx=15, pady=15)

grades_tab = tk.Frame(tabview, bg=TAB_BG)
assignments_tab = tk.Frame(tabview, bg=TAB_BG)
schedules_tab = tk.Frame(tabview, bg=TAB_BG)

tabview.add(grades_tab, text="Grades")
tabview.add(assignments_tab, text="Assignments")
tabview.add(schedules_tab, text="Schedules")

# --------------------- UTILITY FUNCTIONS ---------------------
def style_entry(entry):
    entry.configure(bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR, font=FONT_NORMAL)

def style_button(button):
    button.configure(bg=BTN_COLOR, fg=FG_COLOR, font=FONT_NORMAL, relief="flat", padx=10, pady=5)
    button.bind("<Enter>", lambda e: button.configure(bg=BTN_HOVER))
    button.bind("<Leave>", lambda e: button.configure(bg=BTN_COLOR))

# --------------------- DATA STORAGE ---------------------
grades = {}
assignments = []
schedules = {}

# --------------------- GRADES TAB ---------------------
subject_entry = tk.Entry(grades_tab)
subject_entry.insert(0, "Subject")
subject_entry.pack(pady=5)
style_entry(subject_entry)

grade_entry = tk.Entry(grades_tab)
grade_entry.insert(0, "Grade")
grade_entry.pack(pady=5)
style_entry(grade_entry)

grades_box = tk.Text(grades_tab, height=15, bg=ENTRY_BG, fg=FG_COLOR, font=FONT_NORMAL, insertbackground=FG_COLOR)
grades_box.pack(pady=10)

def add_grade():
    try:
        subject = subject_entry.get()
        grade = float(grade_entry.get())
        grades[subject] = grade
        grades_box.insert("end", f"Saved: {subject} - {grade}\n")
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

add_btn = tk.Button(grades_tab, text="Add Grade", command=add_grade)
view_btn = tk.Button(grades_tab, text="View Grades", command=view_grades)
add_btn.pack(pady=5)
view_btn.pack(pady=5)
style_button(add_btn)
style_button(view_btn)

# --------------------- ASSIGNMENTS TAB ---------------------
assign_name = tk.Entry(assignments_tab)
assign_name.insert(0, "Assignment Name")
assign_name.pack(pady=5)
style_entry(assign_name)

assign_deadline = tk.Entry(assignments_tab)
assign_deadline.insert(0, "Deadline")
assign_deadline.pack(pady=5)
style_entry(assign_deadline)

assign_box = tk.Text(assignments_tab, height=15, bg=ENTRY_BG, fg=FG_COLOR, font=FONT_NORMAL, insertbackground=FG_COLOR)
assign_box.pack(pady=10)

def add_assignment():
    name = assign_name.get()
    deadline = assign_deadline.get()
    assignments.append((name, deadline))
    assign_box.insert("end", f"{name} - Due: {deadline}\n")

def view_assignments():
    assign_box.delete("1.0","end")
    if assignments:
        for name, deadline in assignments:
            assign_box.insert("end", f"{name} - Due: {deadline}\n")
    else:
        assign_box.insert("end","No assignments saved")

add_btn2 = tk.Button(assignments_tab, text="Add Assignment", command=add_assignment)
view_btn2 = tk.Button(assignments_tab, text="View Assignments", command=view_assignments)
add_btn2.pack(pady=5)
view_btn2.pack(pady=5)
style_button(add_btn2)
style_button(view_btn2)

# --------------------- SCHEDULES TAB ---------------------
sched_subject = tk.Entry(schedules_tab)
sched_subject.insert(0, "Subject")
sched_subject.pack(pady=5)
style_entry(sched_subject)

sched_time = tk.Entry(schedules_tab)
sched_time.insert(0, "Day & Time")
sched_time.pack(pady=5)
style_entry(sched_time)

sched_box = tk.Text(schedules_tab, height=15, bg=ENTRY_BG, fg=FG_COLOR, font=FONT_NORMAL, insertbackground=FG_COLOR)
sched_box.pack(pady=10)

def add_schedule():
    subject = sched_subject.get()
    time = sched_time.get()
    schedules[subject] = time
    sched_box.insert("end", f"{subject} - {time}\n")

def view_schedule():
    sched_box.delete("1.0","end")
    if schedules:
        for subject, time in schedules.items():
            sched_box.insert("end", f"{subject}: {time}\n")
    else:
        sched_box.insert("end","No schedules saved")

add_btn3 = tk.Button(schedules_tab, text="Add Schedule", command=add_schedule)
view_btn3 = tk.Button(schedules_tab, text="View Schedules", command=view_schedule)
add_btn3.pack(pady=5)
view_btn3.pack(pady=5)
style_button(add_btn3)
style_button(view_btn3)

app.mainloop()

