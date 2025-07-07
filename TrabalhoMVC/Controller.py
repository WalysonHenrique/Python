import tkinter as tk
from tkinter import messagebox
from View import Application
from Model import Database
import re


class ControllerApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de cadastro de usuário.")
        self.database = Database()
        self.view = Application(master, self)
        
    
    def is_valid_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def insert_user(self):
        name = self.view.input_name.get().strip()
        mail = self.view.input_mail.get().strip()

        if not name or not mail:
            messagebox.showwarning("Campos Obrigatórios!", "Preencha todos os campos.")
            return

        if not self.is_valid_email(mail):
            messagebox.showerror("E-mail inválido", "Digite um e-mail válido.")
            return

        self.database.insert_user(name, mail)
        messagebox.showinfo("Sucesso!", "Usuário inserido com sucesso.")
        self.view.input_name.delete(0, tk.END)
        self.view.input_mail.delete(0, tk.END)

        
    def list_users(self):
        window = tk.Toplevel(self.master)
        window.title("Usuários Inseridos")
        data = self.database.list_users()
        
        for i, (id, name, mail) in enumerate(data):
            text = f"{i+1}. {name} - {mail}"
            tk.Label(window, text=text).grid(row=i, column=0, sticky="w", padx=10, pady=2)
            
            
    def clear_users(self):
        self.database.clear_users()
        messagebox.showinfo("Dados Excluidos","Dados excluidos com sucesso.")
        
    
    def quit():
        print("sair")

        
        
