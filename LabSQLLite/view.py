from model import BancoDeDados
import tkinter as tk
from tkinter import messagebox


class AplicacaoCadastro:
    def __init__(self, master, controller):
        self.master = master
        self.master.title("Sistema de Cadastro de Usuários")
        self.controller = controller
        self.banco = BancoDeDados()
        self.criar_widgets()
    
    def criar_widgets(self):
       
        frame_formulario = tk.Frame(self.master)
        frame_formulario.pack(padx=20, pady=10)

        tk.Label(frame_formulario, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entrada_nome = tk.Entry(frame_formulario, width=35)
        self.entrada_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_formulario, text="E-mail:").grid(row=1, column=0, sticky="w")
        self.entrada_email = tk.Entry(frame_formulario, width=35)
        self.entrada_email.grid(row=1, column=1, padx=5, pady=5)

     
        frame_botoes = tk.Frame(self.master)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Salvar", command=self.controller.salvar_dados).pack(side="left", padx=10)
        tk.Button(frame_botoes, text="Listar Usuários", command=self.controller.mostrar_usuarios).pack(side="left", padx=10)
        tk.Button(frame_botoes, text="Sair", command=self.master.quit).pack(side="left", padx=10)
        tk.Button(frame_botoes, text="Limpar Dados", command=self.controller.limpar_dados).pack(side="left", padx=10)

    