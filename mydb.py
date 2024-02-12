# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:30:41 2024

@author: shrut
"""

import sqlite3

class Student:
    def __init__(self, id, name, age, grade, course):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course

class StudentManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
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
        self.cur.execute("INSERT INTO students (name, age, grade, course) VALUES (?, ?, ?, ?)", (name, age, grade, course))
        self.conn.commit()

    def read_student(self, id):
        self.cur.execute("SELECT * FROM students WHERE id=?", (id,))
        row = self.cur.fetchone()
        if row:
            return Student(row[0], row[1], row[2], row[3], row[4])
        return None

    def update_student(self, id, name=None, age=None, grade=None, course=None):
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
            self.cur.execute("UPDATE students SET name=?, age=?, grade=?, course=? WHERE id=?", (student.name, student.age, student.grade, student.course, student.id))
            self.conn.commit()
            return True
        return False

    def delete_student(self, id):
        student = self.read_student(id)
        if student:
            self.cur.execute("DELETE FROM students WHERE id=?", (id,))
            self.conn.commit()
            return True
        return False

    def display_students(self):
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        return rows

    def close_connection(self):
        self.conn.close()
