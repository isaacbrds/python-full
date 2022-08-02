from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "usuario"
SENHA = 'S3cr3t4#'
HOST = "localhost"
BANCO = "pythonfullcursos"
PORT = 3306

CONEXAO = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONEXAO, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Pessoa(Base):
  __tablename__ = "Pessoa"
  id = Column(Integer, primary_key=True)
  nome = Column(String(100))
  usuario = Column(String(20))
  senha = Column(String(10))

Base.metadata.create_all(engine)