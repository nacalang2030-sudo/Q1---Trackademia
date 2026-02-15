# Trackademia
## Q1 Project – Task Management System (Python)

## Overview
Trackademia is a simple Python-based academic management system designed to help students manage grades, assignments, and class schedules in one centralized console application. The system allows users to input and view grades, monitor assignments with deadlines, and organize class schedules.

It is designed to be lightweight, easy to use, and practical for students.

## Problem Statement
Students often manage grades, assignments, and schedules separately, which can lead to confusion, missed deadlines, and poor academic tracking. Without a centralized system, academic information becomes disorganized.

There is a need for a simple, structured tool that allows students to:
- Store and compute grades
- Track assignments and deadlines
- Organize class schedules

Trackademia provides a centralized and organized solution.

## Objectives
- To develop a simple academic management tool using Python
- To allow users to input and keep track of their subject grades
- To store and display assignments with deadlines
- To manage class schedules efficiently
- To provide an easy-to-use console interface for students

## Key Features
- Add, view, and store subject grades
- Add assignments with deadlines
- View saved assignments
- Add class schedules
- View saved schedules
- Menu-driven interface
- Input validation for invalid menu choices

## Methodology

### System Structure
The system runs using a continuous `while True` loop that displays a menu and allows the user to select options until they choose to exit.

Data is stored using built-in Python data structures:
- **Dictionary** for grades
- **List** for assignments
- **Dictionary** for schedules

### Core Feature Implementation

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
Assignments are stored in a list of tuples:
```python
assignments.append((name, deadline))
```

Each tuple contains:
- Assignment name
- Deadline

The system loops through the list to display saved assignments.

#### Schedule Management
Schedules are stored in a dictionary:
```python
schedules[subject] = schedule
```

Each subject is linked to its scheduled day and time.

## Technologies Used and Justification

### Python
Python was chosen because:
- It is beginner-friendly and readable
- It allows fast development of logic-based systems
- It provides built-in data structures like lists and dictionaries
- It is suitable for console-based applications
- No external libraries were used, keeping the system simple and focused on core programming concepts

## Design Decisions and Trade-offs

### Console-Based Interface
**Decision:** Used a text-based menu system.

**Trade-off:** Less visually interactive than a GUI, however it simplifies development and focuses on logic.

### In-Memory Data Storage
**Decision:** Data is stored in dictionaries and lists during runtime.

**Trade-off:** Data is not saved permanently after the program closes, but this keeps it simpler and avoids file or database complexity.

### Menu Loop Structure
**Decision:** Used `while True` loop for continuous interaction.

**Benefit:** Keeps the program running until the user exits and improves user experience.

## Ethical Considerations
Trackademia follows responsible programming practices:
- No collection of personal or sensitive data
- All code is original and written by the developers
- No misuse of external copyrighted material
- The system avoids storing confidential information

### Programming and Computing Ethics
This project aligns with the ACM Code of Ethics by:
- Ensuring honesty and integrity in coding
- Respecting intellectual property
- Avoiding harm by not collecting unnecessary data
- Providing clear and transparent system behavior

**Reference:**
Association for Computing Machinery. (2018). ACM Code of Ethics and Professional Conduct. https://www.acm.org/code-of-ethics

## Inputs
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
- Exit message

## Logic Plan

### Program Flow
1. Display welcome message
2. Show menu options
3. User selects a choice
4. Program executes corresponding block:
   - Add/View grades
   - Add/View assignments
   - Add/View schedules
5. Return to menu
6. Exit when user selects "0"

## How to Use
1. Run the program
2. Choose a menu option
3. Enter required information
4. View saved data
5. Select "0" to exit
