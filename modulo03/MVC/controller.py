from dal import PessoaDal
from model import Pessoa


class PessoaController:
    @classmethod
    def cadastrar(cls, nome, idade, cpf):
        if len(nome) > 8 and (idade > 0 and idade < 150) and len(cpf) == 11:
            try:
                PessoaDal.salvar(Pessoa(nome, cpf,idade))
                return True
            except: 
                return False
        else:
            return False


    @classmethod
    def ler(cls):
        try:
            pessoas = PessoaDal.ler()

        except:
            return False


