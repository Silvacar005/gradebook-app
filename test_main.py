import unittest
import os
from main import Student, Gradebook

class TestStudent(unittest.TestCase):

    def test_student_creation(self):
        s = Student("1", "Alice")
        self.assertEqual(s.student_id, "1")
        self.assertEqual(s.name, "Alice")
        self.assertEqual(s.grades, {})

    def test_add_grade_and_average(self):
        s = Student("1", "Alice")
        s.add_grade("Math", 90)
        s.add_grade("Science", 80)
        self.assertEqual(s.get_average(), 85)

    def test_letter_grades(self):
        s = Student("1", "Test")
        s.grades = {"A": 95}
        self.assertEqual(s.get_letter_grade(), "A")
        s.grades = {"B": 85}
        self.assertEqual(s.get_letter_grade(), "B")
        s.grades = {"C": 75}
        self.assertEqual(s.get_letter_grade(), "C")
        s.grades = {"D": 65}
        self.assertEqual(s.get_letter_grade(), "D")
        s.grades = {"F": 50}
        self.assertEqual(s.get_letter_grade(), "F")

    def test_to_and_from_dict(self):
        s = Student("1", "Alice", {"Math": 90})
        data = s.to_dict()
        new_s = Student.from_dict(data)
        self.assertEqual(new_s.student_id, "1")
        self.assertEqual(new_s.name, "Alice")
        self.assertEqual(new_s.grades["Math"], 90)


class TestGradebook(unittest.TestCase):

    def setUp(self):
        # Use a temporary JSON file for testing
        self.test_file = "test_gradebook.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.gradebook = Gradebook(filename=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_student(self):
        s = Student("1", "Bob")
        self.gradebook.add_student(s)
        self.assertEqual(len(self.gradebook.students), 1)

    def test_find_student(self):
        s = Student("2", "Charlie")
        self.gradebook.add_student(s)
        found = self.gradebook.find_student("2")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Charlie")

    def test_record_grade(self):
        s = Student("3", "David")
        self.gradebook.add_student(s)
        self.gradebook.record_grade("3", "History", 88)
        self.assertEqual(s.grades["History"], 88)

    def test_delete_student(self):
        s = Student("4", "Eve")
        self.gradebook.add_student(s)
        result = self.gradebook.delete_student("4")
        self.assertTrue(result)
        self.assertEqual(len(self.gradebook.students), 0)

    def test_save_and_load_data(self):
        s = Student("5", "Frank", {"Math": 90})
        self.gradebook.add_student(s)
        self.gradebook.save_data()

        # Create a new gradebook to load data
        new_gradebook = Gradebook(filename=self.test_file)
        loaded_student = new_gradebook.find_student("5")

        self.assertIsNotNone(loaded_student)
        self.assertEqual(loaded_student.name, "Frank")
        self.assertEqual(loaded_student.grades["Math"], 90)

    def test_class_average(self):
        s1 = Student("6", "Gina", {"Math": 90})
        s2 = Student("7", "Hank", {"Math": 70})
        self.gradebook.add_student(s1)
        self.gradebook.add_student(s2)
        avg = self.gradebook.calculate_class_average()
        self.assertEqual(avg, 80)


if __name__ == "__main__":
    unittest.main()

