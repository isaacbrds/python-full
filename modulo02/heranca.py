class Pessoa:
    def falar(self):
        print('Estou falando!')


class Vendedor(Pessoa):
    
    def vender(self):
        print('Estou vendendo')


class Cliente(Pessoa):
    
    def comprar(self):
        print('Estou comprando!')


cliente = Cliente()
cliente.falar()
cliente.comprar()