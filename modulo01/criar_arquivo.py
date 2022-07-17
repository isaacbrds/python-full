arquivo = open('arquivo.txt', 'a')

while True:
  opcao = input('Digite o nome do cliente ou -1 para encerrar: \n')
  if opcao == '-1': 
    break
  arquivo.write(opcao + '-')
