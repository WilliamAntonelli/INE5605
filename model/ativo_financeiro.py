from model.investimento import Investimento
from util.enums import ClasseAtivo, TipoAtivo


class AtivoFinanceiro:
    def __init__(self, classe, tipo, nome):
        self.__classe = classe
        self.__tipo = tipo
        self.__nome = nome


    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, classe):

        if isinstance(classe, ClasseAtivo):
            self.__classe = classe
        else:
            raise Exception("Classe do Ativo inválido, coloque uma classe válida")

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):

        if isinstance(tipo, TipoAtivo):
            self.__tipo = tipo
        else:
            raise Exception("Tipo do Ativo inválido, coloque um tipo válido")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
