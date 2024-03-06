from tkinter import Tk
from student_gui import StudentGUI

def main():
    """Main function to initialize the Tkinter application.""" 
    root = Tk()
    StudentGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
