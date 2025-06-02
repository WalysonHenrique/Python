from sqlalchemy import Column, Integer, String
from database import Base
class User(Base):
    __tablename__ = "users" # nome da tabela no banco
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)
