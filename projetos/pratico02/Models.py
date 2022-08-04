from sqlalchemy import create_engine, String, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conexao = "sqlite:///projeto.db"

engine = create_engine(conexao, echo=True)
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()


class Usuario(Base):
  __tablename__ = "Usuario"
  id = Column(Integer, primary_key=True)
  nome = Column(String(100))
  email = Column(String(80))
  senha = Column(String(100))

Base.metadata.create_all(engine)

