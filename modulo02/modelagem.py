class Pessoas:
  possui_boca = True
  raca = "Humana"
  def __init__(self,  nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf

  def retorna_nome(self):
    return self.nome

  def logar_sistema(self):
    print(f'{self.retorna_nome()} - Logando no sistema')
  
  @classmethod
  def andar(cls):
    cls.pernas = 2
    return None

  @staticmethod
  def e_adulto(idade):
    if idade > 18:
      return True
    return False

pessoa1 = Pessoas('Isaac', 39, '000.211.185-75')

print(pessoa1.nome)
print(pessoa1.cpf)

pessoa1.logar_sistema()
print(Pessoas.possui_boca)

Pessoas.andar()

print(Pessoas.pernas)

print(Pessoas.e_adulto(20))