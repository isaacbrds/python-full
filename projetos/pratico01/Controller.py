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
      else:
        print('A categoria que deseja alterar já existe')
    else: 
      print('A categoria que deseja alterar não existe!')
    
    with open('categoria.txt', 'w') as arquivo:
      for i in categorias:
        arquivo.writelines(i.categoria)
        arquivo.writelines('\n')

