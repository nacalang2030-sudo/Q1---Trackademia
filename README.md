# Trackademia
## Q1 Project – Task Management System (Python) 

## Overview Trackademia is a simple Python-based academic management system designed to help students manage grades, assignments, and class schedules in one centralized Graphical User Interface (GUI). The system allows users to log in, input and view grades, monitor assignments with deadlines, and organize class schedules.

It is designed to be lightweight, easy to use, and practical for students. 

## Problem Statement Students often manage grades, assignments, and schedules separately, which can lead to confusion, missed deadlines, and poor academic tracking. Without a centralized system, academic information becomes disorganized.

There is a need for a simple, structured tool that allows students to:
- Store and compute grades
- Track assignments and deadlines
- Organize class schedules
 Trackademia provides a centralized and organized solution.

## Objectives - To develop a simple academic management tool using Python's Tkinter library.\ 
- To implement a secure log in gateway for user authentication.
- To allow users to input and keep track of their subject grades
- To store and display assignments with deadlines
- To manage class schedules efficiently
- To provide an easy-to-useconsole interface for students

## Key Features
- Log in system
- Add, view, and store subject grades
- Add assignments with deadlines
- View saved assignments
- Add class schedules
- View saved schedules
- Menu-driven interface
- Input validation for invalid menu choices

## Methodology

### System Structure
The system is built using a GUI-based:
- **login system** autthenticates user credentials
- **main application** displays a tabbed interface using ttk.Notebook
- **Tabs** Grades, Assignments, schedules

### Core Feature Implementation

#### Log in system
- validates username and password
- displays success or erros using messagebox
- shows the main application after succesfully logging in


#### Grade Storage and Average Calculation
Grades are stored in a dictionary:
```python
grades = {}
```

Each subject is used as a key, and the grade is stored as its value.

When viewing grades:
- The program iterates through the dictionary
- It computes the average using: `average = sum(grades.values()) / len(grades)`

#### Assignment Management
Assignments are stored in a list of dictionaries:
```python
assignments.append({
    "name": name,
    "due": deadline,
    "completed": False
})
```     

Each assignments contains:
- Assignment name
- Deadline

The system loops through the list to display saved assignments.

#### Schedule Management
Schedules are stored in a list of dictionaries:
```python
schedules.append({
    "event": subject,
    "time": time
})
```

Each schedule contains:
- Event or subject name
- Day and time

## Technologies Used and Justification

### Python
Python was chosen because:
- It is beginner-friendly and readable
- It allows fast development of logic-based systems
- It provides built-in data structures like lists and dictionaries
- It supports GUI development through Tkinter library
- No external libraries were used, keeping the system simple and focused on core programming concepts

## Design Decisions and Trade-offs

### GUI-Based Interface
**Decision:** Used a JSON file storage to save and load data.

**Trade-off:**  More complex to develop than a text-based interface, but significantly improves user experience and visual interaction.


### In-Memory Data Storage
**Decision:** Data is stored in dictionaries and lists during runtime.

**Trade-off:** Data is required manual saving to preserve data, but this keeps it simpler and easy to manage.

### Menu Loop Structure
**Decision:** Used Tkinter's eent-driven programming.

**Benefit:** Smoother user interaction through buttons and GUI events.

## Ethical Considerations
Trackademia follows responsible programming practices:
- No collection of personal or sensitive data
- All code is original and written by the developers
- No misuse of external copyrighted material
- The data is stored locally in a JSON file and is not shared externally.

### Programming and Computing Ethics
This project aligns with the ACM Code of Ethics by:
- Ensuring honesty and integrity in coding
- Respecting intellectual property
- Avoiding harm by not collecting unnecessary data
- Providing clear and transparent system behavior

**Reference:**
Association for Computing Machinery. (2018). ACM Code of Ethics and Professional Conduct. https://www.acm.org/code-of-ethics

## Inputs
- Username and password (string)
- Subject name (string)
- Grade (float)
- Assignment name (string)
- Assignment deadline (string)
- Subject schedule (string)
- Menu choice (string)

## Outputs
- Display of stored grades
- Computed average grade
- Display of assignments with deadlines
- Display of schedules
- Confirmation messages (e.g., "Grades saved", "Assignment saved!")
- saved data file (student_data,json)
- Exit message

## Logic Plan

### Program Flow
1. Display login window
2. User enters username and password
3. if valid, main application window will load
4. Show menu options
5. User selects a choice
6. Program executes corresponding block:
   - Add/View grades
   - Add/View assignments
   - Add/View schedules
7. Save changes or load data using JSON file
8. Return to menu
9. Exit when user selects "0"

## How to Use
1. Run the program
2. shows log in window
3. Choose through tabs:
   - Grades
   - assignments
   - schedules
5. Enter required information
6. Click buttons to manage data
7. Use Save Data to store progress and Load Data to retrieve it

## Contributors
1. Nadine Angela A. Calang
2. Liahm Pyia A. Gumanit
3. MC David C. Demiar
6. Select "0" to exit
