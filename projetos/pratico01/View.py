import Controller
import os.path

def criarArquivos(*args):
  for i in args:
    if not os.path.exists(i):
      with open(i, 'w') as arquivo:
        arquivo.writelines("")

criarArquivos('categoria.txt', 'cliente.txt', 
'estoque.txt', 'funcionario.txt', 'venda.txt')

if __name__ == '__main__':
  while True:
    local = int(input("Digite 1 para acessar (Categorias) \n"
      "Digite 2 para acessar os Produtos mais vendidos \n"
      "Digite 3 para acessar (Estoque) \n"
      "Digite 4 para acessar (Fornecedor) \n"
      "Digite 5 para acessar (Cliente) \n"
      "Digite 6 para acessar (Funcionario) \n"
      "Digite 7 para acessar (Vendas) \n"
      "Digite 8 para Sair do sistema :-)!!! \n"
                ))
    if local == 1:
      categoria = Controller.ControllerCategoria()
      while True:
        decisao = int(input("Digite 1 para cadastrar uma categoria\n"
                      "Digite 2 para alterar uma categoria\n"
                      "Digite 3 para mostrar uma categoria\n"
                      "Digite 4 para remover uma categoria\n"
                      "Digite 5 para voltar ao menu anterior\n"
                      ))
        if decisao == 1:
          categoria_cadastrar = input('Digite um nome para uma categoria\n')
          categoria.cadastrar(categoria_cadastrar)
        elif decisao == 2:
          categoria_buscada = input('Digite a categoria que deseja alterar\n')
          nova_categoria = input('Digite a nova categoria\n')
          categoria.alterar(categoria_buscada, nova_categoria)
        elif decisao == 3:
          categoria_buscada = input('Digite a categoria que deseja obter informação\n')
          categoria.mostrar(categoria_buscada)
        elif decisao == 4:
          categoria_buscada = input('Digite a categoria que deseja remover\n')
          categoria.remover(categoria_buscada)
        else:
          print('Voltando')
          break
    if local == 2:
      vendas = Controller.ControllerVenda()
      vendas.relatorioProdutos()
      
    if local == 3:
      estoque = Controller.ControllerEstoque()
      while True:
        decisao = int(input("Digite 1 para cadastrar um novo produto\n"
                      "Digite 2 para alterar um produto\n"
                      "Digite 3 para mostrar um produto\n"
                      "Digite 4 para remover um produto\n"
                      "Digite 5 para voltar ao menu anterior\n"
                      ))
        if decisao == 1: 
          nome = input('Digite o nome do produto\n')
          preco = input('Digite o preço do produto\n')
          categoria = input('Digite a categoria do produto\n')
          quantidade = input('Digite a quantidade do produto\n')
          estoque.cadastrar(nome, preco, categoria, quantidade)
        elif decisao == 2:
          nomeAlterar =  input('Digite o nome do produto que deseja alterar\n')
          nome = input('Digite o nome do produto\n')
          preco = input('Digite o preço do produto\n')
          categoria = input('Digite a categoria do produto\n')
          quantidade = input('Digite a quantidade do produto\n')
          estoque.alterar(nomeAlterar, nome, preco, categoria, quantidade)
        elif decisao == 3: 
          nome = input('Digite o nome do produto\n')
          estoque.mostrar(nome)
        elif decisao == 4:
          nome = input('Digite o nome do produto\n')
          estoque.remover(nome)
        else:
          print('Voltando')
          break
    if local == 4:
      fornecedor = Controller.ControllerFornecedor()
      while True:
        decisao = int(input("Digite 1 para cadastrar um novo fornecedor\n"
                      "Digite 2 para alterar um fornecedor\n"
                      "Digite 3 para mostrar um fornecedor\n"
                      "Digite 4 para remover um fornecedor\n"
                      "Digite 5 para voltar ao menu anterior\n"
                      ))
        if decisao == 1:
          nome = input('Digite o nome do fornecedor\n')
          cnpj = input('Digite o cnpj do fornecedor\n')
          telefone = input('Digite o telefone do fornecedor\n')
          categoria = input('Digite a categoria do fornecedor\n') 
          fornecedor.cadastrar(nome, cnpj, telefone, categoria)
        elif decisao == 2: 
          nomeAlterar =  input('Digite o nome do fornecedor que deseja alterar\n')
          nome = input('Digite o nome do fornecedor\n')
          cnpj = input('Digite o cnpj do fornecedor\n')
          telefone = input('Digite o telefone do fornecedor\n')
          categoria = input('Digite a categoria do fornecedor\n') 
          fornecedor.alterar(nomeAlterar, nome, cnpj, telefone, categoria)
        elif decisao == 3: 
          nome = input('Digite o nome do fornecedor\n')
          fornecedor.mostrar(nome)
        elif decisao == 4:
          nome = input('Digite o nome do fornecedor\n')
          fornecedor.remover(nome)
        else:
          print('Voltando')
          break
    if local == 5:
      cliente = Controller.ControllerCliente()
      while True:
        decisao = int(input("Digite 1 para cadastrar um novo cliente\n"
                      "Digite 2 para alterar um cliente\n"
                      "Digite 3 para mostrar um cliente\n"
                      "Digite 4 para remover um cliente\n"
                      "Digite 5 para voltar ao menu anterior\n"
                      ))
        if decisao == 1: 
          nome = input('Digite o nome do cliente\n')
          cpf = input('Digite o cpf do cliente\n')
          telefone = input('Digite o telefone do cliente\n')
          email = input('Digite o email do cliente\n') 
          endereco = input('Digite o endereço do cliente\n') 
          cliente.cadastrar(nome, telefone, cpf, email, endereco)
        elif decisao == 2: 
          nomeAlterar =  input('Digite o nome do cliente que deseja alterar\n')
          nome = input('Digite o nome do cliente\n')
          cpf = input('Digite o cpf do cliente\n')
          telefone = input('Digite o telefone do cliente\n')
          email = input('Digite o email do cliente\n') 
          endereco = input('Digite o endereço do cliente\n') 
          cliente.alterar(nomeAlterar, nome, telefone, cpf, email, endereco)
        elif decisao == 3: 
          nome = input('Digite o nome do cliente\n')
          cliente.mostrar(nome)
        elif decisao == 4:
          nome = input('Digite o nome do cliente\n')
          cliente.remover(nome)
        else:
          print('Voltando')
          break
    if local == 6:
      funcionario = Controller.ControllerFuncionario()
      while True:
        decisao = int(input("Digite 1 para cadastrar um novo funcionario\n"
                      "Digite 2 para alterar um funcionario\n"
                      "Digite 3 para mostrar um funcionario\n"
                      "Digite 4 para remover um funcionario\n"
                      "Digite 5 para voltar ao menu anterior\n"
                      ))
        if decisao == 1: 
          nome = input('Digite o nome do funcionário\n')
          cpf = input('Digite o cpf do funcionário\n')
          telefone = input('Digite o telefone do funcionário\n')
          email = input('Digite o email do funcionário\n') 
          endereco = input('Digite o endereço do funcionário\n')
          clt = input('Digite o clt do funcionário\n') 
          funcionario.cadastrar(clt, nome, telefone, cpf, email, endereco)
        elif decisao == 2: 
          nomeAlterar =  input('Digite o nome do funcionário que deseja alterar\n')
          nome = input('Digite o nome do funcionário\n')
          cpf = input('Digite o cpf do funcionário\n')
          telefone = input('Digite o telefone do funcionário\n')
          email = input('Digite o email do funcionário\n') 
          endereco = input('Digite o endereço do funcionário\n')
          clt = input('Digite o clt do funcionário\n') 
          funcionario.alterar(nomeAlterar, clt, nome, telefone, cpf, email, endereco)
        elif decisao == 3: 
          nome = input('Digite o nome do funcionário\n')
          funcionario.mostrar(nome)
        elif decisao == 4:
          nome = input('Digite o nome do funcionário\n')
          funcionario.remover(nome)
        else:
          print('Voltando')
          break
    if local == 7:
      vendas = Controller.ControllerVenda()
      while True:
        decisao = int(input("Digite 1 para cadastrar um novo vendas\n"
                      "Digite 2 para alterar um vendas\n"
                      "Digite 3 para mostrar um vendas\n"
                      "Digite 4 para remover um vendas\n"
                      "Digite 5 para voltar ao menu anterior\n"
                      ))
        if decisao == 1:
          nome = input('Digite o nome do produto\n')
          comprador = input('Digite o comprador do produto\n')
          vendedor = input('Digite o nome do vendedor do produto\n')
          quantidade = input('Digite a quantidade vendida do produto\n')
          vendas.cadastrar(nome, vendedor, comprador, quantidade)
        elif decisao == 2: 
          nome = input('Digite o nome do produto\n')
          dataInicio = input('Digite o data de inicio da consulta\n')
          dataFim = input('Digite o data final da consulta\n')
          vendas.mostrar(nome, dataInicio, dataFim)
        else:
          print('Voltando')
          break
    if local == 8:
      print('Tenha um bom dia!!!')
      break