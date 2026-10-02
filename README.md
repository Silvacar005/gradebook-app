# Student Grade Management System

A desktop gradebook application built with **Python** and **Tkinter**. It provides a simple graphical interface for managing students and course grades while demonstrating object-oriented design, persistent JSON storage, input validation, and automated testing.

## Features

- Add and delete students using unique student IDs
- Record grades by course
- Calculate individual student averages and letter grades
- Calculate the overall class average
- Save and reload gradebook data automatically with JSON
- Validate required fields, duplicate IDs, and numeric grade input
- Display student records and course grades in a Tkinter interface
- Unit tests for the core `Student` and `Gradebook` functionality

## Technologies

- **Python 3**
- **Tkinter** for the desktop GUI
- **JSON** for local data persistence
- **unittest** for automated testing

## Project Structure

```text
gradebook-app/
├── main.py          # Application logic and Tkinter GUI
├── test_main.py     # Unit tests
├── DESIGN.md        # Architecture and design notes
├── Data/            # Project data directory
└── Tests/           # Testing-related files
```

The application is organized around three classes:

- `Student` — stores a student's ID, name, and grades and calculates averages and letter grades.
- `Gradebook` — manages students, records grades, calculates the class average, and handles JSON persistence.
- `GradebookApp` — provides the Tkinter interface and connects user actions to the gradebook logic.

## Getting Started

### Requirements

- Python 3.8 or newer
- Tkinter (included with most standard Python installations)

### Run the application

```bash
cd gradebook-app
python main.py
```

Student data is saved locally to `gradebook_data.json` and loaded again when the application starts.

### Run the tests

From the application directory:

```bash
python -m unittest test_main.py
```

## What This Project Demonstrates

This project was built to practice turning core programming concepts into a complete desktop application. It demonstrates class-based design, separation of application logic from the user interface, file persistence, validation and error handling, and unit testing.

## Future Improvements

Potential extensions include search and sorting, CSV/PDF report export, grade-distribution charts, and a more polished interface.

## Author

**Carlos Silva**  
Computer Science student interested in software development, web development, and building practical applications.
