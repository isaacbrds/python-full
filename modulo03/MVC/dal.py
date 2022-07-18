from model import Pessoa
class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('Pessoa.txt', 'a') as arq:
            arq.write(pessoa.nome + "-" + str(pessoa.cpf) + "-" + str(pessoa.idade) + " ")
    
    @classmethod
    def ler(cls):
        linhas = ''
        with open('Pessoa.txt', 'r') as arq:
            linhas = arq.read().split('-')
        return linhas
