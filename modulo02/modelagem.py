class Pessoas:
  def __init__(self,  nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf

  def logar_sistema(self):
    print(f'{self.nome} - Logando no sistema')
  
pessoa1 = Pessoas('Isaac', 39, '000.211.185-75')

print(pessoa1.nome)
print(pessoa1.cpf)

pessoa1.logar_sistema()