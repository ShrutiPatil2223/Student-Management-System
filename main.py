# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:29:51 2024

@author: shrut
"""

from tkinter import Tk
from student_gui import StudentGUI

def main():
    root = Tk()
    app = StudentGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
