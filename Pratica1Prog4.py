import mysql.connector
import hashlib

def conectar(db):
    try:
        con = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        database=db,
        password="root")    
        mycursor = con.cursor()
        print(f"Banco {db} foi conectado!")
        return con, mycursor
    except mysql.connector.errors.ProgrammingError:
        print(f"Criando banco {db}")
        con = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root")
        
        mycursor = con.cursor()
        mycursor.execute(f"create database {db}")
        con.commit()
    
        return con, mycursor
    

def inserir(nome, email, senha):
    con, mycursor = conectar("pratica")
    mycursor.execute("use pratica")
    senhaCriptografada = hashlib.sha256(senha.encode()).hexdigest()

    try:
        mycursor.execute(f"insert into users(nome, email, senha) values ('{nome}', '{email}','{senhaCriptografada}')")
        con.commit()
        con.close()
        print(f"Dados inseridos na tabela!")
    except:
        print(f"Criando tabela e inserindo os dados !")
        mycursor.execute(f"create table users(nome varchar(255), email varchar(255), senha varchar(255))")
        con.commit()
        mycursor.execute(f"insert into users(nome, email, senha) values ('{nome}', '{email}', '{senhaCriptografada}')")
        con.commit()
        con.close()
        
        
def listar():
    con, mycursor = conectar("pratica")
    mycursor.execute("use pratica;")
    
    

    try:
        mycursor.execute("select * from users;")
        dados = mycursor.fetchall()
        for dado in dados:
            print(dado)
    except:
        print("A tabela nao existe")
    
    
    
def validar(email, senha):
    senha = hashlib.sha256(senha.encode()).hexdigest()
    con, mycursor = conectar("pratica")
    mycursor.execute("use pratica;")
    try:
        mycursor.execute(f"select * from users where email = '{email}'")
        resultado = mycursor.fetchone()
        if resultado == None:
            print("Nenhum usuario com este email")
            return
        if resultado[2] == senha:
            print(f"O usuario {resultado[0]} esta validado!")
        else:
            print("Email ou senhas invalidos!")

    except:
        print("A tabela nao existe")
        
        



#listar()
escolha = None
while escolha != 0:
    
    print("Escolha uma açao:")
    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Validar")
    escolha = int(input())

    match escolha:
        case 1:
            nome = input("Insira um nome...")
            email = input("Insira um email...")
            senha = input("Insira a sua senha...")
            
            inserir(nome, email, senha)
        case 2:
            listar()
        case 3:
            email = input("Insira um email...")
            senha = input("Insira a sua senha...")
            validar(email, senha)
        