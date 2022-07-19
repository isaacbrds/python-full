from Models import *

class DaoCategoria:

  @classmethod
  def salvar(cls, categoria):
    with open('categoria.txt', 'a') as arquivo:
      try:
        arquivo.write(categoria + '\n')
        
      except:
        return False
    
  @classmethod
  def ler(cls):
    with open('categoria.txt', 'r') as arquivo:
      cls.categoria = arquivo.readlines()

    cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

    categorias = []
    for i in cls.categoria:
      categorias.append(Categoria(i))
    
    return categorias


class DaoVenda:
  @classmethod
  def salvar(cls, venda: Venda):
    with open('venda.txt', 'a') as arquivo:
      arquivo.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.preco + "|" + 
                        venda.itensVendido.categoria + "|" + venda.vendedor + "|" + 
                        venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + venda.data) 
      arquivo.writelines('\n')

  @classmethod
  def ler(cls):
    with open('venda.txt', 'r') as arquivo:
      cls.venda = arquivo.readlines()
    
    cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
    cls.venda = list(map(lambda x: x.split('|'), cls.venda))
    
    vendas = []
    for i in cls.venda:
      vendas.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
    
    return vendas

#produto = Produtos('Maçã', '20', 'Frutas')
#venda = Venda(produto, 'Vendedor', 'Comprador', '10')
#DaoVenda.salvar(venda)
venda = DaoVenda.ler()
print(venda[0].itensVendido.nome)