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

class DaoEstoque:
  @classmethod
  def salvar(cls, produto: Produtos, quantidade):
    with open('estoque.txt', 'a') as arquivo:
      arquivo.writelines(produto.nome + "|" + produto.preco + "|" + produto.categoria +
      "|" + str(quantidade))
      arquivo.writelines("\n")

  @classmethod
  def ler(cls):
    with open('estoque.txt', 'r') as arquivo:
      cls.estoque = arquivo.readlines()
    
    cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
    cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

    estoque = []

    if len(cls.estoque) > 0:
      for i in cls.estoque:
        estoque.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
      
    return estoque

class DaoFornecedor:
  @classmethod
  def salvar(cls, fornecedor: Fornecedor):
    with open('fornecedor.txt', 'a') as arquivo:
      arquivo.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone
      +"|" + fornecedor.categoria)
      arquivo.writelines("\n")

  @classmethod
  def ler(cls):
    with open('fornecedor.txt', 'r') as arquivo:
      cls.fornecedor = arquivo.readlines()
    
    cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
    cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

    fornecedores = []
    for i in cls.fornecedor:
      fornecedores.append(Fornecedor(i[0], i[1], i[2],i[3]))

    return fornecedores

class DaoPessoa:
  @classmethod
  def salvar(cls,pessoas: Pessoa):
    with open('cliente.txt', 'a') as arquivo:
      arquivo.writelines(pessoas.nome + "|" + pessoas.telefone + "|" + pessoas.cpf
      + "|" + pessoas.email + "|" + pessoas.endereco)
      arquivo.writelines("\n")

  @classmethod
  def ler(cls):
    with open('cliente.txt', 'r') as arquivo:
      cls.clientes = arquivo.readlines()
    
    cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
    cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

    clientes = []
    for i in cls.clientes:
      clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
    
    return clientes