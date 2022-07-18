from controller import PessoaController

while True:
    opcao = int(input('Digite 1 para cadastrar usuario , 2  para ver informação cadastrada e 3 para sair: '))
    if opcao == 3:
        print('Saindo!!!!')
        break
    elif opcao == 2:
        print(f'{PessoaController.ler()}')
    else:
        nome = input('Digite o nome do usuario: ')
        cpf = input('Digite o cpf do usuario: ')
        idade = int(input('Digite a idade do usuario: '))
        if PessoaController.cadastrar(nome, idade, cpf):
            print('Pessoa Cadastrada com Sucesso!')
        else:
            print('Digite os dados válidos!!')