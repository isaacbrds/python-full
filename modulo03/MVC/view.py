from controller import PessoaController
from model import Pessoa

while True:
    opcao = input('Digite 1 para cadastrar usuário e 2 para sair: ')
    if opcao == '2':
        print('Saindo!!!!')
        break
    elif opcao == '3':
        
    else:
        nome = input('Digite o nome do usuário: ')
        cpf = input('Digite o cpf do usuário: ')
        idade = input('Digite a idade do usuário: ')
        if PessoaController.cadastrar(nome, idade, cpf):
            print('Pessoa Cadastrada com Sucesso!')
        else:
            print('Digite os dados válidos!!')