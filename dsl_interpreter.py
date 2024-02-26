from mydb import StudentManager

def interpret(command, manager):
    tokens = command.split()
    if tokens[0] == "CREATE":
        manager.create_student(tokens[1], int(tokens[2]), tokens[3], tokens[4])
    elif tokens[0] == "DISPLAY":
        students = manager.display_students()
        for student in students:
            print(student)
    elif tokens[0] == "UPDATE":
        manager.update_student(int(tokens[1]), tokens[2], int(tokens[3]), tokens[4], tokens[5])
    elif tokens[0] == "DELETE":
        manager.delete_student(int(tokens[1]))

def main():
    manager = StudentManager("students.db")
    with open("student.dsl") as f:
        for line in f:
            interpret(line.strip(), manager)

if __name__ == "__main__":
    main()
