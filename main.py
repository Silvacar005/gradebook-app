# Author: Carlos Silva
import tkinter as tk
from tkinter import messagebox
import json
import os


class Student:
    def __init__(self, student_id, name, grades=None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades else {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_average(self):
        valid_grades = [g for g in self.grades.values() if isinstance(g, (int, float))]
        if not valid_grades:
            return 0
        return sum(valid_grades) / len(valid_grades)

    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {"student_id": self.student_id, "name": self.name, "grades": self.grades}

    @staticmethod
    def from_dict(data):
        clean_grades = {
            k: v for k, v in data.get("grades", {}).items() if isinstance(v, (int, float))
        }
        return Student(data["student_id"], data["name"], clean_grades)


class Gradebook:
    def __init__(self, filename="gradebook_data.json"):
        self.students = []
        self.filename = filename
        self.load_data()

    def add_student(self, student):
        self.students.append(student)
        self.save_data()

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def delete_student(self, student_id):
        """Delete a student by ID."""
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            self.save_data()
            return True
        return False

    def record_grade(self, student_id, course, grade):
        student = self.find_student(student_id)
        if student:
            student.add_grade(course, grade)
            self.save_data()
            return True
        return False

    def calculate_class_average(self):
        if not self.students:
            return 0
        total = sum(s.get_average() for s in self.students)
        return total / len(self.students)

    def save_data(self):
        data = [s.to_dict() for s in self.students]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(d) for d in data]


class GradebookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Management System")
        self.root.geometry("620x580")

        self.gradebook = Gradebook()

        tk.Label(root, text="Add Student", font=("Arial", 12, "bold")).pack(pady=5)

        self.id_label = tk.Label(root, text="Student ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(root, width=30)
        self.id_entry.pack(pady=2)

        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack(pady=2)

        # Add / Delete buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        self.add_student_btn = tk.Button(btn_frame, text="Add Student", command=self.add_student)
        self.add_student_btn.grid(row=0, column=0, padx=5)

        self.delete_student_btn = tk.Button(btn_frame, text="Delete Student", command=self.delete_student)
        self.delete_student_btn.grid(row=0, column=1, padx=5)

        tk.Label(root, text="Record Grade", font=("Arial", 12, "bold")).pack(pady=5)

        self.course_label = tk.Label(root, text="Course:")
        self.course_label.pack()
        self.course_entry = tk.Entry(root, width=30)
        self.course_entry.pack(pady=2)

        self.grade_label = tk.Label(root, text="Grade (0–100):")
        self.grade_label.pack()
        self.grade_entry = tk.Entry(root, width=30)
        self.grade_entry.pack(pady=2)

        self.record_btn = tk.Button(root, text="Record Grade", command=self.record_grade)
        self.record_btn.pack(pady=5)

        self.avg_btn = tk.Button(root, text="Show Class Average", command=self.show_class_average)
        self.avg_btn.pack(pady=5)

        self.listbox = tk.Listbox(root, width=75, height=18)
        self.listbox.pack(pady=10)

        self.refresh_listbox()

    def add_student(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()

        if not student_id or not name:
            messagebox.showwarning("Input Error", "Please fill in both ID and Name.")
            return

        if self.gradebook.find_student(student_id):
            messagebox.showwarning("Duplicate ID", "A student with this ID already exists.")
            return

        student = Student(student_id, name)
        self.gradebook.add_student(student)
        self.refresh_listbox()
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Student '{name}' added successfully!")

    def delete_student(self):
        student_id = self.id_entry.get().strip()
        if not student_id:
            messagebox.showwarning("Input Error", "Enter the Student ID to delete.")
            return

        student = self.gradebook.find_student(student_id)
        if not student:
            messagebox.showerror("Error", "Student not found.")
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{student.name}'?")
        if confirm:
            self.gradebook.delete_student(student_id)
            self.refresh_listbox()
            messagebox.showinfo("Deleted", f"Student '{student.name}' has been deleted.")
            self.id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)

    def record_grade(self):
        student_id = self.id_entry.get().strip()
        course = self.course_entry.get().strip()
        grade = self.grade_entry.get().strip()

        if not student_id or not course or not grade:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        try:
            grade = float(grade)
        except ValueError:
            messagebox.showerror("Invalid Input", "Grade must be a number.")
            return

        success = self.gradebook.record_grade(student_id, course, grade)
        if success:
            self.refresh_listbox()
            self.course_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Grade recorded successfully!")
        else:
            messagebox.showerror("Error", "Student not found.")

    def show_class_average(self):
        avg = self.gradebook.calculate_class_average()
        messagebox.showinfo("Class Average", f"Class Average: {avg:.2f}")

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for s in self.gradebook.students:
            avg = s.get_average()
            self.listbox.insert(tk.END, f"{s.student_id} - {s.name} | Avg: {avg:.2f} ({s.get_letter_grade()})")
            if s.grades:
                for course, grade in s.grades.items():
                    self.listbox.insert(tk.END, f"     • {course}: {grade}")
            self.listbox.insert(tk.END, "----------------------------------------")


if __name__ == "__main__":
    root = tk.Tk()
    app = GradebookApp(root)
    root.mainloop()
