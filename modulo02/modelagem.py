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
  
pessoa1 = Pessoas('Isaac', 39, '000.211.185-75')

print(pessoa1.nome)
print(pessoa1.cpf)

pessoa1.logar_sistema()
print(Pessoas.possui_boca)