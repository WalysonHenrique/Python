from database import SessionLocal
from sqlalchemy import text
from models import User
db = SessionLocal()
user = db.query(User).filter_by(email="athus@email.com").first()    

def listar(user):
    if (user):
        print(user.id, user.nome, user.senha)
    else:
        print("Nenhum usuario encontrado")
    
def deletar(user):
    db.delete(user) # user funciona como key para o ORM
    db.commit()

def alterar(user):
    user.nome = "Walyson"
    db.commit()
    
def inserir():
    novo_user = User(nome="Athus",
    email="athus@email.com",
    senha="1234")
    db.add(novo_user)
    db.commit()
    


deletar(user)