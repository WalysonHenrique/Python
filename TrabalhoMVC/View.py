import tkinter as tk
from tkinter import messagebox
from Model import Database
import tkinter.ttk as ttk
class Application:
    def __init__(self, master, controller):
        self.master = master
        self.master.title("Sistema de cadastro de usuários.")
        self.controller = controller
        self.data = Database()
        self.create_widgets()
        
        
    def create_widgets(self):
        frame_forms = tk.Frame(self.master)
        frame_forms.pack(padx=20, pady=10)
        
        tk.Label(frame_forms, text="Name:").grid(row=0, column=0, sticky="w")
        self.input_name = ttk.Entry(frame_forms, width=35)
        self.input_name.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame_forms, text="Mail:").grid(row=1, column=0, sticky="w")
        self.input_mail = ttk.Entry(frame_forms, width=35)
        self.input_mail.grid(row=1, column=1, padx=5, pady=5)
        
        frame_button = tk.Frame(self.master)
        frame_button.pack(pady=10)
        
        ttk.Button (frame_button, text="Salvar", command=self.controller.insert_user).pack(side="left", padx=10)
        ttk.Button (frame_button, text="Listar Usuários", command=self.controller.list_users).pack(side="left", padx=10)
        ttk.Button (frame_button, text="Sair", command=self.master.quit).pack(side="left", padx=10)
        ttk.Button (frame_button, text="Limpar Registros", command=self.controller.clear_users).pack(side="left", padx=10)
        
        
        
        