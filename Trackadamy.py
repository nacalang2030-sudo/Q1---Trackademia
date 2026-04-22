import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

BG_COLOR = "#0D0221"
TAB_BG = "#1A0833"
FG_COLOR = "#E9D8FD"
BTN_COLOR = "#A855F7"
BTN_HOVER = "#D8B4FE"
ENTRY_BG = "#2D1B4E"
ENTRY_FG = "#F5F3FF"

FONT_TITLE = ("Arial", 20, "bold")
FONT_NORMAL = ("Arial", 10)
FONT_SMALL = ("Arial", 8)

DATA_FILE = "student_data.json"
grades = {}
assignments = []

def style_button(btn):
    btn.configure(bg=BTN_COLOR, fg="white", relief="flat", bd=0, padx=10, pady=5)
    btn.bind("<Enter>", lambda e: btn.configure(bg=BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.configure(bg=BTN_COLOR))

def load_file():
    global grades, assignments
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
            grades = data.get("grades", {})
            assignments = data.get("assignments", [])
            messagebox.showinfo("Success", "Data loaded!")
            return True
        except:
            messagebox.showerror("Error", "File corrupted!")
            return False
    else:
        messagebox.showwarning("Error", "No saved file!")
        return False

def save_file():
    if not grades and not assignments:
        messagebox.showwarning("Error", "Nothing to save!")
        return
    try:
        with open(DATA_FILE, "w") as f:
            json.dump({"grades": grades, "assignments": assignments}, f)
        messagebox.showinfo("Success", "Data saved!")
    except:
        messagebox.showerror("Error", "Save failed!")

def calc_gwa(g_dict):
    if not g_dict:
        return 0
    total = 0
    units = 0
    for subject, data in g_dict.items():
        total += data["grade"] * data["units"]
        units += data["units"]
    return total / units if units > 0 else 0

def days_left(deadline_str):
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
        days = (deadline - datetime.now()).days
        return days
    except:
        return None

def format_days(days):
    if days is None:
        return "Invalid date"
    if days < 0:
        return f"OVERDUE ({abs(days)} days)"
    elif days == 0:
        return "DUE TODAY!!!"
    elif days == 1:
        return "DUE TOMORROW"
    elif days <= 3:
        return f"{days} days left (SOON!)"
    else:
        return f"{days} days left"

def main_app():
    root.title("Trackademia - Student Manager")
    root.geometry("1000x700")
    
    top = tk.Frame(root, bg=BG_COLOR)
    top.pack(pady=15, fill="x")
    
    title = tk.Label(top, text="Trackademia Student Manager", font=FONT_TITLE, fg=FG_COLOR, bg=BG_COLOR)
    title.pack()
    
    info_frame = tk.Frame(root, bg=TAB_BG, relief="sunken", bd=1)
    info_frame.pack(fill="x", padx=10, pady=5)
    
    info_label = tk.Label(info_frame, text="Current GWA: N/A | Pending Assignments: 0", 
                         bg=TAB_BG, fg=FG_COLOR, font=FONT_SMALL, justify="left")
    info_label.pack(anchor="w", padx=10, pady=5)
    
    def update_info():
        gwa = calc_gwa(grades)
        pending = sum(1 for a in assignments if not a["done"])
        info_label.config(text=f"Current GWA: {gwa:.2f} | Pending Assignments: {pending}")
    
    tabs = ttk.Notebook(root)
    tabs.pack(fill="both", expand=True, padx=10, pady=10)
    
    # ===== GRADES TAB =====
    g_tab = tk.Frame(tabs, bg=TAB_BG)
    tabs.add(g_tab, text="Grades")

    g_input = tk.Frame(g_tab, bg=TAB_BG, relief="ridge", bd=1)
    g_input.pack(fill="x", padx=10, pady=10)
    
    tk.Label(g_input, text="Subject:", bg=TAB_BG, fg=FG_COLOR, font=FONT_NORMAL, width=12, anchor="w").pack(side="left", padx=5, pady=5)
    subj = ttk.Combobox(g_input, values=["Mathematics 2", "English", "Social Science", "PHEM", "Mathematics 3", "Adtech", "Physics", "Chemistry", "Biology", "Earth Science", "Filipino", "Computer Science"], state="readonly", width=20)
    subj.set("Select Subject")
    subj.pack(side="left", padx=5, pady=5)
    
    tk.Label(g_input, text="Grade (1.0-5.0):", bg=TAB_BG, fg=FG_COLOR, font=FONT_NORMAL, width=15, anchor="w").pack(side="left", padx=5, pady=5)
    grade_in = tk.Entry(g_input, bg=ENTRY_BG, fg=ENTRY_FG, width=10)
    grade_in.pack(side="left", padx=5, pady=5)
    
    tk.Label(g_input, text="Units:", bg=TAB_BG, fg=FG_COLOR, font=FONT_NORMAL, width=8, anchor="w").pack(side="left", padx=5, pady=5)
    units_in = tk.Entry(g_input, bg=ENTRY_BG, fg=ENTRY_FG, width=5)
    units_in.insert(0, "0")
    units_in.pack(side="left", padx=5, pady=5)
    
    grade_box = tk.Text(g_tab, height=13, bg=ENTRY_BG, fg=FG_COLOR, font=("Courier", 9))
    grade_box.pack(pady=10, padx=10, fill="both", expand=True)
    
    def add_grade():
        try:
            s = subj.get()
            if s == "Select Subject" or not s:
                messagebox.showerror("Error", "Pick a subject!")
                return
            g = float(grade_in.get())
            if g < 1.0 or g > 5.0:
                messagebox.showerror("Error", "Grade must be 1.0-5.0!")
                return
            u = float(units_in.get())
            grades[s] = {"grade": g, "units": u}
            grade_in.delete(0, "end")
            units_in.delete(0, "end")
            units_in.insert(0, "0")
            subj.set("Select Subject")
            messagebox.showinfo("Success", f"Added {s}: {g}")
            view_grades()
            update_info()
        except:
            messagebox.showerror("Error", "Invalid input!")
    
    def view_grades():
        grade_box.delete("1.0", "end")
        if grades:
            grade_box.insert("end", "SUBJECT                 GRADE  UNITS\n")
            grade_box.insert("end", "-" * 45 + "\n")
            total = 0
            units = 0
            for s, d in sorted(grades.items()):
                grade_box.insert("end", f"{s:<22} {d['grade']:>6.2f}  {d['units']:>5.1f}\n")
                total += d['grade'] * d['units']
                units += d['units']
            if units > 0:
                gwa = total / units
                grade_box.insert("end", "-" * 45 + "\n")
                grade_box.insert("end", f"{'WEIGHTED GWA':<22} {gwa:>6.2f}\n")
        else:
            grade_box.insert("end", "No grades added yet. Add one above!")

    def del_grade():
        s = subj.get()
        if s == "Select Subject" or not s:
            messagebox.showerror("Error", "Select a subject to delete!")
            return
        if s in grades:
            del grades[s]
            subj.set("Select Subject")
            messagebox.showinfo("Success", f"Deleted {s}!")
            view_grades()
            update_info()
        else:
            messagebox.showerror("Error", "Subject not found!")

    def clear_grades():
        if messagebox.askyesno("Confirm", "Delete ALL grades?"):
            grades.clear()
            view_grades()
            update_info()

    btn_frame1 = tk.Frame(g_tab, bg=TAB_BG)
    btn_frame1.pack(pady=10)

    add_g = tk.Button(btn_frame1, text="Add", command=add_grade)
    view_g = tk.Button(btn_frame1, text="View All", command=view_grades)
    del_g = tk.Button(btn_frame1, text="Delete", command=del_grade)
    clear_g = tk.Button(btn_frame1, text="Clear All", command=clear_grades)

    for btn in [add_g, view_g, del_g, clear_g]:
        btn.pack(side="left", padx=5)
        style_button(btn)

    # ===== ASSIGNMENTS TAB =====
    a_tab = tk.Frame(tabs, bg=TAB_BG)
    tabs.add(a_tab, text="Assignments")

    a_input = tk.Frame(a_tab, bg=TAB_BG, relief="ridge", bd=1)
    a_input.pack(fill="x", padx=10, pady=10)
    
    tk.Label(a_input, text="Name:", bg=TAB_BG, fg=FG_COLOR, font=FONT_NORMAL, width=12, anchor="w").pack(side="left", padx=5, pady=5)
    assign_in = tk.Entry(a_input, bg=ENTRY_BG, fg=ENTRY_FG, width=35)
    assign_in.pack(side="left", padx=5, pady=5)
    
    tk.Label(a_input, text="Due:", bg=TAB_BG, fg=FG_COLOR, font=FONT_NORMAL, width=8, anchor="w").pack(side="left", padx=5, pady=5)
    due_in = tk.Entry(a_input, bg=ENTRY_BG, fg="#888888", width=15)
    PLACEHOLDER = "YYYY-MM-DD"
    due_in.insert(0, PLACEHOLDER)
    due_in.pack(side="left", padx=5, pady=5)

    def due_focus_in(e):
        if due_in.get() == PLACEHOLDER:
            due_in.delete(0, "end")
            due_in.config(fg=ENTRY_FG)

    def due_focus_out(e):
        if not due_in.get().strip():
            due_in.insert(0, PLACEHOLDER)
            due_in.config(fg="#888888")

    due_in.bind("<FocusIn>", due_focus_in)
    due_in.bind("<FocusOut>", due_focus_out)
    
    assign_box = tk.Text(a_tab, height=13, bg=ENTRY_BG, fg=FG_COLOR, font=("Courier", 9))
    assign_box.pack(pady=10, padx=10, fill="both", expand=True)
    
    def add_assign():
        name = assign_in.get().strip()
        due = due_in.get().strip()

        if not name or not due or due == PLACEHOLDER:
            messagebox.showerror("Error", "Enter name and date!")
            return

        try:
            datetime.strptime(due, "%Y-%m-%d")
        except:
            messagebox.showerror("Error", "Date must be YYYY-MM-DD!")
            return

        for item in assignments:
            if item["name"] == name:
                messagebox.showerror("Error", "Already exists!")
                return

        assignments.append({"name": name, "due": due, "done": False})
        assign_in.delete(0, "end")
        due_in.delete(0, "end")
        due_in.insert(0, PLACEHOLDER)
        due_in.config(fg="#888888")
        messagebox.showinfo("Success", f"Added: {name}")
        view_assign()
        update_info()
    
    def view_assign():
        assign_box.delete("1.0", "end")
        if assignments:
            assign_box.insert("end", "ASSIGNMENT              DUE DATE    STATUS           DAYS LEFT\n")
            assign_box.insert("end", "-" * 70 + "\n")
            for item in sorted(assignments, key=lambda x: x['due']):
                days = days_left(item["due"])
                status = "DONE" if item["done"] else "PENDING"
                days_str = format_days(days)
                assign_box.insert("end", f"{item['name']:<20} {item['due']}  {status:<10} {days_str}\n")
        else:
            assign_box.insert("end", "No assignments yet. Add one above!")
    
    def mark_done():
        name = assign_in.get().strip()
        if not name:
            messagebox.showerror("Error", "Enter name!")
            return
        for item in assignments:
            if item["name"] == name:
                item["done"] = True
                assign_in.delete(0, "end")
                messagebox.showinfo("Success", "Marked as done!")
                view_assign()
                update_info()
                return
        messagebox.showerror("Error", "Not found!")
    
    def del_assign():
        name = assign_in.get().strip()
        if not name:
            messagebox.showerror("Error", "Enter name!")
            return
        global assignments
        found = False
        for i, item in enumerate(assignments):
            if item["name"] == name:
                assignments.pop(i)
                found = True
                break
        if found:
            assign_in.delete(0, "end")
            messagebox.showinfo("Success", "Deleted!")
            view_assign()
            update_info()
        else:
            messagebox.showerror("Error", "Not found!")
    
    def clear_assign():
        if messagebox.askyesno("Confirm", "Delete ALL assignments?"):
            assignments.clear()
            view_assign()
            update_info()
    
    btn_frame2 = tk.Frame(a_tab, bg=TAB_BG)
    btn_frame2.pack(pady=10)
    
    add_a = tk.Button(btn_frame2, text="Add", command=add_assign)
    view_a = tk.Button(btn_frame2, text="View All", command=view_assign)
    done_a = tk.Button(btn_frame2, text="Mark Done", command=mark_done)
    del_a = tk.Button(btn_frame2, text="Delete", command=del_assign)
    clear_a = tk.Button(btn_frame2, text="Clear All", command=clear_assign)
    
    for btn in [add_a, view_a, done_a, del_a, clear_a]:
        btn.pack(side="left", padx=5)
        style_button(btn)
    
    # ===== BOTTOM BUTTONS =====
    bottom = tk.Frame(root, bg=BG_COLOR)
    bottom.pack(pady=10, fill="x")
    
    save_btn = tk.Button(bottom, text="Save Data", command=save_file)
    def do_load():
        if load_file():
            view_grades()
            view_assign()
            update_info()
    load_btn = tk.Button(bottom, text="Load Data", command=do_load)
    
    save_btn.pack(side="left", padx=5)
    load_btn.pack(side="left", padx=5)
    
    for btn in [save_btn, load_btn]:
        style_button(btn)
    
    load_file()
    update_info()

# ===== MAIN =====
root = tk.Tk()
root.configure(bg=BG_COLOR)
root.geometry("1000x700")

main_app()

root.mainloop()
