from functools import reduce
from mydb import Student

# Higher-Order Function
def process_data(students, func):
    return list(map(func, students))

# Side-Effect Free Function
def get_student_age(student):
    return student.age

# Closure
def make_course_filter(course):
    def course_filter(student):
        return student.course == course
    return course_filter

# Final Data Structure
students = [
    Student(1, 'John', 20, 'A', 'Math'),
    Student(2, 'Jane', 21, 'B', 'Science'),
    Student(3, 'Alice', 22, 'C', 'Art'),
]

# Functions as Parameters and Return Values
filter_math_students = make_course_filter('Math')
math_students = list(filter(filter_math_students, students))
total_age = reduce(lambda x, y: x + y, process_data(math_students, get_student_age))

print("Total age of Math students: ", total_age)
