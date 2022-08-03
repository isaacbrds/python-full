from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from inicio import Pessoa


def retorna_session():
  USUARIO = "usuario"
  SENHA = 'S3cr3t4#'
  HOST = "localhost"
  BANCO = "pythonfullcursos"
  PORT = 3306

  CONEXAO = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

  engine = create_engine(CONEXAO, echo=True)
  Session = sessionmaker(bind=engine)
  return Session()


session = retorna_session()

pessoa = session.query(Pessoa).filter(Pessoa.id == 1).all()
print(pessoa[0].nome)
pessoa[0].nome = 'Usuário'
print(pessoa[0].nome)
session.commit()

