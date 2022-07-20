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

categoria = ControllerCategoria()
categoria.remover('Frios')

