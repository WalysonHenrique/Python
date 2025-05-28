import sqlite3

class BancoDeDados:
    def __init__(self, nome_arquivo="usuarios.db"):
        self.conexao = sqlite3.connect(nome_arquivo)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()
        
    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        self.conexao.commit()
        
    def inserir_usuario(self, nome, email):
        self.cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        self.conexao.commit()
        
    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()
    
    def limpar_dados(self):
        self.cursor.execute("delete from usuarios")
        self.conexao.commit()
    