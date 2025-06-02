from models import User # Usa a classe/model
from database import SessionLocal
db = SessionLocal()
novo_user = User(nome="Athus",
    email="athus@email.com",
    senha="1234")
db.add(novo_user)
db.commit()
