# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:30:15 2024

@author: shrut
"""

from tkinter import Frame, StringVar, Entry, Label, Button, messagebox, ttk
from mydb import StudentManager

class StudentGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management System")

        self.frame1 = Frame(master)
        self.frame1.pack(padx=10, pady=10)

        self.frame2 = Frame(master)
        self.frame2.pack(padx=10, pady=10)

        f = ('Times new roman', 14)

        # variables
        self.namevar = StringVar()
        self.agevar = StringVar()
        self.gradevar = StringVar()
        self.coursevar = StringVar()

        # Label widgets
        Label(self.frame1, text='Name:', font=f).grid(row=1, column=0, sticky='w')
        Label(self.frame1, text='Age:', font=f).grid(row=2, column=0, sticky='w')
        Label(self.frame1, text='Course:', font=f).grid(row=3, column=0, sticky='w')
        Label(self.frame1, text='Grade:', font=f).grid(row=4, column=0, sticky='w')
        
        # Entry widgets
        self.entry_name = Entry(self.frame1, font=f, textvariable=self.namevar)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5, sticky='we')
        self.entry_age = Entry(self.frame1, font=f, textvariable=self.agevar)
        self.entry_age.grid(row=2, column=1, padx=10, pady=5, sticky='we')
        self.entry_course = Entry(self.frame1, font=f, textvariable=self.coursevar)
        self.entry_course.grid(row=3, column=1, padx=10, pady=5, sticky='we')
        self.entry_grade = Entry(self.frame1, font=f, textvariable=self.gradevar)
        self.entry_grade.grid(row=4, column=1, padx=10, pady=5, sticky='we')

        # Button widgets
        self.button_create_student = Button(self.frame1, text="Create Student", font=f, command=self.create_student)
        self.button_create_student.grid(row=1, column=2, sticky='ew', padx=(20, 0))

        self.button_display_students = Button(self.frame1, text="Display Students", font=f, command=self.display_students)
        self.button_display_students.grid(row=2, column=2, sticky='ew', padx=(20, 0))

        self.button_update_student = Button(self.frame1, text="Update Student", font=f, command=self.update_student)
        self.button_update_student.grid(row=3, column=2, sticky='ew', padx=(20, 0))

        self.button_delete_student = Button(self.frame1, text="Delete Student", font=f, command=self.delete_student)
        self.button_delete_student.grid(row=4, column=2, sticky='ew', padx=(20, 0))

        # Treeview widget
        self.tv = ttk.Treeview(self.frame2, columns=(1, 2, 3, 4, 5), show='headings', height=8)
        self.tv.pack(side="left")

        self.tv.column(1, anchor='center', stretch='no', width=50)
        self.tv.column(2, anchor='center')
        self.tv.column(3, anchor='center')
        self.tv.column(4, anchor='center')
        self.tv.column(5, anchor='center')
        self.tv.heading(1, text="ID")
        self.tv.heading(2, text="Name")
        self.tv.heading(3, text="Age")
        self.tv.heading(4, text="Course")
        self.tv.heading(5, text="Grade")

        self.manager = StudentManager("students.db")

    def create_student(self):
        name = self.namevar.get()
        age = self.agevar.get()
        grade = self.gradevar.get()
        course = self.coursevar.get()

        if name and age and grade and course:
            self.manager.create_student(name, age, grade, course)
            messagebox.showinfo("Success", "Student added successfully.")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def display_students(self):
        for record in self.tv.get_children():
            self.tv.delete(record)

        students = self.manager.display_students()
        for student in students:
            self.tv.insert("", "end", values=(student[0], student[1], student[2], student[4], student[3]))

    def update_student(self):
        selected_item = self.tv.selection()
        if selected_item:
            selected_id = self.tv.item(selected_item, 'values')[0]
            name = self.namevar.get()
            age = self.agevar.get()
            grade = self.gradevar.get()
            course = self.coursevar.get()

            if self.manager.update_student(selected_id, name, age, grade, course):
                messagebox.showinfo("Success", "Student updated successfully.")
                self.clear_fields()
                self.display_students()
            else:
                messagebox.showerror("Error", "Student not found.")
        else:
            messagebox.showerror("Error", "Please select a student to update.")

    def delete_student(self):
        selected_item = self.tv.selection()
        if selected_item:
            selected_id = self.tv.item(selected_item, 'values')[0]
            if self.manager.delete_student(selected_id):
                messagebox.showinfo("Success", "Student deleted successfully.")
                self.clear_fields()
                self.display_students()
            else:
                messagebox.showerror("Error", "Student not found.")
        else:
            messagebox.showerror("Error", "Please select a student to delete.")

    def clear_fields(self):
        self.namevar.set("")
        self.agevar.set("")
        self.gradevar.set("")
        self.coursevar.set("")