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
    cateogira_lida = DaoCategoria.ler()
    categoria_filtrada = list(filter(lambda x: x.categoria == novaCategoria, cateogira_lida))
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

# estoque = ControllerEstoque()
# estoque.cadastrar('Pera', '5', 'Frutas', 50)

venda = ControllerVenda()
#venda.cadastrar('Pera', 'Vendedor', 'Comprador', 10)
venda.relatorioProdutos()