import sqlite3

class Student:
    """Represents a student."""
    def __init__(self, id, name, age, grade, course):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course

class StudentManager:
    """Manages student data in a SQLite database."""
    def __init__(self, db_file):
        """Initializes the StudentManager with the given database file."""
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates the 'students' table in the database."""
        self.cur.execute("DROP TABLE IF EXISTS students")
        self.cur.execute("""
            CREATE TABLE students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                grade TEXT,
                course TEXT
            )
        """)
        self.conn.commit()

    def create_student(self, name, age, grade, course):
        """Inserts a new student into the database."""
        self.cur.execute("INSERT INTO students (name, age, grade, course) VALUES (?, ?, ?, ?)",
                         (name, age, grade, course))
        self.conn.commit()

    def read_student(self, id):
        """Reads a student from the database by id."""
        self.cur.execute("SELECT * FROM students WHERE id=?", (id,))
        row = self.cur.fetchone()
        if row:
            return Student(row[0], row[1], row[2], row[3], row[4])
        return None

    def update_student(self, id, name=None, age=None, grade=None, course=None):
        """Updates an existing student's information in the database."""
        student = self.read_student(id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            if course:
                student.course = course
            self.cur.execute("UPDATE students SET name=?, age=?, grade=?, course=? WHERE id=?",
                             (student.name, student.age, student.grade, student.course, student.id))
            self.conn.commit()
            return True
        return False

    def delete_student(self, id):
        """Deletes a student from the database by id."""
        student = self.read_student(id)
        if student:
            self.cur.execute("DELETE FROM students WHERE id=?", (id,))
            self.conn.commit()
            return True
        return False

    def display_students(self):
        """Displays all students in the database."""
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        return rows

    def close_connection(self):
        """Closes the database connection."""
        self.conn.close()
