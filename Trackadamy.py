import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# DATA STORAGE
grades = {}
assignments = []
schedules = {}

# MAIN WINDOW
app = ctk.CTk()
app.title("Trackademia")
app.geometry("700x500")

title = ctk.CTkLabel(app, text="Trackademia Student Manager", font=("Arial", 24))
title.pack(pady=10)

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=20, pady=20)

tabview.add("Grades")
tabview.add("Assignments")
tabview.add("Schedules")

# ---------------- GRADES TAB ----------------

subject_entry = ctk.CTkEntry(tabview.tab("Grades"), placeholder_text="Subject")
subject_entry.pack(pady=5)

grade_entry = ctk.CTkEntry(tabview.tab("Grades"), placeholder_text="Grade")
grade_entry.pack(pady=5)

grades_box = ctk.CTkTextbox(tabview.tab("Grades"), height=200)
grades_box.pack(pady=10)

def add_grade():
    subject = subject_entry.get()
    grade = float(grade_entry.get())
    grades[subject] = grade
    grades_box.insert("end", f"Saved: {subject} - {grade}\n")

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

add_grade_btn = ctk.CTkButton(tabview.tab("Grades"), text="Add Grade", command=add_grade)
add_grade_btn.pack(pady=5)

view_grade_btn = ctk.CTkButton(tabview.tab("Grades"), text="View Grades", command=view_grades)
view_grade_btn.pack(pady=5)

# ---------------- ASSIGNMENTS TAB ----------------

assign_name = ctk.CTkEntry(tabview.tab("Assignments"), placeholder_text="Assignment Name")
assign_name.pack(pady=5)

assign_deadline = ctk.CTkEntry(tabview.tab("Assignments"), placeholder_text="Deadline")
assign_deadline.pack(pady=5)

assign_box = ctk.CTkTextbox(tabview.tab("Assignments"), height=200)
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

ctk.CTkButton(tabview.tab("Assignments"), text="Add Assignment", command=add_assignment).pack(pady=5)
ctk.CTkButton(tabview.tab("Assignments"), text="View Assignments", command=view_assignments).pack(pady=5)

# ---------------- SCHEDULE TAB ----------------

sched_subject = ctk.CTkEntry(tabview.tab("Schedules"), placeholder_text="Subject")
sched_subject.pack(pady=5)

sched_time = ctk.CTkEntry(tabview.tab("Schedules"), placeholder_text="Day & Time")
sched_time.pack(pady=5)

sched_box = ctk.CTkTextbox(tabview.tab("Schedules"), height=200)
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

ctk.CTkButton(tabview.tab("Schedules"), text="Add Schedule", command=add_schedule).pack(pady=5)
ctk.CTkButton(tabview.tab("Schedules"), text="View Schedules", command=view_schedule).pack(pady=5)

app.mainloop()
