from model import BancoDeDados
import tkinter as tk
from tkinter import messagebox
from view import AplicacaoCadastro

class ControllerAplicacao:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Cadastro de Usuários")
        self.banco = BancoDeDados()
        self.view = AplicacaoCadastro(master, self)

        
    def salvar_dados(self):
        nome = self.view.entrada_nome.get().strip()
        email = self.view.entrada_email.get().strip()

        if not nome or not email:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return

        self.banco.inserir_usuario(nome, email)
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        self.view.entrada_nome.delete(0, tk.END)
        self.view.entrada_email.delete(0, tk.END)
    
    def mostrar_usuarios(self):
        janela = tk.Toplevel(self.master)
        janela.title("Usuários Cadastrados")
        dados = self.banco.listar_usuarios()

        for i, (id, nome, email) in enumerate(dados):
            texto = f"{i+1}. {nome} - {email}"
            tk.Label(janela, text=texto).grid(row=i, column=0, sticky="w", padx=10, pady=2)
            
            
    def limpar_dados(self):
        self.banco.limpar_dados()
        messagebox.showinfo("Dados Excluidos","Dados excluidos com sucesso!")

 
        