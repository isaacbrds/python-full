pessoas = []

while True:
  opcao = input('Digite 1 para cadastrar uma pessoa ou 2 para sair: ')
  if opcao == '1':
    pessoa = {'nome': input('Digite o nome da pessoa: '),
               'idade': input('Digite idade da pessoa: '),
               'altura': input('Digite a altura da pessoa: ') 
               }
    pessoas.append(pessoa) 
  else:
    break
