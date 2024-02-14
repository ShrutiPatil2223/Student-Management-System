from tkinter import Tk
from student_gui import StudentGUI

def main():
    root = Tk()
    app = StudentGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
