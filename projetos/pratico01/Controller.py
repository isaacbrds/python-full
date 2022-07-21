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


estoque = ControllerEstoque()
estoque.cadastrar('Banana', '10', 'Frutas', 10)
estoque.alterar('Banana','Maça' , '15', 'Frutas', 10)
estoque.remover('Maça')
