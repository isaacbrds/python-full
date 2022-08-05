from Models import Usuario
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def retorna_session():
  conexao = "sqlite:///projeto.db"
  engine = create_engine(conexao, echo=True)
  Session = sessionmaker(bind=engine)
  return Session()

class ControllerCadastro:
  @classmethod
  def verifica_dados(cls, nome, email, senha):
    if len(nome) > 100 or len(nome) < 3:
      return 2
    if len(email) > 80:
      return 3
    if len(senha) > 100 or len(senha) < 6:
      return 4
    
    return 1
  
  @classmethod
  def cadastrar(cls, nome, email, senha):
    session = retorna_session()
    usuario = session.query(Usuario).filter(Usuario.email == email).all()
    
    if len(usuario) > 0:
      return 5

    dados_verificados = cls.verifica_dados(nome, email, senha)

    if dados_verificados != 1:
      
      return dados_verificados
    
    try:
      senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
      
      novo_usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
      session.add(novo_usuario)
      session.commit()
      return 1
    
    except:
      return '3 Ocorreu uma exceção'

  @classmethod
  def busca_usuario(cls, email):
    session = retorna_session()
    usuario = session.query(Usuario).filter(Usuario.email == email).all()
    return usuario

  @classmethod
  def get_usuarios(cls):
    session = retorna_session()
    usuarios = session.query(Usuario).all()
    return usuarios



print(ControllerCadastro.cadastrar(2, 'Usuario', 'usuario@mail.com', '123456'))
for i in ControllerCadastro.get_usuarios():
  print(str(i.id) + "|" + i.nome + "|" + i.email)