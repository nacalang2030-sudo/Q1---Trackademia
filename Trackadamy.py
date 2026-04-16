import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os

# --------------------- COLORS & STYLES ---------------------
# Enhanced modern color scheme
BG_COLOR = "#0D0221"  # Darker, richer background
TAB_BG = "#1A0833"
FG_COLOR = "#E9D8FD" 

BTN_COLOR = "#A855F7"  # Purple button
BTN_HOVER = "#D8B4FE"  # Light purple on hover
BTN_ACTIVE = "#9333EA"  # Darker purple on click

ENTRY_BG = "#2D1B4E" 
ENTRY_FG = "#F5F3FF" 

# Enhanced fonts - added Segoe UI for modern look
FONT_TITLE = ("Segoe UI", 28, "bold") 
FONT_NORMAL = ("Segoe UI", 11)
FONT_LABEL = ("Segoe UI", 11, "bold")
FONT_SMALL = ("Segoe UI", 9)
FONT_SUBTITLE = ("Segoe UI", 16, "bold")

# Additional color aliases and variables
BG_PRIMARY = BG_COLOR
BG_SECONDARY = "#140428"
ACCENT_PRIMARY = "#A855F7"
ACCENT_SECONDARY = "#D8B4FE"
FG_PRIMARY = FG_COLOR
FG_MUTED = "#C4B5D4"

# Spacing constants
PADDING_SMALL = 8
PADDING_MEDIUM = 12
PADDING_LARGE = 20

# --------------------- UTILITY FUNCTIONS ---------------------
def style_entry(entry):
    entry.configure(bg=ENTRY_BG, 
                    fg=ENTRY_FG, 
                    insertbackground=FG_COLOR,
                    font=FONT_NORMAL
                   )

def create_placeholder_entry(parent, placeholder="", width=30):
    """Create a styled Entry widget with modern look."""
    entry = tk.Entry(parent, font=FONT_NORMAL, width=width,
                    bg=ENTRY_BG, fg=ENTRY_FG,
                    insertbackground=ACCENT_SECONDARY, relief="flat",
                    bd=0, borderwidth=0)
    
    # Add a frame for border effect
    border_frame = tk.Frame(parent, bg=ACCENT_PRIMARY, highlightthickness=0)
    border_frame.pack_before(entry)
    entry_inner = tk.Frame(border_frame, bg=ENTRY_BG, highlightthickness=0)
    entry_inner.pack(padx=1, pady=1)
    
    return entry

def create_button(parent, text, command, style="primary", width=20):
    """Create a modern styled button with hover effects."""
    if style == "primary":
        button = tk.Button(parent, text=text, command=command, 
                          font=FONT_NORMAL, width=width,
                          bg=ACCENT_PRIMARY, fg="white",
                          relief="flat", bd=0, borderwidth=0,
                          padx=PADDING_MEDIUM, pady=PADDING_SMALL,
                          activebackground=BTN_ACTIVE, activeforeground="white",
                          cursor="hand2")
    else:
        button = tk.Button(parent, text=text, command=command,
                          font=FONT_NORMAL, width=width,
                          bg=ACCENT_PRIMARY, fg="white",
                          relief="flat", bd=0, borderwidth=0,
                          padx=PADDING_MEDIUM, pady=PADDING_SMALL,
                          activebackground=BTN_ACTIVE, activeforeground="white",
                          cursor="hand2")
    return button

def style_button(button):
    button.configure(
        bg=ACCENT_PRIMARY, 
        fg="white", 
        font=FONT_NORMAL,
        relief="flat",
        padx=PADDING_MEDIUM,
        pady=PADDING_SMALL,
        activebackground=BTN_ACTIVE,
        activeforeground="white",
        bd=0,
        borderwidth=0,
        cursor="hand2"
    )
    button.bind("<Enter>", lambda e: button.configure(bg=BTN_HOVER) if button.cget("state") != "disabled" else None)
    button.bind("<Leave>", lambda e: button.configure(bg=ACCENT_PRIMARY) if button.cget("state") != "disabled" else None)

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

grades = {}
assignments = []
schedules = []

# --------------------- MAIN WINDOW ---------------------



def build_main_app():
    global login_frame
    login_frame.pack_forget()
    
    # Define screen variables
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    root.attributes('-fullscreen', True)  
    root.title("Trackademia")
    root.geometry("750x550")
    root.configure(bg=BG_COLOR)
    
    # Allow exiting fullscreen with Escape key
    def exit_fullscreen(event=None):
        root.attributes('-fullscreen', False)
        root.geometry("1200x800")  
    
    root.bind('<Escape>', exit_fullscreen)

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

    subject_combo = ttk.Combobox(grades_tab, values=["Mathematics 2", "English", "Social Science", "PHEM", "Mathematics 3", "Adtech", "Physics", "Chemistry", "Biology", "Earth Science", "Filipino", "Computer Science"], state="readonly", font=FONT_NORMAL)
    subject_combo.set("Select Subject")
    subject_combo.pack(pady=5)

    grade_entry = tk.Entry(grades_tab)
    grade_entry.insert(0, "Grade")
    grade_entry.pack(pady=5)
    style_entry(grade_entry)
    grade_entry.bind("<FocusIn>", lambda e: grade_entry.delete(0, "end") if grade_entry.get() == "Grade" else None)
    grade_entry.bind("<FocusOut>", lambda e: grade_entry.insert(0, "Grade") if grade_entry.get() == "" else None)

    # Add units input field
    units_entry = tk.Entry(grades_tab)
    units_entry.insert(0, "Units (3 for most, 4 for English)")
    units_entry.pack(pady=5)
    style_entry(units_entry)
    units_entry.bind("<FocusIn>", lambda e: units_entry.delete(0, "end") if units_entry.get() == "Units (3 for most, 4 for English)" else None)
    units_entry.bind("<FocusOut>", lambda e: units_entry.insert(0, "Units (3 for most, 4 for English)") if units_entry.get() == "" else None)

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
            
            # Get units and set defaults
            units_text = units_entry.get().strip()
            if units_text == "Units (3 for most, 4 for English)" or units_text == "":
                # Auto-set units based on subject
                units = 4 if subject == "English" else 3
            else:
                try:
                    units = float(units_text)
                except ValueError:
                    messagebox.showerror("Error", "Units must be a number")
                    return
            
            # Store grade with units
            grades[subject] = {"grade": grade, "units": units}
            subject_combo.set("Select Subject")
            grade_entry.delete(0, "end")
            grade_entry.insert(0, "Grade")
            units_entry.delete(0, "end")
            units_entry.insert(0, "Units (3 for most, 4 for English)")
            view_grades()
        except ValueError:
            messagebox.showerror("Error", "Grade must be a number")

    def view_grades():
        grades_box.delete("1.0","end")
        if grades:
            total_grade_units = 0
            total_units = 0
            grades_box.insert("end", "Subject                Grade  Units\n")
            grades_box.insert("end", "-" * 40 + "\n")
            for subject, data in grades.items():
                grade = data["grade"]
                units = data["units"]
                grades_box.insert("end", f"{subject:<20} {grade:>6.2f}  {units:>5.1f}\n")
                total_grade_units += grade * units
                total_units += units
            
            if total_units > 0:
                gwa = total_grade_units / total_units
                grades_box.insert("end", "-" * 40 + "\n")
                grades_box.insert("end", f"Weighted GWA: {gwa:.2f}\n")
            else:
                grades_box.insert("end", "No units recorded")
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
    
    # Create button frame for horizontal layout
    button_frame = tk.Frame(grades_tab, bg=TAB_BG)
    button_frame.pack(pady=10, fill="x", padx=10)
    
    add_btn = tk.Button(button_frame, text="Add Grade", command=add_grade)
    view_btn = tk.Button(button_frame, text="View Grades", command=view_grades)
    delete_btn = tk.Button(button_frame, text="Delete Grade", command=delete_grade)
    clear_btn = tk.Button(button_frame, text="Clear All", command=clear_all_grades)
    add_btn.pack(side="left", padx=5)
    view_btn.pack(side="left", padx=5)
    delete_btn.pack(side="left", padx=5)
    clear_btn.pack(side="left", padx=5)
    
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
    
    # Create button frame for horizontal layout
    button_frame2 = tk.Frame(assignments_tab, bg=TAB_BG)
    button_frame2.pack(pady=10, fill="x", padx=10)
    
    add_btn2 = tk.Button(button_frame2, text="Add Assignment", command=add_assignment)
    view_btn2 = tk.Button(button_frame2, text="View Assignments", command=view_assignments)
    complete_btn2 = tk.Button(button_frame2, text="Mark Complete", command=complete_assignment)
    delete_btn2 = tk.Button(button_frame2, text="Delete Assignment", command=delete_assignment)
    clear_btn2 = tk.Button(button_frame2, text="Clear All", command=clear_all_assignments)
    add_btn2.pack(side="left", padx=5)
    view_btn2.pack(side="left", padx=5)
    complete_btn2.pack(side="left", padx=5)
    delete_btn2.pack(side="left", padx=5)
    clear_btn2.pack(side="left", padx=5)
    
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
    
    # Create button frame for horizontal layout
    button_frame3 = tk.Frame(schedules_tab, bg=TAB_BG)
    button_frame3.pack(pady=10, fill="x", padx=10)
    
    add_btn3 = tk.Button(button_frame3, text="Add Schedule", command=add_schedule)
    view_btn3 = tk.Button(button_frame3, text="View Schedules", command=view_schedule)
    delete_btn3 = tk.Button(button_frame3, text="Delete Schedule", command=delete_schedule_func)
    clear_btn3 = tk.Button(button_frame3, text="Clear All", command=clear_all_schedules_func)
    add_btn3.pack(side="left", padx=5)
    view_btn3.pack(side="left", padx=5)
    delete_btn3.pack(side="left", padx=5)
    clear_btn3.pack(side="left", padx=5)
    
    style_button(add_btn3)
    style_button(view_btn3)
    style_button(delete_btn3)
    style_button(clear_btn3)

    # Auto-load data on startup
    load_data_file()

# ==================== LOGIN INTERFACE ====================
root = tk.Tk()
root.title("Trackademia - Login")
root.configure(bg=BG_PRIMARY)
root.resizable(False, False)

# Define screen variables and center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500
window_height = 600
center_x = (screen_width - window_width) // 2
center_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

main_frame = tk.Frame(root, bg=BG_PRIMARY)
main_frame.pack(fill="both", expand=True)

# Modern gradient-style header with enhanced spacing
header = tk.Frame(main_frame, bg=ACCENT_PRIMARY, height=140)
header.pack(fill="x")
header.pack_propagate(False)

# Add decorative top bar
top_bar = tk.Frame(header, bg=ACCENT_SECONDARY, height=3)
top_bar.pack(fill="x")

title_label = tk.Label(header, text="🎓 Trackademia", font=FONT_TITLE,
                      fg="white", bg=ACCENT_PRIMARY)
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(header, text="Student Management System",
                         font=("Segoe UI", 10), fg=ACCENT_SECONDARY, bg=ACCENT_PRIMARY)
subtitle_label.pack(pady=(0, 20))

# Centered login form container with padding
login_frame = tk.Frame(main_frame, bg=BG_PRIMARY)
login_frame.pack(expand=True, fill="both", padx=PADDING_LARGE, pady=PADDING_LARGE)

# Modern card-style login form with border effect
border_frame = tk.Frame(login_frame, bg=ACCENT_PRIMARY, highlightthickness=0)
border_frame.pack(expand=True, fill="both")

form_frame = tk.Frame(border_frame, bg=BG_SECONDARY)
form_frame.pack(fill="both", expand=True, padx=2, pady=2)

# Form title with icon
form_title = tk.Label(form_frame, text="🔐 SIGN IN", font=FONT_SUBTITLE,
                     fg=ACCENT_SECONDARY, bg=BG_SECONDARY)
form_title.pack(anchor="w", padx=PADDING_LARGE, pady=(PADDING_LARGE, 5))

form_subtitle = tk.Label(form_frame, text="Enter your credentials to continue", 
                        font=("Segoe UI", 9), fg=FG_MUTED, bg=BG_SECONDARY)
form_subtitle.pack(anchor="w", padx=PADDING_LARGE, pady=(0, PADDING_LARGE))

# Separator line
separator = tk.Frame(form_frame, bg=ACCENT_PRIMARY, height=1)
separator.pack(fill="x", padx=PADDING_LARGE, pady=(0, PADDING_LARGE))

# Username field
username_label = tk.Label(form_frame, text="👤 Username", font=FONT_LABEL,
         fg=ACCENT_SECONDARY, bg=BG_SECONDARY)
username_label.pack(anchor="w", padx=PADDING_LARGE, pady=(0, PADDING_SMALL))

username_entry = tk.Entry(form_frame, font=FONT_NORMAL, width=35,
                    bg=ENTRY_BG, fg=ENTRY_FG,
                    insertbackground=ACCENT_SECONDARY, relief="flat",
                    bd=0, borderwidth=0)
username_entry.pack(padx=PADDING_LARGE, pady=(0, PADDING_LARGE), fill="x")

# Password field
password_label = tk.Label(form_frame, text="🔑 Password", font=FONT_LABEL,
         fg=ACCENT_SECONDARY, bg=BG_SECONDARY)
password_label.pack(anchor="w", padx=PADDING_LARGE, pady=(0, PADDING_SMALL))

password_entry = tk.Entry(form_frame, font=FONT_NORMAL, width=35,
                         bg=ENTRY_BG, fg=ENTRY_FG, show="•",
                         insertbackground=ACCENT_SECONDARY, relief="flat",
                         bd=0, borderwidth=0)
password_entry.pack(padx=PADDING_LARGE, pady=(0, PADDING_LARGE*1.5), fill="x")

# Login function
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "johnsmith" and password == "12345":
        build_main_app()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!\n\nDemo: johnsmith / 12345")
        password_entry.delete(0, "end")

# Login button with modern styling
login_btn = create_button(form_frame, "🚀 LOGIN", login, "primary", width=30)
login_btn.pack(pady=(0, PADDING_MEDIUM), padx=PADDING_LARGE, fill="x", ipady=12)

# Demo info with styling
info_frame = tk.Frame(form_frame, bg=BG_SECONDARY)
info_frame.pack(fill="x", padx=PADDING_LARGE, pady=(PADDING_MEDIUM, PADDING_LARGE))

info = tk.Label(info_frame, text="📋 Demo Credentials: johnsmith / 12345",
               font=FONT_SMALL, fg=FG_MUTED, bg=BG_SECONDARY, justify="center")
info.pack(anchor="center")

# Allow Enter key for login
root.bind('<Return>', lambda e: login())

root.mainloop()      

