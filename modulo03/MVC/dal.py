from model import Pessoa
class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('Pessoa.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.cpf) + " " + str(pessoa.idade))
    
    @classmethod
    def ler(cls):
        with open('Pessoa.txt', 'r') as arq:
            linha  = arq.read()
        return linha
