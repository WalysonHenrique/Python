from database import Base, engine
from models import User
# Não altera a estrutura das tabelas existentes
Base.metadata.create_all(bind=engine)