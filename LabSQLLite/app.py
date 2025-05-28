from controller import ControllerAplicacao
import tkinter as tk
from tkinter import messagebox
import sqlite3

if __name__ == '__main__':
    root = tk.Tk()
    app = ControllerAplicacao(root)
    root.mainloop()