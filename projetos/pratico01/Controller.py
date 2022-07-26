from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
  def cadastrar(self, novaCategoria):
    existe = False
    categorias = DaoCategoria.ler()
    for i in categorias:
      if i.categoria == novaCategoria:
        existe = True
    
    if not existe:
      DaoCategoria.salvar(novaCategoria)
      print(f'Categoria {novaCategoria} com sucesso!')
    else:
      print('A categoria que deseja cadastrar já existe!')

  def remover(self, categoriaRemover):
    categorias = DaoCategoria.ler()
    categoria = list(filter(lambda x: x.categoria == categoriaRemover, categorias))
    if len(categoria) < 0:
      print('A categoria que deseja remover não existe!')
    else:
      for i in range(len(categorias)):
        if categorias[i].categoria == categoriaRemover:
          del categorias[i]
          break
      
      print('Categoria removida com sucesso!')
      #TODO: remover categoria no estoque
      with open('categoria.txt', 'w') as arquivo:
        for i in categorias:
          arquivo.writelines(i.categoria)
          arquivo.writelines('\n')
    
    estoque = DaoEstoque.ler()

    estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem Categoria'), x.quantidade) if x.produto.categoria == categoriaRemover else x, estoque ))
    
    with open('estoque.txt', 'w') as arquivo:
      for i in estoque:
        arquivo.writelines(i.produto.nome + "|" + i.produto.preco + "|" 
        + i.produto.categoria + "|" + str(i.quantidade))
        arquivo.writelines("\n")
    

  def alterar(self,categoriaAlterar, categoriaAlterada):
    categorias = DaoCategoria.ler()
    categoria_a = list(filter(lambda x: x.categoria == categoriaAlterar, categorias))

    if len(categoria_a) > 0:
      categoria_nao_existe = list(filter(lambda x: x.categoria == categoriaAlterada, categorias))
      if len(categoria_nao_existe) == 0:
        categorias = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), categorias))
        #TODO: alterar categoria no estoque
        print('A alteração foi realizada com sucesso!')
      else:
        print('A categoria que deseja alterar já existe')
    else: 
      print('A categoria que deseja alterar não existe!')
      return None
    
    with open('categoria.txt', 'w') as arquivo:
      for i in categorias:
        arquivo.writelines(i.categoria)
        arquivo.writelines('\n')

  def mostrar(self, categoria):
    categorias = DaoCategoria.ler()

    categoria = list(filter(lambda x: x.categoria == categoria, categorias))

    if len(categoria) > 0:
      for i in categoria:
        print(i.categoria)
    else:
      print('Categoria não encontrada!')

class ControllerEstoque:
  def cadastrar(self, nome, preco, categoria, quantidade):
    estoque_lido = DaoEstoque.ler()
    categoria_lida = DaoCategoria.ler()

    categoria_filtrada = list(filter(lambda x: x.categoria == categoria, categoria_lida))
    estoque = list(filter(lambda x: x.produto.nome == nome, estoque_lido))

    if len(categoria_filtrada) > 0:
      if len(estoque) == 0:
        produto = Produtos(nome, preco, categoria)
        DaoEstoque.salvar(produto, quantidade)
        print('Produto cadastrado com sucesso!')
      else:
        print('Produto já existe em estoque!')
    else:
        print('Categoria inexistente!')

  def remover(self, nome):
    estoque_lido = DaoEstoque.ler()
    estoque_filtrado = list(filter(lambda x: x.produto.nome == nome, estoque_lido))
    if len(estoque_filtrado) > 0:
      for i in range(len(estoque_lido)):
        if estoque_lido[i].produto.nome == nome:
          del(estoque_lido[i])
          break

      print('Produto removido com sucesso!')
    else:
      print('Esse produto não existe em estoque')
    
    with open('estoque.txt', 'w') as arquivo:
      for i in estoque_lido:
        arquivo.writelines(i.produto.nome + "|" + i.produto.preco 
        + "|" + i.produto.categoria + "|" + str(i.quantidade))
        arquivo.writelines("\n")

  def alterar(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
    estoque_lido = DaoEstoque.ler()  
    categoria_lida = DaoCategoria.ler()
    categoria_filtrada = list(filter(lambda x: x.categoria == novaCategoria, categoria_lida))
    if(len(categoria_filtrada)) > 0:
      estoque_filtrado = list(filter(lambda x: x.produto.nome == nomeAlterar, estoque_lido))
      if len(estoque_filtrado) > 0:
        estoque_filtrado = list(filter(lambda x: x.produto.nome == novoNome, estoque_lido))
        if len(estoque_filtrado) == 0:
          estoque_lido = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria) ,novaQuantidade) if(x.produto.nome == nomeAlterar) else (x), estoque_lido ))
          print('Produto alterado com sucesso!')
        else:
          print('Produto já cadastrado!')
      else:
        print('O produto que deseja alterar não existe!')
        return None

      with open('estoque.txt', 'w') as arquivo:
        for i in estoque_lido:
          arquivo.writelines(i.produto.nome + "|" + i.produto.preco 
          + "|" + i.produto.categoria + "|" + str(i.quantidade))
          arquivo.writelines("\n")
    else:
      print('Categoria informada não existe!')

  def mostrar(self, nome):
    estoque_lido = DaoEstoque.ler()

    estoque_filtrado = list(filter(lambda x: x.produto.nome == nome, estoque_lido))

    if len(estoque_filtrado) > 0:
      for i in estoque_lido:
        print(i.produto.nome + "|" + i.produto.preco)
    else:
      print('Produto não encontrada!')

class ControllerVenda:
  def cadastrar(self, nomeProduto, vendedor, comprador, quantidadeVendida):
    estoque_lido = DaoEstoque.ler()
    temporaria = []
    existe_produto = False
    tem_em_estoque = False

    for i in estoque_lido:
      if existe_produto == False:
        if i.produto.nome == nomeProduto:
          existe_produto = True
          if int(i.quantidade) >= quantidadeVendida:
            tem_em_estoque = True
            i.quantidade = int(i.quantidade) - int(quantidadeVendida)

            vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

            valor_da_compra = int(quantidadeVendida) * int(i.produto.preco) 

            DaoVenda.salvar(vendido)
      
      temporaria.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
    
    arquivo = open('estoque.txt', 'w')
    arquivo.write("")

    for i in temporaria:
      with open('estoque.txt','a') as arquivo:
        arquivo.writelines(i.produto.nome + "|" + i.produto.preco + "|" 
        + i.produto.categoria + "|" + str(i.quantidade))
        arquivo.writelines("\n")

    if existe_produto == False:
      print('Produto não existe!')
      return None
    elif not tem_em_estoque:
      print("O produto solicitado não possui essa quantidade em estoque!")
    else:
      print("Venda cadastrada com sucesso!")
      return valor_da_compra

  def relatorioProdutos(self):
    vendas = DaoVenda.ler()
    produtos = []
    for i in vendas:
      nome = i.itensVendido.nome
      quantidade = i.quantidadeVendida
      tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
      if len(tamanho) > 0:
        produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
        if(x['produto'] == nome) else(x), produtos))
      else:
        produtos.append({'produto': nome, 'quantidade': int(quantidade)})

    
    ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
      
    print('Esses são os produtos mais vendidos')
    
    a = 1
    for i in ordenado:
      print(f'================ Produto[{a}] ===============')
      print(f"Produto: {i['produto']}\n" f"Quantidade: {i['quantidade']}\n")

      a += 1

  def mostrar(self, dataInicio, dataFim):
    vendas = DaoVenda.ler()
    dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
    dataTermino = datetime.strptime(dataFim, '%d/%m/%Y')

    vendaSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 
                                    and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino, vendas))
    contador = 1
    total  = 0 
    for i in vendaSelecionadas:
      print(f'============= Venda[{contador}]============')
      print(f'Nome: {i.itensVendido.nome}\n'
            f'Categoria: {i.itensVendido.categoria}\n'
            f'Data: {i.data}\n'
            f'Quantidade: {i.quantidadeVendida}\n'
            f'Cliente: {i.comprador}\n'
            f'Vendedor: {i.vendedor}')
      total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
      contador += 1
    
    print(f"Total vendido: {total}")

class ControllerFornecedor:
  def cadastrar(self, nome, cnpj, telefone, categoria):
    fornecedor = DaoFornecedor.ler()
    listaCnpj = list(filter(lambda x: x.cnpj == cnpj, fornecedor))
    listaTelfone = list(filter(lambda x: x.telefone == telefone, fornecedor))
    
    if len(listaCnpj) > 0:
      print('Cnpj já foi cadastrado!')
    elif len(listaTelfone) > 0:
      print('Telfone já foi cadastrado!')
    else:
      if len(cnpj) == 18 and len(telefone) <= 15 and len(telefone) >= 10:
        DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
        print('Fornecedor cadastrado com sucesso!')
      else:
        print('Digite um cnpj ou telefone válido!')

  def alterar(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
    fornecedor = DaoFornecedor.ler()
    
    fornecedor_filtrado = list(filter(lambda x: x.nome == nomeAlterar, fornecedor))
    if len(fornecedor_filtrado) > 0:
      fornecedor_filtrado = list(filter(lambda x: x.cnpj == novoCnpj, fornecedor))
      if len(fornecedor_filtrado) == 0:
        fornecedor = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if x.nome == nomeAlterar else(x), fornecedor_filtrado))
      else:
        print('CNPJ já existe')
    
    else:
      print('O fornecedor que deseja alterar não existe!')
    
    with open('fornecedor.txt', 'w') as arquivo:
      for i in fornecedor:
        arquivo.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
        arquivo.writelines("\n")
      print('Fornecedor alterado com sucesso!')

  def remover(self, nome):
    fornecedor = DaoFornecedor.ler()

    fornecedor_filtrado = list(filter(lambda x: x.nome == nome, fornecedor))
    if len(fornecedor_filtrado) > 0:
      for i in range(len(fornecedor)):
        if fornecedor[i].nome == nome:
          del fornecedor[i]
          break
    else:
      print('Fornecedor que deseja remover não existe!')
      return None

    with open('fornecedor.txt', 'w') as arquivo:
      for i in fornecedor:
        arquivo.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
        arquivo.writelines("\n")
      print('Fornecedor removido com sucesso!')

  def mostrar(self, nome):
    fornecedor = DaoFornecedor.ler()
    fornecedor_filtrado = list(filter(lambda x: x.nome == nome, fornecedor))
    if len(fornecedor_filtrado) > 0:
      for i in fornecedor_filtrado:
        print(f'============= Fornecedor============')
        print(f'Nome: {i.nome}\n'
            f'Categoria: {i.categoria}\n'
            f'Cnpj: {i.cnpj}\n'
            f'Telefone: {i.telefone}\n'
            )
    else:
      print('Fornecedor não encontrado!')

class ControllerCliente:
  def cadastrar(self, nome, telefone, cpf, email, endereco):
    cliente = DaoPessoa.ler()

    cliente_filtrado = list(filter(lambda x: x.cpf == cpf, cliente))
    if len(cliente_filtrado) > 0:
      print('CPF já existe!')
    else:
      if len(cpf) == 14 and len(telefone) >= 10 and len(telefone) <= 15:
        DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
        print('Cliente salvo com sucesso!')
      else:
        print('Digite um cpf ou cnpj válido')

  def alterar(self, nomeAlterar, novoNome, novoCpf, novoTelefone, novoEmail, novoEndereco):
    cliente = DaoPessoa.ler()

    cliente_filtrado = list(filter(lambda x: x.nome == nomeAlterar, cliente))

    if len(cliente_filtrado) > 0:
      cliente_filtrado = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) 
              if x.nome == nomeAlterar else(x), cliente))
    else:
      print('Cliente não encontrado!')    
      return None          
    
    with open('cliente.txt', 'w') as arquivo:
      for i in cliente_filtrado:
        arquivo.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
        arquivo.writelines("\n")

      print('Cliente alterado com sucesso!')

  def mostrar(self, nome):
    cliente = DaoPessoa.ler()
    cliente_filtrado = list(filter(lambda x: x.nome == nome, cliente))
    if len(cliente_filtrado) == 0:
      print('Cliente não localizado!')
    else:
      for i in cliente_filtrado:
        print(f'============= Cliente ============')
        print(f'Nome: {i.nome}\n'
            f'CPF: {i.cpf}\n'
            f'Email: {i.email}\n'
            f'Telefone: {i.telefone}\n'
            f'Endereço: {i.endereco}\n'
            )

  def remover(self, nome):
    cliente = DaoPessoa.ler()
    cliente_filtrado = list(filter(lambda x: x.nome == nome, cliente))
    if len(cliente_filtrado) > 0:
      for i in range(len(cliente)):
        if cliente_filtrado[i].nome == nome:
          del cliente[i]
          break
    else:
      print('Cliente não encontrado!')
      return None
      
    with open('cliente.txt', 'w') as arquivo:
      for i in cliente:
        arquivo.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + 
       '|' + i.email + "|" + i.endereco) 
        arquivo.writelines("\n")
      
      print('Cliente removido com sucesso!')


class ControllerFuncionario:
  def cadastrar(self, nome, telefone, cpf, email, endereco, clt):
    funcionario = DaoFuncionario.ler()

    funcionario_cpf = list(filter(lambda x: x.cpf == cpf, funcionario))
    funcionario_clt = list(filter(lambda x: x.clt == clt, funcionario))

    if len(funcionario_cpf) > 0:
      print('CPF já existe!')
    elif len(funcionario_clt) > 0:
      print('Funcionário com essa CLT já existe!')
    else:
      if len(cpf) == 14 and len(telefone) >= 10 and len(telefone) <= 15: 
        DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
        print('Funcionário salvo com com sucesso!')
      else:
        print('Digite um cpf ou um telefone válido!')

  def alterar(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco, novaClt):
    funcionario = DaoFuncionario.ler()
    funcionario_filtrado = list(filter(lambda x: x.nome == nomeAlterar, funcionario))
    
    if len(funcionario_filtrado) == 0:
      print('Funcionario não localizado!')
      return None
    else:
      funcionario_filtrado = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone,novoCpf, novoEmail, novoEndereco) 
                if x.nome == nomeAlterar else(x), funcionario))
      
    with open('funcionario.txt', 'w') as arquivo:
      for i in funcionario_filtrado:
        arquivo.writelines(i.clt +"|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
        arquivo.writelines("\n")

      print('Funcionario alterado com sucesso!')

  def mostrar(self, nome):
    funcionario = DaoFuncionario.ler()

    funcionario_filtrado = list(filter(lambda x: x.nome == nome, funcionario))
    
    if len(funcionario_filtrado) == 0:
      print('Funcionário não localizado!')
    else:
      for i in funcionario_filtrado:
        print(f'============= Cliente ============')
        print(f'Nome: {i.nome}\n'
            f'CPF: {i.cpf}\n'
            f'Email: {i.email}\n'
            f'Telefone: {i.telefone}\n'
            f'Endereço: {i.endereco}\n'
            f'CLT: {i.clt}\n'
            )

  def remover(self, nome):
    funcionario = DaoFuncionario.ler()
    funcionario_filtrado = list(filter(lambda x: x.nome == nome, funcionario))
    if len(funcionario_filtrado) > 0:
      for i in range(len(funcionario)):
        if funcionario_filtrado[i].nome == nome:
          del funcionario[i]
          break
    else:
      print('Funcionario não encontrado!')
      return None
      
    with open('funcionario.txt', 'w') as arquivo:
      for i in funcionario:
        arquivo.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + 
       '|' + i.email + "|" + i.endereco + "|" + i.clt) 
        arquivo.writelines("\n")
      
      print('Funcionario removido com sucesso!')


categoria = ControllerCategoria()
categoria.remover("Frutas")