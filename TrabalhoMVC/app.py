import tkinter as tk
from tkinter import messagebox
from Controller import ControllerApplication
import sqlite3

if __name__ == '__main__':
    root = tk.Tk()
    app = ControllerApplication(root)
    root.mainloop()