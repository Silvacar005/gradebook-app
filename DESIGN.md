DESIGN DOCUMENT:

# 1. Introduction
This document explains the system architecture, class structure, design decisions, and OOP principles used in the *Student Grade Management System*. The application combines a clean data model, persistent storage, and a Tkinter-based GUI.

---

# 2. System Architecture

The core of the system is divided into 3 layers:

    ### **1. Data Model Layer**
    - `Student` class  
    - `Gradebook` class  
    Handles logic, storage, calculations, and validation.

    ### **2. Application Logic Layer**
    - Methods that add/delete students, record grades, calculate averages, etc.

    ### **3. User Interface Layer (GUI)**
    - `GradebookApp` class using Tkinter  
    - Handles buttons, forms, error messages, listbox updates.

    ### Data Flow
    User Input → GUI → Gradebook Methods → Student Objects → JSON Storage
---

# 3. Class Descriptions & OOP Principles

### ### **Student Class**
Represents a single student and stores:
- `student_id`
- `name`
- `grades` (dictionary: course → numeric grade)

#### Encapsulation
- Grades are stored internally and only modified through `add_grade()`.
- Average and letter grade are calculated using methods, not manually by the user.

#### Polymorphism
- The `get_letter_grade()` method reacts differently depending on numerical values.

### **Gradebook Class**
Manages the collection of `Student` objects.

Responsibilities:
- Add and delete students
- Find students by ID
- Record grades
- Save and load data through JSON
- Calculate class average

#### Encapsulation
- Students are stored inside the class and cannot be edited directly.

#### Persistence
- Uses JSON to store all records in `gradebook_data.json`.

### **GradebookApp Class (GUI)**
Tkinter-based interface providing:
- Entry fields
- Buttons
- Listbox visual display
- Message boxes for warnings/errors

#### Role
Acts as the controller that bridges user actions with the gradebook system.

---

## 4. Design Pattern Used
### **Factory-Like Behavior in Student.from_dict()**
Although a full design pattern implementation is not required, the project uses a **Factory-style method** in:
@staticmethod
def from_dict(data):

This method constructs a `Student` object cleanly from raw JSON data.

This is functionally similar to the Factory pattern because it abstracts object creation and cleans the data before initializing the object.

---

## 5. Error Handling
The GUI includes input validation and prevents:
- Empty name/ID fields
- Adding duplicate student IDs
- Entering non-numeric grades
- Editing/deleting non-existent students

Messages use:
messagebox.showwarning()
messagebox.showerror()
messagebox.showinfo()

---

## 6. Testing Strategy

To test the system, `unittest` can be used with tests such as:

### **Student Class Tests**
- Adding grades
- Calculating averages properly
- Letter grade conversion

### **Gradebook Class Tests**
- Adding/deleting students
- JSON load/save consistency
- Recording grades correctly

Sample structure:
tests/
test_student.py
test_gradebook.py





---

## 7. Reflection: What I Learned

Through this project, I learned:

- How to build a full GUI using Tkinter  
- How to structure a project using OOP principles  
- How to implement persistent storage using JSON  
- How to manage listboxes, inputs, data validation, and message dialogs  
- How to design a clean architecture that separates logic from presentation  

### Possible Future Improvements
- Adding a menu bar or settings page  
- Exporting student reports to PDF or CSV  
- Adding charts to visualize grade distribution  
- Improving UI styling  
- Adding sorting/search features  

---

## 8. Conclusion
This project demonstrates a complete, functional, and well-organized application that uses object-oriented programming, a GUI framework, persistent storage, and proper design principles. It is structured for maintainability and easy expansion in future versions.
