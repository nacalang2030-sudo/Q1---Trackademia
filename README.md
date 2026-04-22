Trackademia is a Python-based academic management system built using Tkinter GUI. It helps students organize their grades and assignments in one centralized and interactive interface.

The system allows users to:

Input and compute weighted grades (GWA)
Track assignments with deadlines
Monitor pending and completed tasks
Save and load data using a JSON file

It is designed to be simple, visually organized, and practical for everyday student use.

#Problem Statement#

Students often track grades and assignments separately, which leads to:

Missed deadlines
Disorganized academic data
Difficulty computing overall performance

There is a need for a centralized tool that allows students to:

Store and compute grades with units
Track assignment deadlines
Monitor academic progress in real time

Trackademia provides a structured and user-friendly solution.

##Objectives##

Develop a GUI-based academic tool using Python Tkinter
Allow users to input and manage grades with units
Compute General Weighted Average (GWA)
Enable assignment tracking with deadline monitoring
Provide data persistence using JSON
Create an intuitive and easy-to-use interface
Key Features
Grades Management
Add subject grades (1.0 – 5.0)
Input subject units
Automatically compute weighted GWA
View all grades in a formatted table
Delete individual subjects or clear all
Assignment Tracker
Add assignments with due dates (YYYY-MM-DD)
Automatically calculates days remaining
Status labels:
DONE
PENDING
Deadline indicators:
OVERDUE
DUE TODAY
DUE TOMORROW
SOON (≤ 3 days)
Mark assignments as done
Delete or clear assignments

#Data Management#

Save data to student_data.json
Load saved data anytime

Error handling for:
Missing file
Corrupted file
Empty save attempts
Dashboard Info Bar

##Displays:##

Current GWA
Number of pending assignments
Technologies Used
Python
Core programming language
Handles logic and data structures
Tkinter
GUI framework for interface
Uses widgets such as Frame, Label, Button, Text, and Notebook
JSON
Used for data persistence
Stores grades and assignments
Built-in Libraries
datetime for deadline calculations
os for file handling
System Structure
Data Storage

##Grades (Dictionary):##

grades = {
    "Math": {"grade": 1.5, "units": 3}
}

Assignments (List of Dictionaries):

assignments = [
    {"name": "Project", "due": "2026-05-01", "done": False}
]
Core Logic
GWA Calculation
GWA = sum(grade × units) / total units

Deadline Tracking

Converts string to date
Computes difference from current date
Outputs readable status (e.g., “2 days left”)

#How to Use#

Run the program
The main window will open
Grades Tab
Select subject
Enter grade and units
Click Add
Click View All to display
Assignments Tab
Enter assignment name
Enter deadline (YYYY-MM-DD)
Click Add
Use:
Mark Done
Delete
View All
Data
Click Save Data to store progress
Click Load Data to retrieve saved data
Design Decisions and Trade-offs

##GUI-Based Interface##

Provides a more user-friendly experience compared to text-based systems
Requires more development effort

##JSON Storage##

Enables persistent data saving
Requires manual save/load actions

#In-Memory Data Structures#

Simple and efficient for runtime operations
Data is lost if not saved
Ethical Considerations
No collection of personal or sensitive data
All code is original
No external copyrighted material used
Data is stored locally and not shared externally
Programming Ethics

This project aligns with the ACM Code of Ethics by:
Ensuring honesty and integrity in development
Respecting intellectual property
Avoiding harm by minimizing data collection
Providing transparent system behavior

##Reference:##

Association for Computing Machinery. (2018). ACM Code of Ethics and Professional Conduct. https://www.acm.org/code-of-ethics

##Contributors##

Nadine Angela A. Calang
Liahm Pyia A. Gumanit
MC David C. Demiar
