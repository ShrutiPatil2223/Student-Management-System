import unittest
from mydb import StudentManager

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudentManager(":memory:")
        self.manager.create_student("Deepali Swami", 29, "A", "E&TC")
        self.manager.create_student("Alok Rao", 28, "B", "E&TC")

    def test_create_student(self):
        # Test creating a new student
        self.manager.create_student("Pooja Mule", 29, "A", "Computer Science")
        student = self.manager.read_student(3)
        self.assertEqual(student.name, "Pooja Mule")
        self.assertEqual(student.age,29)
        self.assertEqual(student.grade, "A")
        self.assertEqual(student.course, "Computer Science")

    def test_update_student(self):
        # Test updating an existing student
        self.manager.update_student(2, name="Harshal Patil", age=35)
        student = self.manager.read_student(2)
        self.assertEqual(student.name, "Harshal Patil")
        self.assertEqual(student.age, 35)

    def tearDown(self):
        self.manager.close_connection()

if __name__ == "__main__":
    unittest.main()
